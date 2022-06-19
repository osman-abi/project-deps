FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /backend
WORKDIR /backend
COPY . /backend
RUN pip install virtualenvwrapper
RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN /venv/bin/pip install -r requirements.txt