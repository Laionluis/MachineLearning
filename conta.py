#Como escolhi k=5 então Teremos que separar os dados em 5 partes mais ou menos iguais
#Ou seja, temos que balancear os dados das 6 classes entre 5 folds. 

import os

def get_filepaths(directory):
    arquivoClasse_0 = open('../Classes/classe_0.txt', 'a')
    arquivoClasse_1 = open('../Classes/classe_1.txt', 'a')
    arquivoClasse_2 = open('../Classes/classe_2.txt', 'a')
    arquivoClasse_3 = open('../Classes/classe_3.txt', 'a')
    arquivoClasse_4 = open('../Classes/classe_4.txt', 'a')
    arquivoClasse_5 = open('../Classes/classe_5.txt', 'a')

    file_paths = []  
    for root, directories, files in os.walk(directory): 
        for filename in files:            
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
            classe = filepath[-5:][0]
            if(classe != 't' and classe != 'a'):
                if classe == '0':
                    arquivoClasse_0.write(filepath + '\n')
                if classe == '1':
                    arquivoClasse_1.write(filepath + '\n')
                if classe == '2':
                    arquivoClasse_2.write(filepath + '\n')
                if classe == '3':
                    arquivoClasse_3.write(filepath + '\n')
                if classe == '4':
                    arquivoClasse_4.write(filepath + '\n')
                if classe == '5':
                    arquivoClasse_5.write(filepath + '\n')            	        	
        
    arquivoClasse_0.close()
    arquivoClasse_1.close()
    arquivoClasse_2.close()
    arquivoClasse_3.close()
    arquivoClasse_4.close()
    arquivoClasse_5.close()

    return file_paths  

full_file_paths = get_filepaths(".")



