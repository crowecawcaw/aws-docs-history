

# IBM Instana Observability on AWS
<a name="ibm-instana-observability"></a>

Publication date: **February 28, 2023 ([Diagram history](#diagram-history))**

This architecture shows how to use IBM Instana on AWS for automated observability of your entire technology stack.

## IBM Instana Observability on AWS
<a name="diagram1"></a>

![Architecture diagram showing IBM Instana observability on AWS for automated application performance management.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ibm-instana-observability/images/ibm-instana-observability.png)


1. Site reliability engineers (SREs) and developers access IBM Instana dashboards to troubleshoot and identify optimization opportunities.

1. IBM Instana collects data from monitored systems by using a single host agent on each host. You can deploy these agents on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html), [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), Amazon ECS, and Red Hat OpenShift Service on AWS (ROSA).

1. Host agents dynamically deploy sensors from sensor repositories for over 300 different technologies.

1. IBM Instana sensors collect traces and metrics data from [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) of AWS services like [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html), Amazon MSK, [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), Amazon Aurora, DynamoDB, and [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

1. IBM Instana sensors also collect traces and metrics from workloads deployed on AWS, like ROSA, IBM Db2, IBM MQ, and others.

1. Host agents collect and aggregate data from various IBM Instana sensors before sending the data to the IBM Instana backend.

1. You can also deploy IBM Instana agents on hosts in your corporate data center to collect and send data to the IBM Instana backend service.

1. The IBM Instana backend service sends alerts and events to users through methods such as APIs, webhooks, email, and instant messaging.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon CloudWatch product page](https://aws.amazon.com/cloudwatch/)
+ [ product page](https://aws.amazon.com/opensearch-service/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | February 28, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.