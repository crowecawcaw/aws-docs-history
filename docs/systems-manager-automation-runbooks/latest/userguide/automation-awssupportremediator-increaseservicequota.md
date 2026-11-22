

# `AWSSupportRemediator-IncreaseServiceQuota`

**Description**

Submits a quota increase request for a specified AWS service in Service Quotas by calling the Service Quotas `RequestServiceQuotaIncrease` API.

The runbook requests a new quota value equal to the current quota value plus the `Increment` parameter.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor checks [EC2-VPC Elastic IP Address](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html#ec2-vpc-elastic-ip-address), [VPC Internet Gateways](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html#vpc-internet-gateways), [VPC](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html#vpc-quota-check), [Auto Scaling Groups](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html#auto-scaling-groups), [RDS Option Groups](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html#rds-option-groups), [ELB Application Load Balancers](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html#elb-application-load-balancers), and [ELB Network Load Balancers](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html#elb-network-load-balancers).

The runbook checks for an open quota increase request (status `PENDING` or `CASE_OPENED`) with the same service code and quota code in the AWS account. If one exists, the runbook completes successfully without submitting a new request.

This check is best-effort. Two concurrent runs with the same service code and quota code can each observe no open request and submit duplicate requests. AWS Remediator orchestration serializes runs per finding, so concurrent invocations are not expected in the supported use case.

Submitting a quota increase request creates an AWS Support case in the AWS account and Region where the runbook runs. AWS Support evaluates the request; this runbook does not guarantee approval. This runbook cannot automatically withdraw a request after it submits one. To cancel a request, update the resulting AWS Support case. The first invocation of `RequestServiceQuotaIncrease` in an AWS account also creates the AWS Identity and Access Management (IAM) service-linked role for Service Quotas (`AWSServiceRoleForServiceQuotas`, for the `servicequotas.amazonaws.com` service principal). This happens only if the role does not already exist.

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
+ QuotaCode

  Type: String

  Description: (Required) The code that identifies the quota in Service Quotas.
+ ServiceCode

  Type: String

  Description: (Required) The code that identifies the AWS service in Service Quotas.
+ Increment

  Type: Integer

  Description: (Optional) The amount to add to the current quota value to compute the new quota value.

  Default: 3

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `iam:CreateServiceLinkedRole`
+ `servicequotas:GetServiceQuota`
+ `servicequotas:ListRequestedServiceQuotaChangeHistoryByQuota`
+ `servicequotas:RequestServiceQuotaIncrease`

**Document Steps**

1. **validateInputs** - Retrieves the current quota value for the `ServiceCode` and `QuotaCode` parameters. Checks whether an open quota increase request (status `PENDING` or `CASE_OPENED`) already exists for the same service and quota in the AWS account. Returns no change required when an open request already exists; otherwise computes the desired new quota value.

1. **branchOnChangeRequired** - Branches on whether a change is required. Continues to `requestNewQuota` when `validateInputs.ChangeRequired` is `true`. Otherwise, ends the runbook successfully.

1. **requestNewQuota** - Calls the Service Quotas `RequestServiceQuotaIncrease` API using the desired value that `validateInputs` computes. Submitting the request creates an AWS Support case in the AWS account.

**Outputs**
+ validateInputs.ChangeRequired: Whether the runbook needs to submit a new quota increase request. `false` when an open quota increase request already exists for the same service code and quota code.
+ validateInputs.ValidationMessage: A message describing why the runbook makes no change; `N/A` when the runbook needs to make a change.
+ validateInputs.InitialLimit: The current quota value that the runbook reads from Service Quotas before it runs.
+ validateInputs.DesiredValue: The new quota value the runbook submits when it needs to make a change; otherwise, the desired value from the existing open request.
+ validateInputs.ExistingRequestId: The request ID of an existing open quota increase request, or `N/A` when no open request exists.
+ validateInputs.ExistingRequestStatus: The status of an existing open quota increase request, or `N/A` when no open request exists.
+ requestNewQuota.RequestId: The ID of the quota increase request that this runbook submits.
+ requestNewQuota.RequestStatus: The status of the quota increase request that this runbook submits.