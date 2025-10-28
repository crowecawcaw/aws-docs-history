# Strategies for distributed training

Distributed training is usually split by two approaches: data parallel and model parallel.
_Data parallel_ is the most common approach to distributed
training: You have a lot of data, batch it up, and send blocks of data to multiple CPUs or
GPUs (nodes) to be processed by the neural network or ML algorithm, then combine the results.
The neural network is the same on each node. A _model
parallel_ approach is used with large models that won’t fit in a node’s memory in
one piece; it breaks up the model and places different parts on different nodes. In this
situation, you need to send your batches of data out to each node so that the data is
processed on all parts of the model.

The terms _network_ and _model_ are often used interchangeably: A large model is really a large network
with many layers and parameters. Training with a large network produces a large model, and
loading the model back onto the network with all your pre-trained parameters and their weights
loads a large model into memory. When you break apart a model to split it across nodes, you’re
also breaking apart the underlying network. A network consists of layers, and to split up the
network, you put layers on different compute devices.

A common pitfall of naively splitting layers across devices is severe GPU
under-utilization. Training is inherently sequential in both forward and backward passes, and
at a given time, only one GPU can actively compute, while the others wait on the activations
to be sent. Modern model parallel libraries solve this problem by using pipeline execution
schedules to improve device utilization. However, only the Amazon SageMaker AI's distributed model
parallel library includes automatic model splitting. The two core features of the library,
automatic model splitting and pipeline execution scheduling, simplifies the process of
implementing model parallelism by making automated decisions that lead to efficient device
utilization.

## Train with data parallel and model

parallel

If you are training with a large dataset, start with a data parallel approach. If you
run out of memory during training, you may want to switch to a model parallel approach, or
try hybrid model and data parallelism. You can also try the following to improve performance
with data parallel:

- Change your model’s hyperparameters.
- Reduce the batch size.
- Keep reducing the batch size until it fits. If you reduce batch size to 1, and still
  run out of memory, then you should try model-parallel training.

Try gradient compression (FP16, INT8):

- On NVIDIA TensorCore-equipped hardware, using [mixed precision training](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html "https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html") creates both speed-up and memory consumption
  reduction.
- SageMaker AI's distributed data parallelism library supports Automatic Mixed Precision
  (AMP) out of the box. No extra action is needed to enable AMP other than the
  framework-level modifications to your training script. If gradients are in FP16, the
  SageMaker AI data parallelism library runs its `AllReduce` operation in FP16.
  For more information about implementing AMP APIs to your training script, see the
  following resources:
  - [Frameworks - PyTorch](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#pytorch "https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#pytorch") in the _NVIDIA Deep Learning
    Performance documentation_
  - [Frameworks - TensorFlow](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#tensorflow "https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#tensorflow") in the _NVIDIA Deep
    Learning Performance documentation_
  - [Automatic
    Mixed Precision for Deep Learning](https://developer.nvidia.com/automatic-mixed-precision "https://developer.nvidia.com/automatic-mixed-precision") in the _NVIDIA
    Developer Docs_
  - [Introducing native PyTorch automatic mixed precision for faster training on
    NVIDIA GPUs](https://pytorch.org/blog/accelerating-training-on-nvidia-gpus-with-pytorch-automatic-mixed-precision/ "https://pytorch.org/blog/accelerating-training-on-nvidia-gpus-with-pytorch-automatic-mixed-precision/") in the _PyTorch Blog_
  - [TensorFlow mixed
    precision APIs](https://www.tensorflow.org/guide/mixed_precision "https://www.tensorflow.org/guide/mixed_precision") in the _TensorFlow
    documentation_

Try reducing the input size:

- Reduce the NLP sequence length if you increase the sequence link, need to adjust the
  batch size down, or adjust the GPUs up to spread the batch.
- Reduce image resolution.

Check if you use batch normalization, since this can impact convergence. When you use
distributed training, your batch is split across GPUs and the effect of a much lower batch
size can be a higher error rate thereby disrupting the model from converging. For example,
if you prototyped your network on a single GPU with a batch size of 64, then scaled up to
using four p3dn.24xlarge, you now have 32 GPUs and your per-GPU batch size drops from 64 to 2. This will likely break the convergence you saw with a single node.

Start with model-parallel training when:

- Your model does not fit on a single device.
- Due to your model size, you’re facing limitations in choosing larger batch sizes,
  such as if your model weights take up most of your GPU memory and you are forced to
  choose a smaller, suboptimal batch size.

To learn more about the SageMaker AI distributed libraries, see the following:

- [Run distributed training with the SageMaker AI distributed data
  parallelism library](data-parallel.md "data-parallel.md")
- [(Archived) SageMaker model parallelism library v1.x](model-parallel.md "model-parallel.md")
