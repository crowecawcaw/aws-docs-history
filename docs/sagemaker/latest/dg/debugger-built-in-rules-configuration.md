# Use Debugger built-in rules with

the default parameter settings

To specify Debugger built-in rules in an estimator, you need to configure a list object.
The following example code shows the basic structure of listing the Debugger built-in
rules:

```
from sagemaker.debugger import Rule, rule_configs

rules=[
    Rule.sagemaker(rule_configs.`built_in_rule_name_1`()),
    Rule.sagemaker(rule_configs.`built_in_rule_name_2`()),
    ...
    Rule.sagemaker(rule_configs.`built_in_rule_name_n`()),
    ... # You can also append more profiler rules in the ProfilerRule.sagemaker(rule_configs.*()) format.
]
```

For more information about default parameter values and descriptions of the built-in
rule, see [List of Debugger built-in rules](debugger-built-in-rules.md "debugger-built-in-rules.md").

To find the SageMaker Debugger API reference, see [`sagemaker.debugger.rule_configs`](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.sagemaker.debugger.rule_configs "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.sagemaker.debugger.rule_configs") and [`sagemaker.debugger.Rule`](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.Rule "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.Rule").

For example, to inspect the overall training performance and progress of your model,
construct a SageMaker AI estimator with the following built-in rule configuration.

```
from sagemaker.debugger import Rule, rule_configs

rules=[
    Rule.sagemaker(rule_configs.`loss_not_decreasing`()),
    Rule.sagemaker(rule_configs.`overfit`()),
    Rule.sagemaker(rule_configs.`overtraining`()),
    Rule.sagemaker(rule_configs.`stalled_training_rule`())
]
```

When you start the training job, Debugger collects system resource utilization data
every 500 milliseconds and the loss and accuracy values every 500 steps by default.
Debugger analyzes the resource utilization to identify if your model is having
bottleneck problems. The `loss_not_decreasing`, `overfit`,
`overtraining`, and `stalled_training_rule` monitors if your
model is optimizing the loss function without those training issues. If the rules detect
training anomalies, the rule evaluation status changes to `IssueFound`. You
can set up automated actions, such as notifying training issues and stopping training
jobs using Amazon CloudWatch Events and AWS Lambda. For more information, see [Action on Amazon SageMaker Debugger rules](debugger-action-on-rules.md "debugger-action-on-rules.md").
