

# Operational Best Practices for NZISM 3.9 (Extension)
<a name="operational-best-practices-for-nzism-extension"></a>

Conformance packs provide a general-purpose compliance framework designed to enable you to create security, operational or cost-optimization governance checks using managed or custom AWS Config rules and AWS Config remediation actions. Conformance Packs, as sample templates, are not designed to fully ensure compliance with a specific governance or compliance standard. You are responsible for making your own assessment of whether your use of the Services meets applicable legal and regulatory requirements.

The following provides a sample mapping between the [New Zealand Government Communications Security Bureau (GCSB) Information Security Manual (NZISM) 2025-11 Version 3.9](https://www.nzism.gcsb.govt.nz/ism-document) and AWS Managed Config rules. Each Config rule applies to a specific AWS resource type, and relates to one or more NZISM controls. An NZISM control can be related to multiple Config rules. Refer to the following table for more detail and guidance related to these mappings. Only controls representing recommended or baseline practice for information classified RESTRICTED and below are included in the mappings.

This sample conformance pack template contains mappings to controls within the NZISM framework, which is an integral part of the Protective Security Requirements (PSR) framework that sets out the New Zealand Government’s expectations for the management of personnel, information and physical security.

The Foundation part of this conformance pack can be deployed to the Sydney and global regions. The NZ Transition part contains the subset of Foundation Config rules that are currently available in the New Zealand region. The Foundation part will not currently deploy to the New Zealand region. The Extension part of this conformance pack can be deployed to the Sydney and New Zealand regions to augment the Config rules provided in the Foundation and NZ Transition parts.

The NZISM is licensed under the Creative Commons Attribution 4.0 New Zealand licence, available at [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/). Copyright information can be found at [NZISM New Zealand Information Security Manual \| Legal, Privacy, and Copyright](https://www.nzism.gcsb.govt.nz/legal-privacy-and-copyright/).



| Control ID  | Control Description  | AWS Config Rule  | Guidance  | 
| --- | --- | --- | --- | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [api-gw-cache-enabled-and-encrypted](api-gw-cache-enabled-and-encrypted.md) | To help protect data at rest, ensure encryption is enabled for your API Gateway stage's cache. Because sensitive data can be captured for the API method, enable encryption at rest to help protect that data. An exemption is available for pre-production environments. | 
| 2082 | Cryptography, Cryptographic Fundamentals, Reducing storage and physical transfer requirements (17.1.53.C.04.) | [s3-default-encryption-kms](s3-default-encryption-kms.md) | To help protect data at rest, ensure that encryption is enabled for your S3 buckets. Because sensitive data can exist at rest in an Amazon S3 bucket, enable encryption at rest to help protect that data. For more information about the encryption process and administration, use the AWS Key Management Service (AWS KMS) customer-managed CMKs. An exemption is available for buckets containing non-sensitive data provided SSE is enabled. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [alb-waf-enabled](alb-waf-enabled.md) | Ensure AWS WAF is enabled on Elastic Load Balancers (ELB) to help protect web applications. A WAF helps to protect your web applications or APIs against common web exploits. These web exploits may affect availability, compromise security, or consume excessive resources within your environment. An exemption is available if the load balancer is the origin for a CloudFront distribution with WAF enabled. | 
| 3562 | Gateway security, Gateways, Configuration of gateways (19.1.12.C.01.) | [api-gw-associated-with-waf](api-gw-associated-with-waf.md) | This control checks whether an API Gateway stage uses a AWS WAF web access control list (ACL). This control fails if a AWS WAF Regional web ACL is not attached to a REST API Gateway stage. AWS WAF is a web application firewall that helps protect web applications and APIs from attacks. It enables you to configure an ACL, which is a set of rules that allow, block, or count web requests based on customizable web security rules and conditions that you define. Ensure that your API Gateway stage is associated with an AWS WAF web ACL to help protect it from malicious attacks. An exemption is available if the API Gateway is the origin for a CloudFront distribution with WAF enabled. | 
| 4333 | Data management, Content Filtering, Content validation (20.3.7.C.02.) | [alb-waf-enabled](alb-waf-enabled.md) | Ensure AWS WAF is enabled on Elastic Load Balancers (ELB) to help protect web applications. A WAF helps to protect your web applications or APIs against common web exploits. These web exploits may affect availability, compromise security, or consume excessive resources within your environment. | 
| 4333 | Data management, Content Filtering, Content validation (20.3.7.C.02.) | [api-gw-associated-with-waf](api-gw-associated-with-waf.md) | This control checks whether an API Gateway stage uses a AWS WAF web access control list (ACL). This control fails if a AWS WAF Regional web ACL is not attached to a REST API Gateway stage. AWS WAF is a web application firewall that helps protect web applications and APIs from attacks. It enables you to configure an ACL, which is a set of rules that allow, block, or count web requests based on customizable web security rules and conditions that you define. Ensure that your API Gateway stage is associated with an AWS WAF web ACL to help protect it from malicious attacks. An exemption is available if the API Gateway is the origin for a CloudFront distribution with WAF enabled. | 
| 4829 | Enterprise systems security, Cloud Computing, System Availability (22.1.23.C.01.) | [rds-cluster-multi-az-enabled](rds-cluster-multi-az-enabled.md) | Amazon Aurora stores copies of the data in a DB cluster across multiple Availability Zones in a single AWS Region. Aurora stores these copies regardless of whether the instances in the DB cluster span multiple Availability Zones. When data is written to the primary DB instance, Aurora synchronously replicates the data across Availability Zones to six storage nodes associated with your cluster volume. Doing so provides data redundancy, eliminates I/O freezes, and minimizes latency spikes during system backups. Running a DB instance with high availability can enhance availability during planned system maintenance, and help protect your databases against failure and Availability Zone disruption. This rule checks if Multi-AZ replication is enabled on Amazon Aurora clusters managed by Amazon Relational Database Service (RDS). An exemption is available for pre-production environments. | 
| 4829 | Enterprise systems security, Cloud Computing, System Availability (22.1.23.C.01.) | [rds-multi-az-support](rds-multi-az-support.md) | Multi-AZ support in Amazon Relational Database Service (RDS) provides enhanced availability and durability for database instances. When you provision a Multi-AZ database instance, Amazon RDS automatically creates a primary database instance, and synchronously replicates the data to a standby instance in a different Availability Zone. Each Availability Zone runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable. In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby so that you can resume database operations as soon as the failover is complete. An exemption is available for pre-production environments. | 
| 4839 | Enterprise systems security, Cloud Computing, Unauthorised Access (22.1.24.C.04.) | [sns-encrypted-kms](sns-encrypted-kms.md) | To help protect data at rest, ensure that your Amazon Simple Notification Service (Amazon SNS) topics require encryption using AWS Key Management Service (AWS KMS). Because sensitive data can exist at rest in published messages, enable encryption at rest to help protect that data. An exemption is available when messages published to the topic do not contain sensitive data. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [dynamodb-in-backup-plan](dynamodb-in-backup-plan.md) | To help with data back-up processes, ensure your Amazon DynamoDB tables are a part of an AWS Backup plan. AWS Backup is a fully managed backup service with a policy-based backup solution. This solution simplifies your backup management and enables you to meet your business and regulatory backup compliance requirements. An exemption is available when a compensating recovery solution has been configured. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [ebs-in-backup-plan](ebs-in-backup-plan.md) | To help with data back-up processes, ensure your Amazon Elastic Block Store (Amazon EBS) volumes are a part of an AWS Backup plan. AWS Backup is a fully managed backup service with a policy-based backup solution. This solution simplifies your backup management and enables you to meet your business and regulatory backup compliance requirements. An exemption is available when a compensating recovery solution has been configured. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [efs-in-backup-plan](efs-in-backup-plan.md) | To help with data back-up processes, ensure your Amazon Elastic File System (Amazon EFS) file systems are a part of an AWS Backup plan. AWS Backup is a fully managed backup service with a policy-based backup solution. This solution simplifies your backup management and enables you to meet your business and regulatory backup compliance requirements. An exemption is available when a compensating recovery solution has been configured. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [rds-in-backup-plan](rds-in-backup-plan.md) | To help with data back-up processes, ensure your Amazon Relational Database Service (RDS) instances are a part of an AWS Backup plan. AWS Backup is a fully managed backup service with a policy-based backup solution. This solution simplifies your backup management and enables you to meet your business and regulatory backup compliance requirements. An exemption is available when a compensating recovery solution has been configured. | 
| 4849 | Enterprise systems security, Cloud Computing, Backup, Recovery Archiving and Data Remanence (22.1.26.C.01.) | [s3-bucket-versioning-enabled](s3-bucket-versioning-enabled.md) | Amazon Simple Storage Service (Amazon S3) bucket versioning helps keep multiple variants of an object in the same Amazon S3 bucket. Use versioning to preserve, retrieve, and restore every version of every object stored in your Amazon S3 bucket. Versioning helps you to easily recover from unintended user actions and application failures. An exemption is available when only a single variant of an object will be created, or when a compensating recovery solution has been configured. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [alb-waf-enabled](alb-waf-enabled.md) | Ensure AWS WAF is enabled on Elastic Load Balancers (ELB) to help protect web applications. A WAF helps to protect your web applications or APIs against common web exploits. These web exploits may affect availability, compromise security, or consume excessive resources within your environment. | 
| 7466 | Public Cloud Security, Data Protection in Public Cloud, Data accessibility (23.4.10.C.01.) | [api-gw-associated-with-waf](api-gw-associated-with-waf.md) | This control checks whether an API Gateway stage uses a AWS WAF web access control list (ACL). This control fails if a AWS WAF Regional web ACL is not attached to a REST API Gateway stage. AWS WAF is a web application firewall that helps protect web applications and APIs from attacks. It enables you to configure an ACL, which is a set of rules that allow, block, or count web requests based on customizable web security rules and conditions that you define. Ensure that your API Gateway stage is associated with an AWS WAF web ACL to help protect it from malicious attacks. An exemption is available if the API Gateway is the origin for a CloudFront distribution with WAF enabled. | 

## Template
<a name="nzism-extension-conformance-pack-sample"></a>

```
            ##################################################################################
            #
            #   Conformance Pack:
            #     Operational Best Practices for NZISM Extension
            #
            #   This conformance pack helps verify compliance with NZISM requirements.
            #
            ##################################################################################

            Resources:
              AlbWafEnabled:
                Condition: checkAlbWafEnabled
                Controls: [ '3562', '4333', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: alb-waf-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ElasticLoadBalancingV2::LoadBalancer
                  Source:
                    Owner: AWS
                    SourceIdentifier: ALB_WAF_ENABLED
                  Description: "MUST 19.1.12.C.01[CID:3562], SHOULD 20.3.7.C.02[CID:4333], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Data management/Conten..."
              ApiGwAssociatedWithWaf:
                Condition: checkApiGwAssociatedWithWaf
                Controls: [ '3562', '4333', '7466' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: api-gw-associated-with-waf
                  Source:
                    Owner: AWS
                    SourceIdentifier: API_GW_ASSOCIATED_WITH_WAF
                  Description: "MUST 19.1.12.C.01[CID:3562], SHOULD 20.3.7.C.02[CID:4333], MUST 23.4.10.C.01[CID:7466]| Gateway security/Gateways/Configuration of gateways and Data management/Conten..."
              ApiGwCacheEnabledAndEncrypted:
                Condition: checkApiGwCacheEnabledAndEncrypted
                Controls: [ '2082' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: api-gw-cache-enabled-and-encrypted
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::ApiGateway::Stage
                  Source:
                    Owner: AWS
                    SourceIdentifier: API_GW_CACHE_ENABLED_AND_ENCRYPTED
                  Description: "SHOULD 17.1.53.C.04[CID:2082]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical transfer requirements"
              DynamodbInBackupPlan:
                Condition: checkDynamodbInBackupPlan
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: dynamodb-in-backup-plan
                  Source:
                    Owner: AWS
                    SourceIdentifier: DYNAMODB_IN_BACKUP_PLAN
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              EbsInBackupPlan:
                Condition: checkEbsInBackupPlan
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: ebs-in-backup-plan
                  Source:
                    Owner: AWS
                    SourceIdentifier: EBS_IN_BACKUP_PLAN
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              EfsInBackupPlan:
                Condition: checkEfsInBackupPlan
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: efs-in-backup-plan
                  Source:
                    Owner: AWS
                    SourceIdentifier: EFS_IN_BACKUP_PLAN
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              RdsClusterMultiAzEnabled:
                Condition: checkRdsClusterMultiAzEnabled
                Controls: [ '4829' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-cluster-multi-az-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBCluster
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_CLUSTER_MULTI_AZ_ENABLED
                  Description: "MUST 22.1.23.C.01[CID:4829]| Enterprise systems security/Cloud Computing/System Availability"
              RdsInBackupPlan:
                Condition: checkRdsInBackupPlan
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-in-backup-plan
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_IN_BACKUP_PLAN
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              RdsMultiAzSupport:
                Condition: checkRdsMultiAzSupport
                Controls: [ '4829' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: rds-multi-az-support
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::RDS::DBInstance
                  Source:
                    Owner: AWS
                    SourceIdentifier: RDS_MULTI_AZ_SUPPORT
                  Description: "MUST 22.1.23.C.01[CID:4829]| Enterprise systems security/Cloud Computing/System Availability"
              S3BucketVersioningEnabled:
                Condition: checkS3BucketVersioningEnabled
                Controls: [ '4849' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: s3-bucket-versioning-enabled
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::S3::Bucket
                  Source:
                    Owner: AWS
                    SourceIdentifier: S3_BUCKET_VERSIONING_ENABLED
                  Description: "MUST 22.1.26.C.01[CID:4849]| Enterprise systems security/Cloud Computing/Backup, Recovery Archiving and Data Remanence"
              S3DefaultEncryptionKms:
                Condition: checkS3DefaultEncryptionKms
                Controls: [ '2082' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: s3-default-encryption-kms
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::S3::Bucket
                  Source:
                    Owner: AWS
                    SourceIdentifier: S3_DEFAULT_ENCRYPTION_KMS
                  Description: "SHOULD 17.1.53.C.04[CID:2082]| Cryptography/Cryptographic Fundamentals/Reducing storage and physical transfer requirements"
              SnsEncryptedKms:
                Condition: checkSnsEncryptedKms
                Controls: [ '4839' ]
                Type: AWS::Config::ConfigRule
                Properties:
                  ConfigRuleName: sns-encrypted-kms
                  Scope:
                    ComplianceResourceTypes:
                      - AWS::SNS::Topic
                  Source:
                    Owner: AWS
                    SourceIdentifier: SNS_ENCRYPTED_KMS
                  Description: "SHOULD 22.1.24.C.04[CID:4839]| Enterprise systems security/Cloud Computing/Unauthorised Access"
```