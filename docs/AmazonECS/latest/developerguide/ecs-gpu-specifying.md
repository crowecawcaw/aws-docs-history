# Specifying GPUs in an Amazon ECS task definition

To use the GPUs on a container instance and the Docker GPU runtime, make sure that you
designate the number of GPUs your container requires in the task definition. As
containers that support GPUs are placed, the Amazon ECS container agent pins the desired
number of physical GPUs to the appropriate container. The number of GPUs reserved for
all containers in a task cannot exceed the number of available GPUs on the container
instance the task is launched on. For more information, see [Creating an Amazon ECS task definition using the console](create-task-definition.md "create-task-definition.md").

###### Important

If your GPU requirements aren't specified in the task definition, the task uses
the default Docker runtime.

The following shows the JSON format for the GPU requirements in a task
definition:

```
{
  "containerDefinitions": [
     {
        ...
        **"resourceRequirements" : [
 {
 "type" : "GPU",
 "value" : "`2`"
 }
 ],**
     },
...
}
```

The following example demonstrates the syntax for a Docker container that specifies a
GPU requirement. This container uses two GPUs, runs the `nvidia-smi` utility,
and then exits.

```
{
  "containerDefinitions": [
    {
      "memory": 80,
      "essential": true,
      "name": "gpu",
      "image": "nvidia/cuda:11.0.3-base",
      "resourceRequirements": [
         {
           "type":"GPU",
           "value": "2"
         }
      ],
      "command": [
        "sh",
        "-c",
        "nvidia-smi"
      ],
      "cpu": 100
    }
  ],
  "family": "example-ecs-gpu"
}
```

The following example task definition shows a TensorFlow container that
prints the number of available GPUs. The task runs on Amazon ECS Managed Instances, requires one
GPU, and uses a `g4dn.xlarge` instance.

```
{
  "family": "tensorflow-gpu",
  "networkMode": "awsvpc",
  "executionRoleArn": "arn:aws:iam::account-id:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "tensorflow",
      "image": "tensorflow/tensorflow:latest-gpu",
      "essential": true,
      "command": [
        "python",
        "-c",
        "import tensorflow as tf; print('Num GPUs Available: ', len(tf.config.list_physical_devices('GPU')))"
      ],
      "resourceRequirements": [
        {
          "type": "GPU",
          "value": "1"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/tensorflow-gpu",
          "awslogs-region": "region",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "requiresCompatibilities": [
    "MANAGED_INSTANCES"
  ],
  "cpu": "4096",
  "memory": "8192",
}
```
