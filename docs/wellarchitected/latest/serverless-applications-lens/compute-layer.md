# Compute layer

The compute layer of your workload manages requests from external systems, controlling
access and verifying that requests are appropriately authorized. Your business logic will be
deployed and started by the runtime environment that it contains.

[AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") lets you run stateless serverless
applications on a managed platform that supports microservice architectures, deployment, and
management of execution at the function layer.

With [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/"), you can run a fully
managed REST API that integrates with [Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") to
apply your business logic, and includes traffic management, authorization and access control,
monitoring, and API versioning.

[AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/") orchestrates serverless workflows including
coordination, state, and function chaining as well as combining long-running executions not
supported within [Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") execution limits by breaking into multiple steps or by calling workers
running on [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") instances or on-premises.
