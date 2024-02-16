FROM public.ecr.aws/lambda/python:3.11


ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_INDEX_URL=https://pypi.python.org/simple/


# Copy function code
COPY ./app ${LAMBDA_TASK_ROOT}
# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]