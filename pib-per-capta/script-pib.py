#
# carregamento de variaveis
#

import pandas as pd

#
# codigo princinpal
# 1. carregar  o arquivo base.xlsx
# 2. exibir linhas do arquivo

print ("inicio do script de pib x percapta")
r = pd.ExcelFile("C:\\devweb\\fatec-tec-2022\\pib-per-capta\\base.xlsx")
print(pd.read_excel(r, "UF_Regiao"))