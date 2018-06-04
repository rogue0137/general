import sys
import wave_dataset
import boston_housing_dataset
import mglearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# TODO : FIX THIS ERROR MESSAGE
# /Users/krystalflores/virtual_environments/venv/machine_learning/lib/python3.6/site-packages/scipy/linalg/basic.py:1226:
# RuntimeWarning: internal gelsd driver lwork query error, required iwork dimension not returned.
# This is likely the result of LAPACK bug 0038, fixed in LAPACK 3.2.2 (released July 21, 2010).
# Falling back to 'gelss' driver.


which_line = (sys.argv[1])

if which_line == "linear models":
    mglearn.plots.plot_linear_regression_wave()

elif "least squares" in which_line:
    if which_line == "wave least squares":
        X, y = wave_dataset.create_wave(60)

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
        lr = LinearRegression().fit(X_train, y_train)

        print("lr.coef_: {}".format(lr.coef_))
        print("lr.intercept_: {}".format(lr.intercept_))
        print("Training set score: {:.2f}".format(lr.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(lr.score(X_test, y_test)))

    elif which_line == "boston housing least squares":
        X, y = boston_housing_dataset.load_boston()

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
        lr = LinearRegression().fit(X_train, y_train)

        print("Training set score: {:.2f}".format(lr.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(lr.score(X_test, y_test)))

    else:
        print("You have not supplied the right argument. \n Values are:")


if plt:
    plt.show()


