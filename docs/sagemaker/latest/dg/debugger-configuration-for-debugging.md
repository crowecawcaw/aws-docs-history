# Launch training jobs with Debugger

using the SageMaker Python SDK

To configure a SageMaker AI estimator with SageMaker Debugger, use [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") and
specify Debugger-specific parameters. To fully utilize the debugging functionality, there are
three parameters you need to configure: `debugger_hook_config`,
`tensorboard_output_config`, and `rules`.

###### Important

Before constructing and running the estimator fit method to launch a training job,
make sure that you adapt your training script following the instructions at [Adapting your training script to register a
hook](debugger-modify-script.md "debugger-modify-script.md").

## Constructing a SageMaker AI Estimator with

Debugger-specific parameters

The code examples in this section show how to construct a SageMaker AI estimator with the
Debugger-specific parameters.

###### Note

The following code examples are templates for constructing the SageMaker AI framework estimators
and not directly executable. You need to proceed to the next sections and configure
the Debugger-specific parameters.

PyTorch

```
# An example of constructing a SageMaker AI PyTorch estimator
import boto3
import sagemaker
from sagemaker.pytorch import PyTorch
from sagemaker.debugger import CollectionConfig, DebuggerHookConfig, Rule, rule_configs

session=boto3.session.Session()
region=session.region_name

`debugger_hook_config`=`DebuggerHookConfig(...)`
`rules`=[
    `Rule.sagemaker(rule_configs.built_in_rule())`
]

estimator=PyTorch(
    entry_point="`directory/to/your_training_script.py`",
    role=sagemaker.get_execution_role(),
    base_job_name="`debugger-demo`",
    instance_count=`1`,
    instance_type="`ml.p3.2xlarge`",
    framework_version="`1.12.0`",
    py_version="`py37`",

    # Debugger-specific parameters
    debugger_hook_config=`debugger_hook_config`,
    rules=`rules`
)

estimator.fit(wait=False)
```

TensorFlow

```
# An example of constructing a SageMaker AI TensorFlow estimator
import boto3
import sagemaker
from sagemaker.tensorflow import TensorFlow
from sagemaker.debugger import CollectionConfig, DebuggerHookConfig, Rule, rule_configs

session=boto3.session.Session()
region=session.region_name

`debugger_hook_config`=`DebuggerHookConfig(...)`
`rules`=[
    `Rule.sagemaker(rule_configs.built_in_rule())`,
    `ProfilerRule.sagemaker(rule_configs.BuiltInRule())`
]

estimator=TensorFlow(
    entry_point="`directory/to/your_training_script.py`",
    role=sagemaker.get_execution_role(),
    base_job_name="`debugger-demo`",
    instance_count=`1`,
    instance_type="`ml.p3.2xlarge`",
    framework_version="`2.9.0`",
    py_version="`py39`",

    # Debugger-specific parameters
    debugger_hook_config=`debugger_hook_config`,
    rules=`rules`
)

estimator.fit(wait=False)
```

MXNet

```
# An example of constructing a SageMaker AI MXNet estimator
import sagemaker
from sagemaker.mxnet import MXNet
from sagemaker.debugger import CollectionConfig, DebuggerHookConfig, Rule, rule_configs

`debugger_hook_config`=`DebuggerHookConfig(...)`
`rules`=[
    `Rule.sagemaker(rule_configs.built_in_rule())`
]

estimator=MXNet(
    entry_point="`directory/to/your_training_script.py`",
    role=sagemaker.get_execution_role(),
    base_job_name="`debugger-demo`",
    instance_count=`1`,
    instance_type="`ml.p3.2xlarge`",
    framework_version="`1.7.0`",
    py_version="`py37`",

    # Debugger-specific parameters
    debugger_hook_config=`debugger_hook_config`,
    rules=`rules`
)

estimator.fit(wait=False)
```

XGBoost

```
# An example of constructing a SageMaker AI XGBoost estimator
import sagemaker
from sagemaker.xgboost.estimator import XGBoost
from sagemaker.debugger import CollectionConfig, DebuggerHookConfig, Rule, rule_configs

`debugger_hook_config`=`DebuggerHookConfig(...)`
`rules`=[
    `Rule.sagemaker(rule_configs.built_in_rule())`
]

estimator=XGBoost(
    entry_point="`directory/to/your_training_script.py`",
    role=sagemaker.get_execution_role(),
    base_job_name="`debugger-demo`",
    instance_count=`1`,
    instance_type="`ml.p3.2xlarge`",
    framework_version="`1.5-1`",

    # Debugger-specific parameters
    debugger_hook_config=`debugger_hook_config`,
    rules=`rules`
)

estimator.fit(wait=False)
```

Generic estimator

```
# An example of constructing a SageMaker AI generic estimator using the XGBoost algorithm base image
import boto3
import sagemaker
from sagemaker.estimator import Estimator
from sagemaker import image_uris
from sagemaker.debugger import CollectionConfig, DebuggerHookConfig, Rule, rule_configs

`debugger_hook_config`=`DebuggerHookConfig(...)`
`rules`=[
    `Rule.sagemaker(rule_configs.built_in_rule())`
]

region=boto3.Session().region_name
xgboost_container=sagemaker.image_uris.retrieve("xgboost", region, "1.5-1")

estimator=Estimator(
    role=sagemaker.get_execution_role()
    image_uri=xgboost_container,
    base_job_name="`debugger-demo`",
    instance_count=`1`,
    instance_type="`ml.m5.2xlarge`",

    # Debugger-specific parameters
    debugger_hook_config=`debugger_hook_config`,
    rules=`rules`
)

estimator.fit(wait=False)
```

Configure the following parameters to activate SageMaker Debugger:

- `debugger_hook_config` (an object of [`DebuggerHookConfig`](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DebuggerHookConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DebuggerHookConfig")) – Required to activate
  the hook in the adapted training script during [Adapting your training script to register a
  hook](debugger-modify-script.md "debugger-modify-script.md"), configure the SageMaker training
  launcher (estimator) to collect output tensors from your training job, and save
  the tensors into your secured S3 bucket or local machine. To learn how to
  configure the `debugger_hook_config` parameter, see [Configuring SageMaker Debugger to save
  tensors](debugger-configure-hook.md "debugger-configure-hook.md").
- `rules` (a list of [`Rule`](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.Rule "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.Rule") objects) – Configure this parameter to
  activate SageMaker Debugger built-in rules that you want to run in real time. The
  built-in rules are logics that automatically debug the training progress of your
  model and find training issues by analyzing the output tensors saved in your
  secured S3 bucket. To learn how to configure the `rules` parameter,
  see [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md"). To find a complete list of
  built-in rules for debugging output tensors, see [Debugger rule](debugger-built-in-rules.md#debugger-built-in-rules-Rule "debugger-built-in-rules.md#debugger-built-in-rules-Rule"). If you want to create your own
  logic to detect any training issues, see [Creating custom rules using the Debugger client
  library](debugger-custom-rules.md "debugger-custom-rules.md").

###### Note

The built-in rules are available only through SageMaker training
instances. You cannot use them in local mode.

- `tensorboard_output_config` (an object of [`TensorBoardOutputConfig`](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.TensorBoardOutputConfig "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.TensorBoardOutputConfig")) – Configure
  SageMaker Debugger to collect output tensors in the TensorBoard-compatible format
  and save to your S3 output path specified in the
  `TensorBoardOutputConfig` object. To learn more, see [Visualize Amazon SageMaker Debugger output tensors in
  TensorBoard](debugger-enable-tensorboard-summaries.md "debugger-enable-tensorboard-summaries.md").

###### Note

The `tensorboard_output_config` must be configured with the
`debugger_hook_config` parameter, which also requires you to
adapt your training script by adding the `sagemaker-debugger`
hook.

###### Note

SageMaker Debugger securely saves output tensors in subfolders of your S3 bucket. For
example, the format of the default S3 bucket URI in your account is
`s3://amzn-s3-demo-bucket-sagemaker-<region>-<12digit_account_id>/<base-job-name>/<debugger-subfolders>/`.
There are two subfolders created by SageMaker Debugger: `debug-output`, and
`rule-output`. If you add the `tensorboard_output_config`
parameter, you'll also find `tensorboard-output` folder.

See the following topics to find more examples of how to configure the Debugger-specific
parameters in detail.

###### Topics

- [Configuring SageMaker Debugger to save
  tensors](debugger-configure-hook.md "debugger-configure-hook.md")
- [How to configure Debugger built-in rules](use-debugger-built-in-rules.md "use-debugger-built-in-rules.md")
- [Turn off Debugger](debugger-turn-off.md "debugger-turn-off.md")
- [Useful SageMaker AI estimator class methods
  for Debugger](debugger-estimator-classmethods.md "debugger-estimator-classmethods.md")
