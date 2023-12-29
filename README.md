Project Title

# pinterest-data-pipeline885

Description:

pinterest-data-pipeline is a project to simulate Pinterest's data pipeline systems using AWS Cloud as a technical exercise. Learning objectives included configuring the EC2 Kafka Client, connecting an MSK cluster to an S3 bucket to ingest data from EC2 Client, configuring an API in API Gateway, mounting and processing batch data using Spark on Databricks for cleaning and finding metrics, orchestrate a Databricks workload on AWS MWAA, send streaming data to Kinesis data streams and then read stream from Databricks leading to transformations using spark streaming before writing the transformed streamed data to Delta Tables on Databricks.


List of technologies used:
    Python (pandas, numpy, re, phonenumbers, dateutil, yaml, sqlalchemy, tabula, requests, boto3)
    PySpark
    AWS EC2
    AWS MSK Connect
    AWS S3
    AWS API Gateway
    AWS MWAA
    AWS Kinesis
    Databricks
    Apache Spark
    Apache Airflow
    Apache Kafka
    GitHub

Installation instructions:

1) Install python3 module in terminal
2) Clone the repo


Usage instructions:

1) Use .pem file and supplied credentials to connect to EC2 terminal using Terminal on MacOS
2) Download and initialize Apache Kafka on the EC2 client machine.
3) Install the IAM MSK authentication package on the EC2 client machine and initialize using the IAM console on your AWS account.
4) Initialize the Kafka client by modifying client.properties file in kafka_folder/bin directory using your own credentials.
5) Create Kafka topics on the EC2 client machine.
6) Install the Confluent-7.2.0 package on the EC2 client machine.
7) Modify the kafka-rest.properties file in the confluent-7.2.0/etc/ directory using your own credentials available in the API Gateway.
8) Start the REST proxy on the EC2 client machine.
9) Run user_posting_emulation.py through the terminal. (Check EC2 bucket to see if data is correctly ingested)
10) Login to Databricks using supplied credentials.
11) Open user-0e8c5a5fa275-notebook to clean data from EC2 and observe metrics using set queries.
12) Open Apache Airflow UI on AWS to configure and set DAG running schedules for the Databricks Notebook
13) Open user-0e8c5a5fa275-notebook-streaming to observe streaming data from Kinesis streams, the transformation and cleaning process before being store into Delta Tables on Databricks.



File structure of the project:


    ├── ...
    └── pinterest-data-pipeline885    # Main folder
        ├── 0e8c5a5fa275-key-pair.pem    # Pem file containing credentials to connect to EC2 Instance
        ├── user_posting_emulation.py      # File containing methods to emulate pinterest posts' data to connected EC2 bucket for batch processing. Calling the file directly will make it loop indefinitely
        ├── user_posting_emulation_streaming.py     # File containing methods to emulate pinterest posts' data to connected Kinesis stream for stream processing. Calling the file directly will make it loop indefinitely
        ├── 0e8c5a5fa275_dag.py   # File containing Airflow DAG data to schedule and automate Databricks runs. Schedule is set to daily     
        ├── LICENSE                  # File containing license information  
        └── README.md                # File containing essential information and instructions




License information:
Copyright 2023 Armand Kushairi.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.