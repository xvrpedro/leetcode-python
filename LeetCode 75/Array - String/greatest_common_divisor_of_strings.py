'''
Greatest Common Divisor of Strings (Easy)
https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

Ideia: as duas strings só têm um divisor em comum se forem feitas
mesmo pedaço repetido. Se str1 + str2 for diferente str2 + str1,
logo não existe esse pedaço e a resposta é "".
Se existir, o tamanho dele é o MDC dos tamanhos das duas strings.

Padrão: strings + matemática (MDC).

Como eu cheguei: 1) olhei os exemplos e vi o padrão da repetição;
2) testei combinações que batiam com as respostas; 3) traduzi em código.
'''

import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # O False se dá pela troca de ordem das strings, porque não há divisor comum
        if str1 + str2 != str2 + str1:
            return ""

        # Se passou pra cá, pela lógica, há divisor comum.
        # O maior pedaço comum tem o tamanho do MDC dos comprimentos.
        comprimento_mdc = math.gcd(len(str1), len(str2))
        return str1[0:comprimento_mdc]