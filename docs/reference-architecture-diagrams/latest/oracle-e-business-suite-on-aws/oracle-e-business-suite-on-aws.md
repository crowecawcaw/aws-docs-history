

# Oracle E-Business Suite on AWS
<a name="oracle-e-business-suite-on-aws"></a>

Publication date: **August 3, 2023 ([Diagram history](#diagram-history))**

This reference architecture can be used to deploy Oracle E-Business Suite on AWS by showing how to configure high availability for the database and application tier.

## Oracle E-Business Suite on AWS Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how to deploy Oracle E-Business Suite on AWS by showing how to configure high availability for the database and application tier.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/oracle-e-business-suite-on-aws/images/oracle-e-business-suite-on-aws.png)


1. The architecture starts with a single Region and single Virtual Private Cloud (VPC) on-par with the on-premises data center. 

1.  Multiple Availability Zones (AZs) provide resilience and high availability for the production workload. 

1.  **Application Load Balancer** distributes network traffic to improve the scalability and availability of your applications across multiple AZs. 

1.  **AWS WAF** is the web application firewall that protects the Oracle E-Business Suite applications against common web exploits. 

1.  **Amazon Route 53** provides domain name service (DNS) configuration. 

1.  **Amazon WorkSpaces** provides a desktop experience in the cloud. Use **AWS Directory Service** to enable user authentication. 

1.  **Amazon Simple Storage Service** (Amazon S3) is used for storing backups, files, and objects. 

1.  **Amazon CloudWatch** is used for application logging, monitoring, and alarms. 

1.  **AWS Systems Manager** provides bastion-less access to instances in private subnet, along with management and monitoring capabilities. 

1.  **AWS Backup** is a fully managed service that enables you to centralize and automate data protection across on-premise and AWS services. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Contributors
<a name="contributors"></a>

 Contributors to this reference architecture diagram include: 
+  Joyjeet Banerjee, Senior Partner Solutions Architect, Amazon Web Services 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | August 3, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.