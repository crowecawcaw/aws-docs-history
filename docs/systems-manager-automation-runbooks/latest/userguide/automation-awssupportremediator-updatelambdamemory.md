

# `AWSSupportRemediator-UpdateLambdaMemory`

**Description**

Updates the memory allocation of an AWS Lambda function to a specified size by calling the Lambda [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html) API.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Compute Optimizer [Lambda function recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-lambda-recommendations.html).

If the Lambda function does not exist or its memory already matches the recommended size, the automation completes successfully without making changes.

The automation does not lock the Lambda function during execution. AWS Remediator serializes runs per Lambda function. Running this runbook from other sources with concurrent, differing `RecommendedMemorySize` values leaves the final memory size dependent on the order in which the requests complete.

To revert the change, run this runbook again and pass the original memory size from the previous execution's `validateInput.InitialMemorySize` output.

Changing the memory allocation affects both the performance and the per-invocation cost of the Lambda function. Decreasing memory below what the workload requires can cause out-of-memory errors or longer invocation times. For more information about pricing, see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).

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
+ LambdaFunctionName

  Type: String

  Description: (Required) The name of the Lambda function to update.
+ RecommendedMemorySize

  Type: Integer

  Description: (Required) The target memory allocation for the Lambda function, in MB. Valid range is 128 to 10240.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `lambda:GetFunctionConfiguration`
+ `lambda:UpdateFunctionConfiguration`

**Document Steps**

1. **validateInput** - Validates that the Lambda function exists and determines whether its current memory size differs from the value of the `RecommendedMemorySize` parameter.

1. **branchOnChangeRequired** - Branches on whether the memory requires an update according to the `ChangeRequired` output from the `validateInput` step.

1. **updateMemorySize** - Updates the memory allocation of the Lambda function to the value of the `RecommendedMemorySize` parameter by calling the Lambda `UpdateFunctionConfiguration` API.

**Outputs**
+ validateInput.InitialMemorySize: The initial memory size of the Lambda function before any changes.
+ validateInput.ValidationMessage: The reason for the validation result.
+ updateMemorySize.NewMemorySize: The new memory size of the Lambda function after the update.