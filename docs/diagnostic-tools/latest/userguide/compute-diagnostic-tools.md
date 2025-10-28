# Tools for managing and optimizing AWS compute infrastructure and applications

The compute tools in the AWS Diagnostic Tools service are used for monitoring, troubleshooting, and
optimizing AWS infrastructure and applications on your AWS accounts.

## Amazon EC2 diagnostic tools

Amazon Elastic Compute Cloud (Amazon EC2) diagnostic tools provide you insights into your Amazon EC2 instances'
performance, status, and resource utilization. You can use these tools to identify and resolve
issues such as high CPU or memory usage, network connectivity problems, instance status checks
failures, and disk space limitations.

**Amazon EC2 tools**

- Amazon EC2 Spot Fleet Requests Lookup
- Amazon EC2 Spot Instance Requests Lookup
- Amazon EC2 Systems Manager
- Amazon EC2 Capacity Reservation

## AWS Lambda diagnostic tools

Lambda diagnostic tools are designed to enhance the visibility and manageability of your AWS Lambda environment, contributing to a more efficient and reliable serverless architecture.

**Lambda tools**

- Lambda Functions Lookup - provides AWS users with a comprehensive overview of all Lambda functions within their AWS account. This tool is designed to streamline management and diagnostic processes by offering a quick snapshot of the Lambda functions on an account.
- Lambda Function Details - provides an in-depth view of individual AWS Lambda functions, presenting a detailed configuration and operational overview. This tool is essential for troubleshooting, configuration verification, and ensuring optimal performance of your Lambda functions.

## Application Load Balancer tools

Application Load Balancer (ALB) diagnostic tools help you monitor and manage your Application Load Balancers, including routing
rules, target group configurations, and listener settings. With these tools, you can diagnose
routing issues, identify misconfigured listeners or target groups, and understand whether your
load balancer settings need to be optimized for improved traffic distribution.

**Application Load Balancer tools**

- Application Load Balancer Target Group Details
- Application Load Balancer Target on Target Groups Lookup
- Application Load Balancer List Listeners

## AWS Elemental Live tools

AWS Elemental Live tools are designed for media processing and streaming workflows. These provide
insights into the health and performance of AWS Elemental MediaLive, helping troubleshoot issues related to
video encoding, streaming latency, packaging, and content delivery.

**AWS Elemental Live tools**

- AWS Elemental MediaLive Lookup

## Benefits for partners

Using these sets of tools, your partners are equipped to handle common compute related
troubleshooting scenarios that may include the following:

- _Performance optimization:_ Identify bottlenecks, resource
  overutilization, or underutilization in Amazon EC2 instances and Lambda functions. Adjust
  resource allocation or configurations for better performance.
- _Error analysis:_ Diagnose errors or failures in Lambda functions,
  Application Load Balancer routing, or event-driven workflows. Investigate error logs and metrics to pinpoint
  the root cause.
- _Scaling challenges:_ Monitor resource scaling in Amazon EC2 instances
  and Lambda functions to ensure they can handle varying workloads effectively. Adjust
  auto-scaling policies as needed.
- _Security and access control:_ Ensure that IAM roles and
  permissions are correctly configured for Lambda functions and other AWS resources. Detect
  and remediate security vulnerabilities.
- _Latency and load balancing:_ Analyze Application Load Balancer metrics to detect
  latency issues or uneven traffic distribution. Adjust target group settings and routing
  rules to optimize load balancing.
- _Media processing and streaming issues:_ Troubleshoot media
  encoding failures, streaming latency, or content delivery problems with MediaLive tools.
  Optimize video encoding settings and CDN configurations.
- _Event-driven workflow debugging:_ Identify issues in event-driven
  architectures using Amazon EventBridge. Check rule configurations, target configurations, and event
  source integrations to ensure events are handled correctly.
