from copyreg import pickle
from flask import Flask, request
import streamlit as st
import pickle
from sklearn.linear_model import LogisticRegression

pickled_model = open("pickle_wine_model.pkl", "rb")
classifier = pickle.load(pickled_model)

def predict_wine():

    try :
        st.title("Predicting Wine")
        a = st.text_input("Alcohol")
        b= st.text_input("malic_acid")
        c = st.text_input("ash")
        d = st.text_input("alcalinity_of_ash")
        e = st.text_input("magnesium")
        f = st.text_input("total_phenols")
        g = st.text_input("flavanoids")
        h = st.text_input("nonflavanoid_phenols")
        i = st.text_input("proanthocyanins")
        j = st.text_input("color_intensity")
        k = st.text_input("hue")
        l = st.text_input("od280/od315_of_diluted_wines")
        m = st.text_input("proline")
        


        result = classifier.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m ]])
        
        if st.button("Print output"):
            st.success(result)
    except Exception as e :
        return f" Error occuredd with message : {e}"

if __name__=="__main__":
    predict_wine()