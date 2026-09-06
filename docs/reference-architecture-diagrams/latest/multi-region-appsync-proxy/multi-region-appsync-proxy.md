

# Multi-Region Custom-Domain AppSync Proxy API
<a name="multi-region-appsync-proxy"></a>

Publication date: **May 6, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to reduce latency for end users while increasing availability by providing GraphQL API endpoints in multiple AWS Regions. You use [Amazon AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) with active-active real-time data synchronization supported by [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) Global Tables.

## Multi-Region Custom-Domain AppSync Proxy API
<a name="diagram1"></a>

![Architecture diagram showing a multi-Region GraphQL API using Amazon AppSync, Amazon API Gateway, Amazon DynamoDB Global Tables, and Amazon Route 53.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multi-region-appsync-proxy/images/multi-region-appsync-proxy.png)


The following steps describe the architecture:

1. Create one or more DynamoDB database tables in the first AWS Region to store your workload's data. Enable the DynamoDB Global Table feature to propagate data changes bidirectionally in multi-active mode to all other Regions.

1. Create an Amazon AppSync GraphQL API endpoint in each Region in scope, using DynamoDB Global Tables to store and replicate your workload's data.

1. Create an [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) proxy API endpoint in each Region in scope, forwarding all requests to the same Regional AppSync endpoint.

1. Create or import an SSL certificate for your domain to the AWS Certificate Manager (ACM) of each Region. Configure each Regional API Gateway to support HTTPS requests by referencing your domain's SSL certificate.

1. Configure all Regional AppSync endpoints to use a common authorization mechanism using [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) or a common [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) authorizer for seamless client authorization.

1. Configure [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) to forward your domain's requests to the Regional API Gateway endpoint with the lowest latency to the client's location.

1. Clients across the world send requests for commands and queries to the nearest Region.

1. DynamoDB Global Tables automatically replicate data changes to all configured Regions.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | May 6, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.