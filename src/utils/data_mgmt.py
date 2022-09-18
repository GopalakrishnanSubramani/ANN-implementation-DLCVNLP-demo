import tensorflow as tf

def get_data(validation_datasize):
    mnist = tf.keras.datasets.mnist
    (X_train_full, y_train_full), (X_test, y_test) = mnist.load_data(path="https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-labels-idx1-ubyte.gz")
    X_valid, X_train = X_train_full[:validation_datasize] / 255.0, X_train_full[validation_datasize:] / 255.0
    y_valid, y_train = y_train_full[:validation_datasize], y_train_full[validation_datasize:]
    X_test = X_test / 255.0
    return (X_train, y_train), (X_valid, y_valid), (X_test, y_test)