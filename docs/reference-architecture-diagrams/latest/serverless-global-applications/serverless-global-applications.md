# Serverless Architecture for Global Applications

Publication date: **October 15, 2020 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture shows how to improve customer experience on your global services by deploying into multiple AWS Regions. You can apply event-driven architectural patterns such as event sourcing, saga orchestration, and CQRS to reduce latency and increase performance.

## Serverless Architecture for Global Applications

![Architecture diagram showing a serverless global application using Amazon API Gateway, AWS Lambda, Amazon DynamoDB, AWS Step Functions, and Amazon EventBridge across multiple Regions.](images/serverless-global-applications.png)

The following steps describe the architecture:

1. Route traffic from edge locations based on the request path using [Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md "../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md"), allowing gradual migration of single-CNAME legacy API operations. Then route requests to the Region with the least latency using [Route 53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md").
2. Front each Region with an entry API using [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md") implementing the CQRS pattern. For query requests, read from the data layer. For synchronous write commands, invoke the logic layer.
3. Process asynchronous commands by adding them to the event bus using [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md"). Source additional events from external systems.
4. Process transactional logic with [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") functions and run long-running tasks with containers on [AWS Fargate](../../../AmazonECS/latest/developerguide/AWS_Fargate.md "../../../AmazonECS/latest/developerguide/AWS_Fargate.md"). Use the Saga pattern to orchestrate distributed transactions with [AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") for eventual consistency.
5. Store data for access patterns using [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md") for key-value stores, Amazon Aurora for relational queries, and [Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") for data lake analytics and AI/ML.
6. Raise logic events from the logic layer to run event-driven workflow steps following the Transformation pattern.
7. Raise data events after changes to the canonical data model on the data layer, reducing redundancy in the logic layer.
8. Propagate changes across Regions with active-active data replication using DynamoDB Global Tables, Amazon S3 Cross-Region Replication, and Amazon Aurora Global Database.
9. For heavy reading scenarios on other Regions, send write requests to primary Regions. For fast global writes, replicate the event and command logic on all Regions.

## Further reading

For additional information, refer to the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date             |
| ------------------- | ----------------------------------------------- | ---------------- |
| Initial publication | Reference architecture diagram first published. | October 15, 2020 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
