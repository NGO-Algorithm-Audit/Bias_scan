import sys
import random
import numpy as np
import pandas as pd
import seaborn as sns   
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def init_GermanCredit_dataset(raw_data, features, with_errors=True, just_features=True, scale_features=True, with_classes=True):
    """ Initializing dataset: scaling features, adding new columns which are required for HBAC """

    new_data = raw_data.copy(deep=True)

    to_scale = new_data.drop(['predicted_class', 'true_class', 'errors'], axis=1).columns
    new_data[to_scale] = StandardScaler().fit_transform(features[to_scale])

    new_data['clusters'] = 0
    new_data['new_clusters'] = -1
    return new_data

def init_dataset(raw_data, features):
    """ Initializing dataset: scaling features, adding new columns which are required for HBAC """

    new_data = raw_data.copy(deep=True)

    to_scale = new_data.drop(['text','predicted_class', 'true_class', 'errors'], axis=1).columns
    new_data[to_scale] = StandardScaler().fit_transform(features[to_scale])
    new_data = new_data.drop(['text'], axis=1)

    new_data['clusters'] = 0
    new_data['new_clusters'] = -1
    return new_data
    
def accuracy(results):
    ''' Accuracy of dataframe '''
    
    correct = results.loc[results['errors'] == 0]
    acc = len(correct)/len(results)
    return acc

def bias_acc(data, cluster_id, cluster_col):
    ''' Negative bias := accuracy of the selected cluster - accuracy of the remaining clusters '''
    cluster_x = data.loc[data[cluster_col] == cluster_id]
    if len(cluster_x) ==0:
        print("This is an empty cluster! cluster ", cluster_id)
    remaining_clusters = data.loc[data[cluster_col] != cluster_id]
    if len(remaining_clusters) == 0:
        print("This cluster is the entire dataset. cluster ", cluster_id)
    return accuracy(cluster_x) - accuracy(remaining_clusters)

def get_max_negative_bias(fulldata, function=bias_acc):
    ''' Calculates the highest negative bias of the newly introduced clusters '''
    max_abs_bias = -999999
    for cluster_number in fulldata['new_clusters'].unique():
        current_bias = (function(fulldata, cluster_number, "new_clusters"))
        if current_bias < max_abs_bias:
            print('current bias: ', current_bias)
            print('max abs bias: ', max_abs_bias)
            max_abs_bias = current_bias
    return max_abs_bias

def get_max_bias_cluster(fulldata, function=bias_acc):
    ''' Identifies cluster linked to the highest negative bias of the newly introduced clusters '''
    max_abs_bias = 100
    best_cluster = -2
    for cluster_number in fulldata['clusters'].unique():
        current_bias = (function(fulldata, cluster_number, "clusters"))
        print(f"{cluster_number} has bias {current_bias}")
        if current_bias < max_abs_bias:
            max_abs_bias = current_bias
            best_cluster = cluster_number
    return best_cluster

def get_min_cluster_size(data):
    ''' Size of smallest new cluster '''
    min_cluster_size = len(data)
    for i in data['new_clusters'].unique():
        # exclude the cluster -1 from being seen as a cluster, since it contains outliers
        if i == -1:
            continue
        size = len(data.loc[data['new_clusters']==i])
        if size < min_cluster_size:
            min_cluster_size = size
    return min_cluster_size

def get_next_cluster(data):
    ''' Identifies cluster number with the highest variance. The variance is calculated based on the errors of each cluster.
    The cluster with the highest variance will be selected as splitting cluster '''
    n_cluster = max(data['clusters'])
    highest_variance = -1
    cluster_number = 0

    for i in data['clusters'].unique():
        if (i == -1):
            continue
        cluster_i = data.loc[data['clusters'] == i]
        variance_cluster = np.var(cluster_i['errors'])
        
        if variance_cluster > highest_variance:
            highest_variance = variance_cluster
            cluster_number = i

    return cluster_number

def calculate_variance(data):
    ''' Determines variance for a dataframe. '''
    variance_list_local = []
    for j in data['clusters'].unique():
        average_accuracy = accuracy(data)
        neg_bias_clus = bias_acc(data, j, 'clusters') 
        variance_list_local.append(neg_bias_clus) 
    variance = np.var(variance_list_local)
    return variance

def get_random_cluster(clusters):
    ''' Identifies value of a random cluster '''
    result = -1
    while (result == -1):
        result = random.randint(0, len(clusters.unique()))
    return result

def pca_plot(data):
    """ PCA dimensionality reduction to display identified clusters as scatterplot. """
    
    pca_features = data.drop(['predicted_class', 'true_class', 'errors', 'clusters', 'new_clusters'], axis=1)
    other_features = data[['predicted_class', 'true_class', 'errors', 'clusters', 'new_clusters']]
    
    df = pd.DataFrame(pca_features)
    pca = pd.DataFrame(PCA(n_components=2).fit_transform(df), index=df.index)
    temp_dataset = pca.join(other_features, how='left')
    temp_dataset.rename( columns={0 :'PCA - 1st'}, inplace=True )
    temp_dataset.rename( columns={1 :'PCA - 2nd'}, inplace=True )

    scatterplot = sns.scatterplot(data=temp_dataset, x='PCA - 1st', y='PCA - 2nd', hue="clusters", size='errors', sizes=(150, 30), palette="Set1")
    scatterplot.set_title('HBAC bias scan (k-means) on AI classifier')
    lgd = scatterplot.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), ncol=1)
    plt.show()
#     plt.savefig('./test.png', bbox_extra_artists=(lgd,), bbox_inches='tight')