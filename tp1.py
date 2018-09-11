import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

#eventos = pd.read_csv('events.csv', low_memory=False)
#print(eventos.info())

"""
trips["date"] = pd.to_datetime(trips.start_date, format = '%m/%d/%Y %H:%M')
trips["month"] = trips["date"].apply(lambda x: x.month)
trips["day"] = trips["date"].apply(lambda x: x.day)
trips["year"] = trips["date"].apply(lambda x: x.year)
trips["DATE"] = pd.to_datetime(trips[['year','month','day']], yearfirst = True)
"""
def preprocesado1(eventos):
	evs = eventos.iloc[:,:8]
	evs = evs.drop(columns=['url'])
	evs['fecha'] = pd.to_datetime(evs.timestamp, format = '%Y-%m-%d %H:%M:%S') 
	evs['dia'] = evs['fecha'].apply(lambda x: x.weekday)	
	evs['mes'] = evs['fecha'].apply(lambda x: x.month)
	evs['anio'] = evs['fecha'].apply(lambda x: x.year)
	evs['cantidad']= 1
	return evs

def eventosPorDiaDeLaSemana(eventos):
#	nuevo = pd.DataFrame({'cantidad': dat.groupby('hermano')['viajes'].sum()}).reset_index()
#	evs = pd.DataFrame({'cantidad': eventos.groupby('dia')['cantidad'].sum()}).reset_index()
#	x = ['lunes','martes','miercoles','jueves','viernes']
#	plt.bar(range(len(x), evs.))
#	plt.xticks(range(len(x)),x)
	eventos.groupby('dia').sum().plot(figsize=(14,4))
	plt.show()

def main():
	eventos = pd.read_csv('events.csv', low_memory=False)
	eventos1 = preprocesado1(eventos)
	#print(eventos1.head(3))
	#print(eventos1.info())
	eventosPorDiaDeLaSemana(eventos1)

main()