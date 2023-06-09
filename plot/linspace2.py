import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

if __name__ == '__main__':
    x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), num=100)
    y1 = norm.pdf(x)
    plt.figure('PDF')
    plt.xlim(x.min()-.1,x.max()+0.1)
    plt.ylim(y1.min(),y1.max()+0.01)
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.title('Normal CDF')
    y2 = norm.cdf(x)
    plt.scatter(x, y2, c=x, cmap='jet')
    plt.show()
    plt.close('CDF')
    plt.figure('ICDF')
    plt.xlabel('Probability')
    plt.ylabel('x')
    plt.title('Normal ICDF(PPF)')
    y3 = norm.ppf(x)
    plt.scatter(x, y3, c=x, cmap='jet')
    plt.show()
    plt.close('ICDF')
    
