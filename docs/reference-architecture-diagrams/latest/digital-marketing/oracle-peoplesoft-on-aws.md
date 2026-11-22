

# Oracle PeopleSoft on AWS

Publication date: **March 21, 2023 ([Diagram history](diagram-history.md))**

With this architecture, you can deploy a highly available and resilient Oracle PeopleSoft production environment on AWS.

## Oracle PeopleSoft on AWS diagram
<a name="oracle-peoplesoft-on-aws-diagram"></a>

![Oracle PeopleSoft runs on AWS across multiple Availability Zones for a highly available, resilient environment.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/digital-marketing/images/oracle-peoplesoft-on-aws.png)


The following steps describe the architecture:

1.  A single Region and single Virtual Private Cloud (VPC) on-par with the on-premises data center. 

1.  Multiple Availability Zones (AZs) provide resilience and high availability for the production workload. 

1.  [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) (ALB) distributes network traffic to improve the scalability and availability of your applications across multiple AZs. 

1.  [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) is the web application firewall that protects PeopleSoft against common web exploits. 

1.  [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) provides domain name service (DNS) configuration. 

1.  [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/) provides users with a desktop experience in the cloud. Use [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/) to enable user authentication. 

1.  [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) is used for storing backups, files, and objects. 

1.  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) is used for application logging, monitoring, and alarms. 

1.  [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) provides bastion-less access to instances in private subnet along with management and monitoring capabilities. 

1.  [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/) is a fully managed service that enables you to centralize and automate data protection across on-premises and AWS services. 

## Further reading
<a name="oracle-peoplesoft-on-aws-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 