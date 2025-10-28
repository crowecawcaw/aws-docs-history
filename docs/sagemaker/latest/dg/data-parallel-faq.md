# Amazon SageMaker AI distributed data parallelism library FAQ

Use the following to find answers to commonly asked questions about the SMDDP
library.

**Q: When using the library, how are the
`allreduce`-supporting CPU instances managed? Do I have to create heterogeneous
CPU-GPU clusters, or does the SageMaker AI service create extra C5s for jobs that use the SMDDP
library?**

The SMDDP library only supports GPU instances, more specificcally, P4d and P4de instances
with NVIDIA A100 GPUs and EFA. No additional C5 or CPU instances are launched; if your SageMaker AI
training job is on an 8-node P4d cluster, only 8 `ml.p4d.24xlarge` instances are
used. No additional instances are provisioned.

**Q: I have a training job taking 5 days on a single
`ml.p3.24xlarge` instance with a set of hyperparameters H1 (learning rate, batch
size, optimizer, etc). Is using SageMaker AI's data parallelism library and a five-time bigger cluster
enough to achieve an approximate five-time speedup? Or do I have to revisit its training
hyperparameters after activating the SMDDP library?**

The library changes the overall batch size. The new overall batch size is scaled linearly
with the number of training instances used. As a result of this, hyperparameters, such as
learning rate, have to be changed to ensure convergence.

**Q: Does the SMDDP library support Spot?**

Yes. You can use managed spot training. You specify the path to the checkpoint file in the
SageMaker training job. You save and restore checkpoints in their training script as mentioned in the
last steps of [Use the SMDDP library in your TensorFlow training
script (deprecated)](data-parallel-modify-sdp-tf2.md "data-parallel-modify-sdp-tf2.md") and [Use the SMDDP library in your PyTorch training
script](data-parallel-modify-sdp-pt.md "data-parallel-modify-sdp-pt.md").

**Q: Is the SMDDP library relevant in a single-host, multi-device
setup?**

The library can be used in single-host multi-device training but the library offers
performance improvements only in multi-host training.

**Q: Where should the training dataset be stored?**

The training dataset can be stored in an Amazon S3 bucket or on an Amazon FSx drive. See this [document for various supported input file systems for a training job](https://sagemaker.readthedocs.io/en/stable/api/utility/inputs.html#sagemaker.inputs.FileSystemInput "https://sagemaker.readthedocs.io/en/stable/api/utility/inputs.html#sagemaker.inputs.FileSystemInput").

**Q: When using the SMDDP library, is it mandatory to have training data
in FSx for Lustre? Can Amazon EFS and Amazon S3 be used?**

We generally recommend you use Amazon FSx because of its lower latency and higher throughput. If
you prefer, you can use Amazon EFS or Amazon S3.

**Q: Can the library be used with CPU nodes?**

No. To find instance types supported by the SMDDP library, see [Supported instance
types](distributed-data-parallel-support.md#distributed-data-parallel-supported-instance-types "distributed-data-parallel-support.md#distributed-data-parallel-supported-instance-types").

**Q: What frameworks and framework versions are currently supported by
the SMDDP library at launch?**

the SMDDP library currently supports PyTorch v1.6.0 or later and TensorFlow v2.3.0 or later. It
doesn't support TensorFlow 1.x. For more information about which version of the SMDDP library is
packaged within AWS deep learning containers, see [Release Notes for Deep
Learning Containers](../../../deep-learning-containers/latest/devguide/dlc-release-notes.md "../../../deep-learning-containers/latest/devguide/dlc-release-notes.md").

**Q: Does the library support AMP?**

Yes, the SMDDP library supports Automatic Mixed Precision (AMP) out of the box. No extra
action is needed to use AMP other than the framework-level modifications to your training
script. If gradients are in FP16, the SageMaker AI data parallelism library runs its
`AllReduce` operation in FP16. For more information about implementing AMP APIs to
your training script, see the following resources:

- [Frameworks - PyTorch](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#pytorch "https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#pytorch") in the _NVIDIA Deep Learning
  Performace documentation_
- [Frameworks - TensorFlow](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#tensorflow "https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#tensorflow") in the _NVIDIA Deep Learning
  Performace documentation_
- [Automatic Mixed
  Precision for Deep Learning](https://developer.nvidia.com/automatic-mixed-precision "https://developer.nvidia.com/automatic-mixed-precision") in the _NVIDIA Developer
  Docs_
- [Introducing native PyTorch automatic mixed precision for faster training on NVIDIA
  GPUs](https://pytorch.org/blog/accelerating-training-on-nvidia-gpus-with-pytorch-automatic-mixed-precision/ "https://pytorch.org/blog/accelerating-training-on-nvidia-gpus-with-pytorch-automatic-mixed-precision/") in the _PyTorch Blog_
- [TensorFlow mixed precision
  APIs](https://www.tensorflow.org/guide/mixed_precision "https://www.tensorflow.org/guide/mixed_precision") in the _TensorFlow documentation_
  **Q: How do I identify if my distributed training job is slowed down due
  to I/O bottleneck?**

With a larger cluster, the training job requires more I/O throughput, and therefore the
training throughput might take longer (more epochs) to ramp up to the maximum performance. This
indicates that I/O is being bottlenecked and cache is harder to build up as you scale nodes up
(higher throughput requirement and more complex network topology). For more information about
monitoring the Amazon FSx throughput on CloudWatch, see [Monitoring
FSx for Lustre](../../../fsx/latest/LustreGuide/monitoring_overview.md "../../../fsx/latest/LustreGuide/monitoring_overview.md") in the _FSx for Lustre User Guide_.

**Q: How do I resolve I/O bottlenecks when running a distributed
training job with data parallelism?**

We highly recommend that you use Amazon FSx as your data channel if you are using Amazon S3. If you
are already using Amazon FSx but still having I/O bottleneck problems, you might have set up your
Amazon FSx file system with a low I/O throughput and a small storage capacity. For more information
about how to estimate and choose the right size of I/O throughput capacity, see [Use Amazon FSx and set up an optimal storage and
throughput capacity](data-parallel-config.md#data-parallel-config-fxs "data-parallel-config.md#data-parallel-config-fxs").

**Q: (For the library v1.4.0 or later) How do I resolve the
`Invalid backend` error while initializing process group.**

If you encounter the error message `ValueError: Invalid backend: 'smddp'` when
calling `init_process_group`, this is due to the breaking change in the SMDDP library
v1.4.0 and later. You must import the PyTorch client of the library,
`smdistributed.dataparallel.torch.torch_smddp`, which registers `smddp`
as a backend for PyTorch. To learn more, see [Use the SMDDP library in your PyTorch training
script](data-parallel-modify-sdp-pt.md "data-parallel-modify-sdp-pt.md").

**Q: (For the SMDDP library v1.4.0 or later) I would like to call the
collective primitives of the [`torch.distributed`](https://pytorch.org/docs/stable/distributed.html "https://pytorch.org/docs/stable/distributed.html") interface. Which primitives does the
`smddp` backend support?**

In v1.4.0, the SMDDP library supports `all_reduce`, `broadcast`,
`reduce`, `all_gather`, and `barrier` of of the
`torch.distributed` interface.

**Q: (For the SMDDP library v1.4.0 or later) Does this new API work with
other custom DDP classes or libraries like Apex DDP?**

The SMDDP library is tested with other third-party distributed data parallel libraries and
framework implementations that use the `torch.distribtued` modules. Using the SMDDP
library with custom DDP classes works as long as the collective operations used by the custom
DDP classes are supported by the SMDDP library. See the preceding question for a list of
supported collectives. If you have these use cases and need further support, reach out to the
SageMaker AI team through the [AWS Support Center](https://console.aws.amazon.com/support/ "https://console.aws.amazon.com/support/") or
[AWS Developer Forums for
Amazon SageMaker AI](https://forums.aws.amazon.com/forum.jspa?forumID=285 "https://forums.aws.amazon.com/forum.jspa?forumID=285").

**Q: Does the SMDDP library support the bring-your-own-container (BYOC)
option? If so, how do I install the library and run a distributed training job by writing a
custom Dockerfile?**

If you want to integrate the SMDDP library and its minimum dependencies into your own Docker
container, BYOC is the right approach. You can build your own container using the binary file of
the library. The recommended process is to write a custom Dockerfile with the library and its
dependencies, build the Docker container, host it in Amazon ECR, and use the ECR image URI to launch
a training job using the SageMaker AI generic estimator class. For more instructions on how to prepare a
custom Dockerfile for distributed training in SageMaker AI with the SMDDP library, see [Create your own Docker container with
the SageMaker AI distributed data parallel library](data-parallel-bring-your-own-container.md "data-parallel-bring-your-own-container.md").
