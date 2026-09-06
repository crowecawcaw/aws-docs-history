

# SQL Based Data Processing in Amazon ECS
<a name="sql-data-processing-ecs"></a>

Publication date: **March 8, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to build a configuration-driven, codeless extract-transform-load (ETL) alternative using a containerized ETL framework ([ARC](https://arc.tripl.ai/)) that simplifies and accelerates data processing with Apache Spark. You run the framework on [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) with [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html).

## SQL Based Data Processing in Amazon ECS
<a name="diagram1"></a>

![Architecture diagram showing SQL-based data processing using Amazon Elastic Container Service, AWS Fargate, AWS Lambda, Amazon Simple Storage Service, and Amazon CloudWatch.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/sql-data-processing-ecs/images/sql-data-processing-ecs.png)


The following steps describe the architecture:

1. A user creates an ETL data pipeline based on the ARC framework and SQL scripts in an interactive ARC Jupyter Notebook. The notebook runs on Amazon ECS with AWS Fargate.

1. The notebook and ETL jobs process batch and stream data through AWS PrivateLink. Traffic between ETL processes and data stores does not leave the Amazon network.

1. The ARC Jupyter notebook produces a job flow configuration JSON file. The user uploads the file and SQL scripts to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) through a CI/CD automated deployment process or manually.

1. An Amazon S3 file arrival event triggers an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function.

1. The Lambda function spins up an Amazon ECS task to process batch data in a transient way, or to process stream data continuously in a long-running container. Each job uses isolated compute resources.

1. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) Events schedules and orchestrates regular ARC ETL jobs and Amazon ECS tasks with AWS Fargate or Amazon EC2 launch types.

1. ARC ETL jobs generate application logs for each data processing stage at a granular level. CloudWatch provides monitoring and alerting capabilities.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 8, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.