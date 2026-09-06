

# Example Neuron task definitions
<a name="ecs-inference-task-def"></a>

## Managed device allocation example
<a name="ecs-inference-task-def-managed"></a>

The following example shows a task definition that requests all Neuron devices on the instance using the `resourceRequirements` parameter. This approach is only available on Managed Instances.

```
{
    "family": "ecs-neuron",
    "requiresCompatibilities": ["MANAGED_INSTANCES"],
    "networkMode": "awsvpc",
    "cpu": "8192",
    "memory": "16384",
    "executionRoleArn": "{{${YOUR_EXECUTION_ROLE}}}",
    "containerDefinitions": [
        {
            "name": "neuron-inference",
            "image": "763104351884.dkr.ecr.us-east-1.amazonaws.com/huggingface-vllm-inference-neuronx:0.11.0-optimum0.4.5-neuronx-py310-sdk2.26.1-ubuntu22.04",
            "essential": true,
            "command": [
                "--model", "{{${YOUR_HUGGING_FACE_MODEL_ID}}}",
                "--port", "8080",
                "--tensor-parallel-size", "2",
                "--allow-non-cached-model"
            ],
            "portMappings": [
                {
                    "containerPort": 8080,
                    "protocol": "tcp"
                }
            ],
            "resourceRequirements": [
                {
                    "type": "NeuronDevice",
                    "value": "ALL"
                }
            ]
        }
    ]
}
```

In this example, the container image includes a vLLM inference server optimized for AWS Neuron. The image's entrypoint downloads a model from HuggingFace, compiles it for Neuron, and starts an OpenAI-compatible API server on port 8080. Replace `{{${YOUR_HUGGING_FACE_MODEL_ID}}}` with your HuggingFace model ID.

## Manual device specification example
<a name="ecs-inference-task-def-ec2"></a>

The following example shows a Linux task definition for `inf1.xlarge` using the EC2 launch type with `linuxParameters.devices` to specify Neuron device paths.

```
{
    "family": "ecs-neuron",
    "requiresCompatibilities": ["EC2"],
    "placementConstraints": [
        {
            "type": "memberOf",
            "expression": "attribute:ecs.os-type == linux"
        },
        {
            "type": "memberOf",
            "expression": "attribute:ecs.instance-type == {{inf1.xlarge}}"
        }
    ],
    "executionRoleArn": "{{${YOUR_EXECUTION_ROLE}}}",
    "containerDefinitions": [
        {
            "entryPoint": [
                "/usr/local/bin/entrypoint.sh",
                "--port=8500",
                "--rest_api_port=9000",
                "--model_name=resnet50_neuron",
                "--model_base_path=s3://{{amzn-s3-demo-bucket/resnet50_neuron/}}"
            ],
            "portMappings": [
                {
                    "hostPort": 8500,
                    "protocol": "tcp",
                    "containerPort": 8500
                },
                {
                    "hostPort": 8501,
                    "protocol": "tcp",
                    "containerPort": 8501
                },
                {
                    "hostPort": 0,
                    "protocol": "tcp",
                    "containerPort": 80
                }
            ],
            "linuxParameters": {
                "devices": [
                    {
                        "containerPath": "/dev/neuron0",
                        "hostPath": "/dev/neuron0",
                        "permissions": [
                            "read",
                            "write"
                        ]
                    }
                ],
                "capabilities": {
                    "add": [
                        "IPC_LOCK"
                    ]
                }
            },
            "cpu": 0,
            "memoryReservation": 1000,
            "image": "{{763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-inference-neuron:1.15.4-neuron-py37-ubuntu18.04}}",
            "essential": true,
            "name": "resnet50"
        }
    ]
}
```