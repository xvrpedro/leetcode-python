# Two Sum (Easy) - https://leetcode.com/problems/two-sum/
#
# Ideia: preciso achar dois números da lista que somam o alvo.
# Para cada número, guardo "o que falta para chegar no alvo" no dicionário.
# Quando um número novo é igual a algum "falta" guardado, achei o par.
#
# Padrão: dicionário (chave = o que falta, valor = índice de quem precisa dele).

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hasher = {}  # guarda: (alvo - número) -> índice desse número
        for idx, num in enumerate(nums):
            # se o número atual é o que alguém anterior esperava, achei o par
            # ("is not None" porque o índice 0 contaria como falso num "if" simples)
            if hasher.get(num) is not None:
                return [hasher.get(num), idx]
            # senão, guardo o que falta para este número fechar o alvo
            hasher[target-num] = idx
