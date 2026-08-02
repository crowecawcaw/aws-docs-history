# Estimator configuration with parameters for basic profiling using the Amazon SageMaker Debugger Python modules

###### Note

End of support notice: On June 30, 2027, AWS will end support for Amazon SageMaker Profiler. After June 30, 2027, you will no longer be able to access the Profiler console or Profiler resources.
For more information, see [Profiler availability change](profiler-availability-change.md "profiler-availability-change.md").

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

## Code template for configuring a SageMaker AI estimator object with the SageMaker Debugger Python modules in the SageMaker AI Python SDK

To adjust the basic profiling configuration (`profiler_config`) or add the
profiler rules (`rules`), use the following template for setting up a SageMaker AI
training job. In the subsequent pages, you can find more information about how to
configure the two parameters.

###### Note

The following code examples are not directly executable. Proceed to the next
sections to learn how to configure each parameter.

```
# An example of creating a training job with profiler configuration
import boto3
from sagemaker.core import image_uris
from sagemaker.core.resources import TrainingJob
from sagemaker.core.shapes import (
    AlgorithmSpecification,
    ResourceConfig,
    OutputDataConfig,
    StoppingCondition,
    ProfilerConfig as CoreProfilerConfig,
    ProfilerRuleConfiguration,
)

session=boto3.session.Session()
region=session.region_name

# Retrieve the training image for your framework
# Change framework to "tensorflow", "mxnet", "xgboost", etc. as needed
training_image = image_uris.retrieve(
    framework="pytorch",  # or "tensorflow", "mxnet", "xgboost"
    region=region,
    version="`1.12.0`",
    py_version="`py37`",
    instance_type="`ml.p3.2xlarge`",
    image_scope="training"
)

`profiler_config`=`CoreProfilerConfig(...)`
`profiler_rule_configurations`=[
    `ProfilerRuleConfiguration(
 rule_configuration_name="BuiltInRule",
 rule_evaluator_image="rule-evaluator-image-uri",
 )`
]

TrainingJob.create(
    training_job_name="`debugger-profiling-demo`",
    algorithm_specification=AlgorithmSpecification(
        training_image=training_image,
        training_input_mode="File",
    ),
    role_arn="`arn:aws:iam::123456789012:role/SageMakerRole`",
    resource_config=ResourceConfig(instance_type="`ml.p3.2xlarge`", instance_count=`1`, volume_size_in_gb=`30`),
    output_data_config=OutputDataConfig(s3_output_path="`s3://bucket/output`"),
    stopping_condition=StoppingCondition(max_runtime_in_seconds=`3600`),

    # SageMaker Debugger parameters
    profiler_config=`profiler_config`,
    profiler_rule_configurations=`profiler_rule_configurations`,
)
```

###### Note

For MXNet and XGBoost, when configuring the `profiler_config`
parameter, you can only configure for system monitoring. Profiling
framework metrics is not supported for MXNet or XGBoost.

The following provides brief descriptions of the parameters.

- `profiler_config` – Configure Debugger to collect system
  metrics and framework metrics from your training job and save into your secured
  S3 bucket URI or local machine. You can set how frequently or loosely collect
  the system metrics. To learn how to configure the `profiler_config`
  parameter, see [Configure settings for basic profiling of system resource utilization](debugger-configure-system-monitoring.md "debugger-configure-system-monitoring.md") and [Estimator configuration for framework profiling](debugger-configure-framework-profiling.md "debugger-configure-framework-profiling.md").
- `rules` – Configure this parameter to activate SageMaker Debugger
  built-in rules that you want to run in parallel. Make sure that your training
  job has access to this S3 bucket. The rules runs on processing containers and
  automatically analyze your training job to find computational and operational
  performance issues. The [ProfilerReport](debugger-built-in-profiler-rules.md#profiler-report "debugger-built-in-profiler-rules.md#profiler-report")
  rule is the most integrated rule that runs all
  built-in profiling rules and saves the profiling results as a report into your
  secured S3 bucket. To learn how to configure the `rules` parameter,
  see [Use built-in profiler rules managed by Amazon SageMaker Debugger](use-debugger-built-in-profiler-rules.md "use-debugger-built-in-profiler-rules.md").

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

- [Configure settings for basic profiling of system resource utilization](debugger-configure-system-monitoring.md "debugger-configure-system-monitoring.md")
- [Estimator configuration for framework profiling](debugger-configure-framework-profiling.md "debugger-configure-framework-profiling.md")
- [Updating Debugger system monitoring and framework profiling configuration while a training job is running](debugger-update-monitoring-profiling.md "debugger-update-monitoring-profiling.md")
- [Turn off Debugger](debugger-turn-off-profiling.md "debugger-turn-off-profiling.md")
