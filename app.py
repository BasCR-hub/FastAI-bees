from fastai.vision import *
import streamlit as st
import pickle
from io import BytesIO
model = load_learner('.')

st.title(" LA question du moment : abeille, bourdon ou guêpe ?")

img = st.file_uploader('Tu sais quoi faire avec cette boite ! Nous n acceptons que les jpg ', type = ['jpg','jpeg'])
if img:
    st.write(img)
    img2 = img.read()
    img3 = open_image(BytesIO(img2))
    pred_class,pred_idx,outputs = model.predict(img3)
    st.write(pred_class.obj)

    # img2 = io.BytesIO(img)
    # img3 = open_image(BytesIO(img))
    # pred_class,pred_idx,outputs = model.predict(img3)
    # st.write(pred_class.obj)
    # with urllib.request.urlopen(url) as f:
	# b = io.BytesIO(f.read())
	# im = Image.open(b)

