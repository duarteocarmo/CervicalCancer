# CervicalCancer

In collaboration with Konstantinos Kalogeropoulos.

### Purpose:

Patients usually are not familiarized with the importance of routine screening for diseases that canpotentially have a huge effect in their lives. This low problem awareness is often more prominent indeveloping countries, when this fact is combined with the limited resources these countries can offer.Moreover, the choice of the screening method highly depends on the medical personnel’s expertise andpreferences.

Therefore, the prediction of the individual patient’s risk and the best screening strategy during the diagnosis becomes a fundamental problem.

The aim of this project is to attempt to predict the risk of cervical cancer from the attributes provided in the data set, and the best screening test to predict the aforementioned disease.

### Parts:

- Get the first part [here](https://www.dropbox.com/s/inzgff0gtp68q0h/Machine_Learning_Project_1%20%282%29.pdf?dl=0).
- Get the second part here. *(in progress)*
- Get the third part here. *(in progress)*

### Some findings: 

- Hormonal contraceptives and amount of sexual partners, age and age of first sexual intercourse,presence of STDs and presence of CC, are all negatively correlated.
- Four principal components were enough to account for more than 90% of the variance in thedata set. These 4 PCs emphasize variations in age, years of smoking, years of taking hormonalcontraceptives and year of first sexual intercourse, respectively.
- The positive class (has CC) appears to be centralized in the negative class clusters, in almost ofthe plots of the first four PCs against each other.

### Some data visualisation: 

PCA correlations: 

![PCA_MATRIX](https://github.com/duarteocarmo/CervicalCancer/blob/master/Images/PCA_MATRIX.png)

Attribute correlations: 

![Attribute Correlation](https://github.com/duarteocarmo/CervicalCancer/blob/master/Images/Attribute%20Correlation.png)