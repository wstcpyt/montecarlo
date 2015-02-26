__author__ = 'yutongpang'
import numpy as np
def simple_pi():

    n_hits = 0
    m_trials = 10000
    counter = 0

    while counter < m_trials:

        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1)
        if x**2 + y**2 <1:
            n_hits+= 1

        counter+=1

    return 4*n_hits/m_trials

def markov_pi():
    n_hits = 0
    m_trials = 20000
    x = 0
    y = 0
    countr = 0
    p = 0.001

    while countr < m_trials:
        dx = np.random.uniform(-p,p)
        dy = np.random.uniform(-p,p)

        if abs(x+dx) <1 and abs(y+dy)<1:
            x = x+dx
            y = y+dy

        if x**2 + y**2 < 1:
            n_hits+=1

        countr+=1
    return 4*n_hits/m_trials


def simple_integrate():
    integral = 0
    m_trials = 10000
    counter = 0
    n=2

    while counter < m_trials:
        x = np.random.uniform(0,1)
        integral += x**n
        counter += 1

    return integral/m_trials