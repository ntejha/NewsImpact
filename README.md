# NewsImpact

The primary objective as the intial project was not real-time. I am going to retain the idea but the processing and deployment. I am going to document my steps in detail.

## Steps

We are going to branch the existing code,
- creation of branch : `git branch aws-databricks`
- transition to the branch : `git checkout aws-databricks`
- remove all the files in the branch.

### Project setup

#### Project structure

```
news-stock-impact/
├── venv/                    # Python 3.10 virtual environment
├── data/                    # Stores bronze/silver/gold files
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── streaming/               # Kafka producers and consumers
│   ├── producer_news.py
│   └── consumer_news.py
├── airflow/                 # Airflow DAGs and setup (added later)
│   └── dags/
├── dashboard/               # Streamlit dashboard (added later)
│   └── app.py
├── requirements.txt
└── README.md

```
#### Environment setup

As i am doing this project is Fedora. Check the commands accordingly.

- Creation of venv : `python3.10 -m venv venv`
- Activate venv : `source venv/bin/activate`
- Creation of requirements.txt file : `touch requirements.txt`
- Edit the content : `vim requirements.txt`

requirements.txt content : 

```
requests
pandas
textblob
kafka-python
nltk
```

The below command is important because textblob relies on NLTK corpora.
- `python -m textblob.download_corpora`



