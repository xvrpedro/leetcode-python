# Merge Strings Alternately (Easy)
# https://leetcode.com/problems/merge-strings-alternately/
#
# Ideia: pegar uma letra de cada palavra, na ordem, até acabarem as duas.
# Se uma palavra for maior, as letras que sobram vão para o final.
#
# Padrão: duas strings percorridas com o mesmo índice.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []  # lista de letras (mais eficiente que somar strings)
        i = 0

        # continua enquanto ainda sobrar letra em alguma das palavras
        while i < len(word1) or i < len(word2):
            if i < len(word1):  # só pega se word1 ainda tem letra nessa posição
                res.append(word1[i])

            if i < len(word2):  # mesma coisa para word2
                res.append(word2[i])

            i += 1

        return "".join(res)  # junta a lista de letras numa string
