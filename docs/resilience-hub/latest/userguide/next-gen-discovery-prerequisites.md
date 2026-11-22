

# Prerequisites for dependency discovery

Before you enable dependency discovery, ensure the following requirements are met:
+ Your service must have compute resources that make DNS queries: Amazon Elastic Compute Cloud instances, Amazon Elastic Container Service tasks, Amazon Elastic Kubernetes Service pods, or AWS Lambda functions.
+ Amazon EC2 instances, Amazon ECS tasks, and Amazon EKS pods must be in a VPC that uses Route 53 DNS resolvers. The same applies to Lambda functions connected to a VPC. Lambda functions that aren't connected to a VPC need no setup.
+ Your service must include at least one Amazon Elastic Compute Cloud instance, AWS Lambda function, or VPC resource. Next generation Resilience Hub counts these resources toward the eligible resource count. A Lambda function connected to a VPC counts only in the Regions listed in [Coverage and known limitations](next-gen-discovery-limitations.md). Dependency discovery attributes the queries of some of these functions to their VPC, so also include the VPC in the service. You can verify which resources your service includes by viewing the Service topology in the console.
+ No additional IAM permissions are required beyond the standard invoker role – dependency discovery uses Next generation Resilience Hub's own service credentials to access DNS query data.