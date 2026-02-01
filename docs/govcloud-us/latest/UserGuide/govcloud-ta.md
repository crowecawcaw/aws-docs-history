# AWS Trusted Advisor in AWS GovCloud (US)

An online resource to help you reduce cost, increase performance, and improve security by optimizing your AWS environment, Trusted Advisor provides real time guidance to help you provision your resources following AWS best practices.

## How AWS Trusted Advisor Differs for AWS GovCloud (US)

- Email notifications for Trusted Advisor check summaries aren’t supported in the AWS GovCloud (US) Regions.
- The organizational view feature is currently not supported in the AWS GovCloud (US) Regions.
- For a list of supported checks in the AWS GovCloud (US) Regions, see [Supported Trusted Advisor checks](#supported-ta-checks "#supported-ta-checks"). You can also sign in to the [Trusted Advisor console](https://console.aws.amazon.com/trustedadvisor "https://console.aws.amazon.com/trustedadvisor").
- Email notifications for Trusted Advisor Priority recommendation summaries aren’t supported in the AWS GovCloud (US) Regions.
- Not all checks are automatically refreshed. For checks not automatically refreshed, customers can manually refresh via the Console or API.

### Supported Trusted Advisor checks

The following tables list the Trusted Advisor checks that are available in the AWS GovCloud (US) Regions and the required support level.

###### Topics

- [Cost optimization](#cost-optimization "#cost-optimization")
- [Fault tolerance](#fault-tolerance "#fault-tolerance")
- [Operational Excellence](#operation-excellence "#operation-excellence")
- [Performance](#performance "#performance")
- [Security](#security "#security")
- [Service quotas](#service-quotas "#service-quotas")

#### Cost optimization

The following table lists the Trusted Advisor checks for cost optimization that are available in the AWS GovCloud (US) Regions.

| ​                                                                       | Check                   | Support level |
| ----------------------------------------------------------------------- | ----------------------- | ------------- |
| Amazon EC2 Instances Stopped                                            | Business and Enterprise |
| Amazon ECR Repository Without Lifecycle Policy Configured               | Business and Enterprise |
| AWS Account Not Part of AWS Organizations                               | Business and Enterprise |
| Amazon RDS Idle DB Instances                                            | Business and Enterprise |
| Amazon S3 Bucket Lifecycle Policy Configured                            | Business and Enterprise |
| Amazon S3 version enabled buckets without lifecycle policies configured | Business and Enterprise |
| Idle Load Balancers                                                     | Business and Enterprise |
| Low Utilization Amazon EC2 Instances                                    | Business and Enterprise |
| Unassociated Elastic IP Addresses                                       | Business and Enterprise |
| Underutilized Amazon EBS Volumes                                        | Business and Enterprise |

#### Fault tolerance

The following table lists the Trusted Advisor checks for fault tolerance that are available in the AWS GovCloud (US) Regions.

| ​                                                                    | Check                   | Support level |
| -------------------------------------------------------------------- | ----------------------- | ------------- |
| Amazon Aurora DB Instance Accessibility                              | Business and Enterprise |
| Amazon DynamoDB Table Not Included in Backup Plan                    | Business and Enterprise |
| Amazon EBS Not Included in AWS Backup Plan                           | Business and Enterprise |
| Amazon EBS Snapshots                                                 | Business and Enterprise |
| Amazon EC2 Auto Scaling Group does not have ELB Health check Enabled | Business and Enterprise |
| Amazon EC2 Availability Zone Balance                                 | Business and Enterprise |
| Amazon EC2 Detailed Monitoring Not Enabled                           | Business and Enterprise |
| Amazon ECS service using a single AZ                                 | Business and Enterprise |
| Amazon ECS Multi-AZ placement strategy                               | Business and Enterprise |
| Amazon ElastiCache Multi-AZ Clusters                                 | Business and Enterprise |
| Amazon ElastiCache Redis clusters Automatic Backup                   | Business and Enterprise |
| AWS Lambda Functions without a dead-letter queue configured          | Business and Enterprise |
| Amazon MemoryDB Multi-AZ Clusters                                    | Business and Enterprise |
| Amazon Redshift cluster automated snapshots                          | Business and Enterprise |
| Amazon RDS not in AWS Backup Plan                                    | Business and Enterprise |
| Amazon RDS Backups                                                   | Business and Enterprise |
| Amazon RDS DB Instance Enhanced Monitoring Not Enabled               | Business and Enterprise |
| Amazon RDS Multi-AZ                                                  | Business and Enterprise |
| Amazon RDS Multi-AZ Standby Instance Not Enabled                     | Business and Enterprise |
| Amazon S3 Bucket Logging                                             | Business and Enterprise |
| Amazon S3 Bucket Replication Not Enabled                             | Business and Enterprise |
| Amazon S3 Bucket Versioning                                          | Business and Enterprise |
| Auto Scaling Group Resources                                         | Business and Enterprise |
| AWS Site-to-Site VPN has at least one Tunnel in DOWN Status          | Business and Enterprise |
| Auto Scaling Group Health Check                                      | Business and Enterprise |
| ELB Connection Draining                                              | Business and Enterprise |
| ELB Cross-Zone Load Balancing                                        | Business and Enterprise |
| Load Balancer Optimization                                           | Business and Enterprise |
| VPN Tunnel Redundancy                                                | Business and Enterprise |
| ActiveMQ Availability Zone Redundancy                                | Business and Enterprise |
| RabbitMQ Availability Zone Redundancy                                | Business and Enterprise |

#### Operational Excellence

The following table lists the Trusted Advisor checks for operational excellence that are available in the AWS GovCloud (US) Regions.

| ​                                                                                 | Check                   | Support level |
| --------------------------------------------------------------------------------- | ----------------------- | ------------- |
| Amazon API Gateway Not Logging Execution Logs                                     | Business and Enterprise |
| Amazon API Gateway REST APIs Without X-Ray Tracing Enabled                        | Business and Enterprise |
| Amazon EC2 Instance Not Managed by AWS Systems Manager                            | Business and Enterprise |
| Amazon ECR Repository With Tag Immutability Disabled                              | Business and Enterprise |
| Amazon ECS clusters with Container Insights disabled                              | Business and Enterprise |
| Amazon S3 does not have Event Notifications enabled                               | Business and Enterprise |
| Amazon VPC Without Flow Logs                                                      | Business and Enterprise |
| CloudFormation Stack Notification                                                 | Business and Enterprise |
| AWS CloudTrail data events logging for objects in an S3 bucket                    | Business and Enterprise |
| AWS CodeBuild Project Logging                                                     | Business and Enterprise |
| AWS Elastic Beanstalk Enhanced Health Reporting Is Not Configured                 | Business and Enterprise |
| AWS Elastic Beanstalk with Managed Platform Updates disabled                      | Business and Enterprise |
| AWS Fargate platform version is not latest                                        | Business and Enterprise |
| AWS Systems Manager State Manager Association in Non-compliant Status             | Business and Enterprise |
| Application Load Balancers and Classic Load Balancers Without Access Logs Enabled | Business and Enterprise |
| CloudTrail trails is not configured with Amazon CloudWatch Logs                   | Business and Enterprise |
| Elastic Load Balancing Deletion Protection Not Enabled for Load Balancers         | Business and Enterprise |
| RDS Cluster Deletion Protection Check                                             | Business and Enterprise |
| RDS DB Instance Automatic Minor Version Upgrade Check                             | Business and Enterprise |

#### Performance

The following table lists the Trusted Advisor checks for performance that are available in the AWS GovCloud (US) Regions.

| ​                                                                 | Check                   | Support level |
| ----------------------------------------------------------------- | ----------------------- | ------------- |
| Amazon DynamoDB Auto Scaling Not Enabled                          | Business and Enterprise |
| Amazon EBS Optimization Not Enabled                               | Business and Enterprise |
| Amazon EBS Provisioned IOPS (SSD) Volume Attachment Configuration | Business and Enterprise |
| Amazon EC2 to EBS Throughput Optimization                         | Business and Enterprise |
| Amazon EC2 Virtualization Type is Paravirtual                     | Business and Enterprise |
| High Utilization Amazon EC2 Instances                             | Business and Enterprise |
| Large Number of EC2 Security Group Rules Applied to an Instance   | Business and Enterprise |
| Large Number of Rules in an EC2 Security Group                    | Business and Enterprise |
| Overutilized Amazon EBS Magnetic Volumes                          | Business and Enterprise |
| AWS Lambda Functions without Concurrency Limit configured         | Business and Enterprise |

#### Security

The following table lists the Trusted Advisor checks for security that are available in the AWS GovCloud (US) Regions.

| ​                                                                                     | Check                   | Support level |
| ------------------------------------------------------------------------------------- | ----------------------- | ------------- |
| Amazon CloudWatch Log Group retention period less than 365 days                       | All support levels      |
| Amazon EBS Public Snapshots                                                           | All support levels      |
| Amazon RDS Security Group Access Risk                                                 | Business and Enterprise |
| Amazon RDS Public Snapshots                                                           | All support levels      |
| Amazon S3 Bucket Permissions                                                          | All support levels      |
| AWS Backup Vault Without Resource-Based Policy to Prevent Deletion of Recovery Points | Business and Enterprise |
| AWS CloudTrail Logging                                                                | Business and Enterprise |
| ELB Security Groups                                                                   | Business and Enterprise |
| ELB Listener Security                                                                 | Business and Enterprise |
| IAM Access Key Rotation                                                               | All support levels      |
| IAM Use                                                                               | All support levels      |
| IAM Password Policy                                                                   | Business and Enterprise |
| Security Groups – Specific Ports Unrestricted                                         | All support levels      |
| Security Groups – Unrestricted Access                                                 | Business and Enterprise |

#### Service quotas

The following table lists the checks for Trusted Advisor service quotas, formerly known as limits, that are available in the AWS GovCloud (US) Regions.

| ​                                                 | Check              | Support level |
| ------------------------------------------------- | ------------------ | ------------- |
| Amazon DynamoDB Throughput                        | All support levels |
| Auto Scaling Groups                               | All support levels |
| Auto Scaling Launch Configurations                | All support levels |
| CloudFormation Stacks                             | All support levels |
| DynamoDB Read Capacity                            | All support levels |
| DynamoDB Write Capacity                           | All support levels |
| EBS Active Snapshots                              | All support levels |
| EBS Cold HDD (sc1) Volume Storage                 | All support levels |
| EBS General Purpose SSD (gp2) Volume Storage      | All support levels |
| EBS General Purpose SSD (gp3) Volume Storage      | All support levels |
| EBS Magnetic (standard) Volume Storage            | All support levels |
| EBS Provisioned IOPS (SSD) Volume Aggregate IOPS  | All support levels |
| EBS Provisioned IOPS SSD (io1) Volume Storage     | All support levels |
| EBS Throughput Optimized HDD (st1) Volume Storage | All support levels |
| EC2 Reserved Instance Leases                      | All support levels |
| ELB Classic Load Balancers                        | All support levels |
| ELB Network Load Balancers                        | All support levels |
| ELB Application Load Balancers                    | All support levels |
| IAM Group                                         | All support levels |
| IAM Instance Profiles                             | All support levels |
| IAM Policies                                      | All support levels |
| IAM Roles                                         | All support levels |
| IAM Server Certificates                           | All support levels |
| IAM Users                                         | All support levels |
| Kinesis Shards per Region                         | All support levels |
| RDS Cluster Parameter Groups                      | All support levels |
| RDS Cluster Roles                                 | All support levels |
| RDS Clusters                                      | All support levels |
| RDS DB Instances                                  | All support levels |
| RDS DB Parameter Groups                           | All support levels |
| RDS DB Security Groups                            | All support levels |
| RDS DB Manual Snapshots                           | All support levels |
| RDS Event Subscriptions                           | All support levels |
| RDS Max Auths per Security Group                  | All support levels |
| RDS Option Groups                                 | All support levels |
| RDS Read Replicas per Master                      | All support levels |
| RDS Reserved Instances                            | All support levels |
| RDS Subnet Groups                                 | All support levels |
| RDS Subnets per Subnet Group                      | All support levels |
| RDS Total Storage Quota                           | All support levels |
| VPC                                               | All support levels |
| VPC Elastic IP Address                            | All support levels |
| VPC Internet Gateways                             | All support levels |

## Documentation for AWS Trusted Advisor

See the following topics:

- [AWS Trusted Advisor](../../../awssupport/latest/user/trusted-advisor.md "../../../awssupport/latest/user/trusted-advisor.md") in the _AWS Support User Guide_
- For more information about Trusted Advisor features, see [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/ "https://aws.amazon.com/premiumsupport/trustedadvisor/").
- For a complete list of Trusted Advisor checks, see the [AWS Trusted Advisor best practice checklist](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.
