import openpyxl
from openpyxl.styles import PatternFill
from datetime import datetime, timedelta

from Cores import Seletor
import Dicionário

# Enumeração para dias da semana.

# Criar solução excel.
arquivoExcel = openpyxl.Workbook()
arquivoExcel.title = 'Calendário da fusão'

# Criar planilha dentro da solução.
fusãoAtual = arquivoExcel.active
fusãoAtual.title = 'Fusão'

# Fixar a primeira linha.
fusãoAtual.freeze_panes = 'A2'

# Retornar os dias da semana.
dataInicial = '2023-04-02'
dataFinal = '2023-04-14'

diaInicio = datetime.strptime(dataInicial, '%Y-%m-%d')
diaFinal = datetime.strptime(dataFinal, '%Y-%m-%d')
diasQtd = (diaFinal - diaInicio).days

listaData = []
listaDia = []
for acréscimo in range(diasQtd):
    data = diaInicio + timedelta(days = acréscimo)
    dia = Dicionário.diasPtBr[data.weekday()]
    listaData.append(data)
    listaDia.append(dia)

for valor in range(diasQtd):
    fusãoAtual.cell(row = 1, column = valor + 1).value = listaDia[valor]
    fusãoAtual.cell(row = 2, column = valor + 1).value = listaData[valor]
    fusãoAtual.cell(row = 1, column = valor + 1).fill = Seletor.corDias(listaData[valor].weekday())

# Write some data into cells
fusãoAtual['A5'] = 'Exemplo'

# Savar solução.
print('Salvando arquivo...')
arquivoExcel.save('Calendário.xlsx')
print('Calendário salvo em "Calendário.xlsx".')