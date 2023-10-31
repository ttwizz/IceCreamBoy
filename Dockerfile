FROM python:3.10
WORKDIR /IceCreamBoy
COPY requirements.txt /IceCreamBoy/
RUN pip install -r requirements.txt
COPY . /IceCreamBoy
CMD python IceCreamBoy.py