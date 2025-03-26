# AWS Bedrock POC

## Overview
This is a simple chatbot API using **AWS Bedrock** to generate AI-powered responses.

## Setup Instructions

### 1. Run Locally (Without Docker)

#### Prerequisites:
- Python 3.7+
- AWS credentials configured

#### Steps:
```sh
git clone https://github.com/arpitshah2991996/awsbedrock-poc.git
pip install -r requirements.txt
python app.py
```

### 2. Run with Docker

#### Prerequisites:
- Docker installed

#### Steps:
```sh
git clone https://github.com/arpitshah2991996/awsbedrock-poc.git
docker build -t awsbedrock-poc .
docker run -p 5000:5000 awsbedrock-poc
```

## API Usage
Send a POST request to `/chat`:
```sh
curl -X POST "http://127.0.0.1:5000/chat" -H "Content-Type: application/json" -d '{"query": "What is Generative AI?"}'
```
