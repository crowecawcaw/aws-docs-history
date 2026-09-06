

# Operational Best Practices for NZISM 3.9 (Foundation)
<a name="operational-best-practices-for-nzism-foundation"></a>

Conformance packs provide a general-purpose compliance framework designed to enable you to create security, operational or cost-optimization governance checks using managed or custom AWS Config rules and AWS Config remediation actions. Conformance Packs, as sample templates, are not designed to fully ensure compliance with a specific governance or compliance standard. You are responsible for making your own assessment of whether your use of the Services meets applicable legal and regulatory requirements.

The following provides a sample mapping between the [New Zealand Government Communications Security Bureau (GCSB) Information Security Manual (NZISM) 2025-11 Version 3.9](https://www.nzism.gcsb.govt.nz/ism-document) and AWS Managed Config rules. Each Config rule applies to a specific AWS resource type, and relates to one or more NZISM controls. An NZISM control can be related to multiple Config rules. Refer to the table below for more detail and guidance related to these mappings. Only controls representing recommended or baseline practice for information classified RESTRICTED and below are included in the mappings.

This sample conformance pack template contains mappings to controls within the NZISM framework, which is an integral part of the Protective Security Requirements (PSR) framework that sets out the New Zealand Government’s expectations for the management of personnel, information and physical security.

The Foundation part of this conformance pack can be deployed to the Sydney and global regions. The NZ Transition part contains the subset of Foundation Config rules that are currently available in the New Zealand region. The Foundation part will not currently deploy to the New Zealand region. The Extension part of this conformance pack can be deployed to the Sydney and New Zealand regions in order to augment the Config rules provided in the Foundation and NZ Transition parts.

The NZISM is licensed under the Creative Commons Attribution 4.0 New Zealand licence, available at [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/). Copyright information can be found at [NZISM New Zealand Information Security Manual \| Legal, Privacy, and Copyright](https://www.nzism.gcsb.govt.nz/legal-privacy-and-copyright/).



| Control ID  | Control Description  | AWS Config Rule  | Guidance  | 
| --- | --- | --- | --- | 
| 1149 | Software security, Standard Operating Environments, Developing hardened SOEs (14.1.8.C.01.) | [ec2-instance-managed-by-systems-manager](ec2-instance-managed-by-systems-manager.md) | An inventory of the software platforms and applications within the organization is possible by managing Amazon Elastic Compute Cloud (Amazon EC2) instances with AWS Systems Manager. Use AWS Systems Manager to provide detailed system configurations, operating system patch levels, services name and type, software installations, application name, publisher and version, and other details about your environment. | 
| 1149 | Software security, Standard Operating Environments, Developing hardened SOEs (14.1.8.C.01.) | [ec2-managedinstance-association-compliance-status-check](ec2-managedinstance-association-compliance-status-check.md) | Use AWS Systems Manager Associations to help with inventory of software platforms and applications within an organization. AWS Systems Manager assigns a configuration state to your managed instances and allows you to set baselines of operating system patch levels, software installations, application configurations, and other details about your environment. | 
| 1149 | Software security, Standard Operating Environments, Developing hardened SOEs (14.1.8.C.01.) | [ecs-containers-nonprivileged](ecs-containers-nonprivileged.md) | This control checks if the privileged parameter in the container definition of Amazon ECS Task Definitions is set to true. The control fails if this parameter is equal to true. This control only evaluates the latest active revision of an Amazon ECS task definition. We recommend that you remove elevated privileges from your ECS task definitions. When the privilege parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). | 
| 1149 | Software security, Standard Operating Environments, Developing hardened SOEs (14.1.8.C.01.) | [ecs-containers-readonly-access](ecs-containers-readonly-access.md) | This control checks if Amazon ECS containers are limited to read-only access to mounted root filesystems. This control fails if the ReadonlyRootFilesystem parameter in the container definition of Amazon ECS task definitions is set to false. This control only evaluates the latest active revision of an Amazon ECS task definition. Enabling this option reduces security attack vectors since the container instance's filesystem cannot be tampered with or written to unless it has explicit read-write permissions on its filesystem folder and directories. This control also adheres to the principle of least privilege. | 
| 1154 | Information Security Incidents, Detecting Information Security Incidents, Preventing and detecting information security incidents (7.1.7.C.02.) | [guardduty-runtime-monitoring-enabled](guardduty-runtime-monitoring-enabled.md) | This control checks if Runtime Monitoring is enabled for Amazon GuardDuty in your account or organization. Runtime Monitoring observes and analyzes operating system-level, networking, and file events to help you detect potential threats in specific AWS workloads in your environment. | 
| 1661 | Software security, Web Application Development, Agency website content (14.5.6.C.01.) | [cloudfront-default-root-object-configured](cloudfront-default-root-object-configured.md) | This control checks whether an Amazon CloudFront distribution is configured to return a specific object, that is the default root object. The control fails if the CloudFront distribution does not have a default root object configured. A user might sometimes request the distribution's root URL instead of an object in the distribution. When this happens, specifying a default root object can help you to avoid exposing the contents of your web distribution. This rule must be applied in the us-east-1 region. Deploy with template parameter DeployEdgeRules = true. | 
| 1667 | Software security, Web Application Development, Web applications (14.5.8.C.01.) | [acm-certificate-expiration-check](acm-certificate-expiration-check.md) | Ensure network integrity is protected by ensuring X509 certificates are issued by AWS ACM. These certificates must be valid and unexpired. This rule requires a value for daysToExpiration. The value is 90 days. | 
| 1667 | Software security, Web Application Development, Web applications (14.5.8.C.01.) | [elb-tls-https-listeners-only](elb-tls-https-listeners-only.md) | Ensure that your Elastic Load Balancers (ELBs) are configured with SSL or HTTPS listeners. Because sensitive data can exist, enable encryption in transit to help protect that data. | 
| 1841 | Access Control and Passwords, Identification, Authentication and Passwords, Methods for system user identification and authentication (16.1.35.C.02.) | [iam-user-mfa-enabled](iam-user-mfa-enabled.md) | Enable this rule to restrict access to resources in the AWS Cloud. This rule ensures multi-factor authentication (MFA) is enabled for all IAM users. MFA adds an extra layer of protection on top of a user name and password. Reduce the incidents of compromised accounts by requiring MFA for IAM users. | 
| 1841 | Access Control and Passwords, Identification, Authentication and Passwords, Methods for system user identification and authentication (16.1.35.C.02.) | [mfa-enabled-for-iam-console-access](mfa-enabled-for-iam-console-access.md) | Manage access to resources in the AWS Cloud by ensuring that multi-factor authentication (MFA) is enabled for all AWS Identity and Access Management (IAM) users that have a console password. MFA adds an extra layer of protection on top of a user name and password. By requiring MFA for IAM users, you can reduce incidents of compromised accounts and keep sensitive data from being accessed by unauthorized users. | 
| 1841 | Access Control and Passwords, Identification, Authentication and Passwords, Methods for system user identification and authentication (16.1.35.C.02.) | [root-account-hardware-mfa-enabled](root-account-hardware-mfa-enabled.md) | Manage access to resources in the AWS Cloud by ensuring hardware multi-factor authentication (MFA) is enabled for the root user. The root user is the most privileged user in an AWS account. The MFA adds an extra layer of protection for a user name and password. By requiring MFA for the root user, you can reduce the incidents of compromised AWS accounts. | 
| 1841 | Access Control and Passwords, Identification, Authentication and Passwords, Methods for system user identification and authentication (16.1.35.C.02.) | [root-account-mfa-enabled](root-account-mfa-enabled.md) | Manage access to resources in the AWS Cloud by ensuring multi-factor authentication (MFA) is enabled for the root user. The root user is the most privileged user in an AWS account. The MFA adds an extra layer of protection for a user name and password. By requiring MFA for the root user, you can reduce the incidents of compromised AWS accounts. | 
| 1847 | Access Control and Passwords, Identification, Authentication and Passwords, Protecting authentication data in transit (16.1.37.C.01.) | [alb-http-to-https-redirection-check](alb-http-to-https-redirection-check.md) | To help protect data in transit, ensure that your Application Load Balancer automatically redirects unencrypted HTTP requests to HTTPS. Because sensitive data can exist, enable encryption in transit to help protect that data. | 
| 1847 | Access Control and Passwords, Identification, Authentication and Passwords, Protecting authentication data in transit (16.1.37.C.01.) | [cloudfront-viewer-policy-https](cloudfront-viewer-policy-https.md) | This control checks whether an Amazon CloudFront distribution requires viewers to use HTTPS directly or whether it uses redirection. The control fails if ViewerProtocolPolicy is set to allow-all for defaultCacheBehavior or for cacheBehaviors. HTTPS (TLS) can be used to help prevent potential attackers from using person-in-the-middle or similar attacks to eavesdrop on or manipulate network traffic. Only encrypted connections over HTTPS (TLS) should be allowed. This rule must be applied in the us-east-1 region. Deploy with template parameter DeployEdgeRules = true. | 
| 1847 | Access Control and Passwords, Identification, Authentication and Passwords, Protecting authentication data in transit (16.1.37.C.01.) | [elasticsearch-node-to-node-encryption-check](elasticsearch-node-to-node-encryption-check.md) | This control checks whether Elasticsearch domains have node-to-node encryption enabled. This control fails if node-to-node encryption is disabled on the domain. HTTPS (TLS) can be used to help prevent potential attackers from eavesdropping on or manipulating network traffic using person-in-the-middle or similar attacks. Only encrypted connections over HTTPS (TLS) should be allowed. Enabling node-to-node encryption for Elasticsearch domains ensures that intra-cluster communications are encrypted in transit. | 
| 1847 | Access Control and Passwords, Identification, Authentication and Passwords, Protecting authentication data in transit (16.1.37.C.01.) | [elb-tls-https-listeners-only](elb-tls-https-listeners-only.md) | Ensure that your Elastic Load Balancers (ELBs) are configured with SSL or HTTPS listeners. Because sensitive data can exist, enable encryption in transit to help protect that data. | 
| 1847 | Access Control and Passwords, Identification, Authentication and Passwords, Protecting authentication data in transit (16.1.37.C.01.) | [opensearch-node-to-node-encryption-check](opensearch-node-to-node-encryption-check.md) | This control checks whether OpenSearch domains have node-to-node encryption enabled. This control fails if node-to-node encryption is disabled on the domain. HTTPS (TLS) can be used to help prevent potential attackers from eavesdropping on or manipulating network traffic using person-in-the-middle or similar attacks. Only encrypted connections over HTTPS (TLS) should be allowed. Enabling node-to-node encryption for OpenSearch domains ensures that intra-cluster communications are encrypted in transit. | 
| 1893 | Access Control and Passwords, Identification, Authentication and Passwords, Suspension of access (16.1.46.C.02.) | [iam-user-unused-credentials-check](iam-user-unused-credentials-check.md) | AWS Identity and Access Management (IAM) can help you with access permissions and authorizations by checking for IAM passwords and access keys that are not used for a specified time period. If these unused credentials are identified, you should disable and/or remove the credentials, as this may violate the principle of least privilege. This rule sets maxCredentialUsageAge to 30 days. | 
| 1946 | Access Control and Passwords, Privileged User Access, Use of privileged accounts (16.3.5.C.02.) | [iam-policy-no-statements-with-admin-access](iam-policy-no-statements-with-admin-access.md) | AWS Identity and Access Management (IAM) can help you incorporate the principles of least privilege and separation of duties with access permissions and authorizations, restricting policies from containing "Effect": "Allow" with "Action": "\*" over "Resource": "\*". Allowing users to have more privileges than needed to complete a task may violate the principle of least privilege and separation of duties. | 
| 1946 | Access Control and Passwords, Privileged User Access, Use of privileged accounts (16.3.5.C.02.) | [iam-root-access-key-check](iam-root-access-key-check.md) | Access to systems and assets can be controlled by checking that the root user does not have access keys attached to their AWS Identity and Access Management (IAM) role. Ensure that the root access keys are deleted. Instead, create and use role-based AWS accounts to help to incorporate the principle of least functionality. | 
| 1998 | Access Control and Passwords, Event Logging and Auditing, Maintaining system management logs (16.6.6.C.02.) | [cloud-trail-cloud-watch-logs-enabled](cloud-trail-cloud-watch-logs-enabled.md) | You should configure CloudTrail with CloudWatch Logs to monitor your trail logs and be notified when specific activity occurs. This rule checks whether AWS CloudTrail trails are configured to send logs to Amazon CloudWatch logs. | 
| 1998 | Access Control and Passwords, Event Logging and Auditing, Maintaining system management logs (16.6.6.C.02.) | [cloudtrail-enabled](cloudtrail-enabled.md) | AWS CloudTrail can help in non-repudiation by recording AWS Management Console actions and API calls. You can identify the users and AWS accounts that called an AWS service, the source IP address where the calls generated, and the timings of the calls. Details of captured data are seen within AWS CloudTrail Record Contents. | 
| 1998 | Access Control and Passwords, Event Logging and Auditing, Maintaining system management logs (16.6.6.C.02.) | [cw-loggroup-retention-period-check](cw-loggroup-retention-period-check.md) | Ensure a minimum duration of event log data is retained for your log groups to help with troubleshooting and forensics investigations. The lack of available past event log data makes it difficult to reconstruct and identify potentially malicious events. The minimum retention is 18 months. | 
| 2013 | Access Control and Passwords, Event Logging and Auditing, Additional events to be logged (16.6.10.C.02.) | [api-gw-execution-logging-enabled](api-gw-execution-logging-enabled.md) | API Gateway logging displays detailed views of users who accessed the API and the way they accessed the API. This insight enables visibility of user activities. | 
| 2013 | Access Control and Passwords, Event Logging and Auditing, Additional events to be logged (16.6.10.C.02.) | [cloudfront-accesslogs-enabled](cloudfront-accesslogs-enabled.md) | This control checks whether server access logging is enabled on CloudFront distributions. The control fails if access logging is not enabled for a distribution. CloudFront access logs provide detailed information about every user request that CloudFront receives. Each log contains information such as the date and time the request was received, the IP address of the viewer that made the request, the source of the request, and the port number of the request from the viewer. These logs are useful for applications such as security and access audits and forensics investigation. This rule must be applied in the us-east-1 region. Deploy with template parameter DeployEdgeRules = true | 
| 2013 | Access Control and Passwords, Event Logging and Auditing, Additional events to be logged (16.6.10.C.02.) | [cloudtrail-enabled](cloudtrail-enabled.md) | AWS CloudTrail can help in non-repudiation by recording AWS Management Console actions and API calls. You can identify the users and AWS accounts that called an AWS service, the source IP address where the calls generated, and the timings of the calls. Details of captured data are seen within AWS CloudTrail Record Contents. | 
| 2013 | Access Control and Passwords, Event Logging and Auditing, Additional events to be logged (16.6.10.C.02.) | [elb-logging-enabled](elb-logging-enabled.md) | Elastic Load Balancing activity is a central point of communication within an environment. Ensure ELB logging is enabled. The collected data provides detailed information about requests sent to the ELB. Each log contains information such as the time the request was received, the client's IP address, latencies, request paths, and server responses. | 
| 2013 | Access Control and Passwords, Event Logging and Auditing, Additional events to be logged (16.6.10.C.02.) | [rds-logging-enabled](rds-logging-enabled.md) | To help with logging and monitoring within your environment, ensure Amazon Relational Database Service (RDS) logging is enabled. With Amazon RDS logging, you can capture events such as connections, disconnections, queries, or tables queried. | 
| 2013 | Access Control and Passwords, Event Logging and Auditing, Additional events to be logged (16.6.10.C.02.) | [wafv2-logging-enabled](wafv2-logging-enabled.md) | To help with logging and monitoring within your environment, enable AWS WAF (V2) logging on regional and global web ACLs. AWS WAF logging provides detailed information about the traffic that is analyzed by your web ACL. The logs record the time that AWS WAF received the request from your AWS resource, information about the request, and an action for the rule that each request matched. | 
| 2022 | Access Control and Passwords, Event Logging and Auditing, Event log protection (16.6.12.C.01.) | [cloud-trail-log-file-validation-enabled](cloud-trail-log-file-validation-enabled.md) | Utilize AWS CloudTrail log file validation to check the integrity of CloudTrail logs. Log file validation helps determine if a log file was modified or deleted or unchanged after CloudTrail delivered it. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection. | 
| 2022 | Access Control and Passwords, Event Logging and Auditing, Event log protection (16.6.12.C.01.) | [cloudwatch-log-group-encrypted](cloudwatch-log-group-encrypted.md) | To help protect sensitive data at rest, ensure encryption is enabled for your Amazon CloudWatch Log Groups. | 
| 2028 | Access Control and Passwords, Event Logging and Auditing, Event log archives (16.6.13.C.01.) | [cw-loggroup-retention-period-check](cw-loggroup-retention-period-check.md) | Ensure a minimum duration of event log data is retained for your log groups to help with troubleshooting and forensics investigations. The lack of available past event log data makes it difficult to reconstruct and identify potentially malicious events. The minimum retention is 18 months. | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [cloud-trail-encryption-enabled](cloud-trail-encryption-enabled.md) | Because sensitive data may exist and to help protect data at rest, ensure encryption is enabled for your AWS CloudTrail trails. | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [ec2-ebs-encryption-by-default](ec2-ebs-encryption-by-default.md) | To help protect data at rest, ensure that encryption is enabled for your Amazon Elastic Block Store (EBS) volumes. Because sensitive data can exist at rest in these volumes, enable encryption at rest to help protect that data. | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [efs-encrypted-check](efs-encrypted-check.md) | Because sensitive data can exist and to help protect data at rest, ensure encryption is enabled for your Amazon Elastic File System (EFS). | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [elasticsearch-encrypted-at-rest](elasticsearch-encrypted-at-rest.md) | This control checks whether Elasticsearch domains have encryption-at-rest configuration enabled. The check fails if encryption at rest is not enabled. For an added layer of security for sensitive data, you should configure your Elasticsearch Service domain to be encrypted at rest. When you configure encryption of data at rest, Amazon Key Management Service (KMS) stores and manages your encryption keys. To perform the encryption, AWS KMS uses the Advanced Encryption Standard algorithm with 256-bit keys (AES-256). | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [encrypted-volumes](encrypted-volumes.md) | Because senstive data can exist and to help protect data at rest, ensure encryption is enabled for your Amazon Elastic Block Store (EBS) volumes. | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [opensearch-encrypted-at-rest](opensearch-encrypted-at-rest.md) | This control checks whether OpenSearch domains have encryption-at-rest configuration enabled. The check fails if encryption at rest is not enabled. For an added layer of security for sensitive data, you should configure your OpenSearch Service domain to be encrypted at rest. When you configure encryption of data at rest, Amazon Key Management Service (KMS) stores and manages your encryption keys. To perform the encryption, AWS KMS uses the Advanced Encryption Standard algorithm with 256-bit keys (AES-256). | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [rds-snapshot-encrypted](rds-snapshot-encrypted.md) | Ensure that encryption is enabled for your Amazon Relational Database Service (RDS) snapshots. Because sensitive data can exist at rest, enable encryption at rest to help protect that data. | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [rds-storage-encrypted](rds-storage-encrypted.md) | To help protect data at rest, ensure that encryption is enabled for your Amazon Relational Database Service (RDS) instances. Because sensitive data can exist at rest in Amazon RDS instances, enable encryption at rest to help protect that data. | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [s3-bucket-server-side-encryption-enabled](s3-bucket-server-side-encryption-enabled.md) | To help protect data at rest, ensure encryption is enabled for your Amazon Simple Storage Service (Amazon S3) buckets. Because sensitive data can exist at rest in Amazon S3 buckets, enable encryption to help protect that data. | 
| 2090 | Cryptography, Cryptographic Fundamentals, Information and Systems Protection (17.1.55.C.02.) | [alb-http-to-https-redirection-check](alb-http-to-https-redirection-check.md) | To help protect data in transit, ensure that your Application Load Balancer automatically redirects unencrypted HTTP requests to HTTPS. Because sensitive data can exist, enable encryption in transit to help protect that data. | 
| 2090 | Cryptography, Cryptographic Fundamentals, Information and Systems Protection (17.1.55.C.02.) | [elb-tls-https-listeners-only](elb-tls-https-listeners-only.md) | Ensure that your Elastic Load Balancers (ELBs) are configured with SSL or HTTPS listeners. Because sensitive data can exist, enable encryption in transit to help protect that data. | 
| 2090 | Cryptography, Cryptographic Fundamentals, Information and Systems Protection (17.1.55.C.02.) | [redshift-require-tls-ssl](redshift-require-tls-ssl.md) | Ensure that your Amazon Redshift clusters require TLS/SSL encryption to connect to SQL clients. Because sensitive data can exist, enable encryption in transit to help protect that data. | 
| 2598 | Cryptography, Transport Layer Security, Using TLS (17.4.16.C.01.) | [elb-custom-security-policy-ssl-check](elb-custom-security-policy-ssl-check.md) | To help protect data in transit, ensure that your Classic ElasticLoadBalancer SSL listeners are using a custom security policy. These policies can provide various high-strength cryptographic algorithms to help ensure encrypted network communications between systems. This rule requires that you set a custom security policy for your SSL listeners. The security policy is: Protocol-TLSv1.2,ECDHE-ECDSA-AES128-GCM-SHA256. | 
| 2600 | Cryptography, Transport Layer Security, Using TLS (17.4.16.C.02.) | [elb-custom-security-policy-ssl-check](elb-custom-security-policy-ssl-check.md) | To help protect data in transit, ensure that your Classic ElasticLoadBalancer SSL listeners are using a custom security policy. These policies can provide various high-strength cryptographic algorithms to help ensure encrypted network communications between systems. This rule requires that you set a custom security policy for your SSL listeners. The default security policy is: Protocol-TLSv1.2,ECDHE-ECDSA-AES128-GCM-SHA256. | 
| 2726 | Cryptography, Secure Shell, Automated remote access (17.5.8.C.02.) | [restricted-ssh](restricted-ssh.md) | Amazon Elastic Compute Cloud (Amazon EC2) Security Groups can help manage network access by providing stateful filtering of ingress and egress network traffic to AWS resources. Not allowing ingress (or remote) traffic from 0.0.0.0/0 to port 22 on your resources help you restricting remote access. | 
| 3021 | Cryptography, Key Management, Contents of KMPs (17.9.25.C.01.) | [cmk-backing-key-rotation-enabled](cmk-backing-key-rotation-enabled.md) | Amazon Key Management Service (KMS) enables customers to rotate the backing key, which is key material stored in AWS KMS and is tied to the key ID of the customer managed key (CMK). It's the backing key that is used to perform cryptographic operations such as encryption and decryption. Automated key rotation currently retains all previous backing keys so that decryption of encrypted data can take place transparently. Rotating encryption keys helps reduce the potential impact of a compromised key because data encrypted with a new key can't be accessed with a previous key that might have been exposed. | 
| 3205 | Network security, Network Management, Limiting network access (18.1.13.C.02.) | [vpc-sg-open-only-to-authorized-ports](vpc-sg-open-only-to-authorized-ports.md) | Manage access to resources in the AWS Cloud by ensuring common ports are restricted on Amazon Elastic Compute Cloud (Amazon EC2) Security Groups. Not restricting access on ports to trusted sources can lead to attacks against the availability, integrity and confidentiality of systems. By restricting access to resources within a security group from the internet (0.0.0.0/0) remote access can be controlled to internal systems. The authorized Internet port list is: 443 only | 
| 3449 | Product Security, Product Patching and Updating, Patching vulnerabilities in products (12.4.4.C.02.) | [ec2-managedinstance-patch-compliance-status-check](ec2-managedinstance-patch-compliance-status-check.md) | Enable rule to help with identification and documentation of Amazon Elastic Compute Cloud (Amazon EC2) vulnerabilities. The rule checks if Amazon EC2 instance patch compliance in AWS Systems Manager as required by your organisation's policies and procedures. | 
| 3449 | Product Security, Product Patching and Updating, Patching vulnerabilities in products (12.4.4.C.02.) | [ecr-private-image-scanning-enabled](ecr-private-image-scanning-enabled.md) | This control checks whether a private Amazon Elastic Container Registry (ECR) repository has image scanning configured. This control fails if a private ECR repository doesn't have image scanning configured. Note that you must also configure scan on push for each repository to pass this control. ECR image scanning helps in identifying software vulnerabilities in your container images. ECR uses the Common Vulnerabilities and Exposures (CVEs) database from the open-source Clair project and provides a list of scan findings. Enabling image scanning on ECR repositories adds a layer of verification for the integrity and safety of the images being stored. | 
| 3449 | Product Security, Product Patching and Updating, Patching vulnerabilities in products (12.4.4.C.02.) | [redshift-cluster-maintenancesettings-check](redshift-cluster-maintenancesettings-check.md) | This rule ensures that Amazon Redshift clusters have the preferred settings for your organization. Specifically, that they have preferred maintenance windows and automated snapshot retention periods for the database. This rule sets allowVersionUpgrade to true. | 
| 3451 | Product Security, Product Patching and Updating, Patching vulnerabilities in products (12.4.4.C.04.) | [ec2-managedinstance-patch-compliance-status-check](ec2-managedinstance-patch-compliance-status-check.md) | Enable rule to help with identification and documentation of Amazon Elastic Compute Cloud (Amazon EC2) vulnerabilities. The rule checks if Amazon EC2 instance patch compliance in AWS Systems Manager as required by your organisation's policies and procedures. | 
| 3452 | Product Security, Product Patching and Updating, Patching vulnerabilities in products (12.4.4.C.05.) | [ec2-managedinstance-patch-compliance-status-check](ec2-managedinstance-patch-compliance-status-check.md) | Enable rule to help with identification and documentation of Amazon Elastic Compute Cloud (Amazon EC2) vulnerabilities. The rule checks if Amazon EC2 instance patch compliance in AWS Systems Manager as required by your organisation's policies and procedures. | 
| 3452 | Product Security, Product Patching and Updating, Patching vulnerabilities in products (12.4.4.C.05.) | [elastic-beanstalk-managed-updates-enabled](elastic-beanstalk-managed-updates-enabled.md) | This control checks whether managed platform updates are enabled for the Elastic Beanstalk environment. Enabling managed platform updates ensures that the latest available platform fixes, updates, and features for the environment are installed. Keeping up to date with patch installation is an important step in securing systems. | 
| 3452 | Product Security, Product Patching and Updating, Patching vulnerabilities in products (12.4.4.C.05.) | [rds-automatic-minor-version-upgrade-enabled](rds-automatic-minor-version-upgrade-enabled.md) | This control checks whether automatic minor version upgrades are enabled for the Amazon Relational Database Service (RDS) database instance. Enabling automatic minor version upgrades ensures that the latest minor version updates to the relational database management system (RDBMS) are installed. These upgrades might include security patches and bug fixes. Keeping up to date with patch installation is an important step in securing systems. | 
| 3453 | Product Security, Product Patching and Updating, Patching vulnerabilities in products (12.4.4.C.06.) | [ec2-managedinstance-patch-compliance-status-check](ec2-managedinstance-patch-compliance-status-check.md) | Enable rule to help with identification and documentation of Amazon Elastic Compute Cloud (Amazon EC2) vulnerabilities. The rule checks if Amazon EC2 instance patch compliance in AWS Systems Manager as required by your organisation's policies and procedures. | 
| 3453 | Product Security, Product Patching and Updating, Patching vulnerabilities in products (12.4.4.C.06.) | [redshift-cluster-maintenancesettings-check](redshift-cluster-maintenancesettings-check.md) | This rule ensures that Amazon Redshift clusters have the preferred settings for your organization. Specifically, that they have preferred maintenance windows and automated snapshot retention periods for the database. This rule sets allowVersionUpgrade to true. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [cloudfront-associated-with-waf](cloudfront-associated-with-waf.md) | This control checks whether CloudFront distributions are associated with either AWS WAF or AWS WAFv2 web ACLs. The control fails if the distribution is not associated with a web ACL. AWS WAF is a web application firewall that helps protect web applications and APIs from attacks. It allows you to configure a set of rules, called a web access control list (web ACL), that allow, block, or count web requests based on customizable web security rules and conditions that you define. Ensure your CloudFront distribution is associated with an AWS WAF web ACL to help protect it from malicious attacks. This rule must be applied in the us-east-1 region. Deploy with template parameter DeployEdgeRules = true. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [dms-replication-not-public](dms-replication-not-public.md) | Manage access to the AWS Cloud by ensuring AWS Database Migration Service (DMS) replication instances cannot be publicly accessed. DMS replication instances can contain sensitive information and access control is required for such accounts. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [ec2-imdsv2-check](ec2-imdsv2-check.md) | Ensure the Instance Metadata Service Version 2 (IMDSv2) method is enabled to help protect access and control of Amazon Elastic Compute Cloud (Amazon EC2) instance metadata. The IMDSv2 method uses session-based controls. With IMDSv2, controls can be implemented to restrict changes to instance metadata. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [ec2-instance-no-public-ip](ec2-instance-no-public-ip.md) | Manage access to the AWS Cloud by ensuring Amazon Elastic Compute Cloud (Amazon EC2) instances cannot be publicly accessed. Amazon EC2 instances can contain sensitive information and access control is required for such accounts. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [ec2-instances-in-vpc](ec2-instances-in-vpc.md) | Deploy Amazon Elastic Compute Cloud (Amazon EC2) instances within an Amazon Virtual Private Cloud (Amazon VPC) to enable secure communication between an instance and other services within the Amazon VPC, without requiring an internet gateway, NAT device, or VPN connection. All traffic remains securely within the AWS Cloud. Because of their logical isolation, domains that reside within an Amazon VPC have an extra layer of security when compared to domains that use public endpoints. Assign Amazon EC2 instances to an Amazon VPC to properly manage access. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [elasticsearch-in-vpc-only](elasticsearch-in-vpc-only.md) | This control checks whether Elasticsearch domains are in a virtual private cloud (VPC). It does not evaluate the VPC subnet routing configuration to determine public access. You should ensure that Elasticsearch domains are not attached to public subnets. Elasticsearch domains deployed within a VPC can communicate with VPC resources over the private AWS network, without the need to traverse the public internet. This configuration increases the security posture by limiting access to the data in transit. VPCs provide a number of network controls to secure access to Elasticsearch domains, including network ACL and security groups | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [emr-master-no-public-ip](emr-master-no-public-ip.md) | Manage access to the AWS Cloud by ensuring Amazon Elastic MapReduce (EMR) cluster master nodes cannot be publicly accessed. Amazon EMR cluster master nodes can contain sensitive information and access control is required for such accounts. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [guardduty-enabled-centralized](guardduty-enabled-centralized.md) | Amazon GuardDuty can help to monitor and detect potential cybersecurity events by using threat intelligence feeds. These include lists of malicious IPs and machine learning to identify unexpected, unauthorized, and malicious activity within your AWS Cloud environment. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [lambda-function-public-access-prohibited](lambda-function-public-access-prohibited.md) | Manage access to resources in the AWS Cloud by ensuring AWS Lambda functions cannot be publicly accessed. Public access can potentially lead to degradation of availability of resources. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [opensearch-in-vpc-only](opensearch-in-vpc-only.md) | This control checks whether OpenSearch domains are in a virtual private cloud (VPC). It does not evaluate the VPC subnet routing configuration to determine public access. You should ensure that OpenSearch domains are not attached to public subnets. OpenSearch domains deployed within a VPC can communicate with VPC resources over the private AWS network, without the need to traverse the public internet. This configuration increases the security posture by limiting access to the data in transit. VPCs provide a number of network controls to secure access to OpenSearch domains, including network ACL and security groups. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [rds-instance-public-access-check](rds-instance-public-access-check.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Relational Database Service (RDS) instances are not public. Amazon RDS database instances can contain sensitive information, and principles and access control is required for such accounts. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [redshift-cluster-public-access-check](redshift-cluster-public-access-check.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Redshift clusters are not public. Amazon Redshift clusters can contain sensitive information and principles and access control is required for such accounts. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [s3-account-level-public-access-blocks-periodic](s3-account-level-public-access-blocks-periodic.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Simple Storage Service (Amazon S3) buckets cannot be publicly accessed. This rule helps keeping sensitive data safe from unauthorized remote users by preventing public access. This rule sets ignorePublicAcls to True, blockPublicPolicy to True, blockPublicAcls to True, and restrictPublicBuckets to True. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [sagemaker-notebook-no-direct-internet-access](sagemaker-notebook-no-direct-internet-access.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon SageMaker notebooks do not allow direct internet access. By preventing direct internet access, you can keep sensitive data from being accessed by unauthorized users. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [vpc-default-security-group-closed](vpc-default-security-group-closed.md) | Amazon Elastic Compute Cloud (Amazon EC2) security groups can help in the management of network access by providing stateful filtering of ingress and egress network traffic to AWS resources. Restricting all the traffic on the default security group helps in restricting remote access to your AWS resources. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [vpc-flow-logs-enabled](vpc-flow-logs-enabled.md) | The virtual private cloud (VPC) flow logs provide detailed records for information about the IP traffic going to and from network interfaces in your Amazon Virtual Private Cloud (Amazon VPC). By default, the flow log record includes values for the different components of the IP flow, including the source, destination, and protocol. | 
| 3623 | Gateway security, Gateways, Demilitarised zones (19.1.14.C.02.) | [elasticsearch-in-vpc-only](elasticsearch-in-vpc-only.md) | This control checks whether Elasticsearch domains are in a virtual private cloud (VPC). It does not evaluate the VPC subnet routing configuration to determine public access. You should ensure that Elasticsearch domains are not attached to public subnets. Elasticsearch domains deployed within a VPC can communicate with VPC resources over the private AWS network, without the need to traverse the public internet. This configuration increases the security posture by limiting access to the data in transit. VPCs provide a number of network controls to secure access to Elasticsearch domains, including network ACL and security groups. | 
| 3623 | Gateway security, Gateways, Demilitarised zones (19.1.14.C.02.) | [opensearch-in-vpc-only](opensearch-in-vpc-only.md) | This control checks whether OpenSearch domains are in a virtual private cloud (VPC). It does not evaluate the VPC subnet routing configuration to determine public access. You should ensure that OpenSearch domains are not attached to public subnets. OpenSearch domains deployed within a VPC can communicate with VPC resources over the private AWS network, without the need to traverse the public internet. This configuration increases the security posture by limiting access to the data in transit. VPCs provide a number of network controls to secure access to OpenSearch domains, including network ACL and security groups. | 
| 3623 | Gateway security, Gateways, Demilitarised zones (19.1.14.C.02.) | [rds-instance-public-access-check](rds-instance-public-access-check.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Relational Database Service (RDS) instances are not public. Amazon RDS database instances can contain sensitive information, and principles and access control is required for such accounts. | 
| 3623 | Gateway security, Gateways, Demilitarised zones (19.1.14.C.02.) | [redshift-cluster-public-access-check](redshift-cluster-public-access-check.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Redshift clusters are not public. Amazon Redshift clusters can contain sensitive information and principles and access control is required for such accounts. | 
| 3815 | Network security, Intrusion Detection and Prevention, IDS/IPS Maintenance (18.4.9.C.01.) | [guardduty-enabled-centralized](guardduty-enabled-centralized.md) | Amazon GuardDuty can help to monitor and detect potential cybersecurity events by using threat intelligence feeds. These include lists of malicious IPs and machine learning to identify unexpected, unauthorized, and malicious activity within your AWS Cloud environment. | 
| 3857 | Network security, Intrusion Detection and Prevention, Configuring the IDS/IPS (18.4.11.C.01.) | [guardduty-eks-protection-audit-enabled](guardduty-eks-protection-audit-enabled.md) | This control checks whether GuardDuty EKS Audit Log Monitoring is enabled. GuardDuty EKS Audit Log Monitoring helps you detect potentially suspicious activities in your Amazon Elastic Kubernetes Service (Amazon EKS) clusters. EKS Audit Log Monitoring uses Kubernetes audit logs to capture chronological activities from users, applications using the Kubernetes API, and the control plane. | 
| 3857 | Network security, Intrusion Detection and Prevention, Configuring the IDS/IPS (18.4.11.C.01.) | [guardduty-eks-protection-runtime-enabled](guardduty-eks-protection-runtime-enabled.md) | This control checks whether GuardDuty EKS Runtime Monitoring with automated agent management is enabled. EKS Protection in Amazon GuardDuty provides threat detection coverage to help you protect Amazon EKS clusters within your AWS environment. EKS Runtime Monitoring uses operating system-level events to help you detect potential threats in EKS nodes and containers within your EKS clusters. | 
| 3857 | Network security, Intrusion Detection and Prevention, Configuring the IDS/IPS (18.4.11.C.01.) | [guardduty-lambda-protection-enabled](guardduty-lambda-protection-enabled.md) | This control checks whether GuardDuty Lambda Protection is enabled. GuardDuty Lambda Protection helps you identify potential security threats when an AWS Lambda function gets invoked. After your enable Lambda Protection, GuardDuty starts monitoring Lambda network activity logs associated with the Lambda functions in your AWS account. When a Lambda function gets invoked and GuardDuty identifies suspicious network traffic that indicates the presence of a potentially malicious piece of code in your Lambda function, GuardDuty generates a finding. | 
| 3857 | Network security, Intrusion Detection and Prevention, Configuring the IDS/IPS (18.4.11.C.01.) | [guardduty-s3-protection-enabled](guardduty-s3-protection-enabled.md) | This control checks whether GuardDuty S3 Protection is enabled. S3 Protection enables GuardDuty to monitor object-level API operations to identify potential security risks for data within your Amazon S3 buckets. GuardDuty monitors threats against your S3 resources by analyzing AWS CloudTrail management events and CloudTrail S3 data events. | 
| 3875 | Network security, Intrusion Detection and Prevention, Event management and correlation (18.4.12.C.01.) | [guardduty-enabled-centralized](guardduty-enabled-centralized.md) | Amazon GuardDuty can help to monitor and detect potential cybersecurity events by using threat intelligence feeds. These include lists of malicious IPs and machine learning to identify unexpected, unauthorized, and malicious activity within your AWS Cloud environment. | 
| 3875 | Network security, Intrusion Detection and Prevention, Event management and correlation (18.4.12.C.01.) | [securityhub-enabled](securityhub-enabled.md) | AWS Security Hub helps to monitor unauthorized personnel, connections, devices, and software. AWS Security Hub aggregates, organizes, and prioritizes the security alerts, or findings, from multiple AWS services. Some such services are Amazon Security Hub, Amazon Inspector, Amazon Macie, AWS Identity and Access Management (IAM) Access Analyzer, and AWS Firewall Manager, and AWS Partner solutions. | 
| 4441 | Data management, Databases, Database files (20.4.4.C.02.) | [elasticsearch-encrypted-at-rest](elasticsearch-encrypted-at-rest.md) | This control checks whether Elasticsearch domains have encryption-at-rest configuration enabled. The check fails if encryption at rest is not enabled. For an added layer of security for sensitive data, you should configure your Elasticsearch Service domain to be encrypted at rest. When you configure encryption of data at rest, Amazon Key Management Service (KMS) stores and manages your encryption keys. To perform the encryption, AWS KMS uses the Advanced Encryption Standard algorithm with 256-bit keys (AES-256). | 
| 4441 | Data management, Databases, Database files (20.4.4.C.02.) | [opensearch-encrypted-at-rest](opensearch-encrypted-at-rest.md) | This control checks whether OpenSearch domains have encryption-at-rest configuration enabled. The check fails if encryption at rest is not enabled. For an added layer of security for sensitive data, you should configure your OpenSearch Service domain to be encrypted at rest. When you configure encryption of data at rest, Amazon Key Management Service (KMS) stores and manages your encryption keys. To perform the encryption, AWS KMS uses the Advanced Encryption Standard algorithm with 256-bit keys (AES-256). | 
| 4441 | Data management, Databases, Database files (20.4.4.C.02.) | [rds-logging-enabled](rds-logging-enabled.md) | To help with logging and monitoring within your environment, ensure Amazon Relational Database Service (RDS) logging is enabled. With Amazon RDS logging, you can capture events such as connections, disconnections, queries, or tables queried. | 
| 4441 | Data management, Databases, Database files (20.4.4.C.02.) | [rds-snapshot-encrypted](rds-snapshot-encrypted.md) | Ensure that encryption is enabled for your Amazon Relational Database Service (RDS) snapshots. Because sensitive data can exist at rest, enable encryption at rest to help protect that data. | 
| 4441 | Data management, Databases, Database files (20.4.4.C.02.) | [rds-snapshots-public-prohibited](rds-snapshots-public-prohibited.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Relational Database Service (RDS) instances are not public. Amazon RDS database instances can contain sensitive information and principles and access control is required for such accounts. | 
| 4441 | Data management, Databases, Database files (20.4.4.C.02.) | [rds-storage-encrypted](rds-storage-encrypted.md) | To help protect data at rest, ensure that encryption is enabled for your Amazon Relational Database Service (RDS) instances. Because sensitive data can exist at rest in Amazon RDS instances, enable encryption at rest to help protect that data. | 
| 4441 | Data management, Databases, Database files (20.4.4.C.02.) | [redshift-cluster-configuration-check](redshift-cluster-configuration-check.md) | To protect data at rest, ensure that encryption is enabled for your Amazon Redshift clusters. You must also ensure that required configurations are deployed on Amazon Redshift clusters. The audit logging should be enabled to provide information about connections and user activities in the database. This rule sets clusterDbEncrypted to true, and loggingEnabled to true. | 
| 4445 | Data management, Databases, Accountability (20.4.5.C.02.) | [rds-logging-enabled](rds-logging-enabled.md) | To help with logging and monitoring within your environment, ensure Amazon Relational Database Service (RDS) logging is enabled. With Amazon RDS logging, you can capture events such as connections, disconnections, queries, or tables queried. | 
| 4445 | Data management, Databases, Accountability (20.4.5.C.02.) | [redshift-cluster-configuration-check](redshift-cluster-configuration-check.md) | To protect data at rest, ensure that encryption is enabled for your Amazon Redshift clusters. You must also ensure that required configurations are deployed on Amazon Redshift clusters. The audit logging should be enabled to provide information about connections and user activities in the database. This rule sets clusterDbEncrypted to true, and loggingEnabled to true. | 
| 4829 | Enterprise systems security, Cloud Computing, System Availability (22.1.23.C.01.) | [dynamodb-autoscaling-enabled](dynamodb-autoscaling-enabled.md) | Amazon DynamoDB auto scaling uses the AWS Application Auto Scaling service to adjust provisioned throughput capacity that automatically responds to actual traffic patterns. This enables a table or a global secondary index to increase its provisioned read/write capacity to handle sudden increases in traffic, without throttling. | 
| 4829 | Enterprise systems security, Cloud Computing, System Availability (22.1.23.C.01.) | [elb-cross-zone-load-balancing-enabled](elb-cross-zone-load-balancing-enabled.md) | Enable cross-zone load balancing for your Elastic Load Balancers (ELBs) to help maintain adequate capacity and availability. The cross-zone load balancing reduces the need to maintain equivalent numbers of instances in each enabled Availability Zone. It also improves your application's ability to handle the loss of one or more instances. | 
| 4838 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.03.) | [cloudtrail-s3-dataevents-enabled](cloudtrail-s3-dataevents-enabled.md) | The collection of Simple Storage Service (Amazon S3) data events helps in detecting any anomalous activity. The details include AWS account information that accessed an Amazon S3 bucket, IP address, and time of event. | 
| 4838 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.03.) | [ebs-snapshot-public-restorable-check](ebs-snapshot-public-restorable-check.md) | Manage access to the AWS Cloud by ensuring Amazon Elastic Block Store (EBS) snapshots are not publicly restorable. EBS volume snapshots can contain sensitive information and access control is required for such accounts. | 
| 4838 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.03.) | [s3-account-level-public-access-blocks-periodic](s3-account-level-public-access-blocks-periodic.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Simple Storage Service (Amazon S3) buckets cannot be publicly accessed. This rule helps keeping sensitive data safe from unauthorized remote users by preventing public access. This rule sets ignorePublicAcls to True, blockPublicPolicy to True, blockPublicAcls to True, and restrictPublicBuckets to True. | 
| 4838 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.03.) | [s3-bucket-public-read-prohibited](s3-bucket-public-read-prohibited.md) | Manage access to resources in the AWS Cloud by only allowing authorized users, processes, and devices access to Amazon Simple Storage Service (Amazon S3) buckets. The management of access should be consistent with the classification of the data. | 
| 4838 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.03.) | [s3-bucket-public-write-prohibited](s3-bucket-public-write-prohibited.md) | Manage access to resources in the AWS Cloud by only allowing authorized users, processes, and devices access to Amazon Simple Storage Service (Amazon S3) buckets. The management of access should be consistent with the classification of the data. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [dynamodb-table-encrypted-kms](dynamodb-table-encrypted-kms.md) | Ensure that encryption is enabled for your Amazon DynamoDB tables. Because sensitive data can exist at rest in these tables, enable encryption at rest to help protect that data. By default, DynamoDB tables are encrypted with an AWS owned Key Management Service (KMS) key. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [efs-encrypted-check](efs-encrypted-check.md) | Because sensitive data can exist and to help protect data at rest, ensure encryption is enabled for your Amazon Elastic File System (EFS). | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [elasticsearch-encrypted-at-rest](elasticsearch-encrypted-at-rest.md) | This control checks whether Elasticsearch domains have encryption-at-rest configuration enabled. The check fails if encryption at rest is not enabled. For an added layer of security for sensitive data, you should configure your Elasticsearch Service domain to be encrypted at rest. When you configure encryption of data at rest, Amazon Key Management Service (KMS) stores and manages your encryption keys. To perform the encryption, AWS KMS uses the Advanced Encryption Standard algorithm with 256-bit keys (AES-256). | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [elasticsearch-node-to-node-encryption-check](elasticsearch-node-to-node-encryption-check.md) | This control checks whether Elasticsearch domains have node-to-node encryption enabled. This control fails if node-to-node encryption is disabled on the domain. HTTPS (TLS) can be used to help prevent potential attackers from eavesdropping on or manipulating network traffic using person-in-the-middle or similar attacks. Only encrypted connections over HTTPS (TLS) should be allowed. Enabling node-to-node encryption for Elasticsearch domains ensures that intra-cluster communications are encrypted in transit. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [elb-tls-https-listeners-only](elb-tls-https-listeners-only.md) | Ensure that your Elastic Load Balancers (ELBs) are configured with SSL or HTTPS listeners. Because sensitive data can exist, enable encryption in transit to help protect that data. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [encrypted-volumes](encrypted-volumes.md) | Because sensitive data can exist and to help protect data at rest, ensure encryption is enabled for your Amazon Elastic Block Store (EBS) volumes. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [opensearch-encrypted-at-rest](opensearch-encrypted-at-rest.md) | This control checks whether OpenSearch domains have encryption-at-rest configuration enabled. The check fails if encryption at rest is not enabled. For an added layer of security for sensitive data, you should configure your OpenSearch Service domain to be encrypted at rest. When you configure encryption of data at rest, Amazon Key Management Service (KMS) stores and manages your encryption keys. To perform the encryption, AWS KMS uses the Advanced Encryption Standard algorithm with 256-bit keys (AES-256). | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [opensearch-node-to-node-encryption-check](opensearch-node-to-node-encryption-check.md) | This control checks whether OpenSearch domains have node-to-node encryption enabled. This control fails if node-to-node encryption is disabled on the domain. HTTPS (TLS) can be used to help prevent potential attackers from eavesdropping on or manipulating network traffic using person-in-the-middle or similar attacks. Only encrypted connections over HTTPS (TLS) should be allowed. Enabling node-to-node encryption for OpenSearch domains ensures that intra-cluster communications are encrypted in transit. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [rds-snapshot-encrypted](rds-snapshot-encrypted.md) | Ensure that encryption is enabled for your Amazon Relational Database Service (RDS) snapshots. Because sensitive data can exist at rest, enable encryption at rest to help protect that data. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [rds-storage-encrypted](rds-storage-encrypted.md) | To help protect data at rest, ensure that encryption is enabled for your Amazon Relational Database Service (RDS) instances. Because sensitive data can exist at rest in Amazon RDS instances, enable encryption at rest to help protect that data. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [redshift-cluster-configuration-check](redshift-cluster-configuration-check.md) | To protect data at rest, ensure that encryption is enabled for your Amazon Redshift clusters. You must also ensure that required configurations are deployed on Amazon Redshift clusters. The audit logging should be enabled to provide information about connections and user activities in the database. This rule sets clusterDbEncrypted to true, and loggingEnabled to true. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [redshift-require-tls-ssl](redshift-require-tls-ssl.md) | Ensure that your Amazon Redshift clusters require TLS/SSL encryption to connect to SQL clients. Because sensitive data can exist, enable encryption in transit to help protect that data. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [s3-bucket-ssl-requests-only](s3-bucket-ssl-requests-only.md) | To help protect data in transit, ensure that your Amazon Simple Storage Service (Amazon S3) buckets require requests to use Secure Socket Layer (SSL). Because sensitive data can exist, enable encryption in transit to help protect that data. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [sagemaker-endpoint-configuration-kms-key-configured](sagemaker-endpoint-configuration-kms-key-configured.md) | To help protect data at rest, ensure encryption with AWS Key Management Service (KMS) is enabled for your SageMaker endpoint. Because sensitive data can exist at rest in SageMaker endpoint, enable encryption at rest to help protect that data. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [sagemaker-notebook-instance-kms-key-configured](sagemaker-notebook-instance-kms-key-configured.md) | To help protect data at rest, ensure encryption with AWS Key Management Service (KMS) is enabled for your SageMaker notebook. Because sensitive data can exist at rest in SageMaker notebook, enable encryption at rest to help protect that data. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [secretsmanager-using-cmk](secretsmanager-using-cmk.md) | To help protect data at rest, ensure encryption with AWS Key Management Service (KMS) is enabled for AWS Secrets Manager secrets. Because sensitive data can exist at rest in Secrets Manager secrets, enable encryption at rest to help protect that data. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [db-instance-backup-enabled](db-instance-backup-enabled.md) | The backup feature of Amazon Relational Database Service (RDS) creates backups of your databases and transaction logs. Amazon RDS automatically creates a storage volume snapshot of your DB instance, backing up the entire DB instance. The system allows you to set specific retention periods to meet your resilience requirements. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [dynamodb-pitr-enabled](dynamodb-pitr-enabled.md) | Enable this rule to check that information has been backed up. It also maintains the backups by ensuring that point-in-time recovery is enabled in Amazon DynamoDB. The recovery maintains continuous backups of your table for the last 35 days. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [elasticache-redis-cluster-automatic-backup-check](elasticache-redis-cluster-automatic-backup-check.md) | When automatic backups are enabled, Amazon ElastiCache creates a backup of the cluster on a daily basis. The backup can be retained for a number of days as specified by your organization. Automatic backups can help guard against data loss. If a failure occurs, you can create a new cluster, which restores your data from the most recent backup. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [rds-cluster-deletion-protection-enabled](rds-cluster-deletion-protection-enabled.md) | Ensure Amazon Relational Database Service (RDS) instances have deletion protection enabled. Use deletion protection to prevent your RDS instances from being accidentally or maliciously deleted, which can lead to loss of availability for your applications. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [rds-instance-deletion-protection-enabled](rds-instance-deletion-protection-enabled.md) | Ensure Amazon Relational Database Service (RDS) instances have deletion protection enabled. Use deletion protection to prevent your Amazon RDS instances from being accidentally or maliciously deleted, which can lead to loss of availability for your applications. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [redshift-backup-enabled](redshift-backup-enabled.md) | To help with data back-up processes, ensure your Amazon Redshift clusters have automated snapshots. When automated snapshots are enabled for a cluster, Redshift periodically takes snapshots of that cluster. By default, Redshift takes a snapshot every eight hours or every 5 GB per node of data changes, or whichever comes first. | 
| 6843 | Access Control and Passwords, Privileged Access Management, The Principle of Least Privilege (16.4.31.C.02.) | [mfa-enabled-for-iam-console-access](mfa-enabled-for-iam-console-access.md) | Multi-factor authentication (MFA) adds extra security by requiring users to provide unique authentication from an AWS-supported MFA mechanism, in addition to their regular sign-in credentials, when they access AWS websites or services. Supported mechanisms include U2F security keys, virtual or hardware MFA devices, and SMS-based codes. This rule checks whether AWS MFA is enabled for all AWS Identity and Access Management (IAM) users that use a console password. The rule is compliant if MFA is enabled. | 
| 6843 | Access Control and Passwords, Privileged Access Management, The Principle of Least Privilege (16.4.31.C.02.) | [root-account-hardware-mfa-enabled](root-account-hardware-mfa-enabled.md) | Manage access to resources in the AWS Cloud by ensuring hardware multi-factor authentication (MFA) is enabled for the root user. The root user is the most privileged user in an AWS account. The MFA adds an extra layer of protection for a user name and password. By requiring MFA for the root user, you can reduce the incidents of compromised AWS accounts. | 
| 6852 | Access Control and Passwords, Privileged Access Management, Suspension and Revocation of Privileged Access Credentials (16.4.33.C.01.) | [iam-user-unused-credentials-check](iam-user-unused-credentials-check.md) | AWS Identity and Access Management (IAM) can help you with access permissions and authorizations by checking for IAM passwords and access keys that are not used for a specified time period. If these unused credentials are identified, you should disable and/or remove the credentials, as this may violate the principle of least privilege. This rule sets maxCredentialUsageAge to 30 days. | 
| 6860 | Access Control and Passwords, Privileged Access Management, Monitoring and Review (16.4.35.C.02.) | [cloud-trail-cloud-watch-logs-enabled](cloud-trail-cloud-watch-logs-enabled.md) | You should configure CloudTrail with CloudWatch Logs to monitor your trail logs and be notified when specific activity occurs. This rule checks whether AWS CloudTrail trails are configured to send logs to Amazon CloudWatch logs. | 
| 6860 | Access Control and Passwords, Privileged Access Management, Monitoring and Review (16.4.35.C.02.) | [cloudtrail-enabled](cloudtrail-enabled.md) | AWS CloudTrail can help in non-repudiation by recording AWS Management Console actions and API calls. You can identify the users and AWS accounts that called an AWS service, the source IP address where the calls generated, and the timings of the calls. Details of captured data are seen within AWS CloudTrail Record Contents. | 
| 6861 | Access Control and Passwords, Privileged Access Management, Monitoring and Review (16.4.35.C.03.) | [cloudtrail-security-trail-enabled](cloudtrail-security-trail-enabled.md) | This rule helps ensure the use of AWS recommended security best practices for AWS CloudTrail, by checking for the enablement of multiple settings. These include the use of log encryption, log validation, and enabling AWS CloudTrail in multiple Regions. | 
| 6953 | Access Control and Passwords, Multi-Factor Authentication, System Architecture and Security Controls (16.7.34.C.02.) | [mfa-enabled-for-iam-console-access](mfa-enabled-for-iam-console-access.md) | Multi-factor authentication (MFA) adds extra security by requiring users to provide unique authentication from an AWS-supported MFA mechanism, in addition to their regular sign-in credentials, when they access AWS websites or services. Supported mechanisms include U2F security keys, virtual or hardware MFA devices, and SMS-based codes. This rule checks whether AWS MFA is enabled for all AWS Identity and Access Management (IAM) users that use a console password. The rule is compliant if MFA is enabled. | 
| 6953 | Access Control and Passwords, Multi-Factor Authentication, System Architecture and Security Controls (16.7.34.C.02.) | [root-account-hardware-mfa-enabled](root-account-hardware-mfa-enabled.md) | Manage access to resources in the AWS Cloud by ensuring hardware multi-factor authentication (MFA) is enabled for the root user. The root user is the most privileged user in an AWS account. The MFA adds an extra layer of protection for a user name and password. By requiring MFA for the root user, you can reduce the incidents of compromised AWS accounts. | 
| 7436 | Public Cloud Security, Identity Management and Access Control, Username and passwords (23.3.19.C.01.) | [iam-user-mfa-enabled](iam-user-mfa-enabled.md) | Enable this rule to restrict access to resources in the AWS Cloud. This rule ensures multi-factor authentication (MFA) is enabled for all IAM users. MFA adds an extra layer of protection on top of a user name and password. Reduce the incidents of compromised accounts by requiring MFA for IAM users. | 
| 7436 | Public Cloud Security, Identity Management and Access Control, Username and passwords (23.3.19.C.01.) | [mfa-enabled-for-iam-console-access](mfa-enabled-for-iam-console-access.md) | Manage access to resources in the AWS Cloud by ensuring that multi-factor authentication (MFA) is enabled for all AWS Identity and Access Management (IAM) users that have a console password. MFA adds an extra layer of protection on top of a user name and password. By requiring MFA for IAM users, you can reduce incidents of compromised accounts and keep sensitive data from being accessed by unauthorized users. | 
| 7436 | Public Cloud Security, Identity Management and Access Control, Username and passwords (23.3.19.C.01.) | [root-account-hardware-mfa-enabled](root-account-hardware-mfa-enabled.md) | Manage access to resources in the AWS Cloud by ensuring hardware multi-factor authentication (MFA) is enabled for the root user. The root user is the most privileged user in an AWS account. The MFA adds an extra layer of protection for a user name and password. By requiring MFA for the root user, you can reduce the incidents of compromised AWS accounts. | 
| 7436 | Public Cloud Security, Identity Management and Access Control, Username and passwords (23.3.19.C.01.) | [root-account-mfa-enabled](root-account-mfa-enabled.md) | Manage access to resources in the AWS Cloud by ensuring multi-factor authentication (MFA) is enabled for the root user. The root user is the most privileged user in an AWS account. The MFA adds an extra layer of protection for a user name and password. By requiring MFA for the root user, you can reduce the incidents of compromised AWS accounts. | 
| 7437 | Public Cloud Security, Identity Management and Access Control, Username and passwords (23.3.19.C.01.) | [iam-user-mfa-enabled](iam-user-mfa-enabled.md) | Enable this rule to restrict access to resources in the AWS Cloud. This rule ensures multi-factor authentication (MFA) is enabled for all IAM users. MFA adds an extra layer of protection on top of a user name and password. Reduce the incidents of compromised accounts by requiring MFA for IAM users. | 
| 7437 | Public Cloud Security, Identity Management and Access Control, Username and passwords (23.3.19.C.01.) | [mfa-enabled-for-iam-console-access](mfa-enabled-for-iam-console-access.md) | Manage access to resources in the AWS Cloud by ensuring that multi-factor authentication (MFA) is enabled for all AWS Identity and Access Management (IAM) users that have a console password. MFA adds an extra layer of protection on top of a user name and password. By requiring MFA for IAM users, you can reduce incidents of compromised accounts and keep sensitive data from being accessed by unauthorized users. | 
| 7437 | Public Cloud Security, Identity Management and Access Control, Username and passwords (23.3.19.C.01.) | [root-account-hardware-mfa-enabled](root-account-hardware-mfa-enabled.md) | Manage access to resources in the AWS Cloud by ensuring hardware multi-factor authentication (MFA) is enabled for the root user. The root user is the most privileged user in an AWS account. The MFA adds an extra layer of protection for a user name and password. By requiring MFA for the root user, you can reduce the incidents of compromised AWS accounts. | 
| 7437 | Public Cloud Security, Identity Management and Access Control, Username and passwords (23.3.19.C.01.) | [root-account-mfa-enabled](root-account-mfa-enabled.md) | Manage access to resources in the AWS Cloud by ensuring multi-factor authentication (MFA) is enabled for the root user. The root user is the most privileged user in an AWS account. The MFA adds an extra layer of protection for a user name and password. By requiring MFA for the root user, you can reduce the incidents of compromised AWS accounts. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [dms-replication-not-public](dms-replication-not-public.md) | Manage access to the AWS Cloud by ensuring AWS Database Migration Service (DMS) replication instances cannot be publicly accessed. DMS replication instances can contain sensitive information and access control is required for such accounts. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [ec2-imdsv2-check](ec2-imdsv2-check.md) | Ensure the Instance Metadata Service Version 2 (IMDSv2) method is enabled to help protect access and control of Amazon Elastic Compute Cloud (Amazon EC2) instance metadata. The IMDSv2 method uses session-based controls. With IMDSv2, controls can be implemented to restrict changes to instance metadata. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [ec2-instance-no-public-ip](ec2-instance-no-public-ip.md) | Manage access to the AWS Cloud by ensuring Amazon Elastic Compute Cloud (Amazon EC2) instances cannot be publicly accessed. Amazon EC2 instances can contain sensitive information and access control is required for such accounts. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [ec2-instances-in-vpc](ec2-instances-in-vpc.md) | Deploy Amazon Elastic Compute Cloud (Amazon EC2) instances within an Amazon Virtual Private Cloud (VPC) to enable secure communication between an instance and other services within the amazon VPC, without requiring an internet gateway, NAT device, or VPN connection. All traffic remains securely within the AWS Cloud. Because of their logical isolation, domains that reside within anAmazon VPC have an extra layer of security when compared to domains that use public endpoints. Assign Amazon EC2 instances to an Amazon VPC to properly manage access. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [elasticsearch-in-vpc-only](elasticsearch-in-vpc-only.md) | This control checks whether Elasticsearch domains are in a virtual private cloud (VPC). It does not evaluate the VPC subnet routing configuration to determine public access. You should ensure that Elasticsearch domains are not attached to public subnets. Elasticsearch domains deployed within a VPC can communicate with VPC resources over the private AWS network, without the need to traverse the public internet. This configuration increases the security posture by limiting access to the data in transit. VPCs provide a number of network controls to secure access to Elasticsearch domains, including network ACL and security groups | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [emr-master-no-public-ip](emr-master-no-public-ip.md) | Manage access to the AWS Cloud by ensuring Amazon Elastic MapReduce (EMR) cluster master nodes cannot be publicly accessed. Amazon EMR cluster master nodes can contain sensitive information and access control is required for such accounts. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [guardduty-enabled-centralized](guardduty-enabled-centralized.md) | Amazon GuardDuty can help to monitor and detect potential cybersecurity events by using threat intelligence feeds. These include lists of malicious IPs and machine learning to identify unexpected, unauthorized, and malicious activity within your AWS Cloud environment. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [lambda-function-public-access-prohibited](lambda-function-public-access-prohibited.md) | Manage access to resources in the AWS Cloud by ensuring AWS Lambda functions cannot be publicly accessed. Public access can potentially lead to degradation of availability of resources. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [opensearch-in-vpc-only](opensearch-in-vpc-only.md) | This control checks whether OpenSearch domains are in a virtual private cloud (VPC). It does not evaluate the VPC subnet routing configuration to determine public access. You should ensure that OpenSearch domains are not attached to public subnets. OpenSearch domains deployed within a VPC can communicate with VPC resources over the private AWS network, without the need to traverse the public internet. This configuration increases the security posture by limiting access to the data in transit. VPCs provide a number of network controls to secure access to OpenSearch domains, including network ACL and security groups. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [rds-instance-public-access-check](rds-instance-public-access-check.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Relational Database Service (RDS) instances are not public. Amazon RDS database instances can contain sensitive information, and principles and access control is required for such accounts. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [redshift-cluster-public-access-check](redshift-cluster-public-access-check.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Redshift clusters are not public. Amazon Redshift clusters can contain sensitive information and principles and access control is required for such accounts. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [s3-account-level-public-access-blocks-periodic](s3-account-level-public-access-blocks-periodic.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon Simple Storage Service (Amazon S3) buckets cannot be publicly accessed. This rule helps keeping sensitive data safe from unauthorized remote users by preventing public access. This rule sets ignorePublicAcls to True, blockPublicPolicy to True, blockPublicAcls to True, and restrictPublicBuckets to True. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [sagemaker-notebook-no-direct-internet-access](sagemaker-notebook-no-direct-internet-access.md) | Manage access to resources in the AWS Cloud by ensuring that Amazon SageMaker notebooks do not allow direct internet access. By preventing direct internet access, you can keep sensitive data from being accessed by unauthorized users. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [ssm-document-not-public](ssm-document-not-public.md) | Ensure AWS Systems Manager (SSM) documents are not public, as this may allow unintended access to your SSM documents. A public SSM document can expose information about your account, resources and internal processes. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [vpc-default-security-group-closed](vpc-default-security-group-closed.md) | Amazon Elastic Compute Cloud (Amazon EC2) security groups can help in the management of network access by providing stateful filtering of ingress and egress network traffic to AWS resources. Restricting all the traffic on the default security group helps in restricting remote access to your AWS resources. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [vpc-flow-logs-enabled](vpc-flow-logs-enabled.md) | The virtual private cloud (VPC) flow logs provide detailed records for information about the IP traffic going to and from network interfaces in your Amazon Virtual Private Cloud (Amazon VPC). By default, the flow log record includes values for the different components of the IP flow, including the source, destination, and protocol. | 
| 7496 | Public Cloud Security, Logging and Alerting in Public Cloud, Logging requirements (23.5.11.C.01.) | [api-gw-execution-logging-enabled](api-gw-execution-logging-enabled.md) | API Gateway logging displays detailed views of users who accessed the API and the way they accessed the API. This insight enables visibility of user activities. | 
| 7496 | Public Cloud Security, Logging and Alerting in Public Cloud, Logging requirements (23.5.11.C.01.) | [cloud-trail-log-file-validation-enabled](cloud-trail-log-file-validation-enabled.md) | Utilize AWS CloudTrail log file validation to check the integrity of CloudTrail logs. Log file validation helps determine if a log file was modified or deleted or unchanged after CloudTrail delivered it. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection. | 
| 7496 | Public Cloud Security, Logging and Alerting in Public Cloud, Logging requirements (23.5.11.C.01.) | [cloudfront-accesslogs-enabled](cloudfront-accesslogs-enabled.md) | This control checks whether server access logging is enabled on CloudFront distributions. The control fails if access logging is not enabled for a distribution. CloudFront access logs provide detailed information about every user request that CloudFront receives. Each log contains information such as the date and time the request was received, the IP address of the viewer that made the request, the source of the request, and the port number of the request from the viewer. These logs are useful for applications such as security and access audits and forensics investigation. This rule must be applied in the us-east-1 region. | 
| 7496 | Public Cloud Security, Logging and Alerting in Public Cloud, Logging requirements (23.5.11.C.01.) | [cloudtrail-enabled](cloudtrail-enabled.md) | AWS CloudTrail can help in non-repudiation by recording AWS Management Console actions and API calls. You can identify the users and AWS accounts that called an AWS service, the source IP address where the calls generated, and the timings of the calls. Details of captured data are seen within AWS CloudTrail Record Contents. | 
| 7496 | Public Cloud Security, Logging and Alerting in Public Cloud, Logging requirements (23.5.11.C.01.) | [cloudwatch-log-group-encrypted](cloudwatch-log-group-encrypted.md) | To help protect sensitive data at rest, ensure encryption is enabled for your Amazon CloudWatch Log Groups. | 
| 7496 | Public Cloud Security, Logging and Alerting in Public Cloud, Logging requirements (23.5.11.C.01.) | [elb-logging-enabled](elb-logging-enabled.md) | Elastic Load Balancing activity is a central point of communication within an environment. Ensure ELB logging is enabled. The collected data provides detailed information about requests sent to the ELB. Each log contains information such as the time the request was received, the client's IP address, latencies, request paths, and server responses. | 
| 7496 | Public Cloud Security, Logging and Alerting in Public Cloud, Logging requirements (23.5.11.C.01.) | [rds-logging-enabled](rds-logging-enabled.md) | To help with logging and monitoring within your environment, ensure Amazon Relational Database Service (RDS) logging is enabled. With Amazon RDS logging, you can capture events such as connections, disconnections, queries, or tables queried. | 
| 7496 | Public Cloud Security, Logging and Alerting in Public Cloud, Logging requirements (23.5.11.C.01.) | [wafv2-logging-enabled](wafv2-logging-enabled.md) | To help with logging and monitoring within your environment, enable AWS WAF (V2) logging on regional and global web ACLs. AWS WAF logging provides detailed information about the traffic that is analyzed by your web ACL. The logs record the time that AWS WAF received the request from your AWS resource, information about the request, and an action for the rule that each request matched. | 
| 7545 | Access Control and Passwords, Identification, Authentication and Authentication, Passwords and policy (16.1.31.C.02.) | [iam-password-policy](iam-password-policy.md) | Ensure annual password changes on systems that have not implemented multi-factor authentication (MFA) or passwordless authentication. | 
| 7546 | Access Control and Passwords, Identification, Authentication and Authentication, Passwords and policy (16.1.31.C.03.) | [iam-password-policy](iam-password-policy.md) | Ensure a minimum password length of 16 characters (e.g four words). Passwords must be long, strong and unique. No explicit complexity requirements are enforced (e.g. numbers or special characters), however passwords must be unique, or random and may include special characters and numbers to achieve this. | 

## Template
<a name="nzism-foundation-conformance-pack-sample"></a>

```
            ##################################################################################
            #
            #   Conformance Pack:
            #     Operational Best Practices for NZISM Foundation
            #
            #   This conformance pack helps verify compliance with NZISM requirements.
            #
            ##################################################################################

            Resources:
              AcmCertificateExpirationCheck:
                Controls: [ '1667' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: acm-certificate-expiration-check
                  InputParameters:
                    daysToExpiration: '30'
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ACM::Certificate
                  Source:
                    Owner: AWS
                    SourceIdentifier: ACM_CERTIFICATE_EXPIRATION_CHECK
                  Description: "SHOULD 14.5.8.C.01[CID:1667]| Software security/Web Application Development/Web applications"
              AlbHttpToHttpsRedirectionCheck:
                Controls: [ '1847', '2090' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: alb-http-to-https-redirection-check
                  Source:
                    Owner: AWS
                    SourceIdentifier: ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK
                  Description: "MUST 16.1.37.C.01[CID:1847], MUST 17.1.55.C.02[CID:2090]| Access Control and Passwords/Identification, Authentication and Passwords/Protecting authentication data in t..."
              ApiGwExecutionLoggingEnabled:
                Controls: [ '2013', '7496' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: api-gw-execution-logging-enabled
                  InputParameters:
                    loggingLevel: 'ERROR, INFO'
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ApiGateway::Stage
                      - AWS::ApiGatewayV2::Stage
                  Source:
                    Owner: AWS
                    SourceIdentifier: API_GW_EXECUTION_LOGGING_ENABLED
                  Description: "SHOULD 16.6.10.C.02[CID:2013], MUST 23.5.11.C.01[CID:7496]| Access Control and Passwords/Event Logging and Auditing/Additional events to be logged and Public Cloud Se..."
              CloudTrailCloudWatchLogsEnabled:
                Controls: [ '1998', '6860' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloud-trail-cloud-watch-logs-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED
                  Description: "SHOULD 16.6.6.C.02[CID:1998], MUST 16.4.35.C.02[CID:6860]| Access Control and Passwords: (Event Logging and Auditing/Maintaining system management logs and Privileged..."
              CloudTrailEncryptionEnabled:
                Controls: [ '2082' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloud-trail-encryption-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUD_TRAIL_ENCRYPTION_ENABLED
                  Description: "SHOULD 17.1.53.C.04[CID:2082]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical transfer requirements"
              CloudTrailLogFileValidationEnabled:
                Controls: [ '2022', '7496' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloud-trail-log-file-validation-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED
                  Description: "MUST 16.6.12.C.01[CID:2022], MUST 23.5.11.C.01[CID:7496]| Access Control and Passwords/Event Logging and Auditing/Event log protection and Public Cloud Security/Loggi..."
              CloudfrontAccesslogsEnabled:
                Condition: IsEdge
                Controls: [ '2013', '7496' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloudfront-accesslogs-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUDFRONT_ACCESSLOGS_ENABLED
                  Description: "SHOULD 16.6.10.C.02[CID:2013], MUST 23.5.11.C.01[CID:7496]| Access Control and Passwords/Event Logging and Auditing/Additional events to be logged and Public Cloud Se..."
              CloudfrontAssociatedWithWaf:
                Condition: IsEdge
                Controls: [ '3562' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloudfront-associated-with-waf
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUDFRONT_ASSOCIATED_WITH_WAF
                  Description: "MUST 19.1.12.C.01[CID:3562]| Gateway security/Gateways/Configuration of gateways"
              CloudfrontDefaultRootObjectConfigured:
                Condition: IsEdge
                Controls: [ '1661' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloudfront-default-root-object-configured
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUDFRONT_DEFAULT_ROOT_OBJECT_CONFIGURED
                  Description: "SHOULD 14.5.6.C.01[CID:1661]| Software security/Web Application Development/Agency website content"
              CloudfrontViewerPolicyHttps:
                Condition: IsEdge
                Controls: [ '1847' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloudfront-viewer-policy-https
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUDFRONT_VIEWER_POLICY_HTTPS
                  Description: "MUST 16.1.37.C.01[CID:1847]| Access Control and Passwords/Identification, Authentication and Passwords/Protecting authentication data in transit"
              CloudtrailEnabled:
                Controls: [ '1998', '2013', '6860', '7496' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloudtrail-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUD_TRAIL_ENABLED
                  Description: "SHOULD 16.6.6.C.02[CID:1998], SHOULD 16.6.10.C.02[CID:2013], MUST 16.4.35.C.02[CID:6860], MUST 23.5.11.C.01[CID:7496]| Access Control and Passwords: (Event Logging and..."
              CloudtrailS3DataeventsEnabled:
                Controls: [ '4838' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloudtrail-s3-dataevents-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUDTRAIL_S3_DATAEVENTS_ENABLED
                  Description: "SHOULD 22.1.24.C.03[CID:4838]| Enterprise systems security/Cloud Computing/Unauthorised Access"
              CloudtrailSecurityTrailEnabled:
                Controls: [ '6861' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloudtrail-security-trail-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUDTRAIL_SECURITY_TRAIL_ENABLED
                  Description: "MUST 16.4.35.C.03[CID:6861]| Access Control and Passwords/Privileged Access Management/Monitoring and Review"
              CloudwatchLogGroupEncrypted:
                Controls: [ '2022', '7496' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cloudwatch-log-group-encrypted
                  Source:
                    Owner: AWS
                    SourceIdentifier: CLOUDWATCH_LOG_GROUP_ENCRYPTED
                  Description: "MUST 16.6.12.C.01[CID:2022], MUST 23.5.11.C.01[CID:7496]| Access Control and Passwords/Event Logging and Auditing/Event log protection and Public Cloud Security/Loggi..."
              CmkBackingKeyRotationEnabled:
                Controls: [ '3021' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cmk-backing-key-rotation-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: CMK_BACKING_KEY_ROTATION_ENABLED
                  Description: "SHOULD 17.9.25.C.01[CID:3021]| Cryptography/Key Management/Contents of KMPs"
              CwLoggroupRetentionPeriodCheck:
                Controls: [ '1998', '2028' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: cw-loggroup-retention-period-check
                  InputParameters:
                    MinRetentionTime: '545'
                  Source:
                    Owner: AWS
                    SourceIdentifier: CW_LOGGROUP_RETENTION_PERIOD_CHECK
                  Description: "SHOULD 16.6.6.C.02[CID:1998], MUST 16.6.13.C.01[CID:2028]| Access Control and Passwords/Event Logging and Auditing: (Maintaining system management logs and Event log ..."
              DbInstanceBackupEnabled:
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: db-instance-backup-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBInstance
                  Source:
                    Owner: AWS
                    SourceIdentifier: DB_INSTANCE_BACKUP_ENABLED
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              DmsReplicationNotPublic:
                Controls: [ '3562', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: dms-replication-not-public
                  Source:
                    Owner: AWS
                    SourceIdentifier: DMS_REPLICATION_NOT_PUBLIC
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Public Cloud Security/Data Protection in Public Clou..."
              DynamodbAutoscalingEnabled:
                Controls: [ '4829' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: dynamodb-autoscaling-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::DynamoDB::Table
                  Source:
                    Owner: AWS
                    SourceIdentifier: DYNAMODB_AUTOSCALING_ENABLED
                  Description: "MUST 22.1.23.C.01[CID:4829]| Enterprise systems security/Cloud Computing/System Availability"
              DynamodbPitrEnabled:
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: dynamodb-pitr-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::DynamoDB::Table
                  Source:
                    Owner: AWS
                    SourceIdentifier: DYNAMODB_PITR_ENABLED
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              DynamodbTableEncryptedKms:
                Controls: [ '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: dynamodb-table-encrypted-kms
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::DynamoDB::Table
                  Source:
                    Owner: AWS
                    SourceIdentifier: DYNAMODB_TABLE_ENCRYPTED_KMS
                  Description: "SHOULD 22.1.24.C.04[CID:4839]| Enterprise systems security/Cloud Computing/Unauthorised Access"
              EbsSnapshotPublicRestorableCheck:
                Controls: [ '4838' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ebs-snapshot-public-restorable-check
                  Source:
                    Owner: AWS
                    SourceIdentifier: EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK
                  Description: "SHOULD 22.1.24.C.03[CID:4838]| Enterprise systems security/Cloud Computing/Unauthorised Access"
              Ec2EbsEncryptionByDefault:
                Controls: [ '2082' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ec2-ebs-encryption-by-default
                  Source:
                    Owner: AWS
                    SourceIdentifier: EC2_EBS_ENCRYPTION_BY_DEFAULT
                  Description: "SHOULD 17.1.53.C.04[CID:2082]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical transfer requirements"
              Ec2Imdsv2Check:
                Controls: [ '3562', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ec2-imdsv2-check
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::EC2::Instance
                  Source:
                    Owner: AWS
                    SourceIdentifier: EC2_IMDSV2_CHECK
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Public Cloud Security/Data Protection in Public Clou..."
              Ec2InstanceManagedBySystemsManager:
                Controls: [ '1149' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ec2-instance-managed-by-systems-manager
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::EC2::Instance
                      - AWS::SSM::ManagedInstanceInventory
                  Source:
                    Owner: AWS
                    SourceIdentifier: EC2_INSTANCE_MANAGED_BY_SSM
                  Description: "SHOULD 14.1.8.C.01[CID:1149]| Software security/Standard Operating Environments/Developing hardened SOEs"
              Ec2InstanceNoPublicIp:
                Controls: [ '3562', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ec2-instance-no-public-ip
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::EC2::Instance
                  Source:
                    Owner: AWS
                    SourceIdentifier: EC2_INSTANCE_NO_PUBLIC_IP
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Public Cloud Security/Data Protection in Public Clou..."
              Ec2InstancesInVpc:
                Controls: [ '3562', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ec2-instances-in-vpc
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::EC2::Instance
                  Source:
                    Owner: AWS
                    SourceIdentifier: INSTANCES_IN_VPC
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Public Cloud Security/Data Protection in Public Clou..."
              Ec2ManagedinstanceAssociationComplianceStatusCheck:
                Controls: [ '1149' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ec2-managedinstance-association-compliance-status-check
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::SSM::AssociationCompliance
                  Source:
                    Owner: AWS
                    SourceIdentifier: EC2_MANAGEDINSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK
                  Description: "SHOULD 14.1.8.C.01[CID:1149]| Software security/Standard Operating Environments/Developing hardened SOEs"
              Ec2ManagedinstancePatchComplianceStatusCheck:
                Controls: [ '3449', '3451', '3452', '3453' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ec2-managedinstance-patch-compliance-status-check
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::SSM::PatchCompliance
                  Source:
                    Owner: AWS
                    SourceIdentifier: EC2_MANAGEDINSTANCE_PATCH_COMPLIANCE_STATUS_CHECK
                  Description: "MUST 12.4.4.C.02[CID:3449], SHOULD 12.4.4.C.04[CID:3451], SHOULD 12.4.4.C.05[CID:3452], SHOULD 12.4.4.C.06[CID:3453]| Product Security/Product Patching and Updating/Pa..."
              EcrPrivateImageScanningEnabled:
                Controls: [ '3449' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ecr-private-image-scanning-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ECR::Repository
                  Source:
                    Owner: AWS
                    SourceIdentifier: ECR_PRIVATE_IMAGE_SCANNING_ENABLED
                  Description: "MUST 12.4.4.C.02[CID:3449]| Product Security/Product Patching and Updating/Patching vulnerabilities in products"
              EcsContainersNonprivileged:
                Controls: [ '1149' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ecs-containers-nonprivileged
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ECS::TaskDefinition
                  Source:
                    Owner: AWS
                    SourceIdentifier: ECS_CONTAINERS_NONPRIVILEGED
                  Description: "SHOULD 14.1.8.C.01[CID:1149]| Software security/Standard Operating Environments/Developing hardened SOEs"
              EcsContainersReadonlyAccess:
                Controls: [ '1149' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ecs-containers-readonly-access
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ECS::TaskDefinition
                  Source:
                    Owner: AWS
                    SourceIdentifier: ECS_CONTAINERS_READONLY_ACCESS
                  Description: "SHOULD 14.1.8.C.01[CID:1149]| Software security/Standard Operating Environments/Developing hardened SOEs"
              EfsEncryptedCheck:
                Controls: [ '2082', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: efs-encrypted-check
                  Source:
                    Owner: AWS
                    SourceIdentifier: EFS_ENCRYPTED_CHECK
                  Description: "SHOULD 17.1.53.C.04[CID:2082], SHOULD 22.1.24.C.04[CID:4839]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical transfer requirements and Enterpri..."
              ElasticBeanstalkManagedUpdatesEnabled:
                Controls: [ '3452' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: elastic-beanstalk-managed-updates-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ElasticBeanstalk::Environment
                  Source:
                    Owner: AWS
                    SourceIdentifier: ELASTIC_BEANSTALK_MANAGED_UPDATES_ENABLED
                  Description: "SHOULD 12.4.4.C.05[CID:3452]| Product Security/Product Patching and Updating/Patching vulnerabilities in products"
              ElasticacheRedisClusterAutomaticBackupCheck:
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: elasticache-redis-cluster-automatic-backup-check
                  Source:
                    Owner: AWS
                    SourceIdentifier: ELASTICACHE_REDIS_CLUSTER_AUTOMATIC_BACKUP_CHECK
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              ElasticsearchEncryptedAtRest:
                Controls: [ '2082', '4441', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: elasticsearch-encrypted-at-rest
                  Source:
                    Owner: AWS
                    SourceIdentifier: ELASTICSEARCH_ENCRYPTED_AT_REST
                  Description: "SHOULD 17.1.53.C.04[CID:2082], SHOULD 20.4.4.C.02[CID:4441], SHOULD 22.1.24.C.04[CID:4839]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical trans..."
              ElasticsearchInVpcOnly:
                Controls: [ '3562', '3623', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: elasticsearch-in-vpc-only
                  Source:
                    Owner: AWS
                    SourceIdentifier: ELASTICSEARCH_IN_VPC_ONLY
                  Description: "MUST 19.1.12.C.01[CID:3562], SHOULD 19.1.14.C.02[CID:3623], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways: (Configuration of gateways and Demilitarised zones..."
              ElasticsearchNodeToNodeEncryptionCheck:
                Controls: [ '1847', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: elasticsearch-node-to-node-encryption-check
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::Elasticsearch::Domain
                  Source:
                    Owner: AWS
                    SourceIdentifier: ELASTICSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK
                  Description: "MUST 16.1.37.C.01[CID:1847], SHOULD 22.1.24.C.04[CID:4839]| Access Control and Passwords/Identification, Authentication and Passwords/Protecting authentication data in..."
              ElbCrossZoneLoadBalancingEnabled:
                Controls: [ '4829' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: elb-cross-zone-load-balancing-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ElasticLoadBalancing::LoadBalancer
                  Source:
                    Owner: AWS
                    SourceIdentifier: ELB_CROSS_ZONE_LOAD_BALANCING_ENABLED
                  Description: "MUST 22.1.23.C.01[CID:4829]| Enterprise systems security/Cloud Computing/System Availability"
              ElbCustomSecurityPolicySslCheck:
                Controls: [ '2598', '2600' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: elb-custom-security-policy-ssl-check
                  InputParameters:
                    sslProtocolsAndCiphers: 'Protocol-TLSv1.2,ECDHE-ECDSA-AES256-GCM-SHA384'
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ElasticLoadBalancing::LoadBalancer
                  Source:
                    Owner: AWS
                    SourceIdentifier: ELB_CUSTOM_SECURITY_POLICY_SSL_CHECK
                  Description: "SHOULD 17.4.16.C.01[CID:2598], SHOULD NOT 17.4.16.C.02[CID:2600]| Cryptography/Transport Layer Security/Using TLS"
              ElbLoggingEnabled:
                Controls: [ '2013', '7496' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: elb-logging-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ElasticLoadBalancing::LoadBalancer
                      - AWS::ElasticLoadBalancingV2::LoadBalancer
                  Source:
                    Owner: AWS
                    SourceIdentifier: ELB_LOGGING_ENABLED
                  Description: "SHOULD 16.6.10.C.02[CID:2013], MUST 23.5.11.C.01[CID:7496]| Access Control and Passwords/Event Logging and Auditing/Additional events to be logged and Public Cloud Se..."
              ElbTlsHttpsListenersOnly:
                Controls: [ '1667', '1847', '2090', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: elb-tls-https-listeners-only
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ElasticLoadBalancing::LoadBalancer
                  Source:
                    Owner: AWS
                    SourceIdentifier: ELB_TLS_HTTPS_LISTENERS_ONLY
                  Description: "SHOULD 14.5.8.C.01[CID:1667], MUST 16.1.37.C.01[CID:1847], MUST 17.1.55.C.02[CID:2090], SHOULD 22.1.24.C.04[CID:4839]| Software security/Web Application Development/We..."
              EmrMasterNoPublicIp:
                Controls: [ '3562', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: emr-master-no-public-ip
                  Source:
                    Owner: AWS
                    SourceIdentifier: EMR_MASTER_NO_PUBLIC_IP
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Public Cloud Security/Data Protection in Public Clou..."
              EncryptedVolumes:
                Controls: [ '2082', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: encrypted-volumes
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::EC2::Volume
                  Source:
                    Owner: AWS
                    SourceIdentifier: ENCRYPTED_VOLUMES
                  Description: "SHOULD 17.1.53.C.04[CID:2082], SHOULD 22.1.24.C.04[CID:4839]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical transfer requirements and Enterpri..."
              GuarddutyEksProtectionAuditEnabled:
                Controls: [ '3857' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: guardduty-eks-protection-audit-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::GuardDuty::Detector
                  Source:
                    Owner: AWS
                    SourceIdentifier: GUARDDUTY_EKS_PROTECTION_AUDIT_ENABLED
                  Description: "SHOULD 18.4.11.C.01[CID:3857]| Network security/Intrusion Detection and Prevention/Configuring the IDS/IPS"
              GuarddutyEksProtectionRuntimeEnabled:
                Controls: [ '3857' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: guardduty-eks-protection-runtime-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::GuardDuty::Detector
                  Source:
                    Owner: AWS
                    SourceIdentifier: GUARDDUTY_EKS_PROTECTION_RUNTIME_ENABLED
                  Description: "SHOULD 18.4.11.C.01[CID:3857]| Network security/Intrusion Detection and Prevention/Configuring the IDS/IPS"
              GuarddutyEnabledCentralized:
                Controls: [ '3562', '3815', '3875', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: guardduty-enabled-centralized
                  Source:
                    Owner: AWS
                    SourceIdentifier: GUARDDUTY_ENABLED_CENTRALIZED
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 18.4.9.C.01[CID:3815], SHOULD 18.4.12.C.01[CID:3875], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateway..."
              GuarddutyLambdaProtectionEnabled:
                Controls: [ '3857' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: guardduty-lambda-protection-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::GuardDuty::Detector
                  Source:
                    Owner: AWS
                    SourceIdentifier: GUARDDUTY_LAMBDA_PROTECTION_ENABLED
                  Description: "SHOULD 18.4.11.C.01[CID:3857]| Network security/Intrusion Detection and Prevention/Configuring the IDS/IPS"
              GuarddutyRuntimeMonitoringEnabled:
                Controls: [ '1154' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: guardduty-runtime-monitoring-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::GuardDuty::Detector
                  Source:
                    Owner: AWS
                    SourceIdentifier: GUARDDUTY_RUNTIME_MONITORING_ENABLED
                  Description: "SHOULD 7.1.7.C.02[CID:1154]| Information Security Incidents/Detecting Information Security Incidents/Preventing and detecting information security incidents"
              GuarddutyS3ProtectionEnabled:
                Controls: [ '3857' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: guardduty-s3-protection-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::GuardDuty::Detector
                  Source:
                    Owner: AWS
                    SourceIdentifier: GUARDDUTY_S3_PROTECTION_ENABLED
                  Description: "SHOULD 18.4.11.C.01[CID:3857]| Network security/Intrusion Detection and Prevention/Configuring the IDS/IPS"
              IamPasswordPolicy:
                Controls: [ '7545', '7546' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: iam-password-policy
                  InputParameters:
                    MaxPasswordAge: '1095'
                    MinimumPasswordLength: '16'
                    PasswordReusePrevention: '24'
                    RequireUppercaseCharacters: 'false'
                    RequireLowercaseCharacters: 'false'
                    RequireSymbols: 'false'
                    RequireNumbers: 'false'
                  Source:
                    Owner: AWS
                    SourceIdentifier: IAM_PASSWORD_POLICY
                  Description: "MUST 16.1.31.C.02[CID:7545], MUST 16.1.31.C.03[CID:7546]| Access Control and Passwords/Identification, Authentication and Authentication/Passwords and policy"
              IamPolicyNoStatementsWithAdminAccess:
                Controls: [ '1946' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: iam-policy-no-statements-with-admin-access
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::IAM::Policy
                  Source:
                    Owner: AWS
                    SourceIdentifier: IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS
                  Description: "SHOULD 16.3.5.C.02[CID:1946]| Access Control and Passwords/Privileged User Access/Use of privileged accounts"
              IamRootAccessKeyCheck:
                Controls: [ '1946' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: iam-root-access-key-check
                  Source:
                    Owner: AWS
                    SourceIdentifier: IAM_ROOT_ACCESS_KEY_CHECK
                  Description: "SHOULD 16.3.5.C.02[CID:1946]| Access Control and Passwords/Privileged User Access/Use of privileged accounts"
              IamUserMfaEnabled:
                Controls: [ '1841', '7436', '7437' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: iam-user-mfa-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: IAM_USER_MFA_ENABLED
                  Description: "SHOULD 16.1.35.C.02[CID:1841], MUST 23.3.19.C.01[CID:7436], MUST 23.3.19.C.01[CID:7437]| Access Control and Passwords/Identification, Authentication and Passwords/Meth..."
              IamUserUnusedCredentialsCheck:
                Controls: [ '1893', '6852' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: iam-user-unused-credentials-check
                  InputParameters:
                    maxCredentialUsageAge: '90'
                  Source:
                    Owner: AWS
                    SourceIdentifier: IAM_USER_UNUSED_CREDENTIALS_CHECK
                  Description: "SHOULD 16.1.46.C.02[CID:1893], MUST 16.4.33.C.01[CID:6852]| Access Control and Passwords: (Identification, Authentication and Passwords/Suspension of access and Privi..."
              LambdaFunctionPublicAccessProhibited:
                Controls: [ '3562', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: lambda-function-public-access-prohibited
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::Lambda::Function
                  Source:
                    Owner: AWS
                    SourceIdentifier: LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Public Cloud Security/Data Protection in Public Clou..."
              MfaEnabledForIamConsoleAccess:
                Controls: [ '1841', '6843', '6953', '7436', '7437' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: mfa-enabled-for-iam-console-access
                  Source:
                    Owner: AWS
                    SourceIdentifier: MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS
                  Description: "SHOULD 16.1.35.C.02[CID:1841], SHOULD 16.4.31.C.02[CID:6843], SHOULD 16.7.34.C.02[CID:6953], MUST 23.3.19.C.01[CID:7436], MUST 23.3.19.C.01[CID:7437]| Access Control a..."
              OpensearchEncryptedAtRest:
                Controls: [ '2082', '4441', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: opensearch-encrypted-at-rest
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::OpenSearch::Domain
                  Source:
                    Owner: AWS
                    SourceIdentifier: OPENSEARCH_ENCRYPTED_AT_REST
                  Description: "SHOULD 17.1.53.C.04[CID:2082], SHOULD 20.4.4.C.02[CID:4441], SHOULD 22.1.24.C.04[CID:4839]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical trans..."
              OpensearchInVpcOnly:
                Controls: [ '3562', '3623', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: opensearch-in-vpc-only
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::OpenSearch::Domain
                  Source:
                    Owner: AWS
                    SourceIdentifier: OPENSEARCH_IN_VPC_ONLY
                  Description: "MUST 19.1.12.C.01[CID:3562], SHOULD 19.1.14.C.02[CID:3623], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways: (Configuration of gateways and Demilitarised zones..."
              OpensearchNodeToNodeEncryptionCheck:
                Controls: [ '1847', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: opensearch-node-to-node-encryption-check
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::OpenSearch::Domain
                  Source:
                    Owner: AWS
                    SourceIdentifier: OPENSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK
                  Description: "MUST 16.1.37.C.01[CID:1847], SHOULD 22.1.24.C.04[CID:4839]| Access Control and Passwords/Identification, Authentication and Passwords/Protecting authentication data in..."
              RdsAutomaticMinorVersionUpgradeEnabled:
                Controls: [ '3452' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-automatic-minor-version-upgrade-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBInstance
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_AUTOMATIC_MINOR_VERSION_UPGRADE_ENABLED
                  Description: "SHOULD 12.4.4.C.05[CID:3452]| Product Security/Product Patching and Updating/Patching vulnerabilities in products"
              RdsClusterDeletionProtectionEnabled:
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-cluster-deletion-protection-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBCluster
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_CLUSTER_DELETION_PROTECTION_ENABLED
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              RdsInstanceDeletionProtectionEnabled:
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-instance-deletion-protection-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBInstance
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_INSTANCE_DELETION_PROTECTION_ENABLED
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              RdsInstancePublicAccessCheck:
                Controls: [ '3562', '3623', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-instance-public-access-check
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBInstance
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_INSTANCE_PUBLIC_ACCESS_CHECK
                  Description: "MUST 19.1.12.C.01[CID:3562], SHOULD 19.1.14.C.02[CID:3623], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways: (Configuration of gateways and Demilitarised zones..."
              RdsLoggingEnabled:
                Controls: [ '2013', '4441', '4445', '7496' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-logging-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBInstance
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_LOGGING_ENABLED
                  Description: "SHOULD 16.6.10.C.02[CID:2013], SHOULD 20.4.4.C.02[CID:4441], SHOULD 20.4.5.C.02[CID:4445], MUST 23.5.11.C.01[CID:7496]| Access Control and Passwords/Event Logging and ..."
              RdsSnapshotEncrypted:
                Controls: [ '2082', '4441', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-snapshot-encrypted
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBSnapshot
                      - AWS::RDS::DBClusterSnapshot
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_SNAPSHOT_ENCRYPTED
                  Description: "SHOULD 17.1.53.C.04[CID:2082], SHOULD 20.4.4.C.02[CID:4441], SHOULD 22.1.24.C.04[CID:4839]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical trans..."
              RdsSnapshotsPublicProhibited:
                Controls: [ '4441' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-snapshots-public-prohibited
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBSnapshot
                      - AWS::RDS::DBClusterSnapshot
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_SNAPSHOTS_PUBLIC_PROHIBITED
                  Description: "SHOULD 20.4.4.C.02[CID:4441]| Data management/Databases/Database files"
              RdsStorageEncrypted:
                Controls: [ '2082', '4441', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-storage-encrypted
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBInstance
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_STORAGE_ENCRYPTED
                  Description: "SHOULD 17.1.53.C.04[CID:2082], SHOULD 20.4.4.C.02[CID:4441], SHOULD 22.1.24.C.04[CID:4839]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical trans..."
              RedshiftBackupEnabled:
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: redshift-backup-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::Redshift::Cluster
                  Source:
                    Owner: AWS
                    SourceIdentifier: REDSHIFT_BACKUP_ENABLED
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              RedshiftClusterConfigurationCheck:
                Controls: [ '4441', '4445', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: redshift-cluster-configuration-check
                  InputParameters:
                    clusterDbEncrypted: 'true'
                    loggingEnabled: 'true'
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::Redshift::Cluster
                  Source:
                    Owner: AWS
                    SourceIdentifier: REDSHIFT_CLUSTER_CONFIGURATION_CHECK
                  Description: "SHOULD 20.4.4.C.02[CID:4441], SHOULD 20.4.5.C.02[CID:4445], SHOULD 22.1.24.C.04[CID:4839]| Data management/Databases: (Database files and Accountability) and Enterpr..."
              RedshiftClusterMaintenancesettingsCheck:
                Controls: [ '3449', '3453' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: redshift-cluster-maintenancesettings-check
                  InputParameters:
                    allowVersionUpgrade: 'true'
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::Redshift::Cluster
                  Source:
                    Owner: AWS
                    SourceIdentifier: REDSHIFT_CLUSTER_MAINTENANCESETTINGS_CHECK
                  Description: "MUST 12.4.4.C.02[CID:3449], SHOULD 12.4.4.C.06[CID:3453]| Product Security/Product Patching and Updating/Patching vulnerabilities in products"
              RedshiftClusterPublicAccessCheck:
                Controls: [ '3562', '3623', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: redshift-cluster-public-access-check
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::Redshift::Cluster
                  Source:
                    Owner: AWS
                    SourceIdentifier: REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK
                  Description: "MUST 19.1.12.C.01[CID:3562], SHOULD 19.1.14.C.02[CID:3623], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways: (Configuration of gateways and Demilitarised zones..."
              RedshiftRequireTlsSsl:
                Controls: [ '2090', '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                   ConfigRuleName: redshift-require-tls-ssl
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::Redshift::Cluster
                  Source:
                    Owner: AWS
                    SourceIdentifier: REDSHIFT_REQUIRE_TLS_SSL
                  Description: "MUST 17.1.55.C.02[CID:2090], SHOULD 22.1.24.C.04[CID:4839]| Cryptography/Cryptographic Fundamentals/Information and Systems Protection and Enterprise systems security..."
              RestrictedSsh:
                Controls: [ '2726' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: restricted-ssh
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::EC2::SecurityGroup
                  Source:
                    Owner: AWS
                    SourceIdentifier: INCOMING_SSH_DISABLED
                  Description: "SHOULD 17.5.8.C.02[CID:2726]| Cryptography/Secure Shell/Automated remote access"
              RootAccountHardwareMfaEnabled:
                Controls: [ '1841', '6843', '6953', '7436', '7437' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: root-account-hardware-mfa-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: ROOT_ACCOUNT_HARDWARE_MFA_ENABLED
                  Description: "SHOULD 16.1.35.C.02[CID:1841], SHOULD 16.4.31.C.02[CID:6843], SHOULD 16.7.34.C.02[CID:6953], MUST 23.3.19.C.01[CID:7436], MUST 23.3.19.C.01[CID:7437]| Access Control a..."
              RootAccountMfaEnabled:
                Controls: [ '1841', '7436', '7437' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: root-account-mfa-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: ROOT_ACCOUNT_MFA_ENABLED
                  Description: "SHOULD 16.1.35.C.02[CID:1841], MUST 23.3.19.C.01[CID:7436], MUST 23.3.19.C.01[CID:7437]| Access Control and Passwords/Identification, Authentication and Passwords/Meth..."
              S3AccountLevelPublicAccessBlocksPeriodic:
                Controls: [ '3562', '4838', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: s3-account-level-public-access-blocks-periodic
                  Source:
                    Owner: AWS
                    SourceIdentifier: S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS_PERIODIC
                  Description: "MUST 19.1.12.C.01[CID:3562], SHOULD 22.1.24.C.03[CID:4838], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Enterprise systems se..."
              S3BucketPublicReadProhibited:
                Controls: [ '4838' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: s3-bucket-public-read-prohibited
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::S3::Bucket
                  Source:
                    Owner: AWS
                    SourceIdentifier: S3_BUCKET_PUBLIC_READ_PROHIBITED
                  Description: "SHOULD 22.1.24.C.03[CID:4838]| Enterprise systems security/Cloud Computing/Unauthorised Access"
              S3BucketPublicWriteProhibited:
                Controls: [ '4838' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: s3-bucket-public-write-prohibited
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::S3::Bucket
                  Source:
                    Owner: AWS
                    SourceIdentifier: S3_BUCKET_PUBLIC_WRITE_PROHIBITED
                  Description: "SHOULD 22.1.24.C.03[CID:4838]| Enterprise systems security/Cloud Computing/Unauthorised Access"
              S3BucketServerSideEncryptionEnabled:
                Controls: [ '2082' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: s3-bucket-server-side-encryption-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::S3::Bucket
                  Source:
                    Owner: AWS
                    SourceIdentifier: S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED
                  Description: "SHOULD 17.1.53.C.04[CID:2082]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical transfer requirements"
              S3BucketSslRequestsOnly:
                Controls: [ '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: s3-bucket-ssl-requests-only
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::S3::Bucket
                  Source:
                    Owner: AWS
                    SourceIdentifier: S3_BUCKET_SSL_REQUESTS_ONLY
                  Description: "SHOULD 22.1.24.C.04[CID:4839]| Enterprise systems security/Cloud Computing/Unauthorised Access"
              SagemakerEndpointConfigurationKmsKeyConfigured:
                Controls: [ '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: sagemaker-endpoint-configuration-kms-key-configured
                  Source:
                    Owner: AWS
                    SourceIdentifier: SAGEMAKER_ENDPOINT_CONFIGURATION_KMS_KEY_CONFIGURED
                  Description: "SHOULD 22.1.24.C.04[CID:4839]| Enterprise systems security/Cloud Computing/Unauthorised Access"
              SagemakerNotebookInstanceKmsKeyConfigured:
                Controls: [ '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: sagemaker-notebook-instance-kms-key-configured
                  Source:
                    Owner: AWS
                    SourceIdentifier: SAGEMAKER_NOTEBOOK_INSTANCE_KMS_KEY_CONFIGURED
                  Description: "SHOULD 22.1.24.C.04[CID:4839]| Enterprise systems security/Cloud Computing/Unauthorised Access"
              SagemakerNotebookNoDirectInternetAccess:
                Controls: [ '3562', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: sagemaker-notebook-no-direct-internet-access
                  Source:
                    Owner: AWS
                    SourceIdentifier: SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Public Cloud Security/Data Protection in Public Clou..."
              SecretsmanagerUsingCmk:
                Controls: [ '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: secretsmanager-using-cmk
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::SecretsManager::Secret
                  Source:
                    Owner: AWS
                    SourceIdentifier: SECRETSMANAGER_USING_CMK
                  Description: "SHOULD 22.1.24.C.04[CID:4839]| Enterprise systems security/Cloud Computing/Unauthorised Access"
              SecurityhubEnabled:
                Controls: [ '3875' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: securityhub-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: SECURITYHUB_ENABLED
                  Description: "SHOULD 18.4.12.C.01[CID:3875]| Network security/Intrusion Detection and Prevention/Event management and correlation"
              SsmDocumentNotPublic:
                Controls: [ '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ssm-document-not-public
                  Source:
                    Owner: AWS
                    SourceIdentifier: SSM_DOCUMENT_NOT_PUBLIC
                  Description: "MUST 23.4.10.C.01[CID:7466]| Public Cloud Security/Data Protection in Public Cloud/Data accessibility"
              VpcDefaultSecurityGroupClosed:
                Controls: [ '3562', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: vpc-default-security-group-closed
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::EC2::SecurityGroup
                  Source:
                    Owner: AWS
                    SourceIdentifier: VPC_DEFAULT_SECURITY_GROUP_CLOSED
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Public Cloud Security/Data Protection in Public Clou..."
              VpcFlowLogsEnabled:
                Controls: [ '3562', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: vpc-flow-logs-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: VPC_FLOW_LOGS_ENABLED
                  Description: "MUST 19.1.12.C.01[CID:3562], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Public Cloud Security/Data Protection in Public Clou..."
              VpcSgOpenOnlyToAuthorizedPorts:
                Controls: [ '3205' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: vpc-sg-open-only-to-authorized-ports
                  InputParameters:
                    authorizedTcpPorts: '443'
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::EC2::SecurityGroup
                  Source:
                    Owner: AWS
                    SourceIdentifier: VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS
                  Description: "SHOULD 18.1.13.C.02[CID:3205]| Network security/Network Management/Limiting network access"
              Wafv2LoggingEnabled:
                Controls: [ '2013', '7496' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: wafv2-logging-enabled
                  Source:
                    Owner: AWS
                    SourceIdentifier: WAFV2_LOGGING_ENABLED
                  Description: "SHOULD 16.6.10.C.02[CID:2013], MUST 23.5.11.C.01[CID:7496]| Access Control and Passwords/Event Logging and Auditing/Additional events to be logged and Public Cloud Se..."
```