# Instance Types Available for Use With

Amazon SageMaker Studio Classic Notebooks

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

Amazon SageMaker Studio Classic notebooks run on Amazon Elastic Compute Cloud (Amazon EC2) instances. The following Amazon EC2
instance types are available for use with Studio Classic notebooks. For detailed information on
which instance types fit your use case, and their performance capabilities, see [Amazon Elastic Compute Cloud Instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/"). For
information about pricing for these instance types, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").

For information about available Amazon SageMaker Notebook Instance types, see [CreateNotebookInstance](../APIReference/API_CreateNotebookInstance.md#sagemaker-CreateNotebookInstance-request-InstanceType "../APIReference/API_CreateNotebookInstance.md#sagemaker-CreateNotebookInstance-request-InstanceType").

###### Note

For most use cases, you should use a `ml.t3.medium`. This is the default instance type
for CPU-based SageMaker images, and is available as part of the [AWS Free Tier](https://aws.amazon.com/free "https://aws.amazon.com/free").

###### Topics

- [CPU instances](#notebooks-resources-no-gpu "#notebooks-resources-no-gpu")
- [Instances with 1 or more GPUs](#notebooks-resources-gpu "#notebooks-resources-gpu")

## CPU instances

The following table lists the Amazon EC2 CPU instance types with no GPU attached that are
available for use with Studio Classic notebooks. It also lists information about the
specifications of each instance type. The default instance type for CPU-based images is
`ml.t3.medium`.

For detailed information on which instance types fit your use case, and their
performance capabilities, see [Amazon Elastic Compute Cloud
Instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/"). For information about pricing for these instance types, see
[Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").

CPU instances

| Instance        | Use case          | Fast launch | vCPU | Memory (GiB) | Instance Storage (GB) |
| --------------- | ----------------- | ----------- | ---- | ------------ | --------------------- |
| ml.t3.medium    | General purpose   | Yes         | 2    | 4            | Amazon EBS Only       |
| ml.t3.large     | General purpose   | No          | 2    | 8            | Amazon EBS Only       |
| ml.t3.xlarge    | General purpose   | No          | 4    | 16           | Amazon EBS Only       |
| ml.t3.2xlarge   | General purpose   | No          | 8    | 32           | Amazon EBS Only       |
| ml.m5.large     | General purpose   | Yes         | 2    | 8            | Amazon EBS Only       |
| ml.m5.xlarge    | General purpose   | No          | 4    | 16           | Amazon EBS Only       |
| ml.m5.2xlarge   | General purpose   | No          | 8    | 32           | Amazon EBS Only       |
| ml.m5.4xlarge   | General purpose   | No          | 16   | 64           | Amazon EBS Only       |
| ml.m5.8xlarge   | General purpose   | No          | 32   | 128          | Amazon EBS Only       |
| ml.m5.12xlarge  | General purpose   | No          | 48   | 192          | Amazon EBS Only       |
| ml.m5.16xlarge  | General purpose   | No          | 64   | 256          | Amazon EBS Only       |
| ml.m5.24xlarge  | General purpose   | No          | 96   | 384          | Amazon EBS Only       |
| ml.m5d.large    | General purpose   | No          | 2    | 8            | 1 x 75 NVMe SSD       |
| ml.m5d.xlarge   | General purpose   | No          | 4    | 16           | 1 x 150 NVMe SSD      |
| ml.m5d.2xlarge  | General purpose   | No          | 8    | 32           | 1 x 300 NVMe SSD      |
| ml.m5d.4xlarge  | General purpose   | No          | 16   | 64           | 2 x 300 NVMe SSD      |
| ml.m5d.8xlarge  | General purpose   | No          | 32   | 128          | 2 x 600 NVMe SSD      |
| ml.m5d.12xlarge | General purpose   | No          | 48   | 192          | 2 x 900 NVMe SSD      |
| ml.m5d.16xlarge | General purpose   | No          | 64   | 256          | 4 x 600 NVMe SSD      |
| ml.m5d.24xlarge | General purpose   | No          | 96   | 384          | 4 x 900 NVMe SSD      |
| ml.c5.large     | Compute optimized | Yes         | 2    | 4            | Amazon EBS Only       |
| ml.c5.xlarge    | Compute optimized | No          | 4    | 8            | Amazon EBS Only       |
| ml.c5.2xlarge   | Compute optimized | No          | 8    | 16           | Amazon EBS Only       |
| ml.c5.4xlarge   | Compute optimized | No          | 16   | 32           | Amazon EBS Only       |
| ml.c5.9xlarge   | Compute optimized | No          | 36   | 72           | Amazon EBS Only       |
| ml.c5.12xlarge  | Compute optimized | No          | 48   | 96           | Amazon EBS Only       |
| ml.c5.18xlarge  | Compute optimized | No          | 72   | 144          | Amazon EBS Only       |
| ml.c5.24xlarge  | Compute optimized | No          | 96   | 192          | Amazon EBS Only       |
| ml.r5.large     | Memory optimized  | No          | 2    | 16           | Amazon EBS Only       |
| ml.r5.xlarge    | Memory optimized  | No          | 4    | 32           | Amazon EBS Only       |
| ml.r5.2xlarge   | Memory optimized  | No          | 8    | 64           | Amazon EBS Only       |
| ml.r5.4xlarge   | Memory optimized  | No          | 16   | 128          | Amazon EBS Only       |
| ml.r5.8xlarge   | Memory optimized  | No          | 32   | 256          | Amazon EBS Only       |
| ml.r5.12xlarge  | Memory optimized  | No          | 48   | 384          | Amazon EBS Only       |
| ml.r5.16xlarge  | Memory optimized  | No          | 64   | 512          | Amazon EBS Only       |
| ml.r5.24xlarge  | Memory optimized  | No          | 96   | 768          | Amazon EBS Only       |

## Instances with 1 or more GPUs

The following table lists the Amazon EC2 instance types with 1 or more GPUs attached that
are available for use with Studio Classic notebooks. It also lists information about the
specifications of each instance type. The default instance type for GPU-based images is
`ml.g4dn.xlarge`.

For detailed information on which instance types fit your use case, and their
performance capabilities, see [Amazon Elastic Compute Cloud
Instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/"). For information about pricing for these instance types, see
[Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").

Instances with 1 or more GPUs

| Instance         | Use case              | Fast launch | GPUs | vCPU | Memory (GiB) | GPU Memory (GiB) | Instance Storage (GB) |
| ---------------- | --------------------- | ----------- | ---- | ---- | ------------ | ---------------- | --------------------- |
| ml.p3.2xlarge    | Accelerated computing | No          | 1    | 8    | 61           | 16               | Amazon EBS Only       |
| ml.p3.8xlarge    | Accelerated computing | No          | 4    | 32   | 244          | 64               | Amazon EBS Only       |
| ml.p3.16xlarge   | Accelerated computing | No          | 8    | 64   | 488          | 128              | Amazon EBS Only       |
| ml.p3dn.24xlarge | Accelerated computing | No          | 8    | 96   | 768          | 256              | 2 x 900 NVMe SSD      |
| ml.p4d.24xlarge  | Accelerated computing | No          | 8    | 96   | 1152         | 320 GB HBM2      | 8 x 1000 NVMe SSD     |
| ml.p4de.24xlarge | Accelerated computing | No          | 8    | 96   | 1152         | 640 GB HBM2e     | 8 x 1000 NVMe SSD     |
| ml.g4dn.xlarge   | Accelerated computing | Yes         | 1    | 4    | 16           | 16               | 1 x 125 NVMe SSD      |
| ml.g4dn.2xlarge  | Accelerated computing | No          | 1    | 8    | 32           | 16               | 1 x 225 NVMe SSD      |
| ml.g4dn.4xlarge  | Accelerated computing | No          | 1    | 16   | 64           | 16               | 1 x 225 NVMe SSD      |
| ml.g4dn.8xlarge  | Accelerated computing | No          | 1    | 32   | 128          | 16               | 1 x 900 NVMe SSD      |
| ml.g4dn.12xlarge | Accelerated computing | No          | 4    | 48   | 192          | 64               | 1 x 900 NVMe SSD      |
| ml.g4dn.16xlarge | Accelerated computing | No          | 1    | 64   | 256          | 16               | 1 x 900 NVMe SSD      |
| ml.g5.xlarge     | Accelerated computing | No          | 1    | 4    | 16           | 24               | 1 x 250 NVMe SSD      |
| ml.g5.2xlarge    | Accelerated computing | No          | 1    | 8    | 32           | 24               | 1 x 450 NVMe SSD      |
| ml.g5.4xlarge    | Accelerated computing | No          | 1    | 16   | 64           | 24               | 1 x 600 NVMe SSD      |
| ml.g5.8xlarge    | Accelerated computing | No          | 1    | 32   | 128          | 24               | 1 x 900 NVMe SSD      |
| ml.g5.12xlarge   | Accelerated computing | No          | 4    | 48   | 192          | 96               | 1 x 3800 NVMe SSD     |
| ml.g5.16xlarge   | Accelerated computing | No          | 1    | 64   | 256          | 24               | 1 x 1900 NVMe SSD     |
| ml.g5.24xlarge   | Accelerated computing | No          | 4    | 96   | 384          | 96               | 1 x 3800 NVMe SSD     |
| ml.g5.48xlarge   | Accelerated computing | No          | 8    | 192  | 768          | 192              | 2 x 3800 NVMe SSD     |
