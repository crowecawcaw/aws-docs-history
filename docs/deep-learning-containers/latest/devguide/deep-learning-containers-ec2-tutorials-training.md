# Training

This section shows how to run training on AWS Deep Learning Containers for Amazon EC2 using PyTorch and TensorFlow.

###### Contents

- [PyTorch
  training](#deep-learning-containers-ec2-tutorials-training-pytorch "#deep-learning-containers-ec2-tutorials-training-pytorch")
- [TensorFlow
  training](#deep-learning-containers-ec2-tutorials-training-tf "#deep-learning-containers-ec2-tutorials-training-tf")
- [Next
  steps](#deep-learning-containers-ec2-training-pytorch-next "#deep-learning-containers-ec2-training-pytorch-next")

## PyTorch

training

To begin training with PyTorch from your Amazon EC2 instance, use the following commands to
run the container. You must use `nvidia-docker` for GPU images.

- For CPU

```
`$` docker run -it `<CPU training container>`
```

- For GPU

```
`$` nvidia-docker run -it `<GPU training container>`
```

- If you have docker-ce version 19.03 or later, you can use the --gpus flag with
  docker:

```
`$` docker run -it --gpus `<GPU training container>`
```

Run the following to begin training.

- For CPU

```
`$` git clone https://github.com/pytorch/examples.git
`$` python examples/mnist/main.py --no-cuda
```

- For GPU

```
`$` git clone https://github.com/pytorch/examples.git
`$` python examples/mnist/main.py
```

### PyTorch distributed GPU training

with NVIDIA Apex

NVIDIA Apex is a PyTorch extension with utilities for mixed precision and
distributed training. For more information on the utilities offered with Apex, see
the [NVIDIA Apex website](https://nvidia.github.io/apex/ "https://nvidia.github.io/apex/"). Apex is
currently supported by Amazon EC2 instances in the following families:

- [Amazon EC2 P3 Instances](https://aws.amazon.com/ec2/instance-types/p3/ "https://aws.amazon.com/ec2/instance-types/p3/")
- [Amazon EC2 P4 Instances](https://aws.amazon.com/ec2/instance-types/p4/ "https://aws.amazon.com/ec2/instance-types/p4/")
- [Amazon EC2 P5 Instances](https://aws.amazon.com/ec2/instance-types/p5/ "https://aws.amazon.com/ec2/instance-types/p5/")
- [Amazon EC2 G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/ "https://aws.amazon.com/ec2/instance-types/g5/")

To begin distributed training using NVIDIA Apex, run the following in the terminal
of the GPU training container. This example requires at least two GPUs on your Amazon EC2
instance to run parallel distributed training.

```
`$` git clone https://github.com/NVIDIA/apex.git && cd apex
`$` python -m torch.distributed.launch --nproc_per_node=2 examples/simple/distributed/distributed_data_parallel.py
```

## TensorFlow

training

After you log into your Amazon EC2 instance, you can run TensorFlow and TensorFlow 2
containers with the following commands. You must use `nvidia-docker` for GPU
images.

- For CPU-based training, run the following.

```
`$` docker run -it `<CPU training container>`
```

- For GPU-based training, run the following.

```
`$` nvidia-docker run -it `<GPU training container>`
```

The previous command runs the container in interactive mode and provides a shell
prompt inside the container. You can then run the following to import TensorFlow.

```
`$` `python`
```

```
`>> import tensorflow`
```

Press Ctrl+D to return to the bash prompt. Run the following to begin training:

```
`git clone https://github.com/fchollet/keras.git`
```

```
`$` `cd keras`
```

```
`$` `python examples/mnist_cnn.py`
```

## Next

steps

To learn inference on Amazon EC2 using PyTorch with Deep Learning Containers, see [PyTorch
Inference](deep-learning-containers-ec2-tutorials-inference.md#deep-learning-containers-ec2-tutorials-inference-pytorch "deep-learning-containers-ec2-tutorials-inference.md#deep-learning-containers-ec2-tutorials-inference-pytorch") .
