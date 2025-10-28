# Use built-in profiler rules managed

by Amazon SageMaker Debugger

The Amazon SageMaker Debugger built-in profiler rules analyze system metrics and framework operations
collected during the training of a model. Debugger offers the `ProfilerRule` API
operation that helps configure the rules to monitor training compute resources and
operations and to detect anomalies. For example, the profiling rules can help you detect
whether there are computational problems such as CPU bottlenecks, excessive I/O wait time,
imbalanced workload across GPU workers, and compute resource underutilization. To see a full
list of available built-in profiling rules, see [List of Debugger built-in profiler
rules](debugger-built-in-profiler-rules.md "debugger-built-in-profiler-rules.md"). The following topics show how to use
the Debugger built-in rules with default parameter settings and custom parameter
values.

###### Note

The built-in rules are provided through Amazon SageMaker processing containers and fully
managed by SageMaker Debugger at no additional cost. For more information about billing, see
the [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/")
page.

###### Topics

- [Use SageMaker Debugger
  built-in profiler rules with their default parameter settings](#debugger-built-in-profiler-rules-configuration "#debugger-built-in-profiler-rules-configuration")
- [Use Debugger
  built-in profiler rules with custom parameter values](#debugger-built-in-profiler-rules-configuration-param-change "#debugger-built-in-profiler-rules-configuration-param-change")

## Use SageMaker Debugger

built-in profiler rules with their default parameter settings

To add SageMaker Debugger built-in rules in your estimator, you need to configure a
`rules` list object. The following example code shows the basic structure
of listing the SageMaker Debugger built-in rules.

```
from sagemaker.debugger import Rule, ProfilerRule, rule_configs

rules=[
    ProfilerRule.sagemaker(rule_configs.`BuiltInProfilerRuleName_1`()),
    ProfilerRule.sagemaker(rule_configs.`BuiltInProfilerRuleName_2`()),
    ...
    ProfilerRule.sagemaker(rule_configs.`BuiltInProfilerRuleName_n`()),
    ... # You can also append more debugging rules in the Rule.sagemaker(rule_configs.*()) format.
]

estimator=Estimator(
    ...
    rules=rules
)
```

For a complete list of available built-in rules, see [List of Debugger built-in profiler
rules](debugger-built-in-profiler-rules.md "debugger-built-in-profiler-rules.md").

To use the profiling rules and inspect the computational performance and progress of
your training job, add the [`ProfilerReport`](debugger-built-in-profiler-rules.md#profiler-report "debugger-built-in-profiler-rules.md#profiler-report") rule of SageMaker Debugger. This rule activates
all built-in rules under the [Debugger ProfilerRule](debugger-built-in-profiler-rules.md#debugger-built-in-profiler-rules-ProfilerRule "debugger-built-in-profiler-rules.md#debugger-built-in-profiler-rules-ProfilerRule")
`ProfilerRule` family. Furthermore, this rule generates an aggregated
profiling report. For more information, see [Profiling Report Generated Using SageMaker Debugger](debugger-profiling-report.md "debugger-profiling-report.md"). You can use the following
code to add the profiling report rule to your training estimator.

```
from sagemaker.debugger import Rule, rule_configs

rules=[
    ProfilerRule.sagemaker(rule_configs.`ProfilerReport`())
]
```

When you start the training job with the `ProfilerReport` rule, Debugger
collects resource utilization data every 500 milliseconds. Debugger analyzes the resource
utilization to identify if your model is having bottleneck problems. If the rules detect
training anomalies, the rule evaluation status changes to `IssueFound`. You
can set up automated actions, such as notifying training issues and stopping training
jobs using Amazon CloudWatch Events and AWS Lambda. For more information, see [Action on Amazon SageMaker Debugger rules](debugger-action-on-rules.md "debugger-action-on-rules.md").

## Use Debugger

built-in profiler rules with custom parameter values

If you want to adjust the built-in rule parameter values and customize tensor
collection regex, configure the `base_config` and
`rule_parameters` parameters for the `ProfilerRule.sagemaker`
and `Rule.sagemaker` class methods. In case of the
`Rule.sagemaker` class methods, you can also customize tensor collections
through the `collections_to_save` parameter. For instruction on how to use
the `CollectionConfig` class, see [Configure tensor collections
using the CollectionConfig API](debugger-configure-tensor-collections.md "debugger-configure-tensor-collections.md").

Use the following configuration template for built-in rules to customize parameter
values. By changing the rule parameters as you want, you can adjust the sensitivity of
the rules to be initiated.

- The `base_config` argument is where you call the built-in rule
  methods.
- The `rule_parameters` argument is to adjust the default key values
  of the built-in rules listed in [List of Debugger built-in profiler
  rules](debugger-built-in-profiler-rules.md "debugger-built-in-profiler-rules.md").

For more information about the Debugger rule class, methods, and parameters, see [SageMaker AI
Debugger Rule class](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html") in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

```
from sagemaker.debugger import Rule, ProfilerRule, rule_configs, CollectionConfig

rules=[
    ProfilerRule.sagemaker(
        base_config=rule_configs.`BuiltInProfilerRuleName`(),
        rule_parameters={
                "`key`": "`value`"
        }
    )
]
```

The parameter descriptions and value customization examples are provided for each rule
at [List of Debugger built-in profiler
rules](debugger-built-in-profiler-rules.md "debugger-built-in-profiler-rules.md").

For a low-level JSON configuration of the Debugger built-in rules using the
`CreateTrainingJob` API, see [Configure Debugger using SageMaker API](debugger-createtrainingjob-api.md "debugger-createtrainingjob-api.md").
