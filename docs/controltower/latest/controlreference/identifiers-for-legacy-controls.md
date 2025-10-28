# Identifiers for legacy

controls

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

###### Designations for legacy Elective

controls

- [arn:aws:controltower:REGION::control/AWS-GR_AUDIT_BUCKET_ENCRYPTION_ENABLED](../userguide/elective-controls.md#log-archive-encryption-enabled "../userguide/elective-controls.md#log-archive-encryption-enabled")
- [arn:aws:controltower:REGION::control/AWS-GR_AUDIT_BUCKET_LOGGING_ENABLED](../userguide/elective-controls.md#log-archive-access-enabled "../userguide/elective-controls.md#log-archive-access-enabled")
- [arn:aws:controltower:REGION::control/AWS-GR_AUDIT_BUCKET_POLICY_CHANGES_PROHIBITED](../userguide/elective-controls.md#log-archive-policy-changes "../userguide/elective-controls.md#log-archive-policy-changes")
- [arn:aws:controltower:REGION::control/AWS-GR_AUDIT_BUCKET_RETENTION_POLICY](../userguide/elective-controls.md#log-archive-retention-policy "../userguide/elective-controls.md#log-archive-retention-policy")
- [arn:aws:controltower:REGION::control/AWS-GR_IAM_USER_MFA_ENABLED](../userguide/elective-controls.md#disallow-access-mfa "../userguide/elective-controls.md#disallow-access-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR_MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS](../userguide/elective-controls.md#disallow-console-access-mfa "../userguide/elective-controls.md#disallow-console-access-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR_RESTRICT_S3_CROSS_REGION_REPLICATION](../userguide/elective-controls.md#disallow-s3-ccr "../userguide/elective-controls.md#disallow-s3-ccr")
- [arn:aws:controltower:REGION::control/AWS-GR_RESTRICT_S3_DELETE_WITHOUT_MFA](../userguide/elective-controls.md#disallow-s3-delete-mfa "../userguide/elective-controls.md#disallow-s3-delete-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR_S3_VERSIONING_ENABLED](../userguide/elective-controls.md#disallow-s3-no-versioning "../userguide/elective-controls.md#disallow-s3-no-versioning")

###### Designations for legacy Data residency

controls (elective)

- [arn:aws:controltower:REGION::control/AWS-GR_SUBNET_AUTO_ASSIGN_PUBLIC_IP_DISABLED](../userguide/data-residency-controls.md#subnet-auto-assign-public-ip-disabled "../userguide/data-residency-controls.md#subnet-auto-assign-public-ip-disabled")
- [arn:aws:controltower:REGION::control/AWS-GR_AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED](../userguide/data-residency-controls.md#autoscaling-launch-config-public-ip-disabled "../userguide/data-residency-controls.md#autoscaling-launch-config-public-ip-disabled")
- [arn:aws:controltower:REGION::control/AWS-GR_DISALLOW_CROSS_REGION_NETWORKING](../userguide/data-residency-controls.md#prevent-cross-region-networking "../userguide/data-residency-controls.md#prevent-cross-region-networking")
- [arn:aws:controltower:REGION::control/AWS-GR_DISALLOW_VPC_INTERNET_ACCESS](../userguide/data-residency-controls.md#disallow-vpc-internet-access "../userguide/data-residency-controls.md#disallow-vpc-internet-access")
- [arn:aws:controltower:REGION::control/AWS-GR_DISALLOW_VPN_CONNECTIONS](../userguide/data-residency-controls.md#prevent-vpn-connection "../userguide/data-residency-controls.md#prevent-vpn-connection")
- [arn:aws:controltower:REGION::control/AWS-GR_DMS_REPLICATION_NOT_PUBLIC](../userguide/data-residency-controls.md#dms-replication-not-public "../userguide/data-residency-controls.md#dms-replication-not-public")
- [arn:aws:controltower:REGION::control/AWS-GR_EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK](../userguide/data-residency-controls.md#ebs-snapshot-public-restorable-check "../userguide/data-residency-controls.md#ebs-snapshot-public-restorable-check")
- [arn:aws:controltower:REGION::control/AWS-GR_EC2_INSTANCE_NO_PUBLIC_IP](../userguide/data-residency-controls.md#ec2-instance-no-public-ip "../userguide/data-residency-controls.md#ec2-instance-no-public-ip")
- [arn:aws:controltower:REGION::control/AWS-GR_EKS_ENDPOINT_NO_PUBLIC_ACCESS](../userguide/data-residency-controls.md#eks-endpoint-no-public-access "../userguide/data-residency-controls.md#eks-endpoint-no-public-access")
- [arn:aws:controltower:REGION::control/AWS-GR_ELASTICSEARCH_IN_VPC_ONLY](../userguide/data-residency-controls.md#elasticsearch-in-vpc-only "../userguide/data-residency-controls.md#elasticsearch-in-vpc-only")
- [arn:aws:controltower:REGION::control/AWS-GR_EMR_MASTER_NO_PUBLIC_IP](../userguide/data-residency-controls.md#emr-master-no-public-ip "../userguide/data-residency-controls.md#emr-master-no-public-ip")
- [arn:aws:controltower:REGION::control/AWS-GR_LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED](../userguide/data-residency-controls.md#lambda-function-public-access-prohibited "../userguide/data-residency-controls.md#lambda-function-public-access-prohibited")
- [arn:aws:controltower:REGION::control/AWS-GR_NO_UNRESTRICTED_ROUTE_TO_IGW](../userguide/data-residency-controls.md#no-unrestricted-route-to-igw "../userguide/data-residency-controls.md#no-unrestricted-route-to-igw")
- [arn:aws:controltower:REGION::control/AWS-GR_REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK](../userguide/data-residency-controls.md#redshift-cluster-public-access-check "../userguide/data-residency-controls.md#redshift-cluster-public-access-check")
- [arn:aws:controltower:REGION::control/AWS-GR_S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS_PERIODIC](../userguide/data-residency-controls.md#s3-account-level-public-access-blocks-periodic "../userguide/data-residency-controls.md#s3-account-level-public-access-blocks-periodic")
- [arn:aws:controltower:REGION::control/AWS-GR_SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS](../userguide/data-residency-controls.md#sagemaker-notebook-no-direct-internet-access "../userguide/data-residency-controls.md#sagemaker-notebook-no-direct-internet-access")
- [arn:aws:controltower:REGION::control/AWS-GR_SSM_DOCUMENT_NOT_PUBLIC](../userguide/data-residency-controls.md#ssm-document-not-public "../userguide/data-residency-controls.md#ssm-document-not-public")

###### Designations for legacy Strongly

recommended controls

- [arn:aws:controltower:REGION::control/AWS-GR_ENCRYPTED_VOLUMES](../userguide/strongly-recommended-controls.md#ebs-enable-encryption "../userguide/strongly-recommended-controls.md#ebs-enable-encryption")
- [arn:aws:controltower:REGION::control/AWS-GR_EBS_OPTIMIZED_INSTANCE](../userguide/strongly-recommended-controls.md#disallow-not-ebs-optimized "../userguide/strongly-recommended-controls.md#disallow-not-ebs-optimized")
- [arn:aws:controltower:REGION::control/AWS-GR_EC2_VOLUME_INUSE_CHECK](../userguide/strongly-recommended-controls.md#disallow-unattached-ebs "../userguide/strongly-recommended-controls.md#disallow-unattached-ebs")
- [arn:aws:controltower:REGION::control/AWS-GR_RDS_INSTANCE_PUBLIC_ACCESS_CHECK](../userguide/strongly-recommended-controls.md#disallow-rds-public-access "../userguide/strongly-recommended-controls.md#disallow-rds-public-access")
- [arn:aws:controltower:REGION::control/AWS-GR_RDS_SNAPSHOTS_PUBLIC_PROHIBITED](../userguide/strongly-recommended-controls.md#disallow-rds-snapshot-public-access "../userguide/strongly-recommended-controls.md#disallow-rds-snapshot-public-access")
- [arn:aws:controltower:REGION::control/AWS-GR_RDS_STORAGE_ENCRYPTED](../userguide/strongly-recommended-controls.md#disallow-rds-storage-unencrypted "../userguide/strongly-recommended-controls.md#disallow-rds-storage-unencrypted")
- [arn:aws:controltower:REGION::control/AWS-GR_RESTRICTED_COMMON_PORTS](../userguide/strongly-recommended-controls.md#rdp-disallow-internet "../userguide/strongly-recommended-controls.md#rdp-disallow-internet")
- [arn:aws:controltower:REGION::control/AWS-GR_RESTRICTED_SSH](../userguide/strongly-recommended-controls.md#ssh-disallow-internet "../userguide/strongly-recommended-controls.md#ssh-disallow-internet")
- [arn:aws:controltower:REGION::control/AWS-GR_RESTRICT_ROOT_USER](../userguide/strongly-recommended-controls.md#disallow-root-auser-actions "../userguide/strongly-recommended-controls.md#disallow-root-auser-actions")
- [arn:aws:controltower:REGION::control/AWS-GR_RESTRICT_ROOT_USER_ACCESS_KEYS](../userguide/strongly-recommended-controls.md#disallow-root-access-keys "../userguide/strongly-recommended-controls.md#disallow-root-access-keys")
- [arn:aws:controltower:REGION::control/AWS-GR_ROOT_ACCOUNT_MFA_ENABLED](../userguide/strongly-recommended-controls.md#enable-root-mfa "../userguide/strongly-recommended-controls.md#enable-root-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR_S3_BUCKET_PUBLIC_READ_PROHIBITED](../userguide/strongly-recommended-controls.md#s3-disallow-public-read "../userguide/strongly-recommended-controls.md#s3-disallow-public-read")
- [arn:aws:controltower:REGION::control/AWS-GR_S3_BUCKET_PUBLIC_WRITE_PROHIBITED](../userguide/strongly-recommended-controls.md#s3-disallow-public-write "../userguide/strongly-recommended-controls.md#s3-disallow-public-write")
- [arn:aws:controltower:REGION::control/AWS-GR_DETECT_CLOUDTRAIL_ENABLED_ON_MEMBER_ACCOUNTS](../userguide/strongly-recommended-controls.md#ensure-cloudtrail-enabled-recommended "../userguide/strongly-recommended-controls.md#ensure-cloudtrail-enabled-recommended")
