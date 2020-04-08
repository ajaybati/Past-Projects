# import matplotlib.pyplot as plt
#
# from sklearn import datasets
# from sklearn import svm
#
# digits = datasets.load_digits()
#
# clf = svm.SVC(gamma=0.001, C=100)
#
# print(len(digits.data))
# x,y = digits.data[:-1], digits.target[:-1]
# clf.fit(x,y)
#
# print('Prediction:',clf.predict([digits.data[-1]]))
#
# plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from matplotlib import style

style.use("ggplot")



X=np.array([[1,2],
            [5,8],
            [1.5,1.8],
            [8,8],
            [1,0.6],
            [9,1]])

Y=[0,1,0,1,0,1]

clf = svm.SVC(kernel = 'linear', C=1.0)

clf.fit(X,Y)

print(clf.predict([[10.58,10.76]]))

w = clf.coef_[0]

a=-w[0] / w[1]

print(w[0],w[1],clf.intercept_)

xx=np.linspace(0,12)

yy= a*xx - clf.intercept_[0] / w[1]

h0= plt.plot(xx, yy, 'k-', label = "non weighted divide")

plt.scatter(X[:,0], X[:,1], c=Y)
plt.legend()
plt.show()
