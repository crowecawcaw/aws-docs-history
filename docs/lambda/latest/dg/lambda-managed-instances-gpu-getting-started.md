

# Getting started with GPU-accelerated Event Functions

To run GPU-accelerated Event Functions on AWS Lambda Managed Instances, you create a capacity provider with GPU instance types, build a container image from a GPU base image, create a function with accelerator memory on that capacity provider, and publish a version. This page walks through those four steps.

## Step 1: Create a GPU-instance capacity provider
<a name="lambda-managed-instances-gpu-getting-started-step1"></a>

**Note**  
This tutorial assumes you already have a capacity provider operator role and VPC resources (subnets and security groups). To create them, see [Getting started with Lambda Managed Instances](lambda-managed-instances-getting-started.md).

Create a capacity provider for your GPU-accelerated functions by listing at least one [supported GPU instance type](lambda-managed-instances-gpu.md#lambda-managed-instances-gpu-supported-instances) in `AllowedInstanceTypes`. A capacity provider cannot mix GPU and non-GPU instance types, so use a dedicated capacity provider for GPU-accelerated functions. To maximize availability, specify multiple GPU instance types across generations. Lambda attempts to use newer generations and falls back to older generations if capacity for newer generations is unavailable.

```bash
aws lambda create-capacity-provider \
  --capacity-provider-name my-gpu-capacity-provider \
  --vpc-config SubnetIds=[$SUBNET_ID],SecurityGroupIds=[$SECURITY_GROUP_ID] \
  --permissions-config CapacityProviderOperatorRoleArn=arn:aws:iam::${ACCOUNT_ID}:role/MyOperatorRole \
  --instance-requirements '{
    "Architectures": ["x86_64"],
    "AllowedInstanceTypes": ["g6.4xlarge", "g5.4xlarge", "g4dn.4xlarge"]
  }'
```

## Step 2: Build and push your function's container image
<a name="lambda-managed-instances-gpu-getting-started-step2"></a>

GPU-accelerated functions require a container image deployment package. Lambda provides GPU-enabled container base images in the [Amazon ECR Public Gallery](https://gallery.ecr.aws/lambda), with preinstalled GPU libraries including CUDA, PyTorch, vLLM, and SGLang. You can start from a Lambda GPU base image and add your handler code and dependencies, or build your own image from scratch using the Lambda runtime interface client. For more information, see [GPU base images](lambda-managed-instances-gpu-base-images.md).

The following Dockerfile uses the PyTorch base image, downloads the ResNet-18 model weights at build time, and copies in the handler. The Dockerfile saves the weights into the image at `/opt/model`, so the function loads them from there and does not download anything when it starts. The image is read-only when the function runs, and `/tmp` is the only writable directory. Keep anything that your code writes at runtime, such as a model cache, under `/tmp`.

To reduce startup time, we recommend storing large artifacts, such as model weights, outside your container image. For more information, see [Optimizing startup time for GPU-accelerated functions](lambda-managed-instances-gpu-startup.md).

Dockerfile:

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/pytorch:cuda

RUN mkdir -p /opt/model && python3 -c "import torch; from torchvision import models; \
    torch.save(models.resnet18(weights=models.ResNet18_Weights.DEFAULT).state_dict(), '/opt/model/resnet18.pth')" \
    && rm -rf /tmp/torch

COPY handler.py /var/task/
CMD ["handler.handler"]
```

The `handler.py` file loads the ResNet-18 weights from the image onto the GPU during initialization and runs one inference per invocation on a sample tensor:

```python
import torch
from torchvision import models

model = models.resnet18()
model.load_state_dict(torch.load("/opt/model/resnet18.pth", map_location="cpu", weights_only=True))
model = model.cuda().eval()

def handler(event, context):
    x = torch.randn(1, 3, 224, 224, device="cuda")   # image-shaped tensor
    with torch.inference_mode():
        logits = model(x)
    return {"device": str(logits.device), "top_class_index": int(logits.argmax(1))}
```

Then, follow the instructions below to create an Amazon Elastic Container Registry (Amazon ECR) repository, build the image, and push it to the repository.

```bash
aws ecr create-repository --repository-name my-gpu-image --region ${REGION}

aws ecr get-login-password --region ${REGION} | \
  docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

docker build -t my-gpu-image .
docker tag my-gpu-image:latest ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/my-gpu-image:latest
docker push ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/my-gpu-image:latest
```

## Step 3: Create your GPU-accelerated Lambda event function
<a name="lambda-managed-instances-gpu-getting-started-step3"></a>

When creating a GPU-accelerated function, specify the accelerator memory (GPU VRAM) your workload needs using the `AcceleratorConfig` field:

```bash
aws lambda create-function \
  --function-name my-gpu-function \
  --package-type Image \
  --code ImageUri=${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/my-gpu-image:latest \
  --role arn:aws:iam::${ACCOUNT_ID}:role/MyLambdaExecutionRole \
  --architectures x86_64 \
  --memory-size 10240 \
  --timeout 900 \
  --ephemeral-storage Size=32768 \
  --accelerator-config '{"AcceleratorMemorySize":16}' \
  --capacity-provider-config LambdaManagedInstancesCapacityProviderConfig={CapacityProviderArn=arn:aws:lambda:${REGION}:${ACCOUNT_ID}:capacity-provider:my-gpu-capacity-provider}
```

When you set these parameters, keep the following in mind:
+ **Timeout** – `--timeout` sets the maximum duration of an invocation. On Lambda Managed Instances it also determines the initialization timeout, which is the larger of 130 seconds and the function timeout, up to 15 minutes. Set it long enough for your workload's initialization and invocation. For more information, see [Understanding the Lambda Managed Instances execution environment](lambda-managed-instances-execution-environment.md#lambda-managed-instances-init-phase).
+ **Ephemeral storage** – Set `--ephemeral-storage` (`/tmp`) large enough for your workload's storage needs. GPU-accelerated functions run on EC2 instances with NVMe-backed storage, included at no additional charge. The default is 512 MB and the maximum is 32,768 MB. For more information, see the [Limits](lambda-managed-instances-gpu.md#lambda-managed-instances-gpu-limits) section.
+ **Memory size** – Set `--memory-size` to the host memory your function requires. Lambda reserves part of each instance's system memory for management operations. Choose an instance type with enough memory for your function plus this reserved portion.

## Step 4: Publish and invoke
<a name="lambda-managed-instances-gpu-getting-started-step4"></a>

As with other functions on Lambda Managed Instances, publish a version to deploy your GPU-accelerated function to your capacity provider. This example uses `$LATEST.PUBLISHED`, which deploys your latest code without numbered versions. For workloads that require controlled rollouts, or whose invocations run for many minutes, you can use numbered versions with [weighted aliases](configuring-alias-routing.md) to shift traffic between versions. For more information about deployment best practices, see [Deployment best practices for GPU-accelerated functions](lambda-managed-instances-gpu-best-practices.md#lambda-managed-instances-gpu-best-practices-deployments).

**Note**  
Lambda maintains GPU capacity for each active version. To free capacity for new versions, delete or deactivate versions you no longer use.

```bash
aws lambda publish-version --function-name my-gpu-function --publish-to LATEST_PUBLISHED
```

After the publish operation completes and the version is active, invoke your function:

```bash
aws lambda invoke \
  --function-name my-gpu-function \
  --cli-binary-format raw-in-base64-out \
  --payload '{}' \
  response.json
```

**Note**  
The command does not specify a version. When you invoke a function on Lambda Managed Instances without a version or alias, Lambda invokes the `$LATEST.PUBLISHED` version.

## Clean up
<a name="lambda-managed-instances-gpu-getting-started-cleanup"></a>

To avoid incurring charges, delete the resources you created:

1. Delete the function:

   ```bash
   aws lambda delete-function --function-name my-gpu-function
   ```

1. Delete the capacity provider:

   ```bash
   aws lambda delete-capacity-provider --capacity-provider-name my-gpu-capacity-provider
   ```

1. Delete the Amazon ECR repository:

   ```bash
   aws ecr delete-repository --repository-name my-gpu-image --force --region ${REGION}
   ```