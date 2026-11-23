'''
Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

Ideia: inverter as posições atuais das vogais presentes na palavra.

Como cheguei: 1) pensei quais maneiras podem inverter as posições das vogais;
2) fiz dois códigos que davam certo porém maiores e melhorei a lógica, surgindo ideias mais sucintas
para realizar;
3) reutilizei as estruturas de repetição (polindo-as) e as váriaveis dos outros códigos para ser mais 
preciso;
4) coloquei as vogais em uma lista separada
5) apliquei .sort(reverse=True) mas me esqueci que isso organiza os itens em ordem decrescente, 
coloquei .reverse e deu certo, invertendo as posições sem comparar os valores;
6) adicionei por fim uma estrutura de repetição que troca as vogais atuais da palavra pelas vogais 
das posições reversas;
7) retornei a palavra com as novas alterações

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowel = []
        i = 0

        for letter in chars:
            if letter in "aeoiuAEIOU":
                vowel.append(letter)
                i += 1
            else:
                pass
        
        i = 0
        vowel.reverse()

        for idx, letter in enumerate(chars):
            if letter in "aeoiuAEIOU":
                chars[idx] = vowel[i]
                i += 1
        
        return "".join(chars)