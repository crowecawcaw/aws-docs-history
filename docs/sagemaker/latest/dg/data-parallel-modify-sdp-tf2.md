# Use the SMDDP library in your TensorFlow training

script (deprecated)

###### Important

The SMDDP library discontinued support for TensorFlow and is no longer available in
DLCs for TensorFlow later than v2.11.0. To find previous TensorFlow DLCs with the SMDDP
library installed, see [Supported frameworks](distributed-data-parallel-support.md#distributed-data-parallel-supported-frameworks "distributed-data-parallel-support.md#distributed-data-parallel-supported-frameworks").

The following steps show you how to modify a TensorFlow training script to utilize SageMaker AI's
distributed data parallel library. 

The library APIs are designed to be similar to Horovod APIs. For additional details on
each API that the library offers for TensorFlow, see the [SageMaker AI distributed data parallel TensorFlow API documentation](https://sagemaker.readthedocs.io/en/stable/api/training/smd_data_parallel.html#api-documentation "https://sagemaker.readthedocs.io/en/stable/api/training/smd_data_parallel.html#api-documentation").

###### Note

SageMaker AI distributed data parallel is adaptable to TensorFlow training scripts composed of
`tf` core modules except `tf.keras` modules. SageMaker AI distributed data
parallel does not support TensorFlow with Keras implementation.

###### Note

The SageMaker AI distributed data parallelism library supports Automatic Mixed Precision (AMP)
out of the box. No extra action is needed to enable AMP other than the framework-level
modifications to your training script. If gradients are in FP16, the SageMaker AI data parallelism
library runs its `AllReduce` operation in FP16. For more information about
implementing AMP APIs to your training script, see the following resources:

- [Frameworks - TensorFlow](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#tensorflow "https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#tensorflow") in the _NVIDIA Deep Learning
  Performance documentation_
- [Automatic
  Mixed Precision for Deep Learning](https://developer.nvidia.com/automatic-mixed-precision "https://developer.nvidia.com/automatic-mixed-precision") in the _NVIDIA
  Developer Docs_
- [TensorFlow mixed
  precision APIs](https://www.tensorflow.org/guide/mixed_precision "https://www.tensorflow.org/guide/mixed_precision") in the _TensorFlow
  documentation_

1. Import the library's TensorFlow client and initialize it.

```
import smdistributed.dataparallel.tensorflow as sdp 
sdp.init()
```

2. Pin each GPU to a single `smdistributed.dataparallel` process
   with `local_rank`—this refers to the relative rank of the process
   within a given node. The `sdp.tensorflow.local_rank()` API provides you with
   the local rank of the device. The leader node is rank 0, and the worker nodes are rank
   1, 2, 3, and so on. This is invoked in the following code block as
   `sdp.local_rank()`. `set_memory_growth` is not directly related
   to SageMaker AI distributed, but must be set for distributed training with TensorFlow.

```
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
if gpus:
    tf.config.experimental.set_visible_devices(gpus[sdp.local_rank()], 'GPU')
```

3. Scale the learning rate by the number of workers. The
   `sdp.tensorflow.size()` API provides you the number of workers in the
   cluster. This is invoked in the following code block as `sdp.size()`.

```
learning_rate = learning_rate * sdp.size()
```

4. Use the library’s `DistributedGradientTape` to optimize
   `AllReduce` operations during training. This
   wraps `tf.GradientTape`. 

```
with tf.GradientTape() as tape:
      output = model(input)
      loss_value = loss(label, output)
    
# SageMaker AI data parallel: Wrap tf.GradientTape with the library's DistributedGradientTape
tape = sdp.DistributedGradientTape(tape)
```

5. Broadcast the initial model variables from the leader node (rank 0) to all the
   worker nodes (ranks 1 through n). This is needed to ensure a consistent initialization
   across all the worker ranks. Use the `sdp.tensorflow.broadcast_variables` API
   after the model and optimizer variables are initialized. This is invoked in the
   following code block as `sdp.broadcast_variables()`.

```
sdp.broadcast_variables(model.variables, root_rank=0)
sdp.broadcast_variables(opt.variables(), root_rank=0)
```

6. Finally, modify your script to save checkpoints only on the leader node. The leader
   node has a synchronized model. This also avoids worker nodes overwriting the checkpoints
   and possibly corrupting the checkpoints.

```
if sdp.rank() == 0:
    checkpoint.save(checkpoint_dir)
```

The following is an example TensorFlow training script for distributed training with the
library.

```
import tensorflow as tf

# SageMaker AI data parallel: Import the library TF API
import smdistributed.dataparallel.tensorflow as sdp

# SageMaker AI data parallel: Initialize the library
sdp.init()

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
if gpus:
    # SageMaker AI data parallel: Pin GPUs to a single library process
    tf.config.experimental.set_visible_devices(gpus[sdp.local_rank()], 'GPU')

# Prepare Dataset
dataset = tf.data.Dataset.from_tensor_slices(...)

# Define Model
mnist_model = tf.keras.Sequential(...)
loss = tf.losses.SparseCategoricalCrossentropy()

# SageMaker AI data parallel: Scale Learning Rate
# LR for 8 node run : 0.000125
# LR for single node run : 0.001
opt = tf.optimizers.Adam(0.000125 * sdp.size())

@tf.function
def training_step(images, labels, first_batch):
    with tf.GradientTape() as tape:
        probs = mnist_model(images, training=True)
        loss_value = loss(labels, probs)

    # SageMaker AI data parallel: Wrap tf.GradientTape with the library's DistributedGradientTape
    tape = sdp.DistributedGradientTape(tape)

    grads = tape.gradient(loss_value, mnist_model.trainable_variables)
    opt.apply_gradients(zip(grads, mnist_model.trainable_variables))

    if first_batch:
       # SageMaker AI data parallel: Broadcast model and optimizer variables
       sdp.broadcast_variables(mnist_model.variables, root_rank=0)
       sdp.broadcast_variables(opt.variables(), root_rank=0)

    return loss_value

...

# SageMaker AI data parallel: Save checkpoints only from master node.
if sdp.rank() == 0:
    checkpoint.save(checkpoint_dir)

```

After you have completed adapting your training script, move on to [Launching distributed training jobs with SMDDP using the
SageMaker Python SDK](data-parallel-use-api.md "data-parallel-use-api.md").
