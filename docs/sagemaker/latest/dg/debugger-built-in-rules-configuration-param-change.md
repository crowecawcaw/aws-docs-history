# Use Debugger built-in

rules with custom parameter values

If you want to adjust the built-in rule parameter values and customize tensor
collection regex, configure the `base_config` and
`rule_parameters` parameters for the `ProfilerRule.sagemaker`
and `Rule.sagemaker` classmethods. In case of the `Rule.sagemaker`
class methods, you can also customize tensor collections through the
`collections_to_save` parameter. The instruction of how to use the
`CollectionConfig` class is provided at [Configure tensor collections
using the CollectionConfig API](debugger-configure-tensor-collections.md "debugger-configure-tensor-collections.md").

Use the following configuration template for built-in rules to customize parameter
values. By changing the rule parameters as you want, you can adjust the sensitivity of
the rules to be triggered.

- The `base_config` argument is where you call the built-in rule
  methods.
- The `rule_parameters` argument is to adjust the default key values
  of the built-in rules listed in [List of Debugger built-in rules](debugger-built-in-rules.md "debugger-built-in-rules.md").
- The `collections_to_save` argument takes in a tensor configuration
  through the `CollectionConfig` API, which requires `name`
  and `parameters` arguments.

      + To find available tensor collections for `name`, see  [Debugger Built-in Tensor Collections](https://github.com/awslabs/sagemaker-debugger/blob/master/docs/api.md#built-in-collections "https://github.com/awslabs/sagemaker-debugger/blob/master/docs/api.md#built-in-collections") .
      + For a full list of adjustable `parameters`, see  [Debugger CollectionConfig API](https://github.com/awslabs/sagemaker-debugger/blob/master/docs/api.md#configuring-collection-using-sagemaker-python-sdk "https://github.com/awslabs/sagemaker-debugger/blob/master/docs/api.md#configuring-collection-using-sagemaker-python-sdk").

  For more information about the Debugger rule class, methods, and parameters, see [SageMaker AI
  Debugger Rule class](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html") in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

```
from sagemaker.debugger import Rule, ProfilerRule, rule_configs, CollectionConfig

rules=[
    Rule.sagemaker(
        base_config=rule_configs.`built_in_rule_name`(),
        rule_parameters={
                "`key`": "`value`"
        },
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

The parameter descriptions and value customization examples are provided for each rule
at [List of Debugger built-in rules](debugger-built-in-rules.md "debugger-built-in-rules.md").
