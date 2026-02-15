# Mounting Amazon FSx for Lustre and Amazon FSx for OpenZFS to a HyperPod cluster

To mount an Amazon FSx for Lustre shared file system to your HyperPod cluster, set
up the following.

1. Use your Amazon VPC.
   1. For HyperPod cluster instances to communicate within your
      VPC, make sure that you attach the [Setting up SageMaker HyperPod
      with a custom Amazon VPC](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc") to the IAM role for SageMaker HyperPod.
   2. In `create_cluster.json`, include the following VPC
      information.

   ```
   "VpcConfig": {
       "SecurityGroupIds": [ "`string`" ],
       "Subnets": [ "`string`" ]
   }
   ```

   For more tips about setting up Amazon VPC, see [Prerequisites for using
   SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md "sagemaker-hyperpod-prerequisites.md").

2. To finish configuring Slurm with Amazon FSx for Lustre, you can use one of the following approaches. You can find the Amazon FSx information either from the Amazon FSx for Lustre console in your account or by running the following AWS CLI command, `aws fsx describe-file-systems`.

**Option A: API-Driven Configuration (Recommended)**

Specify the Amazon FSx configuration directly in the CreateCluster API payload using `InstanceStorageConfigs` within each instance group. This approach supports both FSx for Lustre and FSx for OpenZFS, and allows per-instance-group FSx configuration.

```
"InstanceStorageConfigs": [
    {
        "FsxLustreConfig": {
            "DnsName": "`fs-12345678a90b01cde`.fsx.`us-west-2`.amazonaws.com",
            "MountPath": "/fsx",
            "MountName": "`1abcdefg`"
        }
    }
]
```

For FSx for OpenZFS, use `FsxOpenZfsConfig` instead:

```
"InstanceStorageConfigs": [
    {
        "FsxOpenZfsConfig": {
            "DnsName": "`fs-12345678a90b01cde`.fsx.`us-west-2`.amazonaws.com",
            "MountPath": "/fsx-openzfs"
        }
    }
]
```

For more details, see [Getting started with SageMaker HyperPod using the AWS CLI](sagemaker-hyperpod-quickstart.md "sagemaker-hyperpod-quickstart.md").

**Option B: Legacy Configuration**

Specify the Amazon FSx DNS name and Amazon FSx mount name in `provisioning_parameters.json` as shown in the figure in the [Base lifecycle scripts provided by HyperPod](sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md "sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md") section.

```
"fsx_dns_name": "`fs-12345678a90b01cde`.fsx.`us-west-2`.amazonaws.com",
"fsx_mountname": "`1abcdefg`"
```
