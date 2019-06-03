import pandas
url = 'https://raw.githubusercontent.com/mcemim/aulapython/master/tabela3939.csv'
data = pandas.read_csv(url, sep=";", header=4,
                       names=["Nível","Cód.","Regiao","2011","2012","2013","2014","2015","2016","2017"])
print(data)
data.head()

data.tail()