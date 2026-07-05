# Creating custom rules using the Debugger client library

###### Note

After careful consideration, we have made the decision to close new customer access to Amazon Sagemaker Debugger, effective 7/30/26.
Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for
Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md "debugger-availability-change.md").

You can create custom rules to monitor your training job using the Debugger rule APIs and
the open source [`smdebug` Python library](https://github.com/awslabs/sagemaker-debugger/ "https://github.com/awslabs/sagemaker-debugger/") that provide tools to build your own
rule containers.

## Prerequisites for creating a custom rule

To create Debugger custom rules, you need the following prerequisites.

- [SageMaker Debugger Rule.custom API](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.Rule.custom "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.Rule.custom")
- [The open source smdebug Python
  library](https://github.com/awslabs/sagemaker-debugger/ "https://github.com/awslabs/sagemaker-debugger/")
- Your own custom rule python script
- [Amazon SageMaker Debugger image URIs for custom rule evaluators](debugger-reference.md#debuger-custom-rule-registry-ids "debugger-reference.md#debuger-custom-rule-registry-ids")

###### Topics

- [Use the smdebug client library to create a custom rule as a Python script](debugger-custom-rules-python-script.md "debugger-custom-rules-python-script.md")
- [Use the Debugger APIs to run your own custom rules](debugger-custom-rules-python-sdk.md "debugger-custom-rules-python-sdk.md")
