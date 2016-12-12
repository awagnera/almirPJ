import os
def cls():
    os.system('cls' if os.name=='nt' else ('clear')

#......................................
def mediaNums(qdadNums,nomearquivo ):
              arquivoNums = open(nomearquivo)
              soma=0
            for i in range(qdadNums):
                num=eval(input("Digite um inteiro: "))
                soma+=num
            return soma/qdadnums
          print(mediaNums(4))
             
