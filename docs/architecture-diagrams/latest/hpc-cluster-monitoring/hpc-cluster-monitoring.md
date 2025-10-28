# Cross-Account Amazon EC2 Status Monitoring for HPC Clusters

Publication date: **February 22, 2024 ([Diagram history](#diagram-history "#diagram-history"))**

This reference architecture demonstrates how to build a mechanism to
monitor [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") (Amazon EC2) state changes for high performance computing
(HPC) clusters across multiple AWS accounts. It includes a dashboard to
help monitor the cluster status as well as each individual Amazon EC2 instance's
status.

The following two use cases might use this architecture:

- A customer organization has many separate divisions using separate AWS accounts
  deploying elastic Amazon EC2-based HPC clusters. A central IT admin group wants to
  monitor these resources in real time from a single centralized source to better
  manage workflows and to be aware of current resource use.
- A third-party partner is managing HPC deployments in a customer account, but wants to help
  the customer meter usage, create budgets, send notifications, and improve overall visibility
  into their HPC use. The customers don’t want to share all logs and activities within an
  account with the partner, only the relevant HPC resources.

## Cross-Account Amazon EC2 Status Monitoring for HPC Clusters Diagram

![Reference architecture diagram showing how to build a mechanism to monitor Amazon EC2 state changes for HPC clusters across multiple AWS accounts. It includes a dashboard to help monitor the cluster status as well as each individual Amazon EC2 instance's status.](images/hpc-cluster-monitoring.png)

1. In this diagram, there are two types of AWS accounts:
   - **HPC cluster account(s)** - These accounts are where the **Amazon EC2** instance-based HPC compute clusters are deployed.
   - **Centralized monitoring account** - This is a centralized account where one or more HPC cluster accounts sends cluster notification statuses.

These are **Amazon EC2** instances to be monitored. When the
[instance state changes](../../../AWSEC2/latest/UserGuide/monitoring-instances-status-check.md "../../../AWSEC2/latest/UserGuide/monitoring-instances-status-check.md")
(start, stop, terminate), it sends the status of related events to [**Amazon EventBridge**](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/"). 2. **EventBridge** events are filtered by an [**Amazon EC2** tag](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md"),
and only those matching the
tag string are passed to the monitoring account in the form of a **Amazon CloudWatch** log. You need to have
an **Amazon EC2** tag attached (by default, the _HPC_ tag) in order to be
monitored. This limits the volume and type account activity being shared with the centralized monitoring account. 3. Once events are logged in [**Amazon CloudWatch Logs**](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")
in the HPC cluster account, it shares these logs with the centralized monitoring account by enabling the
[cross-account observability](https://aws.amazon.com/blogs/aws/new-amazon-cloudwatch-cross-account-observability/ "https://aws.amazon.com/blogs/aws/new-amazon-cloudwatch-cross-account-observability/")
feature in **Amazon CloudWatch**. 4. Monitor the latest cluster status in the **CloudWatch** dashboard. A dashboard is preconfigured and deployed
into the centralized monitoring account as a part of the deployment.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/hpc-cluster-monitoring.md "samples/hpc-cluster-monitoring.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | February 22, 2024 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
