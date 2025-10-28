# AwsStepFunctions resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsStepFunctions` resources.

AWS Security Hub normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsStepFunctionStateMachine

The `AwsStepFunctionStateMachine` object provides information about an
AWS Step Functions state machine, which is a workflow consisting of a series of event-driven
steps.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsStepFunctionStateMachine` object. To view descriptions of
`AwsStepFunctionStateMachine` attributes, see [AwsStepFunctionStateMachine](../../1.0/APIReference/API_AwsStepFunctionStateMachineDetails.md "../../1.0/APIReference/API_AwsStepFunctionStateMachineDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsStepFunctionStateMachine": {
    "StateMachineArn": "arn:aws:states:us-east-1:123456789012:stateMachine:StepFunctionsLogDisableNonCompliantResource-fQLujTeXvwsb",
    "Name": "StepFunctionsLogDisableNonCompliantResource-fQLujTeXvwsb",
    "Status": "ACTIVE",
    "RoleArn": "arn:aws:iam::123456789012:role/teststepfunc-StatesExecutionRole-1PNM71RVO1UKT",
    "Type": "STANDARD",
    "LoggingConfiguration": {
        "Level": "OFF",
        "IncludeExecutionData": false
    },
    "TracingConfiguration": {
        "Enabled": false
    }
}
```
