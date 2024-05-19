import numpy as np
import pickle
import sklearn
import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

model = pickle.load(open('models/model.pkl','rb'))
def main():
    st.title("Anomaly Detection System")
    feature1 = st.text_input('No. of source bytes')
    feature2 = st.text_input('No. of destination bytes')
    feature3 = st.text_input('dst_host_rerror_rate')
    feature4 = st.text_input('dst_host_diff_srv_rate')
    feature5 = st.text_input('dst_host_srv_count')

    if st.button('Submit'):
        prediction = model.predict([[feature1,feature2,feature3,feature4,feature5]])
        output = prediction
        st.success("The predicted class is: {}".format(output[0]))
        print(f"The predicted class is: {output[0]}")


if __name__ == '__main__':
    main()