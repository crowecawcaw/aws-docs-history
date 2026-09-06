

# Multi-Region GraphQL API with CloudFront
<a name="multi-region-graphql-cloudfront"></a>

Publication date: **April 25, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to reduce latency for end users while increasing your application's availability. You can provide GraphQL API endpoints in multiple AWS Regions with active/active real-time data synchronization supported by [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) global tables.

## Multi-Region GraphQL API with CloudFront
<a name="diagram1"></a>

![Architecture diagram showing a multi-region GraphQL API with CloudFront, Amazon AppSync, DynamoDB global tables, and Lambda.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multi-region-graphql-cloudfront/images/multi-region-graphql-cloudfront.png)


The following steps describe the architecture:

1. Deploy a GraphQL API in two or more AWS Regions using [Amazon AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html), then handle the AppSync commands and queries using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) resolvers connected to a DynamoDB database.

1. To notify clients about data changes across all Regions, enable DynamoDB global tables to keep data in sync across Regions. Handle DynamoDB data streams with a Lambda handler, triggering purposely built GraphQL schema subscriptions.

1. To support custom domains, upload the domain's SSL Certificate into AWS Certificate Manager (ACM) and attach it to an [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) distribution.

1. Point your domain name to CloudFront by using Amazon Route 53 as your DNS name resolution service.

1. Set up a routing rule on Route 53 to route your global clients to the Region with the lowest latency to their location.

1. To authenticate clients seamlessly to AppSync endpoints in any Region, use Lambda@Edge to query Route 53 for the best Region to forward the request to, and to normalize authorization by abstracting the specificities of each Regional AppSync.

1. Clients across the globe can then connect to your GraphQL API on a single endpoint available in edge locations.

1. CloudFront seamlessly routes client requests to the API in the Region with the lowest latency to the client's location.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | April 25, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.