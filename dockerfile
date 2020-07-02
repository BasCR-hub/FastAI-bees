FROM paperspace/fastai
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["streamlit run app.py"]