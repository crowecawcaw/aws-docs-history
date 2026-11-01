

# Using GPU partitions on SageMaker AI real-time endpoints
<a name="inference-components-accelerator-partitioning"></a>

Amazon SageMaker AI GPU partitioning (GPU partitioning) lets you run several models on one Graphics Processing Unit (GPU). GPU partitioning uses NVIDIA Multi-Instance GPU (MIG) to divide one physical GPU into multiple independent partitions. MIG gives each partition a fixed share of the GPU's compute slices and a dedicated block of its memory.

Use GPU partitioning when your models don't each need a whole GPU. Instead of one GPU per model, several inference components share one GPU, each in its own partition. For more information about inference components, see [Inference components](realtime-endpoints-deploy-models.md#inference-components).

## Benefits
<a name="accelerator-partitioning-benefits"></a>

Improved GPU utilization  
Host several models on one GPU instead of dedicating a whole GPU to a model that can't fill it.

Hardware-enforced isolation  
Each partition has its own compute slices and GPU memory, so one model can't read another model's GPU memory or take its throughput.

No change to invocation  
You invoke a model by inference component name, as you do without partitioning. The partition doesn't appear in the request.

**Note**  
GPU partitioning isolates the GPU's compute slices and memory. Models on the same instance still share host CPU, host memory, storage, and networking.

## How GPU partitioning works
<a name="accelerator-partitioning-how"></a>

You turn on GPU partitioning with two optional API fields:
+ `AcceleratorPartitionLayouts` on a production variant of an endpoint that hosts inference components. It declares how SageMaker AI partitions every accelerator on every instance in that variant.
+ `AcceleratorPartitionType` on an inference component. It assigns the inference component to a partition type.

GPU partitioning adds no new API operations, resource types, or IAM actions. Endpoints that omit both fields behave as they do without partitioning.

A partition type states one partition's share of an accelerator. For example, `mig-4g.20gb` is 4 compute slices and 20 GB of GPU memory.

SageMaker AI partitions the accelerators while it launches the instances for the endpoint. When the endpoint is `InService`, every accelerator is partitioned and the partitions are empty. You then place models on the partitions by creating inference components.

**Important**  
To use a different partition layout, create a new endpoint. You can't change the partition layout of a running endpoint. An `UpdateEndpoint` request to an endpoint configuration with a different layout returns a 400 error.

### Monitor partitioned endpoints
<a name="accelerator-partitioning-monitoring"></a>

To monitor with Amazon CloudWatch, use the invocation and latency metrics that the endpoint publishes. Partitioned endpoints and their inference components don't publish GPU, CPU, or memory utilization metrics.

## Supported instances and Regions
<a name="accelerator-partitioning-supported"></a>

GPU partitioning is supported on the following instance families:
+ P4d, NVIDIA A100 (40 GB) accelerators
+ P5, NVIDIA H100 (80 GB) accelerators
+ G7, NVIDIA RTX PRO 4500 (32 GB) accelerators
+ G7e, NVIDIA RTX PRO 6000 (96 GB) accelerators

GPU partitioning is available in the following AWS Regions:
+ US East (N. Virginia) `us-east-1`
+ US East (Ohio) `us-east-2`
+ US West (Oregon) `us-west-2`
+ Asia Pacific (Singapore) `ap-southeast-1`
+ Asia Pacific (Tokyo) `ap-northeast-1`
+ Europe (Frankfurt) `eu-central-1`
+ Europe (Ireland) `eu-west-1`

**Note**  
Instance availability varies by AWS Region. Confirm that your instance type is available in your Region, and that you have endpoint usage quota for it.

### GPU partition types
<a name="accelerator-partitioning-types"></a>

The valid partition types depend on the instance's GPU. If you specify a partition type for a different GPU, SageMaker AI rejects the request with a 400 error that lists the valid values.

The **Partitions per GPU** column is the number of partitions of that type that fit on one GPU. To find the number of partitions on an instance, multiply by the number of GPUs on the instance. For example, an `ml.p4d.24xlarge` instance has 8 GPUs, so a layout of three `mig-1g.5gb` partitions provides 24 partitions on the instance.

**P4d, NVIDIA A100 (40 GB)**


**Partition types for P4d instances**  

| Partition type | GPU memory | Partitions per GPU | 
| --- | --- | --- | 
| `mig-1g.5gb` | 5 GB | 7 | 
| `mig-1g.10gb` | 10 GB | 4 | 
| `mig-2g.10gb` | 10 GB | 3 | 
| `mig-3g.20gb` | 20 GB | 2 | 
| `mig-4g.20gb` | 20 GB | 1 | 
| `mig-7g.40gb` | 40 GB | 1 | 

**Important**  
On P4d instances, the `mig-1g.10gb` partition type requires a newer NVIDIA driver than the default image provides. If you request it on the default image, SageMaker AI accepts the request, and the host then fails to partition the accelerators without reporting which partition type caused the failure. To use `mig-1g.10gb` on a P4d instance, set `InferenceAmiVersion` to `al2023-ami-sagemaker-inference-gpu-4-1` on the production variant. For the driver version that each AMI version provides, see [Current versions and supported instance families](inference-gpu-drivers.md#inference-gpu-drivers-versions).

**P5, NVIDIA H100 (80 GB)**


**Partition types for P5 instances**  

| Partition type | GPU memory | Partitions per GPU | 
| --- | --- | --- | 
| `mig-1g.10gb` | 10 GB | 7 | 
| `mig-1g.20gb` | 20 GB | 4 | 
| `mig-2g.20gb` | 20 GB | 3 | 
| `mig-3g.40gb` | 40 GB | 2 | 
| `mig-4g.40gb` | 40 GB | 1 | 
| `mig-7g.80gb` | 80 GB | 1 | 

**G7, NVIDIA RTX PRO 4500 (32 GB)**


**Partition types for G7 instances**  

| Partition type | GPU memory | Partitions per GPU | 
| --- | --- | --- | 
| `mig-1g.16gb` | 16 GB | 2 | 
| `mig-2g.32gb` | 32 GB | 1 | 

**G7e, NVIDIA RTX PRO 6000 (96 GB)**


**Partition types for G7e instances**  

| Partition type | GPU memory | Partitions per GPU | 
| --- | --- | --- | 
| `mig-1g.24gb` | 24 GB | 4 | 
| `mig-2g.48gb` | 48 GB | 2 | 
| `mig-4g.96gb` | 96 GB | 1 | 

## Resources
<a name="accelerator-partitioning-resources"></a>

For more information about MIG, see the following NVIDIA documentation:
+ [NVIDIA Supported MIG Profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html)
+ [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/)

**Topics**
+ [Benefits](#accelerator-partitioning-benefits)
+ [How GPU partitioning works](#accelerator-partitioning-how)
+ [Supported instances and Regions](#accelerator-partitioning-supported)
+ [Resources](#accelerator-partitioning-resources)
+ [Create an endpoint with GPU partitions](inference-components-accelerator-partitioning-create.md)
+ [Deploy models to GPU partitions with inference components](inference-components-accelerator-partitioning-deploy.md)
+ [Manage GPU partitioned endpoints](inference-components-accelerator-partitioning-manage.md)
+ [Troubleshooting](inference-components-accelerator-partitioning-troubleshoot.md)