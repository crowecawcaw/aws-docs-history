# Pipelining a Model

One of the core features of SageMaker's model parallelism library is _pipeline parallelism_, which determines the order in which
computations are made and data is processed across devices during model training.
Pipelining is a technique to achieve true parallelization in model parallelism, by
having the GPUs compute simultaneously on different data samples, and to overcome the
performance loss due to sequential computation. When you use pipeline parallelism,
training job is executed in a pipelined fashion over microbatches to maximize GPU
usage.

###### Note

Pipeline parallelism, also called model partitioning, is available for both
PyTorch and TensorFlow. For supported versions of the frameworks, see [Supported Frameworks and
AWS Regions](distributed-model-parallel-support.md "distributed-model-parallel-support.md").

## Pipeline Execution

Schedule

Pipelining is based on splitting a mini-batch into microbatches, which are fed
into the training pipeline one-by-one and follow an execution schedule defined by
the library runtime. A _microbatch_ is a smaller
subset of a given training mini-batch. The pipeline schedule determines which
microbatch is executed by which device for every time slot.

For example, depending on the pipeline schedule and the model partition, GPU
`i` might perform (forward or backward) computation on microbatch
`b` while GPU `i+1` performs computation on microbatch
`b+1`, thereby keeping both GPUs active at the same time. During a
single forward or backward pass, execution flow for a single microbatch might visit
the same device multiple times, depending on the partitioning decision. For
instance, an operation that is at the beginning of the model might be placed on the
same device as an operation at the end of the model, while the operations in between
are on different devices, which means this device is visited twice.

The library offers two different pipeline schedules, _simple_ and _interleaved_, which can
be configured using the `pipeline` parameter in the SageMaker Python SDK. In
most cases, interleaved pipeline can achieve better performance by utilizing the
GPUs more efficiently.

### Interleaved

Pipeline

In an interleaved pipeline, backward execution of the microbatches is
prioritized whenever possible. This allows quicker release of the memory used
for activations, using memory more efficiently. It also allows for scaling the
number of microbatches higher, reducing the idle time of the GPUs. At
steady-state, each device alternates between running forward and backward
passes. This means that the backward pass of one microbatch may run before the
forward pass of another microbatch finishes.

![Example execution schedule for the interleaved pipeline over 2 GPUs.](images/distributed/model-parallel/interleaved-pipeline-execution.png)

The preceding figure illustrates an example execution schedule for the
interleaved pipeline over 2 GPUs. In the figure, F0 represents the forward pass
for microbatch 0, and B1 represents the backward pass for microbatch 1.
**Update** represents the optimizer update of the
parameters. GPU0 always prioritizes backward passes whenever possible (for
instance, executes B0 before F2), which allows for clearing of the memory used
for activations earlier.

### Simple

Pipeline

A simple pipeline, by contrast, finishes running the forward pass for each
microbatch before starting the backward pass. This means that it only pipelines
the forward pass and backward pass stages within themselves. The following
figure illustrates an example of how this works, over 2 GPUs.

![Example on a pipeline running the forward pass for each microbatch before starting the backward pass.](images/distributed/model-parallel/simple-pipeline-execution.png)

### Pipelining Execution in Specific

Frameworks

Use the following sections to learn about the framework-specific pipeline
scheduling decisions SageMaker's model parallelism library makes for TensorFlow and
PyTorch.

#### Pipeline

Execution with TensorFlow

The following image is an example of a TensorFlow graph partitioned by the
model parallelism library, using automated model splitting. When a graph is
split, each resulting subgraph is replicated B times (except for the
variables), where B is the number of microbatches. In this figure, each
subgraph is replicated 2 times (B=2). An `SMPInput` operation is
inserted at each input of a subgraph, and an `SMPOutput`
operation is inserted at each output. These operations communicate with the
library backend to transfer tensors to and from each other.

![Example of a TensorFlow graph partitioned by the model parallelism library, using automated model splitting.](images/distributed/model-parallel/interleaved-pipeline-tf.png)

The following image is an example of 2 subgraphs split with B=2 with
gradient operations added. The gradient of a `SMPInput` op is a
`SMPOutput` op, and vice versa. This enables the gradients to
flow backwards during back-propagation.

![Example of 2 subgraphs split with B=2 with gradient operations added.](images/distributed/model-parallel/interleaved-pipeline-tf.gif)

This GIF demonstrates an example interleaved pipeline execution schedule
with B=2 microbatches and 2 subgraphs. Each device sequentially executes one
of the subgraph replicas to improve GPU utilization. As B grows larger, the
fraction of idle time slots goes to zero. Whenever it is time to do (forward
or backward) computation on a specific subgraph replica, the pipeline layer
signals to the corresponding blue `SMPInput` operations to start
executing.

Once the gradients from all microbatches in a single mini-batch are
computed, the library combines the gradients across microbatches, which can
then be applied to the parameters.

#### Pipeline

Execution with PyTorch

Conceptually, pipelining follows a similar idea in PyTorch. However, since
PyTorch does not involve static graphs and so the model parallelism
library's PyTorch feature uses a more dynamic pipelining paradigm.

As in TensorFlow, each batch is split into a number of microbatches, which are
executed one at a time on each device. However, the execution schedule is
handled via execution servers launched on each device. Whenever the output
of a submodule that is placed on another device is needed on the current
device, an execution request is sent to the execution server of the remote
device along with the input tensors to the submodule. The server then
executes this module with the given inputs and returns the response to the
current device.

Since the current device is idle during the remote submodule execution,
the local execution for the current microbatch pauses, and the library
runtime switches execution to another microbatch which the current device
can actively work on. The prioritization of microbatches is determined by
the chosen pipeline schedule. For an interleaved pipeline schedule,
microbatches that are in the backward stage of the computation are
prioritized whenever possible.
