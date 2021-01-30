# Bayesian Binary logistic regression in 1d for iris flowers

# Code is based on 
# https://github.com/aloctavodia/BAP/blob/master/code/Chp4/04_Generalizing_linear_models.ipynb

import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import arviz as az
from sklearn.datasets import load_iris

if 0:
    # SAT data from 
    # https://github.com/probml/pmtk3/blob/master/demos/logregSATdemoBayes.m

    X = [525, 533, 545, 582, 581, 576, 572, 609, 559, 543, 576, 525, 574, 582, 574,
         471, 595, 557, 557, 584, 599, 517, 649, 584, 463, 591, 488, 563, 553, 549];

    y = [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1];

    x_n = 'SAT'
    x_0 = np.array(X)
    y_0 = np.array(y)
else:
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Convert to pandas dataframe 
    df_iris = pd.DataFrame(data=iris.data,
                           columns=['sepal_length', 'sepal_width',
                                    'petal_length', 'petal_width'])
    df_iris['species'] = pd.Series(iris.target_names[y], dtype='category')

    df = df_iris.query("species == ('setosa', 'versicolor')")
    y_0 = pd.Categorical(df['species']).codes
    x_n = 'sepal_length'
    x_0 = df[x_n].values

xmean = np.mean(x_0)
x_c = x_0 - xmean

print(x_c)

with pm.Model() as model_0:
    a = pm.Normal('a', mu=0, sd=10)
    b = pm.Normal('b', mu=0, sd=10)

    u = a + pm.math.dot(x_c, b)
    o = pm.Deterministic('o', pm.math.sigmoid(u))
    bd = pm.Deterministic('bd', -a / b)  # decision boundary

    yl = pm.Bernoulli('yl', p=o, observed=y_0)

    trace_0 = pm.sample(1000)

varnames = ['a', 'b', 'bd']
az.summary(trace_0, varnames)

theta = trace_0['o'].mean(axis=0)
idx = np.argsort(x_c)

plt.figure()
# plot logistic curve
plt.plot(x_c[idx], theta[idx], color='C2', lw=3)
az.plot_hpd(x_c, trace_0['o'], color='C2')

# plot decision boundary
plt.vlines(trace_0['bd'].mean(), 0, 1, color='k')
bd_hpd = az.hpd(trace_0['bd'])
plt.fill_betweenx([0, 1], bd_hpd[0], bd_hpd[1], color='k', alpha=0.5)

# plot jittered data
plt.scatter(x_c, np.random.normal(y_0, 0.02),
            marker='.', color=[f'C{x}' for x in y_0])

plt.xlabel(x_n)
plt.ylabel('p(y=1)', rotation=0)
# use original scale for xticks
locs, _ = plt.xticks()
plt.xticks(locs, np.round(locs + xmean, 1))
# plt.xticks(x_c[idx], np.round(x_0[idx], 1))
# plt.savefig('../figures/logreg_bayes_1d_sat.pdf', dpi=300)
plt.tight_layout()
plt.savefig('../figures/logreg_iris_bayes_1d.pdf', dpi=300)
