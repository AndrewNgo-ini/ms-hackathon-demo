# ms-hackathon-demo

## Create python environment

```
conda create -n ms-hackathon-demo python=3.9
pip install -r requirements.txt 
conda activate ms-hackathon-demo
```

## Setup Environement

Clone .env file

```
cp .env.sample .env
```

Add your environment

```
SERPAPI_API_KEY=
OPENAI_API_KEY=
```

Run chatbot 

```
python chat.py
```