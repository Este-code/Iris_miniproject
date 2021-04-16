import numpy as np
# Loading the data set
iris_txt = np.loadtxt("iris-head-num.txt", delimiter=',', dtype='object')
# Saving first_row
first_row = np.array(iris_txt[0,:])
# Saving data
iris_data = np.array(iris_txt[1:,:4], dtype=float)
# Saving iris species
# 1 = iris setosa
# 2 = iris versicolor
# 3 = iris virginica
iris_species = np.array(iris_txt[1:,4], dtype=float)

# Array Statistics (Maximum, minimum, mean, standard deviation) of overall species
# will divide data to get the statistics of singular species

# using resize function on iris_species to 2 dimension so that I can horizontally stack(hstack) the array to iris_data
iris_species.resize((150, 1))
all_data=np.hstack([iris_data, iris_species])

temp_setosa = []
temp_versicolor = []
temp_virginica = []
for i in all_data:
    if(i[4]==1):
        temp_setosa.append(i)
    elif(i[4]==2):
        temp_versicolor.append(i)
    else:
        temp_virginica.append(i)

# creating numpy array for each species with their data
setosa=np.array(temp_setosa)
versicolor=np.array(temp_versicolor)
virginica=np.array(temp_virginica)


# Array Statistics for each species
# and creating array with all the statistics for each iris species

# SETOSA
# mean of setosa data column-wise
average_setosa = np.mean(setosa, axis=0)
# max of setosa data column-wise
maxi_setosa = setosa.max(axis=0)
# minimum of setosa data column-wise
mini_setosa = setosa.min(axis=0)
# standard deviation of setosa data column-wise
std_setosa = np.std(setosa, axis=0)

# VERSICOLOR
# mean of versicolor data column-wise
average_versicolor = np.mean(versicolor, axis=0)
# max of versicolor data column-wise
maxi_versicolor = versicolor.max(axis=0)
# minimum of versicolor data column-wise
mini_versicolor = versicolor.min(axis=0)
# standard deviation of versicolor data column-wise
std_versicolor = np.std(versicolor, axis=0)

# VIRGINICA
# mean of virginica data column-wise
average_virginica = np.mean(virginica, axis=0)
# max of virginica data column-wise
maxi_virginica = virginica.max(axis=0)
# minimum of virginica data column-wise
mini_virginica = virginica.min(axis=0)
# standard deviation of virginica data column-wise
std_virginica = np.std(virginica, axis=0)

#Finding outliers of each statistic per species
# Using the formula:
# lower = mean - 2*std
# upper = mean + 2*std
temp_setosa = []
temp_versicolor = []
temp_virginica = []

# SETOSA outliers
rows, cols = setosa.shape
for i in range(0, cols):
    lower = average_setosa[i] - 2*std_setosa[i]
    temp_setosa.append(lower)
for i in range(0, cols):
    upper = average_setosa[i] + 2*std_setosa[i]
    temp_setosa.append(upper)

outliers_setosa=np.array(temp_setosa)
outliers_setosa.resize(2,5)


# VERSICOLOR outliers
rows, cols = versicolor.shape
for i in range(0, cols):
    lower = average_versicolor[i] - 2*std_versicolor[i]
    temp_versicolor.append(lower)
for i in range(0, cols):
    upper = average_versicolor[i] + 2*std_versicolor[i]
    temp_versicolor.append(upper)

outliers_versicolor=np.array(temp_versicolor)
outliers_versicolor.resize(2,5)



# VIRGINICA outliers
rows, cols = virginica.shape
for i in range(0, cols):
    lower = average_virginica[i] - 2*std_virginica[i]
    temp_virginica.append(lower)
for i in range(0, cols):
    upper = average_virginica[i] + 2*std_virginica[i]
    temp_virginica.append(upper)

outliers_virginica=np.array(temp_virginica)
outliers_virginica.resize(2,5)



# EXPORT TO A FILE

# adding lower and upper outliers statistics to first row 
# using round to get only one decimal

# first column is going to be shared between tables
first_column=np.array(['Average','Maximum','Minimum','Standard_d','LowerOutlier','UpperOutlier'])
first_column.resize(6,1)

first_row = np.hstack(['Versicolor',first_row[:4]])
versicolor_statistics = np.vstack([np.round_(average_versicolor, 1),np.round_(maxi_versicolor, 1),np.round_(mini_versicolor,1),np.round_(std_versicolor,1),np.round_(outliers_versicolor,1)])
versicolor_statistics = np.array(versicolor_statistics[:,:4])
versicolor_statistics = np.hstack([first_column,versicolor_statistics])
versicolor_statistics = np.vstack([first_row,versicolor_statistics])

first_row[0] = 'Setosa'
setosa_statistics = np.vstack([np.round_(average_setosa, 1),np.round_(maxi_setosa, 1),np.round_(mini_setosa,1),np.round_(std_setosa,1),np.round_(outliers_setosa,1)])
setosa_statistics = np.array(setosa_statistics[:,:4])
setosa_statistics = np.hstack([first_column,setosa_statistics])
setosa_statistics = np.vstack([first_row,setosa_statistics])

first_row[0] = 'Virginica'
virginica_statistics = np.vstack([np.round_(average_virginica, 1),np.round_(maxi_virginica, 1),np.round_(mini_virginica,1),np.round_(std_virginica,1),np.round_(outliers_virginica,1)])
virginica_statistics = np.array(virginica_statistics[:,:4])
virginica_statistics = np.hstack([first_column,virginica_statistics])
virginica_statistics = np.vstack([first_row,virginica_statistics])


# EXPORT TO FILE

np.savetxt("setosa_statistics.csv", setosa_statistics, delimiter=',', fmt='%s')
np.savetxt("versicolor_statistics.csv", versicolor_statistics, delimiter=',', fmt='%s')
np.savetxt("virginica_statistics.csv", virginica_statistics, delimiter=',', fmt='%s')








