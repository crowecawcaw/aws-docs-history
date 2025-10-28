# Adapt your TensorFlow training

script

To start collecting model output tensors and debug training issues, make the following
modifications to your TensorFlow training script.

**Create a hook for training jobs within
SageMaker AI**

```
import smdebug.tensorflow as smd

hook=smd.get_hook(hook_type="keras", create_if_not_exists=True)
```

This creates a hook when you start a SageMaker training job. When you launch a training job
in [Launch training jobs with Debugger
using the SageMaker Python SDK](debugger-configuration-for-debugging.md "debugger-configuration-for-debugging.md") with any of the
`DebuggerHookConfig`, `TensorBoardConfig`, or
`Rules` in your estimator, SageMaker AI adds a JSON configuration file to your
training instance that is picked up by the `smd.get_hook` method. Note that
if you do not include any of the configuration APIs in your estimator, there will be no
configuration file for the hook to find, and the function returns
`None`.

**(Optional) Create a hook for training jobs outside
SageMaker AI**

If you run training jobs in local mode, directly on SageMaker Notebook instances, Amazon EC2
instances, or your own local devices, use `smd.Hook` class to create a hook.
However, this approach can only store the tensor collections and usable for TensorBoard
visualization. SageMaker Debugger’s built-in Rules don’t work with the local mode. The
`smd.get_hook` method also returns `None` in this case.

If you want to create a manual hook, use the following code snippet with the logic to
check if the hook returns `None` and create a manual hook using the
`smd.Hook` class.

```
import smdebug.tensorflow as smd

hook=smd.get_hook(hook_type="keras", create_if_not_exists=True)

if hook is None:
    hook=smd.KerasHook(
        out_dir='`/path/to/your/local/output/`',
        export_tensorboard=True
    )
```

After adding the hook creation code, proceed to the following topic for TensorFlow
Keras.

###### Note

SageMaker Debugger currently supports TensorFlow Keras only.

## Register the hook in your TensorFlow Keras training script

The following precedure walks you through how to use the hook and its methods to
collect output scalars and tensors from your model and optimizer.

1. Wrap your Keras model and optimizer with the hook’s class methods.

The `hook.register_model()` method takes your model and
iterates through each layer, looking for any tensors that match with regular
expressions that you’ll provide through the configuration in [Launch training jobs with Debugger
using the SageMaker Python SDK](debugger-configuration-for-debugging.md "debugger-configuration-for-debugging.md"). The collectable
tensors through this hook method are weights, biases, and
activations.

```
model=tf.keras.Model(...)
hook.register_model(model)
```

2. Wrap the optimizer by the `hook.wrap_optimizer()`
   method.

```
optimizer=tf.keras.optimizers.Adam(...)
optimizer=hook.wrap_optimizer(optimizer)
```

3. Compile the model in eager mode in TensorFlow.

To collect tensors from the model, such as the input and output tensors of
each layer, you must run the training in eager mode. Otherwise, SageMaker AI
Debugger will not be able to collect the tensors. However, other tensors,
such as model weights, biases, and the loss, can be collected without
explicitly running in eager mode.

```
model.compile(
    loss="categorical_crossentropy",
    optimizer=optimizer,
    metrics=["accuracy"],
    # Required for collecting tensors of each layer
    run_eagerly=True
)
```

4. Register the hook to the [`tf.keras.Model.fit()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit "https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit") method.

To collect the tensors from the hooks that you registered, add
`callbacks=[hook]` to the Keras `model.fit()`
class method. This will pass the `sagemaker-debugger` hook as a
Keras callback.

```
model.fit(
    X_train, Y_train,
    batch_size=batch_size,
    epochs=epoch,
    validation_data=(X_valid, Y_valid),
    shuffle=True,
    callbacks=[hook]
)
```

5. TensorFlow 2.x provides only symbolic gradient variables that do not
   provide access to their values. To collect gradients, wrap
   `tf.GradientTape` by the [`hook.wrap_tape()`](https://sagemaker-debugger.readthedocs.io/en/website/hook-methods.html#tensorflow-specific-hook-api "https://sagemaker-debugger.readthedocs.io/en/website/hook-methods.html#tensorflow-specific-hook-api") method, which requires you to
   write your own training step as follows.

```
def training_step(model, dataset):
    **with hook.wrap\_tape(tf.GradientTape()) as tape:**
        pred=model(data)
        loss_value=loss_fn(labels, pred)
    grads=tape.gradient(loss_value, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
```

By wrapping the tape, the `sagemaker-debugger` hook can
identify output tensors such as gradients, parameters, and losses. Wrapping
the tape ensures that the `hook.wrap_tape()` method around
functions of the tape object, such as `push_tape()`,
`pop_tape()`, `gradient()`, will set up the
writers of SageMaker Debugger and save tensors that are provided as input to
`gradient()` (trainable variables and loss) and output of
`gradient()` (gradients).

###### Note

To collect with a custom training loop, make sure that you use eager
mode. Otherwise, SageMaker Debugger is not able to collect any tensors.

For a full list of actions that the `sagemaker-debugger` hook APIs
offer to construct hooks and save tensors, see [Hook Methods](https://sagemaker-debugger.readthedocs.io/en/website/hook-methods.html "https://sagemaker-debugger.readthedocs.io/en/website/hook-methods.html") in the
_`sagemaker-debugger` Python SDK
documentation_.

After you have completed adapting your training script, proceed to [Launch training jobs with Debugger
using the SageMaker Python SDK](debugger-configuration-for-debugging.md "debugger-configuration-for-debugging.md").
