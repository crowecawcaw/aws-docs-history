# Inference

This section shows how to run inference on AWS Deep Learning Containers for Amazon Elastic Container Service (Amazon ECS) using PyTorch, and TensorFlow.

###### Important

If your account has already created the Amazon ECS service-linked role, then that role is used by
default for your service unless you specify a role here. The service-linked role is
required if your task definition uses the **awsvpc** network mode. The
role is also required if the service is configured to use service discovery, an external
deployment controller, multiple target groups, or Elastic Inference accelerators in
which case you should not specify a role here. For more information, see [Using Service-Linked Roles for Amazon ECS](../../../AmazonECS/latest/developerguide/using-service-linked-roles.md "../../../AmazonECS/latest/developerguide/using-service-linked-roles.md") in the _Amazon ECS Developer
Guide_.

###### Contents

- [PyTorch inference](#deep-learning-containers-ecs-tutorials-inference-pytorch "#deep-learning-containers-ecs-tutorials-inference-pytorch")
- [TensorFlow
  inference](#deep-learning-containers-ecs-tutorials-inference-tf "#deep-learning-containers-ecs-tutorials-inference-tf")

## PyTorch inference

Before you can run a task on your Amazon ECS cluster, you must register a task
definition. Task definitions are lists of containers grouped together. The following
examples use a sample Docker image that adds either CPU or GPU inference scripts to
Deep Learning Containers.

### Next steps

To learn about using Custom Entrypoints with Deep Learning Containers on Amazon ECS, see [Custom
entrypoints](deep-learning-containers-ecs-tutorials-custom-entry.md "deep-learning-containers-ecs-tutorials-custom-entry.md").

## TensorFlow

inference

The following examples use a sample Docker image that adds either CPU or GPU
inference scripts to Deep Learning Containers from your host machine's command line.

### CPU-based inference

Use the following example to run CPU-based inference.

1. Create a file named
   `ecs-dlc-cpu-inference-taskdef.json` with the
   following contents. You can use this with either TensorFlow or TensorFlow 2.
   To use it with TensorFlow 2, change the Docker image to a TensorFlow 2 image
   and clone the r2.0 serving repository branch instead of r1.15.

```
{
	"requiresCompatibilities": [
		"EC2"
	],
	"containerDefinitions": [{
		"command": [
			"mkdir -p /test && cd /test && git clone -b r1.15 https://github.com/tensorflow/serving.git && tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=saved_model_half_plus_two --model_base_path=/test/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu"
		],
		"entryPoint": [
			"sh",
			"-c"
		],
		"name": "`tensorflow-inference-container`",
		"image": "`763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-inference:1.15.0-cpu-py36-ubuntu18.04`",
		"memory": `8111`,
		"cpu": `256`,
		"essential": true,
		"portMappings": [{
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
				"containerPort": 80,
				"protocol": "tcp"
			}
		],
		"logConfiguration": {
			"logDriver": "awslogs",
			"options": {
				"awslogs-group": "/ecs/tensorflow-inference-gpu",
				"awslogs-region": "`us-east-1`",
				"awslogs-stream-prefix": "`half-plus-two`",
				"awslogs-create-group": "true"
			}
		}
	}],
	"volumes": [],
	"networkMode": "bridge",
	"placementConstraints": [],
	"family": "`tensorflow-inference`"
}
```

2. Register the task definition. Note the revision number in the
   output and use it in the next step.

```
`aws ecs register-task-definition --cli-input-json file://`ecs-dlc-cpu-inference-taskdef.json``
```

3. Create an Amazon ECS service. When you specify the task definition,
   replace `revision_id` with the revision number of the task
   definition from the output of the previous step.

```
`aws ecs create-service --cluster `ecs-ec2-training-inference` \
 --service-name `cli-ec2-inference-cpu` \
 --task-definition `Ec2TFInference:revision_id` \
 --desired-count `1` \
 --launch-type `EC2` \
 --scheduling-strategy="`REPLICA`" \
 --region `us-east-1``
```

4. Verify the service and get the network endpoint by completing the
   following steps.
   1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
   2. Select the `ecs-ec2-training-inference` cluster.
   3. On the **Cluster** page, choose
      **Services** and then
      **cli-ec2-inference-cpu**.
   4. After
      your task is in a
      `RUNNING` state, choose the task
      identifier.
   5. Under **Logs**, choose **View logs in
      CloudWatch**. This takes you to the CloudWatch console to
      view the training progress logs.
   6. Under **Containers**, expand the container
      details.
   7. Under **Name** and then **Network
      Bindings**, under **External Link**
      note the IP address for port
      8501
      and use it in the next
      step.

5. To run inference, use the following command. Replace the external
   IP address with the external link IP address from the previous step.

```
`curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://`<External ip>`:8501/v1/models/saved_model_half_plus_two:predict`
```

The following is sample output.

```
{
    "predictions": [2.5, 3.0, 4.5
    ]
}
```

###### Important

If you are unable to connect to the external IP address, be sure that
your corporate firewall is not blocking non-standards ports, like 8501.
You can try switching to a guest network to verify.

### GPU-based inference

Use the following example to run GPU-based inference.

1. Create a file named
   `ecs-dlc-gpu-inference-taskdef.json` with the
   following contents. You can use this with either TensorFlow or TensorFlow 2.
   To use it with TensorFlow 2, change the Docker image to a TensorFlow 2 image
   and clone the r2.0 serving repository branch instead of r1.15.

```
{
	"requiresCompatibilities": [
		"EC2"
	],
	"containerDefinitions": [{
		"command": [
			"mkdir -p /test && cd /test && git clone -b r1.15 https://github.com/tensorflow/serving.git && tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=saved_model_half_plus_two --model_base_path=/test/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_gpu"
		],
		"entryPoint": [
			"sh",
			"-c"
		],
		"name": "`tensorflow-inference-container`",
		"image": "`763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-inference:1.15.0-gpu-py36-cu100-ubuntu18.04`",
		"memory": `8111`,
		"cpu": `256`,
		"resourceRequirements": [{
			"type": "GPU",
			"value": "1"
		}],
		"essential": true,
		"portMappings": [{
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
				"containerPort": 80,
				"protocol": "tcp"
			}
		],
		"logConfiguration": {
			"logDriver": "awslogs",
			"options": {
				"awslogs-group": "/ecs/TFInference",
				"awslogs-region": "`us-east-1`",
				"awslogs-stream-prefix": "`ecs`",
				"awslogs-create-group": "true"
			}
		}
	}],
	"volumes": [],
	"networkMode": "bridge",
	"placementConstraints": [],
	"family": "`TensorFlowInference`"
}
```

2. Register the task definition. Note the revision number in the
   output and use it in the next step.

```
`aws ecs register-task-definition --cli-input-json file://`ecs-dlc-gpu-inference-taskdef.json``
```

3. Create an Amazon ECS service. When you specify the task definition,
   replace `revision_id` with the revision number of the task
   definition from the output of the previous step.

```
`aws ecs create-service --cluster `ecs-ec2-training-inference` \
 --service-name `cli-ec2-inference-gpu` \
 --task-definition `Ec2TFInference:revision_id` \
 --desired-count `1` \
 --launch-type `EC2` \
 --scheduling-strategy="`REPLICA`" \
 --region `us-east-1``
```

4. Verify the service and get the network endpoint by completing the
   following steps.
   1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
   2. Select the `ecs-ec2-training-inference` cluster.
   3. On the **Cluster** page, choose
      **Services** and then
      **cli-ec2-inference-cpu**.
   4. After your task is in a `RUNNING` state, choose the
      task identifier.
   5. Under **Logs**, choose **View logs in
      CloudWatch**. This takes you to the CloudWatch console to
      view the training progress logs.
   6. Under **Containers**, expand the container
      details.
   7. Under **Name** and then **Network
      Bindings**, under **External Link**
      note the IP address for port 8501 and use it in the next
      step.

5. To run inference, use the following command. Replace the external
   IP address with the external link IP address from the previous step.

```
`curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://`<External ip>`:8501/v1/models/saved_model_half_plus_two:predict`
```

The following is sample output.

```
{
    "predictions": [2.5, 3.0, 4.5
    ]
}
```

###### Important

If you are unable to connect to the external IP address, be sure that
your corporate firewall is not blocking non-standards ports, like 8501.
You can try switching to a guest network to verify.
