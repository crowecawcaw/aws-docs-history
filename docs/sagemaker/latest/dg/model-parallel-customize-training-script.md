# Step 1: Modify Your Own Training

Script Using SageMaker's Distributed Model Parallel Library

Use this section to learn how to customize your training script to use the core features
of the Amazon SageMaker AI model parallelism library. To use the library-specific API functions and
parameters, we recommend you use this documentation alongside the [SageMaker model parallel library APIs](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html") in the _SageMaker Python SDK
documentation_.

The training script examples provided in these sections are simplified and designed to
highlight the required changes you must make to use the library. For end-to-end, runnable
notebook examples that demonstrate how to use a TensorFlow or PyTorch training script with the
SageMaker model parallelism library, see [Amazon SageMaker AI model parallelism library
v2 examples](distributed-model-parallel-v2-examples.md "distributed-model-parallel-v2-examples.md").

###### Topics

- [Split the model of your
  training script using the SageMaker model parallelism library](#model-parallel-model-splitting-using-smp-lib "#model-parallel-model-splitting-using-smp-lib")
- [Modify a TensorFlow training
  script](model-parallel-customize-training-script-tf.md "model-parallel-customize-training-script-tf.md")
- [Modify a PyTorch Training
  Script](model-parallel-customize-training-script-pt.md "model-parallel-customize-training-script-pt.md")

## Split the model of your

training script using the SageMaker model parallelism library

There are two ways to modify your training script to set up model splitting: automated
splitting or manual splitting.

### Automated model splitting

When you use SageMaker's model parallelism library, you can take advantage of _automated model splitting_, also referred to as _automated model partitioning_. The library uses a
partitioning algorithm that balances memory, minimizes communication between devices,
and optimizes performance. You can configure the automated partitioning algorithm to
optimize for speed or memory.

Alternatively, you can use manual model splitting. We recommend automated model
splitting, unless you are very familiar with the model architecture and have a good
idea of how to efficiently partition your model.

#### How it works

Auto-partitioning occurs during the first training step, when the
`smp.step`-decorated function is first called. During this call,
the library first constructs a version of the model on the CPU RAM (to avoid GPU
memory limitations), and then analyzes the model graph and makes a partitioning
decision. Based on this decision, each model partition is loaded on a GPU, and
only then the first step is executed. Because of these analysis and partitioning
steps, the first training step might take longer.

In either framework, the library manages the communication between devices
through its own backend, which is optimized for AWS infrastructure.

The auto-partition design adapts to the characteristics of the framework, and
the library does the partitioning at the granularity level that is more natural
in each framework. For instance, in TensorFlow, each specific operation can be
assigned to a different device, whereas in PyTorch, the assignment is done at
the module level, where each module consists of multiple operations. The follow
section reviews the specifics of the design in each framework.

During the first training step, the model parallelism library internally
runs a tracing step that is meant to construct the model graph and determine
the tensor and parameter shapes. After this tracing step, the library
constructs a tree, which consists of the nested `nn.Module`
objects in the model, as well as additional data gathered from tracing, such
as the amount of stored `nn.Parameters`, and execution time for
each `nn.Module`.

Next, the library traverses this tree from the root and runs a
partitioning algorithm that assigns each `nn.Module` to a
device, which balances computational load (measured by module execution
time) and memory use (measured by the total stored
`nn.Parameter` size and activations). If multiple
`nn.Modules` share the same `nn.Parameter`,
then these modules are placed on the same device to avoid maintaining
multiple versions of the same parameter. Once the partitioning decision
is made, the assigned modules and weights are loaded to their
devices.

For instructions on how to register the `smp.step`
decorator to your PyTorch training script, see [Automated splitting
with PyTorch](model-parallel-customize-training-script-pt.md#model-parallel-customize-training-script-pt-16 "model-parallel-customize-training-script-pt.md#model-parallel-customize-training-script-pt-16").

The model parallelism library analyzes the sizes of the trainable
variables and the graph structure, and internally uses a graph partitioning
algorithm. This algorithm comes up with a device assignment for each
operation, with the objective of minimizing the amount of communication
needed across devices, subject to two constraints:

- Balancing the number of variables stored in each device
- Balancing the number of operations executed in each
  device
  If you specify `speed` for `optimize` (in the model
  parallelism parameters in the Python SDK), the library tries to balance the
  number of operations and `tf.Variable` objects in each device.
  Otherwise, it tries to balance the total size of
  `tf.Variables`.

Once the partitioning decision is made, the library creates a
serialized representation of the subgraph that each device needs to
execute and imports them onto each device. While partitioning, the
library places operations that consume the same `tf.Variable`
and operations that are part of the same Keras layer onto the same
device. It also respects the colocation constraints imposed by
TensorFlow. This means that, for example, if there are two Keras layers
that share a `tf.Variable`, then all operations that are part
of these layers are placed on a single device.

For instructions on how to register the `smp.step`
decorator to your PyTorch training script, see [Automated splitting
with TensorFlow](model-parallel-customize-training-script-tf.md#model-parallel-customize-training-script-tf-23 "model-parallel-customize-training-script-tf.md#model-parallel-customize-training-script-tf-23").

##### Comparison of automated model splitting

between frameworks

In TensorFlow, the fundamental unit of computation is a `tf.Operation`,
and TensorFlow represents the model as a directed acyclic graph (DAG) of
`tf.Operation`s, and therefore the model parallelism library
partitions this DAG so that each node goes to one device. Crucially,
`tf.Operation` objects are sufficiently rich with customizable
attributes, and they are universal in the sense that every model is guaranteed
to consist of a graph of such objects.

PyTorch on the other hand, does not have an equivalent notion of operation
that is sufficiently rich and universal. The closest unit of computation in
PyTorch that has these characteristics is an `nn.Module`, which
is at a much higher granularity level, and this is why the library does
partitioning at this level in PyTorch.

### Manual Model Splitting

If you want to manually specify how to partition your model across devices, use
the `smp.partition` context manager. For instructions on how to set the
context manager for manual partitioning, see the following pages.

- [Manual
  splitting with TensorFlow](model-parallel-customize-training-script-tf.md#model-parallel-customize-training-script-tf-manual "model-parallel-customize-training-script-tf.md#model-parallel-customize-training-script-tf-manual")
- [Manual
  splitting with PyTorch](model-parallel-customize-training-script-pt.md#model-parallel-customize-training-script-pt-16-hvd "model-parallel-customize-training-script-pt.md#model-parallel-customize-training-script-pt-16-hvd")

To use this option after making modifications, in Step 2, you'll need to set
`auto_partition` to `False`, and define a
`default_partition` in the framework estimator class of the SageMaker
Python SDK. Any operation that is not explicitly placed on a partition through the
`smp.partition` context manager is executed on the
`default_partition`. In this case, the automated splitting logic is
bypassed, and each operation is placed based on your specification. Based on the
resulting graph structure, the model parallelism library creates a pipelined
execution schedule automatically.
