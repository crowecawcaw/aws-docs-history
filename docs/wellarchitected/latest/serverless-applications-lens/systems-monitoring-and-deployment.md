# Systems monitoring and deployment

The system monitoring layer of your workload manages system visibility through metrics
and creates contextual awareness of how it operates and behaves over time. The deployment
layer defines how your workload changes are promoted through a release management process.

With [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"), you can access system metrics on all the
AWS services you use, consolidate system and application level logs, and create business key
performance indicators (KPIs) as custom metrics for your specific needs. It provides
dashboards and alerts that can trigger automated actions on the platform.

[AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/") helps you analyze and debug serverless
applications by providing distributed tracing and service maps to easily identify performance
bottlenecks by visualizing a request end-to-end.

[AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/ "https://aws.amazon.com/serverless/sam/") (AWS SAM) is an
extension of [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") that is used to package, test, and deploy serverless applications. The
[AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/ "https://aws.amazon.com/serverless/sam/") CLI can also enable faster debugging cycles when developing [Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") functions locally.
