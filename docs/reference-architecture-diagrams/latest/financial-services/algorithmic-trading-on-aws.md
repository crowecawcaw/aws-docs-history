

# Algorithmic trading on AWS

Publication date: **December 21, 2020 ([Diagram history](diagram-history.md))**

With this architecture, you can backtest and host machine learning (ML)-based algorithmic trading strategies. The solution uses [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) with [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) for containerized services, [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for model training, and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for transactional data storage.

## Algorithmic trading on AWS diagram
<a name="algotrading-diagram"></a>

![Price data flows through Athena to train a model in SageMaker AI and run trading strategies on Amazon ECS with DynamoDB.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/algorithmic-trading-on-aws.png)


The following steps describe the data flow and trading components for this architecture:

1. Get historical price data from [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/) or external market data sources.

1. Catalog historical price data in [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/) and query data by using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/).

1. Train the ML model for ML-based trading strategies by using SageMaker AI.

1. Run the backtest for your trading strategy as a task through AWS Fargate and Amazon ECS.

1. Run the Market Data Adapter as a service through AWS Fargate and Amazon ECS. Feed data into DynamoDB.

1. Run the Broker Adapter as a service through AWS Fargate and Amazon ECS. Use DynamoDB as the transaction store.

1. Run the Trading Strategy as a service through AWS Fargate and Amazon ECS.

1. Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) for job scheduling with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions. Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) for monitoring.

## Further reading
<a name="algotrading-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 