import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
inputThing = input("Do you want to see the scatter graph ? (Yes/No) \n")
if(inputThing == 'Yes'):
	fig = px.scatter(mean, x='student_id', y='level', color='attempt', size='attempt')
	fig.show()
elif(inputThing == 'No'):
	print('Ok Bye...')
else:
	print("That's Not A Valid Input")