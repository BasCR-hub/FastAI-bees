FROM python:3.7
COPY . /app
WORKDIR /app
EXPOSE 8501
RUN pip install -r requirements.txt
CMD ["/bin/bash"]