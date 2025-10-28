# Training

###### Note

This section shows how to run training on AWS Deep Learning Containers for Amazon Elastic Container Service using PyTorch and TensorFlow.

###### Important

If your account has already created the Amazon ECS service-linked role, that role is used by
default for your service unless you specify a role here. The service-linked role is
required if your task definition uses the **awsvpc** network mode or if
the service is configured to use service discovery. The role is also required if the
service uses an external deployment controller, multiple target groups, or Elastic
Inference accelerators in which case you should not specify a role here. For more
information, see [Using Service-Linked Roles for Amazon ECS](../../../AmazonECS/latest/developerguide/using-service-linked-roles.md "../../../AmazonECS/latest/developerguide/using-service-linked-roles.md") in the _Amazon ECS Developer
Guide_.

###### Contents

- [PyTorch training](#deep-learning-containers-ecs-tutorials-training-pytorch "#deep-learning-containers-ecs-tutorials-training-pytorch")
- [Next steps](#deep-learning-containers-ecs-training-pytorch-next "#deep-learning-containers-ecs-training-pytorch-next")
- [TensorFlow
  training](#deep-learning-containers-ecs-tutorials-training-tf "#deep-learning-containers-ecs-tutorials-training-tf")
- [Next steps](#deep-learning-containers-ecs-training-tf-next "#deep-learning-containers-ecs-training-tf-next")

## PyTorch training

Before you can run a task on your Amazon ECS cluster, you must register a task
definition. Task definitions are lists of containers grouped together. The following
example uses a sample Docker image that adds training scripts to Deep Learning Containers.

1. Create a file named
   `ecs-deep-learning-container-training-taskdef.json`
   with the following contents.
   - For CPU

   ```
   {
      "requiresCompatibilities":[
         "EC2"
      ],
      "containerDefinitions":[
         {
            "command":[
               "git clone https://github.com/pytorch/examples.git && python examples/mnist/main.py --no-cuda"
            ],
            "entryPoint":[
               "sh",
               "-c"
            ],
            "name":"`pytorch-training-container`",
            "image":"`763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:1.5.1-cpu-py36-ubuntu16.04`",
            "memory":`4000`,
            "cpu":`256`,
            "essential":true,
            "portMappings":[
               {
                  "containerPort":80,
                  "protocol":"tcp"
               }
            ],
            "logConfiguration":{
               "logDriver":"awslogs",
               "options":{
                  "awslogs-group":"/ecs/pytorch-training-cpu",
                  "awslogs-region":"`us-east-1`",
                  "awslogs-stream-prefix":"`mnist`",
                  "awslogs-create-group":"true"
               }
            }
         }
      ],
      "volumes":[

      ],
      "networkMode":"bridge",
      "placementConstraints":[

      ],
      "family":"`pytorch`"
   }
   ```

   - For GPU

   ```
   {
         "requiresCompatibilities": [
           "EC2"
         ],
         "containerDefinitions": [
           {
       "command": [
                   "git clone https://github.com/pytorch/examples.git && python examples/mnist/main.py"
                ],
                "entryPoint": [
                   "sh",
                   "-c"
                ],
             "name": "`pytorch-training-container`",
             "image": "`763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:1.5.1-gpu-py36-cu101-ubuntu16.04`",
             "memory": `6111`,
             "cpu": `256`,
             "resourceRequirements" : [{
               "type" : "GPU",
               "value" : "1"
             }],
             "essential": true,
             "portMappings": [
               {
                 "containerPort": 80,
                 "protocol": "tcp"
               }
             ],
             "logConfiguration": {
                 "logDriver": "awslogs",
                 "options": {
                     "awslogs-group": "/ecs/pytorch-training-gpu",
                     "awslogs-region": "`us-east-1`",
                     "awslogs-stream-prefix": "`mnist`",
                         "awslogs-create-group": "true"
                 }
             }
           }
         ],
         "volumes": [],
         "networkMode": "bridge",
         "placementConstraints": [],
         "family": "`pytorch-training`"
       }
   ```

2. Register the task definition. Note the revision number in the output
   and use it in the next step.

```
`aws ecs register-task-definition --cli-input-json file://`ecs-deep-learning-container-training-taskdef.json``
```

3. Create a task using the task definition. You need the revision
   identifier from the previous step.

```
`aws ecs run-task --cluster `ecs-ec2-training-inference` --task-definition `pytorch`:`1``
```

4. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
5. Select the `ecs-ec2-training-inference` cluster.
6. On the **Cluster** page, choose
   **Tasks**.
7. After your task is in a `RUNNING` state, choose the task
   identifier.
8. Under **Logs**, choose **View logs in
   CloudWatch**. This takes you to the CloudWatch console to view the training
   progress logs.

## Next steps

To learn inference on Amazon ECS using PyTorch with Deep Learning Containers, see [PyTorch inference](deep-learning-containers-ecs-tutorials-inference.md#deep-learning-containers-ecs-tutorials-inference-pytorch "deep-learning-containers-ecs-tutorials-inference.md#deep-learning-containers-ecs-tutorials-inference-pytorch").

## TensorFlow

training

Before you can run a task on your ECS cluster, you must register a task
definition. Task definitions are lists of containers grouped together. The following
example uses a sample Docker image that adds training scripts to Deep Learning Containers. You can use
this script with either TensorFlow or TensorFlow 2. To use it with TensorFlow 2, change
the Docker image to a TensorFlow 2 image.

1. Create a file named
   `ecs-deep-learning-container-training-taskdef.json`
   with the following contents.
   - For CPU

   ```
   {
           "requiresCompatibilities": [
               "EC2"
           ],
           "containerDefinitions": [{
               "command": [
                   "mkdir -p /test && cd /test && git clone https://github.com/fchollet/keras.git && chmod +x -R /test/ && python keras/examples/mnist_cnn.py"
               ],
               "entryPoint": [
                   "sh",
                   "-c"
               ],
               "name": "`tensorflow-training-container`",
               "image": "`763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-inference:1.15.2-cpu-py36-ubuntu18.04`",
               "memory": `4000`,
               "cpu": `256`,
               "essential": true,
               "portMappings": [{
                   "containerPort": 80,
                   "protocol": "tcp"
               }],
               "logConfiguration": {
                   "logDriver": "awslogs",
                   "options": {
                       "awslogs-group": "awslogs-tf-ecs",
                       "awslogs-region": "`us-east-1`",
                       "awslogs-stream-prefix": "`tf`",
                       "awslogs-create-group": "true"
                   }
               }
           }],
           "volumes": [],
           "networkMode": "bridge",
           "placementConstraints": [],
           "family": "`TensorFlow`"
       }
   ```

   - For GPU

   ```
   {
             "requiresCompatibilities": [
               "EC2"
             ],
             "containerDefinitions": [
               {
           "command": [
                       "mkdir -p /test && cd /test && git clone https://github.com/fchollet/keras.git && chmod +x -R /test/ && python keras/examples/mnist_cnn.py"
                    ],
                    "entryPoint": [
                       "sh",
                       "-c"
                    ],
                 "name": "`tensorflow-training-container`",
                 "image": "`763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:1.15.2-gpu-py37-cu100-ubuntu18.04`",
                 "memory": `6111`,
                 "cpu": `256`,
                 "resourceRequirements" : [{
                   "type" : "GPU",
                   "value" : "`1`"
                 }],
                 "essential": true,
                 "portMappings": [
                   {
                     "containerPort": 80,
                     "protocol": "tcp"
                   }
                 ],
                 "logConfiguration": {
                     "logDriver": "awslogs",
                     "options": {
                         "awslogs-group": "awslogs-tf-ecs",
                         "awslogs-region": "`us-east-1`",
                         "awslogs-stream-prefix": "`tf`",
                             "awslogs-create-group": "true"
                     }
                 }
               }
             ],
             "volumes": [],
             "networkMode": "bridge",
             "placementConstraints": [],
             "family": "`tensorflow-training`"
           }
   ```

2. Register the task definition. Note the revision number in the output
   and use it in the next step.

```
`aws ecs register-task-definition --cli-input-json file://`ecs-deep-learning-container-training-taskdef.json``
```

3. Create a task using the task definition. You need the revision number
   from the previous step and the name of the cluster you created during
   setup

```
`aws ecs run-task --cluster `ecs-ec2-training-inference` --task-definition `tf`:`1``
```

4. Open the Amazon ECS classic console at
   [https://console.aws.amazon.com/ecs/](https://console.aws.amazon.com/ecs/ "https://console.aws.amazon.com/ecs/").
5. Select the `ecs-ec2-training-inference` cluster.
6. On the **Cluster** page, choose
   **Tasks**.
7. After your task is in a `RUNNING` state, choose the task
   identifier.
8. Under **Logs**, choose **View logs in
   CloudWatch**. This takes you to the CloudWatch console to view the
   training progress logs.

## Next steps

To learn inference on Amazon ECS using TensorFlow with Deep Learning Containers, see [TensorFlow
inference](deep-learning-containers-ecs-tutorials-inference.md#deep-learning-containers-ecs-tutorials-inference-tf "deep-learning-containers-ecs-tutorials-inference.md#deep-learning-containers-ecs-tutorials-inference-tf").
