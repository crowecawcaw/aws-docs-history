

# Multi-Region CQRS for On-Premises Monoliths
<a name="multi-region-cqrs-monoliths"></a>

Publication date: **July 1, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to expand your on-premises transactional monolith to the cloud using the AWS global network. You reduce latency for end users around the world while maintaining transactional isolation, using the Command Query Responsibility Segregation (CQRS) and the read-local write-global architectural patterns.

## Multi-Region CQRS for On-Premises Monoliths
<a name="diagram1"></a>

![Architecture diagram showing multi-Region CQRS using AWS Direct Connect, Amazon Kinesis Data Streams, AWS Lambda, Amazon DynamoDB Global Tables, and Amazon Route 53.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multi-region-cqrs-monoliths/images/multi-region-cqrs-monoliths.png)


The following steps describe the architecture:

1. Deploy an AWS Direct Connect connection between your on-premises installations and the nearest AWS Region to ensure low-latency hybrid connectivity.

1. Set up a change data capture (CDC) stream from your on-premises relational database by attaching AWS Database Migration Service (AWS DMS) to the source database. Stream the events with Amazon Kinesis Data Streams.

1. Handle Kinesis CDC events with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), storing them in denormalized [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) Global Tables.

1. Expose an API to your customers in the Region with Direct Connect (the primary Region), and handle query requests by reading denormalized data in DynamoDB.

1. Handle client command requests by dispatching them to the on-premises monolith service to maintain transactional isolation and atomicity.

1. Expose additional APIs in one or more secondary Regions, serving read requests with data replicated to the local DynamoDB table, and dispatching command requests to the primary Region.

1. Set up [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) monitoring of your Regions in the us-east-1 Region, sending health alarms to [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).

1. Handle health alarms with Lambda, storing the state and location of Regional APIs in a DynamoDB Global Table.

1. Set up circuit breakers on the API dispatchers based on the state of available Regions in DynamoDB.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | July 1, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.