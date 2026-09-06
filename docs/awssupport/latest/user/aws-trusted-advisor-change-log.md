

# Change log for AWS Trusted Advisor
<a name="aws-trusted-advisor-change-log"></a>

See the following topic for recent changes to Trusted Advisor checks. 

**Note**  
If you use the Trusted Advisor console or the AWS Support API, deprecated checks won't appear in check results. If you use a deprecated check, such as specifying the check ID in an AWS Support API operation or your code, then you receive API call errors. Remove these checks to avoid errors.

For more information about the available checks, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).


| Change date | Check name | Change description | 
| --- | --- | --- | 
| August 27, 2026 | Updated Security Hub CSPM checks in Trusted Advisor | Trusted Advisor supports only AWS Security Hub CSPM controls available through July 8, 2026. For more information, see [Viewing AWS Security Hub CSPM controls in AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/security-hub-controls-with-trusted-advisor.html). | 
| February 19, 2026 | New [Idle NAT gateways](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#idle-nat-gateways) | Added a new check to identify idle or underutilized NAT gateways that might be candidates for cost optimization. | 
| January 9, 2026 | Deprecated 5 Cost Optimization Trusted Advisor checks | The following checks were deprecated:+ Savings Plan - vZ2c2W1srf<br />+ Amazon Relational Database Service (RDS) Reserved Instance Optimization - 1qazXsw23e<br />+ Amazon Redshift Reserved Node Optimization - 1qw23er45t<br />+ Amazon ElastiCache Reserved Node Optimization - h3L1otH3re<br />+ Amazon OpenSearch Service Reserved Instance Optimization - 7ujm6yhn5t | 
| December 18, 2025 | Updated [Amazon S3 Bucket Versioning](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-s3-bucket-versioning) | Added a new **Alert criteria**:+ Yellow: Trusted Advisor doesn't have access to validate versioning | 
| December 17, 2025 | Updated [Amazon S3 Bucket Permissions](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#amazon-s3-bucket-permissions) | Updated the **Alert criteria** section. | 
| November 21, 2025 | Updated [Application Load Balancer security group](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#alb-security-group) | Updated the Application Load Balancer security group alerts and recommendations. | 
| November 17, 2025 | Updated [AWS STS global endpoint usage across AWS Regions check](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#sts-global-endpoint) description  | Updated the AWS STS global endpoint usage across AWS Regions check description to clarify when check results are refreshed. | 
| October 15, 2025 | Updated multiple check descriptions | A note was added to multiple check descriptions to indicate that the check reports all resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources. | 
| October 10, 2025 | Updated check reference | Updated the check reference to show all available checks. | 
| September 11, 2025 | [L4dfs2Q4C5: AWS Lambda functions using deprecated runtimes](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#aws-lambda-functions-deprecated-runtimes) | Updated **Yellow** alert criterion to indicate that runtimes deprecating within at least 180 are included. | 
| August 19, 2025 | [Pfx0RwqBli: Amazon S3 Bucket Permissions](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#amazon-s3-bucket-permissions) | Alert criteria updated: *Trusted Advisor does not have permission to check the policy or ACL, or the policy or ACL could not be evaluated for other reasons* changed from **Yellow** to **Red**. | 
| July 22, 2025 |  + vjafUGJ9H0: AWS CloudTrail Logging<br />+ BueAdJ7NrP: Amazon S3 Bucket Logging  | These checks are deprecated. | 
| July 03, 2025 | [Pfx0RwqBli: Amazon S3 Bucket Permissions](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#amazon-s3-bucket-permissions) | The **Alert criteria** is updated to reflect all Yellow and Red criteria. | 
| July 03, 2025 | [c1dfprch15: Amazon EC2 instances with Ubuntu LTS end of standard support](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#amazon-ec2-instances-ubuntu-lts-end-of-standard-support) | Updated the note to indicate that this check refreshes at least once daily. | 
| July 02, 2025 | [c1dvkm4z6b: Amazon ECS AWSLogs driver in blocking mode](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-ecs-awslogs-driver-blockingmode) | Amazon ECS changed the default setting for awslogs driver logging configuration parameter mode from `blocking` to `non-blocking`. The Yellow status description has been updated to reflect this change. | 
| July 02, 2025 | [7DAFEmoDos: MFA on root account](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#mfa-root-account) | Added information indicating that member account root user credentials can be deleted centrally, removing the need to manage MFA on root user credentials. | 
| June 9, 2025 | [c1z7kmr17n: Amazon Aurora cost optimization recommendations for DB cluster storage](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#aurora-cost-opt-db-cluster-storage) | New check | 
| June 09, 2025 | [c15m0mgld3: AWS STS global endpoint usage across AWS Regions](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#sts-global-endpoint) | Updated check: This check is now available for all AWS Support plans. | 
| June 02, 2025 | [c15m0mgld3: AWS STS global endpoint usage across AWS Regions](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#sts-global-endpoint) | New check | 
| May 30, 2025 |  + c1z7kmr15n: [Amazon DynamoDB reserved capacity purchase recommendations](cost-optimization-checks.md#dynamodb-reserved-capacity-purchase-rec)<br />+ c1z7kmr02n: [Amazon EBS cost optimization recommendations for volumes](cost-optimization-checks.md#ebs-cost-opt-for-volumes)<br />+ c1z7kmr01n: [Amazon EC2 cost optimization recommendations for Amazon EC2 Auto Scaling groups](cost-optimization-checks.md#ec2-cost-opt-for-autoscaling)<br />+ c1z7kmr00n: [Amazon EC2 cost optimization recommendations for instances](cost-optimization-checks.md#ec2-cost-opt-for-instances)<br />+ c1z7kmr13n: [Amazon ElastiCache reserved node purchase recommendations](cost-optimization-checks.md#elasticache-reserved-node-purchase-recommendations)<br />+ c1z7kmr16n: [Amazon MemoryDB reserved node purchase recommendations](cost-optimization-checks.md#memorydb-reserved-node-purchase-recommendations)<br />+ c1z7kmr14n: [Amazon OpenSearch Service Reserved Instance purchase recommendations](cost-optimization-checks.md#os-ri-purchase-recommendations)<br />+ c1z7kmr04n: [Amazon RDS cost optimization recommendations for DB instance storage](cost-optimization-checks.md#rds-cost-opt-for-db-instance-storage)<br />+ c1z7kmr03n: [Amazon RDS cost optimization recommendations for DB instances](cost-optimization-checks.md#rds-cost-opt-for-db-instances)<br />+ c1z7kmr11n: [Amazon RDS Reserved Instance purchase recommendations](cost-optimization-checks.md#rds-ri-purchase-recommendations)<br />+ c1z7kmr12n: [Amazon Redshift reserved node purchase recommendations](cost-optimization-checks.md#redshift-reserved-node-purchase-recommendations)<br />+ c1z7kmr06n: [AWS Fargate cost optimization recommendations for Amazon ECS](cost-optimization-checks.md#fargate-cost-opt-for-ecs)<br />+ c1z7kmr05n: [AWS Lambda cost optimization recommendations for functions](cost-optimization-checks.md#lambda-cost-opt-for-functions)<br />+ c1z7kmr08n: [AWS Savings Plans purchase recommendations for Amazon SageMaker AI](cost-optimization-checks.md#savings-plans-purchase-recommendations-sagemaker)<br />+ c1z7kmr09n: [AWS Savings Plans purchase recommendations for compute](cost-optimization-checks.md#savings-plans-purchase-recommendations-compute)  | New Cost Optimization Hub checks | 
| April 30, 2025 |  + [N420c450f2: CloudFront Alternate Domain Names](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#cloudfront-domain-name-check)<br />+ [N425c450f2: CloudFront Custom SSL Certificates in the IAM Certificate Store](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#cloudfront-custom-ssl-certificates-iam-certificate-store)  | Added a note indicating that this check applies to classic Amazon CloudFront distributions. | 
| April 30, 2025 | [N415c450f2: CloudFront Header Forwarding and Cache Hit Ratio](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#cloudfront-forwarded-headers) | Added a note indicating that this check applies to classic Amazon CloudFront distributions. | 
| April 02, 2025 | c1dfprch02: Amazon EFS Throughput Mode Optimization | The description of this check has changed. For more information, see [Amazon EC2 instances with Microsoft Windows Server end of support](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#ec2-instances-with-windows-server-end-of-support). | 
| April 02, 2025 | Qsdfp3A4L4: Amazon EC2 instances with Microsoft Windows Server end of support | The description of this check has changed. For more information, see [Amazon EFS Throughput Mode Optimization](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#amazon-efs-throughput-mode-optimization). | 

## Older updates
<a name="older-updates"></a>

The following AWS Security Hub CSPM checks are deprecated:


| Check name | Check ID | 
| --- | --- | 
| S3.10 - S3 general purpose buckets with versioning enabled should have lifecycle configurations | `Hs4Ma3G211` | 
| S3.11 - S3 general purpose buckets should have event notifications enabled | `Hs4Ma3G212` | 
| CodeBuild.5 - CodeBuild project environments should not have privileged mode enabled | `Hs4Ma3G218` | 
| CloudFormation.1 - CloudFormation stacks should be integrated with Amazon Simple Notification Service (SNS) | `Hs4Ma3G245` | 
| SNS.2 - Logging of delivery status should be enabled for notification messages sent to a topic | `Hs4Ma3G263` | 
| Athena.1 - Athena workgroups should be encrypted at rest | `Hs4Ma3G294` | 

## New check: Amazon RDS Continuous Backup Not Enabled
<a name="amazon-rds-cont-backups-new"></a>

Trusted Advisor added the following check on December 23, 2024.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| Amazon RDS Continuous Backup Not Enabled | Fault tolerance | `44fde09ab5` | 

Checks if an Amazon RDS instance is enabled with automated backups using Amazon RDS or with continuous backups of AWS Backup. Continuous backups reduce the risk of unexpected data loss and allow for point-in-time recovery.

For more information, see [Amazon RDS Continuous Backup Not Enabled](fault-tolerance-checks.md#amazon-rds-cont-backups).

## New check: AWS CloudTrail Management Events Logging
<a name="ct-man-event-logging-new"></a>

Trusted Advisor added the following check on December 23, 2024.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| AWS CloudTrail Management Events Logging | Security | `c25hn9x03v` | 

Checks your use of AWS CloudTrail.

For more information, see [AWS CloudTrail Management Event Logging](security-checks.md#aws-cloudtrail-man-events-log).

## Updated the Auto Scaling Group Resources check
<a name="as-group-resources-update"></a>

Trusted Advisor updated the following check on December 23, 2024.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| Auto Scaling Group Resources | Fault tolerance | `8CNsSllI5v` | 

The description of this check is updated to include launch configurations and launch templates.

A new alert critera, `Red: A launch template is associated with a deleted Amazon Machine Image (AMI).` was added.

For more information, see [Auto Scaling Group Resources](fault-tolerance-checks.md#auto-scaling-group-resources).

## Updated the IAM Access Analyzer External Access check
<a name="external-iam-analyzer-check-update"></a>

Trusted Advisor updated the following check on December 23, 2024.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| IAM Access Analyzer External Access | Security | `07602fcad6` | 

The description of this check is updated to indicate that it analyzes IAM access at the account level. For more information, see [IAM Access Analyzer External Access](security-checks.md#iam-access-analyzer-external-access).

## Added 1 new check
<a name="trusted-advisor-checks-nov-22"></a>

Trusted Advisor added 1 new check on November 22, 2024:
+ 8604e947f2 - [Application Load Balancer Security Groups](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#alb-security-group)

## Updated 3 checks
<a name="trusted-advisor-checks-nov-7"></a>

Trusted Advisor updated 3 checks on November 7, 2024:
+ b92b83d667 - [ELB Target Imbalance](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#elb-target-imbalance)
+ 8CNsSllI5v - [Auto Scaling Group Resources](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#auto-scaling-group-resources)
+ wuy7G1zxql - [Amazon EC2 Availability Zone Balance](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-ec2-availability-zone-balance)

## Added 4 checks
<a name="trusted-advisor-checks-oct-11"></a>

Trusted Advisor added 4 new checks on October 11, 2024:
+ 07602fcad6 - IAM Access Analyzer - external access
+ 528d6f5ee7 - GWLB - Endpoint AZ
+ c2vlfg0jp6 - Inactive VPC interface endpoints
+ c2vlfg0k35 - Inactive Gateway Load Balancer endpoints

## Updated 3 checks
<a name="trusted-advisor-checks-oct-2"></a>

Trusted Advisor updated 3 checks on October 2, 2024:
+ Check ID 7040ea389a moved from Cost Optimization pillar to the Fault Tolerance pillar
+ Updated Check ID 7DAFEmoDos
+ Updated Check ID Cmsvnj8db2

## Added 9 new checks
<a name="added-trusted-advisor-checks-aug-23"></a>

Trusted Advisor added 9 new checks on August 23, 2024:
+ c2vlfg0p86 - [IAM] - SAML 2.0 Identity Provider
+ 7040ea389a - Network Firewall endpoint Cross-AZ Data Transfer
+ c2vlfg0bfw - Low utilization Network Firewall
+ c2vlfg0gqd - Network Firewall Multi-AZ
+ c2vlfg0p1w - Application Load Balancer Target Groups encrypted protocol
+ c2vlfg022t - [NAT Gateway] - Underutilized Resource
+ c243hjzrhn - AWS Outposts Single Rack deployment
+ b92b83d667 - ELB Target Imbalance
+ 90046ff5b5 - MSK availability is limited to two zones

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## Updated 1 Security check and added 1 Security check
<a name="updated-trusted-advisor-checks-aug-22"></a>

Trusted Advisor updated 1 Operational Excellence checks on August 22, 2024:
+ c1fd6b96l4

Trusted Advisor added 1 Security checks on August 22, 2024:
+ c2vlfg0f4h

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## Updated 6 Security checks
<a name="updated-trusted-advisor-checks-aug-20"></a>

Trusted Advisor updated 6 Security checks on August 20, 2024:
+ nNauJisYIT
+ c9D319e7sG
+ a2sEc6ILx
+ HCP4007jGY
+ 1iG5NDGVre
+ Yw2K9puPzl

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## Updated 1 fault tolerance checks
<a name="updated-trusted-advisor-checks-aug-12"></a>

Trusted Advisor updated the 1 fault tolerance check and 1 security on August 12, 2024:
+ VPN Tunnel Redundancy
+ Amazon RDS engine minor version upgrade is required 

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## Updated 9 checks
<a name="updated-trusted-advisor-checks-july-21"></a>

Trusted Advisor updated the 9 checks on July 21, 2024:
+ 7qGXsKIUw
+ ZRxQlPsb6c
+ N425c450f2
+ 7DAFEmoDos
+ Pfx0RwqBli
+ H7IgTzjTYb
+ C056F80cR3
+ Yw2K9puPzl
+ xSqX82fQu

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## Removed 5 checks and added 1 check
<a name="deprecated-trusted-advisor-checks-may-15"></a>

Trusted Advisor deprecated 3 Fault Tolerance checks, 1 Perfomance check, and 1 Security check on May 15, 2024:
+ IAM Use
+ ELB Cross-Zone Load Balancing
+ Overutilized Amazon EBS Magnetic Volumes
+ Large Number of EC2 Security Group Rules Applied to an Instance
+ Large Number of Rules in an EC2 Security Group

Trusted Advisor added 1 new security check on May 15, 2024:
+ Amazon S3 Server Access Logs Enabled

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## Removed fault tolerance checks
<a name="deprecated-trusted-advisor-checks-april-25"></a>

Trusted Advisor deprecated 3 Fault Tolerance check on April 25, 2024:
+ Direct Connect Connection Redundancy
+ Direct Connect Location Redundancy 
+ Direct Connect Virtual Interface Redundancy 

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## New fault tolerance check
<a name="new-trusted-advisor-checks-feb-29"></a>

Trusted Advisor added 1 Fault Tolerance check on February 29, 2024:
+ NLB - Internet-facing resource in private subnet

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## Updated fault tolerance and security checks
<a name="new-trusted-advisor-checks-march-28"></a>

Trusted Advisor added 1 new Fault Tolerance check and amended 1 existing Fault tolerance and 1 Security check on March 28 2024:
+ Added AWS Resilience Hub Application Component check
+ Updated AWS Lambda VPC-enabled Functions without Multi-AZ Redundancy
+ Updated AWS Lambda Functions Using Deprecated Runtimes 

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## New fault tolerance check
<a name="new-trusted-advisor-checks-january-31"></a>

Trusted Advisor added 1 Fault Tolerance check on January 31, 2024:
+ Direct Connect Location Resiliency 

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## Updated fault tolerance check
<a name="new-trusted-advisor-checks-january-08"></a>

Trusted Advisor amended 1 Fault Tolerance check on January 08, 2024:
+ Amazon RDS innodb\_flush\_log\_at\_trx\_commit parameter is not 1

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## Updated security check
<a name="new-trusted-advisor-checks-december-20"></a>

Trusted Advisor amended 1 Security check on December 21, 2023:
+ AWS Lambda Functions Using Deprecated Runtimes

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## New security and performance checks
<a name="new-trusted-advisor-checks-december-20"></a>

Trusted Advisor added 2 new Security checks and 2 new Performance checks on December 20, 2023:
+ Amazon EFS clients not using data-in-transit encryption
+ Amazon Aurora DB cluster under-provisioned for read workload
+ Amazon RDS instance under-provisioned for system capacity
+ Amazon EC2 instances with Ubuntu LTS end of standard support

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## New security check
<a name="new-trusted-advisor-checks-december-15"></a>

Trusted Advisor added 1 new Security check on December 15, 2023:
+ Amazon Route 53 mismatching CNAME records pointing directly to S3 buckets

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## New fault tolerance and cost optimization checks
<a name="new-trusted-advisor-checks-december-07"></a>

Trusted Advisor added 2 new Fault Tolerance checks and 1 new Cost Optimization check on December 07, 2023:
+ Amazon DocumentDB Single-AZ clusters
+ Amazon S3 Incomplete Multipart Upload Abort Configuration
+ Amazon ECS AWSLogs driver in blocking mode

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## New fault tolerance checks
<a name="new-trusted-advisor-checks-november-17"></a>

Trusted Advisor added 3 new fault tolerance checks on November 17, 2023:
+ ALB Multi-AZ
+ NLB Multi-AZ
+ VPC interface endpoint network interfaces in multiple AZs

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## New checks for Amazon RDS
<a name="new-trusted-advisor-checks-november-14"></a>

Trusted Advisor added 37 new checks for Amazon RDS on November 15, 2023.

For more information, see the [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md).

## New AWS Trusted Advisor API
<a name="new-trusted-advisor-api-11-13-2023"></a>

 AWS Trusted Advisor introduces new APIs to enable you to programmatically access Trusted Advisor best practice checks, recommendations, and prioritized recommendations. Trusted Advisor APIs enable you to programmatically integrate Trusted Advisor with your preferred operational tool to automate and optimize your workloads at scale. Available to Business, Enterprise On-Ramp, or Enterprise Support customers, the new APIs provide access to Trusted Advisor recommendations for your account or all the linked accounts within a payer account. Enterprise Support customers with access to management or delegated administrator accounts can additionally programmatically retrieve prioritized recommendations across their organization. 

 The new Trusted Advisor APIs will replace the 3 functionalities previously offered through AWS Support API (SAPI). SAPI will continue to offer case and other support information. 

 Trusted Advisor APIs are generally available in the US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Seoul), Asia Pacific (Sydney), and Europe (Ireland) Regions. 

 To learn more, please visit the [AWS Trusted Advisor API page](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html). 

## Trusted Advisor check removal
<a name="remove-checks-11-09-2023"></a>

Trusted Advisor removed the following checks on November 9, 2023.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| EBS volumes should be attached to EC2 instances | Security | `Hs4Ma3G119` | 
| S3 buckets should have server-side encryption enabled | Security | `Hs4Ma3G167` | 
| CloudFront distributions should have origin access identity enabled | Security | `Hs4Ma3G195` | 

## Integration of AWS Config checks into Trusted Advisor
<a name="new-trusted-advisor-checks-october-26"></a>

Trusted Advisor added 64 new checks powered by AWS Config on October 30, 2023.

For more information, see the [View AWS Trusted Advisor checks powered by AWS Config](aws-config-integration-with-ta.md).

## New fault tolerance checks
<a name="new-trusted-advisor-checks-october-12"></a>

Trusted Advisor added the following checks on October 12, 2023.
+ Amazon RDS ReplicaLag
+ Amazon RDS FreeStorageSpace
+ Amazon RDS DiskQueueDepth
+ Amazon Route 53 Resolver Endpoint Availability Zone Redundancy
+ Auto Scaling available IPs in Subnets
+ Amazon MSK brokers hosting too many partitions

For more information, see the [Fault tolerance](fault-tolerance-checks.md) category.

## New service limits check
<a name="new-trusted-advisor-checks-august-17"></a>

Trusted Advisor added the following check on August 17, 2023.
+ Lambda Code Storage Usage

For more information, see the [Service limits](service-limits.md) category.

## New fault tolerance check
<a name="new-trusted-advisor-checks-august-03"></a>

Trusted Advisor added the following check on August 3, 2023.
+ AWS Lambda On Failure Event Destinations

For more information, see the [Fault tolerance](fault-tolerance-checks.md) category.

## New fault tolerance and performance checks
<a name="new-trusted-advisor-checks-june-01"></a>

Trusted Advisor added the following checks on June 1, 2023.
+ Amazon EFS No Mount Target Redundancy
+ Amazon EFS Throughput Mode Optimization
+ ActiveMQ Availability Zone Redundancy
+ RabbitMQ Availability Zone Redundancy

For more information, see the [Fault tolerance](fault-tolerance-checks.md) category and [Performance](performance-checks.md) category.

## New fault tolerance checks
<a name="new-trusted-advisor-checks-may-16"></a>

Trusted Advisor added the following checks on May 16, 2023.
+ NAT Gateway AZ Independence
+ Single AZ Application Check

For more information, see the [Fault tolerance](fault-tolerance-checks.md) category.

## New fault tolerance checks
<a name="new-trusted-advisor-checks-april-27"></a>

Trusted Advisor added the following checks on April 27, 2023.
+ Number of AWS Regions in an Incident Manager replication set
+ AWS Resilience Hub assessment age

For more information, see the [Fault tolerance](fault-tolerance-checks.md) category.

## Region Expansion of Amazon ECS Fault Tolerance Checks
<a name="add-ecs-checks-region-coverage"></a>

Trusted Advisor expanded the following checks into additional regions on April 27, 2023. Trusted Advisor checks for Amazon ECS are now available in all regions where Amazon ECS is generally available.
+ Amazon ECS service using a single AZ
+ Amazon ECS Multi-AZ placement strategy

Regions expanded into include Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Europe (Milan), Europe (Spain), Europe (Zurich), Middle East (Bahrain), Middle East (UAE).

## New fault tolerance checks
<a name="new-trusted-advisor-checks-march-30"></a>

Trusted Advisor added the following checks on March 30, 2023.
+ Amazon ECS service using a single AZ
+ Amazon ECS Multi-AZ placement strategy

For more information, see the [Fault tolerance](fault-tolerance-checks.md) category.

## New fault tolerance checks
<a name="new-trusted-advisor-checks-december-15"></a>

Trusted Advisor added the following checks on December 15, 2022.
+ AWS CloudHSM clusters running HSM instances in a single AZ
+ Amazon ElastiCache Multi-AZ clusters
+ Amazon MemoryDB Multi-AZ clusters

To receive results in Trusted Advisor for your AWS CloudHSM, ElastiCache, and MemoryDB clusters, you must have clusters in your Availability Zones. For more information, see the following documentation:
+ [AWS CloudHSM User Guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/)
+ [Amazon MemoryDB Developer Guide](https://docs.aws.amazon.com/memorydb/latest/devguide)

Trusted Advisor updated the following check information on December 15, 2022.
+ AWS Resilience Hub policy breached – App Name was updated to Application Name
+ AWS Resilience Hub resilience scores – App Name and App Resilience Score were updated to Application Name and Application Resilience Score

For more information, see the [Fault tolerance](fault-tolerance-checks.md) category.

## Updates to the Trusted Advisor integration with AWS Security Hub CSPM
<a name="security-hub-archived-findings"></a>

Trusted Advisor made the following update on November 17, 2022.

If you disable Security Hub CSPM or AWS Config for an AWS Region, Trusted Advisor now removes your control findings for that AWS Region within 7-9 days. Previously, the time frame to remove your Security Hub CSPM data from Trusted Advisor was 90 days.

For more information, see the following sections in the [Troubleshooting](security-hub-controls-with-trusted-advisor.md#troubleshooting-security-hub-integration) topic:
+ [I turned off Security Hub CSPM or AWS Config in a Region](security-hub-controls-with-trusted-advisor.md#disable-security-hub-regions)
+ [My control is archived in Security Hub CSPM, but I still see the findings in Trusted Advisor](security-hub-controls-with-trusted-advisor.md#archived-resource-still-appears-trusted-advisor)

## New fault tolerance checks for AWS Resilience Hub
<a name="new-trusted-advisor-checks-november-17"></a>

Trusted Advisor added the following checks on November 17, 2022.
+ AWS Resilience Hub policy breached
+ AWS Resilience Hub resilience scores

You can use these checks to view the latest resilience policy status and resilience score for your applications. Resilience Hub provides you with a central place to define, track, and manage the resiliency and availability of your applications.

To receive results in Trusted Advisor for your Resilience Hub applications, you must deploy an AWS application and use Resilience Hub to track the resiliency posture of the application. For more information, see the [AWS Resilience Hub User Guide](https://docs.aws.amazon.com/resilience-hub/latest/userguide).

To receive results in Trusted Advisor for your ElastiCache and MemoryDB clusters, you must have clusters in your Availability Zones. For more information, see the following documentation:

[Amazon MemoryDB Developer Guide](https://docs.aws.amazon.com/memorydb/latest/devguide)

For more information, see the [Fault tolerance](fault-tolerance-checks.md) category.

## Update to the Trusted Advisor console
<a name="ta-recommendations"></a>

Trusted Advisor added the following change on November 16, 2022.

The Trusted Advisor Dashboard in the console is now Trusted Advisor Recommendations. The Trusted Advisor Recommendations page still shows the check results and the available checks for each category for your AWS account.

This name change only updates the Trusted Advisor console. You can continue to use the Trusted Advisor console and the Trusted Advisor operations in the Support API as usual.

For more information, see [Get started with Trusted Advisor Recommendations](get-started-with-aws-trusted-advisor.md).

## New checks for Amazon EC2
<a name="ec2-windows-server-check"></a>

Trusted Advisor added the following check on September 1, 2022.
+ Amazon EC2 instances with Microsoft Windows Server end of support

For more information, see the [Security](security-checks.md) category.

## Added Security Hub CSPM checks to Trusted Advisor
<a name="added-security-hub-controls-06-22-2022"></a>

As of June 23, 2022, Trusted Advisor only supports Security Hub CSPM controls available through April 7, 2022. This release supports all controls in the AWS Foundational Security Best Practices security standard except for controls in the Category: Recover > Resilience. For more information, see [Viewing AWS Security Hub CSPM controls in AWS Trusted Advisor](security-hub-controls-with-trusted-advisor.md).

For a list of supported controls, see [AWS Foundational Security Best Practices controls](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html) in the *AWS Security Hub CSPM User Guide*.

## Added checks from AWS Compute Optimizer
<a name="added-checks-compute-optimizer"></a>

Trusted Advisor added the following checks on May 4, 2022.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| Amazon EBS over-provisioned volumes | Cost optimization | `COr6dfpM03` | 
| Amazon EBS under-provisioned volumes | Performance | `COr6dfpM04` | 
| AWS Lambda over-provisioned functions for memory size | Cost optimization | `COr6dfpM05` | 
| AWS Lambda under-provisioned functions for memory size | Performance | `COr6dfpM06` | 

You must opt in your AWS account for Compute Optimizer so that these checks can receive data from your Lambda and Amazon EBS resources. For more information, see [Opt in AWS Compute Optimizer for Trusted Advisor checks](compute-optimizer-with-trusted-advisor.md).

## Updates to the Exposed Access Keys check
<a name="update-exposed-access-keys-check"></a>

Trusted Advisor updated the following check on April 25, 2022.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| Exposed Access Keys | Security | `12Fnkpl8Y5` | 

Trusted Advisor now refreshes this check for you automatically. This check can't be refreshed manually from the Trusted Advisor console or the AWS Support API. If your application or code refreshes this check for your AWS account, we recommend that you update it to no longer refresh this check. Otherwise, you will receive the `InvalidParameterValue` error.

Any access keys that you excluded before this update will no longer be excluded and will appear as affected resources. You can't exclude access keys from your check results. For more information, see [Exposed Access Keys](security-checks.md#exposed-access-keys).

**Note**  
If you created your AWS account after April 25, 2022, the check results for Exposed Access Keys initially shows the gray icon (![Circular icon with a sad face emoticon, representing negative feedback or dissatisfaction.](http://docs.aws.amazon.com/awssupport/latest/user/images/gray.png)) even for unexposed access keys. This means that Trusted Advisor hasn't identified any changes to the check.  
If Trusted Advisor identifies a resource at risk, the status changes to the action recommended icon (![Red circle with white X inside, indicating an error or cancellation symbol.](http://docs.aws.amazon.com/awssupport/latest/user/images/red.png)). After you fix or delete the resource, the check result shows the check mark icon (![Green checkmark icon indicating success or approval.](http://docs.aws.amazon.com/awssupport/latest/user/images/green.png)).

## Updated checks for AWS Direct Connect
<a name="updated-checks-for-aws-direct-connect"></a>

Trusted Advisor updated the following checks on March 29, 2022.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| AWS Direct Connect Connection Redundancy | Fault tolerance | `0t121N1Ty3` | 
| AWS Direct Connect Location Redundancy | Fault tolerance | `8M012Ph3U5` | 
| AWS Direct Connect Virtual Interface Redundancy | Fault tolerance | `4g3Nt5M1Th` | 
+ The value for the **Region** column now shows the AWS Region code instead of the full name. For example, resources in US East (N. Virginia) will now have the `us-east-1` value.
+ The value for the **Time Stamp** column now appears in the RFC 3339 format, such as `2022-03-30T01:02:27.000Z`.
+ Resources that don't have any detected problems will now appear in the check table. These resources will have a check mark icon (![](http://docs.aws.amazon.com/awssupport/latest/user/images/green.png)) next to them.

  Previously, only resources that Trusted Advisor recommended that you investigate appeared in the table. These resources have a warning icon (![Warning triangle symbol with an exclamation mark inside.](http://docs.aws.amazon.com/awssupport/latest/user/images/warning.png)) next to them.

## AWS Security Hub CSPM controls added to the AWS Trusted Advisor console
<a name="new-security-hub-controls-for-trusted-advisor"></a>

AWS Trusted Advisor added 111 Security Hub CSPM controls to the **Security** category on January 18, 2022.

You can view your findings for Security Hub CSPM controls from the AWS Foundational Security Best Practices security standard. This integration doesn't include controls that have the **Category: Recover > Resilience**.

For more information about this feature, see [Viewing AWS Security Hub CSPM controls in AWS Trusted Advisor](security-hub-controls-with-trusted-advisor.md).

## New checks for Amazon EC2 and AWS Well-Architected
<a name="well-architected-sql-server-checks"></a>

Trusted Advisor added the following checks on December 20, 2021.
+ Amazon EC2 instances consolidation for Microsoft SQL Server
+ Amazon EC2 instances over-provisioned for Microsoft SQL Server
+ Amazon EC2 instances with Microsoft SQL Server end of support
+ AWS Well-Architected high risk issues for cost optimization
+ AWS Well-Architected high risk issues for performance
+ AWS Well-Architected high risk issues for security
+ AWS Well-Architected high risk issues for reliability

For more information, see the [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html).

## Updated check name for Amazon OpenSearch Service
<a name="check-name-change"></a>

Trusted Advisor updated the name for the Amazon OpenSearch Service Reserved Instance Optimization check on September 8, 2021.

The check recommendations, category, and ID are the same.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| Amazon OpenSearch Service Reserved Instance Optimization | Cost optimization | `7ujm6yhn5t` | 

**Note**  
If you use Trusted Advisor for Amazon CloudWatch metrics, the metric name for this check is also updated. For more information, see [Creating Amazon CloudWatch alarms to monitor AWS Trusted Advisor metrics](cloudwatch-metrics-ta.md).

## Added checks for Amazon Elastic Block Store volume storage
<a name="ebs-volume-storage-quota-checks"></a>

Trusted Advisor added the following checks on June 8, 2021.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| EBS General Purpose SSD (gp3) Volume Storage | Service limits | `dH7RR0l6J3` | 
| EBS Provisioned IOPS SSD (io2) Volume Storage | Service limits | `gI7MM0l7J2` | 

## Added checks for AWS Lambda
<a name="added-lambda-checks"></a>

Trusted Advisor added the following checks on March 8, 2021.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| AWS Lambda Functions with Excessive Timeouts | Cost optimization | `L4dfs2Q3C3` | 
| AWS Lambda Functions with High Error Rates | Cost optimization | `L4dfs2Q3C2` | 
| AWS Lambda Functions Using Deprecated Runtimes | Security | `L4dfs2Q4C5` | 
| AWS Lambda VPC-enabled Functions without Multi-AZ Redundancy | Fault tolerance | `L4dfs2Q4C6` | 

For more information about how to use these checks with Lambda, see [Example AWS Trusted Advisor workflow to view recommendations](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-servicemap.html#monitoring-ta-example) in the *AWS Lambda Developer Guide*.

## Trusted Advisor check removal
<a name="remove-checks-03-08-21"></a>

Trusted Advisor removed the following check for the AWS GovCloud (US) Region on March 8, 2021.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| EC2 Elastic IP Addresses | Service limits | `aW9HH0l8J6` | 

## Updated checks for Amazon Elastic Block Store
<a name="updated-checks-for-ebs-volume"></a>

Trusted Advisor updated the unit of Amazon EBS volume from gibibyte (GiB) to tebibyte (TiB) for the following checks on March 5, 2021. 

**Note**  
If you use Trusted Advisor for Amazon CloudWatch metrics, the metric names for these five checks are also updated. For more information, see [Creating Amazon CloudWatch alarms to monitor AWS Trusted Advisor metrics](cloudwatch-metrics-ta.md).


| Check name | Check category | Check ID | Updated CloudWatch metric for ServiceLimit | 
| --- | --- | --- | --- | 
| EBS Cold HDD (sc1) Volume Storage | Service limits | `gH5CC0e3J9` | Cold HDD (sc1) volume storage (TiB) | 
| EBS General Purpose SSD (gp2) Volume Storage | Service limits | `dH7RR0l6J9` | General Purpose SSD (gp2) volume storage (TiB) | 
| EBS Magnetic (standard) Volume Storage | Service limits | `cG7HH0l7J9` | Magnetic (standard) volume storage (TiB) | 
| EBS Provisioned IOPS SSD (io1) Volume Storage | Service limits | `gI7MM0l7J9` | Provisioned IOPS (SSD) storage (TiB) | 
| EBS Throughput Optimized HDD (st1) Volume Storage | Service limits | `wH7DD0l3J9` | Throughput Optimized HDD (st1) volume storage (TiB) | 

## Trusted Advisor check removal
<a name="trusted-advisor-checks-removal"></a>

**Note**  
Trusted Advisor removed the following checks on November 18, 2020.



| Checks removed on November 18, 2020 | Check category | Check ID | 
| --- | --- | --- | 
| EC2Config Service for EC2 Windows Instances | Fault tolerance | `V77iOLlBqz` | 
| ENA Driver Version for EC2 Windows Instances | Fault tolerance | `TyfdMXG69d` | 
| NVMe Driver Version for EC2 Windows Instances | Fault tolerance | `yHAGQJV9K5` | 
| PV Driver Version for EC2 Windows Instances | Fault tolerance | `Wnwm9Il5bG` | 
| EBS Active Volumes | Service limits | `fH7LL0l7J9` | 

Amazon Elastic Block Store no longer has a limit on the number of volumes that you can provision.

You can monitor your Amazon EC2 instances and verify they are up to date by using [AWS Systems Manager Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html), other third-party tools, or write your own scripts to return driver information for Windows Management Instrumentation (WMI).

## Trusted Advisor check removal
<a name="remove-checks-02-20-2020"></a>

Trusted Advisor removed the following check on February 18, 2020.


| Check name | Check category | Check ID | 
| --- | --- | --- | 
| Service Limits | Performance | `eW7HH0l7J9` | 