import shutil
import re

arquivoClasse_0 = open('./Classes/classe_0.txt', 'r')
arquivoClasse_1 = open('./Classes/classe_1.txt', 'r')
arquivoClasse_2 = open('./Classes/classe_2.txt', 'r')
arquivoClasse_3 = open('./Classes/classe_3.txt', 'r')
arquivoClasse_4 = open('./Classes/classe_4.txt', 'r')
arquivoClasse_5 = open('./Classes/classe_5.txt', 'r')


i = 0
kfold = 1
for line in arquivoClasse_0:
    if i == 600:
        kfold = kfold + 1
        i = 0
    shutil.copy2('../lung_blocks'+r'{}'.format(line).replace('\n',''), './Fold' + str(kfold))
    i = i + 1;


i = 0
kfold = 1
for line in arquivoClasse_1:
    if kfold == 1 or kfold == 2:
        if i == 1146:
            kfold = kfold + 1
            i = 0
    else:
        if i == 1147:
            kfold = kfold + 1
            i = 0

    shutil.copy2('../lung_blocks'+r'{}'.format(line).replace('\n',''), './Fold' + str(kfold))
    i = i + 1;

i = 0
kfold = 1
for line in arquivoClasse_2:
    if kfold == 1 or kfold == 2 or kfold == 3:
        if i == 203:
            kfold = kfold + 1
            i = 0
    else:
        if i == 204:
            kfold = kfold + 1
            i = 0

    shutil.copy2('../lung_blocks'+r'{}'.format(line).replace('\n',''), './Fold' + str(kfold))
    i = i + 1;

i = 0
kfold = 1
for line in arquivoClasse_3:
    if kfold == 1 or kfold == 2 or kfold == 3:
        if i == 388:
            kfold = kfold + 1
            i = 0
    else:
        if i == 389:
            kfold = kfold + 1
            i = 0

    shutil.copy2('../lung_blocks'+r'{}'.format(line).replace('\n',''), './Fold' + str(kfold))
    i = i + 1;

i = 0
kfold = 1
for line in arquivoClasse_4:
    if kfold == 5:
        if i == 558:
            kfold = kfold + 1
            i = 0
    else:
        if i == 557:
            kfold = kfold + 1
            i = 0

    shutil.copy2('../lung_blocks'+r'{}'.format(line).replace('\n',''), './Fold' + str(kfold))
    i = i + 1;

i = 0
kfold = 1
for line in arquivoClasse_5:
    if kfold == 1 or kfold == 2 or kfold == 3:
        if i == 1222:
            kfold = kfold + 1
            i = 0
    else:
        if i == 1223:
            kfold = kfold + 1
            i = 0

    shutil.copy2('../lung_blocks'+r'{}'.format(line).replace('\n',''), './Fold' + str(kfold))
    i = i + 1;

print('pronto')

arquivoClasse_0.close()
arquivoClasse_1.close()
arquivoClasse_2.close()
arquivoClasse_3.close()
arquivoClasse_4.close()
arquivoClasse_5.close()
