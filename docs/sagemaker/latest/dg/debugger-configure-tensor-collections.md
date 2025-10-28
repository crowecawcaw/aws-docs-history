# Configure tensor collections

using the `CollectionConfig` API

Use the `CollectionConfig` API operation to configure tensor
collections. Debugger provides pre-built tensor collections that cover a variety of
regular expressions (regex) of parameters if using Debugger-supported deep learning
frameworks and machine learning algorithms. As shown in the following example code,
add the built-in tensor collections you want to debug.

```
from sagemaker.debugger import CollectionConfig

collection_configs=[
    CollectionConfig(name="weights"),
    CollectionConfig(name="gradients")
]
```

The preceding collections set up the Debugger hook to save the tensors every 500
steps based on the default `"save_interval"` value.

For a full list of available Debugger built-in collections, see [Debugger Built-in Collections](https://github.com/awslabs/sagemaker-debugger/blob/master/docs/api.md#collection "https://github.com/awslabs/sagemaker-debugger/blob/master/docs/api.md#collection").

If you want to customize the built-in collections, such as changing the save
intervals and tensor regex, use the following `CollectionConfig` template
to adjust parameters.

```
from sagemaker.debugger import CollectionConfig

collection_configs=[
    CollectionConfig(
        name="`tensor_collection`",
        parameters={
            "`key_1`": "`value_1`",
            "`key_2`": "`value_2`",
            ...
            "`key_n`": "`value_n`"
        }
    )
]
```

For more information about available parameter keys, see [CollectionConfig](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.CollectionConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.CollectionConfig") in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"). For example, the
following code example shows how you can adjust the save intervals of the "losses"
tensor collection at different phases of training: save loss every 100 steps in
training phase and validation loss every 10 steps in validation phase.

```
from sagemaker.debugger import CollectionConfig

collection_configs=[
    CollectionConfig(
        name="`losses`",
        parameters={
            "`train.save_interval`": "`100`",
            "`eval.save_interval`": "`10`"
        }
    )
]
```

###### Tip

This tensor collection configuration object can be used for both [DebuggerHookConfig](debugger-configure-hook.md#debugger-configure-tensor-hook "debugger-configure-hook.md#debugger-configure-tensor-hook") and [Rule](use-debugger-built-in-rules.md#debugger-built-in-rules-configuration-param-change "use-debugger-built-in-rules.md#debugger-built-in-rules-configuration-param-change") API operations.
