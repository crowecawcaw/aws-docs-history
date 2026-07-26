# Restore an Amazon EKS cluster

You can restore EKS cluster backups using the AWS Backup console or CLI.
EKS backups are composite recovery points that include both EKS cluster state and
persistent volume backups.

AWS Backup supports multiple restore experiences including granular namespace-level restores.
Restores are non-destructive and will not overwrite any existing Kubernetes objects in your target EKS cluster.
Restores will also not overwrite the Kubernetes versions of the target EKS cluster.

EKS Backups have to be restored to a target EKS cluster,
meaning an Amazon EKS cluster that has been pre-provisioned. As part of the restore workflow,
you can opt to create a new EKS cluster which AWS Backup will create on your behalf.

###### Note

AWS Backup will provide a limited set of options for creating a new EKS cluster as a part of a restore.
For all EKS cluster creation functionality, customers can create a new EKS cluster using
the [EKS Console](https://console.aws.amazon.com/eks/home "https://console.aws.amazon.com/eks/home") or APIs and select this as their restore target.

**Restore capabilities for Amazon EKS**

| Restore type              | Restore target                                               | Restore behavior                                                                                                                                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Existing cluster restore  | Restore to the source EKS cluster or existing EKS cluster    | Restores all Kubernetes resources and persistent volumes to existing EKS clusters.<br>All restores are non-destructives and existing objects are not overwritten.<br>For objects that are skipped, you can subscribe to [SNS Notifications](backup-notifications.md "backup-notifications.md") |
| New cluster restore       | Creates a new Amazon EKS cluster as part of your EKS restore | Restore creates new EKS cluster and restores all Kubernetes resources and persistent<br>volumes to newly created cluster                                                                                                                                                                       |
| Namespace restore         | Existing Amazon EKS cluster                                  | Restores only specified namespaces, their Kubernetes resources and corresponding<br>persistent storage restores are non-destructives and existing objects are not overwritten.<br>For objects that are skipped, you can subscribe to SNS Notifications                                         |
| Peristent Storage Restore | Persistent Storage Dependent                                 | Restore individual persistent storage as standalone restores.<br>See Restore Behavior of [Amazon EBS](restoring-ebs.md "restoring-ebs.md"), [Amazon S3](restoring-s3.md "restoring-s3.md"), [Amazon EFS](restoring-efs.md "restoring-efs.md").                                                 |

**Permissions**

The permissions required depend on the restore type and target destination.

- AWS Backup's managed policy [AWSBackupServiceRolePolicyForRestores](security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForRestores "security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForRestores") contains the required
  permissions to restore your Amazon EKS cluster and EBS and EFS persistent storage.
- If your EKS Cluster contains an S3 bucket, or you are restoring the child S3 recovery
  point alone you will need to ensure the following policies or permissions within are assigned
  to your role [AWSBackupServiceRolePolicyForS3Restore](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Restore.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Restore.md").
  **Considerations before restoring**

Before you begin an EKS restore job, review the following. If you are restoring an EKS backup that has
been copied across account or region ensure you check these considerations ahead of restores to prevent
restore failures.

1. **IAM Roles**: when restoring onto a different cluster, the IAM Roles used in
   the source cluster (such as Pod identity, IRSA. OIDC provider configs etc) must be present in the
   account / region as the destination cluster.
2. **Ensure EKS Version and Compatibility**: The API Versions of the objects that
   you're wanting to restore should be the same version (or as close to as possible) and supported in
   the new cluster. AWS Backup will perform a best effort restore between EKS versions, though
   compatibility issues may arise when restoring between significantly different versions.
3. **Matching Storage Classes**: For restores to an existing EKS cluster, ensure
   that the appropriate CSI Storage Driver add-ons are installed prior to restore
4. **S3 Buckets**: When restoring an EKS cluster with S3 Buckets, ensure your
   S3 bucket are versioned and accessible in the destination account or region.
5. **Image Repository**: When restoring an EKS cluster ensure that the destination
   EKS cluster's account or region have access to the images that are being referenced as part of the
   restore. Check that your registry has the sufficient cross-region / account policy permissions.
6. **Security Groups**: Security groups should be pre-created for ALB, Pod
   Identities, EKS Node Groups etc. in the target account and region if creating a new EKS cluster
   as part of your restore
7. **EBS Availability Zones and Nodes**: The Availability Zones where you recover
   your EBS volumes should be mapped to the Availability Zone of an existing EKS node
8. **Non-destructive restores**: All EKS restores will be non-destructive and not
   overwrite Kubernetes objects of the target restore.
9. **Enable EKS Audit Logs**: Enable EKS Audit Logs for additional logging
   and troubleshooting prior to restore. You can also subscribe to
   [SNS
   notifications](backup-notifications.md "backup-notifications.md") to notify of skipped or failed objects on restore.
10. **New EKS Cluster Creation Restore Buffer**: When creating a new EKS cluster
    during restore, AWS Backup introduces a 15-minute buffer after the EKS cluster reaches an available state
    but before creating any additional EKS resources. This buffer ensures that all underlying EKS
    components are fully initialized before dependent resources are created.
11. **User data in launch template**: When creating a node group using a launch
    template, do not specify `spec.cluster` in the user data section of the launch template.
    Amazon EKS automatically injects the cluster identity parameters
    (`apiServerEndpoint`, `certificateAuthority`, and
    `serviceIpv4Cidr`) and merges them with any additional configurations
    defined in the user data.
    **EKS Configurations**

When you restore the composite Amazon AWS Backup, you choose the restore type and target destination.
You can choose to restore to the source EKS cluster,
an existing EKS cluster or create a new EKS cluster as the restore target.
For new EKS clusters, you can choose to use the same existing infrastructure settings
(e.g. VPC, subnets) as the backed up cluster or configure new ones.
AWS Backup is designed to perform a non-destructive restore that doesn't overwrite existing resources.

For namespace restores, you can specify up to 5 namespaces to restore selectively.
Only namespace-scoped resources are restored, while cluster-scoped resources are
excluded except for related persistent volumes.

As an advanced setting you can opt to change the restore order of the Kubernetes Objects.
By Default, AWS Backup will restore all Kubernetes objects in the following order:

**Cluster Scoped Kubernetes Resources**

1. Custom Resource Definitions
2. Namespaces (the namespace itself, not the resources within that namespace)
3. StorageClasses
4. PersistentVolumes
   **Namespace Scoped Kubernetes Resources**

5. PersistentVolumeClaims
6. Secrets
7. ConfigMaps
8. ServiceAccounts
9. LimitRanges
10. Pods
11. ReplicaSets
    **Persistent Storage Configurations**

As part of the composite Amazon EKS backup restore,
the second step will be to configure your Persistent Storage configurations.
This will vary based on the persistent storage backed up as part of your EKS cluster.

For Amazon EBS Snapshots you are required to provide an Availability Zone,
where the Amazon EBS volume will be restored and created.
AWS Backup will then attempt to create the EKS pod in the same availability zone
as selected so your volume can be remounted to your EKS cluster as part of restore.

As part of the restore, AWS Backup will remount your Amazon EBS volumes
and Amazon S3 buckets to your restored EKS cluster.
Amazon EFS filesystems restore to random prefixes and require manual access point creation
after restore to remount to your EKS cluster.
AWS Backup does not create access points or mount targets on your behalf,
refer to guidance here for [access points](../../../efs/latest/ug/create-access-point.md "../../../efs/latest/ug/create-access-point.md") and [mount targets](../../../efs/latest/ug/manage-fs-access-create-delete-mount-targets.md "../../../efs/latest/ug/manage-fs-access-create-delete-mount-targets.md").

## Amazon EKS restore procedure

Follow these steps to restore Amazon EKS backups using the AWS Backup console or AWS CLI:

Console

###### To restore your Amazon EKS cluster

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Backup vaults**.
3. Choose the backup vault that contains your Amazon EKS backup, then select the recovery point for your Amazon EKS backup.
4. Choose **Restore**.
5. In the **Restore options** pane, choose your restore type:

   - **Restore full EKS cluster** - Restores the entire Amazon EKS composite recovery point
   - **Select namespaces to restore** - Restores up to five specific namespaces

6. Configure the target destination:

   - For cluster restore, choose to create a new cluster or use an existing cluster
   - For new clusters, specify cluster name, Kubernetes version, VPC configuration, IAM roles, subnets, Additional security groups, node group settings, fargate profiles and Pod identity IAM roles
   - For existing clusters, select the target cluster from the dropdown
   - For namespace restore, specify the target cluster and namespace names

7. Optionally, configure advanced settings for custom restore order for Kubernetes resources.
8. Choose the IAM restore role for the job. If not using the default role, ensure the selected role includes the iam:PassRole permission.
9. Choose **Restore backup**.

AWS CLI
Use the `aws backup start-restore-job` command with Amazon EKS-specific metadata.

The required metadata depends on your restore type. All restore operations require the `clusterName` parameter.

**Restore Amazon EKS recovery points through AWS CLI**

Use StartRestoreJob. You can specify the following metadata during Amazon EKS restores:

**Mandatory metadata:**

- `clusterName` - Name of cluster to restore to

**Optional metadata:**

- `newCluster` - (true/false) If we should create a new EKS cluster during restore. If newCluster is "true", the following metadata fields apply:

  - `eksClusterVersion` - Desired K8s version of cluster if wanting to increase cluster version during restore
  - `clusterRole` - The IAM Role ARN to attach to the created EKS cluster
  - `encryptionConfigProviderKeyArn` - Specify the KMS key ARN to encrypt the destination cluster.
    This can be either the KMS key from the source cluster, or a different KMS key.
    A different KMS key must be provided when performing cross-region or cross-account restore.
    Omit this metadata entirely if the source cluster is not encrypted.
  - `clusterVpcConfig` - VPC/Networking configuration for the created EKS cluster. This field has the following nested fields:

    - `vpcId` - The VPC associated with your cluster
    - `subnetIds [Required]` - The subnets associated with your cluster
    - `securityGroupIds [Required]` - The additional security groups associated with your cluster

  - `nodeGroups` - The Managed Node Groups to be created on the EKS Cluster. The NodeGroups for restore must have all of the same node groups from backup time and have matching nodeGroupId.

    - `nodeGroupId [Required]` - The ID of the node group
    - `subnetIds [Required]` - The subnets that were specified for the Auto Scaling group that is associated with your node group
    - `instanceTypes` - If the node group wasn't deployed with a launch template, then this is the instance type that is associated with the node group
    - `nodeRole [Required]` - The IAM role associated with your node group
    - `securityGroupIds` - The security group IDs that are allowed SSH access to the nodes
    - `remoteAccessEc2SshKey` - The Amazon EC2 SSH key name that provides access for SSH communication with the nodes in the managed node group
    - `launchTemplateId` - Specify the launch template ID to create the node group.
      This can be either the launch template ID from the source cluster, or a different launch template ID.
      If the source cluster's launch template contains hard-coded endpoint that points to the source cluster itself, you must provide a different launch template ID.
      Omit this metadata entirely if the source cluster does not use a launch template.
    - `launchTemplateVersion` - Launch template version associated with the specified launch template ID.

  - `fargateProfiles` - The Fargate Profiles to be created on the EKS Cluster. The Fargate Profiles for restore must have all the same Fargate Profiles from backup time and have matching name.

    - `name [Required]` - The name of the Fargate profile
    - `subnetIds` - The IDs of subnets to launch a Pod into
    - `podExecutionRoleArn [Required]` - The IAM Role ARN of the Pod execution role to use for a Pod that matches the selectors in the Fargate profile

  - `podIdentityAssociations` - The Pod Identity Associations to be created on the EKS Cluster

    - `associationId` - The ID of the Pod Identity Association
    - `roleArn` - The IAM Role ARN for the Pod Identity Association

- `kubernetesRestoreOrder` - Override the order the Kubernetes manifests are restored in. This order will take precedence over the default service restore order. This follow the format: group/version/kind or version/kind

Ex: `["v1/persistentvolumes","v1/pods","customresource/v2/custom"]`

- `namespaceLevelRestore` - (true/false) If you would like to perform a namespace level restore
- `namespaces` - A list of namespaces to restore if namespaceLevelRestore is "true". Can provide up to 5 namespaces to restore.

Ex: `["ns-1","ns-2","ns-3","ns-4","ns-5"]`

- `restoreKubernetesManifestsOnly` - (true/false) If you would like to only restore the Kubernetes manifest files and no persistent storage systems (EBS, S3, EFS, etc.)
- `nestedRestoreJobs` - Restore Metadata configuration of all of the nested Recovery Points for the PersistentVolume storage systems in the composite Recovery Point. This is a map of RecoveryPointArn: RestoreMetadata of that Recovery Point

**Restore to existing cluster**

```
aws backup start-restore-job \
    --recovery-point-arn "arn:aws:backup:us-west-2:123456789012:recovery-point:composite:eks/my-cluster-20240115" \
    --iam-role-arn "arn:aws:iam::123456789012:role/AWSBackupDefaultServiceRole" \
    --metadata '{"clusterName":"existing-cluster","newCluster":"false"}' \
    --resource-type "EKS"
```

**Restore specific namespaces to an existing cluster:**

```
aws backup start-restore-job \
    --recovery-point-arn "arn:aws:backup:us-west-2:123456789012:recovery-point:composite:eks/my-cluster-20240115" \
    --iam-role-arn "arn:aws:iam::123456789012:role/AWSBackupDefaultServiceRole" \
    --metadata '{"clusterName":"existing-cluster","newCluster":"false","namespaceLevelRestore":"true","namespaces":"[\"ns-1\",\"ns-2\",\"ns-3\",\"ns-4\",\"ns-5\"]"}' \
    --resource-type "EKS"
```

**Restore nested persistent volumes to an existing cluster:**

```
aws backup start-restore-job \
    --recovery-point-arn "arn:aws:backup:us-west-2:123456789012:recovery-point:composite:eks/my-cluster-20240115" \
    --iam-role-arn "arn:aws:iam::123456789012:role/AWSBackupDefaultServiceRole" \
    --metadata '{"clusterName":"existing-cluster","newCluster":"false","namespaceLevelRestore":"true","nestedrestorejobs":"{\"arn:aws:ec2:us-west-2::snapshot/snap-abc123\":\"{\\\"AvailabilityZone\\\":\\\"us-west-2a\\\"}\",\"arn:aws:backup:us-west-2:123456789012:recovery-point:fa71a304-2555-4c37-8128-f154b9578032\":\"{\\\"DestinationBucketName\\\":\\\"bucket-name\\\"}\"}"}' \
    --resource-type "EKS"
```

**Restore to new cluster**

```
aws backup start-restore-job \
    --recovery-point-arn "arn:aws:backup:us-west-2:123456789012:recovery-point:composite:eks/my-cluster-20240115" \
    --iam-role-arn "arn:aws:iam::123456789012:role/AWSBackupDefaultServiceRole" \
    --metadata '{"clusterName":"new-cluster","newCluster":"true","clusterRole":"arn:aws:iam::123456789012:role/EKSClusterRole","eksClusterVersion":"1.33","encryptionConfigProviderKeyArn":"arn:aws:kms:us-west-2:123456789012:key/ecb2b326-784d-4ec0-8d07-20ab826b5a13","clusterVpcConfig":"{\"vpcId\":\"vpc-1234\",\"subnetIds\":[\"subnet-1\",\"subnet-2\",\"subnet-3\"],\"securityGroupIds\":[\"sg-123\"]}","nodeGroups":"[{\"nodeGroupId\":\"nodegroup-1\",\"subnetIds\":[\"subnet-1\",\"subnet-2\",\"subnet-3\"],\"nodeRole\":\"arn:aws:iam::123456789012:role/EKSNodeGroupRole\",\"instanceTypes\":[\"t3.small\"],\"launchTemplateId\":\"lt-0b13949aae3f2b867\",\"launchTemplateVersion\":\"1\"}]","fargateProfiles":"[{\"name\":\"fargate-profile-1\",\"subnetIds\":[\"subnet-1\",\"subnet-2\",\"subnet-3\"],\"podExecutionRoleArn\":\"arn:aws:iam::123456789012:role/EKSFargateProfileRole\"}]"}' \
    --resource-type "EKS"
```

After starting the restore job, use `describe-restore-job` to monitor progress:

```
aws backup describe-restore-job --restore-job-id `restore-job-id`
```

You can subscribe to **Notification Events** for failed and skipped objects for restore.
For more information, see [Notification options with AWS Backup.](backup-notifications.md "backup-notifications.md")

**Amazon EKS restore status messages**

When a restore job completes, you might see the following status messages.
The table shows the possible scenarios and their corresponding job status values:

| Scenario                                  | Job Status | Example message                                                                                                        |
| ----------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------- |
| All objects restored successfully         | COMPLETED  | —                                                                                                                      |
| One or more objects failed to be restored | COMPLETED  | "One or more Kubernetes objects failed to restore. To get notified of these failures, enable SNS event notifications." |
| Restore could not complete                | FAILED     | (error details)                                                                                                        |

**Skipped objects during restore**

The following Kubernetes objects are restored on a best-effort basis. If they fail to
restore, they are moved to the skipped list. These objects are system-managed and
recreated by Kubernetes or Amazon EKS:

- FlowSchemas with the `apf.kubernetes.io/autoupdate-spec: "true"` annotation
- PriorityLevelConfigurations with the `apf.kubernetes.io/autoupdate-spec: "true"` annotation
- The `eks-exempt` FlowSchema (EKS-managed, references the protected exempt PriorityLevelConfiguration)
- The `kubernetes` Service in the `default` namespace (API server endpoint)
- The `kube-dns` Service in the `kube-system` namespace (CoreDNS)
  The following Kubernetes objects are always skipped during a restore. These objects include
  node infrastructure and networking components. They reference cluster-specific state. Kubernetes controllers
  automatically recreate these objects when nodes and services become active in the target cluster. If you
  restore these objects from a backup, they might cause conflicts or errors. These conflicts occur because
  the restored objects reference resources that don't exist on the target cluster.

- Endpoints (`v1/endpoints`) - Network endpoints that define IP addresses for Services. The Endpoints controller automatically manages these based on Service selectors.
- EndpointSlices (`discovery.k8s.io/v1/endpointslices`) - The EndpointSlice controller automatically manages these objects.
- IPAddresses (`networking.k8s.io/v1/ipaddresses`) - Kubernetes networking manages these cluster-internal IP allocations.
- CSINodes (`storage.k8s.io/v1/csinodes`) - The kubelet automatically creates these objects when CSI drivers register on a node.
- VolumeAttachments (`storage.k8s.io/v1/volumeattachments`) - The attach/detach controller automatically creates these objects when pods require volumes.
  Objects that already exist on the target cluster are also skipped. EKS restores are
  non-destructive — existing objects are never overwritten or deleted.

To receive notifications about skipped or failed objects during restore, subscribe to
[SNS event notifications](backup-notifications.md "backup-notifications.md").
For more information, see [Notification options with AWS Backup](backup-notifications.md "backup-notifications.md").

**OIDC and IRSA considerations for cross-cluster restore**

When restoring an Amazon EKS backup to a different cluster than the source,
Kubernetes objects referencing IAM Roles for Service Accounts (IRSA) retain the source
cluster's OIDC provider endpoint. These references exist in service account
annotations and IAM trust policies. AWS Backup does not automatically update them during
restore.

If your workloads use IRSA, a cross-cluster restore requires:

- The destination cluster must have an OIDC provider configured.
- All IAM roles referenced by Kubernetes service accounts must have their
  trust policies updated to include the destination cluster's OIDC provider
  endpoint.
- Service account annotations (`eks.amazonaws.com/role-arn`) will
  still reference the original roles — verify these match valid roles in the
  destination account.
  If these dependencies are not satisfied, pods will fail to assume IAM roles after
  restore, and restore jobs might report failures during validation.

**Recommendation**: For workloads that require
cross-cluster or cross-account restore portability, we recommend using
[EKS Pod Identity](../../../eks/latest/userguide/pod-identities.md "../../../eks/latest/userguide/pod-identities.md")
instead of IRSA. EKS Pod Identity does not depend on cluster-specific OIDC providers
and simplifies cross-cluster restore scenarios.
