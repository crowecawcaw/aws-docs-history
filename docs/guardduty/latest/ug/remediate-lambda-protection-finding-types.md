# Remediating a potentially

compromised Lambda function

When GuardDuty generates [Lambda Protection finding types](lambda-protection-finding-types.md "lambda-protection-finding-types.md"), your Lambda function
may be compromised. If the activity that caused GuardDuty to generate this finding was expected, you can consider
using [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md").
We recommend completing the following steps to remediate a compromised Lambda
function:

###### To remediate Lambda Protection findings

1. **Identify the potentially compromised Lambda function
   version**.

A GuardDuty finding for Lambda Protection provides the name, Amazon Resource Name (ARN), function
version, and revision ID associated with the Lambda function listed in the finding
details. 2. **Identify the source of the potentially suspicious
activity**.

    1. Review the code associated with the Lambda function version involved in the finding.
    2. Review the imported libraries and layers of the Lambda function version involved in
     the finding.
    3. If you have enabled [Scanning AWS Lambda functions with
     Amazon Inspector](../../../inspector/latest/user/scanning-lambda.md "../../../inspector/latest/user/scanning-lambda.md"), review the [Amazon Inspector
     findings](../../../inspector/latest/user/findings-understanding-locating-analyzing.md "../../../inspector/latest/user/findings-understanding-locating-analyzing.md") associated with the Lambda function involved in the finding.
    4. Review the AWS CloudTrail logs to identify the principal that caused the function update
     and ensure that the activity was authorized or expected.

3. **Remediate the potentially compromised Lambda
   function**.
   1. Disable the execution triggers of the Lambda function involved in the finding. For
      more information, see [DeleteFunctionEventInvokeConfig](../../../lambda/latest/dg/API_DeleteFunctionEventInvokeConfig.md "../../../lambda/latest/dg/API_DeleteFunctionEventInvokeConfig.md").
   2. Review the Lambda code and update the libraries imports and [Lambda function
      layers](../../../lambda/latest/dg/chapter-layers.md "../../../lambda/latest/dg/chapter-layers.md") to remove the potentially suspicious libraries and layers.
   3. Mitigate Amazon Inspector findings related to the Lambda function involved in the finding.
