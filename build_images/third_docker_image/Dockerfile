FROM python:3.12

#RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip install --upgrade pip

RUN pip install Faker streamlit pandas redis


# Sets the working directory within the Docker image to /src.
WORKDIR /src

COPY src /src

#CMD ["streamlit", "run", "/src/streamlit.py.py"]