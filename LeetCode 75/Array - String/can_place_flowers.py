'''
Can Place Flowers
https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

Ideia: n = números de flores a serem colocados, se colocar uma flor em um espaço do array, 
não pode haver uma flor nem antes nem depois; 
se for o primeiro espaço, só o próximo não pode haver uma flor; 
se for o último espaço, só o anterior não pode haver uma flor;
para retornar true o n menor ou igual a zero

Como cheguei: 1) procurei padrões que dessem true e false;
2) criei um for iterando todos os espaços;
3) adicionei a estrutura de controle de fluxo (if/else) para se caso o espaço anterior e
o próximo espaço tivesse uma flor;
4) adicionei uma estrutura final de controle de fluxo para caso n for menor ou igual a zero
retornar true, ou caso contrário, retornar false.
5) criei mais um if e um elif para se o idx fosse o primeiro ou o último (sendo uma
lógica diferente)
6) poli o código resolvendo IndexError.
'''



class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for idx, num in enumerate(flowerbed):
            if idx == 0 and num == 0 and (len(flowerbed) == 1 or flowerbed[idx+1] == 0):
                flowerbed[idx] = 1
                n = n - 1

            elif idx == len(flowerbed)-1 and idx > 0 and num == 0 and flowerbed[idx-1] == 0:
                flowerbed[idx] = 1
                n = n - 1

            elif 0 < idx < len(flowerbed) and num == 0 and flowerbed[idx-1] == 0 and flowerbed[idx+1] == 0:
                flowerbed[idx] = 1
                n = n - 1

        if n <= 0:
            return True
        else:
            return False