

# Restore an Amazon EKS cluster

You can restore EKS cluster backups using the AWS Backup console or CLI. EKS backups are composite recovery points that include both EKS cluster state and persistent volume backups.

AWS Backup supports multiple restore experiences including granular namespace-level restores. Restores are non-destructive and will not overwrite any existing Kubernetes objects in your target EKS cluster. Restores will also not overwrite the Kubernetes versions of the target EKS cluster.

EKS Backups have to be restored to a target EKS cluster, meaning an Amazon EKS cluster that has been pre-provisioned. As part of the restore workflow, you can opt to create a new EKS cluster which AWS Backup will create on your behalf.

**Note**  
AWS Backup will provide a limited set of options for creating a new EKS cluster as a part of a restore. For all EKS cluster creation functionality, customers can create a new EKS cluster using the [EKS Console](https://console.aws.amazon.com/eks/home) or APIs and select this as their restore target.

**Restore capabilities for Amazon EKS**


| Restore type | Restore target | Restore behavior | 
| --- | --- | --- | 
| Existing cluster restore | Restore to the source EKS cluster or existing EKS cluster | Restores all Kubernetes resources and persistent volumes to existing EKS clusters. All restores are non-destructives and existing objects are not overwritten. For objects that are skipped, you can subscribe to [SNS Notifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html) | 
| New cluster restore | Creates a new Amazon EKS cluster as part of your EKS restore | Restore creates new EKS cluster and restores all Kubernetes resources and persistent volumes to newly created cluster | 
| Namespace restore | Existing Amazon EKS cluster | Restores only specified namespaces, their Kubernetes resources and corresponding persistent storage restores are non-destructive and existing objects are not overwritten. All cluster-scoped resources will also be restored. For objects that are skipped, you can subscribe to SNS Notifications | 
| Peristent Storage Restore | Persistent Storage Dependent | Restore individual persistent storage as standalone restores. See Restore Behavior of [Amazon EBS](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-ebs.html), [Amazon S3](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-s3.html), [Amazon EFS](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-efs.html). | 

**Permissions**

The permissions required depend on the restore type and target destination.
+ AWS Backup's managed policy [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-iam-awsmanpol.html#AWSBackupServiceRolePolicyForRestores) contains the required permissions to restore your Amazon EKS cluster and EBS and EFS persistent storage.
+ If your EKS Cluster contains an S3 bucket, or you are restoring the child S3 recovery point alone you will need to ensure the following policies or permissions within are assigned to your role [AWSBackupServiceRolePolicyForS3Restore](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Restore.html).

**Considerations before restoring**

Before you begin an EKS restore job, review the following. If you are restoring an EKS backup that has been copied across account or region ensure you check these considerations ahead of restores to prevent restore failures.

1. **IAM Roles**: when restoring onto a different cluster, the IAM Roles used in the source cluster (such as Pod identity, IRSA. OIDC provider configs etc) must be present in the account / region as the destination cluster.

1. **Ensure EKS Version and Compatibility**: The API Versions of the objects that you're wanting to restore should be the same version (or as close to as possible) and supported in the new cluster. AWS Backup will perform a best effort restore between EKS versions, though compatibility issues may arise when restoring between significantly different versions.

1. **Matching Storage Classes**: For restores to an existing EKS cluster, ensure that the appropriate CSI Storage Driver add-ons are installed prior to restore

1. **S3 Buckets**: When restoring an EKS cluster with S3 Buckets, ensure your S3 bucket are versioned and accessible in the destination account or region.

1. **Image Repository**: When restoring an EKS cluster ensure that the destination EKS cluster's account or region have access to the images that are being referenced as part of the restore. Check that your registry has the sufficient cross-region / account policy permissions.

1. **Security Groups**: Security groups should be pre-created for ALB, Pod Identities, EKS Node Groups etc. in the target account and region if creating a new EKS cluster as part of your restore

1. **EBS Availability Zones and Nodes**: The Availability Zones where you recover your EBS volumes should be mapped to the Availability Zone of an existing EKS node

1. **Non-destructive restores**: All EKS restores will be non-destructive and not overwrite Kubernetes objects of the target restore.

1. **Enable EKS Audit Logs**: Enable EKS Audit Logs for additional logging and troubleshooting prior to restore. You can also subscribe to [SNS notifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html) to notify of skipped or failed objects on restore.

1. **New EKS Cluster Creation Restore Buffer**: When creating a new EKS cluster during restore, AWS Backup introduces a 15-minute buffer after the EKS cluster reaches an available state but before creating any additional EKS resources. This buffer ensures that all underlying EKS components are fully initialized before dependent resources are created.

1. **User data in launch template**: When creating a node group using a launch template, do not specify `spec.cluster` in the user data section of the launch template. Amazon EKS automatically injects the cluster identity parameters (`apiServerEndpoint`, `certificateAuthority`, and `serviceIpv4Cidr`) and merges them with any additional configurations defined in the user data.

1. **Amazon EKS Auto Mode and restored Amazon EBS volumes**: If the cluster has Amazon EKS Auto Mode enabled, Auto Mode only attaches an Amazon EBS volume whose `eks:eks-cluster-name` tag matches the cluster's name. AWS Backup does not update this tag on restored volumes, so pods referencing restored volumes might remain in `ContainerCreating` with `FailedAttachVolume` errors when restoring to a different cluster, even though the restore job succeeds. To resolve this, manually tag each restored Amazon EBS volume with the destination cluster's name with the following command: `aws ec2 create-tags --resources vol-123456abcdef --tags Key=eks:eks-cluster-name,Value=destination-cluster-name`

**EKS Configurations**

When you restore the composite Amazon AWS Backup, you choose the restore type and target destination. You can choose to restore to the source EKS cluster, an existing EKS cluster or create a new EKS cluster as the restore target. For new EKS clusters, you can choose to use the same existing infrastructure settings (for example, VPC, subnets) as the backed up cluster or configure new ones. AWS Backup is designed to perform a non-destructive restore that doesn't overwrite existing resources.

For namespace restores, you can specify up to 5 namespaces to restore selectively. We will also restore all cluster-scoped resources as well.

As an advanced setting you can opt to change the restore order of the Kubernetes Objects. By Default, AWS Backup will restore all Kubernetes objects in the following order: 

**Cluster Scoped Kubernetes Resources**

1. Custom Resource Definitions

1. Namespaces (the namespace itself, not the resources within that namespace)

1. StorageClasses

1. PersistentVolumes

**Namespace Scoped Kubernetes Resources**

1. PersistentVolumeClaims

1. Secrets

1. ConfigMaps

1. ServiceAccounts

1. LimitRanges

1. Pods

1. ReplicaSets

**Persistent Storage Configurations**

As part of the composite Amazon EKS backup restore, the second step will be to configure your Persistent Storage configurations. This will vary based on the persistent storage backed up as part of your EKS cluster.

For Amazon EBS Snapshots you are required to provide an Availability Zone, where the Amazon EBS volume will be restored and created. AWS Backup will then attempt to create the EKS pod in the same availability zone as selected so your volume can be remounted to your EKS cluster as part of restore.

As part of the restore, AWS Backup will remount your Amazon EBS volumes and Amazon S3 buckets to your restored EKS cluster. Amazon EFS filesystems restore to random prefixes and require manual access point creation after restore to remount to your EKS cluster. AWS Backup does not create access points or mount targets on your behalf, refer to guidance here for [ access points](https://docs.aws.amazon.com/efs/latest/ug/create-access-point.html) and [mount targets](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-create-delete-mount-targets.html).

## Restore customizations
<a name="eks-restore-customizations"></a>

AWS Backup can customize your Kubernetes objects during an Amazon EKS restore. You define *resource modifiers*, a set of rules that transform objects before they are restored to the target cluster. These customizations are applied in memory during the restore and do not alter the original backup data.

Resource modifiers are particularly useful when a restored cluster contains references to the source environment that must be updated for the destination, such as container image registry URIs, database endpoints, or storage class names. This is common in cross-Region and cross-account disaster recovery, where the restored objects would otherwise point at resources that do not exist in the destination. You can use resource modifiers for any change you need to make to your objects as they are restored.

### Providing resource modifiers
<a name="eks-restore-customizations-providing"></a>

1. Create a resource modifiers file in YAML format.

1. Upload the file to an Amazon S3 bucket in the same account and Region from which you start the restore job.

1. Pass the Amazon S3 URI of the file in the `resourceModifiers` restore metadata key when you start the restore job.

AWS Backup reads the file once, when you start the restore job, and uses that copy for the whole restore. Changing or deleting the file after you start the restore job has no effect on that restore.

The principal that calls `StartRestoreJob` must have `s3:GetObject` permission on the resource modifiers file. This is the identity making the API call, not the role you pass in `iam-role-arn`.

The file must be valid UTF-8 YAML, must set `version: v1`, and must not exceed 1 MB. It must not use YAML anchors or aliases, and it must not contain duplicate keys. AWS Backup validates the file when you submit the restore job and rejects the job before it starts if the file is missing, inaccessible, or invalid.

The file must be in an Amazon S3 bucket in the same AWS account and Region as the restore job. If the bucket has a bucket policy, make sure that it does not deny the calling principal. AWS Backup reads the file on your behalf rather than from your network, so a policy that restricts access to a specific VPC endpoint, IP address range, or principal list blocks the read even when your IAM permissions are correct.

The `resourceModifiers` restore metadata key is optional. If you omit it, the restore proceeds with no customer-defined modifications.

### Resource modifiers file schema
<a name="eks-restore-customizations-schema"></a>

```yaml
version: v1
resourceModifierRules:
  - conditions:
      groupResource: group/version/resource   # ex: apps/v1/deployments, or v1/pods for core resources
      resourceNameRegex: string               # ex: my-pod.*
      namespaces:
        - namespace1
        - namespace2
      labelSelector:
        matchLabels:
          foo: bar
          test: label
    patches:
      - operation: replace
        path: "/spec/storageClassName"
        value: "new-sc"
      - operation: remove
        path: "/metadata/uid"
```

Each rule consists of conditions, which decide which objects are modified, and patches, which decide what is modified in those objects.

### Conditions
<a name="eks-restore-customizations-conditions"></a>

Conditions decide which objects a rule applies to. All conditions are optional, but each rule **must specify** at least one. When a rule specifies more than one condition, an object must match all of them.
+ `groupResource` - The Kubernetes group, version, and plural resource name that the patches apply to, in the form `group/version/resource`, or `version/resource` for core resources that have no group. The last segment is the plural resource name reported by the Kubernetes API, such as `deployments` or `pods`, not the object kind. A rule whose `groupResource` does not correspond to a resource in the backup matches no objects, and the restore job completes without applying it.
+ `resourceNameRegex` - A regular expression matched against the object's name, using RE2 syntax. RE2 does not support lookarounds or backreferences. The expression must match the entire name, not part of it, so `my-pod` matches only an object named exactly `my-pod`. To match a family of names, use `my-pod.*`. Omit this condition to match objects with any name.
+ `namespaces` - A list of namespaces that the objects must be in. If omitted or empty, the rule matches objects in all namespaces. This is the namespace name as stored in the backed-up object, not the namespace the object is restored into.
+ `labelSelector` - A set of key and value label pairs. An object matches only if it has all of the specified labels with exactly the specified values. An object with no labels never matches a rule that specifies a label selector.

### Patches
<a name="eks-restore-customizations-patches"></a>

Patches decide what is modified in the matched objects. Each rule must specify at least one patch. AWS Backup applies each patch as a JSON Patch `add`, `remove`, or `replace` operation, and `path` uses JSON Pointer syntax, including array indexes. Each patch supports the following fields:
+ `operation` - The modification to perform, one of `add`, `remove`, or `replace`.
+ `path` - The JSON Pointer to the field to modify. For example, `/spec/storageClassName` targets the value at `spec.storageClassName`.
+ `value` - The value to apply. Required for `add` and `replace`, and not allowed for `remove`. AWS Backup treats a null value as no value, so it rejects the restore job if an `add` or `replace` patch omits `value` or sets it to null, or if a `remove` patch specifies `value`.

The parent path of a patch must already exist on the object. `add` creates only the final field in the path, so adding `/metadata/labels/team` to an object that has no `labels` map fails.

Unlike a standalone JSON Patch document, which is applied all-or-nothing, AWS Backup continues applying the remaining operations after one of them fails.

**Patching arrays**

To target an element of an array, use its zero-based index in the path. For example, `/spec/template/spec/containers/0/image` is the image of the first container.
+ `add` with an index inserts the value at that position and moves later elements back by one. Use `-` as the index to append to the end of the array, for example `/spec/template/spec/containers/-`.
+ `replace` and `remove` with an index change or delete the element at that position.

The following patches fail at run time:
+ An `add` whose index is greater than the length of the array.
+ A `replace` or `remove` whose index does not exist in the array.
+ A `replace` or `remove` that uses `-` as the index.

Paths do not support wildcards. To change the same field in several array elements, such as the image of every container, specify one patch for each index.

### Order of application
<a name="eks-restore-customizations-order"></a>
+ You can specify multiple patches for a single rule. Patches are applied in the order listed. If multiple patches target the same `path`, the last one takes effect.
+ You can specify multiple rules in the file. Rules are applied in the order listed. AWS Backup does not give precedence to the most specific match, so place your most specific rule last to give it the final say.

### Modification results and notifications
<a name="eks-restore-customizations-results"></a>

A patch can fail at run time if the `path` it targets does not exist on the matched object, for example targeting `/spec/containers/3/image` on an object that has only two containers. When a patch fails at run time:
+ Only the failed operation is skipped. Operations listed before it in the same rule stay applied, operations after it are still attempted, and changes made by earlier rules are kept. AWS Backup still attempts to restore the object with whatever modifications succeeded, so if it restores, it can be partially modified rather than unmodified.
+ The modification failure does not change the job status. If any modification failed, the job's status message includes "Some Kubernetes Objects were restored without their requested modifications." Status messages are additive, so this message can appear alongside other messages from the same restore.

A patch that applies successfully can still produce an object that your cluster does not accept, for example by removing a field the object requires or by setting a field to a value of the wrong type. AWS Backup does not check whether a modified object is still valid, so your cluster rejects it during the restore and that object fails to restore. Other objects in the same restore are not affected. Test your resource modifiers with a non-production restore before you rely on them.

To get details about which objects were modified or failed to be modified, subscribe to the following SNS event notifications:
+ `EKS_RESTORE_MODIFICATION_SUCCESS` - One or more rules matched an object and every patch was applied successfully.
+ `EKS_RESTORE_MODIFICATION_FAILED` - A rule matched an object but one of its patches failed to apply at run time. AWS Backup still attempts to restore the object, with whatever other modifications succeeded.

AWS Backup reports these events once per object. For more information, see [ Notification options with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html).

### Example: cross-account, cross-Region restore
<a name="eks-restore-customizations-example"></a>

The following resource modifiers file is used when restoring from account `111122223333` in `us-east-1` to account `444455556666` in `us-west-2`. It updates the container image and database endpoint of the `payment` Deployment in the `production` namespace, and adds an annotation recording the backup it was restored from. The Deployment must already have an `annotations` map for the third patch to apply.

```yaml
version: v1
resourceModifierRules:
  - conditions:
      groupResource: apps/v1/deployments
      namespaces:
        - production
      labelSelector:
        matchLabels:
          app: payment
    patches:
      - operation: replace
        path: "/spec/template/spec/containers/0/image"
        value: "444455556666.dkr.ecr.us-west-2.amazonaws.com/payment-service:v2.1.0"
      - operation: replace
        path: "/spec/template/spec/containers/0/env/0/value"
        value: "payment-db.cluster-dst789.us-west-2.rds.amazonaws.com"
      - operation: add
        path: "/metadata/annotations/backup.aws.com~1restored-from"
        value: "arn:aws:backup:us-east-1:111122223333:recovery-point:rp-abc123"
```

**Note**  
In JSON Pointer paths, `~1` is the escape sequence for a literal `/` in a key name, so `backup.aws.com~1restored-from` refers to the annotation key `backup.aws.com/restored-from`.

#### The Deployment before and after these rules
<a name="eks-restore-customizations-example-before-after"></a>

These excerpts show only the fields that the three patches change.

**In the recovery point**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment
  namespace: production
  labels:
    app: payment
  annotations:
    team: payments
spec:
  template:
    spec:
      containers:
        - name: payment-service
          image: 111122223333.dkr.ecr.us-east-1.amazonaws.com/payment-service:v2.1.0
          env:
            - name: DB_HOST
              value: payment-db.cluster-src123.us-east-1.rds.amazonaws.com
```

**Restored to the cluster**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment
  namespace: production
  labels:
    app: payment
  annotations:
    team: payments
    backup.aws.com/restored-from: arn:aws:backup:us-east-1:111122223333:recovery-point:rp-abc123
spec:
  template:
    spec:
      containers:
        - name: payment-service
          image: 444455556666.dkr.ecr.us-west-2.amazonaws.com/payment-service:v2.1.0
          env:
            - name: DB_HOST
              value: payment-db.cluster-dst789.us-west-2.rds.amazonaws.com
```

The first two `replace` patches changed the container image and the database endpoint, and the `add` patch added the `restored-from` annotation to the existing `annotations` map. The recovery point is not changed.

## Amazon EKS restore procedure
<a name="eks-restore-backup-section"></a>

Follow these steps to restore Amazon EKS backups using the AWS Backup console or AWS CLI:

------
#### [ Console ]

**To restore your Amazon EKS cluster**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the navigation pane, choose **Backup vaults**.

1. Choose the backup vault that contains your Amazon EKS backup, then select the recovery point for your Amazon EKS backup.

1. Choose **Restore**.

1. In the **Restore options** pane, choose your restore type:
   + **Restore full EKS cluster** - Restores the entire Amazon EKS composite recovery point
   + **Select namespaces to restore** - Restores up to five specific namespaces

1. Configure the target destination:
   + For cluster restore, choose to create a new cluster or use an existing cluster
   + For new clusters, specify cluster name, Kubernetes version, VPC configuration, IAM roles, subnets, Additional security groups, node group settings, fargate profiles and Pod identity IAM roles
   + For existing clusters, select the target cluster from the dropdown
   + For namespace restore, specify the target cluster and namespace names

1. Optionally, configure advanced settings for custom restore order for Kubernetes resources.

1. Choose the IAM restore role for the job. If not using the default role, ensure the selected role includes the iam:PassRole permission.
**Note**  
If role manager is enabled in your account, AWS Backup selects the default service role for you, and a **Customize** option is available. For more information, see [IAM role creation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.

1. Choose **Restore backup**.

------
#### [ AWS CLI ]

Use the `aws backup start-restore-job` command with Amazon EKS-specific metadata.

The required metadata depends on your restore type. All restore operations require the `clusterName` parameter.

**Restore Amazon EKS recovery points through AWS CLI**

Use StartRestoreJob. You can specify the following metadata during Amazon EKS restores:

**Mandatory metadata:**
+ `clusterName` - Name of cluster to restore to

**Optional metadata:**
+ `newCluster` - (true/false) If we should create a new EKS cluster during restore. If newCluster is "true", the following metadata fields apply:
  + `eksClusterVersion` - Desired K8s version of cluster if wanting to increase cluster version during restore
  + `clusterRole` - The IAM Role ARN to attach to the created EKS cluster
  + `controlPlaneScalingTier` - The control plane scaling tier for the new cluster. If you omit this field, the restore uses the tier captured in the backup, or the Standard control plane if no tier was captured. To restore a provisioned control plane as Standard, specify `standard`. For available tier values, see [Amazon EKS Provisioned Control Plane](https://docs.aws.amazon.com/eks/latest/userguide/eks-provisioned-control-plane.html).
  + `encryptionConfigProviderKeyArn` - Specify the KMS key ARN to encrypt the destination cluster. This can be either the KMS key from the source cluster, or a different KMS key. A different KMS key must be provided when performing cross-region or cross-account restore. Omit this metadata entirely if the source cluster is not encrypted.
  + `clusterVpcConfig` - VPC/Networking configuration for the created EKS cluster. This field has the following nested fields:
    + `vpcId` - The VPC associated with your cluster
    + `subnetIds [Required]` - The subnets associated with your cluster
    + `securityGroupIds [Required]` - The additional security groups associated with your cluster
  + `computeConfig` - The compute configuration for clusters created with Amazon EKS Auto Mode. This field has the following nested field:
    + `nodeRoleArn` - The IAM role ARN that Amazon EKS Auto Mode attaches to the nodes. If omitted, the restore uses the node role from the source cluster. When performing a cross-account restore, you must provide a node role in the destination account. Otherwise, the restore fails.
  + `nodeGroups` - The Managed Node Groups to be created on the EKS Cluster. The NodeGroups for restore must have all of the same node groups from backup time and have matching nodeGroupId.
    + `nodeGroupId [Required]` - The ID of the node group
    + `subnetIds [Required]` - The subnets that were specified for the Auto Scaling group that is associated with your node group
    + `instanceTypes` - If the node group wasn't deployed with a launch template, then this is the instance type that is associated with the node group
    + `nodeRole [Required]` - The IAM role associated with your node group
    + `securityGroupIds` - The security group IDs that are allowed SSH access to the nodes
    + `remoteAccessEc2SshKey` - The Amazon EC2 SSH key name that provides access for SSH communication with the nodes in the managed node group
    + `launchTemplateId` - Specify the launch template ID to create the node group. This can be either the launch template ID from the source cluster, or a different launch template ID. If the source cluster's launch template contains hard-coded endpoint that points to the source cluster itself, you must provide a different launch template ID. Omit this metadata entirely if the source cluster does not use a launch template.
    + `launchTemplateVersion` - Launch template version associated with the specified launch template ID.
  + `fargateProfiles` - The Fargate Profiles to be created on the EKS Cluster. The Fargate Profiles for restore must have all the same Fargate Profiles from backup time and have matching name.
    + `name [Required]` - The name of the Fargate profile
    + `subnetIds` - The IDs of subnets to launch a Pod into
    + `podExecutionRoleArn [Required]` - The IAM Role ARN of the Pod execution role to use for a Pod that matches the selectors in the Fargate profile
  + `podIdentityAssociations` - The Pod Identity Associations to be created on the EKS Cluster
    + `associationId` - The ID of the Pod Identity Association
    + `roleArn` - The IAM Role ARN for the Pod Identity Association
+ `kubernetesRestoreOrder` - Override the order the Kubernetes manifests are restored in. This order will take precedence over the default service restore order. This follow the format: group/version/kind or version/kind

  Ex: `["v1/persistentvolumes","v1/pods","customresource/v2/custom"]`
+ `namespaceLevelRestore` - (true/false) If you would like to perform a namespace level restore
+ `namespaces` - A list of namespaces to restore if namespaceLevelRestore is "true". Can provide up to 5 namespaces to restore.

  Ex: `["ns-1","ns-2","ns-3","ns-4","ns-5"]`
+ `restoreKubernetesManifestsOnly` - (true/false) If you would like to only restore the Kubernetes manifest files and no persistent storage systems (EBS, S3, EFS, etc.)
+ `nestedRestoreJobs` - Restore Metadata configuration of all of the nested Recovery Points for the PersistentVolume storage systems in the composite Recovery Point. This is a map of RecoveryPointArn: RestoreMetadata of that Recovery Point
+ `resourceModifiers` - The Amazon S3 URI of a YAML file containing resource modifier rules that customize Kubernetes objects during restore. The file must be in an Amazon S3 bucket in the same account and Region as the restore job, must not exceed 1 MB, and the principal that calls `StartRestoreJob` must have `s3:GetObject` permission on it. AWS Backup validates the file when the job is submitted and rejects the job if the file is missing, inaccessible, or invalid. For the file schema and examples, see **Restore customizations**.

  Ex: `"s3://my-backup-bucket/restore-configs/account-modifiers.yaml"`

**Restore to existing cluster**

```bash
aws backup start-restore-job \
    --recovery-point-arn "arn:aws:backup:us-west-2:123456789012:recovery-point:composite:eks/my-cluster-20240115" \
    --iam-role-arn "arn:aws:iam::123456789012:role/AWSBackupDefaultServiceRole" \
    --metadata '{"clusterName":"existing-cluster","newCluster":"false"}' \
    --resource-type "EKS"
```

**Restore specific namespaces to an existing cluster:**

```bash
aws backup start-restore-job \
    --recovery-point-arn "arn:aws:backup:us-west-2:123456789012:recovery-point:composite:eks/my-cluster-20240115" \
    --iam-role-arn "arn:aws:iam::123456789012:role/AWSBackupDefaultServiceRole" \
    --metadata '{"clusterName":"existing-cluster","newCluster":"false","namespaceLevelRestore":"true","namespaces":"[\"ns-1\",\"ns-2\",\"ns-3\",\"ns-4\",\"ns-5\"]"}' \
    --resource-type "EKS"
```

**Restore nested persistent volumes to an existing cluster:**

```bash
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
    --metadata '{"clusterName":"new-cluster","newCluster":"true","clusterRole":"arn:aws:iam::123456789012:role/EKSClusterRole","eksClusterVersion":"1.33","controlPlaneScalingTier":"tier-2xl","encryptionConfigProviderKeyArn":"arn:aws:kms:us-west-2:123456789012:key/ecb2b326-784d-4ec0-8d07-20ab826b5a13","clusterVpcConfig":"{\"vpcId\":\"vpc-1234\",\"subnetIds\":[\"subnet-1\",\"subnet-2\",\"subnet-3\"],\"securityGroupIds\":[\"sg-123\"]}","nodeGroups":"[{\"nodeGroupId\":\"nodegroup-1\",\"subnetIds\":[\"subnet-1\",\"subnet-2\",\"subnet-3\"],\"nodeRole\":\"arn:aws:iam::123456789012:role/EKSNodeGroupRole\",\"instanceTypes\":[\"t3.small\"],\"launchTemplateId\":\"lt-0b13949aae3f2b867\",\"launchTemplateVersion\":\"1\"}]","fargateProfiles":"[{\"name\":\"fargate-profile-1\",\"subnetIds\":[\"subnet-1\",\"subnet-2\",\"subnet-3\"],\"podExecutionRoleArn\":\"arn:aws:iam::123456789012:role/EKSFargateProfileRole\"}]","computeConfig":"{\"nodeRoleArn\":\"arn:aws:iam::123456789012:role/EKSAutoModeNodeRole\"}"}' \
    --resource-type "EKS"
```

After starting the restore job, use `describe-restore-job` to monitor progress:

```
aws backup describe-restore-job --restore-job-id {{restore-job-id}}
```

------

You can subscribe to **Notification Events** for failed and skipped objects for restore. For more information, see [ Notification options with AWS Backup.](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html)

**Amazon EKS restore status messages**

When a restore job completes, you might see the following status messages. The table shows the possible scenarios and their corresponding job status values:


| Scenario | Job Status | Example message | 
| --- | --- | --- | 
| All objects restored successfully | COMPLETED | — | 
| One or more objects failed to be restored | COMPLETED | "One or more Kubernetes objects failed to restore. To get notified of these failures, enable SNS event notifications." | 
| One or more resource modifications failed to apply | COMPLETED | "Some Kubernetes Objects were restored without their requested modifications. To get notified of these failures, enable SNS event notifications." | 
| Restore could not complete | FAILED | (error details) | 

**Skipped objects during restore**

The following Kubernetes objects are restored on a best-effort basis. If they fail to restore, they are moved to the skipped list. These objects are system-managed and recreated by Kubernetes or Amazon EKS:
+ FlowSchemas with the `apf.kubernetes.io/autoupdate-spec: "true"` annotation
+ PriorityLevelConfigurations with the `apf.kubernetes.io/autoupdate-spec: "true"` annotation
+ The `eks-exempt` FlowSchema (EKS-managed, references the protected exempt PriorityLevelConfiguration)
+ The `kubernetes` Service in the `default` namespace (API server endpoint)
+ The `kube-dns` Service in the `kube-system` namespace (CoreDNS)

The following Kubernetes objects are always skipped during a restore. These objects include node infrastructure and networking components. They reference cluster-specific state. Kubernetes controllers automatically recreate these objects when nodes and services become active in the target cluster. If you restore these objects from a backup, they might cause conflicts or errors. These conflicts occur because the restored objects reference resources that don't exist on the target cluster.
+ Endpoints (`v1/endpoints`) - Network endpoints that define IP addresses for Services. The Endpoints controller automatically manages these based on Service selectors.
+ EndpointSlices (`discovery.k8s.io/v1/endpointslices`) - The EndpointSlice controller automatically manages these objects.
+ IPAddresses (`networking.k8s.io/v1/ipaddresses`) - Kubernetes networking manages these cluster-internal IP allocations.
+ CSINodes (`storage.k8s.io/v1/csinodes`) - The kubelet automatically creates these objects when CSI drivers register on a node.
+ VolumeAttachments (`storage.k8s.io/v1/volumeattachments`) - The attach/detach controller automatically creates these objects when pods require volumes.

Objects that already exist on the target cluster are also skipped. EKS restores are non-destructive — existing objects are never overwritten or deleted.

To receive notifications about skipped or failed objects during restore, subscribe to [SNS event notifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html). For more information, see [ Notification options with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html).

**OIDC and IRSA considerations for cross-cluster restore**

When restoring an Amazon EKS backup to a different cluster than the source, Kubernetes objects referencing IAM Roles for Service Accounts (IRSA) retain the source cluster's OIDC provider endpoint. These references exist in service account annotations and IAM trust policies. AWS Backup does not automatically update them during restore.

If your workloads use IRSA, a cross-cluster restore requires:
+ The destination cluster must have an OIDC provider configured.
+ All IAM roles referenced by Kubernetes service accounts must have their trust policies updated to include the destination cluster's OIDC provider endpoint.
+ Service account annotations (`eks.amazonaws.com/role-arn`) will still reference the original roles — verify these match valid roles in the destination account.

If these dependencies are not satisfied, pods will fail to assume IAM roles after restore, and restore jobs might report failures during validation.

**Recommendation**: For workloads that require cross-cluster or cross-account restore portability, we recommend using [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) instead of IRSA. EKS Pod Identity does not depend on cluster-specific OIDC providers and simplifies cross-cluster restore scenarios.