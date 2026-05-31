# Prerequisites for dependency discovery

Before you can enable dependency discovery, ensure the following requirements are met:

- Your service must have compute resources (Amazon Elastic Compute Cloud instances, Amazon Elastic Container Service tasks, Amazon Elastic Kubernetes Service
  pods, or VPC bound Lambda functions) that make DNS queries through Route 53 resolvers.
- The compute resources must reside in a VPC configured to use Route 53 DNS
  resolvers.
- No additional IAM permissions are required beyond the standard invoker role –
  dependency discovery uses Next generation Resilience Hub's own service credentials to access DNS query
  data.
