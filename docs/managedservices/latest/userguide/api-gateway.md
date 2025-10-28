# Use AMS SSP to provision Amazon API Gateway in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon API Gateway capabilities directly in your AMS managed account. [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md") is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure
APIs at any scale. Using the AWS Management Console you can create REST and WebSocket APIs that act as a front door for applications to access data,
business logic, or functionality from your
back-end services, such as workloads running on Amazon Elastic Compute Cloud
([Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")), code running on
[AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/"), any web application, or real-time communication applications.

API Gateway handles all the tasks involved in accepting and processing up-to hundreds of thousands of concurrent API calls, including traffic management,
authorization and access control, monitoring, and API version management. API Gateway has no minimum fees or startup costs. You pay only for the API calls you
receive and the amount of data transferred out and, with the API Gateway tiered pricing model, you can reduce your cost as your API usage scales.
To learn more, see
[Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/").

## FAQ: API Gateway in AMS

**Q: How do I request access to Amazon API Gateway in my AMS account?**

Request access to API Gateway by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM roles to your account: `customer_apigateway_author_role` and `customer_apigateway_cloudwatch_role`.
After provisioned in your account, you must onboard the roles in your federation solution.

**Q: What are the restrictions to using Amazon API Gateway in my AMS account?**

- API Gateway configuration is limited to resources without
  `AMS-` or `MC-` prefixes to prevent any modifications to AMS infrastructure.
- `CREATE` privileges for VPCLink are disabled in order to prevent unregulated
  creation of Elastic Load Balancers. If VPCLinks are required, see
  [Application Load Balancer | Create](../ctref/deployment-advanced-application-load-balancer-create.md "../ctref/deployment-advanced-application-load-balancer-create.md").

**Q: What are the prerequisites or dependencies to using Amazon API Gateway in my AMS account?**

It depends on the type of API Gateway you want to deploy. It can be a
standalone service, but it can also request access to existing services (for
instance, network load balancer).
