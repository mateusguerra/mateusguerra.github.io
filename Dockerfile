FROM python:2.7

WORKDIR /tmp

# Add sample application
ADD . .

EXPOSE 8000

# Run it
ENTRYPOINT ["python", "/tmp/application.py"]
