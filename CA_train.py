from typing import overload
import numpy as np
from scipy.sparse import dok_matrix
from sklearn.base import BaseEstimator, ClusterMixin

class CA(BaseEstimator, ClusterMixin):

    NOISE_LABEL = -1

    def __init__(self, Lambda = 50, minCIM = 0.6, init_node_num = 1):
        self.Lambda = Lambda
        self.minCIM = minCIM
        self.init_node_num = init_node_num
        self.num_signal = 0
        self.numNodes = 0
        self._reset_state()

    def _reset_state(self):
        self.weight = []
        self.CountNode = []   # wining times
        self.adaptiveSig = []
        self.labels_ = []

    def fit(self, X):
        """
            　train data in batch manner
             :param X: array-like or ndarray
        """
        self._reset_state()
        for x in X:
            self.input_signal(x)
        self.labels_ = self.__label_samples(X)
        return self

    def fit_predict(self, X, y=None):
        return self.fit(X).labels_

    def input_signal(self, signal:np.ndarray):
        """
             structure of CA train
             Input a signal one by one, and train it.
        """
        signal = self.__check_signal(signal)
        self.num_signal += 1

        if (not self.weight) or (self.num_signal % self.Lambda == 0):
            estSigCA = self.SigmaEstimation(self.DATA, self.num_signal, self.Lambda )
        if self.nodes.shape[0] < self.init_node_num:
            self.__add_node(signal)
            return
        else:
            winner, dists = self.__find_nearest_nodes

            if self.minCIM < dists[0]: #Case 1 V < CIM_k1
                # add Node
                self.__add_node(signal)
                return
            else:
                # update weight of s1 node
                self.__update_winner(winner[0], signal)
                if self.minCIM >= dists[1]:
                    #update weight of s2 node
                    self.__update_winner(winner[1], signal)








        globalCIM = self.CIM(input, weight, mean(adaptiveSig))






