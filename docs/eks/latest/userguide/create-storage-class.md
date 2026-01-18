**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create a storage class

A `StorageClass` in Amazon EKS Auto Mode defines how Amazon EBS volumes are automatically provisioned when applications request persistent storage. This page explains how to create and configure a `StorageClass` that works with the Amazon EKS Auto Mode to provision EBS volumes.

By configuring a `StorageClass`, you can specify default settings for your EBS volumes including volume type, encryption, IOPS, and other storage parameters. You can also configure the `StorageClass` to use AWS KMS keys for encryption management.

EKS Auto Mode does not create a `StorageClass` for you. You must create a `StorageClass` referencing `ebs.csi.eks.amazonaws.com` to use the storage capability of EKS Auto Mode.

First, create a file named `storage-class.yaml`:

```
 apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: auto-ebs-sc
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
allowedTopologies:
- matchLabelExpressions:
  - key: eks.amazonaws.com/compute-type
    values:
    - auto
provisioner: ebs.csi.eks.amazonaws.com
volumeBindingMode: WaitForFirstConsumer
parameters:
  type: gp3
  encrypted: "true"
```

Second, apply the storage class to your cluster.

```
 kubectl apply -f storage-class.yaml
```

**Key components:**

- `provisioner: ebs.csi.eks.amazonaws.com` - Uses EKS Auto Mode
- `allowedTopologies` - Specifying `matchLabelExpressions` to match on `eks.amazonaws.com/compute-type:auto` will ensure that if your pods need a volume to be automatically provisioned using Auto Mode then the pods will not be scheduled on non-Auto nodes.
- `volumeBindingMode: WaitForFirstConsumer` - Delays volume creation until a pod needs it
- `type: gp3` - Specifies the EBS volume type
- `encrypted: "true"` - EBS will encrypt any volumes created using the `StorageClass`. EBS will use the default `aws/ebs` key alias. For more information, see [How Amazon EBS encryption works](../../../ebs/latest/userguide/how-ebs-encryption-works.md "../../../ebs/latest/userguide/how-ebs-encryption-works.md") in the Amazon EBS User Guide. This value is optional but suggested.
- `storageclass.kubernetes.io/is-default-class: "true"` - Kubernetes will use this storage class by default, unless you specify a different volume class on a persistent volume claim. This value is optional. Use caution when setting this value if you are migrating from a different storage controller.

## Use self-managed KMS key to encrypt EBS volumes

To use a self-managed KMS key to encrypt EBS volumes automated by EKS Auto Mode, you need to:

1. Create a self-managed KMS key.
   - For more information, see [Create a symmetric encryption KMS key](../../../kms/latest/developerguide/create-symmetric-cmk.md "../../../kms/latest/developerguide/create-symmetric-cmk.md") or [How Amazon Elastic Block Store (Amazon EBS) uses KMS](../../../kms/latest/developerguide/services-ebs.md "../../../kms/latest/developerguide/services-ebs.md") in the KMS User Guide.

2. Create a new policy that permits access to the KMS key.
   - Use the sample IAM policy below to create the policy. Insert the ARN of the new self-managed KMS key. For more information, see
     [Creating roles and attaching policies (console)](../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md "../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md") in the AWS IAM User Guide.

3. Attach the policy to the EKS Cluster Role.
   - Use the AWS console to find the ARN of the EKS Cluster Role. The role information is visible in the **Overview** section. For more information, see [Amazon EKS cluster IAM role](cluster-iam-role.md "cluster-iam-role.md").

4. Update the `StorageClass` to reference the KMS Key ID at the `parameters.kmsKeyId` field.

### Sample self-managed KMS IAM Policy

Update the following values in the policy below:

- `<account-id>` – Your AWS account ID, such as `111122223333`
- `<aws-region>` – The AWS region of your cluster, such as `us-west-2`

```
 {
  "Version":"2012-10-17",
  "Id": "key-auto-policy-3",
  "Statement": [
      {
          "Sid": "Enable IAM User Permissions",
          "Effect": "Allow",
          "Principal": {
              "AWS": "arn:aws:iam::123456789012:root"
          },
          "Action": "kms:*",
          "Resource": "*"
      },
      {
        "Sid": "Allow access through EBS for all principals in the account that are authorized to use EBS",
        "Effect": "Allow",
        "Principal": {
            "AWS": "*"
        },
        "Action": [
            "kms:Encrypt",
            "kms:Decrypt",
            "kms:ReEncrypt*",
            "kms:GenerateDataKey*",
            "kms:CreateGrant",
            "kms:DescribeKey"
        ],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "kms:CallerAccount": "123456789012",
                "kms:ViaService": "ec2.us-east-1.amazonaws.com"
            }
        }
    }
  ]
}
```

### Sample self-managed KMS `StorageClass`

```
 parameters:
  type: gp3
  encrypted: "true"
  kmsKeyId: <custom-key-arn>
```

## `StorageClass` Parameters Reference

For general information on the Kubernetes `StorageClass` resources, see [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/ "https://kubernetes.io/docs/concepts/storage/storage-classes/") in the Kubernetes Documentation.

THe `parameters` section of the `StorageClass` resource is specific to AWS. Use the following table to review available options.

| Parameters                   | Values                                             | Default | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | -------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "csi.storage.k8s.io/fstype"  | xfs, ext2, ext3, ext4                              | ext4    | File system type that will be formatted during volume creation. This parameter is case sensitive!                                                                                                                                                                                                                                                                                                 |
| "type"                       | io1, io2, gp2, gp3, sc1, st1, standard, sbp1, sbg1 | gp3     | EBS volume type.                                                                                                                                                                                                                                                                                                                                                                                  |
| "iopsPerGB"                  |                                                    |         | I/O operations per second per GiB. Can be specified for IO1, IO2, and GP3 volumes.                                                                                                                                                                                                                                                                                                                |
| "allowAutoIOPSPerGBIncrease" | true, false                                        | false   | When `"true"`, the CSI driver increases IOPS for a volume when `iopsPerGB<br>• <volume size>` is too low to fit into IOPS range supported by AWS. This allows dynamic provisioning to always succeed, even when user specifies too small PVC capacity or `iopsPerGB` value. On the other hand, it may introduce additional costs, as such volumes have higher IOPS than requested in `iopsPerGB`. |
| "iops"                       |                                                    |         | I/O operations per second. Can be specified for IO1, IO2, and GP3 volumes.                                                                                                                                                                                                                                                                                                                        |
| "throughput"                 |                                                    | 125     | Throughput in MiB/s. Only effective when gp3 volume type is specified.                                                                                                                                                                                                                                                                                                                            |
| "encrypted"                  | true, false                                        | false   | Whether the volume should be encrypted or not. Valid values are "true" or "false".                                                                                                                                                                                                                                                                                                                |
| "blockExpress"               | true, false                                        | false   | Enables the creation of io2 Block Express volumes.                                                                                                                                                                                                                                                                                                                                                |
| "kmsKeyId"                   |                                                    |         | The full ARN of the key to use when encrypting the volume. If not specified, AWS will use the default KMS key for the region the volume is in. This will be an auto-generated key called `/aws/ebs` if not changed.                                                                                                                                                                               |
| "blockSize"                  |                                                    |         | The block size to use when formatting the underlying filesystem. Only supported on linux nodes and with fstype `ext2`, `ext3`, `ext4`, or `xfs`.                                                                                                                                                                                                                                                  |
| "inodeSize"                  |                                                    |         | The inode size to use when formatting the underlying filesystem. Only supported on linux nodes and with fstype `ext2`, `ext3`, `ext4`, or `xfs`.                                                                                                                                                                                                                                                  |
| "bytesPerInode"              |                                                    |         | The `bytes-per-inode` to use when formatting the underlying filesystem. Only supported on linux nodes and with fstype `ext2`, `ext3`, `ext4`.                                                                                                                                                                                                                                                     |
| "numberOfInodes"             |                                                    |         | The `number-of-inodes` to use when formatting the underlying filesystem. Only supported on linux nodes and with fstype `ext2`, `ext3`, `ext4`.                                                                                                                                                                                                                                                    |
| "ext4BigAlloc"               | true, false                                        | false   | Changes the `ext4` filesystem to use clustered block allocation by enabling the `bigalloc` formatting option. Warning: `bigalloc` may not be fully supported with your node’s Linux kernel.                                                                                                                                                                                                       |
| "ext4ClusterSize"            |                                                    |         | The cluster size to use when formatting an `ext4` filesystem when the `bigalloc` feature is enabled. Note: The `ext4BigAlloc` parameter must be set to true.                                                                                                                                                                                                                                      |

For more information, see the [AWS EBS CSI Driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/parameters.md "https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/parameters.md") on GitHub.

## Considerations

###### Note

You can only deploy workloads depending on EKS Auto Mode StorageClasses on EKS Auto Mode nodes. If you have a cluster with mixed types of nodes, you need to configure your workloads to run only on EKS Auto Mode nodes. For more information, see [Control if a workload is deployed on EKS Auto Mode nodes](associate-workload.md "associate-workload.md").

The block storage capability of EKS Auto Mode is different from the EBS CSI Driver.

- Static Provisioning
  - If you want to use externally-created EBS volumes with EKS Auto Mode, you need to manually add an AWS tag with the key `eks:eks-cluster-name` and the value of the cluster name.

- Node Startup Taint
  - You cannot use the node startup taint feature to prevent pod scheduling before storage capability readiness

- Custom Tags on Dynamically Provisioned Volumes
  - You cannot use the extra-tag CLI flag to configure custom tags on dynamically provisioned EBS volumes
  - You can use `StorageClass` tagging to add custom tags. EKS Auto Mode will add tags to the associated AWS resources. You will need to update the Cluster IAM Role for custom tags. For more information, see [Custom AWS tags for EKS Auto resources](auto-learn-iam.md#tag-prop "auto-learn-iam.md#tag-prop").

- EBS Detailed Performance Metrics
  - You cannot access Prometheus metrics for EBS detailed performance

## Install CSI Snapshot Controller add-on

EKS Auto Mode is compatible with the CSI Snapshot Controller Amazon EKS add-on.

AWS suggests you configure this add-on to run on the built-in `system` node pool.

For more information, see:

- [Run critical add-ons on dedicated instances](critical-workload.md "critical-workload.md")
- [Enable or Disable Built-in NodePools](set-builtin-node-pools.md "set-builtin-node-pools.md")
- [Enable snapshot functionality for CSI volumes](csi-snapshot-controller.md "csi-snapshot-controller.md")

### To install snapshot controller in system node pool

1. Open your EKS cluster in the AWS console
2. From the **Add-ons** tab, select **Get more add-ons**
3. Select the **CSI Snapshot Controller** and then **Next**
4. On the **Configure selected add-ons settings** page, select **Optional configuration settings** to view the **Add-on configuration schema**
   1. Insert the following yaml to associate the snapshot controller with the `system` node pool. The snapshot controller includes a toleration for the `CriticalAddonsOnly` taint.

   ```
    {
           "nodeSelector": {
               "karpenter.sh/nodepool": "system"
           }
   }
   ```

   2. Select **Next**

5. Review the add-on configuration and then select **Create**
