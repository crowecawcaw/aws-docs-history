# Blocked services for manual

grouping

AWS Resilience Hub blocks you from manually grouping resources of certain AWS services to
prevent configuration errors that could affect the resilience assessment and
recommendations for your application. These services are automatically grouped based
on their dependencies and configurations. When you define an application inclusive
of these resources on AWS Resilience Hub, it analyzes their relationships, dependencies, and
resilience requirements to create optimal groupings that ensure accurate assessment
results.

List of AWS services blocked for manual grouping:

- Amazon API Gateway
- Amazon DocumentDB
- Amazon DynamoDB
- Amazon Elastic Block Store
- Amazon Elastic File System
- Amazon Relational Database Service
- Amazon S3
- Amazon Simple Queue Service
- FSx for Windows File Server
- NAT Gateway
