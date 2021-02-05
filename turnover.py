import streamlit as st
import pickle
import pands as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

st.sidebar.title('Estimate Your Employee Turnover')

html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Employee Turnover</h2>
</div><br><br>"""

st.markdown(html_temp,unsafe_allow_html=True)

selection=st.selectbox("Select Your Model", ["GradientBoosting", "KNeighbour", "Random Forest"])

if selection =="GradientBoosting":
    st.write("You selected", selection, "model")
    model= pickle.load(open('gbmod', 'rb'))
elif selection =="KNeighbour":
    st.write("You selected", selection, "model")
    model= pickle.load(open('knnmod', 'rb'))
else:
    st.write("You selected", selection, "model")
    model= pickle.load(open('rfmod', 'rb'))
    
satisfaction=st.sidebar.slider("How well you satisfied with the Company?",0.1,1, step=0.1)x
salary=st.sidebar.selectbox("What is your salary level (low:1, medium:2, high:3)?", (1, 2, 3))
                            
my_dict = {
    "satisfaction": satisfaction,
    "salary": salary
}
                            
columns=["satisfaction_level", "salary"]
                            
df = pd.DataFrame.from_dict([my_dict])

X = df
                            
prediction = model.predict(X)

st.header("The configuration of your car is below")
st.table(df)
st.subheader("Press predict if configuration is okay")
                            
if st.button('Predict'):
    st.success("Turnover estimation of your employee is{}. ".format(int(prediction[0])))
                            
                            