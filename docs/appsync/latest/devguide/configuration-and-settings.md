# Configuration and settings in AWS AppSync

AWS AppSync enables you to:

- Cache data that's requested often but unlikely to change from request to request.
  This can reduce the load on your resolvers. For more information, see [Configuring server-side caching and API payload compression in AWS AppSync](enabling-caching.md "enabling-caching.md").
- Version GraphQL objects to handle and avoid conflict among multiple clients. For more
  information, see [Versioning, conflict detection, and sync operations for DynamoDB data sources in AWS AppSync](conflict-detection-and-sync.md "conflict-detection-and-sync.md").
- Use custom domain names to configure a single, memorable domain that works for both
  your GraphQL and real-time APIs. For more information, see [Configuring custom domain
  names](custom-domain-name.md "custom-domain-name.md").
- Allow access to your GraphQL APIs through a VPC. For more information, see [Using
  AWS AppSync Private APIs](using-private-apis.md "using-private-apis.md").
- Share your GraphQL APIs through an integration with AWS Resource Access Manager. For more information, see [Sharing your AWS AppSync APIs](sharing-graphql-apis.md "sharing-graphql-apis.md").
- Enable introspection and set query depth and resolver limits per query. For more
  information, see [Configuration
  limits](custom-domain-name.md "custom-domain-name.md").
- Use environment variables to adjust your AWS AppSync resolvers' and functions' behavior
  without updating your code. For more information, see [Using environment variables
  in AWS AppSync](environment-variables.md "environment-variables.md").
  Additionally, AWS AppSync includes the following standard AWS tools for logging, monitoring,
  and tracing:

- [Logging in AWS CloudTrail](cloudtrail-logging.md "cloudtrail-logging.md")
- [Monitoring with Amazon CloudWatch](monitoring.md "monitoring.md")
- [Tracing with AWS X-Ray](x-ray-tracing.md "x-ray-tracing.md")
