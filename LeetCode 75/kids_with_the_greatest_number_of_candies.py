'''
Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

Ideia: se adicionar os doces da criança com os doces extras, precisa ser maior ou igual
à quantidade de doces da criança que tem mais.

Como cheguei: 1) vi os exemplos e analisei o que dava false ou true;
2) criei loops para iterar cada valor e adicionei os doces extras;
3) adicionei a estrutura de controle de fluxo (if/else) que acrescenta os valores
precisos ao array vazio para a resposta final;
4) corrigi o código para acabar com os erros
'''



class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        for idx, num in enumerate(candies):
            if candies[idx] + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res