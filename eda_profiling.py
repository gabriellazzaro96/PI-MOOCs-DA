import pandas as pd
import ydata_profiling as ydata

# Creamos los datasets
df1 = pd.read_csv('Datasets/Coursera_courses.csv')
df2 = pd.read_csv('Datasets/edx_courses.csv')
df3 = pd.read_csv('Datasets/udemy_courses.csv')
# df4 = pd.read_pickle('../Data/Raw Data/Coursera_reviews.pkl')

# Realizamos el EDA con la libreria ydata
profile1 = ydata.ProfileReport(df1)
profile2 = ydata.ProfileReport(df2)
profile3 = ydata.ProfileReport(df3)
# profile4 = ydata.ProfileReport(df4)

# Exportamos como HTML
profile1.to_file('Idata_Profiling_html/Coursera_courses.html')
profile2.to_file('Idata_Profiling_html/edx_courses.html')
profile3.to_file('Idata_Profiling_html/udemy_courses.html')
# profile4.to_file('../Web/Routes/Coursera_reviews.html')