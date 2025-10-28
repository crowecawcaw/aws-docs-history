# Key Management

Customers can specify AWS KMS keys, including bring your own keys (BYOK), to use for
envelope encryption with Amazon S3 input/output buckets and machine learning (ML) Amazon EBS volumes.
ML volumes for notebook instances and for processing, training, and hosted model Docker
containers can be optionally encrypted by using AWS KMS customer-owned keys. All instance OS
volumes are encrypted with an AWS-managed AWS KMS key.

###### Note

Certain Nitro-based instances include local storage, dependent on the instance type.
Local storage volumes are encrypted using a hardware module on the instance. You can't
request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see
[Instance Store Volumes](../../../AWSEC2/latest/UserGuide/InstanceStorage.md#instance-store-volumes "../../../AWSEC2/latest/UserGuide/InstanceStorage.md#instance-store-volumes").

For more information about local instance storage encryption, see
[SSD Instance Store Volumes](../../../AWSEC2/latest/UserGuide/ssd-instance-store.md "../../../AWSEC2/latest/UserGuide/ssd-instance-store.md").

For more information about storage volumes on nitro-based instances, see [Amazon EBS and NVMe on Linux
Instances](../../../AWSEC2/latest/UserGuide/nvme-ebs-volumes.md "../../../AWSEC2/latest/UserGuide/nvme-ebs-volumes.md").

For information about AWS KMS keys see [What is AWS Key Management
Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service Developer Guide_.
