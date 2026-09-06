

# Create a job definition on Amazon ECS Managed Instances
<a name="create-job-definition-ecs-managed-instances"></a>

Amazon ECS Managed Instances job definitions use `ecsProperties` with the `MANAGED_INSTANCES` platform capability. Unlike Fargate, there are no restrictions on vCPU and memory size combinations, and GPU resources are supported. For more information about supported parameters, see [Job definitions on Amazon ECS Managed Instances](ecs-managed-instances-job-definitions.md).

## Creating a job definition on Amazon ECS Managed Instances (console)
<a name="create-jd-ecs-managed-instances-console"></a>

**To create a new job definition on Amazon ECS Managed Instances:**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. From the top navigation bar, choose the AWS Region to use.

1. In the left navigation pane, choose **Job definitions**.

1. Choose **Create**.

1. For **Orchestration type**, choose **ECS Managed Instances**.

1. For **Name**, enter a unique name for your job definition. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).

1. (Optional) For **Execution timeout**, enter the timeout value (in seconds). The execution timeout is the length of time before an unfinished job is terminated. If an attempt exceeds the timeout duration, the attempt is stopped and moves to a `FAILED` status. For more information, see [Job timeouts](job_timeouts.md). The minimum value is 60 seconds.

1. For **Execution role**, choose an IAM role that grants the Amazon ECS container agent permission to make AWS API calls on your behalf. This role is required for Amazon ECS Managed Instances jobs. For example, the role is used to pull container images from Amazon ECR.

1. In the **Container configuration** section:

   1. For **Image**, enter the container image to use for the job. Images in Amazon ECR registries can be specified with the `{{repository-url}}/{{image}}:{{tag}}` naming convention. Images in public registries use the full URI (for example, `public.ecr.aws/amazonlinux/amazonlinux:2023`).

   1. For **Command**, enter the command to pass to the container.

   1. For **vCPUs**, specify the number of vCPUs to reserve for the container.

   1. For **Memory**, specify the memory limit (in MiB) available to the container.

   1. (Optional) For **GPUs**, specify the number of GPU devices to make available to the container. The compute environment must have GPU instances available.

1. (Optional) Expand **Tags**, and then choose **Add tag** to add tags to the resource. Turn on **Propagate tags** to propagate tags from the job and job definition.

1. Choose **Create job definition**.

## Creating a job definition on Amazon ECS Managed Instances (AWS CLI)
<a name="create-jd-ecs-managed-instances-cli"></a>

Use the `register-job-definition` command to create a job definition for Amazon ECS Managed Instances.

### Basic example
<a name="create-jd-ecs-managed-instances-cli-basic"></a>

The following example creates a minimal job definition that runs a simple command.

```
$ aws batch register-job-definition \
    --job-definition-name {{my-managed-instances-job-def}} \
    --type container \
    --platform-capabilities MANAGED_INSTANCES \
    --ecs-properties '{
      "taskProperties": [{
        "containers": [{
          "image": "public.ecr.aws/amazonlinux/amazonlinux:2023",
          "name": "main",
          "command": ["echo", "hello managed instances"],
          "resourceRequirements": [
            {"type": "VCPU", "value": "1"},
            {"type": "MEMORY", "value": "1024"}
          ]
        }],
        "executionRoleArn": "arn:aws:iam::{{123456789012}}:role/{{ecsTaskExecutionRole}}"
      }]
    }'
```

### GPU job definition
<a name="create-jd-ecs-managed-instances-cli-gpu"></a>

The following example creates a job definition that requests GPU resources.

```
$ aws batch register-job-definition \
    --job-definition-name {{my-gpu-managed-instances-job-def}} \
    --type container \
    --platform-capabilities MANAGED_INSTANCES \
    --ecs-properties '{
      "taskProperties": [{
        "containers": [{
          "image": "{{123456789012}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{my-gpu-image}}:latest",
          "name": "main",
          "command": ["nvidia-smi"],
          "resourceRequirements": [
            {"type": "VCPU", "value": "4"},
            {"type": "MEMORY", "value": "16384"},
            {"type": "GPU", "value": "1"}
          ]
        }],
        "executionRoleArn": "arn:aws:iam::{{123456789012}}:role/{{ecsTaskExecutionRole}}"
      }]
    }'
```

### Multi-container (sidecar) job definition
<a name="create-jd-ecs-managed-instances-cli-sidecar"></a>

The following example creates a job definition with a main container and a sidecar logging container.

```
$ aws batch register-job-definition \
    --job-definition-name {{my-sidecar-managed-instances-job-def}} \
    --type container \
    --platform-capabilities MANAGED_INSTANCES \
    --ecs-properties '{
      "taskProperties": [{
        "containers": [{
          "image": "public.ecr.aws/amazonlinux/amazonlinux:2023",
          "name": "main",
          "command": ["echo", "processing data"],
          "essential": true,
          "resourceRequirements": [
            {"type": "VCPU", "value": "2"},
            {"type": "MEMORY", "value": "4096"}
          ]
        },
        {
          "image": "public.ecr.aws/amazonlinux/amazonlinux:2023",
          "name": "sidecar",
          "command": ["echo", "logging sidecar"],
          "essential": false,
          "resourceRequirements": [
            {"type": "VCPU", "value": "1"},
            {"type": "MEMORY", "value": "512"}
          ]
        }],
        "executionRoleArn": "arn:aws:iam::{{123456789012}}:role/{{ecsTaskExecutionRole}}"
      }]
    }'
```