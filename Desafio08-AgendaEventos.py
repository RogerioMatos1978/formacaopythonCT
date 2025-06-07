from datetime import datetime, timedelta
from dateutil.rrule import rrule, rruleset, WEEKLY, MONTHLY, FR, MO, TU, WE, TH, SA
from collections import defaultdict

# Data de início (hoje) e data de fim (90 dias depois)
start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
end_date = start_date + timedelta(days=90)

# Regras de recorrência verificar
eventos = {
    "Seminário de Inovação": rrule(freq=WEEKLY, byweekday=MO, dtstart=start_date, until=end_date),
    "Dia de Mentoria": rrule(freq=WEEKLY, byweekday=TU, dtstart=start_date, until=end_date),
    "Workshop de Design": rrule(freq=WEEKLY, byweekday=WE, dtstart=start_date, until=end_date),
    "Hackathon Interno": rrule(freq=WEEKLY, byweekday=TH, dtstart=start_date, until=end_date),
    "Treinamento de Segurança": rrule(freq=WEEKLY, byweekday=FR, dtstart=start_date, until=end_date),
    "Encontro de Clientes": rrule(freq=WEEKLY, interval=2, byweekday=SA, dtstart=start_date, until=end_date),
    "Conferência Regional": rrule(freq=MONTHLY, bymonthday=15, dtstart=start_date, until=end_date),
    "Feira de Carreiras": rrule(freq=MONTHLY, bymonthday=20, dtstart=start_date, until=end_date),
    "Retiro da Equipe": rrule(freq=MONTHLY, byweekday=TH(1), dtstart=start_date, until=end_date),
    "Dia de Voluntariado": rrule(freq=MONTHLY, byweekday=FR(-1), dtstart=start_date, until=end_date),
}

# Construir dicionário de datas com lista de eventos
datas_eventos = defaultdict(list)

for nome, regra in eventos.items():
    for data in regra:
        data_str = data.date().isoformat()
        datas_eventos[data_str].append(nome)

# Filtrar conflitos (duas ou mais ocorrências no mesmo dia)
conflitos = {data: evts for data, evts in datas_eventos.items() if len(evts) > 1}

# Exibir conflitos organizados
if conflitos:
    print("Conflitos de Agenda nos Próximos 90 Dias:\n")
    for data in sorted(conflitos):
        print(f"{data}: {', '.join(conflitos[data])}")
else:
    print("Nenhum conflito de agenda nos próximos 90 dias.")
