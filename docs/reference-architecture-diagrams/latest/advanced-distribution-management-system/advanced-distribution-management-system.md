

# Advanced Distribution Management System on AWS
<a name="advanced-distribution-management-system"></a>

Publication date: **July 21, 2022 ([Diagram history](#adms-history))**

With this architecture, you can deploy an advanced distribution management system (ADMS) on [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/). The system is fully automated, resilient, and highly available. The solution meets low-latency, data residency, and local data processing requirements. It also connects to AWS Regional services for analytics and machine learning (ML).

## Advanced Distribution Management System diagram
<a name="adms-diagram"></a>

![Reference architecture diagram showing how to deploy ADMS on AWS Outposts with connectivity to AWS Regional services for analytics and ML.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/advanced-distribution-management-system/images/advanced-distribution-management-system.png)


The following steps describe the deployment topology and connectivity for this architecture:

1. Install two AWS Outposts racks in different physically isolated sites for a resilient and highly available setup. Home each rack to a different Availability Zone in the parent AWS Region.

1. Deploy multiple ADMS applications on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances running on AWS Outposts inside your data center. Use a purpose-built AWS database or deploy a vendor-supported database on Amazon EC2.

1. Connect the ADMS application to on-premises applications in the OT network and to field devices such as sensors and actuators. Use a low-latency local network through the Outposts local gateway.

1. Connect the Outpost to the home AWS Region through a service link for management of the AWS Outposts instance and intra-VPC traffic. Use your existing internet connection or [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. Connect applications running on AWS Outposts securely to other applications running in the AWS Region, such as a Distributed Energy Resource Management System (DERMS). Use services in the AWS Region such as [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/), [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html), and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for data analytics and ML use cases.

## Further reading
<a name="adms-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="adms-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#adms-history) | Reference architecture diagram first published. | July 21, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.