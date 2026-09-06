

# Security
<a name="security-checks"></a>

You can use the following checks for the security category.

**Note**  
If you enabled Security Hub CSPM for your AWS account, you can view your findings in the Trusted Advisor console. For information, see [Viewing AWS Security Hub CSPM controls in AWS Trusted Advisor](security-hub-controls-with-trusted-advisor.md).  
You can view all controls in the AWS Foundational Security Best Practices security standard *except* for controls that have the **Category: Recover > Resilience**. For a list of supported controls, see [AWS Foundational Security Best Practices controls](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html) in the *AWS Security Hub CSPM User Guide*.

**Contents**
+ [Application Load Balancer security group](#alb-security-group)
+ [Amazon CloudWatch Log Group Retention Period](#cloudwatch-log-group-retention-less-than-365)
+ [Amazon EC2 instances with Microsoft SQL Server end of support](#ec2-instances-with-sql-server-end-of-support)
+ [Amazon EC2 instances with Microsoft Windows Server end of support](#ec2-instances-with-windows-server-end-of-support)
+ [Amazon EC2 instances with Ubuntu LTS end of standard support](#amazon-ec2-instances-ubuntu-lts-end-of-standard-support)
+ [Amazon EFS clients not using data-in-transit encryption](#amazon-efs-clients-not-using-data-in-transit-encryption)
+ [Amazon EBS Public Snapshots](#amazon-ebs-public-snapshots)
+ [Amazon RDS Aurora storage encryption is turned off](#amazon-rds-aurora-storage-encryption-off)
+ [Amazon RDS engine minor version upgrade is required](#amazon-rds-engine-minor-version-upgrade-required)
+ [Amazon RDS Public Snapshots](#amazon-rds-public-snapshots)
+ [Amazon RDS Security Group Access Risk](#amazon-rds-security-group-access-risk)
+ [Amazon RDS storage encryption is turned off](#amazon-rds-storage-encryption-off)
+ [Amazon Route 53 mismatching CNAME records pointing directly to S3 buckets](#amazon-route-53-mismatching-cname-records-s3-buckets)
+ [Amazon Route 53 MX Resource Record Sets and Sender Policy Framework](#amazon-route-53-mx-resorc-resource-record-sets-sender-policy-framework)
+ [Amazon S3 Bucket Permissions](#amazon-s3-bucket-permissions)
+ [Amazon VPC Peering Connections with DNS Resolution Disabled](#amazon-vpc-peering-connections-no-dns-resolution)
+ [Application Load Balancer Target Groups Encrypted Protocol](#application-load-balancer-target-groups)
+ [AWS Backup Vault Without Resource-based Policy to Prevent Deletion of Recovery Points](#backup-vault-without-resource-based-policy-prevent-delete)
+ [AWS CloudTrail Management Event Logging](#aws-cloudtrail-man-events-log)
+ [AWS Lambda Functions Using Deprecated Runtimes](#aws-lambda-functions-deprecated-runtimes)
+ [AWS Well-Architected high risk issues for security](#well-architected-high-risk-issues-security)
+ [CloudFront Custom SSL Certificates in the IAM Certificate Store](#cloudfront-custom-ssl-certificates-iam-certificate-store)
+ [CloudFront SSL Certificate on the Origin Server](#cloudfront-ssl-certificate-origin-server)
+ [ELB Listener Security](#elb-listener-security)
+ [Classic Load Balancer Security Groups](#elb-security-groups)
+ [Exposed Access Keys](#exposed-access-keys)
+ [IAM Access Key Rotation](#iam-access-key-rotation)
+ [IAM Access Analyzer External Access](#iam-access-analyzer-external-access)
+ [IAM Password Policy](#iam-password-policy)
+ [IAM SAML 2.0 Identity Provider](#iam-saml-identity-provider)
+ [MFA on root account](#mfa-root-account)
+ [Root User Access Key](#root-user-access-key)
+ [Security Groups – Specific Ports Unrestricted](#security-groups-specific-ports-unrestricted)
+ [Security Groups – Unrestricted Access](#security-groups-unrestricted-access)

## Application Load Balancer security group
<a name="alb-security-group"></a>

**Description**  
Checks the security groups attached to the Application Load Balancer and its Amazon EC2 targets. Application Load Balancer security groups should only allow inbound ports that are configured in a listener. A target's security groups should not accept direct connections from the internet in the same port the target receives traffic from the load balancer.  
If a security group allows access to ports that are not configured for the load balancer or allows direct access to targets, the risk of loss of data or malicious attacks increases.  
This check excludes the following groups:  
+ Target Groups that are not associated with IP addresses or EC2 instances.
+ Security group rules for IPv6 traffic.
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`8604e947f2`

**Alert Criteria**  
+ Red: Target has a public IP and a security group that allows inbound connections on the target control port from everywhere (0.0.0.0/0).
+ Red: Target has a public IP and a security group that allows inbound connections on the traffic port from everywhere (0.0.0.0/0).
+ Red: Application Load Balancer has authentication enabled and target allows inbound connections on the traffic port from everywhere (0.0.0.0/0).
+ Yellow: Target's security group allow inbound connections on the traffic port from everywhere (0.0.0.0/0).
+ Yellow: Target's security group allow inbound connections on the target control port from everywhere (0.0.0.0/0).
+ Yellow: Application Load Balancer security group allow inbound connections on ports that don't have a corresponding listener.
+ Yellow: Target's security group allow inbound connections on the target control port from a security group that is not attached to Application Load Balancer.
+ Green: Application Load Balancer security group only allows inbound connections on ports that match with a listener.

**Recommended Action**  
For improved security, make sure that your security groups only allow the necessary traffic flows:  
+ The Application Load Balancer's security groups should allow inbound connections only for the same ports configured in its listeners.
+ Use exclusive security groups for load balancers and targets.
+ Target security groups should allow connections in the traffic port only from the load balancer(s) it’s associated with.
+ Target security groups should allow connections in the target control port only from the load balancer(s) it's associated with.

**Additional Resources**  
+ [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
+ [Security groups for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-groups.html)

**Report columns**  
+ Status
+ Region
+ Target Group
+ ALB Name
+ ALB SG ID
+ Target SG ID
+ Auth Enabled
+ Last Updated Time

## Amazon CloudWatch Log Group Retention Period
<a name="cloudwatch-log-group-retention-less-than-365"></a>

**Description**  
Checks if Amazon CloudWatch log group retention period is set to 365 days or other specified number.  
By default, logs are kept indefinitely and never expire. However, you can adjust the retention policy for each log group to comply with industry regulations or legal requirements for a specific period.  
You can specify the minimum retention time and log group names using the **LogGroupNames** and **MinRetentionTime** parameters in your AWS Config rules.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz186`

**Source**  
`AWS Config Managed Rule: cw-loggroup-retention-period-check`

**Alert Criteria**  
Yellow: Retention period of an Amazon CloudWatch log group is less than the desired minimum number of days.

**Recommended Action**  
Configure a retention period of more than 365 days for your log data stored in Amazon CloudWatch Logs to meet compliance requirements.  
For more information, see [Change log data retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention).

**Additional Resources**  
[Altering CloudWatch log retention](https://docs.aws.amazon.com/managedservices/latest/userguide/log-customize-retention.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EC2 instances with Microsoft SQL Server end of support
<a name="ec2-instances-with-sql-server-end-of-support"></a>

**Description**  
Checks the SQL Server versions for Amazon Elastic Compute Cloud (Amazon EC2) instances running in the past 24 hours. This check alerts you if the versions are near or have reached the end of support. Each SQL Server version offers 10 years of support, including 5 years of mainstream support and 5 years of extended support. After the end of support, the SQL Server version won’t receive regular security updates. Running applications with unsupported SQL Server versions can bring security or compliance risks.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Qsdfp3A4L3`

**Alert Criteria**  
+ Red: An EC2 instance has an SQL Server version that reached the end of support.
+ Yellow: An EC2 instance has an SQL Server version that will reach the end of support in 12 months.

**Recommended Action**  
To modernize your SQL Server workloads, consider refactoring to AWS Cloud native databases like Amazon Aurora. For more information, see [Modernize Windows Workloads with AWS](https://aws.amazon.com/windows/modernization/).  
 To move to a fully managed database, consider replatforming to Amazon Relational Database Service (Amazon RDS). For more information, see [Amazon RDS for SQL Server](https://aws.amazon.com/rds/sqlserver/).  
To upgrade your SQL Server on Amazon EC2, consider using the automation runbook to simplify your upgrade. For more information, see the [AWS Systems Manager documentation](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awsec2-CloneInstanceAndUpgradeSQLServer.html).  
 If you can’t upgrade your SQL Server on Amazon EC2, consider the End-of-Support Migration Program (EMP) for Windows Server. For more information, see the [EMP Website](https://aws.amazon.com/emp-windows-server/).

**Additional Resources**  
+ [Get ready for SQL Server end of support with AWS](https://aws.amazon.com/sql/sql2008-eos/)
+ [Microsoft SQL Server on AWS](https://aws.amazon.com/sql)

**Report columns**  
+ Status
+ Region
+ Instance ID
+ SQL Server Version
+ Support Cycle
+ End of Support
+ Last Updated Time

## Amazon EC2 instances with Microsoft Windows Server end of support
<a name="ec2-instances-with-windows-server-end-of-support"></a>

**Description**  
This check alerts you if your Microsoft Windows Server versions are near or have reached the end of support. Each Windows Server version offers 10 years of support, including 5 years of mainstream support and 5 years of extended support. After the end of support, the Windows Server version won't receive regular security updates. Running applications with unsupported Windows Server versions can bring security or compliance risks.  
 This check generates results based on the AMI used to launch the EC2 instance. It's possible for the current instance operating system to be different from its launch AMI. For example, if you launched an instance from a Windows Server 2016 AMI and later upgrade to Windows Server 2019, the launch AMI doesn't change.
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Qsdfp3A4L4`

**Alert criteria**  
+ Red: An EC2 instance runs on a Windows Server version that reached the end of support (Windows Server 2003, 2003 R2, 2008, and 2008 R2).
+ Yellow: An EC2 instance runs on a Windows Server version that will reach the end of support in less than 18 months (Windows Server 2012 and 2012 R2).

**Recommended action**  
To modernize your Windows Server workloads, consider the various options available on [Modernize Windows Workloads with AWS](https://aws.amazon.com/windows/modernization/).  
To upgrade your Windows Server workloads to run on more recent versions of Windows Server, you can use an automation runbook. For more information, see the [AWS Systems Manager documentation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/os-inplaceupgrade.html).  
Complete the following steps:  
+ Upgrade the Windows Server version
+ Hard stop and start upon upgrading
+ If using EC2Config, migrate to EC2Launch

**Report columns**  
+ Status
+ Region
+ Instance ID
+ Windows Server Version
+ Support Cycle
+ End of Support
+ Last Updated Time

## Amazon EC2 instances with Ubuntu LTS end of standard support
<a name="amazon-ec2-instances-ubuntu-lts-end-of-standard-support"></a>

**Description**  
This check alerts you if the versions are near or have reached the end of standard support. It is important to take action – either by migrating to the next LTS or upgrading to Ubuntu Pro. After the end of support, your 18.04 LTS machines will not receive any security updates. With an Ubuntu Pro subscription, your Ubuntu 18.04 LTS deployment can receive Expanded Security Maintenance (ESM) until 2028. Security vulnerabilities that remain unpatched open your systems to hackers and the potential of a major breach.   
Results for this check are automatically refreshed at least once daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dfprch15`

**Alert Criteria**  
 Red: An Amazon EC2 instance has an Ubuntu version that reached the end of standard support (Ubuntu 18.04 LTS, 18.04.1 LTS, 18.04.2 LTS, 18.04.3 LTS, 18.04.4 LTS, 18.04.5 LTS, and 18.04.6 LTS).  
Yellow: An Amazon EC2 instance has an Ubuntu version that will reach the end of standard support in less than 6 months (Ubuntu 20.04 LTS, 20.04.1 LTS, 20.04.2 LTS, 20.04.3 LTS, 20.04.4 LTS, 20.04.5 LTS, and 20.04.6 LTS).  
Green: All Amazon EC2 instances are compliant.

**Recommended Action**  
To upgrade the Ubuntu 18.04 LTS instances to a supported LTS version, please follow the steps mentioned in [this article](https://ubuntu.com/server/docs/upgrade-introduction). To upgrade the Ubuntu 18.04 LTS instances to [Ubuntu Pro](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-ubuntu-pro-subscription-model/), visit AWS License Manager console and follow the steps mentioned in the [AWS License Manager user guide](https://docs.aws.amazon.com/license-manager/latest/userguide/license-conversion.html). You can also refer to the [Ubuntu blog](https://discourse.ubuntu.com/t/how-to-upgrade-ubuntu-lts-to-ubuntu-pro-on-aws-using-aws-license-manager/35449) showing a step by step demo of upgrading Ubuntu instances to Ubuntu Pro.

**Additional Resources**  
For information about pricing, reach out to [Support](https://aws.amazon.com/support).

**Report columns**  
+ Status
+ Region
+ Ubuntu Lts Version
+ Expected End Of Support Date
+ Instance ID
+ Support Cycle
+ Last Updated Time

## Amazon EFS clients not using data-in-transit encryption
<a name="amazon-efs-clients-not-using-data-in-transit-encryption"></a>

**Description**  
Checks if Amazon EFS file system is mounted using data-in-transit encryption. AWS recommends that customers use data-in-transit encryption for all data flows to protect data from accidental exposure or unauthorized access. Amazon EFS recommends clients use the ‘-o tls’ mount setting using the Amazon EFS mount helper to encrypt data in transit using TLS v1.2. 

**Check ID**  
` c1dfpnchv1`

**Alert Criteria**  
Yellow: One or more NFS clients for your Amazon EFS file system are not using the recommended mount settings that provide data-in-transit encryption.  
 Green: All NFS clients for your Amazon EFS file system are using the recommended mount settings that provide data-in-transit encryption.

**Recommended Action**  
To take advantage of data-in-transit encryption feature on Amazon EFS, we recommend that you remount your file system using the Amazon EFS mount helper and the recommended mount settings.   
Some Linux distributions don't include a version of stunnel that supports TLS features by default. If you're using an unsupported Linux distribution (see [Supported distributions](https://docs.aws.amazon.com/efs/latest/ug/using-amazon-efs-utils.html#efs-utils-supported-distros) in the *Amazon Elastic File System User Guide*), then it's a best practice that you upgrade it before remounting with the recommended mount setting.


**Additional Resources**  
+ [Encrypting data in transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html)

**Report columns**  
+ Status
+ Region
+ EFS File System ID
+ AZs with Unencrypted Connections
+ Last Updated Time

## Amazon EBS Public Snapshots
<a name="amazon-ebs-public-snapshots"></a>

**Description**  
Checks the permission settings for your Amazon Elastic Block Store (Amazon EBS) volume snapshots and alerts you if any snapshots are publicly accessible.   
When you make a snapshot public, you give all AWS accounts and users access to all the data on the snapshot. To share a snapshot only with specific users or accounts, mark the snapshot as private. Then, specify the user or accounts that you want to share the snapshot data with. Note that if you have Block Public Access enabled in ‘block all sharing’ mode, then your public snapshots aren't publicly accessible and don't appear in the results of this check.   
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.

**Check ID**  
`ePs02jT06w`

**Alert Criteria**  
Red: The EBS volume snapshot is publicly accessible.

**Recommended Action**  
Unless you are certain that you want to share all the data in the snapshot with all AWS accounts and users, modify the permissions: mark the snapshot as private, and then specify the accounts that you want to give permissions to. For more information, see [Sharing an Amazon EBS Snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html). Use Block Public Access for EBS Snapshots to control the settings that allow public access to your data. This check can't be excluded from view in the Trusted Advisor console.  
To modify permissions for your snapshots directly, use a runbook in the AWS Systems Manager console. For more information, see [`AWSSupport-ModifyEBSSnapshotPermission`](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-modifyebssnapshotpermission.html).

**Additional Resources**  
[Amazon EBS Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)

**Report columns**  
+ Status
+ Region
+ Volume ID
+ Snapshot ID
+ Description

## Amazon RDS Aurora storage encryption is turned off
<a name="amazon-rds-aurora-storage-encryption-off"></a>

**Description**  
Amazon RDS supports encryption at rest for all the database engines by using the keys that you manage in AWS Key Management Service. On an active DB instance with Amazon RDS encryption, the data stored at rest in the storage is encrypted, similar to automated backups, read replicas, and snapshots.  
If encryption isn't turned on while creating an Aurora DB cluster, then you must restore a decrypted snapshot to an encrypted DB cluster.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.
This check relies on Amazon RDS Recommendations. This check doesn't evaluate DB instances in AWS Regions where Amazon RDS Recommendations isn't available. For information about regional availability, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html).

**Check ID**  
`c1qf5bt005`

**Alert Criteria**  
Red: Amazon RDS Aurora resources don't have encryption enabled.

**Recommended Action**  
Turn on encryption of data at rest for your DB cluster.

**Additional Resources**  
You can turn on encryption while creating a DB instance or use a workaround to turn on the encryption on an active DB instance. You can't modify a decrypted DB cluster to an encrypted DB cluster. However, you can restore a decrypted snapshot to an encrypted DB cluster. When you restore from the decrypted snapshot, you must specify a AWS KMS key.  
For more information, see [Encrypting Amazon Aurora resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html).

**Report columns**  
+ Status
+ Region
+ Resouce
+ Engine Name
+ Last Updated Time

## Amazon RDS engine minor version upgrade is required
<a name="amazon-rds-engine-minor-version-upgrade-required"></a>

**Description**  
Your database resources aren't running the latest minor DB engine version. The latest minor version contains the latest security fixes and other improvements.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.
This check relies on Amazon RDS Recommendations. This check doesn't evaluate DB instances in AWS Regions where Amazon RDS Recommendations isn't available. For information about regional availability, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html).

**Check ID**  
`c1qf5bt003`

**Alert Criteria**  
  
Yellow: Amazon RDS resources aren't running the latest minor DB engine version. 

**Recommended Action**  
Upgrade to the latest engine version.

**Additional Resources**  
We recommend that you maintain your database with the latest DB engine minor version as this version includes the latest security and functionality fixes. The DB engine minor version upgrades contain only the changes which are backward-compatible with earlier minor versions of the same major version of the DB engine.  
For more information, see [Upgrading a DB instance engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html).

**Report columns**  
+ Status
+ Region
+ Resouce
+ Engine Name
+ Engine Version Current
+ Recommended Value
+ Last Updated Time

## Amazon RDS Public Snapshots
<a name="amazon-rds-public-snapshots"></a>

**Description**  
Checks the permission settings for your Amazon Relational Database Service (Amazon RDS) DB snapshots and alerts you if any snapshots are marked as public.   
When you make a snapshot public, you give all AWS accounts and users access to all the data on the snapshot. If you want to share a snapshot only with specific users or accounts, mark the snapshot as private. Then, specify the user or accounts you want to share the snapshot data with.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.

**Check ID**  
`rSs93HQwa1`

**Alert Criteria**  
Red: The Amazon RDS snapshot is marked as public.

**Recommended Action**  
Unless you are certain you want to share all the data in the snapshot with all AWS accounts and users, modify the permissions: mark the snapshot as private, and then specify the accounts that you want to give permissions to. For more information, see [Sharing a DB Snapshot or DB Cluster Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html). This check can't be excluded from view in the Trusted Advisor console.  
To modify permissions for your snapshots directly, you can use a runbook in the AWS Systems Manager console. For more information, see [`AWSSupport-ModifyRDSSnapshotPermission`](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-modifyrdssnapshotpermission.html).

**Additional Resources**  
[Backing Up and Restoring Amazon RDS DB Instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)

**Report columns**  
+ Status
+ Region
+ DB Instance or Cluster ID
+ Snapshot ID

## Amazon RDS Security Group Access Risk
<a name="amazon-rds-security-group-access-risk"></a>

**Description**  
Checks security group configurations for Amazon Relational Database Service (Amazon RDS) and warns when a security group rule grants overly permissive access to your database. The recommended configuration for a security group rule is to allow access only from specific Amazon Elastic Compute Cloud (Amazon EC2) security groups or from a specific IP address.   
This check evaluates only security groups that are attached toAmazon RDS instances running outside on an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). 

**Check ID**  
`nNauJisYIT`

**Alert Criteria**  
+ Yellow: A DB security group rule references an Amazon EC2 security group that grants global access on one of these ports: 20, 21, 22, 1433, 1434, 3306, 3389, 4333, 5432, 5500. 
+ Red: A DB security group rule grants global access (the CIDR rule suffix is /0).
+ Green: A DB security group doesn't include permissive rules.

**Recommended Action**  
EC2-Classic was retired on August 15, 2022. It's recommend to move your Amazon RDS instances to a VPC and use Amazon EC2 security groups. For more information of moving your DB instance to a VPC see [Moving a DB instance not in a VPC into a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html).  
If you are unable to migrate your Amazon RDS instances to a VPC, then review your security group rules and restrict access to authorized IP addresses or IP ranges. To edit a security group, use the [AuthorizeDBSecurityGroupIngress](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AuthorizeDBSecurityGroupIngress.html) API or the AWS Management Console. For more information, see [Working with DB Security Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithSecurityGroups.html). 

**Additional Resources**  
+ [Amazon RDS Security Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html)
+ [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
+ [List of TCP and UDP port numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)

**Report columns**  
+ Status
+ Region
+ RDS Security Group Name
+ Ingress Rule
+ Reason

## Amazon RDS storage encryption is turned off
<a name="amazon-rds-storage-encryption-off"></a>

**Description**  
Amazon RDS supports encryption at rest for all the database engines by using the keys that you manage in AWS Key Management Service. On an active DB instance with Amazon RDS encryption, the data stored at rest in the storage is encrypted, similar to automated backups, read replicas, and snapshots.  
If encryption isn't turned on while creating a DB instance, then you must restore an encrypted copy of the decrypted snapshot before you turn on the encryption.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.
This check relies on Amazon RDS Recommendations. This check doesn't evaluate DB instances in AWS Regions where Amazon RDS Recommendations isn't available. For information about regional availability, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html).

**Check ID**  
`c1qf5bt006`

**Alert Criteria**  
Red: Amazon RDS resources don't have encryption enabled.

**Recommended Action**  
Turn on encryption of data at rest for your DB instance.

**Additional Resources**  
You can encrypt a DB instance only when you create the DB instance. To encrypt an existing active DB instance:  

**Create an encrypted copy of the original DB instance**

1. Create a snapshot of your DB instance.

1. Create an encrypted copy of the snapshot created in step 1.

1. Restore a DB instance from the encrypted snapshot.
For more information, see the following resources:  
+ [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
+ [Copying a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html)

**Report columns**  
+ Status
+ Region
+ Resouce
+ Engine Name
+ Last Updated Time

## Amazon Route 53 mismatching CNAME records pointing directly to S3 buckets
<a name="amazon-route-53-mismatching-cname-records-s3-buckets"></a>

**Description**  
Checks the Amazon Route 53 Hosted Zones with CNAME records pointing directly to Amazon S3 bucket hostnames and alerts if your CNAME does not match with your S3 bucket name. 

**Check ID**  
`c1ng44jvbm`

**Alert Criteria**  
Red: Amazon Route 53 Hosted Zone has CNAME records pointing to mismatching S3 bucket hostnames.  
Green: No mismatching CNAME records found in your Amazon Route 53 Hosted Zone.

**Recommended Action**  
When pointing CNAME records to S3 bucket hostnames, you must make sure that a matching bucket exists for any CNAME or alias record you configure. By doing this, you avoid the risk of your CNAME records being spoofed. You also prevent any unauthorized AWS user from hosting faulty or malicious web content with your domain.  
To avoid pointing CNAME records directly to S3 bucket hostnames, consider using origin access control (OAC) to access your S3 bucket web assets through Amazon CloudFront.  
For more information about associating CNAME with an Amazon S3 bucket hostname, see [Customizing Amazon S3 URLs with CNAME records](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#VirtualHostingCustomURLs).

**Additional Resources**  
+ [How to associate a hostname with an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#VirtualHostingCustomURLsHowTo)
+ [Restricting access to an Amazon S3 origin with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

**Report columns**  
+ Status
+ Hosted Zone ID
+ Hosted Zone ARN
+ Matching CNAME Records
+ Mismatching CNAME Records
+ Last Updated Time

## Amazon Route 53 MX Resource Record Sets and Sender Policy Framework
<a name="amazon-route-53-mx-resorc-resource-record-sets-sender-policy-framework"></a>

**Description**  
   For each MX record, checks for an associated TXT record that contains a valid SPF value. The TXT record value must start with “v=spf1". SPF record types are deprecated by the Internet Engineering Task Force (IETF). With Route 53, I'ts a best practice to use a TXT record instead of an SPF record. Trusted Advisor reports this check as green when an MX record has at least one associated TXT record with a valid SPF value.    
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`c9D319e7sG`

**Alert Criteria**  
+  Green: An MX resource record set has a TXT resource record that contains a valid SPF value. 
+  Yellow: An MX resource record set has a TXT or SPF resource record that contains a valid SPF value. 
+  Red: An MX resource record set doesn't have a TXT or SPF resource record that contains a valid SPF value. 

**Recommended Action**  
For each MX resource record set, create a TXT resource record set that contains a valid SPF value. For more information, see [Sender Policy Framework: SPF Record Syntax](http://www.open-spf.org/SPF_Record_Syntax) and [Creating Resource Record Sets By Using the Amazon Route 53 Console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RRSchanges_console.html). 

**Additional Resources**  
+ [MX record type](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#MXFormat)
+ [SPF record type](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#SPFFormat)
+ [re:Post Guidance](https://repost.aws/knowledge-center/route53-spf-record)
+ [RFC 7208](https://tools.ietf.org/html/rfc7208#section-14.1)

**Report columns**  
+ Hosted Zone Name
+ Hosted Zone ID
+ Resource Record Set Name
+ Status

## Amazon S3 Bucket Permissions
<a name="amazon-s3-bucket-permissions"></a>

**Description**  
Checks buckets in Amazon Simple Storage Service (Amazon S3) that have open access permissions, or that allow access to any authenticated AWS user.   
This check examines explicit bucket permissions, as well as bucket policies that might override those permissions. Granting list access permissions to all users for an Amazon S3 bucket is not recommended. These permissions can lead to unintended users listing objects in the bucket at high frequency, which can result in higher than expected charges. Permissions that grant upload and delete access to everyone can lead to security vulnerabilities in your bucket.

**Check ID**  
`Pfx0RwqBli`

**Alert criteria**  
+ Red: The bucket ACL allows List access or Upload/Delete access for **Everyone** or **Any Authenticated AWS User** and **Block Public Access** settings are not enabled.
+ Red: A bucket policy allows public access and **Block Public Access** settings are not enabled.
+ Red: Trusted Advisor does not have permission to check the policy, or the policy could not be evaluated for other reasons.
+ Yellow: A bucket policy allows public access, but the **Restrict Public Buckets** setting is turned on and restricts access to only authorized users of that account.
+ Yellow: The bucket is compliant but does not have full **Block Public Access** protection enabled.
+ Green: The bucket is compliant and has full **Block Public Access** protection enabled.
Public ACL grants are not evaluated when Block Public Access **Ignore Public ACLs** is enabled.

**Recommended action**  
If a bucket allows open access, determine if open access is truly needed. For example to host a static website, you can use Amazon CloudFront to serve the content hosted on Amazon S3. See [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the Amazon CloudFront Developer Guide. When possible,,  update the bucket permissions to restrict access to the owner or specific users. Use Amazon S3 Block Public Access to control the settings that allow public access to your data. See [Setting Bucket and Object Access Permissions](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/set-permissions.html).

**Additional resources**  
[Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html)  
[Configuring block public access settings for your Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html)

**Report columns**  
+ Status
+ Region Name
+ Region API Parameter
+ Bucket Name
+ ACL Allows List
+ ACL Allows Upload/Delete
+ Policy Allows Access

## Amazon VPC Peering Connections with DNS Resolution Disabled
<a name="amazon-vpc-peering-connections-no-dns-resolution"></a>

**Description**  
Checks if your VPC peering connections have DNS resolution turned on for both the acceptor and requester VPCs.  
DNS resolution for a VPC peering connection allows the resolution of public DNS hostnames to private IPv4 addresses when queried from your VPC. This allows the use of DNS names for communication between resources in peered VPCs. DNS resolution in your VPC peering connections makes application development and management simpler and less error-prone, and it ensures that resources always communicate privately over the VPC peering connection.  
You can specify the VPC IDs, using the **vpcIds** parameters in your AWS Config rules.  
For more information, see [Enable DNS resolution for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html#vpc-peering-dns).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz124`

**Source**  
`AWS Config Managed Rule: vpc-peering-dns-resolution-check`

**Alert Criteria**  
Yellow: DNS resolution is not enabled for both the acceptor and the requestor VPCs in a VPC peering connection.

**Recommended Action**  
Turn on DNS resolution for your VPC peering connections.

**Additional Resources**  
+ [Modify VPC peering connection options](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html#vpc-peering-dns)
+ [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Application Load Balancer Target Groups Encrypted Protocol
<a name="application-load-balancer-target-groups"></a>

**Description**  
Checks Application Load Balancer (ALB) target groups are using HTTPS protocol to encrypt communication in transit for back-end target types of instance or IP. HTTPS requests between ALB and back-end targets help to maintain data confidentiality for data in transit.

**Check ID**  
`c2vlfg0p1w`

**Alert Criteria**  
+ Yellow: Application Load Balancer target group using HTTP.
+ Green: Application Load Balancer target group using HTTPS.

**Recommended Action**  
Configure back-end target types of instance or IP to support HTTPS access, and change target group to use HTTPS protocol to encrypt communication between ALB and back-end target types of instance or IP.

**Additional Resources**  
[Enforce encryption in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html)  
[Application Load Balancer Target Types](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#target-type)  
[Application Load Balancer Routing Configuration](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#target-group-routing-configuration)  
[Data Protection in Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/data-protection.html)

**Report columns**  
+ Status
+ Region
+ ALB Arn
+ ALB Name
+ ALB VPC Id
+ Target Group Arn
+ Target Group Name
+ Target Group Protocol
+ Last Updated Time

## AWS Backup Vault Without Resource-based Policy to Prevent Deletion of Recovery Points
<a name="backup-vault-without-resource-based-policy-prevent-delete"></a>

**Description**  
Checks if AWS Backup vaults have an attached resource-based policy that prevents recovery point deletion.  
The resource-based policy prevents unexpected deletion of recovery points, which allows you to enforce access control with least privileges against your backup data.  
You can specify the AWS Identity and Access Management ARNs that you don't want the rule to check in the **principalArnList** parameter of your AWS Config rules.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz152`

**Source**  
`AWS Config Managed Rule: backup-recovery-point-manual-deletion-disabled`

**Alert Criteria**  
Yellow: There are AWS Backup vaults that don't have a resource-based policy to prevent deletion of recovery points.

**Recommended Action**  
Create resource-based policies for your AWS Backup vaults to prevent unexpected deletion of recovery points.  
The policy must include a "Deny" statement with backup:DeleteRecoveryPoint, backup:UpdateRecoveryPointLifecycle, and backup:PutBackupVaultAccessPolicy permissions.  
For more information, see [Set access policies on backup vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-a-vault-access-policy.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## AWS CloudTrail Management Event Logging
<a name="aws-cloudtrail-man-events-log"></a>

**Description**  
Checks your use of AWS CloudTrail. CloudTrail provides increased visibility into activity in your AWS account. It does this by recording information about AWS API calls that are made on the account. You can use these logs to determine, for example, what actions a particular user has taken during a specified time period, or which users have taken actions on a particular resource during a specified time period.   
Because CloudTrail delivers log files to an Amazon Simple Storage Service (Amazon S3) bucket, CloudTrail must have write permissions for the bucket. If a trail applies to all AWS Regions (the default when creating a new trail), then the trail appears multiple times in the Trusted Advisor report.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c25hn9x03v`

**Alert Criteria**  
+ Red: No trail is created for an AWS Region, or logging isn’t enabled for any trail.
+ Yellow: CloudTrail is enabled but all trails report log delivery errors.
+ Green: CloudTrail is enabled and no log delivery errors are reported.

**Recommended Action**  
To create a trail and start logging from the console, open the [AWS CloudTrail console](https://console.aws.amazon.com/cloudtrail/home).   
To start logging, see [Stopping and Starting Logging for a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_using_cli.html#stopstartclil).   
If you receive log delivery errors, then make sure that the bucket exists and that the necessary policy is attached to the bucket. See [Amazon S3 Bucket Policy](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_bucket_policy.html). 

**Additional Resources**  
+ [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/)
+ [Supported Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_supported_regions.html)
+ [Supported Services](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_supported_services.html)
+ [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

**Report columns**  
+ Status
+ Region
+ Logging Enabled
+ Delivery Error Reported
+ Last Updated Time

## AWS Lambda Functions Using Deprecated Runtimes
<a name="aws-lambda-functions-deprecated-runtimes"></a>

**Description**  
 Checks for Lambda functions whose $LATEST version is configured to use a runtime that is approaching deprecation, or is deprecated. Deprecated runtimes are not eligible for security updates or technical support  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
Published Lambda function versions are immutable, which means they can be invoked but not updated. Only the `$LATEST` version for a Lambda function can be updated. For more information, see [Lambda function versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html).

**Check ID**  
`L4dfs2Q4C5`

**Alert Criteria**  
+ Red: The function's $LATEST version is configured to use a runtime that is already deprecated.
+ Yellow: The function's $LATEST version is running on a runtime that is approaching deprecation. Functions are included at least 180 days before the runtime deprecation date.

**Recommended Action**  
If you have functions that are running on a runtime that is approaching deprecation, you should prepare for migration to a supported runtime. For more information, see [Runtime support policy](https://docs.aws.amazon.com/lambda/latest/dg/runtime-support-policy.html).  
We recommend that you delete earlier function versions that you’re no longer using.

**Additional Resources**  
[Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)

**Report columns**  
+ Status
+ Region
+ Function ARN
+ Runtime
+ Days to Deprecation
+ Deprecation Date
+ Average Daily Invokes
+ Last Updated Time

## AWS Well-Architected high risk issues for security
<a name="well-architected-high-risk-issues-security"></a>

**Description**  
Checks for high risk issues (HRIs) for your workloads in the security pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Wxdfp4B1L3`

**Alert Criteria**  
+ Red: At least one active high risk issue was identified in the security pillar for AWS Well-Architected.
+ Green: No active high risk issues were detected in the security pillar for AWS Well-Architected.

**Recommended Action**  
AWS Well-Architected detected high risk issues during your workload evaluation. These issues present opportunities to reduce risk and save money. Sign in to the [AWS Well-Architected](https://console.aws.amazon.com/wellarchitected) tool to review your answers and take action to resolve your active issues.

**Report columns**  
+ Status
+ Region
+ Workload ARN
+ Workload Name
+ Reviewer Name
+ Workload Type
+ Workload Started Date
+ Workload Last Modified Date
+ Number of identified HRIs for Security
+ Number of HRIs resolved for Security
+ Number of questions for Security
+ Total number of questions in Security pillar
+ Last Updated Time

## CloudFront Custom SSL Certificates in the IAM Certificate Store
<a name="cloudfront-custom-ssl-certificates-iam-certificate-store"></a>

**Description**  
This check applies to classic Amazon CloudFront distributions.
Checks the SSL certificates for CloudFront alternate domain names in the IAM certificate store. This check alerts you if a certificate is expired, will expire soon, uses outdated encryption, or is not configured correctly for the distribution.   
When a custom certificate for an alternate domain name expires, browsers that display your CloudFront content might show a warning message about the security of your website. Certificates that are encrypted by using the SHA-1 hashing algorithm are being deprecated by most web browsers such as Chrome and Firefox.  
A certificate must contain a domain name that matches either the Origin Domain Name or the domain name in the host header of a viewer request. If it doesn't match, CloudFront returns an HTTP status code of 502 (bad gateway) to the user. For more information, see [Using Alternate Domain Names and HTTPS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS).  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`N425c450f2`

**Alert Criteria**  
+ Red: A custom SSL certificate is expired.
+ Yellow: A custom SSL certificate expires in the next seven days.
+ Yellow: A custom SSL certificate was encrypted by using the SHA-1 hashing algorithm.
+ Yellow: One or more of the alternate domain names in the distribution don't appear either in the Common Name field or the Subject Alternative Names field of the custom SSL certificate.

**Recommended Action**  
We recommend using AWS Certificate Manager to provision, manage, and deploy your server certificates. With ACM, you can request a new certificate or deploy an existing ACM or external certificate to AWS resources. Certificates provided by ACM are free and can be automatically renewed. For more information about using ACM, see the [AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html). To verify the AWS Regions ACM supports, see [AWS Certificate Manager endpoints](https://docs.aws.amazon.com/general/latest/gr/acm.html) and quotas in the AWS General Reference.  
 Renew expired certificates or certificates that are about to expire. For more information on renewing a certificate see [Managing server certificates](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html) in IAM.  
Replace a certificate that was encrypted by using the SHA-1 hashing algorithm with a certificate that is encrypted by using the SHA-256 hashing algorithm.  
Replace the certificate with a certificate that contains the applicable values in the Common Name or Subject Alternative Domain Names fields.

**Additional Resources**  
[Using an HTTPS Connection to Access Your Objects](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html)  
[Importing Certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html)  
[AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)

**Report columns**  
+ Status
+ Distribution ID
+ Distribution Domain Name
+ Certificate Name
+ Reason

## CloudFront SSL Certificate on the Origin Server
<a name="cloudfront-ssl-certificate-origin-server"></a>

**Description**  
Checks your origin server for SSL certificates that are expired, about to expire, missing, or that use outdated encryption. If a certificate has one of these issues, CloudFront responds to requests for your content with HTTP status code 502, Bad Gateway.  
Certificates that were encrypted by using the SHA-1 hashing algorithm are being deprecated by web browsers such as Chrome and Firefox. Depending on the number of SSL certificates that you have associated with your CloudFront distributions, this check might add a few cents per month to your bill with your web hosting provider, for example, AWS if you're using Amazon EC2 or Elastic Load Balancing as the origin for your CloudFront distribution. This check does not validate your origin certificate chain or certificate authorities. You can check these in your CloudFront configuration.   
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`N430c450f2`

**Alert Criteria**  
+ Red: An SSL certificate on your origin has expired or is missing.
+ Yellow: An SSL certificate on your origin expires in the next thirty days.
+ Yellow: An SSL certificate on your origin was encrypted by using the SHA-1 hashing algorithm.
+ Yellow: An SSL certificate on your origin can't be located. The connection might have failed due to timeout, or other HTTPS connection problems.

**Recommended Action**  
Renew the certificate on your origin if it has expired or is about to expire.  
Add a certificate if one does not exist.  
Replace a certificate that was encrypted by using the SHA-1 hashing algorithm with a certificate that is encrypted by using the SHA-256 hashing algorithm.

**Additional Resources**  
[Using Alternate Domain Names and HTTPS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS)

**Report columns**  
+ Status
+ Distribution ID
+ Distribution Domain Name
+ Origin
+ Reason

## ELB Listener Security
<a name="elb-listener-security"></a>

**Description**  
   
Checks for classic load balancers with listeners that don't use the recommended security configurations for encrypted communication. AWS recommends that you use a secure protocol (HTTPS or SSL), up-to-date security policies, and ciphers and protocols that are secure. When you use a secure protocol for a front-end connection (client to load balancer), the requests are encrypted between your clients and the load balancer. This creates a more secure environment. Elastic Load Balancing provides predefined security policies with ciphers and protocols that adhere to AWS security best practices. New versions of predefined policies are released as new configurations become available.

**Check ID**  
`a2sEc6ILx`

**Alert Criteria**  
+  Red: A load balancer has no listeners configured with a secure protocol (HTTPS). 
+ Yellow: A load balancer HTTPS listener is configured with a Security Policy that contains a weak cipher.
+ Yellow: A load balancer HTTPS listener is not configured with the recommended Security Policy. 
+  Green: A load balancer has at least one HTTPS listener AND all HTTPS listeners are configured with the recommended policy. 

**Recommended Action**  
If the traffic to your load balancer must be secure, use either the HTTPS or the SSL protocol for the front-end connection.  
Upgrade your load balancer to the latest version of the predefined SSL security policy.  
Use only the recommended ciphers and protocols.  
For more information, see [Listener Configurations for Elastic Load Balancing](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-listener-config.html).

**Additional Resources**  
+ [Listener Configurations Quick Reference](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/using-elb-listenerconfig-quickref.html)
+ [Update SSL Negotiation Configuration of Your Load Balancer](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/ssl-config-update.html)
+ [SSL Negotiation Configurations for Elastic Load Balancing](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-ssl-security-policy.html)
+ [SSL Security Policy Table](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-security-policy-table.html)

**Report columns**  
+ Status
+ Region
+ Load Balancer Name
+ Load Balancer Port
+ Reason

## Classic Load Balancer Security Groups
<a name="elb-security-groups"></a>

**Description**  
Checks for load balancers configured with  a security group that allows access to ports that are not configured for the load balancer.   
 If a security group allows access to ports that are not configured for the load balancer, the risk of loss of data or malicious attacks increases.

**Check ID**  
`xSqX82fQu`

**Alert Criteria**  
+ Yellow: The inbound rules of an Amazon VPC security group associated with a load balancer allow access to ports that are not defined in the load balancer's listener configuration. 
+ Green: The inbound rules of an Amazon VPC security group associated with a load balancer do not allow access to ports that are not defined in the load balancers listener configuration. 

**Recommended Action**  
Configure the security group rules to restrict access to only those ports and protocols that are defined in the load balancer listener configuration, plus the ICMP protocol to support Path MTU Discovery. See [Listeners for Your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html) and [Security Groups for Load Balancers in a VPC](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-security-groups).  
If a security group is missing, apply a new security group to the load balancer. Create security group rules that restrict access to only those ports and protocols that are defined in the load balancer listener configuration. See [Security Groups for Load Balancers in a VPC](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-security-groups). 

**Additional Resources**  
+ [Elastic Load Balancing User Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/)
+ [Migrate your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/migrate-classic-load-balancer.html)
+ [Configure Your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-configure-load-balancer.html)

**Report columns**  
+ Status
+ Region
+ Load Balancer Name
+ Security Group IDs
+ Reason

## Exposed Access Keys
<a name="exposed-access-keys"></a>

**Description**  
Checks popular code repositories for access keys that have been exposed to the public and for irregular Amazon Elastic Compute Cloud (Amazon EC2) usage that could be the result of a compromised access key.   
An access key consists of an access key ID and the corresponding secret access key. Exposed access keys pose a security risk to your account and other users, could lead to excessive charges from unauthorized activity or abuse, and violate the [AWS Customer Agreement](https://aws.amazon.com/agreement).   
If your access key is exposed, take immediate action to secure your account. To protect your account from excessive charges, AWS temporarily limits your ability to create some AWS resources. This does not make your account secure. It only partially limits the unauthorized usage for which you could be charged.  
This check doesn't guarantee the identification of exposed access keys or compromised EC2 instances. You are ultimately responsible for the safety and security of your access keys and AWS resources.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
 If a deadline is shown for an access key, AWS may suspend your AWS account if the unauthorized usage is not stopped by that date. If you believe an alert is in error, [contact AWS Support](https://console.aws.amazon.com/support/home?#/case/create?issueType=customer-service&serviceCode=customer-account&categoryCode=security).  
The information displayed in Trusted Advisor might not reflect the most recent state of your account. No exposed access keys are marked as resolved until all exposed access keys on the account have been resolved. This data synchronization can take up to one week.

**Check ID**  
`12Fnkpl8Y5`

**Alert Criteria**  
+ Red: Potentially compromised – AWS has identified an access key ID and corresponding secret access key that have been exposed on the Internet and may have been compromised (used).
+ Red: Exposed – AWS has identified an access key ID and corresponding secret access key that have been exposed on the Internet.
+ Red: Suspected - Irregular Amazon EC2 usage indicates that an access key may have been compromised, but it has not been identified as exposed on the Internet.

**Recommended Action**  
Delete the affected access key as soon as possible. If the key is associated with an IAM user, see [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html).  
Check your account for unauthorized usage. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and check each service console for suspicious resources. Pay special attention to running Amazon EC2 instances, Spot Instance requests, access keys, and IAM users. You can also check overall usage on the [Billing and Cost Management console](https://console.aws.amazon.com/billing/home#/).

**Additional Resources**  
+ [Best Practices for Managing AWS Access Keys](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html)
+ [AWS Security Audit Guidelines](https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html)

**Report columns**  
+ Access Key ID
+ User Name (IAM or Root)
+ Fraud Type
+ Case ID
+ Time Updated
+ Location
+ Deadline
+ Usage (USD per Day)

## IAM Access Key Rotation
<a name="iam-access-key-rotation"></a>

**Description**  
Checks for active IAM access keys that have not been rotated in the last 90 days.   
When you rotate your access keys regularly, you reduce the chance that a compromised key could be used without your knowledge to access resources. For the purposes of this check, the last rotation date and time is when the access key was created or most recently activated. The access key number and date come from the `access_key_1_last_rotated` and `access_key_2_last_rotated` information in the most recent IAM credential report.  
Because the regeneration frequency of a credential report is restricted, refreshing this check might not reflect recent changes. For more information, see [Getting Credential Reports for Your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html).  
In order to create and rotate access keys, a user must have the appropriate permissions. For more information, see [Allow Users to Manage Their Own Passwords, Access Keys, and SSH Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_delegate-permissions_examples.html#creds-policies-credentials).

**Check ID**  
`DqdJqYeRm5`

**Alert Criteria**  
+ Green: The access key is active and has been rotated in the last 90 days.
+ Yellow: The access key is active and has been rotated in the last 2 years, but more than 90 days ago.
+ Red: The access key is active and has not been rotated in the last 2 years.

**Recommended Action**  
 Rotate access keys on a regular basis. See [Rotating Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) and [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

**Additional Resources**  
+ [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+ [How to rotate access keys for IAM users](https://aws.amazon.com/blogs/security/how-to-rotate-access-keys-for-iam-users/)

**Report columns**  
+ Status
+ IAM user
+ Access Key
+ Key Last Rotated
+ Reason

## IAM Access Analyzer External Access
<a name="iam-access-analyzer-external-access"></a>

**Description**  
Checks if the IAM Access Analyzer external access at the account level is present.  
IAM Access Analyzer external access analyzers help identify resources in your accounts that are shared with an external entity. The analyzer then creates a centralized dashboard with the findings. After the new analyzer is activated in the IAM console, security teams can then prioritize which accounts to review based on excessive permissions. An external access analyzer creates public and cross-account access findings for resources, and is provided at no additional charge.

**Check ID**  
`07602fcad6`

**Alert Criteria**  
+ Red: The analyzer external access isn’t activated at the account level.
+ Green: The analyzer external access is activated at the account level.

**Recommended Action**  
The creation of an external access analyzer per account helps security teams to prioritize which accounts to review based on excessive permissions. For more information, see [Getting started with AWS Identity and Access Management Access Analyzer findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html).  
Additionally, its a best practice to utilize the unused access analyzer, a paid feature that simplifies inspecting unused access to guide you toward least privilege. For more information, see [Identifying unused access granted to IAM users and roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html#what-is-access-analyzer-unused-access-analysis).

**Additional Resources**  
+ [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html#what-is-access-analyzer-resource-identification)
+ [IAM Access Analyzer updates: Find unused access, check policies before deployment ](https://aws.amazon.com/blogs/aws/iam-access-analyzer-updates-find-unused-access-check-policies-before-deployment)

**Report columns**  
+ Status
+ Region
+ Account External Access Analyzer Arn
+ Organization External Access Analyzer Arns
+ Last Updated Time

## IAM Password Policy
<a name="iam-password-policy"></a>

**Description**  
Checks the password policy for your account and warns when a password policy is not enabled, or if password content requirements have not been enabled.   
Password content requirements increase the overall security of your AWS environment by enforcing the creation of strong user passwords. When you create or change a password policy, the change is enforced immediately for new users but does not require existing users to change their passwords.

**Check ID**  
`Yw2K9puPzl`

**Alert Criteria**  
+ Green: A password policy is enabled with recommended content requirement enabled. 
+ Yellow: A password policy is enabled, but at least one content requirement is not enabled. 

**Recommended Action**  
If some content requirements are not enabled, consider enabling them. If no password policy is enabled, create and configure one. See [Setting an Account Password Policy for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html).   
To access the AWS Management Console, IAM users need passwords. As a best practice, AWS highly recommends that instead of creating IAM users, you use federation. Federation allows users to use their existing corporate credentials to log into the AWS Management Console. Use IAM Identity Center to create or federate the user, and then assume an IAM role into an account.  
To learn more about identity providers and federation, see [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) in the IAM User Guide. To learn more about IAM Identity Center, see the [IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

**Additional Resources**  
[Managing Passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/Credentials-ManagingPasswords.html)

**Report columns**  
+ Password Policy
+ Uppercase
+ Lowercase
+ Number
+ Non-alphanumeric

## IAM SAML 2.0 Identity Provider
<a name="iam-saml-identity-provider"></a>

**Description**  
Checks if the AWS account is configured for access via an identity provider (IdP) that supports SAML 2.0. Be sure to follow best practices when you centralize identities and configure users in an [external identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) or [AWS IAM Identity Center](https://aws.amazon.com/single-sign-on/).

**Check ID**  
`c2vlfg0p86`

**Alert Criteria**  
+ Yellow: This account isn’t configured for access via an identity provider (IdP) that supports SAML 2.0.
+ Green: This account is configured for access via an identity provider (IdP) that supports SAML 2.0.

**Recommended Action**  
Activate IAM Identity Center for the AWS account. For more information, see [EnablingIAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html). After you turn on IAM Identity Center, you can then perform common tasks like creating a permission set and assigning access for Identity Center groups. For more information, see [Common tasks](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html).  
It’s a best practice to manage human users in IAM Identity Center. But you can activate federated user access with IAM for human users in the short-term for small scale deployments. For more information see [SAML 2.0 federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html).

**Additional Resources**  
[What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)  
[What IsIAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html)

**Report columns**  
+ Status
+ AWS account Id
+ Last Updated Time

## MFA on root account
<a name="mfa-root-account"></a>

**Description**  
Checks the root user credentials of an account and warns if multi-factor authentication (MFA) is not enabled.   
For increased security, we recommend that you protect your account by using MFA, which requires a user to enter a unique authentication code from their MFA hardware or virtual device when interacting with the AWS Management Console and associated websites.  
For your AWS Organizations management account, AWS requires multi-factor authentication (MFA) for the root user when accessing the AWS Management Console.   
For your AWS Organizations member accounts, we recommend that you centrally manage root credentials using AWS Identity and Access Management. Member account root user credentials can be deleted centrally, removing the need to manage MFA on root user credentials. For more information, see [Best practices for member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/best-practices_member-acct.html) in the *AWS Organizations User Guide*. 

**Check ID**  
`7DAFEmoDos`

**Alert criteria**  
+ Red: MFA is not enabled on the root account. 
+ Green: No root user credentials (root password) exist or MFA is enabled for the account.

**Recommended action**  
**If this is a member account in AWS Organizations:** Log in to your management account, enable the root access management feature in IAM, and remove your root user credentials from this member account. See [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html).  
**If this is a standalone or management account in AWS Organizations:** Log in to your root account and activate an MFA device. For more information, see [Check MFA status](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_checking-status.html) and [AWS Multi-factor authentication in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)

**Additional resources**  
+ [Centrally manage root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management)
+ [AWS Multi-factor authentication in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
+  [Multi-factor authentication for AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html) 

## Root User Access Key
<a name="root-user-access-key"></a>

**Description**  
Checks if the root user access key is present. It's strongly recommended that you don't create access key pairs for your root user. Because [only a few tasks require the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-tasks.html) and you typically perform those tasks infrequently, it’s a best practice to log in to the AWS Management Console to perform the root user tasks. Before you create access keys, review the [alternatives to long-term access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html#sec-alternatives-to-long-term-access-keys).

**Check ID**  
`c2vlfg0f4h`

**Alert Criteria**  
+ Red: The root user access key is present
+ Green: The root user access key isn’t present

**Recommended Action**  
Delete the access key(s) for the root user. See [Deleting access keys for the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user_manage_delete-key.html). This task must be performed by the root user. You can't perform these steps as an IAM user or role.

**Additional Resources**  
+ [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-tasks.html)
+ [Resetting a lost or forgotten root user password](https://docs.aws.amazon.com/IAM/latest/UserGuide/reset-root-password.html)

Report columns  
+ Status
+ Account ID
+ Last Updated Time

## Security Groups – Specific Ports Unrestricted
<a name="security-groups-specific-ports-unrestricted"></a>

**Description**  
Checks security groups for rules that allow unrestricted access (0.0.0.0/0) to specific ports.   
Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data). The ports with highest risk are flagged red, and those with less risk are flagged yellow. Ports flagged green are typically used by applications that require unrestricted access, such as HTTP and SMTP.  
If you have intentionally configured your security groups in this manner, we recommend using additional security measures to secure your infrastructure (such as IP tables).  
This check only evaluates security groups that you create and their inbound rules for IPv4 addresses. Security groups created by AWS Directory Service are flagged as red or yellow, but they don’t pose a security risk and can be  excluded. For more information, see the [Trusted Advisor FAQ](https://aws.amazon.com/premiumsupport/faqs/#AWS_Trusted_Advisor).   
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`HCP4007jGY`

**Alert Criteria**  
+ Green: Security Group provides unrestricted access on ports 80, 25, 443, or 465.
+ Red: Security Group provides unrestricted access to port 20, 21, 22 , 1433, 1434, 3306, 3389, 4333, 5432, or 5500.
+ Yellow: Security Group provides unrestricted access to any other port.

**Recommended Action**  
 Restrict access to only those IP addresses that require it. To restrict access to a specific IP address, set the suffix to /32 (for example, 192.0.2.10/32). Be sure to delete overly permissive rules after creating rules that are more restrictive.  
Review and delete unused security groups. You can use AWS Firewall Manager to centrally configure and manage security groups at scale across AWS accounts, For more information, see the [AWS Firewall Manager documentation](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html).  
Consider using Systems Manager Sessions Manager for SSH (Port 22) and RDP (Port 3389) access to EC2 instances. With sessions manager, you can access your EC2 instances without enabling port 22 and 3389 in the security group.   


**Additional Resources**  
+ [Amazon EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html)

  [List of TCP and UDP port numbers](http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
+ [Classless Inter-Domain Routing](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
+ [Working with Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with.html)
+ [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)

**Report columns**  
+ Status
+ Region
+ Security Group Name
+ Security Group ID
+ Protocol
+ From Port
+ To Port
+ Association

## Security Groups – Unrestricted Access
<a name="security-groups-unrestricted-access"></a>

**Description**  
Checks security groups for rules that allow unrestricted access to a resource.   
Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data).  
This check evaluates only security groups that you create and their inbound rules for IPv4 addresses. Security groups created by AWS Directory Service are flagged as red or yellow, but they don’t pose a security risk and can be excluded. For more information, see the [Trusted Advisor FAQ](https://aws.amazon.com/premiumsupport/faqs/#AWS_Trusted_Advisor).   
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`1iG5NDGVre`

**Alert Criteria**  
+ Green: A security group rule has a source IP address with a /0 suffix for ports 25, 80, or 443.
+ Yellow: A security group rule has a source IP address with a /0 suffix for ports other than 25, 80, or 443 and security group is attached to a resource.
+ Red: A security group rule has a source IP address with a /0 suffix for ports other than 25, 80, or 443 and security group is not attached to a resource.

**Recommended Action**  
Restrict access to only those IP addresses that require it. To restrict access to a specific IP address, set the suffix to /32 (for example, 192.0.2.10/32). Be sure to delete overly permissive rules after creating rules that are more restrictive.   
Review and delete unused security groups. You can use AWS Firewall Manager to centrally configure and manage security groups at scale across AWS accounts, For more information, see the [AWS Firewall Manager documentation](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html).  
Consider using Systems Manager Sessions Manager for SSH (Port 22) and RDP (Port 3389) access to EC2 instances. With sessions manager, you can access your EC2 instances without enabling port 22 and 3389 in the security group.   
 

**Additional Resources**  
+ [Amazon EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html)
+ [Classless Inter-Domain Routing](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
+ [Working with Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with.html)
+ [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)

**Report columns**  
+ Status
+ Region
+ Security Group Name
+ Security Group ID
+ Protocol
+ From Port
+ To Port
+ IP Range
+ Association