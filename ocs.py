# -*- coding: utf-8 -*-
"""ocs

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tKOyZfczRw8Kq1YTHd2k6TJUNdkNS6AH
"""

import numpy as np

def sample_unit_sphere(n):
    vec = np.random.randn(3, n)
    vec = vec / np.linalg.norm(vec, axis=0)
    return vec.T

def compute_ocs(obs_resp, illum, res=100):
    P = sample_unit_sphere(res)
    S = obs_resp.T * illum
    A = P @ S
    R = A >= 0
    Phi = R @ S.T
    return Phi.tolist()
