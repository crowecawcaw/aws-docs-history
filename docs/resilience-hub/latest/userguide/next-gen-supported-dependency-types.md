

# Supported dependency types
<a name="next-gen-supported-dependency-types"></a>

Dependency discovery identifies the following types of dependencies:
+ **AWS service endpoints** – Amazon S3, Amazon DynamoDB, SQS, and other AWS services your application calls.
+ **Internal endpoints** – Services within your VPC or organization.
+ **Third-party endpoints** – External services such as LaunchDarkly, Stripe, or Datadog.
+ **Cross-region calls** – Dependencies that resolve to endpoints in other AWS Regions.

Each discovered dependency is categorized by type:


| Type | Description | Example | 
| --- | --- | --- | 
| AWS service | An AWS service endpoint | Amazon S3, Amazon DynamoDB, SQS | 
| Third-party | A service outside AWS and your organization | LaunchDarkly, Stripe, Datadog | 
| Internal | A service within your organization | Internal microservices, shared APIs | 