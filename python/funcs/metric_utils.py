"""
Original Author: Xavier Yang
Link: https://github.com/ivaquero
"""
from os import path

import numpy as np


def multi_guassian_product(mean1, cov1, mean2, cov2):
    cov1 = np.asarray(cov1)
    cov2 = np.asarray(cov2)
    mean1 = np.asarray(mean1)
    mean2 = np.asarray(mean2)

    sum_inv = np.linalg.inv(cov1 + cov2)
    mean = np.dot(cov2, sum_inv).dot(mean1) + np.dot(cov1, sum_inv).dot(mean2)
    cov = np.dot(cov1, sum_inv).dot(cov2)

    return mean, cov
