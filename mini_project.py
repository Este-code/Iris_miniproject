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

# mean of overall data column-wise
average = np.mean(iris_data, axis=0)
# max of overall data column-wise
maxi = iris_data.max(axis=0)
# minimum of overall data column-wise
mini = iris_data.min(axis=0)
# standard deviation of overall data column-wise
std = np.std(iris_data, axis=0)



# Next, will divide data to get the statistics of singular species

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


# using round to get only one decimal
setosa_statistics = np.vstack([first_row,np.round_(average_setosa, 1),np.round_(maxi_setosa, 1),np.round_(mini_setosa,1),np.round_(std_setosa,1)])
first_column=np.array(['setosa','average','maximum','minimum','standard_deviation'])
first_column.resize(5,1)
setosa_statistics = np.hstack([first_column,setosa_statistics])
setosa_statistics = np.array(setosa_statistics[:,:5])


# VERSICOLOR
# mean of versicolor data column-wise
average_versicolor = np.mean(versicolor, axis=0)
# max of versicolor data column-wise
maxi_versicolor = versicolor.max(axis=0)
# minimum of versicolor data column-wise
mini_versicolor = versicolor.min(axis=0)
# standard deviation of versicolor data column-wise
std_versicolor = np.std(versicolor, axis=0)

versicolor_statistics = np.vstack([first_row,np.round_(average_versicolor, 1),np.round_(maxi_versicolor, 1),np.round_(mini_versicolor,1),np.round_(std_versicolor,1)])
first_column=np.array(['versicolor','average','maximum','minimum','standard_deviation'])
first_column.resize(5,1)
versicolor_statistics = np.hstack([first_column,setosa_statistics])
versicolor_statistics = np.array(versicolor_statistics[:,:5])

# VIRGINICA
# mean of virginica data column-wise
average_virginica = np.mean(virginica, axis=0)
# max of virginica data column-wise
maxi_virginica = virginica.max(axis=0)
# minimum of virginica data column-wise
mini_virginica = virginica.min(axis=0)
# standard deviation of virginica data column-wise
std_virginica = np.std(virginica, axis=0)

virginica_statistics = np.vstack([first_row,np.round_(average_virginica, 1),np.round_(maxi_virginica, 1),np.round_(mini_virginica,1),np.round_(std_virginica,1)])
first_column=np.array(['virginica','average','maximum','minimum','standard_deviation'])
first_column.resize(5,1)
virginica_statistics = np.hstack([first_column,setosa_statistics])
virginica_statistics = np.array(virginica_statistics[:,:5])
