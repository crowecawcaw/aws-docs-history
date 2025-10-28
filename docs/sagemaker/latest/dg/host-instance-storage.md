# Instance storage volumes

When you create an endpoint, Amazon SageMaker AI attaches an Amazon Elastic Block Store (Amazon EBS) storage volume to Amazon EC2 instances
that hosts the endpoint. The size of the storage volume is scalable, and storage options are
divided into two categories: SSD-backed storage and HDD-backed storage.

For more information about Amazon EBS storages and features, see the following pages.

- [Amazon EBS Features](https://aws.amazon.com/ebs/features/ "https://aws.amazon.com/ebs/features/")
- [Amazon EBS User Guide](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md")
  For a full list of the host instance storage volumes, see [Host Instance Storage Volumes Table](https://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/ "https://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/")

###### Note

Amazon SageMaker AI attaches an Amazon Elastic Block Store (Amazon EBS) storage volume to Amazon EC2 instances only when you create
[Asynchronous inference](async-inference.md "async-inference.md") or [Real-time inference](realtime-endpoints.md "realtime-endpoints.md") endpoint types.
For more information on customizing Amazon EBS storage volume, see [SageMaker AI endpoint parameters for large model inference](large-model-inference-hosting.md "large-model-inference-hosting.md").
