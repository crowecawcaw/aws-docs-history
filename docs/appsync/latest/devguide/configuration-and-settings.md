

# Configuration and settings in AWS AppSync
<a name="configuration-and-settings"></a>

AWS AppSync enables you to:
+ Cache data that's requested often but unlikely to change from request to request. This can reduce the load on your resolvers. For more information, see [Configuring server-side caching and API payload compression in AWS AppSync](enabling-caching.md).
+ Version GraphQL objects to handle and avoid conflict among multiple clients. For more information, see [Versioning, conflict detection, and sync operations for DynamoDB data sources in AWS AppSync](conflict-detection-and-sync.md).
+ Use custom domain names to configure a single, memorable domain that works for both your GraphQL and real-time APIs. For more information, see [Configuring custom domain names](https://docs.aws.amazon.com/appsync/latest/devguide/custom-domain-name.html).
+ Allow access to your GraphQL APIs through a VPC. For more information, see [Using AWS AppSync Private APIs](https://docs.aws.amazon.com/appsync/latest/devguide/using-private-apis.html).
+ Share your GraphQL APIs through an integration with AWS Resource Access Manager. For more information, see [Sharing your AWS AppSync APIs](https://docs.aws.amazon.com/appsync/latest/devguide/sharing-graphql-apis.html).
+ Enable introspection and set query depth and resolver limits per query. For more information, see [Configuration limits](https://docs.aws.amazon.com/appsync/latest/devguide/custom-domain-name.html).
+ Use environment variables to adjust your AWS AppSync resolvers' and functions' behavior without updating your code. For more information, see [Using environment variables in AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/environment-variables.html).

Additionally, AWS AppSync includes the following standard AWS tools for logging, monitoring, and tracing:
+ [Logging in AWS CloudTrail](cloudtrail-logging.md)
+ [Monitoring with Amazon CloudWatch](monitoring.md)
+ [Tracing with AWS X-Ray](x-ray-tracing.md)