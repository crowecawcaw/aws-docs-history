

# `AWSSupport-RequestSageMakerLimitIncrease`
<a name="automation-awssupport-requestsagemakerlimitincrease"></a>

 **Description** 

The `AWSSupport-RequestSageMakerLimitIncrease` runbook enables bulk submission of multiple Amazon SageMaker AI (SageMaker AI) quota increase requests in a single operation, streamlining quota management for large-scale machine learning workloads. The runbook validates each request against adjustable SageMaker AI service quotas, routes requests within auto-approval thresholds for immediate processing, and creates AWS Support cases for requests that require manual review. Quota increases are applied in the same AWS Region where the runbook is executed.

**Important**  
This runbook does not support quota increase requests for specialized compute instances including P4, P5, and Trainium instance types. For these instance types, submit individual quota increase requests through the AWS Service Quotas console or AWS Support.

The runbook pauses for up to one hour while waiting for approval from designated principals via Amazon Simple Notification Service (Amazon SNS) notification. Review the `ApproveQuotaCodeLimitMapping` step output carefully before approving, as approved quota increases cannot be reversed.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-RequestSageMakerLimitIncrease) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: AWS::IAM::Role::Arn

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows AWS Systems Manager (Systems Manager) Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ ResourcesMapping

  Type: StringList

  Description: (Required) The SageMaker AI service quotas to increase, specified as colon-separated values. Supports three formats:
  + `Category:Resource:NewValue` — when both category and resource names are available. Example: `spot-training-job:ml.c4.xlarge:25`
  + `Resource:NewValue` — when only the resource name is available. Example: `max_number_of_experiment_trial_associations:501`
  + `QuotaCode:NewValue` — when using the direct quota code. Example: `L-9xAxx23x:25`

  You can mix formats in the same request, separated by commas. Maximum 50 items. Example: `studio:CodeEditor-ml.r6id.large:787,spot-training-job:ml.c4.xlarge:34,L-99AEC235:2`
+ SNSTopicArn

  Type: String

  Description: (Required) The ARN of the Amazon SNS topic used to send approval notifications during the automation execution.
+ ApproverIAM

  Type: StringList

  Description: (Required) A list of AWS authenticated principals who can approve or reject the quota increase requests. Maximum 10 approvers. Accepted formats: IAM user name, IAM user ARN, IAM role ARN, or IAM assume role user ARN.
+ MinimumRequiredApprovals

  Type: Integer

  Valid values: 1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \| 8 \| 9 \| 10

  Default: 1

  Description: (Optional) The minimum number of approvals required to resume the automation. Cannot exceed the number of approvers defined in `ApproverIAM`.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `servicequotas:ListServiceQuotas`
+ `servicequotas:RequestServiceQuotaIncrease`
+ `servicequotas:GetRequestedServiceQuotaChange`
+ `sns:Publish`
+ `ssm:SendAutomationSignal`

 **Document Steps** 

1. `VerifyCategoriesAndResources` - Validates all specified categories and resources against adjustable SageMaker AI service quotas using the AWS Service Quotas API. Confirms that each category and resource name exists and is modifiable, and identifies requests where the new limit is lower than the current value.

1. `BranchOnValidCategoriesFound` - Checks whether any valid quota mappings were found. If valid mappings exist, proceeds to `ApproveQuotaCodeLimitMapping`. Otherwise, skips directly to `GenerateSummaryReport`.

1. `ApproveQuotaCodeLimitMapping` - Prepares a detailed approval message showing valid requests ready for processing, invalid requests with explanations (such as limits lower than current values or unsupported quota codes), and a complete breakdown of all quota increase requests for review before approval.

1. `WaitingForApproval` - Pauses the automation and sends an approval notification to the specified Amazon SNS topic. Designated approvers must review the `ApproveQuotaCodeLimitMapping` step output and approve or reject the requests. This step times out after 3600 seconds (one hour) if no action is taken.

1. `RequestQuotaIncreases` - Submits individual quota increase requests for each valid resource via the AWS Service Quotas API. Requests are paced at one per second to prevent API throttling. Handles API exceptions with exponential retry.

1. `WaitForRequestQuotaIncreaseResults` - Polls the status of all submitted quota increase requests until none remain in `PENDING` state. Accepted terminal statuses are `CASE_OPENED`, `APPROVED`, `DENIED`, `NOT_APPROVED`, `CASE_CLOSED`, and `INVALID_REQUEST`.

1. `GetRequestQuotaIncreaseResults` - Retrieves the final status of all submitted quota increase requests from the AWS Service Quotas API and maps support case IDs to their corresponding resources and request IDs for reporting.

1. `GenerateSummaryReport` - Compiles a comprehensive summary of all quota increase requests and their outcomes, including total request counts, per-request details, support case IDs for requests requiring manual review, and actionable next steps.

 **Outputs** 

`GenerateSummaryReport.SummaryReport` - A comprehensive summary of all quota increase requests, their statuses, and any support case IDs created for manual review.