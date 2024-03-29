import streamlit as st

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load iris dataset
iris = load_iris()
X = iris.data
Y = iris.target

# Train a Random Forest Classifier
rf = RandomForestClassifier()
rf.fit(X, Y)

# Create Streamlit app
st.title("Iris Flower Predictor")
st.header("Enter the values for the flower's features:")

# Input fields for sepal length, sepal width, petal length, and petal width
sepal_length = st.slider("Sepal length", float(X[:,0].min()), float(X[:,0].max()), float(X[:,0].mean()))
sepal_width = st.slider("Sepal width", float(X[:,1].min()), float(X[:,1].max()), float(X[:,1].mean()))
petal_length = st.slider("Petal length", float(X[:,2].min()), float(X[:,2].max()), float(X[:,2].mean()))
petal_width = st.slider("Petal width", float(X[:,3].min()), float(X[:,3].max()), float(X[:,3].mean()))

# Define prediction button
if st.button("Predict"):
    # Use classifier to predict the type of iris flower
    pred = rf.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    flower_type = iris.target_names[pred[0]]
    # Display the predicted type of iris flower
    st.write("The predicted type of iris flower is", flower_type)
