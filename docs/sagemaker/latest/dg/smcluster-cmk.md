# Customer managed AWS KMS key encryption for SageMaker HyperPod

By default, the root Amazon EBS volume attached to your SageMaker HyperPod cluster is encrypted using
an AWS KMS key owned by AWS. You now have the option to encrypt both the root Amazon EBS
volume and the secondary volume with your own customer managed KMS keys. The following
topic describes how customer managed keys (CMKs) work with volumes in HyperPod
clusters.

###### Note

The following exclusions apply when using customer managed keys for SageMaker HyperPod
clusters:

- Customer managed key encryption is only supported for clusters using the
  continuous node provisioning mode. Restricted instance groups don't support
  customer managed keys.
- HyperPod clusters don’t currently support passing AWS KMS encryption
  context in customer managed key encryption requests. Therefore, ensure your KMS key policy
  is not scoped down using encryption context conditions, as this prevents the
  cluster from using the key.
- KMS key transition isn't currently supported, so you can't change the KMS key specified
  in your configuration. To use a different key, create a new instance group with
  the desired key and delete your old instance group.
- Specifying customer managed keys for HyperPod clusters through the console
  isn't currently supported.

## Permissions

Before you can use your customer managed key with HyperPod, you must complete the
following prerequisites:

- Ensure that the AWS IAM execution role that you're using for SageMaker AI has the
  following permissions for AWS KMS added. The
  `kms:CreateGrant` permission allows HyperPod to take the
  following actions using permissions to your KMS key:

      + Scaling out your instance count (UpdateCluster operations)
      + Adding cluster nodes (BatchAddClusterNodes operations)
      + Patching software (UpdateClusterSoftware operations)

  For more information on updating your IAM role's permissions, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM
  User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

- Add the following permissions to your KMS key policy. For more
  information, see [Change a key policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md") in the _AWS KMS Developer
  Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "hyperpod-key-policy",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`<iam-role>`"
 },
 "Action": "kms:CreateGrant",
 "Resource": "arn:aws:kms:`us-east-1`:111122223333:key/`key-id`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "sagemaker.`us-east-1`.amazonaws.com"
 },
 "Bool": {
 "kms:GrantIsForAWSResource": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`<iam-role>`"
 },
 "Action": "kms:DescribeKey",
 "Resource": "arn:aws:kms:`us-east-1`:111122223333:key/`key-id`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "sagemaker.`us-east-1`.amazonaws.com"
 }
 }
 }
 ]
}`

```

## How to use your KMS key

You can specify your customer managed keys when creating or updating a cluster using
the [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") and
[UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") API
operations. The `InstanceStorageConfigs` structure allows up to two
`EbsVolumeConfig` configurations, in which you can configure the root
Amazon EBS volume and, optionally, a secondary volume. You can use the same KMS key or a
different KMS key for each volume, depending on your needs.

You can choose to specify a customer managed key for neither, both, or either volume. However, you
can't specify two root volumes or two secondary volumes.

When configuring the root volume, the following requirements apply:

- `RootVolume` must be set to `True`. The default
  value is `False`, which configures the secondary volume
  instead.
- The `VolumeKmsKeyId` field is required and you must specify your
  customer managed key. This is because the root volume
  must always be encrypted with either an AWS owned key or a customer managed key (if you don't
  specify your own, then an AWS owned key is used).
- You can't specify the `VolumeSizeInGB` field for root volumes
  since HyperPod determines the size of the root volume for you.

When configuring the secondary volume, the following requirements apply:

- `RootVolume` must be `False` (the default value of
  this field is `False`).
- The `VolumeKmsKeyId` field is optional. You can use the
  same customer managed key you specified for the root volume, or you can use a different
  key.
- The `VolumeSizeInGB` field is required, since you must specify
  your desired size for the secondary volume.

###### Important

When using customer managed keys, we strongly recommend that you use different KMS keys
for each instance group in your cluster. Using the same customer managed key across multiple
instance groups might lead to unintentional continued permissions even if you try to
revoke a grant. For example, if you revoke an AWS KMS grant for one instance group's
volumes, that instance group might still allow scaling and patching operations due to
grants existing on other instance groups using the same key. To prevent this issue,
ensure that you assign unique KMS keys to each instance group in your cluster.
If you need to restrict permissions on instance groups, you can try one of the following
options:

- Disable the KMS key.
- Apply deny policies to the KMS key policy.
- Revoke all instance group grants for the key (rather than revoking one grant).
- Delete the instance group.
- Delete the cluster.

The following examples show how to specify customer managed keys for both root and
secondary volumes using the CreateCluster and UpdateCluster APIs. These
examples show only the required fields for customer managed key integration. To configure a
customer managed key for only one of the volumes, then only
specify one `EbsVolumeConfig`.

For more information about configuring cluster creation and update requests, see
[Creating
a SageMaker HyperPod cluster](sagemaker-hyperpod-eks-operate-cli-command-create-cluster.md "sagemaker-hyperpod-eks-operate-cli-command-create-cluster.md") and
[Updating
SageMaker HyperPod cluster configuration](sagemaker-hyperpod-eks-operate-cli-command-update-cluster.md "sagemaker-hyperpod-eks-operate-cli-command-update-cluster.md").

CreateCluster
The following example shows a [create-cluster](../../../cli/latest/reference/sagemaker/create-cluster.md "../../../cli/latest/reference/sagemaker/create-cluster.md") AWS CLI request with customer managed key encryption.

```
aws sagemaker create-cluster \
  --cluster-name `<your-hyperpod-cluster>` \
  --instance-groups '[{
    "ExecutionRole": "arn:aws:iam::`111122223333`:role/`<your-SageMaker-Execution-Role>`",
    "InstanceCount": 2,
    "InstanceGroupName": "`<your-ig-name>`",
    "InstanceStorageConfigs": [
            {
                "EbsVolumeConfig": {
                    "RootVolume": True,
                    "VolumeKmsKeyId": "arn:aws:kms:`us-east-1`:111122223333:key/`root-volume-key-id`"
                }
            },
            {
                "EbsVolumeConfig": {
                    "VolumeSizeInGB": 100,
                    "VolumeKmsKeyId": "arn:aws:kms:`us-east-1`:111122223333:key/`secondary-volume-key-id`"
                }
            }
    ],
    "InstanceType": "`<desired-instance-type>`"
  }]' \
  --vpc-config '{
    "SecurityGroupIds": ["`<sg-id>`"],
    "Subnets": ["`<subnet-id>`"]
  }'
```

UpdateCluster
The following example shows an [update-cluster](../../../cli/latest/reference/sagemaker/update-cluster.md "../../../cli/latest/reference/sagemaker/update-cluster.md") AWS CLI request with customer managed key encryption.

```
aws sagemaker update-cluster \
  --cluster-name `<your-hyperpod-cluster>` \
  --instance-groups '[{
    "InstanceGroupName": "`<your-ig-name>`",
    "InstanceStorageConfigs": [
            {
                "EbsVolumeConfig": {
                    "RootVolume": true,
                    "VolumeKmsKeyId": "arn:aws:kms:`us-east-1`:111122223333:key/`root-volume-key-id`"
                }
            },
            {
                "EbsVolumeConfig": {
                    "VolumeSizeInGB": 100,
                    "VolumeKmsKeyId": "arn:aws:kms:`us-east-1`:111122223333:key/`secondary-volume-key-id`"
                }
            }
    ]
  }]'
```
