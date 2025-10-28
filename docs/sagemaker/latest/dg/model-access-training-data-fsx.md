# Configure data input channel to use

Amazon FSx for Lustre

Learn how to use Amazon FSx for Lustre as your data source for higher throughput and faster
training by reducing the time for data loading.

###### Note

When you use EFA-enabled instances such as P4d and P3dn, make sure that you set
appropriate inbound and output rules in the security group. Specially, opening up these
ports is necessary for SageMaker AI to access the Amazon FSx file system in the training job. To learn
more, see [File System Access Control
with Amazon VPC](../../../fsx/latest/LustreGuide/limit-access-security-groups.md "../../../fsx/latest/LustreGuide/limit-access-security-groups.md").

## Sync Amazon S3 and

Amazon FSx for Lustre

To link your Amazon S3 to Amazon FSx for Lustre and upload your training datasets, do the
following.

1. Prepare your dataset and upload to an Amazon S3 bucket. For example, assume that the Amazon S3
   paths for a train dataset and a test dataset are in the following format.

```
s3://amzn-s3-demo-bucket/data/train
s3://amzn-s3-demo-bucket/data/test
```

2. To create an FSx for Lustre file system linked with the Amazon S3 bucket with the training
   data, follow the steps at [Linking your file system
   to an Amazon S3 bucket](../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md "../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md") in the _Amazon FSx for Lustre User Guide_. Make
   sure that you add an endpoint to your VPC allowing Amazon S3 access. For more information,
   see [Create an Amazon S3 VPC Endpoint](train-vpc.md#train-vpc-s3 "train-vpc.md#train-vpc-s3"). When you specify **Data repository
   path**, provide the Amazon S3 bucket URI of the folder that contains your
   datasets. For example, based on the example S3 paths in step 1, the data repository path
   should be the following.

```
s3://amzn-s3-demo-bucket/data
```

3. After the FSx for Lustre file system is created, check the configuration information by
   running the following commands.

```
aws fsx describe-file-systems && \
aws fsx describe-data-repository-association
```

These commands return `FileSystemId`, `MountName`,
`FileSystemPath`, and `DataRepositoryPath`. For example, the
outputs should look like the following.

```
# Output of aws fsx describe-file-systems
"FileSystemId": "fs-0123456789abcdef0"
"MountName": "1234abcd"

# Output of aws fsx describe-data-repository-association
"FileSystemPath": "/ns1",
"DataRepositoryPath": "s3://amzn-s3-demo-bucket/data/"
```

After the sync between Amazon S3 and Amazon FSx has completed, your datasets are saved in
Amazon FSx in the following directories.

```
/ns1/train  # synced with s3://amzn-s3-demo-bucket/data/train
/ns1/test   # synced with s3://amzn-s3-demo-bucket/data/test
```

## Set the Amazon FSx file

system path as the data input channel for SageMaker training

The following procedures walk you through the process of setting the Amazon FSx file system
as the data source for SageMaker training jobs.

Using the SageMaker Python SDK
To properly set the Amazon FSx file system as the data source, configure the SageMaker AI
estimator classes and `FileSystemInput` using the following
instruction.

1. Configure a FileSystemInput class object.

```
from sagemaker.inputs import FileSystemInput

train_fs = FileSystemInput(
    file_system_id="`fs-0123456789abcdef0`",
    file_system_type="FSxLustre",
    directory_path="`/1234abcd/ns1/`",
    file_system_access_mode="ro",
)
```

###### Tip

When you specify `directory_path`, make sure that you provide the
Amazon FSx file system path starting with `MountName`. 2. Configure a SageMaker AI estimator with the VPC configuration used for the Amazon FSx file
system.

```
from sagemaker.`estimator` import `Estimator`

estimator = `Estimator`(
    ...
    role="`your-iam-role-with-access-to-your-fsx`",
    subnets=["`subnet-id`"],  # Should be the same as the subnet used for Amazon FSx
    security_group_ids="`security-group-id`"
)
```

Make sure that the IAM role for the SageMaker training job has the permissions to
access and read from Amazon FSx. 3. Launch the training job by running the estimator.fit method with the Amazon FSx
file system.

```
estimator.fit(train_fs)
```

To find more code examples, see [Use File Systems as Training Inputs](https://sagemaker.readthedocs.io/en/stable/overview.html#use-file-systems-as-training-inputs "https://sagemaker.readthedocs.io/en/stable/overview.html#use-file-systems-as-training-inputs") in the _SageMaker Python SDK
documentation_.

Using the SageMaker AI CreateTrainingJob API
As part of the [CreateTrainingJob](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") request JSON, configure `InputDataConfig` as
follows.

```
"InputDataConfig": [
    {
        "ChannelName": "`string`",
        "DataSource": {
            "FileSystemDataSource": {
                "DirectoryPath": "`/1234abcd/ns1/`",
                "FileSystemAccessMode": "ro",
                "FileSystemId": "`fs-0123456789abcdef0`",
                "FileSystemType": "FSxLustre"
            }
        }
    }
],
```

###### Tip

When you specify `DirectoryPath`, make sure that you provide the
Amazon FSx file system path starting with `MountName`.
