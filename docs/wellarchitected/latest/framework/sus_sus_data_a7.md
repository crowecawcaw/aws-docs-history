# SUS04-BP06 Use shared file systems or storage to access common

data

Adopt shared file systems or storage to avoid data duplication and allow for more efficient
infrastructure for your workload.

**Common anti-patterns:**

- You provision storage for each individual client.
- You do not detach data volume from inactive clients.
- You do not provide access to storage across platforms and systems.

**Benefits of establishing this best practice:** Using shared file
systems or storage allows for sharing data to one or more consumers without having to copy the
data. This helps to reduce the storage resources required for the workload.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

If you have multiple users or applications accessing the same datasets, using shared
storage technology is crucial to use efficient infrastructure for your workload. Shared
storage technology provides a central location to store and manage datasets and avoid data
duplication. It also enforces consistency of the data across different systems. Moreover,
shared storage technology allows for more efficient use of compute power, as multiple compute
resources can access and process data at the same time in parallel.

Fetch data from these shared storage services only as needed and detach unused volumes to
free up resources.

### Implementation steps

- **Use shared storage:** Migrate data to shared storage when the data has multiple consumers. Here are some
  examples of shared storage technology on AWS:

| Storage option                                                                                                                           | When to use                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Amazon EBS Multi-Attach](../../../AWSEC2/latest/UserGuide/ebs-volumes-multi.md "../../../AWSEC2/latest/UserGuide/ebs-volumes-multi.md") | Amazon EBS Multi-Attach allows you to attach a single Provisioned IOPS SSD (io1 or io2) volume to multiple instances that are in the same Availability Zone.                                |
| [Amazon EFS](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/")                                                                  | See [When to Choose Amazon EFS](https://aws.amazon.com/efs/when-to-choose-efs/ "https://aws.amazon.com/efs/when-to-choose-efs/").                                                           |
| [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/")                                                                  | See [Choosing an Amazon FSx File System](https://aws.amazon.com/fsx/when-to-choose-fsx/ "https://aws.amazon.com/fsx/when-to-choose-fsx/").                                                  |
| [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")                                                                     | Applications that do not require a file system structure and are designed to work with object storage can use Amazon S3 as a massively scalable, durable, low-cost object storage solution. | <br>• **Fetch data as needed:** Copy data to or fetch data from shared file systems only as needed. As an example, you can create an [Amazon FSx for Lustre file system backed by Amazon S3](https://aws.amazon.com/blogs/storage/new-enhancements-for-moving-data-between-amazon-fsx-for-lustre-and-amazon-s3/ "https://aws.amazon.com/blogs/storage/new-enhancements-for-moving-data-between-amazon-fsx-for-lustre-and-amazon-s3/") and only load the subset of data required for processing jobs to Amazon FSx. <br>• **Delete unneeded data:** Delete data as appropriate for your usage patterns as outlined in [SUS04-BP03 Use policies to manage the lifecycle of your datasets](sus_sus_data_a4.md "sus_sus_data_a4.md"). <br>• **Detach inactive clients:** Detach volumes from clients that are not actively using them. ## Resources **Related documents:** <br>• [Linking your file system to an Amazon S3 bucket](../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md "../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md") <br>• [Using Amazon EFS for AWS Lambda in your serverless applications](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/ "https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/") <br>• [Amazon EFS Intelligent-Tiering Optimizes Costs for Workloads with Changing Access Patterns](https://aws.amazon.com/blogs/aws/new-amazon-efs-intelligent-tiering-optimizes-costs-for-workloads-with-changing-access-patterns/ "https://aws.amazon.com/blogs/aws/new-amazon-efs-intelligent-tiering-optimizes-costs-for-workloads-with-changing-access-patterns/") <br>• [Using Amazon FSx with your on-premises data repository](../../../fsx/latest/LustreGuide/fsx-on-premises.md "../../../fsx/latest/LustreGuide/fsx-on-premises.md") **related videos:** <br>• [Storage cost optimization with Amazon EFS](https://www.youtube.com/watch?v=0nYAwPsYvBo "https://www.youtube.com/watch?v=0nYAwPsYvBo") <br>• [AWS re:Invent 2023 - What's new with AWS file storage](https://www.youtube.com/watch?v=yXIeIKlTFV0 "https://www.youtube.com/watch?v=yXIeIKlTFV0") <br>• [AWS re:Invent 2023 - File storage for builders and data scientists on Amazon Elastic File System](https://www.youtube.com/watch?v=g0f6lrmEyRM "https://www.youtube.com/watch?v=g0f6lrmEyRM") |
