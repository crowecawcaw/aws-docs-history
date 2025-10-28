# Creating custom rules using the Debugger client

library

You can create custom rules to monitor your training job using the Debugger rule APIs and
the open source [`smdebug` Python library](https://github.com/awslabs/sagemaker-debugger/ "https://github.com/awslabs/sagemaker-debugger/") that provide tools to build your own
rule containers.

## Prerequisites for creating a custom

rule

To create Debugger custom rules, you need the following prerequisites.

- [SageMaker Debugger Rule.custom API](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.Rule.custom "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.Rule.custom")
- [The open source smdebug Python
  library](https://github.com/awslabs/sagemaker-debugger/ "https://github.com/awslabs/sagemaker-debugger/")
- Your own custom rule python script
- [Amazon SageMaker Debugger image URIs for custom rule
  evaluators](debugger-reference.md#debuger-custom-rule-registry-ids "debugger-reference.md#debuger-custom-rule-registry-ids")

###### Topics

- [Use the smdebug
  client library to create a custom rule as a Python script](debugger-custom-rules-python-script.md "debugger-custom-rules-python-script.md")
- [Use the Debugger APIs to run your own
  custom rules](debugger-custom-rules-python-sdk.md "debugger-custom-rules-python-sdk.md")
