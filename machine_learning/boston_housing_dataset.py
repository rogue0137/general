import mglearn
from sklearn.datasets import load_boston


def create_boston():
    boston = load_boston()
    print("Data shape: {}".format(boston.data.shape))

    return boston


def boston_extends():
    X, y = mglearn.datasets.load_extended_boston()
    print("X.shape: {}".format(X.shape))

    return X, y


if __name__ == "__main__":
    create_boston()
    boston_extends()
