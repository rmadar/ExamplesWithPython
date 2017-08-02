import pandas            as pd
import numpy             as np
import matplotlib        as mpl
import matplotlib.pyplot as plt


# Tune the matplotlib plot style
#-------------------------------
mpl.rcParams['figure.facecolor'] = 'w'
mpl.rcParams['lines.color']      = 'r'
mpl.rcParams['legend.frameon']   = False
mpl.rcParams['legend.fontsize']  = 'x-large'


# Number of point, indexation per day
#------------------------------------
Npts  = 10000
dates = pd.date_range('20130101', periods=Npts)


# Create data serie with random numbers
#--------------------------------------
df = pd.DataFrame(np.random.randn(Npts,4), index=dates, columns=('Data 1','Data 2','Data 3','Data 4'))


# Add a new row of data 
#----------------------
dataAddon = pd.Series( np.random.randn(Npts), index=pd.date_range('20130105', periods=Npts) ) 
df['Data 5'] = dataAddon


# Replace NAN with 0.0
#---------------------
df = df.replace(np.nan, 0)


# Print the 10 first rows of the data frame and a summary
#--------------------------------------------------------
print '\nInspect 10 first rows:'
print df.head(10)
print '\nPrint out a data frame summary'
print df.describe()


# Plot time evolution and cumulative evolution
#---------------------------------------------
plt.figure(figsize=(15,5.5))
plt.subplot(121)
plt.title('Raw data')
p1 = plt.plot(df)
plt.legend(p1,df.columns)
plt.subplot(122)
plt.title('Cumulative sum')
p2 = plt.plot(df.apply(np.cumsum))
plt.legend(p2,df.columns)
plt.draw()


# Plot correlations (1/3): matrix
#--------------------------------
correlation = df.corr()
fig, ax     = plt.subplots(1,1, figsize=(8,7))
cax         = plt.imshow(correlation,interpolation="nearest")
plt.title('Data Correlation')
ax.set_xticks(range(len(correlation.columns)))
ax.set_xticklabels(correlation.columns,fontsize=8)
ax.set_yticks(range(len(correlation.columns)))
ax.set_yticklabels(correlation.columns,fontsize=8)
plt.colorbar(cax, ticks=np.linspace(-1,1,10) )
plt.draw()


# Plot correlations (2/3): scatter matrix
#----------------------------------------
pd.plotting.scatter_matrix(df, figsize=(12,12), alpha=0.2, color='green', marker='o--', diagonal='hist')
plt.draw()


# Plot correlations (3/3): time auto-correlation
#-----------------------------------------------
df_ac = pd.DataFrame()
for feature in df.columns.tolist():
    data = df[feature].values
    N    = data.size
    mean = np.mean(data)
    var  = np.var(data)
    ac   = [ ( (data[0:N-t]-mean)*(data[t:N]-mean) ).mean() / var for t in range(0,N) ]
    ac   = np.asarray(ac)
    df_ac[feature] = ac

plt.figure(figsize=(15,5.5))
plt.plot(df_ac)
plt.title('Raw data')
plt.legend(df_ac.columns)
plt.draw()


# Show all plots
#---------------
plt.show()
