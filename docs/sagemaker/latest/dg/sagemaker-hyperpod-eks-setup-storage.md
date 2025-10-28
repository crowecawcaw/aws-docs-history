# Configuring storage for

SageMaker HyperPod clusters orchestrated by Amazon EKS

Cluster admin needs to configure storage for data scientist users to manage input and
output data and storing checkpoints during training on SageMaker HyperPod clusters.

**Handling large datasets (input/output data)**

- **Data access and management**: Data scientists
  often work with large datasets that are required for training machine learning
  models. Specifying storage parameters in the job submission allows them to
  define where these datasets are located (e.g., Amazon S3 buckets, persistent volumes
  in Kubernetes) and how they are accessed during the job execution.
- **Performance optimization**: The efficiency of
  accessing input data can significantly impact the performance of the training
  job. By optimizing storage parameters, data scientists can ensure that data is
  read and written efficiently, reducing I/O bottlenecks.
  **Storing checkpoints**

- **Checkpointing in training**: During
  long-running training jobs, it’s common practice to save
  checkpoints—intermediate states of the model. This allows data scientists to
  resume training from a specific point in case of a failure, rather than starting
  from scratch.
- **Data recovery and experimentation**: By
  specifying the storage location for checkpoints, data scientists can ensure that
  these checkpoints are securely stored, potentially in a distributed storage
  system that offers redundancy and high availability. This is crucial for
  recovering from interruptions and for experimenting with different training
  strategies.

###### Tip

For a hands-on experience and guidance on how to set up storage for SageMaker HyperPod
cluster orchestrated with Amazon EKS, see the following sections in the [Amazon EKS Support in SageMaker HyperPod workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e "https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e").

- [Set up Amazon FSx for Lustre on SageMaker HyperPod](https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e/en-US/01-cluster/06-fsx-for-lustre "https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e/en-US/01-cluster/06-fsx-for-lustre")
- [Set up a mountpoint for Amazon S3](https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e/en-US/01-cluster/09-s3-mountpoint "https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e/en-US/01-cluster/09-s3-mountpoint") using [Mountpoint for
  Amazon S3](../../../AmazonS3/latest/userguide/mountpoint.md "../../../AmazonS3/latest/userguide/mountpoint.md")
