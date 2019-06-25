FROM python
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
CMD scrapy crawl macbook
