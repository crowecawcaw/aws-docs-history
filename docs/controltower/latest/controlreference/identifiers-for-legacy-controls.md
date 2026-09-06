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

- [arn:aws:controltower:REGION::control/AWS-GR\_AUDIT\_BUCKET\_ENCRYPTION\_ENABLED](elective-preventive-controls.md#aws-gr_audit_bucket_encryption_enabled "elective-preventive-controls.md#aws-gr_audit_bucket_encryption_enabled")
- [arn:aws:controltower:REGION::control/AWS-GR\_AUDIT\_BUCKET\_LOGGING\_ENABLED](elective-preventive-controls.md#aws-gr_audit_bucket_logging_enabled "elective-preventive-controls.md#aws-gr_audit_bucket_logging_enabled")
- [arn:aws:controltower:REGION::control/AWS-GR\_AUDIT\_BUCKET\_POLICY\_CHANGES\_PROHIBITED](elective-preventive-controls.md#aws-gr_audit_bucket_policy_changes_prohibited "elective-preventive-controls.md#aws-gr_audit_bucket_policy_changes_prohibited")
- [arn:aws:controltower:REGION::control/AWS-GR\_AUDIT\_BUCKET\_RETENTION\_POLICY](elective-preventive-controls.md#aws-gr_audit_bucket_retention_policy "elective-preventive-controls.md#aws-gr_audit_bucket_retention_policy")
- [arn:aws:controltower:REGION::control/AWS-GR\_IAM\_USER\_MFA\_ENABLED](elective-detective-controls.md#disallow-access-mfa "elective-detective-controls.md#disallow-access-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR\_MFA\_ENABLED\_FOR\_IAM\_CONSOLE\_ACCESS](elective-detective-controls.md#disallow-console-access-mfa "elective-detective-controls.md#disallow-console-access-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICT\_S3\_CROSS\_REGION\_REPLICATION](elective-preventive-controls.md#aws-gr_restrict_s3_cross_region_replication "elective-preventive-controls.md#aws-gr_restrict_s3_cross_region_replication")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICT\_S3\_DELETE\_WITHOUT\_MFA](elective-preventive-controls.md#aws-gr_restrict_s3_delete_without_mfa "elective-preventive-controls.md#aws-gr_restrict_s3_delete_without_mfa")
- [arn:aws:controltower:REGION::control/AWS-GR\_S3\_VERSIONING\_ENABLED](elective-detective-controls.md#disallow-s3-no-versioning "elective-detective-controls.md#disallow-s3-no-versioning")

###### Designations for legacy Data residency controls (elective)

- [arn:aws:controltower:REGION::control/AWS-GR\_SUBNET\_AUTO\_ASSIGN\_PUBLIC\_IP\_DISABLED](data-residency-detective-controls.md#subnet-auto-assign-public-ip-disabled "data-residency-detective-controls.md#subnet-auto-assign-public-ip-disabled")
- [arn:aws:controltower:REGION::control/AWS-GR\_AUTOSCALING\_LAUNCH\_CONFIG\_PUBLIC\_IP\_DISABLED](data-residency-detective-controls.md#autoscaling-launch-config-public-ip-disabled "data-residency-detective-controls.md#autoscaling-launch-config-public-ip-disabled")
- [arn:aws:controltower:REGION::control/AWS-GR\_DISALLOW\_CROSS\_REGION\_NETWORKING](data-residency-preventive-controls.md#prevent-cross-region-networking "data-residency-preventive-controls.md#prevent-cross-region-networking")
- [arn:aws:controltower:REGION::control/AWS-GR\_DISALLOW\_VPC\_INTERNET\_ACCESS](data-residency-preventive-controls.md#disallow-vpc-internet-access "data-residency-preventive-controls.md#disallow-vpc-internet-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_DISALLOW\_VPN\_CONNECTIONS](data-residency-preventive-controls.md#prevent-vpn-connection "data-residency-preventive-controls.md#prevent-vpn-connection")
- [arn:aws:controltower:REGION::control/AWS-GR\_DMS\_REPLICATION\_NOT\_PUBLIC](data-residency-detective-controls.md#dms-replication-not-public "data-residency-detective-controls.md#dms-replication-not-public")
- [arn:aws:controltower:REGION::control/AWS-GR\_EBS\_SNAPSHOT\_PUBLIC\_RESTORABLE\_CHECK](data-residency-detective-controls.md#ebs-snapshot-public-restorable-check "data-residency-detective-controls.md#ebs-snapshot-public-restorable-check")
- [arn:aws:controltower:REGION::control/AWS-GR\_EC2\_INSTANCE\_NO\_PUBLIC\_IP](data-residency-detective-controls.md#ec2-instance-no-public-ip "data-residency-detective-controls.md#ec2-instance-no-public-ip")
- [arn:aws:controltower:REGION::control/AWS-GR\_EKS\_ENDPOINT\_NO\_PUBLIC\_ACCESS](data-residency-detective-controls.md#eks-endpoint-no-public-access "data-residency-detective-controls.md#eks-endpoint-no-public-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_ELASTICSEARCH\_IN\_VPC\_ONLY](data-residency-detective-controls.md#elasticsearch-in-vpc-only "data-residency-detective-controls.md#elasticsearch-in-vpc-only")
- [arn:aws:controltower:REGION::control/AWS-GR\_EMR\_MASTER\_NO\_PUBLIC\_IP](data-residency-detective-controls.md#emr-master-no-public-ip "data-residency-detective-controls.md#emr-master-no-public-ip")
- [arn:aws:controltower:REGION::control/AWS-GR\_LAMBDA\_FUNCTION\_PUBLIC\_ACCESS\_PROHIBITED](data-residency-detective-controls.md#lambda-function-public-access-prohibited "data-residency-detective-controls.md#lambda-function-public-access-prohibited")
- [arn:aws:controltower:REGION::control/AWS-GR\_NO\_UNRESTRICTED\_ROUTE\_TO\_IGW](data-residency-detective-controls.md#no-unrestricted-route-to-igw "data-residency-detective-controls.md#no-unrestricted-route-to-igw")
- [arn:aws:controltower:REGION::control/AWS-GR\_REDSHIFT\_CLUSTER\_PUBLIC\_ACCESS\_CHECK](data-residency-detective-controls.md#redshift-cluster-public-access-check "data-residency-detective-controls.md#redshift-cluster-public-access-check")
- [arn:aws:controltower:REGION::control/AWS-GR\_S3\_ACCOUNT\_LEVEL\_PUBLIC\_ACCESS\_BLOCKS\_PERIODIC](data-residency-detective-controls.md#s3-account-level-public-access-blocks-periodic "data-residency-detective-controls.md#s3-account-level-public-access-blocks-periodic")
- [arn:aws:controltower:REGION::control/AWS-GR\_SAGEMAKER\_NOTEBOOK\_NO\_DIRECT\_INTERNET\_ACCESS](data-residency-detective-controls.md#sagemaker-notebook-no-direct-internet-access "data-residency-detective-controls.md#sagemaker-notebook-no-direct-internet-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_SSM\_DOCUMENT\_NOT\_PUBLIC](data-residency-detective-controls.md#ssm-document-not-public "data-residency-detective-controls.md#ssm-document-not-public")

###### Designations for legacy Strongly recommended controls

- [arn:aws:controltower:REGION::control/AWS-GR\_ENCRYPTED\_VOLUMES](strongly-recommended-detective-controls.md#ebs-enable-encryption "strongly-recommended-detective-controls.md#ebs-enable-encryption")
- [arn:aws:controltower:REGION::control/AWS-GR\_EBS\_OPTIMIZED\_INSTANCE](strongly-recommended-detective-controls.md#disallow-not-ebs-optimized "strongly-recommended-detective-controls.md#disallow-not-ebs-optimized")
- [arn:aws:controltower:REGION::control/AWS-GR\_EC2\_VOLUME\_INUSE\_CHECK](strongly-recommended-detective-controls.md#disallow-unattached-ebs "strongly-recommended-detective-controls.md#disallow-unattached-ebs")
- [arn:aws:controltower:REGION::control/AWS-GR\_RDS\_INSTANCE\_PUBLIC\_ACCESS\_CHECK](strongly-recommended-detective-controls.md#disallow-rds-public-access "strongly-recommended-detective-controls.md#disallow-rds-public-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_RDS\_SNAPSHOTS\_PUBLIC\_PROHIBITED](strongly-recommended-detective-controls.md#disallow-rds-snapshot-public-access "strongly-recommended-detective-controls.md#disallow-rds-snapshot-public-access")
- [arn:aws:controltower:REGION::control/AWS-GR\_RDS\_STORAGE\_ENCRYPTED](strongly-recommended-detective-controls.md#disallow-rds-storage-unencrypted "strongly-recommended-detective-controls.md#disallow-rds-storage-unencrypted")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICTED\_COMMON\_PORTS](strongly-recommended-detective-controls.md#rdp-disallow-internet "strongly-recommended-detective-controls.md#rdp-disallow-internet")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICTED\_SSH](strongly-recommended-detective-controls.md#ssh-disallow-internet "strongly-recommended-detective-controls.md#ssh-disallow-internet")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICT\_ROOT\_USER](strongly-recommended-preventive-controls.md#disallow-root-auser-actions "strongly-recommended-preventive-controls.md#disallow-root-auser-actions")
- [arn:aws:controltower:REGION::control/AWS-GR\_RESTRICT\_ROOT\_USER\_ACCESS\_KEYS](strongly-recommended-preventive-controls.md#disallow-root-access-keys "strongly-recommended-preventive-controls.md#disallow-root-access-keys")
- [arn:aws:controltower:REGION::control/AWS-GR\_ROOT\_ACCOUNT\_MFA\_ENABLED](strongly-recommended-detective-controls.md#enable-root-mfa "strongly-recommended-detective-controls.md#enable-root-mfa")
- [arn:aws:controltower:REGION::control/AWS-GR\_S3\_BUCKET\_PUBLIC\_READ\_PROHIBITED](strongly-recommended-detective-controls.md#s3-disallow-public-read "strongly-recommended-detective-controls.md#s3-disallow-public-read")
- [arn:aws:controltower:REGION::control/AWS-GR\_S3\_BUCKET\_PUBLIC\_WRITE\_PROHIBITED](strongly-recommended-detective-controls.md#s3-disallow-public-write "strongly-recommended-detective-controls.md#s3-disallow-public-write")
- [arn:aws:controltower:REGION::control/AWS-GR\_DETECT\_CLOUDTRAIL\_ENABLED\_ON\_MEMBER\_ACCOUNTS](strongly-recommended-detective-controls.md#ensure-cloudtrail-enabled-recommended "strongly-recommended-detective-controls.md#ensure-cloudtrail-enabled-recommended")
