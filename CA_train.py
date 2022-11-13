import numpy as np
from scipy.sparse import dok_matrix
from sklearn.base import BaseEstimator, ClusterMixin

class CA(BaseEstimator, ClusterMixin):

    NOISE_LABEL = -1

    def __init__(self, Lambda = 50, minCIM = 0.6):
        self.Lambda = Lambda
        self.minCIM = minCIM
        self._reset_state()


    def _reset_state(self):
        self.numNodes = 0
        self.weight = []
        self.CountNode = []
        self.adaptiveSig = []
