# Data e Hora é um objeto no Python
# importando o metodo do modulo datetime
# import datetime as dt # importando todas as funções da datetime

from datetime import date, datetime, timedelta

hoje = date.today()
agora = datetime.now()
ano_que_vem = hoje  + timedelta(days=365)
daqui_2_horas = agora + timedelta(hours=2)
niver_rogerio = date(2025, 7, 30 )
niver_rogerio_matos = '2025-01-30'
# %d - dia ( 01- 31)
# %m - mes ( 01 - 12)
# %Y - ano (0001 - 9999)
# %H - hora
# %M - minuto
# %S - segundo
niver_rogerio_matos_convertido = datetime.strptime(niver_rogerio_matos, '%Y-%m-%d')
formato_br = datetime.strftime(niver_rogerio_matos_convertido, "%d/%m/%y")

print(hoje)
print(agora)
print(ano_que_vem)
print(daqui_2_horas)
print(type(niver_rogerio))
print(niver_rogerio)
print(type(niver_rogerio_matos))
print(niver_rogerio_matos)
print(niver_rogerio_matos_convertido)
print(type(formato_br))
print(formato_br)

# Tempo inicio - fim Loop For
# inicio = datetime.now()
# for i in range(1, 10_000_000):
#     pass
# fim = datetime.now()
# tempo = fim - inicio
# print(f'Levou o total de {tempo.total_seconds():.2f}')

# Trabalhando com fuso horarios
# from zoneinfo import ZoneInfo
#
# agora_ZoneInfo = datetime.now(ZoneInfo('PDT'))
# print(agora_ZoneInfo)

# Trabalhando com relativedelta


from dateutil.relativedelta import relativedelta
# teste









