

# Configuration compliance in Accelerate
<a name="acc-sec-compliance"></a>

AMS Accelerate helps you configure your resources to high standards for security and operational integrity, and comply with the following industry standards:
+ Center for Internet Security (CIS)
+ National Institute of Standards and Technology (NIST) Cloud Security Framework (CSF)
+ Health Insurance Portability and Accountability Act (HIPAA)
+ Payment Card Industry (PCI) Data Security Standard (DSS)

We do this by deploying our entire compliance AWS Config rule set to your account, see [AMS Config Rule library](#acc-sec-compliance-rules). An AWS Config rule represents desired configurations for a resource and is evaluated against configuration changes on the settings of your AWS resources. Any configuration change triggers a large number of rules to test compliance. For example, suppose you create an Amazon S3 bucket, and configure it to be publicly readable, in violation of NIST standards. The [ams-nist-cis-s3-bucket-public-read-prohibited rule](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-read-prohibited.html) detects the violation and labels your S3 bucket **Noncompliant** in your Configuration Report. Because this rule belongs to the **Auto Incident** remediation category, it immediately creates a Incident Report, alerting you to the issue. Other more severe rule violations might cause AMS to automatically remediate the issue. See [Responses to violations in Accelerate](#acc-sec-compliance-responses).

**Important**  
If you want us to do more, for example, if you want AMS to remediate a violation for you, regardless of its remediation category, submit a Service Request that asks AMS to remediate the noncompliant resources for you. In the Service Request, include a comment such as "As part of the AMS config rule remediation, please remediate non-complaint resources {{RESOURCE\_ARNS\_OR\_IDs}}, config rule {{CONFIG\_RULE\_NAME}} in the account" and add the required inputs to remediate the violation.  
 If you want us to do less, for example, if you don't want us to take action on a particular S3 bucket that requires public access by design, you can create exceptions, see [Creating rule exceptions in Accelerate](#acc-sec-compliance-config-reports-exception). 

## AMS Config Rule library
<a name="acc-sec-compliance-rules"></a>

Accelerate deploys a library of AMS config rules to protect your account. These config rules begin with `ams-`. You can view rules within your account, and their compliance state, from either the AWS Config console, AWS CLI, or the AWS Config API. For general information about using AWS Config, see [ ViewingConfiguration Compliance](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_view-compliance.html).

**Note**  
For opt-in AWS Regions, and gov cloud Regions, we only deploy a subset of the config rules due to Region restrictions. Check the rule availability in Regions by checking the link associated to the identifier in the AMS Accelerate config rules table.  
You cannot remove any of the deployed AMS Config Rules.

### Table of Rules
<a name="acc-sec-config-rules-inventory"></a>

Download as [ams\_config\_rules.zip](samples/ams_config_rules.zip).


**AMS Configuration Rules**  

| Rule Name | Service | Trigger | Action | Frameworks | 
| --- | --- | --- | --- | --- | 
| [ams-nist-cis-guardduty-enabled-centralized](https://docs.aws.amazon.com/config/latest/developerguide/guardduty-enabled-centralized.html) | GuardDuty | Periodic | Remediate | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 2.2,3.4,8.2.1;  | 
| [ams-nist-cis-vpc-flow-logs-enabled](https://docs.aws.amazon.com/config/latest/developerguide/vpc-flow-logs-enabled.html) | VPC | Periodic | Remediate | CIS: CIS.6; NIST-CSF: DE.AE-1,DE.AE-3,PR.DS-5,PR.PT-1; HIPAA: 164.308(a)(3)(ii)(A),164.312(b); PCI: 2.2,10.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6;  | 
| [ams-eks-secrets-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/eks-secrets-encrypted.html) | EKS | Periodic | Incident | CIS: NA; NIST-CSF: NA; HIPAA: NA; PCI: NA;  | 
| [ams-eks-endpoint-no-public-access](https://docs.aws.amazon.com/config/latest/developerguide/eks-endpoint-no-public-access.html) | EKS | Periodic | Incident | CIS: NA; NIST-CSF: NA; HIPAA: NA; PCI: NA;  | 
| [ams-nist-cis-vpc-default-security-group-closed](https://docs.aws.amazon.com/config/latest/developerguide/vpc-default-security-group-closed.html) | VPC | Config Changes | Incident | CIS: CIS.11,CIS.12,CIS.9; NIST-CSF: DE.AE-1,PR.AC-3,PR.AC-5,PR.PT-4; HIPAA: 164.312(e)(1); PCI: 1.2,1.3,2.1,2.2,1.2.1,1.3.1,1.3.2,2.2.2;  | 
| [ams-nist-cis-iam-password-policy](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html) | IAM | Periodic | Incident | CIS: NA; NIST-CSF: PR.AC-1,PR.AC-4; HIPAA: 164.308(a)(3)(i),164.308(a)(3)(ii)(A),164.308(a)(3)(ii)(B),164.308(a)(4)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1); PCI: 7.1.2,7.1.3,7.2.1,7.2.2;  | 
| [ams-nist-cis-iam-root-access-key-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-root-access-key-check.html) | IAM | Periodic | Incident | CIS: CIS.16,CIS.4; NIST-CSF: PR.AC-1,PR.AC-4,PR.PT-3; HIPAA: 164.308(a)(3)(i),164.308(a)(3)(ii)(A),164.308(a)(3)(ii)(B),164.308(a)(4)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1); PCI: 2.2,7.1.2,7.1.3,7.2.1,7.2.2;  | 
| [ams-nist-cis-iam-user-mfa-enabled](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-mfa-enabled.html) | IAM | Periodic | Incident | CIS: CIS.16; NIST-CSF: PR.AC-1,PR.AC-4; HIPAA: 164.308(a)(3)(i),164.308(a)(3)(ii)(A),164.308(a)(3)(ii)(B),164.308(a)(4)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1); PCI: 2.2,7.1.2,7.1.3,7.2.1,7.2.2;  | 
| [ams-nist-cis-restricted-ssh](https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html) | Security Groups | Config Changes | Incident | CIS: CIS.16; NIST-CSF: PR.AC-1,PR.AC-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1); PCI: 2.2,7.2.1,8.1.4;  | 
| [ams-nist-cis-restricted-common-ports](https://docs.aws.amazon.com/config/latest/developerguide/restricted-common-ports.html) | Security Groups | Config Changes | Incident | CIS: CIS.11,CIS.12,CIS.9; NIST-CSF: DE.AE-1,PR.AC-3,PR.AC-5,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(3)(ii)(B),164.308(a)(4)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,2.2,1.2.1,1.3.1,1.3.2,2.2.2;  | 
| [ams-nist-cis-s3-account-level-public-access-blocks](https://docs.aws.amazon.com/config/latest/developerguide/s3-account-level-public-access-blocks.html) | S3 | Config Changes | Incident | CIS: CIS.9,CIS.12,CIS.14; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.2.1,1.3,1.3.1,1.3.2,1.3.4,1.3.6,2.2,2.2.2;  | 
| [ams-nist-cis-s3-bucket-public-read-prohibited](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-read-prohibited.html) | S3 | Config Changes | Incident | CIS: CIS.12,CIS.14,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,2.2,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-cis-s3-bucket-public-write-prohibited](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-write-prohibited.html) | S3 | Config Changes | Incident | CIS: CIS.12,CIS.14,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,2.2,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-cis-s3-bucket-server-side-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-server-side-encryption-enabled.html) | S3 | Config Changes | Incident | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(c)(2),164.312(e)(2)(ii); PCI: 2.2,3.4,10.5,8.2.1;  | 
| [ams-nist-cis-securityhub-enabled](https://docs.aws.amazon.com/config/latest/developerguide/securityhub-enabled.html) | Security Hub | Periodic | Incident | CIS: CIS.3,CIS.4,CIS.6,CIS.12,CIS.16,CIS.19; NIST-CSF: PR.DS-5,PR.PT-1; HIPAA: 164.312(b); PCI: NA;  | 
| [ams-nist-cis-ec2-instance-managed-by-systems-manager](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-managed-by-systems-manager.html) | EC2 | Config Changes | Report | CIS: CIS.2,CIS.5; NIST-CSF: ID.AM-2,PR.IP-1; HIPAA: 164.308(a)(5)(ii)(B); PCI: 2.4;  | 
| [ams-nist-cis-cloudtrail-enabled](https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-enabled.html) | CloudTrail | Periodic | Report | CIS: CIS.16,CIS.6; NIST-CSF: DE.AE-1,DE.AE-3,PR.DS-5,PR.MA-2,PR.PT-1; HIPAA: 164.308(a)(3)(ii)(A),164.308(a)(5)(ii)(C),164.312(b); PCI: 10.1,10.2.1,10.2.2,10.2.3,10.2.4,10.2.5,10.2.6,10.2.7,10.3.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6;  | 
| [ams-nist-cis-access-keys-rotated](https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html) | IAM | Periodic | Report | CIS: CIS.16; NIST-CSF: PR.AC-1; HIPAA: 164.308(a)(4)(ii)(B); PCI: 2.2;  | 
| [ams-nist-cis-acm-certificate-expiration-check](https://docs.aws.amazon.com/config/latest/developerguide/acm-certificate-expiration-check.html) | Certificate Manager | Config Changes | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.AC-5,PR.PT-4; HIPAA: NA; PCI: 4.1;  | 
| [ams-nist-cis-alb-http-to-https-redirection-check](https://docs.aws.amazon.com/config/latest/developerguide/alb-http-to-https-redirection-check.html) | ALB | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-2; HIPAA: 164.312(a)(2)(iv),164.312(e)(1),164.312(e)(2)(i),164.312(e)(2)(ii); PCI: 2.3,4.1,8.2.1;  | 
| [ams-nist-cis-api-gw-cache-enabled-and-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/api-gw-cache-enabled-and-encrypted.html) | API Gateway | Config Changes | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4;  | 
| [ams-nist-cis-api-gw-execution-logging-enabled](https://docs.aws.amazon.com/config/latest/developerguide/api-gw-execution-logging-enabled.html) | API Gateway | Config Changes | Report | CIS: CIS.6; NIST-CSF: DE.AE-1,DE.AE-3,PR.PT-1; HIPAA: 164.312(b); PCI: 10.1,10.3.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6,10.5.4;  | 
| [ams-nist-autoscaling-group-elb-healthcheck-required](https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-group-elb-healthcheck-required.html) | ELB | Config Changes | Report | CIS: NA; NIST-CSF: PR.PT-1,PR.PT-5; HIPAA: 164.312(b); PCI: 2.2;  | 
| [ams-nist-cis-cloud-trail-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-encryption-enabled.html) | CloudTrail | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 2.2,3.4,10.5;  | 
| [ams-nist-cis-cloud-trail-log-file-validation-enabled](https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-log-file-validation-enabled.html) | CloudTrail | Periodic | Report | CIS: CIS.6; NIST-CSF: PR.DS-6; HIPAA: 164.312(c)(1),164.312(c)(2); PCI: 2.2,10.5,11.5,10.5.2,10.5.5;  | 
| [ams-nist-cis-cloudtrail-s3-dataevents-enabled](https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-s3-dataevents-enabled.html) | CloudTrail | Periodic | Report | CIS: CIS.6; NIST-CSF: DE.AE-1,DE.AE-3,PR.DS-5,PR.PT-1; HIPAA: 164.308(a)(3)(ii)(A),164.312(b); PCI: 2.2,10.1,10.2.1,10.2.2,10.2.3,10.2.5,10.3.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6;  | 
| [ams-nist-cis-cloudwatch-alarm-action-check](https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-action-check.html) | CloudWatch | Config Changes | Report | CIS: CIS.13,CIS.14; NIST-CSF: NA; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4;  | 
| [ams-nist-cis-cloudwatch-log-group-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-log-group-encrypted.html) | CloudWatch | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: NA; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4;  | 
| [ams-nist-cis-codebuild-project-envvar-awscred-check](https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-envvar-awscred-check.html) | CodeBuild | Config Changes | Report | CIS: CIS.18; NIST-CSF: PR.DS-5; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1); PCI: 8.2.1;  | 
| [ams-nist-cis-codebuild-project-source-repo-url-check](https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-source-repo-url-check.html) | CodeBuild | Config Changes | Report | CIS: CIS.18; NIST-CSF: PR.DS-5; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1); PCI: 8.2.1;  | 
| [ams-nist-cis-db-instance-backup-enabled](https://docs.aws.amazon.com/config/latest/developerguide/db-instance-backup-enabled.html) | RDS | Config Changes | Report | CIS: CIS.10; NIST-CSF: ID.BE-5,PR.DS-4,PR.IP-4,PR.PT-5,RC.RP-1; HIPAA: 164.308(a)(7)(i),164.308(a)(7)(ii)(A),164.308(a)(7)(ii)(B); PCI: NA;  | 
| [ams-nist-cis-dms-replication-not-public](https://docs.aws.amazon.com/config/latest/developerguide/dms-replication-not-public.html) | DMS | Periodic | Report | CIS: CIS.12,CIS.14,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-dynamodb-autoscaling-enabled](https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-autoscaling-enabled.html) | DynamoDB | Periodic | Report | CIS: NA; NIST-CSF: ID.BE-5,PR.DS-4,PR.PT-5,RC.RP-1; HIPAA: 164.308(a)(7)(i),164.308(a)(7)(ii)(C); PCI: NA;  | 
| [ams-nist-cis-dynamodb-pitr-enabled](https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-pitr-enabled.html) | DynamoDB | Periodic | Report | CIS: CIS.10; NIST-CSF: ID.BE-5,PR.DS-4,PR.IP-4,PR.PT-5,RC.RP-1; HIPAA: 164.308(a)(7)(i),164.308(a)(7)(ii)(A),164.308(a)(7)(ii)(B); PCI: NA;  | 
| [ams-nist-dynamodb-throughput-limit-check](https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-throughput-limit-check.html) | DynamoDB | Periodic | Report | CIS: NA; NIST-CSF: NA; HIPAA: 164.312(b); PCI: NA;  | 
| [ams-nist-ebs-optimized-instance](https://docs.aws.amazon.com/config/latest/developerguide/ebs-optimized-instance.html) | EBS | Config Changes | Report | CIS: NA; NIST-CSF: NA; HIPAA: 164.308(a)(7)(i); PCI: NA;  | 
| [ams-nist-cis-ebs-snapshot-public-restorable-check](https://docs.aws.amazon.com/config/latest/developerguide/ebs-snapshot-public-restorable-check.html) | EBS | Periodic | Report | CIS: CIS.12,CIS.14,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-ec2-instance-detailed-monitoring-enabled](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-detailed-monitoring-enabled.html) | EC2 | Config Changes | Report | CIS: NA; NIST-CSF: DE.AE-1,PR.PT-1; HIPAA: 164.312(b); PCI: NA;  | 
| [ams-nist-cis-ec2-instance-no-public-ip](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-no-public-ip.html) | EC2 | Config Changes | Report | CIS: CIS.12,CIS.14,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-cis-ec2-managedinstance-association-compliance-status-check](https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-association-compliance-status-check.html) | EC2 | Config Changes | Report | CIS: CIS.12,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-cis-ec2-managedinstance-patch-compliance-status-check](https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-patch-compliance-status-check.html) | EC2 | Config Changes | Report | CIS: CIS.2,CIS.5; NIST-CSF: ID.AM-2,PR.IP-1; HIPAA: 164.308(a)(5)(ii)(B); PCI: 6.2;  | 
| [ams-nist-cis-ec2-stopped-instance](https://docs.aws.amazon.com/config/latest/developerguide/ec2-stopped-instance.html) | EC2 | Periodic | Report | CIS: CIS.2; NIST-CSF: ID.AM-2,PR.IP-1; HIPAA: NA; PCI: NA;  | 
| [ams-nist-cis-ec2-volume-inuse-check](https://docs.aws.amazon.com/config/latest/developerguide/ec2-volume-inuse-check.html) | EC2 | Config Changes | Report | CIS: CIS.2; NIST-CSF: PR.IP-1; HIPAA: NA; PCI: NA;  | 
| [ams-nist-cis-efs-encrypted-check](https://docs.aws.amazon.com/config/latest/developerguide/efs-encrypted-check.html) | EFS | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4,8.2.1;  | 
| [ams-nist-cis-eip-attached](https://docs.aws.amazon.com/config/latest/developerguide/eip-attached.html) | EC2 | Config Changes | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4,8.2.1;  | 
| [ams-nist-cis-elasticache-redis-cluster-automatic-backup-check](https://docs.aws.amazon.com/config/latest/developerguide/elasticache-redis-cluster-automatic-backup-check.html) | ElastiCache | Periodic | Report | CIS: CIS.10; NIST-CSF: ID.BE-5,PR.DS-4,PR.IP-4,PR.PT-5,RC.RP-1; HIPAA: 164.308(a)(7)(i),164.308(a)(7)(ii)(A),164.308(a)(7)(ii)(B); PCI: NA;  | 
| [ams-nist-cis-opensearch-encrypted-at-rest](https://docs.aws.amazon.com/config/latest/developerguide/opensearch-encrypted-at-rest.html) | OpenSearch | Periodic | Report | CIS: CIS.14,CIS.13; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4,8.2.1;  | 
| [ams-nist-cis-opensearch-in-vpc-only](https://docs.aws.amazon.com/config/latest/developerguide/opensearch-in-vpc-only.html) | OpenSearch | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4,8.2.1;  | 
| [ams-nist-cis-elb-acm-certificate-required](https://docs.aws.amazon.com/config/latest/developerguide/elb-acm-certificate-required.html) | Certificate Manager | Config Changes | Report | CIS: CIS.12,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-elb-deletion-protection-enabled](https://docs.aws.amazon.com/config/latest/developerguide/elb-deletion-protection-enabled.html) | ELB | Config Changes | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-2; HIPAA: 164.312(a)(2)(iv),164.312(e)(1),164.312(e)(2)(i),164.312(e)(2)(ii); PCI: 4.1,8.2.1;  | 
| [ams-nist-cis-elb-logging-enabled](https://docs.aws.amazon.com/config/latest/developerguide/elb-logging-enabled.html) | ELB | Config Changes | Report | CIS: CIS.6; NIST-CSF: DE.AE-1,DE.AE-3,PR.PT-1; HIPAA: 164.312(b); PCI: 10.1,10.3.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6,10.5.4;  | 
| [ams-nist-cis-emr-kerberos-enabled](https://docs.aws.amazon.com/config/latest/developerguide/emr-kerberos-enabled.html) | EMR | Periodic | Report | CIS: CIS.6; NIST-CSF: DE.AE-1,DE.AE-3,PR.PT-1; HIPAA: 164.312(b); PCI: 10.1,10.3.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6,10.5.4;  | 
| [ams-nist-cis-emr-master-no-public-ip](https://docs.aws.amazon.com/config/latest/developerguide/emr-master-no-public-ip.html) | EMR | Periodic | Report | CIS: CIS.14,CIS.16; NIST-CSF: PR.AC-1,PR.AC-4,PR.AC-6; HIPAA: 164.308(a)(3)(i),164.308(a)(3)(ii)(A),164.308(a)(3)(ii)(B),164.308(a)(4)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1); PCI: 7.2.1;  | 
| [ams-nist-cis-encrypted-volumes](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html) | EBS | Config Changes | Report | CIS: CIS.12,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-cis-guardduty-non-archived-findings](https://docs.aws.amazon.com/config/latest/developerguide/guardduty-non-archived-findings.html) | GuardDuty | Periodic | Report | CIS: CIS.12,CIS.13,CIS.16,CIS.19,CIS.3,CIS.4,CIS.6,CIS.8; NIST-CSF: DE.AE-2,DE.AE-3,DE.CM-4,DE.DP-5,ID.RA-1,ID.RA-3,PR.DS-5,PR.PT-1; HIPAA: 164.308(a)(5)(ii)(C),164.308(a)(6)(ii),164.312(b); PCI: 6.1,11.4,5.1.2;  | 
| [ams-nist-iam-group-has-users-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-group-has-users-check.html) | IAM | Config Changes | Report | CIS: NA; NIST-CSF: PR.AC-4,PR.AC-1; HIPAA: 164.308(a)(3)(i),164.308(a)(3)(ii)(A),164.308(a)(3)(ii)(B),164.308(a)(4)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1); PCI: 7.1.2,7.1.3,7.2.1,7.2.2;  | 
| [ams-nist-cis-iam-policy-no-statements-with-admin-access](https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-no-statements-with-admin-access.html) | IAM | Config Changes | Report | CIS: CIS.16; NIST-CSF: PR.AC-6,PR.AC-7; HIPAA: 164.308(a)(4)(ii)(B),164.308(a)(5)(ii)(D),164.312(d); PCI: 8.2.3,8.2.4,8.2.5;  | 
| [ams-nist-cis-iam-user-group-membership-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-group-membership-check.html) | IAM | Config Changes | Report | CIS: CIS.16,CIS.4; NIST-CSF: PR.AC-1,PR.AC-4,PR.PT-3; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(a)(2)(i); PCI: 2.2,7.1.2,7.2.1,8.1.1;  | 
| [ams-nist-cis-iam-user-no-policies-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-no-policies-check.html) | IAM | Config Changes | Report | CIS: CIS.16; NIST-CSF: PR.AC-1,PR.AC-7; HIPAA: 164.308(a)(4)(ii)(B),164.312(d); PCI: 8.3;  | 
| [ams-nist-cis-iam-user-unused-credentials-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-unused-credentials-check.html) | IAM | Periodic | Report | CIS: CIS.16; NIST-CSF: PR.AC-1,PR.AC-4,PR.PT-3; HIPAA: 164.308(a)(3)(i),164.308(a)(3)(ii)(A),164.308(a)(3)(ii)(B),164.308(a)(4)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1); PCI: 2.2,7.1.2,7.1.3,7.2.1,7.2.2;  | 
| [ams-nist-cis-ec2-instances-in-vpc](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instances-in-vpc.html) | EC2 | Config Changes | Report | CIS: CIS.11,CIS.12,CIS.9; NIST-CSF: DE.AE-1,PR.AC-3,PR.AC-5,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(3)(ii)(B),164.308(a)(4)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(B),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,2.2,1.2.1,1.3.1,1.3.2,2.2.2;  | 
| [ams-nist-cis-internet-gateway-authorized-vpc-only](https://docs.aws.amazon.com/config/latest/developerguide/internet-gateway-authorized-vpc-only.html) | Internet Gateway | Periodic | Report | CIS: CIS.9,CIS.12; NIST-CSF: NA; HIPAA: NA; PCI: NA;  | 
| [ams-nist-cis-kms-cmk-not-scheduled-for-deletion](https://docs.aws.amazon.com/config/latest/developerguide/kms-cmk-not-scheduled-for-deletion.html) | KMS | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: NA; PCI: 3.5,3.6;  | 
| [ams-nist-lambda-concurrency-check](https://docs.aws.amazon.com/config/latest/developerguide/lambda-concurrency-check.html) | Lambda | Config Changes | Report | CIS: NA; NIST-CSF: NA; HIPAA: 164.312(b); PCI: NA;  | 
| [ams-nist-lambda-dlq-check](https://docs.aws.amazon.com/config/latest/developerguide/lambda-dlq-check.html) | Lambda | Config Changes | Report | CIS: NA; NIST-CSF: NA; HIPAA: 164.312(b); PCI: NA;  | 
| [ams-nist-cis-lambda-function-public-access-prohibited](https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-public-access-prohibited.html) | Lambda | Config Changes | Report | CIS: CIS.12,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,2.2.2;  | 
| [ams-nist-cis-lambda-inside-vpc](https://docs.aws.amazon.com/config/latest/developerguide/lambda-inside-vpc.html) | Lambda | Config Changes | Report | CIS: CIS.12,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,2.2.2;  | 
| [ams-nist-cis-mfa-enabled-for-iam-console-access](https://docs.aws.amazon.com/config/latest/developerguide/mfa-enabled-for-iam-console-access.html) | IAM | Periodic | Report | CIS: CIS.16; NIST-CSF: PR.AC-7; HIPAA: 164.312(d); PCI: 2.2,8.3;  | 
| [ams-nist-cis-multi-region-cloudtrail-enabled](https://docs.aws.amazon.com/config/latest/developerguide/multi-region-cloudtrail-enabled.html) | CloudTrail | Periodic | Report | CIS: CIS.6; NIST-CSF: DE.AE-1,DE.AE-3,PR.DS-5,PR.MA-2,PR.PT-1; HIPAA: 164.308(a)(3)(ii)(A),164.312(b); PCI: 2.2,10.1,10.2.1,10.2.2,10.2.3,10.2.4,10.2.5,10.2.6,10.2.7,10.3.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6;  | 
| [ams-nist-rds-enhanced-monitoring-enabled](https://docs.aws.amazon.com/config/latest/developerguide/rds-enhanced-monitoring-enabled.html) | RDS | Config Changes | Report | CIS: NA; NIST-CSF: PR.PT-1; HIPAA: 164.312(b); PCI: NA;  | 
| [ams-nist-cis-rds-instance-public-access-check](https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html) | RDS | Config Changes | Report | CIS: CIS.12,CIS.14,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-rds-multi-az-support](https://docs.aws.amazon.com/config/latest/developerguide/rds-multi-az-support.html) | RDS | Config Changes | Report | CIS: NA; NIST-CSF: ID.BE-5,PR.DS-4,PR.PT-5,RC.RP-1; HIPAA: 164.308(a)(7)(i),164.308(a)(7)(ii)(C); PCI: NA;  | 
| [ams-nist-cis-rds-snapshots-public-prohibited](https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html) | RDS | Config Changes | Report | CIS: CIS.12,CIS.14,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-cis-rds-storage-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html) | RDS | Config Changes | Report | CIS: CIS.13,CIS.5,CIS.6; NIST-CSF: DE.AE-1,DE.AE-3,PR.DS-1,PR.PT-1; HIPAA: 164.312(a)(2)(iv),164.312(b),164.312(e)(2)(ii); PCI: 3.4,10.1,10.2.1,10.2.2,10.2.3,10.2.4,10.2.5,10.3.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6,8.2.1;  | 
| [ams-nist-cis-redshift-cluster-configuration-check](https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-configuration-check.html) | RedShift | Config Changes | Report | CIS: CIS.6,CIS.13,CIS.5; NIST-CSF: DE.AE-1,DE.AE-3,PR.DS-1,PR.PT-1; HIPAA: 164.312(a)(2)(iv),164.312(b),164.312(e)(2)(ii); PCI: 3.4,8.2.1,10.1,10.2.1,10.2.2,10.2.3,10.2.4,10.2.5,10.3.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6;  | 
| [ams-nist-cis-redshift-cluster-public-access-check](https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-public-access-check.html) | RedShift | Config Changes | Report | CIS: CIS.12,CIS.14,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-cis-redshift-require-tls-ssl](https://docs.aws.amazon.com/config/latest/developerguide/redshift-require-tls-ssl.html) | RedShift | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-2; HIPAA: 164.312(a)(2)(iv),164.312(e)(1),164.312(e)(2)(i),164.312(e)(2)(ii); PCI: 2.3,4.1;  | 
| [ams-nist-cis-root-account-hardware-mfa-enabled](https://docs.aws.amazon.com/config/latest/developerguide/root-account-hardware-mfa-enabled.html) | IAM | Periodic | Report | CIS: CIS.16,CIS.4; NIST-CSF: PR.AC-7; HIPAA: 164.312(d); PCI: 2.2,8.3;  | 
| [ams-nist-cis-root-account-mfa-enabled](https://docs.aws.amazon.com/config/latest/developerguide/root-account-mfa-enabled.html) | IAM | Periodic | Report | CIS: CIS.16,CIS.4; NIST-CSF: PR.AC-7; HIPAA: 164.312(d); PCI: 2.2,8.3;  | 
| [ams-nist-cis-s3-bucket-default-lock-enabled](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-default-lock-enabled.html) | S3 | Config Changes | Report | CIS: CIS.14,CIS.13; NIST-CSF: ID.BE-5,PR.PT-5,RC.RP-1; HIPAA: NA; PCI: NA;  | 
| [ams-nist-cis-s3-bucket-logging-enabled](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-logging-enabled.html) | S3 | Config Changes | Report | CIS: CIS.6; NIST-CSF: DE.AE-1,DE.AE-3,PR.DS-5,PR.PT-1; HIPAA: 164.308(a)(3)(ii)(A),164.312(b); PCI: 2.2,10.1,10.2.1,10.2.2,10.2.3,10.2.4,10.2.5,10.2.7,10.3.1,10.3.2,10.3.3,10.3.4,10.3.5,10.3.6;  | 
| [ams-nist-cis-s3-bucket-replication-enabled](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-replication-enabled.html) | S3 | Config Changes | Report | CIS: CIS.10; NIST-CSF: ID.BE-5,PR.DS-4,PR.IP-4,PR.PT-5,RC.RP-1; HIPAA: 164.308(a)(7)(i),164.308(a)(7)(ii)(A),164.308(a)(7)(ii)(B); PCI: 2.2,10.5.3;  | 
| [ams-nist-cis-s3-bucket-ssl-requests-only](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-ssl-requests-only.html) | S3 | Config Changes | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-2; HIPAA: 164.312(a)(2)(iv),164.312(c)(2),164.312(e)(1),164.312(e)(2)(i),164.312(e)(2)(ii); PCI: 2.2,4.1,8.2.1;  | 
| [ams-nist-cis-s3-bucket-versioning-enabled](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-versioning-enabled.html) | S3 | Periodic | Report | CIS: CIS.10; NIST-CSF: ID.BE-5,PR.DS-4,PR.DS-6,PR.IP-4,PR.PT-5,RC.RP-1; HIPAA: 164.308(a)(7)(i),164.308(a)(7)(ii)(A),164.308(a)(7)(ii)(B),164.312(c)(1),164.312(c)(2); PCI: 10.5.3;  | 
| [ams-nist-cis-sagemaker-endpoint-configuration-kms-key-configured](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-endpoint-configuration-kms-key-configured.html) | SageMaker | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4,8.2.1;  | 
| [ams-nist-cis-sagemaker-notebook-instance-kms-key-configured](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-endpoint-configuration-kms-key-configured.html) | SageMaker | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4,8.2.1;  | 
| [ams-nist-cis-sagemaker-notebook-no-direct-internet-access](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-no-direct-internet-access.html) | SageMaker | Periodic | Report | CIS: CIS.12,CIS.9; NIST-CSF: PR.AC-3,PR.AC-4,PR.AC-5,PR.DS-5,PR.PT-3,PR.PT-4; HIPAA: 164.308(a)(3)(i),164.308(a)(4)(ii)(A),164.308(a)(4)(ii)(C),164.312(a)(1),164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,1.3.4,1.3.6,2.2.2;  | 
| [ams-nist-cis-secretsmanager-rotation-enabled-check](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-rotation-enabled-check.html) | Secrets Manager | Config Changes | Report | CIS: CIS.16; NIST-CSF: PR.AC-1; HIPAA: 164.308(a)(4)(ii)(B); PCI: NA;  | 
| [ams-nist-cis-secretsmanager-scheduled-rotation-success-check](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-scheduled-rotation-success-check.html) | Secrets Manager | Config Changes | Report | CIS: CIS.16; NIST-CSF: PR.AC-1; HIPAA: 164.308(a)(4)(ii)(B); PCI: NA;  | 
| [ams-nist-cis-sns-encrypted-kms](https://docs.aws.amazon.com/config/latest/developerguide/sns-encrypted-kms.html) | SNS | Config Changes | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 8.2.1;  | 
| [ams-nist-cis-vpc-sg-open-only-to-authorized-ports](https://docs.aws.amazon.com/config/latest/developerguide/vpc-sg-open-only-to-authorized-ports.html) | VPC | Config Changes | Report | CIS: CIS.11,CIS.12,CIS.9; NIST-CSF: DE.AE-1,PR.AC-3,PR.AC-5,PR.PT-4; HIPAA: 164.312(e)(1); PCI: 1.2,1.3,1.2.1,1.3.1,1.3.2,2.2.2;  | 
| [ams-nist-vpc-vpn-2-tunnels-up](https://docs.aws.amazon.com/config/latest/developerguide/vpc-vpn-2-tunnels-up.html) | VPC | Config Changes | Report | CIS: NA; NIST-CSF: ID.BE-5,PR.DS-4,PR.PT-5,RC.RP-1; HIPAA: 164.308(a)(7)(i); PCI: NA;  | 
| [ams-cis-ec2-ebs-encryption-by-default](https://docs.aws.amazon.com/config/latest/developerguide/ec2-ebs-encryption-by-default.html) | EC2 | Periodic | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 2.2,3.4,8.2.1;  | 
| [ams-cis-rds-snapshot-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshot-encrypted.html) | RDS | Config Changes | Report | CIS: CIS.13,CIS.14; NIST-CSF: PR.DS-1; HIPAA: 164.312(a)(2)(iv),164.312(e)(2)(ii); PCI: 3.4,8.2.1;  | 
| [ams-cis-redshift-cluster-maintenancesettings-check](https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-maintenancesettings-check.html) | RedShift | Config Changes | Report | CIS: CIS.5; NIST-CSF: PR.DS-4,PR.IP-1,PR.IP-4; HIPAA: 164.308(a)(5)(ii)(A),164.308(a)(7)(ii)(A); PCI: 6.2;  | 

## Responses to violations in Accelerate
<a name="acc-sec-compliance-responses"></a>

All Config Rule violations appear in your Configuration Report. This is a universal response. Depending on the *Remediation Category* (severity) of the rule, AMS might take additional actions, summarized in the following table. For details on how to customize the *Action Code* for certain rules, see [Customized findings responses](custom-findings-responses.md).

**Remediation Actions**


| Action Code | AMS Actions | 
| --- |--- |
| Report | 1. [Add to Config Report](#acc-sec-compliance-response-universal)  | 
| Incident | 1. [Add to Config Report](#acc-sec-compliance-response-universal) <br />2. [Automatic incident report in Accelerate](#acc-sec-compliance-response-incident)  | 
| Remediate | 1. [Add to Config Report](#acc-sec-compliance-response-universal) <br />2. [Automatic incident report in Accelerate](#acc-sec-compliance-response-incident)<br />3. [Automatic remediation in Accelerate](#acc-sec-compliance-response-autoremediate) | 

**Requesting Additional Help**

**Note**  
AMS can remediate any violation for you, regardless of its remediation category. To request help, submit a Service Request, and indicate which resources you want AMS to remediate with a comment such as "As part of the AMS config rule remediation, please remediate non-complaint resources {{RESOURCE\_ARNS\_OR\_IDs}}resource ARNs/IDs>, config rule {{CONFIG\_RULE\_NAME}}in the account" and add the required inputs to remediate the violation.

AMS Accelerate has a library of AWS Systems Manager automation documents and runbooks to assist in remediating noncompliant resources.

### Add to Config Report
<a name="acc-sec-compliance-response-universal"></a>

AMS generates a Config Report that tracks the compliance status of all rules and resources in your account. You can request the report from your CSDM. You can also review compliance status from the AWS Config console, AWS CLI, or AWS Config API. Your Config Report includes:
+ The top, noncompliant resources in your environment, to discover potential threats and misconfigurations
+ Compliance of resources and config rules over time
+ Config rule descriptions, severity of rules, and recommended remediation steps to fix noncompliant resources

 When any resource goes into a noncompliant state, the resource status (and rule status) becomes **Noncompliant** in your Config Report. If the rule belongs to the **Config Report Only** remediation category, by default, AMS takes no further action. You can always create a Service Request to request additional help or remediation from AMS. 

For more details, see [AWS Config Reporting](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/on-request-reporting.html#acc-report-config-control-compliance).

### Automatic incident report in Accelerate
<a name="acc-sec-compliance-response-incident"></a>

For moderately severe rule violations, AMS automatically creates an Incident Report to notify you that a resource has gone into a noncompliant state, and asks which actions you would like to be performed. You have the following options when responding to an incident:
+ Request that AMS remediate the noncompliant resources listed in the incident. Then, we attempt to remediate the noncompliant resource, and notify you once the underlying incident has been resolved.
+ You can resolve the noncompliant item manually in the console or through your automated deployment system (for example, CI/CD Pipeline template updates); then, you can resolve the incident. The noncompliant resource is re-evaluated as per the rule’s schedule and, if the resource is evaluated as noncompliant, a new incident report is created.
+ You can choose to not resolve the noncompliant resource and simply resolve the incident. If you update the configuration of the resource later, AWS Config will trigger a re-evaluation and you will again be alerted to evaluate the noncompliance of that resource. 

### Automatic remediation in Accelerate
<a name="acc-sec-compliance-response-autoremediate"></a>

 The most critical rules belong to the **Auto Remediate** category. Noncompliance with these rules may strongly impact the security and availability of your accounts. When a resource violates one of these rules: 

1. AMS automatically notifies you with an Incident Report.

1. AMS starts an automated remediation using our automated SSM documents.

1. AMS updates the Incident Report with success or failure of the automated remediation.

1. If automated remediation failed, an AMS engineer investigates the issue.

## Creating rule exceptions in Accelerate
<a name="acc-sec-compliance-config-reports-exception"></a>

The AWS Config Rules resource exception feature allows you to suppress reporting of specific, noncompliant resources for a specific rules.

**Note**  
The exempted resources still show up as **Noncompliant** in your AWS Config Service console. The exempted resources appear with a special flag in Config Reports (resource\_exception:True). Your CSDMs can filter out those resources according to that column when generating reports. 

If you have resources that you know are not compliant, you can eliminate a specific resource for a specific config rule in their Config Reports. To do this:

Submit a service request to Accelerate against your account, with a list of the config rules and resources that to be exempted from report. You must provide an explicit business justification (such as, no need to report that {{resource\_name\_1}} and {{resource\_name\_2}} are not backed up because we do not want them backed up). For help submitting an Accelerate service request, see [Creating a service request in Accelerate](creating-a-sr.md).

Paste into the request the following inputs (for every resource add a separate block with all the required fields, as shown), and then submit:

```
[
    {
        "resource_name": "{{resource_name_1}}",
        "config_rule_name": "{{config_rule_name_1}}",
        "business_justification": "{{REASON_TO_EXEMPT_RESOURCE}}",
        "resource_type": "{{resource_type}}"
    },
    {
        "resource_name": "{{resource_name_2}}",
        "config_rule_name": "{{config_rule_name_2}}",
        "business_justification": "{{REASON_TO_EXEMPT_RESOURCE}}",
        "resource_type": "{{resource_type}}"
    }
]
```

## Reduce AWS Config costs in Accelerate
<a name="acc-sec-compliance-reduct-config-spend"></a>

You can reduce AWS Config costs by using the option to periodically record the `AWS::EC2::Instance` resource type. Periodic recording captures the latest configuration changes of your resources once every 24 hours, reducing the number of changes delivered. When enabled, AWS Config only records the latest configuration of a resource at the end of a 24-hour period. This allows you to tailor configuration data to specific operational planning, compliance, and audit uses cases that don’t require continuous monitoring. This change is recommended only if you have applications that depend on ephemeral architectures, meaning you constantly scale the number of instances up or down. 

To opt in to periodic recording for the `AWS::EC2::Instance` resource type, contact your AMS Delivery Team.