# Migrate from AWS Glue Python shell jobs

AWS launched the AWS Glue Python shell jobs in 2018 AWS launched the AWS Glue Python shell jobs in 2018 in order to give customers an easy way to run
Python scripts for small-to-medium sized ETL jobs, and to trigger SQL queries. However, there are now more modern and flexible options to address the
workloads currently running on PythonShell. This topic explains how to migrate your workloads from AWS Glue Python shell jobs to one of these alternative
options in order to take advantage of the newer capabilities that are available.

This topic explains how to migrate from AWS Glue Python shell jobs to alternative options.

## Migrating workload to AWS Glue Spark jobs

[AWS Glue Spark and PySpark jobs](spark_and_pyspark.md "spark_and_pyspark.md") allow you to run your workloads in a
distributed fashion. Since both AWS Glue Python Shell jobs and AWS Glue Spark jobs run on the same platform, it's easy to migrate, and you can continue using
existing AWS Glue features that you're using with Python Shell jobs, such as AWS Glue Workflows, AWS Glue Triggers, AWS Glue's Amazon EventBridge integration, \
 PIP-based package installation, and so on.

However, AWS Glue Spark jobs are designed to run Spark workloads, and the minimum number of workers is 2. If you migrate from Python Shell jobs without
modifying your scripts, only one worker will be actually used, and the other workers will remain idle. This will increase your costs.

To make it efficient, rewrite your Python job script to utilize Spark's capabilities and distribute the workload across multiple workers. If your
Python script is Pandas-based, it's easy to migrate using the New Pandas API on Spark. Learn more about this in
[the AWS Big Data Blog:
Dive deep into AWS Glue 4.0 for Apache Spark](https://aws.amazon.com/blogs/big-data/dive-deep-into-aws-glue-4-0-for-apache-spark/ "https://aws.amazon.com/blogs/big-data/dive-deep-into-aws-glue-4-0-for-apache-spark/").

## Migrating workload to AWS Lambda

AWS Lambda is a serverless computing service that lets you run code without provisioning or managing servers. Because AWS Lambda
has lower startup times and more flexible options for compute capacity, you can benefit from these advantages. For managing extra Python libraries,
AWS Glue Python Shell jobs use PIP-based installation. However, for AWS Lambda, you need to choose one of the following options: a zip archive, a container image,
or Lambda Layers.

On the other hand, AWS Lambda's maximum timeout is 900 seconds (15 minutes). If the job duration of your existing AWS Glue Python Shell job
workload is more than that, or if your workload has a spiky pattern that may cause longer job durations, then we recommend exploring other options
instead of AWS Lambda.

## Migrating workload to Amazon ECS/Fargate

Amazon Elastic Container Service (Amazon ECS) is a fully managed service that simplifies the deployment, management, and scaling of containerized applications. AWS Fargate is a
serverless compute engine for containerized workloads running on Amazon ECS and Amazon Elastic Kubernetes Service (Amazon EKS). There's no maximum timeout on Amazon ECS and Fargate,
so this is a good option for long-running jobs. Since you have full control over your container image, you can bring your Python script and extra
Python libraries into the container and use them. However, you need to containerize your Python script to use this approach.

## Migrating workload to Amazon Managed Workflows for Apache Airflow Python Operator

Amazon Managed Workflows for Apache Airflow (Managed Workflows for Apache Airflow) is a managed orchestration service for Apache Airflow that makes it easier to set up and operate
end-to-end data pipelines in the cloud at scale. If you already have an MWAA environment, it will be straightforward to use the Python operator instead
of AWS Glue Python Shell jobs. The Python operator is an operator that runs Python code inside an Airflow workflow. However, if you don't have an existing
MWAA environment, we recommend exploring other options.

## Migrating workload to Amazon SageMaker AI AI training jobs

Amazon SageMaker AI Training is a fully managed machine learning (ML) service offered by Amazon SageMaker AI that helps you efficiently train
a wide range of ML models at scale. The core of Amazon SageMaker AI AI jobs is the containerization of ML workloads and the capability of managing
AWS compute resources. If you prefer a serverless environment where there is no maximum timeout, Amazon SageMaker AI AI training jobs could be a
good fit for you. However, the startup latency tends to be longer than AWS Glue Python Shell jobs. For jobs that are latency-sensitive, we recommend
exploring other options.
