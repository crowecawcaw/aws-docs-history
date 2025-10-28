# Estimator configuration with

parameters for basic profiling using the Amazon SageMaker Debugger Python modules

By default, SageMaker Debugger basic profiling is on by default and monitors resource utilization
metrics, such as CPU utilization, GPU utilization, GPU memory utilization, Network, and I/O
wait time, of all SageMaker training jobs submitted using the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"). SageMaker Debugger
collects these resource utilization metrics every 500 milliseconds. You don't need to make
any additional changes in your code, training script, or the job launcher for tracking basic
resource utilization. If you want to change the metric collection interval for basic
profiling, you can specify Debugger-specific parameters while creating a SageMaker training job
launcher using the SageMaker Python SDK, AWS SDK for Python (Boto3), or AWS Command Line Interface (CLI). In this guide, we
focus on how to change profiling options using the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"). This page gives
reference templates for configuring this estimator object.

If you want to access the resource utilization metrics dashboard of your training job in
SageMaker Studio, you can jump onto the [Amazon SageMaker Debugger UI in Amazon SageMaker Studio Classic Experiments](debugger-on-studio.md "debugger-on-studio.md").

If you want to activate the rules that detect system resource utilization problems
automatically, you can add the `rules` parameter in the estimator object for
activating the rules.

###### Important

To use the latest SageMaker Debugger features, you need to upgrade the SageMaker Python SDK and
the `SMDebug` client library. In your iPython kernel, Jupyter Notebook, or
JupyterLab environment, run the following code to install the latest versions of the
libraries and restart the kernel.

```
import sys
import IPython
!{sys.executable} -m pip install -U sagemaker smdebug
IPython.Application.instance().kernel.do_shutdown(True)
```

## Code template for

configuring a SageMaker AI estimator object with the SageMaker Debugger Python modules in the SageMaker AI
Python SDK

To adjust the basic profiling configuration (`profiler_config`) or add the
profiler rules (`rules`), choose one of the tabs to get the template for
setting up a SageMaker AI estimator. In the subsequent pages, you can find more information
about how to configure the two parameters.

###### Note

The following code examples are not directly executable. Proceed to the next
sections to learn how to configure each parameter.

PyTorch

```
# An example of constructing a SageMaker AI PyTorch estimator
import boto3
import sagemaker
from sagemaker.pytorch import PyTorch
from sagemaker.debugger import ProfilerConfig, ProfilerRule, rule_configs

session=boto3.session.Session()
region=session.region_name

`profiler_config`=`ProfilerConfig(...)`
`rules`=[
    `ProfilerRule.sagemaker(rule_configs.BuiltInRule())`
]

estimator=PyTorch(
    entry_point="`directory/to/your_training_script.py`",
    role=sagemaker.get_execution_role(),
    base_job_name="`debugger-profiling-demo`",
    instance_count=`1`,
    instance_type="`ml.p3.2xlarge`",
    framework_version="`1.12.0`",
    py_version="`py37`",

    # SageMaker Debugger parameters
    profiler_config=`profiler_config`,
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
from sagemaker.debugger import ProfilerConfig, ProfilerRule, rule_configs

session=boto3.session.Session()
region=session.region_name

`profiler_config`=`ProfilerConfig(...)`
`rules`=[
    `ProfilerRule.sagemaker(rule_configs.BuiltInRule())`
]

estimator=TensorFlow(
    entry_point="`directory/to/your_training_script.py`",
    role=sagemaker.get_execution_role(),
    base_job_name="`debugger-profiling-demo`",
    instance_count=`1`,
    instance_type="`ml.p3.2xlarge`",
    framework_version="`2.8.0`",
    py_version="`py37`",

    # SageMaker Debugger parameters
    profiler_config=`profiler_config`,
    rules=`rules`
)

estimator.fit(wait=False)
```

MXNet

```
# An example of constructing a SageMaker AI MXNet estimator
import sagemaker
from sagemaker.mxnet import MXNet
from sagemaker.debugger import ProfilerConfig, ProfilerRule, rule_configs

`profiler_config`=`ProfilerConfig(...)`
`rules`=[
    `ProfilerRule.sagemaker(rule_configs.BuiltInRule())`
]

estimator=MXNet(
    entry_point="`directory/to/your_training_script.py`",
    role=sagemaker.get_execution_role(),
    base_job_name="`debugger-profiling-demo`",
    instance_count=`1`,
    instance_type="`ml.p3.2xlarge`",
    framework_version="`1.7.0`",
    py_version="`py37`",

    # SageMaker Debugger parameters
    profiler_config=`profiler_config`,
    rules=`rules`
)

estimator.fit(wait=False)
```

###### Note

For MXNet, when configuring the `profiler_config`
parameter, you can only configure for system monitoring. Profiling
framework metrics is not supported for MXNet.

XGBoost

```
# An example of constructing a SageMaker AI XGBoost estimator
import sagemaker
from sagemaker.xgboost.estimator import XGBoost
from sagemaker.debugger import ProfilerConfig, ProfilerRule, rule_configs

`profiler_config`=`ProfilerConfig(...)`
`rules`=[
    `ProfilerRule.sagemaker(rule_configs.BuiltInRule())`
]

estimator=XGBoost(
    entry_point="`directory/to/your_training_script.py`",
    role=sagemaker.get_execution_role(),
    base_job_name="`debugger-profiling-demo`",
    instance_count=`1`,
    instance_type="`ml.p3.2xlarge`",
    framework_version="`1.5-1`",

    # Debugger-specific parameters
    profiler_config=`profiler_config`,
    rules=`rules`
)

estimator.fit(wait=False)
```

###### Note

For XGBoost, when configuring the `profiler_config`
parameter, you can only configure for system monitoring. Profiling
framework metrics is not supported for XGBoost.

Generic estimator

```
# An example of constructing a SageMaker AI generic estimator using the XGBoost algorithm base image
import boto3
import sagemaker
from sagemaker.estimator import Estimator
from sagemaker import image_uris
from sagemaker.debugger import ProfilerConfig, DebuggerHookConfig, Rule, ProfilerRule, rule_configs

`profiler_config`=`ProfilerConfig(...)`
`rules`=[
    `ProfilerRule.sagemaker(rule_configs.BuiltInRule())`
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
    profiler_config=`profiler_config`,
    rules=`rules`
)

estimator.fit(wait=False)
```

The following provides brief descriptions of the parameters.

- `profiler_config` – Configure Debugger to collect system
  metrics and framework metrics from your training job and save into your secured
  S3 bucket URI or local machine. You can set how frequently or loosely collect
  the system metrics. To learn how to configure the `profiler_config`
  parameter, see [Configure settings for basic
  profiling of system resource utilization](debugger-configure-system-monitoring.md "debugger-configure-system-monitoring.md") and [Estimator configuration for
  framework profiling](debugger-configure-framework-profiling.md "debugger-configure-framework-profiling.md").
- `rules` – Configure this parameter to activate SageMaker Debugger
  built-in rules that you want to run in parallel. Make sure that your training
  job has access to this S3 bucket. The rules runs on processing containers and
  automatically analyze your training job to find computational and operational
  performance issues. The [ProfilerReport](debugger-built-in-profiler-rules.md#profiler-report "debugger-built-in-profiler-rules.md#profiler-report")
  rule is the most integrated rule that runs all
  built-in profiling rules and saves the profiling results as a report into your
  secured S3 bucket. To learn how to configure the `rules` parameter,
  see [Use built-in profiler rules managed
  by Amazon SageMaker Debugger](use-debugger-built-in-profiler-rules.md "use-debugger-built-in-profiler-rules.md").

###### Note

Debugger securely saves output data in subfolders of your default S3 bucket. For
example, the format of the default S3 bucket URI is
`s3://sagemaker-<region>-<12digit_account_id>/<base-job-name>/<debugger-subfolders>/`.
There are three subfolders created by Debugger: `debug-output`,
`profiler-output`, and `rule-output`. You can also
retrieve the default S3 bucket URIs using the [SageMaker AI estimator
classmethods](debugger-estimator-classmethods.md "debugger-estimator-classmethods.md").

See the following topics to find out how to configure the Debugger-specific parameters in
detail.

###### Topics

- [Configure settings for basic
  profiling of system resource utilization](debugger-configure-system-monitoring.md "debugger-configure-system-monitoring.md")
- [Estimator configuration for
  framework profiling](debugger-configure-framework-profiling.md "debugger-configure-framework-profiling.md")
- [Updating Debugger system monitoring
  and framework profiling configuration while a training job is running](debugger-update-monitoring-profiling.md "debugger-update-monitoring-profiling.md")
- [Turn off Debugger](debugger-turn-off-profiling.md "debugger-turn-off-profiling.md")
