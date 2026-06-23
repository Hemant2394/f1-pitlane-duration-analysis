import matplotlib.pyplot as plt
import pandas as pd

circuit = pd.read_csv('circuits.csv')
pit=pd.read_csv('pit_stops.csv')
race=pd.read_csv("races.csv")
race=race.drop(columns=["url"])
circuit=circuit.drop(columns=["url"])

a=pit.merge(race,on="raceId")
merge=a.merge(circuit,on="circuitId")
merge=merge[merge["milliseconds"]<50000]
merge["seconds"]=merge["milliseconds"]/1000

monaco=merge[merge["country"]=="Monaco"]
monza=merge[merge["location"]=="Monza"]
miami=merge[merge["location"]=="Miami"]
las_vegas=merge[merge["location"]=="Las Vegas"]
abu_dhabi=merge[merge["location"]=="Abu Dhabi"]

plt.figure(figsize=(10,7))
plt.hist([monaco["seconds"], monza["seconds"], miami["seconds"], las_vegas["seconds"], abu_dhabi["seconds"]],  label=["Monaco", "Monza", "Miami", "Las Vegas", "Abu Dhabi"],color=['#00F5D4', '#FF5470', '#FEE440', '#0077B6', '#9B5DE5'],bins=50,edgecolor='black',histtype='barstacked',alpha=0.8)
plt.xlabel("Total Pit Lane Time (Seconds)")
plt.ylabel("Number of Pit Stops (Frequency)")
plt.title("F1 Pit Lane Total Duration Distribution by Circuit Location")
plt.legend()
plt.show()
