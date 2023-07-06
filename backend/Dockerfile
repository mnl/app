FROM registry.access.redhat.com/ubi9/python-39

COPY hej ./src /opt/app-root

RUN source ../bin/activate && \
	pip3 install -r ../requirements.txt

EXPOSE 5000

USER 1000

CMD ["python3","-u","/opt/app-root/run.py"]
