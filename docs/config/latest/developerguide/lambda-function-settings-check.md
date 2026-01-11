# lambda-function-settings-check

Checks if the AWS Lambda function settings for runtime, role, timeout, and memory size match the expected values. The rule ignores functions with the 'Image' package type
and functions with runtime set to 'OS-only Runtime'.
The rule is NON_COMPLIANT if the Lambda function settings do not match the expected values.

**Identifier:** LAMBDA_FUNCTION_SETTINGS_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

runtime
Type: CSV

Comma-separated list of AWS Lambda runtime values

role (Optional)
Type: String

Name or ARN of the AWS Lambda execution role

memorySize (Optional)
Type: int
Default: 128

AWS Lambda function size in megabytes

timeout (Optional)
Type: int
Default: 3

AWS Lambda function timeout in seconds

## Proactive Evaluation

For steps on how to run this rule in proactive mode,
see [Evaluating Your Resources with AWS Config Rules](evaluating-your-resources.md#evaluating-your-resources-proactive "evaluating-your-resources.md#evaluating-your-resources-proactive").
For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](../APIReference/API_StartResourceEvaluation.md "../APIReference/API_StartResourceEvaluation.md") API needs to include the following inputs, encoded as a string:

```
"ResourceConfiguration":
...
{
    "MemorySize": `Integer`\*,
    "Role": `String`\*,
    "Runtime": `String`\*,
    "Timeout": `Integer`\*
}
...

```

\*For more information on valid values for these inputs, see [MemorySize](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-memorysize "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-memorysize"), [Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-role "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-role"), [Runtime](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-runtime "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-runtime"), and [Timeout](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-timeout "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-timeout") in the AWS CloudFormation User Guide.

For more information on proactive evaluation, see [Evaluation Mode](evaluate-config-rules.md "evaluate-config-rules.md").

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
