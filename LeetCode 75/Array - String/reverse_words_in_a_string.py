'''
Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

Ideia: inverter as palavras e deixar só um espaço entre as palavras.

Como cheguei: 1) criei uma variável com as palavras no tipo de lista usando split (que ignora 
espaços repetidos e os das pontas, pegando só as palavras como strings);
2) inverti as ordens das palavras e entreguei elas com um espaço entre cada
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])