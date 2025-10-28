# Modify a TensorFlow training

script

In this section, you learn how to modify TensorFlow training scripts to configure the SageMaker
model parallelism library for auto-partitioning and manual partitioning. This selection
of examples also includes an example integrated with Horovod for hybrid model and data
parallelism.

###### Note

To find which TensorFlow versions are supported by the library, see [Supported Frameworks and
AWS Regions](distributed-model-parallel-support.md "distributed-model-parallel-support.md").

The required modifications you must make to your training script to use the library
are listed in [Automated splitting
with TensorFlow](#model-parallel-customize-training-script-tf-23 "#model-parallel-customize-training-script-tf-23").

To learn how to modify your training script to use hybrid model and data parallelism
with Horovod, see [Automated
splitting with TensorFlow and Horovod for hybrid model and data parallelism](#model-parallel-customize-training-script-tf-2.3 "#model-parallel-customize-training-script-tf-2.3").

If you want to use manual partitioning, also review [Manual
splitting with TensorFlow](#model-parallel-customize-training-script-tf-manual "#model-parallel-customize-training-script-tf-manual").

The following topics show examples of training scripts that you can use to configure
SageMaker's model parallelism library for auto-partitioning and manual partitioning TensorFlow
models.

###### Note

Auto-partitioning is enabled by default. Unless otherwise specified, the example
scripts use auto-partitioning.

###### Topics

- [Automated splitting
  with TensorFlow](#model-parallel-customize-training-script-tf-23 "#model-parallel-customize-training-script-tf-23")
- [Automated
  splitting with TensorFlow and Horovod for hybrid model and data parallelism](#model-parallel-customize-training-script-tf-2.3 "#model-parallel-customize-training-script-tf-2.3")
- [Manual
  splitting with TensorFlow](#model-parallel-customize-training-script-tf-manual "#model-parallel-customize-training-script-tf-manual")
- [Unsupported framework
  features](#model-parallel-tf-unsupported-features "#model-parallel-tf-unsupported-features")

## Automated splitting

with TensorFlow

The following training script changes are required to run a TensorFlow model with
SageMaker's model parallelism library:

1. Import and initialize the library with [`smp.init()`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#smp.init "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#smp.init").
2. Define a Keras model by inheriting from [`smp.DistributedModel`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_tensorflow.html "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_tensorflow.html") instead of the Keras
   Model class. Return the model outputs from the call method of the
   `smp.DistributedModel` object. Be mindful that any tensors
   returned from the call method will be broadcast across model-parallel
   devices, incurring communication overhead, so any tensors that are not
   needed outside the call method (such as intermediate activations) should not
   be returned.
3. Set `drop_remainder=True` in `tf.Dataset.batch()`
   method. This is to ensure that the batch size is always divisible by the
   number of microbatches.
4. Seed the random operations in the data pipeline using
   `smp.dp_rank()`, e.g., `shuffle(ds,
seed=smp.dp_rank())` to ensure consistency of data samples across
   GPUs that hold different model partitions.
5. Put the forward and backward logic in a step function and decorate it with
   `smp.step`.
6. Perform post-processing on the outputs across microbatches using [`StepOutput`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#StepOutput "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#StepOutput") methods such as
   `reduce_mean`. The [`smp.step`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#smp.init "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#smp.init") function must have a return value
   that depends on the output of `smp.DistributedModel`.
7. If there is an evaluation step, similarly place the forward logic inside
   an `smp.step`-decorated function and post-process the outputs
   using [`StepOutput` API](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#StepOutput "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#StepOutput").

To learn more about the SageMaker's model parallelism library API, refer to the [API documentation](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html").

The following Python script is an example of a training script after the changes
are made.

```
import tensorflow as tf

# smdistributed: Import TF2.x API
import smdistributed.modelparallel.tensorflow as smp

# smdistributed: Initialize
smp.init()

# Download and load MNIST dataset.
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(
    "MNIST-data-%d" % smp.rank()
)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Add a channels dimension
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

# smdistributed: If needed, seed the shuffle with smp.dp_rank(), and drop_remainder
# in batching to make sure batch size is always divisible by number of microbatches
train_ds = (
    tf.data.Dataset.from_tensor_slices((x_train, y_train))
    .shuffle(10000, seed=smp.dp_rank())
    .batch(256, drop_remainder=True)
)

# smdistributed: Define smp.DistributedModel the same way as Keras sub-classing API
class MyModel(smp.DistributedModel):
    def __init__(self):
        super(MyModel, self).__init__()
        # define layers

    def call(self, x, training=None):
        # define forward pass and return the model output

model = MyModel()

loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="train_accuracy")

# smdistributed: Define smp.step. Return any tensors needed outside
@smp.step
def get_grads(images, labels):
    predictions = model(images, training=True)
    loss = loss_object(labels, predictions)

    grads = optimizer.get_gradients(loss, model.trainable_variables)
    return grads, loss, predictions


@tf.function
def train_step(images, labels):
    gradients, loss, predictions = get_grads(images, labels)

    # smdistributed: Accumulate the gradients across microbatches
    gradients = [g.accumulate() for g in gradients]
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    # smdistributed: Merge predictions and average losses across microbatches
    train_accuracy(labels, predictions.merge())
    return loss.reduce_mean()


for epoch in range(5):
    # Reset the metrics at the start of the next epoch
    train_accuracy.reset_states()
    for images, labels in train_ds:
        loss = train_step(images, labels)
    accuracy = train_accuracy.result()
```

If you are done preparing your training script, proceed to [Step 2: Launch a Training Job Using the SageMaker
Python SDK](model-parallel-sm-sdk.md "model-parallel-sm-sdk.md"). If you
want to run a hybrid model and data parallel training job, continue to the next
section.

## Automated

splitting with TensorFlow and Horovod for hybrid model and data parallelism

You can use the SageMaker model parallelism library with Horovod for hybrid model and
data parallelism. To read more about how the library splits a model for hybrid
parallelism, see [Pipeline parallelism (available for
PyTorch and TensorFlow)](model-parallel-intro.md#model-parallel-intro-pp "model-parallel-intro.md#model-parallel-intro-pp").

In this step, we focus on how to modify your training script to adapt the SageMaker
model parallelism library.

To properly set up your training script to pick up the hybrid parallelism
configuration that you'll set in [Step 2: Launch a Training Job Using the SageMaker
Python SDK](model-parallel-sm-sdk.md "model-parallel-sm-sdk.md"), use the library's helper functions,
`smp.dp_rank()` and `smp.mp_rank()`, which automatically
detect the data parallel rank and model parallel rank respectively.

To find all MPI primitives the library supports, see [MPI Basics](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#mpi-basics "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/v1.2.0/smd_model_parallel_common_api.html#mpi-basics") in the SageMaker Python SDK documentation.

The required changes needed in the script are:

- Adding `hvd.allreduce`
- Broadcasting variables after the first batch, as required by
  Horovod
- Seeding shuffling and/or sharding operations in the data pipeline with
  `smp.dp_rank()`.

###### Note

When you use Horovod, you must not directly call `hvd.init` in your
training script. Instead, you'll have to set `"horovod"` to
`True` in the SageMaker Python SDK `modelparallel`
parameters in [Step 2: Launch a Training Job Using the SageMaker
Python SDK](model-parallel-sm-sdk.md "model-parallel-sm-sdk.md"). This allows the library to
internally initialize Horovod based on the device assignments of model
partitions. Calling `hvd.init()` directly in your training script can
cause problems.

###### Note

Using the `hvd.DistributedOptimizer` API directly in your training
script might result in a poor training performance and speed, because the API
implicitly places the `AllReduce` operation inside
`smp.step`. We recommend you to use the model parallelism library
with Horovod by directly calling `hvd.allreduce` after calling
`accumulate()` or `reduce_mean()` on the gradients
returned from `smp.step`, as will be shown in the following
example.

To learn more about the SageMaker's model parallelism library API, refer to the [API documentation](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html").

```
import tensorflow as tf
import horovod.tensorflow as hvd

# smdistributed: Import TF2.x API
import smdistributed.modelparallel.tensorflow as smp

# smdistributed: Initialize
smp.init()

# Download and load MNIST dataset.
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(
    "MNIST-data-%d" % smp.rank()
)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Add a channels dimension
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

# smdistributed: Seed the shuffle with smp.dp_rank(), and drop_remainder
# in batching to make sure batch size is always divisible by number of microbatches
train_ds = (
    tf.data.Dataset.from_tensor_slices((x_train, y_train))
    .shuffle(10000, seed=smp.dp_rank())
    .batch(256, drop_remainder=True)
)

# smdistributed: Define smp.DistributedModel the same way as Keras sub-classing API
class MyModel(smp.DistributedModel):
    def __init__(self):
        super(MyModel, self).__init__()
        # define layers

    def call(self, x, training=None):
        # define forward pass and return model outputs


model = MyModel()

loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="train_accuracy")

# smdistributed: Define smp.step. Return any tensors needed outside
@smp.step
def get_grads(images, labels):
    predictions = model(images, training=True)
    loss = loss_object(labels, predictions)

    grads = optimizer.get_gradients(loss, model.trainable_variables)
    return grads, loss, predictions


@tf.function
def train_step(images, labels, first_batch):
    gradients, loss, predictions = get_grads(images, labels)

    # smdistributed: Accumulate the gradients across microbatches
    # Horovod: AllReduce the accumulated gradients
    gradients = [hvd.allreduce(g.accumulate()) for g in gradients]
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    # Horovod: Broadcast the variables after first batch
    if first_batch:
        hvd.broadcast_variables(model.variables, root_rank=0)
        hvd.broadcast_variables(optimizer.variables(), root_rank=0)

    # smdistributed: Merge predictions across microbatches
    train_accuracy(labels, predictions.merge())
    return loss.reduce_mean()


for epoch in range(5):
    # Reset the metrics at the start of the next epoch
    train_accuracy.reset_states()

    for batch, (images, labels) in enumerate(train_ds):
        loss = train_step(images, labels, tf.constant(batch == 0))
```

## Manual

splitting with TensorFlow

Use `smp.partition` context managers to place operations in specific
partition. Any operation not placed in any `smp.partition` contexts is
placed in the `default_partition`. To learn more about the SageMaker's model
parallelism library API, refer to the [API documentation](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html").

```
import tensorflow as tf

# smdistributed: Import TF2.x API.
import smdistributed.modelparallel.tensorflow as smp

# smdistributed: Initialize
smp.init()

# Download and load MNIST dataset.
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(
    "MNIST-data-%d" % smp.rank()
)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Add a channels dimension
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

# smdistributed: If needed, seed the shuffle with smp.dp_rank(), and drop_remainder
# in batching to make sure batch size is always divisible by number of microbatches.
train_ds = (
    tf.data.Dataset.from_tensor_slices((x_train, y_train))
    .shuffle(10000, seed=smp.dp_rank())
    .batch(256, drop_remainder=True)
)

# smdistributed: Define smp.DistributedModel the same way as Keras sub-classing API.
class MyModel(smp.DistributedModel):
    def __init__(self):
         # define layers

    def call(self, x):
        with smp.partition(0):
            x = self.layer0(x)
        with smp.partition(1):
            return self.layer1(x)


model = MyModel()

loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="train_accuracy")

# smdistributed: Define smp.step. Return any tensors needed outside
@smp.step
def get_grads(images, labels):
    predictions = model(images, training=True)
    loss = loss_object(labels, predictions)

    grads = optimizer.get_gradients(loss, model.trainable_variables)
    return grads, loss, predictions


@tf.function
def train_step(images, labels):
    gradients, loss, predictions = get_grads(images, labels)

    # smdistributed: Accumulate the gradients across microbatches
    gradients = [g.accumulate() for g in gradients]
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    # smdistributed: Merge predictions and average losses across microbatches
    train_accuracy(labels, predictions.merge())
    return loss.reduce_mean()


for epoch in range(5):
    # Reset the metrics at the start of the next epoch
    train_accuracy.reset_states()
    for images, labels in train_ds:
        loss = train_step(images, labels)
    accuracy = train_accuracy.result()

```

## Unsupported framework

features

The following TensorFlow features are not supported by the library:

- `tf.GradientTape()` is currently not supported. You can use
  `Optimizer.get_gradients()` or
  `Optimizer.compute_gradients()` instead to compute
  gradients.
- The `tf.train.Checkpoint.restore()` API is currently not
  supported. For checkpointing, use `smp.CheckpointManager`
  instead, which provides the same API and functionality. Note that checkpoint
  restores with `smp.CheckpointManager` should take place after the
  first step.
