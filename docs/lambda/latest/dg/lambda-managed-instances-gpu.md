

# Run GPU-accelerated Event Functions on Lambda Managed Instances

With AWS Lambda Managed Instances, you can run Event Functions on GPU-based Amazon EC2 instances. Like all Event Functions, you can invoke your GPU-accelerated functions synchronously, asynchronously, or via [event source mappings (ESMs)](invocation-eventsourcemapping.md) from over 200 AWS services. Lambda manages the underlying GPU instances, including auto-scaling, request routing, and load balancing.

Lambda also manages the GPU drivers on these instances and provides base container images containing popular GPU frameworks and libraries (vLLM, SGLang, and PyTorch) for you to get started. You can use these base images as-is, extend them with your own functionality, or use your own container images. To optimize your GPU resource utilization, Lambda runs multiple invocations concurrently in each execution environment and horizontally scales the underlying instances based on GPU utilization, CPU utilization, and concurrency.

## Key capabilities
<a name="lambda-managed-instances-gpu-key-capabilities"></a>

GPU-accelerated Lambda Event Functions provide the following capabilities:
+ **Managed GPU infrastructure** – Lambda launches GPU instances in your account and manages their lifecycle, operating system and GPU driver patching, health checks, and scaling.
+ **Prebuilt base images** – Lambda provides GPU base images with CUDA, PyTorch, CuPy, and the vLLM and SGLang inference servers. The libraries in each image are compatible with the GPU driver that Lambda installs, so you do not need to match library versions to the driver yourself. You can also extend these base images with additional libraries, or build your own from scratch. For more information, see [GPU base images for Lambda Managed Instances](lambda-managed-instances-gpu-base-images.md).
+ **GPU-based scaling** – Capacity providers with GPU instance types scale on GPU utilization in addition to CPU utilization and concurrency. To avoid paying for idle GPU capacity, you can enable [scaling to zero](lambda-managed-instances-scaling.md#lambda-managed-instances-scale-to-zero). For more information, see [How scaling works for GPU-accelerated Event Functions](lambda-managed-instances-gpu-scaling.md).
+ **Concurrency within an execution environment** – Each execution environment processes several invocations at the same time. You control this with the `PerExecutionEnvironmentMaxConcurrency` setting. For more information, see [How concurrency works for GPU-accelerated Event Functions](lambda-managed-instances-gpu-scaling.md#lambda-managed-instances-gpu-scaling-concurrency).
+ **Larger images and ephemeral storage** – GPU-accelerated functions support larger container images and ephemeral storage than other Event Functions. For values, see [Limits](#lambda-managed-instances-gpu-limits).
+ **Optimizing execution environment startup** – To lower startup time with large images, use lazy loading with Seekable OCI (SOCI), and load model weights from Amazon S3 with the Amazon S3 Connector for PyTorch or the Run:ai Model Streamer included in the base images. The Lambda GPU base images with the `-soci` tag suffix (for example, `base:cuda-v1-soci`) include a prebuilt SOCI index, so lazy loading works without additional setup. For more information, see [Optimizing startup time](lambda-managed-instances-gpu-startup.md).
+ **Event-driven GPU compute** – GPU-accelerated functions support the same event sources as x86 and Arm-based Event Functions. For more information about event sources, see [Invoking Lambda with events from other AWS services](lambda-services.md).
+ **Built-in GPU observability** – Lambda publishes GPU utilization, GPU memory utilization, GPU memory used, and GPU power utilization metrics to Amazon CloudWatch Metrics and displays them in the Lambda console, at both the capacity provider and function level. For more information, see [Monitoring GPU-accelerated functions](lambda-managed-instances-gpu-monitoring.md).
+ **EC2 pricing model** – GPU-accelerated functions use the same pricing model as other functions on Lambda Managed Instances. For details, see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).

## When to use GPU-accelerated functions
<a name="lambda-managed-instances-gpu-use-cases"></a>

GPU-accelerated functions are suited to AI and non-AI workloads that rely on highly parallel computation, such as large matrix operations or per-pixel and per-frame processing. Use this capability when:
+ **Your workload is event-driven** – GPU compute runs as one step in your application. It's triggered by events from Amazon Simple Storage Service, Amazon Simple Queue Service, Amazon API Gateway, or other AWS services, with no custom integration code.
+ **You don't want to manage GPU infrastructure** – You want to run GPU code without managing AMIs, drivers, or CUDA versions. Additionally you want Lambda to manage the instance scaling and utilization.

Consider using [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) when you want to work with foundation models. For model training or control over the machine learning model lifecycle, consider using [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html).

Common use cases for GPU-accelerated functions running on Lambda Managed Instances include:
+ **Custom model inference** – Inference models for decision-making, computer vision, speech-to-text and text-to-speech, recommendation, document analysis, and small-to-mid-size language models deployed as part of an application
+ **Media processing** – Video and image transcoding, encoding, and decoding with the GPU's hardware encoders and decoders
+ **Rendering** – Frames, scenes, and previews rendered with OpenGL or Vulkan
+ **Scientific and numerical computing** – GPU-accelerated array operations, simulations, and data processing triggered by events

## How it works
<a name="lambda-managed-instances-gpu-how-it-works"></a>

GPU-accelerated functions use the same building blocks as other Event Functions on Lambda Managed Instances:

**Note**  
GPU-accelerated functions run on accelerated Amazon EC2 On-Demand instances, and the relevant Amazon EC2 On-Demand instance quota defaults to 0 vCPUs. Request a quota increase before you deploy a GPU-accelerated function. For more information, see the [Limits](#lambda-managed-instances-gpu-limits) section on this page.

1. **Create a GPU capacity provider** – List only GPU instance types from [Supported GPU instances](#lambda-managed-instances-gpu-supported-instances) in `AllowedInstanceTypes`.

1. **Build your container image** – Use one of Lambda's GPU base images directly, extend it with your own handler and dependencies, or use your own custom GPU base image. For more information, see [GPU base images](lambda-managed-instances-gpu-base-images.md).

1. **Create your GPU-accelerated function** – Create a function from your container image, attach it to the capacity provider, and set `AcceleratorConfig` to the accelerator memory your workload needs.

1. **Publish a function version** – When you publish a version, Lambda launches GPU instances in your account, pulls the image you specified, starts execution environments on the GPUs, and marks the version `ACTIVE`.

For a detailed walk-through, see [Getting started with GPU-accelerated Event Functions](lambda-managed-instances-gpu-getting-started.md).

## Supported GPU instances
<a name="lambda-managed-instances-gpu-supported-instances"></a>

GPU-accelerated functions run on the following Amazon EC2 instance families. All sizes in each family are supported except `g4dn.metal`.


| Instance family | GPU | Accelerator memory per GPU | 
| --- | --- | --- | 
| G4dn | NVIDIA T4 | 16 GB | 
| G5 | NVIDIA A10G | 24 GB | 
| G6 | NVIDIA L4 | 24 GB | 
| Gr6 | NVIDIA L4 | 24 GB | 
| G6e | NVIDIA L40S | 48 GB | 
| G6f | NVIDIA L4 (fractional) | 3, 6, or 12 GB, depending on instance size | 
| Gr6f | NVIDIA L4 (fractional) | 12 GB | 

For pricing and Region availability, see the [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/) page.

## GPU assignment
<a name="lambda-managed-instances-gpu-assignment"></a>

Lambda assigns GPUs to execution environments according to the following rules:
+ **One GPU per execution environment** – On GPU instance types with whole GPUs (such as G4dn, G5, G6, Gr6, and G6e), Lambda assigns exactly one GPU to each execution environment. Lambda runs multiple execution environments, one per GPU, on instance types with more than one GPU.
+ **Fractional GPUs** – On fractional GPU instance types (such as G6f and Gr6f), Amazon EC2 provides access to a fraction of a physical GPU as a full virtual GPU, and Lambda assigns that virtual GPU to an execution environment. Each GPU fraction serves one execution environment.

To ensure you have sufficient GPU capacity for your workload, you can purchase EC2 On-Demand Capacity Reservations (ODCRs). If you create an ODCR for an instance type and Availability Zone that match your capacity provider configuration, Lambda automatically uses that reserved capacity. For more information, see [Reserve compute capacity with Amazon EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html).

## Understanding accelerator memory
<a name="lambda-managed-instances-gpu-accelerator-memory"></a>

You specify the accelerator memory (GPU VRAM) your function needs with the `AcceleratorMemorySize` field of `AcceleratorConfig`. Because each execution environment runs on exactly one GPU, or one GPU fraction on fractional GPU instances, Lambda picks an instance type from your provided GPU instance type list such that an instance's GPU memory satisfies your function's specified accelerator memory.

You set `AcceleratorMemorySize` in `AcceleratorConfig` when you create or update the function.
+ Valid values: 3, 6, 12, 16, 24, 48 (GB)
+ `AcceleratorMemorySize` is a minimum. Lambda launches instances whose accelerator has at least this much memory and, when several instance types in your capacity provider qualify, chooses the latest generation with the lowest GPU memory that satisfies your function's GPU memory requirement.
+ When your capacity provider includes multiple instance types and the best-fit type has insufficient capacity, Lambda falls back to another allowed instance type. During instance fallback, Lambda can place the execution environment on a GPU with more memory than you requested. For more information, see [Instance type selection](lambda-managed-instances-gpu-scaling.md#lambda-managed-instances-gpu-scaling-instance-selection).
+ The capacity provider must include at least one instance type whose accelerator has this much memory. Otherwise, the `CreateFunction` and `UpdateFunctionConfiguration` API actions return an `InvalidParameterValueException` that asks you to use a capacity provider with larger GPU instances or to reduce the accelerator memory. The function is not created or updated.

## Limits
<a name="lambda-managed-instances-gpu-limits"></a>

Two controls govern GPU instance usage:
+ **EC2 On-Demand vCPU quota** – GPU-accelerated functions run on EC2 On-Demand GPU instances in your account. The EC2 service quota Running On-Demand G and VT instances controls how many vCPUs of G-family instances your account can run. The default value for this quota is 0 vCPUs for On-Demand G and VT instances, so you must request a quota increase before you can deploy GPU-accelerated functions. To request an increase, open the [Service Quotas console for Amazon EC2](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/) and submit a request for the Running On-Demand G and VT instances quota. For more information about On-Demand Instance quotas, see [Amazon EC2 On-Demand Instance quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html#ec2-on-demand-instances-limits).
+ **Capacity provider MaxVCpuCount (optional)** – To limit GPU usage for a specific capacity provider, set `MaxVCpuCount` to restrict the total vCPUs Lambda can launch. Each GPU instance type consumes a fixed number of vCPUs (for example, `g6.4xlarge` uses 16 vCPUs), so this setting controls how many instances can run within a capacity provider.

The following table compares the function limits for GPU-accelerated functions with those for other Event Functions on Lambda Managed Instances.


| Resource | GPU-accelerated functions | Other Event Functions on Lambda Managed Instances | 
| --- | --- | --- | 
| Deployment package | Container image only | .zip file archive or container image | 
| Runtime | Provided by your container image | Managed runtimes or container image | 
| Container image size | 32 GB | 10 GB | 
| Maximum size of a single file in a container image | 10 GB | 10 GB | 
| Ephemeral storage (/tmp) | 512 MB to 32,768 MB | 512 MB to 10,240 MB | 
| MemorySize | 2,048 MB to 32,768 MB | 2,048 MB to 32,768 MB | 
| AcceleratorMemorySize | 3 GB to 48 GB (valid values: 3, 6, 12, 16, 24, 48) | Not applicable | 
| PerExecutionEnvironmentMaxConcurrency | Default 4, maximum 48 | See the runtime guides in [Lambda Managed Instances runtimes](lambda-managed-instances-runtimes.md) | 
| Default MinExecutionEnvironments | 1 | 3 | 
| GPUs per execution environment | 1 | Not applicable | 