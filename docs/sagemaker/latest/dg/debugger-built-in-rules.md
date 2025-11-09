# List of Debugger built-in rules

You can use the Debugger built-in rules, provided by Amazon SageMaker Debugger, to analyze metrics and tensors collected
while training your models. The following lists the debugger rules, including information
and an example on how to configure and deploy each built-in rule.

The Debugger built-in rules monitor various common conditions that
are critical for the success of a training job. You can call the built-in rules using
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") or the low-level SageMaker API operations.

There's no additional cost for
using the built-in rules. For more information about billing, see the [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") page.

###### Note

The maximum numbers of built-in rules that you can attach to a training job is 20.
SageMaker Debugger fully manages the built-in rules and analyzes your training job
synchronously.

###### Important

To use the new Debugger features, you need to upgrade the SageMaker Python SDK and the SMDebug
client library. In your iPython kernel, Jupyter notebook, or JupyterLab environment, run
the following code to install the latest versions of the libraries and restart the
kernel.

```
import sys
import IPython
!{sys.executable} -m pip install -U sagemaker smdebug
IPython.Application.instance().kernel.do_shutdown(True)
```

## Debugger rule

The following rules are the Debugger built-in rules that are callable using the
`Rule.sagemaker` classmethod.

Debugger built-in rules for generating training reports

| Scope of Validity                                     | Built-in Rules            |
| ----------------------------------------------------- | ------------------------- |
| Training Report for SageMaker AI XGboost training job | • `create_xgboost_report` |

Debugger built-in rules for debugging model
training data (output tensors)

| Scope of Validity                                                                      | Built-in Rules                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deep learning frameworks (TensorFlow, MXNet, and PyTorch)                              | • `dead_relu`<br>• `exploding_tensor`<br>• `poor_weight_initialization`<br>• `saturated_activation`<br>• `vanishing_gradient`<br>• `weight_update_ratio`                                                 |
| Deep learning frameworks (TensorFlow, MXNet, and PyTorch) and the XGBoost<br>algorithm | • `all_zero`<br>• `class_imbalance`<br>• `loss_not_decreasing`<br>• `overfit`<br>• `overtraining`<br>• `similar_across_runs`<br>• `stalled_training_rule`<br>• `tensor_variance`<br>• `unchanged_tensor` |
| Deep learning applications                                                             | • `check_input_images`<br>• `nlp_sequence_ratio`                                                                                                                                                         |
| XGBoost algorithm                                                                      | • `confusion`<br>• `feature_importance_overweight`<br>• `tree_depth`                                                                                                                                     |

**To use the built-in rules with default parameter values** –
use the following configuration format:

```
from sagemaker.debugger import Rule, ProfilerRule, rule_configs

rules = [
    Rule.sagemaker(rule_configs.`built_in_rule_name_1`()),
    Rule.sagemaker(rule_configs.`built_in_rule_name_2`()),
    ...
    Rule.sagemaker(rule_configs.`built_in_rule_name_n`())
]
```

**To use the built-in rules with customizing the parameter
values** – use the following configuration format:

```
from sagemaker.debugger import Rule, ProfilerRule, rule_configs

rules = [
    Rule.sagemaker(
        base_config=rule_configs.`built_in_rule_name`(),
        rule_parameters={
                "`key`": "`value`"
        }
        collections_to_save=[
            CollectionConfig(
                name="`tensor_collection_name`",
                parameters={
                    "`key`": "`value`"
                }
            )
        ]
    )
]
```

To find available keys for the `rule_parameters` parameter, see the parameter description tables.

Sample rule configuration codes are provided for each built-in rule below the parameter
description tables.

- For a full instruction and examples of using the Debugger built-in rules, see [Debugger built-in rules example
  code](debugger-built-in-rules-example.md#debugger-deploy-built-in-rules "debugger-built-in-rules-example.md#debugger-deploy-built-in-rules").
- For a full instruction on using the built-in rules with the low-level SageMaker API
  operations, see [Configure Debugger using SageMaker API](debugger-createtrainingjob-api.md "debugger-createtrainingjob-api.md").

## CreateXgboostReport

The CreateXgboostReport rule collects output tensors from an XGBoost training job and
autogenerates a comprehensive training report. You can download a comprehensive
profiling report while a training job is running or after the training job is complete,
and check progress of training or the final result of the training job. The
CreateXgboostReport rule collects the following output tensors by default:

- `hyperparameters` – Saves at the first step
- `metrics` – Saves loss and accuracy every 5 steps
- `feature_importance` – Saves every 5 steps
- `predictions` – Saves every 5 steps
- `labels` – Saves every 5 steps

Parameter Descriptions for the CreateXgboostReport Rule

| Parameter Name | Description                                                                                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`   | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String |

```
rules=[
    Rule.sagemaker(
        rule_configs.`create_xgboost_report`()
    )
]
```

## DeadRelu

This rule detects when the percentage of rectified linear unit (ReLU) activation
functions in a trial are considered dead because their activation activity has dropped
below a threshold. If the percent of inactive ReLUs in a layer is greater than the
`threshold_layer` value of inactive ReLUs, the rule returns
`True`.

Parameter Descriptions for the DeadRelu Rule

| Parameter Name         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`           | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                               |
| `tensor_regex`         | A list of regex patterns used to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: `".*relu_output"` |
| `threshold_inactivity` | Defines a level of activity below which a ReLU is considered to be<br>dead. A ReLU might be active in the beginning of a trial and then<br>slowly die during the training process. If the ReLU is active less<br>than the `threshold_inactivity`, it is considered to be<br>dead.<br>**Optional**<br>Valid values: Float<br>Default values: `1.0` (in percentage)                                                                                        |
| `threshold_layer`      | Returns `True` if the percentage of inactive ReLUs in a<br>layer is greater than `threshold_layer`.<br>Returns `False` if the percentage of inactive ReLUs in<br>a layer is less than `threshold_layer`.<br>**Optional**<br>Valid values: Float<br>Default values: `50.0` (in percentage)                                                                                                                                                                |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.dead_relu(),
        rule_parameters={
                "tensor_regex": "`.*relu_output|.*ReLU_output`",
                "threshold_inactivity": "`1.0`",
                "threshold_layer": "`50.0`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`custom_relu_collection`",
                parameters={
                    "include_regex: "`.*relu_output|.*ReLU_output`",
                    "save_interval": "`500`"
                }
            )
        ]
    )
]
```

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

###### Note

This rule is not available for the XGBoost algorithm.

## ExplodingTensor

This rule detects whether the tensors emitted during training have non-finite values,
either infinite or NaN (not a number). If a non-finite value is detected, the rule
returns `True`.

Parameter Descriptions for the ExplodingTensor Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                               |
| `collection_names` | The list of collection names whose tensors the rule<br>inspects.<br>**Optional**<br>Valid values: String<br>Default value: `None`                                                                                                                                                                                                                                                                        |
| `tensor_regex`     | A list of regex patterns used to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: String<br>Default value: `None` |
| `only_nan`         | `True` to monitor the `base_trial` tensors<br>only for `NaN` values and not for infinity.<br>`False` to treat both `NaN` and infinity as<br>exploding values and to monitor for both.<br>**Optional**<br>Default value: `False`                                                                                                                                                                          |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`exploding_tensor`(),
        rule_parameters={
                "tensor_regex": "`.*gradient`",
                "only_nan": "`False`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`gradients`",
                parameters={
                    "save_interval": "`500`"
                }
            )
        ]
    )
]
```

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

###### Note

This rule is not available for the XGBoost algorithm.

## PoorWeightInitialization

This rule detects if your model parameters have been poorly initialized.

Good initialization breaks the symmetry of the weights and gradients in a neural
network and maintains commensurate activation variances across layers. Otherwise, the
neural network doesn't learn effectively. Initializers like Xavier aim to keep variance
constant across activations, which is especially relevant for training very deep neural
nets. Too small an initialization can lead to vanishing gradients. Too large an
initialization can lead to exploding gradients. This rule checks the variance of
activation inputs across layers, the distribution of gradients, and the loss convergence
for the initial steps to determine if a neural network has been poorly
initialized.

Parameter Descriptions for the PoorWeightInitialization Rule

| Parameter Name            | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `base_trial`              | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                         |
| `activation_inputs_regex` | A list of regex patterns used to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: String<br>Default value: `".*relu_input"` |
| `threshold`               | If the ratio between minimum and maximum variance of weights per<br>layer exceeds the `threshold` at a step, the rule returns<br>`True`.<br>**Optional**<br>Valid values: Float<br>Default value: `10.0`                                                                                                                                                                                                           |
| `distribution_range`      | If the minimum difference between 5th and 95th percentiles of the<br>gradient distribution is less than the<br>`distribution_range`, the rule returns<br>`True`.<br>**Optional**<br>Valid values: Float<br>Default value: `0.001`                                                                                                                                                                                  |
| `patience`                | The number of steps to wait until the loss is considered to be no<br>longer decreasing.<br>**Optional**<br>Valid values: Integer<br>Default value: `5`                                                                                                                                                                                                                                                             |
| `steps`                   | The number of steps this rule analyzes. You typically need to<br>check only the first few iterations.<br>**Optional**<br>Valid values: Float<br>Default value: `10`                                                                                                                                                                                                                                                |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`poor_weight_initialization`(),
        rule_parameters={
                "activation_inputs_regex": "`.*relu_input|.*ReLU_input`",
                "threshold": "`10.0`",
                "distribution_range": "`0.001`",
                "patience": "`5`",
                "steps": "`10`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`custom_relu_collection`",
                parameters={
                    "`include_regex`": "`.*relu_input|.*ReLU_input`",
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

###### Note

This rule is not available for the XGBoost algorithm.

## SaturatedActivation

This rule detects if the tanh and sigmoid activation layers are becoming saturated. An
activation layer is saturated when the input of the layer is close to the maximum or
minimum of the activation function. The minimum and maximum of the tanh and sigmoid
activation functions are defined by their respective `min_threshold` and
`max_thresholds` values. If the activity of a node drops below the
`threshold_inactivity` percentage, it is considered saturated. If more
than a `threshold_layer` percent of the nodes are saturated, the rule returns
`True`.

Parameter Descriptions for the SaturatedActivation Rule

| Parameter Name          | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `base_trial`            | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                        |
| `collection_names`      | The list of collection names whose tensors the rule<br>inspects.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: None                                                                                                                                                                                                                                              |
| `tensor_regex`          | A list of regex patterns used to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: String<br>Default value: `".\*tanh_input | .\*sigmoid_input".` |
| `threshold_tanh_min`    | The minimum and maximum thresholds that define the extremes of the<br>input for a tanh activation function, defined as:<br>`(min_threshold, max_threshold)`. The default values<br>are determined based on a vanishing gradient threshold of<br>0.0000001.<br>**Optional**<br>Valid values: Float<br>Default values: `-9.4999`                                                                                    |
| `threshold_tanh_max`    | The minimum and maximum thresholds that define the extremes of the<br>input for a tanh activation function, defined as:<br>`(min_threshold, max_threshold)`. The default values<br>are determined based on a vanishing gradient threshold of<br>0.0000001.<br>**Optional**<br>Valid values: Float<br>Default values: `9.4999`                                                                                     |
| `threshold_sigmoid_min` | The minimum and maximum thresholds that define the extremes of the<br>input for a sigmoid activation function, defined as:<br>`(min_threshold, max_threshold)`. The default values<br>are determined based on a vanishing gradient threshold of<br>0.0000001.<br>**Optional**<br>Valid values: Float<br>Default values: `-23`                                                                                     |
| `threshold_sigmoid_max` | The minimum and maximum thresholds that define the extremes of the<br>input for a sigmoid activation function, defined as:<br>`(min_threshold, max_threshold)`. The default values<br>are determined based on a vanishing gradient threshold of<br>0.0000001.<br>**Optional**<br>Valid values: Float<br>Default values: `16.99999`                                                                                |
| `threshold_inactivity`  | The percentage of inactivity below which the activation layer is<br>considered to be saturated. The activation might be active in the<br>beginning of a trial and then slowly become less active during the<br>training process.<br>**Optional**<br>Valid values: Float<br>Default values: `1.0`                                                                                                                  |
| `threshold_layer`       | Returns `True` if the number of saturated activations<br>in a layer is greater than the `threshold_layer`<br>percentage.<br>Returns `False` if the number of saturated activations<br>in a layer is less than the `threshold_layer`<br>percentage.<br>**Optional**<br>Valid values: Float<br>Default values: `50.0`                                                                                               |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`saturated_activation`(),
        rule_parameters={
                "tensor_regex": "`.*tanh_input|.*sigmoid_input`",
                "threshold_tanh_min": "`-9.4999`",
                "threshold_tanh_max": "`9.4999`",
                "threshold_sigmoid_min": "`-23`",
                "threshold_sigmoid_max": "`16.99999`",
                "threshold_inactivity": "`1.0`",
                "threshold_layer": "`50.0`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`custom_activations_collection`",
                parameters={
                    "`include_regex`": "`.*tanh_input|.*sigmoid_input`"
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

###### Note

This rule is not available for the XGBoost algorithm.

## VanishingGradient

This rule detects if the gradients in a trial become extremely small or drop to a zero
magnitude. If the mean of the absolute values of the gradients drops below a specified
`threshold`, the rule returns `True`.

Parameters Descriptions for the VanishingGradient Rule

| Parameter Name | Description                                                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`   | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String |
| `threshold`    | The value at which the gradient is determined to be<br>vanishing.**Optional**Valid values:<br>FloatDefault value:<br>`0.0000001`.                                          |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`vanishing_gradient`(),
        rule_parameters={
                "threshold": "`0.0000001`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`gradients`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

###### Note

This rule is not available for the XGBoost algorithm.

## WeightUpdateRatio

This rule keeps track of the ratio of updates to weights during training and detects
if that ratio gets too large or too small. If the ratio of updates to weights is larger
than the `large_threshold value` or if this ratio is smaller than
`small_threshold`, the rule returns `True`.

Conditions for training are best when the updates are commensurate to gradients.
Excessively large updates can push the weights away from optimal values, and very small
updates result in very slow convergence. This rule requires weights to be available for
two training steps, and `train.save_interval` needs to be set equal to
`num_steps`.

Parameter Descriptions for the WeightUpdateRatio Rule

| Parameter Name,   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`      | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                                                                                                          |
| `num_steps`       | The number of steps across which the rule checks to determine if<br>the tensor has changed.<br>The number of steps across which you want to compare the weight<br>ratios. If you pass no value, the rule runs by default against the<br>current step and the immediately previous saved step. If you<br>override the default by passing a value for this parameter, the<br>comparison is done between weights at step `s` and at a<br>step `>= s<br>• num_steps`.<br>**Optional**<br>Valid values: Integer<br>Default value: `None` |
| `large_threshold` | The maximum value that the ratio of updates to weight can take<br>before the rule returns `True`.<br>**Optional**<br>Valid values: Float<br>Default value: `10.0`                                                                                                                                                                                                                                                                                                                                                                   |
| `small_threshold` | The minimum value that the ratio of updates to weight can take,<br>below which the rule returns `True`.<br>**Optional**<br>Valid values: Float<br>Default value: `0.00000001`                                                                                                                                                                                                                                                                                                                                                       |
| `epsilon`         | A small constant used to ensure that Debugger does not divide by<br>zero when computing the ratio updates to weigh.<br>**Optional**<br>Valid values: Float<br>Default value: `0.000000001`                                                                                                                                                                                                                                                                                                                                          |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`weight_update_ratio`(),
        rule_parameters={
                "num_steps": "`100`",
                "large_threshold": "`10.0`",
                "small_threshold": "`0.00000001`",
                "epsilon": "`0.000000001`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`weights`",
                parameters={
                    "`train.save_interval`": "`100`"
                }
            )
        ]
    )
]
```

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

###### Note

This rule is not available for the XGBoost algorithm.

## AllZero

This rule detects if all or a specified percentage of the tensor values are
zero.

This rule can be applied either to one of the supported deep learning frameworks
(TensorFlow, MXNet, and PyTorch) or to the XGBoost algorithm. You must specify either
the `collection_names` or `tensor_regex` parameter. If both the
parameters are specified, the rule inspects the union of tensors from both sets.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameters Descriptions for the AllZero Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                    |
| `collection_names` | The list of collection names whose tensors the rule<br>inspects.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: `None`                                                                                                                                                                                                                                                                        |
| `tensor_regex`     | A list of regex patterns used to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: `None` |
| `threshold`        | Specifies the percentage of values in the tensor that needs to be<br>zero for this rule to be invoked.<br>**Optional**<br>Valid values: Float<br>Default value: 100 (in percentage)                                                                                                                                                                                                                                                           |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`all_zero`(),
        rule_parameters={
                "tensor_regex": "`.*`",
                "threshold": "`100`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`all`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

## ClassImbalance

This rule measures sampling imbalances between classes and throws errors if the
imbalance exceeds a threshold or if too many mispredictions for underrepresented classes
occur as a result of the imbalance.

Classification models require well-balanced classes in the training dataset or a
proper weighting/sampling of classes during training. The rule performs the following
checks:

- It counts the occurrences per class. If the ratio of number of samples
  between smallest and largest class is larger than the
  `threshold_imbalance`, an error is thrown.
- It checks the prediction accuracy per class. If resampling or weighting has
  not been correctly applied, then the model can reach high accuracy for the class
  with many training samples, but low accuracy for the classes with few training
  samples. If a fraction of mispredictions for a certain class is above
  `threshold_misprediction`, an error is thrown.

This rule can be applied either to one of the supported deep learning frameworks
(TensorFlow, MXNet, and PyTorch) or to the XGBoost algorithm.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the ClassImbalance Rule

| Parameter Name            | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`              | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                             |
| `threshold_imbalance`     | The acceptable imbalance between the number of samples in the<br>smallest class and in the largest class. Exceeding this threshold<br>value throws an error.<br>**Optional**<br>Valid values: Float<br>Default value: `10`                                                                                                                                                                                                             |
| `threshold_misprediction` | A limit on the fraction of mispredictions allowed for each class.<br>Exceeding this threshold throws an error. The underrepresented<br>classes are most at risk of crossing this threshold.<br>**Optional**<br>Valid values: Float<br>Default value: `0.7`                                                                                                                                                                             |
| `samples`                 | The number of labels that have to be processed before an imbalance<br>is evaluated. The rule might not be triggered until it has seen<br>sufficient samples across several steps. The more classes that your<br>dataset contains, the larger this `sample` number should<br>be.<br>**Optional**<br>Valid values: Integer<br>Default value: `500` (assuming a dataset like MNIST<br>with 10 classes)                                    |
| `argmax`                  | If `True`, [np.argmax](https://docs.scipy.org/doc/numpy-1.9.3/reference/generated/numpy.argmax.html "https://docs.scipy.org/doc/numpy-1.9.3/reference/generated/numpy.argmax.html") is applied to the prediction tensor. Required<br>when you have a vector of probabilities for each class. It is used<br>to determine which class has the highest probability.<br>**Conditional**<br>Valid values: Boolean<br>Default value: `False` |
| `labels_regex`            | The name of the tensor that contains the labels.<br>**Optional**<br>Valid values: String<br>Default value: `".*labels"`                                                                                                                                                                                                                                                                                                                |
| `predictions_regex`       | The name of the tensor that contains the predictions.<br>**Optional**<br>Valid values: String<br>Default value: `".*predictions"`                                                                                                                                                                                                                                                                                                      |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`class_imbalance`(),
        rule_parameters={
                "threshold_imbalance": "`10`",
                "threshold_misprediction": "`0.7`",
                "samples": "`500`",
                "argmax": "`False`",
                "labels_regex": "`.*labels`",
                "predictions_regex": "`.*predictions`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`custom_output_collection`",
                parameters={
                    "include_regex": "`.*labels|.*predictions`",
                    "save_interval": "`500`"
                }
            )
        ]
    )
]
```

## LossNotDecreasing

This rule detects when the loss is not decreasing in value at an adequate rate. These
losses must be scalars.

This rule can be applied either to one of the supported deep learning frameworks
(TensorFlow, MXNet, and PyTorch) or to the XGBoost algorithm. You must specify either
the `collection_names` or `tensor_regex` parameter. If both the
parameters are specified, the rule inspects the union of tensors from both sets.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the LossNotDecreasing Rule

| Parameter Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `base_trial`                 | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `collection_names`           | The list of collection names whose tensors the rule<br>inspects.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: `None`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `tensor_regex`               | A list of regex patterns that is used to restrict this comparison<br>to specific scalar-valued tensors. The rule inspects only the<br>tensors that match the regex patterns specified in the list. If no<br>patterns are passed, the rule compares all tensors gathered in the<br>trials by default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: `None`                                                                                                                                                                                                        |
| `use_losses_collection`      | If set to `True`, looks for losses in the collection<br>named "losses" when the collection is present.<br>**Optional**<br>Valid values: Boolean<br>Default value: `True`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `num_steps`                  | The minimum number of steps after which the rule checks if the<br>loss has decreased. Rule evaluation happens every<br>`num_steps`. The rule compares the loss for this step<br>with the loss at a step which is at least `num_steps`<br>behind the current step. For example, suppose that the loss is being<br>saved every three steps, but `num_steps` is set to 10. At<br>step 21, loss for step 21 is compared with loss for step 9. The next<br>step at which loss is checked is step 33, because ten steps after<br>step 21 is step 31, and at step 31 and step 32 loss is not saved.<br>**Optional**<br>Valid values: Integer<br>Default value: `10` |
| `diff_percent`               | The minimum percentage difference by which the loss should<br>decrease between `num_steps`.<br>**Optional**<br>Valid values: `0.0` < float <<br>`100`<br>Default value: `0.1` (in percentage)                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `increase_threshold_percent` | The maximum threshold percent that loss is allowed to increase in case loss has been<br>increasing<br>**Optional**<br>Valid values: `0` < float <<br>`100`<br>Default value: `5` (in percentage)                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `mode`                       | The name of the Debugger mode to query tensor values for rule<br>checking. If this is not passed, the rule checks in order by default<br>for the `mode.EVAL`, then `mode.TRAIN`, and<br>then `mode.GLOBAL`.<br>**Optional**<br>Valid values: String (`EVAL`, `TRAIN`, or<br>`GLOBAL`)<br>Default value: `GLOBAL`                                                                                                                                                                                                                                                                                                                                             |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`loss_not_decreasing`(),
        rule_parameters={
                "tensor_regex": "`.*`",
                "use_losses_collection": "`True`",
                "num_steps": "`10`",
                "diff_percent": "`0.1`",
                "increase_threshold_percent": "`5`",
                "mode": "`GLOBAL`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`losses`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

## Overfit

This rule detects if your model is being overfit to the training data by comparing the
validation and training losses.

This rule can be applied either to one of the supported deep learning frameworks
(TensorFlow, MXNet, and PyTorch) or to the XGBoost algorithm.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

###### Note

A standard way to prevent overfitting is to regularize your model.

Parameter Descriptions for the Overfit Rule

| Parameter Name    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`      | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                  |
| `tensor_regex`    | A list of regex patterns used to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: None |
| `start_step`      | The step from which to start comparing the validation and training<br>loss.<br>**Optional**<br>Valid values: Integer<br>Default value: `0`                                                                                                                                                                                                                                                                                                  |
| `patience`        | The number of steps for which the `ratio_threshold` is<br>allowed to exceed the value set before the model is considered to be<br>overfit.<br>**Optional**<br>Valid values: Integer<br>Default value: `1`                                                                                                                                                                                                                                   |
| `ratio_threshold` | The maximum ratio of the difference between the mean validation<br>loss and mean training loss to the mean training loss. If this<br>threshold is exceeded for a `patience` number of steps,<br>the model is being overfit and the rule returns<br>`True`.<br>**Optional**<br>Valid values: Float<br>Default value: `0.1`                                                                                                                   |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`overfit`(),
        rule_parameters={
                "tensor_regex": "`.*`",
                "start_step": "`0`",
                "patience": "`1`",
                "ratio_threshold": "`0.1`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`losses`",
                parameters={
                    "train.save_interval": "`100`",
                    "eval.save_interval": "`10`"
                }
            )
        ]
    )
]
```

## Overtraining

This rule detects if a model is being overtrained. After a number of training
iterations on a well-behaved model (both training and validation loss decrease), the
model approaches to a minimum of the loss function and does not improve anymore. If the
model continues training it can happen that validation loss starts increasing, because
the model starts overfitting. This rule sets up thresholds and conditions to determine
if the model is not improving, and prevents overfitting problems due to
overtraining.

This rule can be applied either to one of the supported deep learning frameworks
(TensorFlow, MXNet, and PyTorch) or to the XGBoost algorithm.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

###### Note

Overtraining can be avoided by early stopping. For information on early stopping,
see [Stop Training Jobs Early](automatic-model-tuning-early-stopping.md "automatic-model-tuning-early-stopping.md"). For an example that
shows how to use spot training with Debugger, see [Enable Spot Training with Amazon SageMaker Debugger](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/mxnet_spot_training/mxnet-spot-training-with-sagemakerdebugger.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/mxnet_spot_training/mxnet-spot-training-with-sagemakerdebugger.html").

Parameter Descriptions for the Overtraining Rule

| Parameter Name        | Description                                                                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`          | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String |
| `patience_train`      | The number of steps to wait before the training loss is considered<br>to not to be improving anymore.<br>**Optional**<br>Valid values: Integer<br>Default value: `5`       |
| `patience_validation` | The number of steps to wait before the validation loss is considered<br>to not to be improving anymore.**Optional**Valid values:<br>IntegerDefault value: `10`             |
| `delta`               | The minimum threshold by how much the error should improve before<br>it is considered as a new optimum.<br>**Optional**<br>Valid values: Float<br>Default value: `0.01`    |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`overtraining`(),
        rule_parameters={
                "patience_train": "`5`",
                "patience_validation": "`10`",
                "delta": "`0.01`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`losses`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

## SimilarAcrossRuns

This rule compares tensors gathered from a base trial with tensors from another trial.

This rule can be applied either to one of the supported deep learning frameworks
(TensorFlow, MXNet, and PyTorch) or to the XGBoost algorithm.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the SimilarAcrossRuns Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                  |
| `other_trials`     | A completed training job name whose tensors you want to compare to<br>those tensors gathered from the current<br>`base_trial`.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                      |
| `collection_names` | The list of collection names whose tensors the rule<br>inspects.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: None                                                                                                                                                                                                                                                                        |
| `tensor_regex`     | A list of regex patterns used to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: None |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`similar_across_runs`(),
        rule_parameters={
                "other_trials": "`<specify-another-job-name>`",
                "collection_names": "`losses`",
                "tensor_regex": "`.*`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`losses`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

## StalledTrainingRule

StalledTrainingRule detects if there is no progress made on training job, and stops
the training job if the rule fires. This rule requires tensors to be periodically saved
in a time interval defined by its `threshold` parameter. This rule keeps on
monitoring for new tensors, and if no new tensor has been emitted for threshold interval
rule gets fired.

Parameter Descriptions for the StalledTrainingRule Rule

| Parameter Name             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`               | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                                      |
| `threshold`                | A threshold that defines by how much time in seconds the rule<br>waits for a tensor output until it fires a stalled training issue.<br>Default value is 1800 seconds.<br>**Optional**<br>Valid values: Integer<br>Default value: `1800`                                                                                                                                                                                                                         |
| `stop_training_on_fire`    | If set to `True`, watches if the base training job<br>outputs tensors in "`threshold`" seconds.<br>**Optional**<br>Valid values: Boolean<br>Default value: `False`                                                                                                                                                                                                                                                                                              |
| `training_job_name_prefix` | The prefix of base training job name. If<br>`stop_training_on_fire` is true, the rule searches<br>for SageMaker training jobs with this prefix in the same account. If<br>there is an inactivity found, the rule takes a<br>`StopTrainingJob` action. Note if there are multiple<br>jobs found with same prefix, the rule skips termination. It is<br>important that the prefix is set unique per each training<br>job.<br>**Optional**<br>Valid values: String |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`stalled_training_rule`(),
        rule_parameters={
                "threshold": "`1800`",
                "stop_training_on_fire": "`True`",
                "training_job_name_prefix": "`<specify-training-base-job-name>`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`losses`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

## TensorVariance

This rule detects if you have tensors with very high or low variances. Very high or
low variances in a tensor could lead to neuron saturation, which reduces the learning
ability of the neural network. Very high variance in tensors can also eventually lead to
exploding tensors. Use this rule to detect such issues early.

This rule can be applied either to one of the supported deep learning frameworks
(TensorFlow, MXNet, and PyTorch) or to the XGBoost algorithm. You must specify either
the `collection_names` or `tensor_regex` parameter. If both the
parameters are specified, the rule inspects the union of tensors from both sets.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the TensorVariance Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                  |
| `collection_names` | The list of collection names whose tensors the rule<br>inspects.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: None                                                                                                                                                                                                                                                                        |
| `tensor_regex`     | A list of regex patterns used to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: None |
| `max_threshold`    | The threshold for the upper bound of tensor variance.<br>**Optional**<br>Valid values: Float<br>Default value: None                                                                                                                                                                                                                                                                                                                         |
| `min_threshold`    | The threshold for the lower bound of tensor variance.<br>**Optional**<br>Valid values: Float<br>Default value: None                                                                                                                                                                                                                                                                                                                         |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`tensor_variance`(),
        rule_parameters={
                "collection_names": "`weights`",
                "max_threshold": "`10`",
                "min_threshold": "`0.00001`",
        },
        collections_to_save=[
            CollectionConfig(
                name="`weights`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

## UnchangedTensor

This rule detects whether a tensor is no longer changing across steps.

This rule runs the [numpy.allclose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html "https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html") method to check if the tensor isn't changing.

This rule can be applied either to one of the supported deep learning frameworks
(TensorFlow, MXNet, and PyTorch) or to the XGBoost algorithm. You must specify either
the `collection_names` or `tensor_regex` parameter. If both the
parameters are specified, the rule inspects the union of tensors from both sets.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the UnchangedTensor Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                                                                     |
| `collection_names` | The list of collection names whose tensors the rule<br>inspects.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: None                                                                                                                                                                                                                                                                                                                           |
| `tensor_regex`     | A list of regex patternsused to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: None                                                     |
| `num_steps`        | The number of steps across which the rule checks to determine if<br>the tensor has changed.<br>This checks the last `num_steps` that are available.<br>They don't need to be consecutive. If `num_steps` is 2,<br>at step s it doesn't necessarily check for s-1 and s. If s-1 isn't<br>available, it checks the last available step along with s. In that<br>case, it checks the last available step with the current<br>step.<br>**Optional**<br>Valid values: Integer<br>Default value: `3` |
| `rtol`             | The relative tolerance parameter to be passed to the `numpy.allclose` method.<br>**Optional**<br>Valid values: Float<br>Default value: `1e-05`                                                                                                                                                                                                                                                                                                                                                 |
| `atol`             | The absolute tolerance parameter to be passed to the `numpy.allclose` method.<br>**Optional**<br>Valid values: Float<br>Default value: `1e-08`                                                                                                                                                                                                                                                                                                                                                 |
| `equal_nan`        | Whether to compare NaNs as equal. If `True`, NaNs in<br>input array a are considered equal to NaNs in input array b in the<br>output array. This parameter is passed to the `numpy.allclose` method.<br>**Optional**<br>Valid values: Boolean<br>Default value: `False`                                                                                                                                                                                                                        |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`unchanged_tensor`(),
        rule_parameters={
                "collection_names": "`losses`",
                "tensor_regex": "",
                "num_steps": "`3`",
                "rtol": "`1e-05`",
                "atol": "`1e-08`",
                "equal_nan": "`False`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`losses`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

## CheckInputImages

This rule checks if input images have been correctly normalized. Specifically, it
detects if the mean of the sample data differs by more than a threshold value from zero.
Many computer vision models require that input data has a zero mean and unit
variance.

This rule is applicable to deep learning applications.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the CheckInputImages Rule

| Parameter Name      | Description                                                                                                                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`        | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                         |
| `threshold_mean`    | A threshold that defines by how much mean of the input data can<br>differ from 0.<br>**Optional**<br>Valid values: Float<br>Default value: `0.2`                                                                                   |
| `threshold_samples` | The number of images that have to be sampled before an error can<br>be thrown. If the value is too low, the estimation of the dataset<br>mean will be inaccurate.<br>**Optional**<br>Valid values: Integer<br>Default value: `500` |
| `regex`             | The name of the input data tensor.<br>**Optional**<br>Valid values: String<br>Default value: `".*hybridsequential0_input_0"` (the<br>name of the input tensor for Apache MXNet models using<br>HybridSequential)                   |
| `channel`           | The position of the color channel in the input tensor shape array.<br>**Optional**<br>Valid values: Integer<br>Default value: `1` (for example, MXNet expects input<br>data in the form of (batch_size, channel, height, width))   |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`check_input_images`(),
        rule_parameters={
                "`threshold_mean`": "`0.2`",
                "`threshold_samples`": "`500`",
                "`regex`": "`.*hybridsequential0_input_0`",
                "`channel`": "`1`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`custom_inputs_collection`",
                parameters={
                    "`include_regex`": "`.*hybridsequential0_input_0`",
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

## NLPSequenceRatio

This rule calculates the ratio of specific tokens given the rest of the input sequence
that is useful for optimizing performance. For example, you can calculate the percentage
of padding end-of-sentence (EOS) tokens in your input sequence. If the number of EOS
tokens is too high, an alternate bucketing strategy should be performed. You also can
calculate the percentage of unknown tokens in your input sequence. If the number of
unknown words is too high, an alternate vocabulary could be used.

This rule is applicable to deep learning applications.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the NLPSequenceRatio Rule

| Parameter Name             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `base_trial`               | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                                                                                                                                                     |
| `tensor_regex`             | A list of regex patterns used to restrict this comparison to<br>specific scalar-valued tensors. The rule inspects only the tensors<br>that match the regex patterns specified in the list. If no patterns<br>are passed, the rule compares all tensors gathered in the trials by<br>default. Only scalar-valued tensors can be matched.<br>**Optional**<br>Valid values: List of strings or a comma-separated string<br>Default value: `".*embedding0_input_0"` (assuming an<br>embedding as the initial layer of the network) |
| `token_values`             | A string of a list of the numerical values of the tokens. For<br>example, "3, 0".<br>**Optional**<br>Valid values: Comma-separated string of numerical values<br>Default value: `0`                                                                                                                                                                                                                                                                                                                                            |
| `token_thresholds_percent` | A string of a list of thresholds (in percentages) that correspond<br>to each of the `token_values`. For example,"50.0,<br>50.0".<br>**Optional**<br>Valid values: Comma-separated string of floats<br>Default value: `"50"`                                                                                                                                                                                                                                                                                                    |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`nlp_sequence_ratio`(),
        rule_parameters={
                "tensor_regex": "`.*embedding0_input_0`",
                "token_values": "`0`",
                "token_thresholds_percent": "`50`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`custom_inputs_collection`",
                parameters={
                    "`include_regex`": "``.*embedding0_input_0``"
                }
            )
        ]
    )
]
```

## Confusion

This rule evaluates the goodness of a confusion matrix for a classification
problem.

It creates a matrix of size `category_no*category_no` and populates it with
data coming from (`labels`, `predictions`) pairs. For each
(`labels`, `predictions`) pair, the count in
`confusion[labels][predictions]` is incremented by 1. When the matrix is
fully populated, the ratio of data on-diagonal values and off-diagonal values are
evaluated as follows:

- For elements on the diagonal:
  `confusion[i][i]/sum_j(confusion[j][j])>=min_diag`
- For elements off the diagonal:
  `confusion[j][i])/sum_j(confusion[j][i])<=max_off_diag`

This rule can be applied to the XGBoost algorithm.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the Confusion Rule

| Parameter Name           | Description                                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`             | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String |
| `category_no`            | The number of categories.<br>**Optional**<br>Valid values: Integer ≥2<br>Default value: `"None"`                                                                           |
| `labels`                 | The `labels` tensor collection or an 1-d vector of true<br>labels.<br>**Optional**<br>Valid values: String<br>Default value: `"labels"`                                    |
| `predictions`            | The `predictions` tensor collection or an 1-d vector of<br>estimated labels.<br>**Optional**<br>Valid values: String<br>Default value: `"predictions"`                     |
| `labels_collection`      | The rule inspects the tensors in this collection for<br>`labels`.<br>**Optional**<br>Valid values: String<br>Default value: `"labels"`                                     |
| `predictions_collection` | The rule inspects the tensors in this collection for<br>`predictions`.<br>**Optional**<br>Valid values: String<br>Default value: `"predictions"`                           |
| `min_diag`               | The minimum threshold for the ratio of data on the<br>diagonal.<br>**Optional**<br>Valid values: `0`≤float≤`1`<br>Default value: `0.9`                                     |
| `max_off_diag`           | The maximum threshold for the ratio of data off the<br>diagonal.<br>**Optional**<br>Valid values: `0`≤float≤`1`<br>Default value: `0.1`                                    |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`confusion`(),
        rule_parameters={
                "category_no": "`10`",
                "labels": "`labels`",
                "predictions": "`predictions`",
                "labels_collection": "`labels`",
                "predictions_collection": "`predictions`",
                "min_diag": "`0.9`",
                "max_off_diag": "`0.1`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`labels`",
                parameters={
                    "save_interval": "`500`"
                }
            ),
            CollectionConfig(
                name="`predictions`",
                parameters={
                    "include_regex": "`500`"
                }
            )
        ]
    )
]
```

###### Note

This rule infers default values for the optional parameters if their values aren't
specified.

## FeatureImportanceOverweight

This rule accumulates the weights of the n largest feature importance values per step
and ensures that they do not exceed the threshold. For example, you can set the
threshold for the top 3 features to not hold more than 80 percent of the total weights
of the model.

This rule is valid only for the XGBoost algorithm.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the FeatureImportanceOverweight Rule

| Parameter Name | Description                                                                                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `base_trial`   | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                               |
| `threshold`    | Defines the threshold for the proportion of the cumulative sum of<br>the `n` largest features. The number `n` is<br>defined by the `nfeatures` parameter.<br>**Optional**<br>Valid values: Float<br>Default value: `0.8` |
| `nfeatures`    | The number of largest features.<br>**Optional**<br>Valid values: Integer<br>Default value: `3`                                                                                                                           |
| `tensor_regex` | Regular expression (regex) of tensor names the rule to<br>analyze.<br>**Optional**<br>Valid values: String<br>Default value: `".*feature_importance/weight"`                                                             |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`feature_importance_overweight`(),
        rule_parameters={
                "threshold": "`0.8`",
                "nfeatures": "`3`",
                "tensor_regex": "`.*feature_importance/weight`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`feature_importance`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```

## TreeDepth

This rule measures the depth of trees in an XGBoost model. XGBoost rejects splits if
they do not improve loss. This regularizes the training. As a result, the tree might not
grow as deep as defined by the `depth` parameter.

This rule is valid only for the XGBoost algorithm.

For an example of how to configure and deploy a built-in rule, see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md").

Parameter Descriptions for the TreeDepth Rule

| Parameter Name | Description                                                                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`   | The base trial training job name. This parameter is automatically<br>set to the current training job by Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String         |
| `depth`        | The depth of the tree. The depth of the tree is obtained by<br>computing the base 2 logarithm of the largest node ID.<br>**Optional**<br>Valid values: Float<br>Default value: `4` |

```
built_in_rules = [
    Rule.sagemaker(
        base_config=rule_configs.`tree_depth`(),
        rule_parameters={
                "`depth`": "`4`"
        },
        collections_to_save=[
            CollectionConfig(
                name="`tree`",
                parameters={
                    "`save_interval`": "`500`"
                }
            )
        ]
    )
]
```
