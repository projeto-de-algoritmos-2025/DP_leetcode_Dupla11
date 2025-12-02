from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()       # ordenar em ordem crescente para facilitar o DP
        n = len(satisfaction)
        NEG_INF = -10**18         # representa estados impossíveis

        # dp[i][t] = melhor coeficiente like-time usando as primeiras i comidas
        # (índices 0..i-1), preenchendo exatamente t posições de tempo (1..t).
        #
        # Tamanho da tabela: (n+1) × (n+1), pois i e t podem ir até n.
        dp = [[NEG_INF] * (n + 1) for _ in range(n + 1)]

        # Caso base:
        # Preencher 0 posições de tempo -> valor 0, independente de quantas comidas disponíveis
        for i in range(n + 1):
            dp[i][0] = 0

        # Construção bottom-up
        for i in range(1, n + 1):
            # podemos preencher no máximo 'i' posições de tempo, já que só temos i pratos
            for t in range(1, i + 1):

                # Caso 1: não usar o prato (i-1)
                dp[i][t] = max(dp[i][t], dp[i - 1][t])

                # Caso 2: usar o prato (i-1) e colocá-lo na posição de tempo 't'
                # Só é possível se dp[i-1][t-1] não for impossível (NEG_INF)
                if dp[i - 1][t - 1] != NEG_INF:
                    valor = dp[i - 1][t - 1] + satisfaction[i - 1] * t
                    dp[i][t] = max(dp[i][t], valor)

        # A resposta é o melhor valor usando qualquer número de posições de tempo (0..n)
        return max(dp[n])
