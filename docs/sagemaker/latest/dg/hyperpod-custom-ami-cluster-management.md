# Cluster management with custom AMIs

After the custom AMI is built, you can use it for creating or updating an Amazon SageMaker HyperPod cluster.
You can also scale up or add instance groups that use the new AMI.

## Permissions required for

cluster operations

Add the following permissions to the cluster admin user who operates and
configures SageMaker HyperPod clusters. The following policy example includes the
minimum set of permissions for cluster administrators to run the SageMaker HyperPod
core APIs and manage SageMaker HyperPod clusters with custom AMI.

Note that AMI and AMI EBS snapshot sharing permissions are included through
`ModifyImageAttribute` and `ModifySnapshotAttribute`
API permissions as part of the following policy. For scoping down the sharing
permissions, you can take the following steps:

- Add tags to control the AMI sharing permissions to AMI and AMI
  snapshot. For example, you can tag the AMI with
  `AllowSharing` as `true`.
- Add the context key in the policy to only allow AMI sharing for AMIs
  tagged with certain tags.

The following policy is a scoped down policy to ensure only AMIs
tagged with `AllowSharing` as `true` are
allowed.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "`arn:aws:iam::111122223333:role/your-execution-role-name`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateCluster",
 "sagemaker:DeleteCluster",
 "sagemaker:DescribeCluster",
 "sagemaker:DescribeClusterNode",
 "sagemaker:ListClusterNodes",
 "sagemaker:ListClusters",
 "sagemaker:UpdateCluster",
 "sagemaker:UpdateClusterSoftware",
 "sagemaker:BatchDeleteClusterNodes",
 "eks:DescribeCluster",
 "eks:CreateAccessEntry",
 "eks:DescribeAccessEntry",
 "eks:DeleteAccessEntry",
 "eks:AssociateAccessPolicy",
 "iam:CreateServiceLinkedRole",
 "ec2:DescribeImages",
 "ec2:DescribeSnapshots"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:ModifyImageAttribute",
 "ec2:ModifySnapshotAttribute"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/AllowSharing": "true"
 }
 }
 }
 ]
}`

```

###### Important

If you plan to use an encrypted custom AMI, then make sure that your KMS key
meets the permissions described in [Customer managed AWS KMS key encryption for SageMaker HyperPod](smcluster-cmk.md "smcluster-cmk.md"). Additionally, ensure that your custom AMI's
KMS key is also used to encrypt your cluster's Amazon EBS root volume.

## Create a cluster

You can specify your custom AMI in the `ImageId` field for the
`CreateCluster` operation.

The following examples show how to create a cluster with a custom AMI, both with
and without an AWS KMS customer managed key for encrypting the cluster volumes.

Standard example
The following example shows how to create a cluster with a custom AMI.

```
aws sagemaker create-cluster \
   --cluster-name `<exampleClusterName>` \
   --orchestrator 'Eks={ClusterArn='`<eks_cluster_arn>`'}' \
   --node-provisioning-mode Continuous \
   --instance-groups '{
   "InstanceGroupName": "`<exampleGroupName>`",
   "InstanceType": "ml.c5.2xlarge",
   "InstanceCount": 2,
   "LifeCycleConfig": {
      "SourceS3Uri": "`<s3://amzn-s3-demo-bucket>`",
      "OnCreate": "on_create_noop.sh"
   },
   "ImageId": "`<your_custom_ami>`",
   "ExecutionRole": "`<arn:aws:iam::444455556666:role/Admin>`",
   "ThreadsPerCore": 1,
   "InstanceStorageConfigs": [

        {
            "EbsVolumeConfig": {
                "VolumeSizeInGB": 200
            }
        }
   ]
}' --vpc-config '{
   "SecurityGroupIds": ["`<security_group>`"],
   "Subnets": ["`<subnet>`"]
}'
```

Customer managed key example
The following example shows how to create a cluster with a custom AMI
while specifying your own AWS KMS customer managed key for encrypting the cluster's
Amazon EBS volumes. It is possible to specify different customer managed keys for the root volume
and the instance storage volume. If you don't use customer managed keys in the
`InstanceStorageConfigs` field, then an AWS owned
KMS key is used to encrypt the volumes. If you use different keys for the root
volume and secondary instance storage volumes, then set the required KMS key
policies on both of your keys.

```
aws sagemaker create-cluster \
   --cluster-name `<exampleClusterName>` \
   --orchestrator 'Eks={ClusterArn='`<eks_cluster_arn>`'}' \
   --node-provisioning-mode Continuous \
   --instance-groups '{
   "InstanceGroupName": "`<exampleGroupName>`",
   "InstanceType": "ml.c5.2xlarge",
   "InstanceCount": 2,
   "LifeCycleConfig": {
      "SourceS3Uri": "`<s3://amzn-s3-demo-bucket>`",
      "OnCreate": "on_create_noop.sh"
   },
   "ImageId": "`<your_custom_ami>`",
   "ExecutionRole": "`<arn:aws:iam:us-east-1:444455556666:role/Admin>`",
   "ThreadsPerCore": 1,
   "InstanceStorageConfigs": [
             # Root volume configuration
            {
                "EbsVolumeConfig": {
                    "RootVolume": True,
                    "VolumeKmsKeyId": "arn:aws:kms:`us-east-1`:111122223333:key/`key-id`"
                }
            },
            # Instance storage volume configuration
            {
                "EbsVolumeConfig": {
                    "VolumeSizeInGB": 100,
                    "VolumeKmsKeyId": "arn:aws:kms:`us-east-1`:111122223333:key/`key-id`"
                }
            }
   ]
}' --vpc-config '{
   "SecurityGroupIds": ["`<security_group>`"],
   "Subnets": ["`<subnet>`"]
}'
```

## Update the cluster software

If you want to update an existing instance group on your cluster with your
custom AMI, you can use the `UpdateClusterSoftware` operation and specify
your custom AMI in the `ImageId` field. Note that unless you specify
the name of a specific instance group in your request, then the new image is applied to all
of the instance groups in your cluster.

The following example shows how to update a cluster's platform software with a custom AMI:

```
aws sagemaker update-cluster-software \
   --cluster-name `<exampleClusterName>` \
   --instance-groups `<instanceGroupToUpdate>` \
   --image-id `<customAmiId>`
```

## Scale up an instance group

The following examples show how to scale up an instance group for a cluster using a custom AMI,
both with and without using an AWS KMS customer managed key for encryption.

Standard example
The following example shows how to scale up an instance group with a custom AMI.

```
aws sagemaker update-cluster \
    --cluster-name `<exampleClusterName>` --instance-groups '[{
    "InstanceGroupName": "`<exampleGroupName>`",
   "InstanceType": "ml.c5.2xlarge",
   "InstanceCount": 2,
   "LifeCycleConfig": {
      "SourceS3Uri": "`<s3://amzn-s3-demo-bucket>`",
      "OnCreate": "on_create_noop.sh"
   },
   "ExecutionRole": "`<arn:aws:iam::444455556666:role/Admin>`",
   "ThreadsPerCore": 1,
   "ImageId": "`<your_custom_ami>`"
}]'
```

Customer managed key example
The following example shows how to update and scale up your
cluster with a custom AMI while specifying your own AWS KMS customer managed key for
encrypting the cluster's Amazon EBS volumes. It is possible to specify different customer managed keys for the root volume
and the instance storage volume. If you don't use customer managed keys in the
`InstanceStorageConfigs` field, then an AWS owned
KMS key is used to encrypt the volumes. If you use different keys for the root
volume and secondary instance storage volumes, then set the required KMS key
policies on both of your keys.

```
aws sagemaker update-cluster \
    --cluster-name `<exampleClusterName>` --instance-groups '[{
    "InstanceGroupName": "`<exampleGroupName>`",
   "InstanceType": "ml.c5.2xlarge",
   "InstanceCount": 2,
   "LifeCycleConfig": {
      "SourceS3Uri": "`<s3://amzn-s3-demo-bucket>`",
      "OnCreate": "on_create_noop.sh"
   },
   "ExecutionRole": "`<arn:aws:iam::444455556666:role/Admin>`",
   "ThreadsPerCore": 1,
   "ImageId": "`<your_custom_ami>`",
   "InstanceStorageConfigs": [
             # Root volume configuration
            {
                "EbsVolumeConfig": {
                    "RootVolume": True,
                    "VolumeKmsKeyId": "arn:aws:kms:`us-east-1`:111122223333:key/`key-id`"
                }
            },
            # Instance storage volume configuration
            {
                "EbsVolumeConfig": {
                    "VolumeSizeInGB": 100,
                    "VolumeKmsKeyId": "arn:aws:kms:`us-east-1`:111122223333:key/`key-id`"
                }
            }
   ]
}]'
```

## Add an instance

group

The following example shows how to add an instance group to a cluster using a custom AMI:

```
aws sagemaker update-cluster \
   --cluster-name "`<exampleClusterName>`" \
   --instance-groups '{
   "InstanceGroupName": "`<exampleGroupName>`",
   "InstanceType": "ml.c5.2xlarge",
   "InstanceCount": 2,
   "LifeCycleConfig": {
      "SourceS3Uri": "`<s3://amzn-s3-demo-bucket>`",
      "OnCreate": "on_create_noop.sh"
   },
   "ExecutionRole": "`<arn:aws:iam::444455556666:role/Admin>`",
   "ThreadsPerCore": 1,
   "ImageId": "`<your_custom_ami>`"
}' '{
   "InstanceGroupName": "`<exampleGroupName2>`",
   "InstanceType": "ml.c5.2xlarge",
   "InstanceCount": 1,
   "LifeCycleConfig": {
      "SourceS3Uri": "`<s3://amzn-s3-demo-bucket>`",
      "OnCreate": "on_create_noop.sh"
   },
   "ExecutionRole": "`<arn:aws:iam::444455556666:role/Admin>`",
   "ThreadsPerCore": 1,
   "ImageId": "`<your_custom_ami>`"
}'
```
