# List of Debugger built-in profiler

rules

Use the Debugger built-in profiler rules provided by Amazon SageMaker Debugger and analyze metrics collected
while training your models. The Debugger built-in rules monitor various common conditions that
are critical for the success of running a performant training job. You can call the built-in
profiler rules using [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") or the low-level SageMaker API operations. There's no
additional cost for using the built-in rules. For more information about billing, see the
[Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") page.

###### Note

The maximum numbers of built-in profiler rules that you can attach to a training job
is 20. SageMaker Debugger fully manages the built-in rules and analyzes your training job
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

## Profiler rules

The following rules are the Debugger built-in rules that are callable using the
`ProfilerRule.sagemaker` classmethod.

Debugger built-in rule for generating the
profiling report

| Scope of Validity                               | Built-in Rules     |
| ----------------------------------------------- | ------------------ |
| Profiling Report for any SageMaker training job | • `ProfilerReport` |

Debugger built-in rules for profiling hardware
system resource utilization (system metrics)

| Scope of Validity                                              | Built-in Rules                                                                                                                                          |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Generic system monitoring rules for any SageMaker training job | • `BatchSize`<br>• `CPUBottleneck`<br>• `GPUMemoryIncrease`<br>• `IOBottleneck`<br>• `LoadBalancing`<br>• `LowGPUUtilization`<br>• `OverallSystemUsage` |

Debugger built-in rules for profiling framework
metrics

| Scope of Validity                                                     | Built-in Rules                                                              |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Profiling rules for deep learning frameworks (TensorFlow and PyTorch) | • `MaxInitializationTime`<br>• `OverallFrameworkMetrics`<br>• `StepOutlier` |

###### Warning

In favor of [Amazon SageMaker Profiler](train-use-sagemaker-profiler.md "train-use-sagemaker-profiler.md"), SageMaker AI
Debugger deprecates the framework profiling feature starting from TensorFlow 2.11 and
PyTorch 2.0. You can still use the feature in the previous versions of the
frameworks and SDKs as follows.

- SageMaker Python SDK <= v2.130.0
- PyTorch >= v1.6.0, < v2.0
- TensorFlow >= v2.3.1, < v2.11
  See also [March 16, 2023](debugger-release-notes.md#debugger-release-notes-20230315 "debugger-release-notes.md#debugger-release-notes-20230315").

**To use the built-in rules with default parameter values** –
use the following configuration format:

```
from sagemaker.debugger import Rule, ProfilerRule, rule_configs

rules = [
    ProfilerRule.sagemaker(rule_configs.`BuiltInRuleName_1`()),
    ProfilerRule.sagemaker(rule_configs.`BuiltInRuleName_2`()),
    ...
    ProfilerRule.sagemaker(rule_configs.`BuiltInRuleName_n`())
]
```

**To use the built-in rules with customizing the parameter
values** – use the following configuration format:

```
from sagemaker.debugger import Rule, ProfilerRule, rule_configs

rules = [
    ProfilerRule.sagemaker(
        base_config=rule_configs.`BuiltInRuleName`(),
        rule_parameters={
                "`key`": "`value`"
        }
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

## ProfilerReport

The ProfilerReport rule invokes all of the built-in rules for monitoring and
profiling. It creates a profiling report and updates when the individual rules are
triggered. You can download a comprehensive profiling report while a training job is
running or after the training job is complete. You can adjust the rule parameter values
to customize sensitivity of the built-in monitoring and profiling rules. The following
example code shows the basic format to adjust the built-in rule parameters through the
ProfilerReport rule.

```
rules=[
    ProfilerRule.sagemaker(
        rule_configs.`ProfilerReport`(
            `<BuiltInRuleName>`_`<parameter_name>` = `value`
        )
    )
]
```

If you trigger this ProfilerReport rule without any customized parameter as shown in
the following example code, then the ProfilerReport rule triggers all of the built-in
rules for monitoring and profiling with their default parameter values.

```
rules=[ProfilerRule.sagemaker(rule_configs.ProfilerReport())]
```

The following example code shows how to specify and adjust the CPUBottleneck rule's
`cpu_threshold` parameter and the IOBottleneck rule's
`threshold` parameter.

```
rules=[
    ProfilerRule.sagemaker(
        rule_configs.ProfilerReport(
            `CPUBottleneck_cpu_threshold` = `90`,
            `IOBottleneck_threshold` = `90`
        )
    )
]
```

To explore what's in the profiler report, see [SageMaker Debugger Profiling
Report](debugger-profiling-report.md "debugger-profiling-report.md"). Also, because this rule activates all of the profiling rules, you
can also check the rule analysis status using the [SageMaker Debugger UI in SageMaker Studio
Experiments](debugger-on-studio.md "debugger-on-studio.md").

Parameter Descriptions for the OverallSystemUsage Rule

| Parameter Name                       | Description                                                                                                                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`                         | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String |
| `<BuiltInRuleName>_<parameter_name>` | Customizable parameter to adjust thresholds of other built-in<br>monitoring and profiling rules.<br>**Optional**<br>Default value: `None`                                     |

## BatchSize

The BatchSize rule helps detect if GPU is underutilized due to a small batch size. To
detect this issue, this rule monitors the average CPU utilization, GPU utilization, and
GPU memory utilization. If utilization on CPU, GPU, and GPU memory is low on average, it
may indicate that the training job can either run on a smaller instance type or can run
with a bigger batch size. This analysis does not work for frameworks that heavily
overallocate memory. However, increasing the batch size can lead to processing or data
loading bottlenecks because more data preprocessing time is required in each
iteration.

Parameter Descriptions for the BatchSize Rule

| Parameter Name             | Description                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`               | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                  |
| `cpu_threshold_p95`        | Defines the threshold for 95th quantile of CPU utilization<br>in percentage.<br>**Optional**<br>Valid values: Integer<br>Default value: `70` (in percentage)                                                                                                                                                                                                                                   |
| `gpu_threshold_p95`        | Defines the threshold for 95th quantile of GPU utilization<br>in percentage.<br>**Optional**<br>Valid values: Integer<br>Default value: `70` (in percentage)                                                                                                                                                                                                                                   |
| `gpu_memory_threshold_p95` | Defines the threshold for 95th quantile of GPU memory<br>utilization in percentage.<br>**Optional**<br>Valid values: Integer<br>Default values: `70` (in percentage)                                                                                                                                                                                                                           |
| `patience`                 | Defines the number of data points to skip until the rule starts evaluation. The first several<br>steps of training jobs usually show high volume of data processes,<br>so keep the rule patient and prevent it from being invoked too soon<br>with a given number of profiling data that you specify with this<br>parameter.<br>**Optional**<br>Valid values: Integer<br>Default values: `100` |
| `window`                   | Window size for computing quantiles.<br>**Optional**<br>Valid values: Integer<br>Default values:<br>`500`                                                                                                                                                                                                                                                                                      |
| `scan_interval_us`         | Time interval that timeline files are scanned.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                                                                                                                                                                                                                                                     |

## CPUBottleneck

The CPUBottleneck rule helps detect if GPU is underutilized due to CPU
bottlenecks. Rule returns True if number of CPU bottlenecks exceeds a predefined
threshold.

Parameter Descriptions for the CPUBottleneck Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                  |
| `threshold`        | Defines the threshold for proportion of bottlenecked time<br>to the total training time. If the proportion exceeds the<br>percentage specified to the threshold parameter, the rule<br>switches the rule status to True.<br>**Optional**<br>Valid values: Integer<br>Default value: `50` (in percentage)                                                                                       |
| `gpu_threshold`    | A threshold that defines low GPU utilization.<br>**Optional**<br>Valid values: Integer<br>Default value: `10` (in percentage)                                                                                                                                                                                                                                                                  |
| `cpu_threshold`    | A threshold that defines high CPU utilization.<br>**Optional**<br>Valid values: Integer<br>Default values: `90` (in percentage)                                                                                                                                                                                                                                                                |
| `patience`         | Defines the number of data points to skip until the rule starts evaluation. The first several<br>steps of training jobs usually show high volume of data processes,<br>so keep the rule patient and prevent it from being invoked too soon<br>with a given number of profiling data that you specify with this<br>parameter.<br>**Optional**<br>Valid values: Integer<br>Default values: `100` |
| `scan_interval_us` | Time interval with which timeline files are<br>scanned.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                                                                                                                                                                                                                                            |

## GPUMemoryIncrease

The GPUMemoryIncrease rule helps detect a large increase in memory usage on
GPUs.

Parameter Descriptions for the GPUMemoryIncrease Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                  |
| `increase`         | Defines the threshold for absolute memory increase.<br>**Optional**<br>Valid values: Integer<br>Default value: `10` (in percentage)                                                                                                                                                                                                                                                            |
| `patience`         | Defines the number of data points to skip until the rule starts<br>evaluation. The first several steps of training jobs usually show<br>high volume of data processes, so keep the rule patient and prevent<br>it from being invoked too soon with a given number of profiling data<br>that you specify with this parameter.<br>**Optional**<br>Valid values: Integer<br>Default values: `100` |
| `window`           | Window size for computing quantiles.<br>**Optional**<br>Valid values: Integer<br>Default values: `500`                                                                                                                                                                                                                                                                                         |
| `scan_interval_us` | Time interval that timeline files are scanned.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                                                                                                                                                                                                                                                     |

## IOBottleneck

This rule helps to detect if GPU is underutilized due to data IO bottlenecks.
Rule returns True if number of IO bottlenecks exceeds a predefined
threshold.

Parameter Descriptions for the IOBottleneck Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                          |
| `threshold`        | Defines the threshold when Rule to return<br>True.**Optional**Valid values:<br>IntegerDefault value: `50` (in<br>percentage)                                                                                                                                                                                                                                                           |
| `gpu_threshold`    | A threshold that defines when GPU is considered<br>underutilized.<br>**Optional**<br>Valid values: Integer<br>Default value: `70` (in percentage)                                                                                                                                                                                                                                      |
| `io_threshold`     | A threshold that defines high IO wait time.**Optional**Valid<br>values: IntegerDefault values: `50`<br>(in percentage)                                                                                                                                                                                                                                                                 |
| `patience`         | Defines the number of data points to skip until the rule starts<br>evaluation. The first several steps of training jobs usually show high<br>volume of data processes, so keep the rule patient and prevent it from<br>being invoked too soon with a given number of profiling data that you<br>specify with this parameter.**Optional**Valid values:<br>IntegerDefault values: `1000` |
| `scan_interval_us` | Time interval that timeline files are scanned.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                                                                                                                                                                                                                                             |

## LoadBalancing

The LoadBalancing rule helps detect issues in workload balancing among
multiple GPUs.

Parameter Descriptions for the LoadBalancing Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                 |
| `threshold`        | Defines the workload percentage.<br>**Optional**<br>Valid values: Integer<br>Default value: `0.5` (unitless<br>proportion)                                                                                                                                                                                                                                                                    |
| `patience`         | Defines the number of data points to skip until the rule starts<br>evaluation. The first several steps of training jobs usually show<br>high volume of data processes, so keep the rule patient and prevent<br>it from being invoked too soon with a given number of profiling data<br>that you specify with this parameter.<br>**Optional**<br>Valid values: Integer<br>Default values: `10` |
| `scan_interval_us` | Time interval that timeline files are scanned.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                                                                                                                                                                                                                                                    |

## LowGPUUtilization

The LowGPUUtilization rule helps detect if GPU utilization is low or suffers from
fluctuations. This is checked for each GPU on each worker. Rule returns True if 95th
quantile is below threshold_p95 which indicates underutilization. Rule returns true if
95th quantile is above threshold_p95 and 5th quantile is below threshold_p5 which
indicates fluctuations.

Parameter Descriptions for the LowGPUUtilization Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                                                                                                                                   |
| `threshold_p95`    | A threshold for 95th quantile below which GPU is<br>considered to be underutilized.<br>**Optional**<br>Valid values: Integer<br>Default value: `70` (in percentage)                                                                                                                                                                                                                             |
| `threshold_p5`     | A threshold for 5th quantile. Default is 10<br>percent.**Optional**Valid values:<br>IntegerDefault values: `10` (in<br>percentage)                                                                                                                                                                                                                                                              |
| `patience`         | Defines the number of data points to skip until the rule starts<br>evaluation. The first several steps of training jobs usually show<br>high volume of data processes, so keep the rule patient and prevent<br>it from being invoked too soon with a given number of profiling data<br>that you specify with this parameter.<br>**Optional**<br>Valid values: Integer<br>Default values: `1000` |
| `window`           | Window size for computing quantiles.<br>**Optional**<br>Valid values: Integer<br>Default values: `500`                                                                                                                                                                                                                                                                                          |
| `scan_interval_us` | Time interval that timeline files are scanned.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                                                                                                                                                                                                                                                      |

## OverallSystemUsage

The OverallSystemUsage rule measures overall system usage per worker node. The rule currently only aggregates values per node
and computes their percentiles.

Parameter Descriptions for the OverallSystemUsage Rule

| Parameter Name     | Description                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String |
| `scan_interval_us` | Time interval to scan timeline files.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                                             |

## MaxInitializationTime

The MaxInitializationTime rule helps detect if the training initialization is
taking too much time. The rule waits until the first step is available.

Parameter Descriptions for the MaxInitializationTime Rule

| Parameter Name     | Description                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String |
| `threshold`        | Defines the threshold in minutes to wait for the first<br>step to become available.<br>**Optional**<br>Valid values: Integer<br>Default value: `20` (in minutes)              |
| `scan_interval_us` | Time interval with which timeline files are<br>scanned.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                           |

## OverallFrameworkMetrics

The OverallFrameworkMetrics rule summarizes the time spent on framework metrics, such
as forward and backward pass, and data loading.

Parameter Descriptions for the OverallFrameworkMetrics Rule

| Parameter Name     | Description                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String |
| `scan_interval_us` | Time interval to scan timeline files.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                                             |

## StepOutlier

The StepOutlier rule helps detect outliers in step durations. This rule
returns `True` if there are outliers with step durations larger than
`stddev` sigmas of the entire step durations in a time
range.

Parameter Descriptions for the StepOutlier Rule

| Parameter Name     | Description                                                                                                                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base_trial`       | The base trial training job name. This parameter is<br>automatically set to the current training job by<br>Amazon SageMaker Debugger.<br>**Required**<br>Valid values: String                                                                                                 |
| `stddev`           | Defines a factor by which to multiply the standard<br>deviation. For example, the rule is invoked by default when<br>a step duration is larger or smaller than 5 times the<br>standard deviation.<br>**Optional**<br>Valid values: Integer<br>Default value: `5` (in minutes) |
| `mode`             | Mode under which steps have been saved and on which Rule<br>should run on. Per default rule will run on steps from EVAL and<br>TRAIN phase**Optional**Valid values:<br>IntegerDefault value: `5` (in<br>minutes)                                                              |
| `n_outliers`       | How many outliers to ignore before rule returns True**Optional**Valid values:<br>IntegerDefault value: `10`                                                                                                                                                                   |
| `scan_interval_us` | Time interval with which timeline files are<br>scanned.<br>**Optional**<br>Valid values: Integer<br>Default values: `60000000` (in<br>microseconds)                                                                                                                           |
