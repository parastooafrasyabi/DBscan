from pandas import DataFrame
import xlrd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
# Load data : This data is location of venue in Tehran that we get from foursquare API
loc = ("data_checkin_loc.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
x = sheet.col_values(colx=0,start_rowx=1,end_rowx=101)
y = sheet.col_values(colx=1,start_rowx=1,end_rowx=101)
[float(i) for i in x]
[float(i) for i in y]
data = {'x' : x ,
        'y' : y
        }
#  Compute DBSCAN
df = DataFrame(data, columns=['x', 'y'])
clustering = DBSCAN(eps=0.4, min_samples=4).fit(df)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
clusters = clustering.fit_predict(X_scaled)
label_of_points = clustering.labels_
n_clusters_ = len(set(label_of_points)) - (1 if -1 in label_of_points else 0)
n_noise_ = list(label_of_points).count(-1)
print('Lable of points:')
print(label_of_points)
print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)

# Plot result
plt.scatter(x,y, c=clusters, cmap="plasma")
plt.show()