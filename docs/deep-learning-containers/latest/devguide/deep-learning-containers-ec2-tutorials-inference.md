# Inference

This section shows how to run inference on AWS Deep Learning Containers for Amazon Elastic Compute Cloud using PyTorch, and TensorFlow.

###### Contents

- [PyTorch
  Inference](#deep-learning-containers-ec2-tutorials-inference-pytorch "#deep-learning-containers-ec2-tutorials-inference-pytorch")
- [TensorFlow
  Inference](#deep-learning-containers-ec2-tutorials-inference-tf2 "#deep-learning-containers-ec2-tutorials-inference-tf2")

## PyTorch

Inference

Deep Learning Containers with PyTorch version 1.6 and later use TorchServe for inference calls. Deep Learning Containers
with PyTorch version 1.5 and earlier use `multi-model-server` for inference
calls.

### PyTorch 1.6 and later

To run inference with PyTorch, this example uses a model pretrained on Imagenet from a
public S3 bucket. Inference is served using TorchServe. For more information, see
this blog on [Deploying PyTorch inference with TorchServe](https://aws.amazon.com/blogs/machine-learning/serving-pytorch-models-in-production-with-the-amazon-sagemaker-native-torchserve-integration/ "https://aws.amazon.com/blogs/machine-learning/serving-pytorch-models-in-production-with-the-amazon-sagemaker-native-torchserve-integration/").

For CPU instances:

```
`$` docker run -itd --name torchserve -p 80:8080  -p 8081:8081 `<your container image id>` \
torchserve --start --ts-config /home/model-server/config.properties \
--models pytorch-densenet=https://torchserve.s3.amazonaws.com/mar_files/densenet161.mar
```

For GPU instances

```
`$` nvidia-docker run -itd --name torchserve -p 80:8080  -p 8081:8081 `<your container image id>` \
torchserve --start --ts-config /home/model-server/config.properties \
--models pytorch-densenet=https://torchserve.s3.amazonaws.com/mar_files/densenet161.mar
```

If you have docker-ce version 19.03 or later, you can use the `--gpus` flag
when you start Docker.

The configuration file is included in the container.

With your server started, you can now run inference from a different window by using
the following.

```
$ curl -O https://s3.amazonaws.com/model-server/inputs/flower.jpg
curl -X POST http://127.0.0.1:80/predictions/pytorch-densenet -T flower.jpg
```

After you are done using your container, you can remove it using the following.

```
`$` docker rm -f torchserve
```

### PyTorch 1.5 and earlier

To run inference with PyTorch, this example uses a model pretrained on Imagenet
from a public S3 bucket. Inference is served using
multi-model-server, which can support any framework as the backend. For more
information, see [multi-model-server](https://github.com/awslabs/multi-model-server "https://github.com/awslabs/multi-model-server").

For CPU instances:

```
`$` docker run -itd --name mms -p 80:8080  -p 8081:8081 `<your container image id>` \
multi-model-server --start --mms-config /home/model-server/config.properties \
--models densenet=https://dlc-samples.s3.amazonaws.com/pytorch/multi-model-server/densenet/densenet.mar
```

For GPU instances

```
`$` nvidia-docker run -itd --name mms -p 80:8080  -p 8081:8081 `<your container image id>` \
multi-model-server --start --mms-config /home/model-server/config.properties \
--models densenet=https://dlc-samples.s3.amazonaws.com/pytorch/multi-model-server/densenet/densenet.mar
```

If you have docker-ce version 19.03 or later, you can use the `--gpus` flag
when you start Docker.

The configuration file is included in the container.

With your server started, you can now run inference from a different window by using
the following.

```
`$` curl -O https://s3.amazonaws.com/model-server/inputs/flower.jpg
curl -X POST http://127.0.0.1/predictions/densenet -T flower.jpg
```

After you are done using your container, you can remove it using the following.

```
`$` docker rm -f mms
```

## TensorFlow

Inference

To demonstrate how to use Deep Learning Containers for inference, this example uses a simple
_half plus two_ model with TensorFlow 2 Serving. We recommend
using the [Deep
Learning Base AMI](../../../dlami/latest/devguide/overview-base.md "../../../dlami/latest/devguide/overview-base.md") for TensorFlow 2. After you log into your instance run the
following.

```
`$` git clone -b r2.0 https://github.com/tensorflow/serving.git
`$` cd serving
```

Use the commands here to start TensorFlow Serving with the Deep Learning Containers for this model.
Unlike the Deep Learning Containers for training, model serving starts immediately upon running the
container and runs as a background process.

- For CPU instances:

```
`$` docker run -p 8500:8500 -p 8501:8501 --name tensorflow-inference --mount type=bind,source=$(pwd)/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu,target=/models/saved_model_half_plus_two -e MODEL_NAME=saved_model_half_plus_two -d `<cpu inference container>`
```

For example:

```
`$` docker run -p 8500:8500 -p 8501:8501 --name tensorflow-inference --mount type=bind,source=$(pwd)/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu,target=/models/saved_model_half_plus_two -e MODEL_NAME=saved_model_half_plus_two -d 763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-inference:2.0.0-cpu-py36-ubuntu18.04
```

- For GPU instances:

```
`$` nvidia-docker run -p 8500:8500 -p 8501:8501 --name tensorflow-inference --mount type=bind,source=$(pwd)/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_gpu,target=/models/saved_model_half_plus_two -e MODEL_NAME=saved_model_half_plus_two -d `<gpu inference container>`
```

For example:

```
`$` nvidia-docker run -p 8500:8500 -p 8501:8501 --name tensorflow-inference --mount type=bind,source=$(pwd)/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_gpu,target=/models/saved_model_half_plus_two -e MODEL_NAME=saved_model_half_plus_two -d 763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-inference:2.0.0-gpu-py36-cu100-ubuntu18.04
```

###### Note

Loading the GPU model server may take some time.

Next, run inference with the Deep Learning Containers.

```
`$` curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://127.0.0.1:8501/v1/models/saved_model_half_plus_two:predict
```

The output is similar to the following.

```
{
    "predictions": [2.5, 3.0, 4.5
    ]
}
```

###### Note

To debug the container's output, you can use the name to attach to it as shown in the following command:

```
`$` docker attach `<your docker container name>`
```

This example used `tensorflow-inference`.

### Next

steps

To learn about using custom entrypoints with Deep Learning Containers on Amazon ECS, see [Custom Entrypoints](deep-learning-containers-ec2-tutorials-custom-entry.md "deep-learning-containers-ec2-tutorials-custom-entry.md").
