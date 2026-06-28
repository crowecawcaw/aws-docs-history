# Identifiers for legacy controls

The following section contains the Regional `API controlIdentifier`
designations of the legacy **Strongly recommended** and
**Elective**, _preventive_ and
_detective_, controls that are owned by AWS Control Tower,
including the elective **Data residency** controls. This information is
presented as a reference. Although we recommend that you call APIs using the global
identifiers, some controls may have been activated with Regional identifiers and still can be tracked by them.

###### Note

Mandatory controls cannot be deactivated by the control APIs.

Each item in the list that follows serves as a link, which provides more information
about these individual (legacy) controls that are owned by AWS Control Tower, as given in [The AWS Control Tower Control Catalog](controls-reference.md "controls-reference.md").

###### Designations for legacy Elective controls

- [arn:aws:controltower:REGION::control/AWS-GR\_AUDIT\_BUCKET\_ENCRYPTION\_ENABLED](../userguide/elective-controls.md#log-archive-encryption-enabled "../userguide/elective-controls.md#log-archive-encryption-enabled")
- [arn:aws:controltower:REGION::control/AWS-GR\_AUDIT\_BUCKET\_LOGGING\_ENABLED](../userguide/elective-controls.md#log-archive-access-enabled "../userguide/elective-controls.md#log-archive-access-enabled")
- [arn:aws:controltower:REGION::control/AWS-GR\_AUDIT\_BUCKET\_POLICY\_CHANGES\_PROHIBITED](../userguide/elective-controls.md#log-archive-policy-changes "../userguide/elective-controls.md#log-archive-policy-changes")
- [arn:aws:controltower:REGION::control/AWS-GR\_AUDIT\_BUCKET\_RETENTION\_POLICY](../userguide/elective-controls.md#log-archive-retention-policy "../userguide/elective-controls.md#log-archive-retention-policy")
- [arn:aws:controltower:REGION::control/AWS-GR\_IAM\_USER\_MFA\_ENABLED](../userguide/elective-controls.md#disallow-access-mfa "../userguide/elective-controls.md#disallow-access-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR\_MFA\_ENABLED\_FOR\_IAM\_CONSOLE\_ACCESS](../userguide/elective-controls.md#disallow-console-access-mfa "../userguide/elective-controls.md#disallow-console-access-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICT\_S3\_CROSS\_REGION\_REPLICATION](../userguide/elective-controls.md#disallow-s3-ccr "../userguide/elective-controls.md#disallow-s3-ccr")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICT\_S3\_DELETE\_WITHOUT\_MFA](../userguide/elective-controls.md#disallow-s3-delete-mfa "../userguide/elective-controls.md#disallow-s3-delete-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR\_S3\_VERSIONING\_ENABLED](../userguide/elective-controls.md#disallow-s3-no-versioning "../userguide/elective-controls.md#disallow-s3-no-versioning")

###### Designations for legacy Data residency controls (elective)

- [arn:aws:controltower:REGION::control/AWS-GR\_SUBNET\_AUTO\_ASSIGN\_PUBLIC\_IP\_DISABLED](../userguide/data-residency-controls.md#subnet-auto-assign-public-ip-disabled "../userguide/data-residency-controls.md#subnet-auto-assign-public-ip-disabled")
- [arn:aws:controltower:REGION::control/AWS-GR\_AUTOSCALING\_LAUNCH\_CONFIG\_PUBLIC\_IP\_DISABLED](../userguide/data-residency-controls.md#autoscaling-launch-config-public-ip-disabled "../userguide/data-residency-controls.md#autoscaling-launch-config-public-ip-disabled")
- [arn:aws:controltower:REGION::control/AWS-GR\_DISALLOW\_CROSS\_REGION\_NETWORKING](../userguide/data-residency-controls.md#prevent-cross-region-networking "../userguide/data-residency-controls.md#prevent-cross-region-networking")
- [arn:aws:controltower:REGION::control/AWS-GR\_DISALLOW\_VPC\_INTERNET\_ACCESS](../userguide/data-residency-controls.md#disallow-vpc-internet-access "../userguide/data-residency-controls.md#disallow-vpc-internet-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_DISALLOW\_VPN\_CONNECTIONS](../userguide/data-residency-controls.md#prevent-vpn-connection "../userguide/data-residency-controls.md#prevent-vpn-connection")
- [arn:aws:controltower:REGION::control/AWS-GR\_DMS\_REPLICATION\_NOT\_PUBLIC](../userguide/data-residency-controls.md#dms-replication-not-public "../userguide/data-residency-controls.md#dms-replication-not-public")
- [arn:aws:controltower:REGION::control/AWS-GR\_EBS\_SNAPSHOT\_PUBLIC\_RESTORABLE\_CHECK](../userguide/data-residency-controls.md#ebs-snapshot-public-restorable-check "../userguide/data-residency-controls.md#ebs-snapshot-public-restorable-check")
- [arn:aws:controltower:REGION::control/AWS-GR\_EC2\_INSTANCE\_NO\_PUBLIC\_IP](../userguide/data-residency-controls.md#ec2-instance-no-public-ip "../userguide/data-residency-controls.md#ec2-instance-no-public-ip")
- [arn:aws:controltower:REGION::control/AWS-GR\_EKS\_ENDPOINT\_NO\_PUBLIC\_ACCESS](../userguide/data-residency-controls.md#eks-endpoint-no-public-access "../userguide/data-residency-controls.md#eks-endpoint-no-public-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_ELASTICSEARCH\_IN\_VPC\_ONLY](../userguide/data-residency-controls.md#elasticsearch-in-vpc-only "../userguide/data-residency-controls.md#elasticsearch-in-vpc-only")
- [arn:aws:controltower:REGION::control/AWS-GR\_EMR\_MASTER\_NO\_PUBLIC\_IP](../userguide/data-residency-controls.md#emr-master-no-public-ip "../userguide/data-residency-controls.md#emr-master-no-public-ip")
- [arn:aws:controltower:REGION::control/AWS-GR\_LAMBDA\_FUNCTION\_PUBLIC\_ACCESS\_PROHIBITED](../userguide/data-residency-controls.md#lambda-function-public-access-prohibited "../userguide/data-residency-controls.md#lambda-function-public-access-prohibited")
- [arn:aws:controltower:REGION::control/AWS-GR\_NO\_UNRESTRICTED\_ROUTE\_TO\_IGW](../userguide/data-residency-controls.md#no-unrestricted-route-to-igw "../userguide/data-residency-controls.md#no-unrestricted-route-to-igw")
- [arn:aws:controltower:REGION::control/AWS-GR\_REDSHIFT\_CLUSTER\_PUBLIC\_ACCESS\_CHECK](../userguide/data-residency-controls.md#redshift-cluster-public-access-check "../userguide/data-residency-controls.md#redshift-cluster-public-access-check")
- [arn:aws:controltower:REGION::control/AWS-GR\_S3\_ACCOUNT\_LEVEL\_PUBLIC\_ACCESS\_BLOCKS\_PERIODIC](../userguide/data-residency-controls.md#s3-account-level-public-access-blocks-periodic "../userguide/data-residency-controls.md#s3-account-level-public-access-blocks-periodic")
- [arn:aws:controltower:REGION::control/AWS-GR\_SAGEMAKER\_NOTEBOOK\_NO\_DIRECT\_INTERNET\_ACCESS](../userguide/data-residency-controls.md#sagemaker-notebook-no-direct-internet-access "../userguide/data-residency-controls.md#sagemaker-notebook-no-direct-internet-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_SSM\_DOCUMENT\_NOT\_PUBLIC](../userguide/data-residency-controls.md#ssm-document-not-public "../userguide/data-residency-controls.md#ssm-document-not-public")

###### Designations for legacy Strongly recommended controls

- [arn:aws:controltower:REGION::control/AWS-GR\_ENCRYPTED\_VOLUMES](../userguide/strongly-recommended-controls.md#ebs-enable-encryption "../userguide/strongly-recommended-controls.md#ebs-enable-encryption")
- [arn:aws:controltower:REGION::control/AWS-GR\_EBS\_OPTIMIZED\_INSTANCE](../userguide/strongly-recommended-controls.md#disallow-not-ebs-optimized "../userguide/strongly-recommended-controls.md#disallow-not-ebs-optimized")
- [arn:aws:controltower:REGION::control/AWS-GR\_EC2\_VOLUME\_INUSE\_CHECK](../userguide/strongly-recommended-controls.md#disallow-unattached-ebs "../userguide/strongly-recommended-controls.md#disallow-unattached-ebs")
- [arn:aws:controltower:REGION::control/AWS-GR\_RDS\_INSTANCE\_PUBLIC\_ACCESS\_CHECK](../userguide/strongly-recommended-controls.md#disallow-rds-public-access "../userguide/strongly-recommended-controls.md#disallow-rds-public-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_RDS\_SNAPSHOTS\_PUBLIC\_PROHIBITED](../userguide/strongly-recommended-controls.md#disallow-rds-snapshot-public-access "../userguide/strongly-recommended-controls.md#disallow-rds-snapshot-public-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_RDS\_STORAGE\_ENCRYPTED](../userguide/strongly-recommended-controls.md#disallow-rds-storage-unencrypted "../userguide/strongly-recommended-controls.md#disallow-rds-storage-unencrypted")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICTED\_COMMON\_PORTS](../userguide/strongly-recommended-controls.md#rdp-disallow-internet "../userguide/strongly-recommended-controls.md#rdp-disallow-internet")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICTED\_SSH](../userguide/strongly-recommended-controls.md#ssh-disallow-internet "../userguide/strongly-recommended-controls.md#ssh-disallow-internet")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICT\_ROOT\_USER](../userguide/strongly-recommended-controls.md#disallow-root-auser-actions "../userguide/strongly-recommended-controls.md#disallow-root-auser-actions")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICT\_ROOT\_USER\_ACCESS\_KEYS](../userguide/strongly-recommended-controls.md#disallow-root-access-keys "../userguide/strongly-recommended-controls.md#disallow-root-access-keys")
- [arn:aws:controltower:REGION::control/AWS-GR\_ROOT\_ACCOUNT\_MFA\_ENABLED](../userguide/strongly-recommended-controls.md#enable-root-mfa "../userguide/strongly-recommended-controls.md#enable-root-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR\_S3\_BUCKET\_PUBLIC\_READ\_PROHIBITED](../userguide/strongly-recommended-controls.md#s3-disallow-public-read "../userguide/strongly-recommended-controls.md#s3-disallow-public-read")
- [arn:aws:controltower:REGION::control/AWS-GR\_S3\_BUCKET\_PUBLIC\_WRITE\_PROHIBITED](../userguide/strongly-recommended-controls.md#s3-disallow-public-write "../userguide/strongly-recommended-controls.md#s3-disallow-public-write")
- [arn:aws:controltower:REGION::control/AWS-GR\_DETECT\_CLOUDTRAIL\_ENABLED\_ON\_MEMBER\_ACCOUNTS](../userguide/strongly-recommended-controls.md#ensure-cloudtrail-enabled-recommended "../userguide/strongly-recommended-controls.md#ensure-cloudtrail-enabled-recommended")
