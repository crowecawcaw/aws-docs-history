

# AWS DevOps Monitoring Dashboard
<a name="aws-devops-monitoring-dashboard"></a>

Publication date: **April 12, 2022 ([Diagram history](#diagram-history))**

This architecture automates the process of ingesting, analyzing, and visualizing continuous integration/continuous delivery (CI/CD) metrics. This architecture can also be [deployed on AWS](https://docs.aws.amazon.com/solutions/latest/aws-devops-monitoring-dashboard/welcome.html) using an CloudFormation template that launches, configures, and runs the AWS services required to deploy this solution using AWS best practices for security and availability.

## AWS DevOps Monitoring Dashboard
<a name="diagram1"></a>

![Reference architecture diagram showing how you can use AWS services to ingest, analyze, and visualize continuous integration/continuous delivery (CI/CD) metrics.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/aws-devops-monitoring-dashboard/images/aws-devops-monitoring-dashboard.png)


1. An **Amazon EventBridge** events rule detects the events based on predefined event patterns and then sends the event data to an **Amazon Data Firehose** delivery stream. One event rule is created per event source. For activities in **AWS CodeBuild**, a **CloudWatch** metric stream is set up to capture **CloudWatch** metrics and deliver them to a **Firehose** delivery stream. For GitHub push events, an Amazon API endpoint is created to post these events and deliver them to a **Firehose** delivery stream.

1. An **Amazon EventBridge** events rule is also created to capture events from an **Amazon CloudWatch** alarm that monitors the status of an **CloudWatch** synthetics canary, if you have set up the canary and alarm in your account. This alarm is needed to gather data for calculating Mean Time to Recovery (MTTR) metrics.

1. **Firehose** uses an **Lambda** function for data transformation. The **Lambda** function extracts relevant data to each metric and sends it to an **Amazon S3** bucket for downstream processing.

1. The data in **Amazon S3** is linked to an **Amazon Athena** database, which runs queries against this data and returns query results to **Quick**.

1. **Quick** obtains the query results and builds dashboard visualizations for your management team.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Reference architecture updated](#diagram-history) | Updated for technical accuracy | April 12, 2022 | 
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | August 9, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.