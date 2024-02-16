# OrangAI

### Local Setup
* Install Docker & Python 3.11
* Setup Python Virtual Environment
  * python3 -m venv venv
  * source venv/bin/activate
  * pip3 install -r requirements.txt
  * uvicorn app:app --reload
* Api Docs --> http://localhost:8000/docs
* Installing new packages
  * pip3 install <package>
  * pip3 freeze > requirements.txt

### Deploy COMMANDS

* aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 579510303517.dkr.ecr.us-east-1.amazonaws.com
* aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws  
* docker buildx build -t healthcoach .
* docker tag healthcoach:latest 579510303517.dkr.ecr.us-east-1.amazonaws.com/healthcoach:latest
* docker push 579510303517.dkr.ecr.us-east-1.amazonaws.com/healthcoach:latest