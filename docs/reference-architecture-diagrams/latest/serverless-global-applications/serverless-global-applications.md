

# Serverless Architecture for Global Applications
<a name="serverless-global-applications"></a>

Publication date: **October 15, 2020 ([Diagram history](#diagram-history))**

This architecture shows how to improve customer experience on your global services by deploying into multiple AWS Regions. You can apply event-driven architectural patterns such as event sourcing, saga orchestration, and CQRS to reduce latency and increase performance.

## Serverless Architecture for Global Applications
<a name="diagram1"></a>

![Architecture diagram showing a serverless global application using Amazon API Gateway, AWS Lambda, Amazon DynamoDB, AWS Step Functions, and Amazon EventBridge across multiple Regions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/serverless-global-applications/images/serverless-global-applications.png)


The following steps describe the architecture:

1. Route traffic from edge locations based on the request path using [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html), allowing gradual migration of single-CNAME legacy API operations. Then route requests to the Region with the least latency using [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html).

1. Front each Region with an entry API using [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) implementing the CQRS pattern. For query requests, read from the data layer. For synchronous write commands, invoke the logic layer.

1. Process asynchronous commands by adding them to the event bus using [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). Source additional events from external systems.

1. Process transactional logic with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions and run long-running tasks with containers on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html). Use the Saga pattern to orchestrate distributed transactions with [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for eventual consistency.

1. Store data for access patterns using [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) for key-value stores, Amazon Aurora for relational queries, and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for data lake analytics and AI/ML.

1. Raise logic events from the logic layer to run event-driven workflow steps following the Transformation pattern.

1. Raise data events after changes to the canonical data model on the data layer, reducing redundancy in the logic layer.

1. Propagate changes across Regions with active-active data replication using DynamoDB Global Tables, Amazon S3 Cross-Region Replication, and Amazon Aurora Global Database.

1. For heavy reading scenarios on other Regions, send write requests to primary Regions. For fast global writes, replicate the event and command logic on all Regions.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | October 15, 2020 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.