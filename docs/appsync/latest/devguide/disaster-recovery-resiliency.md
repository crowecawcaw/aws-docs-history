# Resilience in AWS AppSync

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, AWS AppSync allows most resources to be defined using AWS CloudFormation templates; for an example of using
AWS CloudFormation templates to declare AWS AppSync resources, see [Practical use
cases for AWS AppSync Pipeline Resolvers](https://aws.amazon.com/blogs/mobile/appsync-pipeline-resolvers-1/ "https://aws.amazon.com/blogs/mobile/appsync-pipeline-resolvers-1/") on the AWS blog and the [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md").
