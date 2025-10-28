# Get started with distributed training in

Amazon SageMaker AI

The following page gives information about the steps needed to get started with
distributed training in Amazon SageMaker AI. If you’re already familiar with distributed training, choose
one of the following options that matches your preferred strategy or framework to get started.
If you want to learn about distributed training in general, see [Distributed training concepts](distributed-training.md#distributed-training-basic-concepts "distributed-training.md#distributed-training-basic-concepts").

The SageMaker AI distributed training libraries are optimized for the SageMaker training environment,
help adapt your distributed training jobs to SageMaker AI, and improve training speed and throughput.
The libraries offer both data parallel and model parallel training strategies. They combine
software and hardware technologies to improve inter-GPU and inter-node communications, and
extend SageMaker AI’s training capabilities with built-in options that require minimal code changes to
your training scripts. 

## Before you get started

SageMaker Training supports distributed training on a single instance as well as multiple
instances, so you can run any size of training at scale. We recommend you to use the framework
estimator classes such as [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator") and [TensorFlow](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator") in the SageMaker Python SDK, which are the training job launchers with
various distributed training options. When you create an estimator object, the object sets up
distributed training infrastructure, runs the `CreateTrainingJob` API in the
backend, finds the Region where your current session is running, and pulls one of the
pre-built AWS deep learning container prepackaged with a number of libraries including deep
learning frameworks, distributed training frameworks, and the [EFA](../../../AWSEC2/latest/UserGuide/efa.md "../../../AWSEC2/latest/UserGuide/efa.md") driver. If you want to mount an FSx file
system to the training instances, you need to pass your VPC subnet and security group ID to
the estimator. Before running your distributed training job in SageMaker AI, read the following
general guidance on the basic infrastructure setup.

### Availability zones and network backplane

When using multiple instances (also called _nodes_),
it’s important to understand the network that connects the instances, how they read the
training data, and how they share information between themselves. For example, when you run
a distributed data-parallel training job, a number of factors, such as communication between
the nodes of a compute cluster for running the `AllReduce` operation and data
transfer between the nodes and data storage in Amazon Simple Storage Service or Amazon FSx for Lustre, play a crucial
role to achieve an optimal use of compute resources and a faster training speed. To reduce
communication overhead, make sure that you configure instances, VPC subnet, and data storage
in the same AWS Region and Availability Zone.

### GPU instances with faster network and high-throughput

storage

You can technically use any instances for distributed training. For cases where you need
to run multi-node distributed training jobs for training large models, such as large
language models (LLMs) and diffusion models, which require faster inter-node commutation, we
recommend [EFA-enabled GPU instances supported by SageMaker AI](http://aws.amazon.com/about-aws/whats-new/2021/05/amazon-sagemaker-supports-elastic-fabric-adapter-distributed-training/ "http://aws.amazon.com/about-aws/whats-new/2021/05/amazon-sagemaker-supports-elastic-fabric-adapter-distributed-training/"). Especially, to achieve the most
performant distributed training job in SageMaker AI, we recommend [P4d and P4de instances equipped with
NVIDIA A100 GPUs](http://aws.amazon.com/ec2/instance-types/p4/ "http://aws.amazon.com/ec2/instance-types/p4/"). These are also equipped with high-throughput low-latency local
instance storage and faster intra-node network. For data storage, we recommend [Amazon FSx for Lustre](../../../fsx/latest/LustreGuide/what-is.md "../../../fsx/latest/LustreGuide/what-is.md") that provides high throughput for storing training datasets and
model checkpoints.

**Use the SageMaker AI distributed data parallelism (SMDDP)
library**

The SMDDP library improves communication between nodes with implementations of
`AllReduce` and `AllGather` collective communication operations that
are optimized for AWS network infrastructure and Amazon SageMaker AI ML instance topology. You can use
the [SMDDP
library as the backend of PyTorch-based distributed training packages](data-parallel-modify-sdp-pt.md "data-parallel-modify-sdp-pt.md"): [PyTorch distributed data parallel
(DDP)](https://pytorch.org/docs/stable/notes/ddp.html "https://pytorch.org/docs/stable/notes/ddp.html"), [PyTorch fully sharded
data parallelism (FSDP)](https://pytorch.org/docs/stable/fsdp.html "https://pytorch.org/docs/stable/fsdp.html"), [DeepSpeed](https://github.com/microsoft/DeepSpeed "https://github.com/microsoft/DeepSpeed"), and [Megatron-DeepSpeed](https://github.com/microsoft/Megatron-DeepSpeed "https://github.com/microsoft/Megatron-DeepSpeed"). The following code example shows how to set a
`PyTorch` estimator for launching a distributed training job on two
`ml.p4d.24xlarge` instances.

```
from sagemaker.pytorch import PyTorch

estimator = PyTorch(
    ...,
    instance_count=`2`,
    instance_type="`ml.p4d.24xlarge`",
    # Activate distributed training with SMDDP
    distribution={ "pytorchddp": { "enabled": True } }  # mpirun, activates SMDDP AllReduce OR AllGather
    # distribution={ "torch_distributed": { "enabled": True } }  # torchrun, activates SMDDP AllGather
    # distribution={ "smdistributed": { "dataparallel": { "enabled": True } } }  # mpirun, activates SMDDP AllReduce OR AllGather
)
```

To learn how to prepare your training script and launch a distributed data-parallel
training job on SageMaker AI, see [Run distributed training with the SageMaker AI distributed data
parallelism library](data-parallel.md "data-parallel.md").

**Use the SageMaker AI model parallelism library (SMP)**

SageMaker AI provides the SMP library and supports various distributed training techniques,
such as sharded data parallelism, pipelining, tensor parallelism, optimizer state sharding,
and more. To learn more about what the SMP library offers, see [Core Features of the SageMaker Model Parallelism
Library](model-parallel-core-features.md "model-parallel-core-features.md").

To use SageMaker AI's model parallelism library, configure the `distribution` parameter
of the SageMaker AI framework estimators. Supported framework estimators are [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator") and [TensorFlow](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator"). The following code example shows how to construct a framework estimator
for distributed training with the model parallelism library on two
`ml.p4d.24xlarge` instances.

```
from sagemaker.`framework` import `Framework`

distribution={
    "smdistributed": {
        "modelparallel": {
            "enabled":True,
            "parameters": {
                ...   # enter parameter key-value pairs here
            }
        },
    },
    "mpi": {
        "enabled" : True,
        ...           # enter parameter key-value pairs here
    }
}

estimator = `Framework`(
    ...,
    instance_count=`2`,
    instance_type="`ml.p4d.24xlarge`",
    distribution=*distribution*
)
```

To learn how to adapt your training script, configure distribution parameters in the
`estimator` class, and launch a distributed training job, see [SageMaker AI's model parallelism library](model-parallel.md "model-parallel.md") (see also [Distributed Training APIs](https://sagemaker.readthedocs.io/en/stable/api/training/distributed.html#the-sagemaker-distributed-model-parallel-library "https://sagemaker.readthedocs.io/en/stable/api/training/distributed.html#the-sagemaker-distributed-model-parallel-library") in the _SageMaker Python SDK
documentation_).

**Use open source distributed training frameworks**

SageMaker AI also supports the following options to operate `mpirun` and
`torchrun` in the backend.

- To use [PyTorch DistributedDataParallel (DDP)](https://pytorch.org/docs/master/generated/torch.nn.parallel.DistributedDataParallel.html "https://pytorch.org/docs/master/generated/torch.nn.parallel.DistributedDataParallel.html") in SageMaker AI with the `mpirun`
  backend, add `distribution={"pytorchddp": {"enabled": True}}` to your PyTorch
  estimator. For more information, see also [PyTorch Distributed Training](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#distributed-pytorch-training "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#distributed-pytorch-training") and [SageMaker AI PyTorch Estimator](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator")'s `distribution` argument in the
  _SageMaker Python SDK documentation_.

###### Note

This option is available for PyTorch 1.12.0 and later.

```
from sagemaker.pytorch import PyTorch

estimator = PyTorch(
    ...,
    instance_count=`2`,
    instance_type="`ml.p4d.24xlarge`",
    distribution={"pytorchddp": {"enabled": True}}  # runs mpirun in the backend
)
```

- SageMaker AI supports the [PyTorch `torchrun` launcher](https://pytorch.org/docs/stable/elastic/run.html "https://pytorch.org/docs/stable/elastic/run.html") for distributed training on GPU-based
  Amazon EC2 instances, such as P3 and P4, as well as Trn1 powered by the [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/ "https://aws.amazon.com/machine-learning/trainium/") device.

To use [PyTorch DistributedDataParallel (DDP)](https://pytorch.org/docs/master/generated/torch.nn.parallel.DistributedDataParallel.html "https://pytorch.org/docs/master/generated/torch.nn.parallel.DistributedDataParallel.html") in SageMaker AI with the `torchrun`
backend, add `distribution={"torch_distributed": {"enabled": True}}` to the
PyTorch estimator.

###### Note

This option is available for PyTorch 1.13.0 and later.

The following code snippet shows an example of constructing a SageMaker AI PyTorch estimator
to run distributed training on two `ml.p4d.24xlarge` instances with the
`torch_distributed` distribution option.

```
from sagemaker.pytorch import PyTorch

estimator = PyTorch(
    ...,
    instance_count=`2`,
    instance_type="`ml.p4d.24xlarge`",
    distribution={"torch_distributed": {"enabled": True}}   # runs torchrun in the backend
)
```

For more information, see [Distributed PyTorch Training](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#distributed-pytorch-training "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#distributed-pytorch-training") and [SageMaker AI PyTorch Estimator](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator")'s `distribution` argument in the
_SageMaker Python SDK documentation_.

**Notes for distributed training on Trn1**

A Trn1 instance consists of up to 16 Trainium devices, and each Trainium device
consists of two [NeuronCores](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/neuroncores-arch.html#neuroncores-v2-arch "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/neuroncores-arch.html#neuroncores-v2-arch"). For specs of the AWS Trainium devices, see [Trainium Architecture](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/trn1-arch.html#id2 "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/trn1-arch.html#id2") in the _AWS Neuron
Documentation_.

To train on the Trainium-powered instances, you only need to specify the Trn1 instance
code, `ml.trn1.*`, in string to the `instance_type` argument of the
SageMaker AI PyTorch estimator class. To find available Trn1 instance types, see [AWS Trn1 Architecture](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/trn1-arch.html#aws-trn1-arch "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/trn1-arch.html#aws-trn1-arch") in the _AWS Neuron
documentation_.

###### Note

SageMaker Training on Amazon EC2 Trn1 instances is currently available only for the PyTorch
framework in the AWS Deep Learning Containers for PyTorch Neuron starting v1.11.0. To
find a complete list of supported versions of PyTorch Neuron, see [Neuron Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#neuron-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#neuron-containers") in the _AWS Deep Learning Containers
GitHub repository_.

When you launch a training job on Trn1 instances using the SageMaker Python SDK, SageMaker AI
automatically picks up and runs the right container from [Neuron Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#neuron-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#neuron-containers") provided by AWS Deep Learning Containers. The Neuron
Containers are prepackaged with training environment settings and dependencies for easier
adaptation of your training job to the SageMaker Training platform and Amazon EC2 Trn1
instances.

###### Note

To run your PyTorch training job on Trn1 instances with SageMaker AI, you should modify your
training script to initialize process groups with the `xla` backend and use
[PyTorch/XLA](https://pytorch.org/xla/release/1.12/index.html "https://pytorch.org/xla/release/1.12/index.html"). To
support the XLA adoption process, the AWS Neuron SDK provides PyTorch Neuron that uses
XLA to make conversion of PyTorch operations to Trainium instructions. To learn how to
modify your training script, see [Developer Guide for Training with PyTorch Neuron (`torch-neuronx`)](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/frameworks/torch/torch-neuronx/programming-guide/training/pytorch-neuron-programming-guide.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/frameworks/torch/torch-neuronx/programming-guide/training/pytorch-neuron-programming-guide.html")
in the _AWS Neuron Documentation_.

For more information, see [Distributed Training with PyTorch Neuron on Trn1 instances](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#id24 "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#id24") and [SageMaker AI PyTorch Estimator](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator")'s `distribution` argument in the
_SageMaker Python SDK documentation_.

- To use MPI in SageMaker AI, add `distribution={"mpi": {"enabled": True}}` to your
  estimator. The MPI distribution option is available for the following frameworks: MXNet,
  PyTorch, and TensorFlow.
- To use a parameter server in SageMaker AI, add `distribution={"parameter_server":
{"enabled": True}}` to your estimator. The parameter server option is available
  for the following frameworks: MXNet, PyTorch, and TensorFlow.

###### Tip

For more information about using the MPI and parameter server options per framework,
use the following links to the _SageMaker Python SDK
documentation_.

    + [MXNet Distributed Training](https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/using_mxnet.html#distributed-training "https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/using_mxnet.html#distributed-training") and [SageMaker AI MXNet Estimator](https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/sagemaker.mxnet.html#mxnet-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/mxnet/sagemaker.mxnet.html#mxnet-estimator")'s `distribution` argument
    + [PyTorch Distributed Training](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#distributed-pytorch-training "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#distributed-pytorch-training") and [SageMaker AI PyTorch Estimator](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#pytorch-estimator")'s `distribution` argument
    + [TensorFlow Distributed Training](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/using_tf.html#distributed-training "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/using_tf.html#distributed-training") and [SageMaker AI TensorFlow Estimator](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator")'s `distribution`
     argument.
