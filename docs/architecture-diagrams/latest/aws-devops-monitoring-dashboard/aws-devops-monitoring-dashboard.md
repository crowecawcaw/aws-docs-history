# AWS DevOps Monitoring Dashboard

Publication date: **April 12, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture automates the process of ingesting, analyzing, and visualizing continuous
integration/continuous delivery (CI/CD) metrics. This architecture can also
be [deployed on AWS](../../../solutions/latest/aws-devops-monitoring-dashboard/welcome.md "../../../solutions/latest/aws-devops-monitoring-dashboard/welcome.md") using an AWS CloudFormation template that
launches, configures, and runs the AWS services required to deploy this solution using AWS best
practices for security and availability.

## AWS DevOps Monitoring Dashboard

![Reference architecture diagram showing how you can use AWS services to ingest, analyze, and visualize continuous integration/continuous delivery (CI/CD) metrics.](images/aws-devops-monitoring-dashboard.png)

1. An **Amazon EventBridge** events rule detects the events based on
   predefined event patterns and then sends the event data to an **Amazon Data Firehose** delivery stream. One event rule is created per event source. For
   activities in **AWS CodeBuild**, a **CloudWatch** metric stream is set up to capture **CloudWatch** metrics and deliver them to a **Firehose**
   delivery stream. For GitHub push events, an Amazon API endpoint is created to post these
   events and deliver them to a **Firehose** delivery
   stream.
2. An **Amazon EventBridge** events rule is also created to capture
   events from an **Amazon CloudWatch** alarm that monitors the status of
   an **CloudWatch** synthetics canary, if you have set up the canary
   and alarm in your account. This alarm is needed to gather data for calculating Mean Time
   to Recovery (MTTR) metrics.
3. **Firehose** uses an **Lambda**
   function for data transformation. The **Lambda** function
   extracts relevant data to each metric and sends it to an **Amazon S3** bucket for downstream processing.
4. The data in **Amazon S3** is linked to an **Amazon Athena** database, which runs queries against this data and
   returns query results to **Quick Suite**.
5. **Quick Suite** obtains the query results and builds dashboard
   visualizations for your management team.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/aws-devops-monitoring-dashboard.md "samples/aws-devops-monitoring-dashboard.md") which
contains an editable PowerPoint.

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

| Change                         | Description                                     | Date           |
| ------------------------------ | ----------------------------------------------- | -------------- |
| Reference architecture updated | Updated for technical accuracy                  | April 12, 2022 |
| Initial publication            | Reference architecture diagram first published. | August 9, 2021 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
