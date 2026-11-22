

# `AWSSupportRemediator-ResizeLambdaMemory`

**Description**

Updates the memory allocation of an AWS Lambda function to the recommended size.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [AWS Lambda over-provisioned functions for memory size](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#aws-lambda-over-provisioned-functions-memory-size).

If the Lambda function does not exist, the actual memory differs from the value reported by Trusted Advisor, or the memory is already at or beyond the recommended size, the automation completes successfully without making changes.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ CurrentMemorySizeFromTrustedAdvisor

  Type: Integer

  Description: (Required) The current memory allocation of the Lambda function as reported by Trusted Advisor, in MB. If the actual memory differs from this value, the automation takes no action.
+ LambdaFunctionName

  Type: String

  Description: (Required) The name of the Lambda function.
+ RecommendedMemorySize

  Type: Integer

  Description: (Required) The recommended memory allocation for the Lambda function, in MB. Valid range is 128–10240.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `lambda:GetFunctionConfiguration`
+ `lambda:UpdateFunctionConfiguration`

**Document Steps**

1. **validateNewMemoryValue** - Validates that the Lambda function exists and determines whether a memory change is required.

1. **branchOnChangeRequired** - Branches on whether memory modification is needed.

1. **setNewMemoryValue** - Updates the Lambda function memory configuration to the recommended size.

**Outputs**
+ validateNewMemoryValue.CurrentSetMemory: The current memory allocation of the Lambda function before modification.
+ setNewMemoryValue.NewSetMemory: The new memory allocation of the Lambda function after modification.
+ validateNewMemoryValue.ValidationMessage: A message describing the validation result.