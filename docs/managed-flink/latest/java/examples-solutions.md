Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Training workshops, labs, and solution implementations

The following end-to-end examples demonstrate advanced Managed Service for Apache Flink solutions.

###### Topics

- [Deploy, operate, and scale applications with
  Amazon Managed Service for Apache Flink](#examples-MSF-workshop "#examples-MSF-workshop")
- [Develop Apache Flink
  applications locally before deploying to Managed Service for Apache Flink](#examples-getting-started-locally-flink "#examples-getting-started-locally-flink")
- [Use event detection with Managed Service for Apache Flink
  Studio](#examples-event-detection-with-kda "#examples-event-detection-with-kda")
- [Use the AWS Streaming data
  solution for Amazon Kinesis](#examples-streaming-solution "#examples-streaming-solution")
- [Practice using a Clickstream lab with Apache
  Flink and Apache Kafka](#examples-clickstream "#examples-clickstream")
- [Set up custom scaling using Application Auto Scaling](#examples-autoscaling "#examples-autoscaling")
- [View a sample Amazon CloudWatch dashboard](#examples-cwdash "#examples-cwdash")
- [Use templates for AWS Streaming data
  solution for Amazon MSK](#examples-ssmsk "#examples-ssmsk")
- [Explore more Managed Service for Apache Flink solutions on GitHub](#examples-solutions-github "#examples-solutions-github")

## Deploy, operate, and scale applications with

Amazon Managed Service for Apache Flink

This workshop covers the development an Apache Flink application in Java, how to run
and debug in your IDE, and how to package, deploy and run on Amazon Managed Service for Apache Flink. You will also
learn how to scale, monitor, and troubleshoot your application.

[Amazon Managed Service for Apache Flink workshop](https://catalog.workshops.aws/managed-flink/en-US "https://catalog.workshops.aws/managed-flink/en-US").

## Develop Apache Flink

applications locally before deploying to Managed Service for Apache Flink

This workshop demonstrates the basics of getting up and started developing Apache Flink applications locally with the long-term goal of deploying to Managed Service for Apache Flink for Apache Flink.

[Starters Guide to Local Development with Apache Flink](https://catalog.us-east-1.prod.workshops.aws/workshops/429cec9e-3222-4943-82f7-1f45c45ed99a/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/429cec9e-3222-4943-82f7-1f45c45ed99a/en-US")

## Use event detection with Managed Service for Apache Flink

Studio

This workshop describes event detection with Managed Service for Apache Flink Studio and deploying it as a Managed Service for Apache Flink application

[Event Detection with Managed Service for Apache Flink for Apache Flink](https://catalog.us-east-1.prod.workshops.aws/workshops/2b03e299-c30f-4144-b452-483356cc5267/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/2b03e299-c30f-4144-b452-483356cc5267/en-US")

## Use the AWS Streaming data

solution for Amazon Kinesis

The AWS Streaming Data Solution for Amazon Kinesis automatically configures the AWS services necessary
to capture, store, process, and deliver streaming data. The solution provides
multiple options for solving streaming data use cases. The Managed Service for Apache Flink option provides an end-to-end streaming
ETL example demonstrating a real-world application that runs analytical operations on simulated New
York taxi data.

Each solution
includes the following components:

- An AWS CloudFormation package to deploy the complete example.
- A CloudWatch dashboard for displaying application metrics.
- CloudWatch alarms on the most relevant application metrics.
- All necessary IAM roles and policies.

[Streaming Data Solution for Amazon Kinesis](https://aws.amazon.com/solutions/implementations/aws-streaming-data-solution-for-amazon-kinesis/ "https://aws.amazon.com/solutions/implementations/aws-streaming-data-solution-for-amazon-kinesis/")

## Practice using a Clickstream lab with Apache

Flink and Apache Kafka

An end to end lab for clickstream use cases using Amazon Managed Streaming for Apache Kafka for streaming storage and
Managed Service for Apache Flink for Apache Flink applications for stream processing.

[Clickstream
Lab](https://amazonmsk-labs.workshop.aws/en/mskkdaflinklab.html "https://amazonmsk-labs.workshop.aws/en/mskkdaflinklab.html")

## Set up custom scaling using Application Auto Scaling

Two samples that show you how to automatically scale your Managed Service for Apache Flink applications
using Application Auto Scaling. This lets you set up custom scaling policies and custom scaling
attributes.

- [Managed Service for Apache Flink App Autoscaling](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/infrastructure/AutoScaling "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/infrastructure/AutoScaling")
- [Scheduled Scaling](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/infrastructure/ScheduledScaling "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/infrastructure/ScheduledScaling")

For more information on you can perform custom scaling, see [Enable metric-based and scheduled scaling for Amazon Managed Service for Apache Flink](https://aws.amazon.com/blogs/big-data/enable-metric-based-and-scheduled-scaling-for-amazon-managed-service-for-apache-flink/ "https://aws.amazon.com/blogs/big-data/enable-metric-based-and-scheduled-scaling-for-amazon-managed-service-for-apache-flink/").

## View a sample Amazon CloudWatch dashboard

A sample CloudWatch dashboard for monitoring Managed Service for Apache Flink applications. The sample dashboard
also includes a [demo application](https://github.com/aws-samples/kda-metrics-dashboard/tree/main/demo-apps "https://github.com/aws-samples/kda-metrics-dashboard/tree/main/demo-apps") to help with demonstrating the
functionality of the dashboard.

[Managed Service for Apache Flink Metrics
Dashboard](https://github.com/aws-samples/kda-metrics-dashboard "https://github.com/aws-samples/kda-metrics-dashboard")

## Use templates for AWS Streaming data

solution for Amazon MSK

The AWS Streaming Data Solution for Amazon MSK provides AWS CloudFormation templates where data flows through producers,
streaming storage, consumers, and destinations.

[AWS Streaming Data Solution for Amazon MSK](https://aws.amazon.com/solutions/implementations/aws-streaming-data-solution-for-amazon-msk/ "https://aws.amazon.com/solutions/implementations/aws-streaming-data-solution-for-amazon-msk/")

## Explore more Managed Service for Apache Flink solutions on GitHub

The following end-to-end examples demonstrate advanced Managed Service for Apache Flink solutions and are available on GitHub:

- [Amazon Managed Service for Apache Flink Flink – Benchmarking Utility](https://github.com/aws-samples/amazon-kinesis-data-analytics-flink-benchmarking-utility "https://github.com/aws-samples/amazon-kinesis-data-analytics-flink-benchmarking-utility")
- [Snapshot Manager – Amazon Managed Service for Apache Flink for Apache Flink](https://github.com/aws-samples/amazon-kinesis-data-analytics-snapshot-manager-for-flink "https://github.com/aws-samples/amazon-kinesis-data-analytics-snapshot-manager-for-flink")
- [Streaming ETL with Apache Flink and Amazon Managed Service for Apache Flink](https://github.com/aws-samples/amazon-kinesisanalytics-MyApplicatiostreaming-etl "https://github.com/aws-samples/amazon-kinesisanalytics-MyApplicatiostreaming-etl")
- [Real-time sentiment analysis on customer feedback](https://github.com/aws-samples/real-time-sentiment-flinksql-kdastudio "https://github.com/aws-samples/real-time-sentiment-flinksql-kdastudio")
