Project Title

# pinterest-data-pipeline885

Description:

pinterest-data-pipeline is a project to simulate Pinterest's data pipeline systems using AWS Cloud as a technical exercise. Learning objectives included configuring the EC2 Kafka Client, connecting an MSK cluster to an S3 bucket to ingest data from EC2 Client, configuring an API in API Gateway, mounting and processing batch data using Spark on Databricks for cleaning and finding metrics, orchestrate a Databricks workload on AWS MWAA, send streaming data to Kinesis data streams and then read stream from Databricks leading to transformations using spark streaming before writing the transformed streamed data to Delta Tables on Databricks.


List of technologies used:
    Python (pandas, numpy, re, phonenumbers, dateutil, yaml, sqlalchemy, tabula, requests, boto3)
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
2) Install PostgreSQL (recommended to install via PgAdmin4)
3) Install Jupyter notebook in terminal via conda
4) Clone the repo


Usage instructions:

1) Run all lines of code in main_operations.ipynb sequentially. Do note to change the credentials in the upload_to_db method in database_utils.py with your specific postgres server credentials.
2) Run all files in Milestone 3 folder sequentially to create database schema. 
3) Run all files in Milestone 4 folder for each queries stated in Milestone 4.


File structure of the project:


    ├── ...
    └── multinational-retail-data-centralisation    # Main folder
        ├── data_cleaning.py         # File containing data cleaning methods
        ├── data_extraction.py       # File containing methods for data extraction
        ├── database_utils.py        # File containing methods to connect and manipulate database
        ├── main_operations.ipynb    # Jupyter notebook file containing milestone 2 operations
        ├── Milestone 3          # Folder containing sql files for milestone 3
        │   ├── ms3_Task_1.sql       # SQL file containing query for Task 1 of milestone 3
        │   ├── ms3_Task_2.sql       # SQL file containing query for Task 2 of milestone 3
        │   ├── ms3_Task_3.sql       # SQL file containing query for Task 3 of milestone 3
        │   ├── ms3_Task_4.sql       # SQL file containing query for Task 4 of milestone 3
        │   ├── ms3_Task_5.sql       # SQL file containing query for Task 5 of milestone 3
        │   ├── ms3_Task_6.sql       # SQL file containing query for Task 6 of milestone 3
        │   ├── ms3_Task_7.sql       # SQL file containing query for Task 7 of milestone 3
        │   ├── ms3_Task_8.sql       # SQL file containing query for Task 8 of milestone 3
        │   └── ms3_Task_9.sql       # SQL file containing query for Task 9 of milestone 3
        ├── Milestone 4          # Folder containing sql files for milestone 4
        │   ├── ms4_Task_1.sql       # SQL file containing query for Task 1 of milestone 3
        │   ├── ms4_Task_2.sql       # SQL file containing query for Task 2 of milestone 3
        │   ├── ms4_Task_2.sql       # SQL file containing query for Task 2 of milestone 3
        │   ├── ms4_Task_3.sql       # SQL file containing query for Task 3 of milestone 3
        │   ├── ms4_Task_4.sql       # SQL file containing query for Task 4 of milestone 3
        │   ├── ms4_Task_5.sql       # SQL file containing query for Task 5 of milestone 3
        │   ├── ms4_Task_6.sql       # SQL file containing query for Task 6 of milestone 3
        │   ├── ms4_Task_7.sql       # SQL file containing query for Task 7 of milestone 3
        │   ├── ms4_Task_8.sql       # SQL file containing query for Task 8 of milestone 3
        │   └──  ms4_Task_9.sql      # SQL file containing query for Task 9 of milestone 3
        ├── temp.csv                 # File to contain temporary csv data for operations.
        ├── products.csv             # File that contains product data downloaded from S3      
        ├── LICENSE                  # File containing license information  
        └── README.md                # File containing essential information and instructions




License information:
Copyright 2023 Armand Kushairi.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.