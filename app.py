from fastai.vision import *
import streamlit as st
import pickle

model = load_learner('export.pkl')

st.title(" LA question du moment : abeille, bourdon ou guêpe ?")

img = st.file_uploader('Tu sais quoi faire avec cette boite ! Nous n acceptons que les jpg ', type = ['jpg','jpeg'])
if img:
    st.write(img)
    img2 = open_image(BytesIO(img))
    pred_class,pred_idx,outputs = model.predict(img)
    st.write(pred_class.obj)
    