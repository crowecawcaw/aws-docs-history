

AWS FinOps Agent is in preview release and is subject to change.

# AWS managed policies for AWS FinOps Agent
<a name="security-iam-awsmanpol"></a>

AWS managed policies are standalone identity-based policies that AWS creates and maintains. AWS FinOps Agent uses the following managed policies for the roles it assumes. If you configure roles manually, see the [IAM setup guide](setting-up.md).

**Topics**
+ [AWS managed policy: FinOpsAgentAgentPolicy](#security-iam-awsmanpol-FinOpsAgentAgentPolicy)
+ [AWS managed policy: FinOpsAgentOperatorPolicy](#security-iam-awsmanpol-FinOpsAgentOperatorPolicy)

## AWS managed policy: FinOpsAgentAgentPolicy
<a name="security-iam-awsmanpol-FinOpsAgentAgentPolicy"></a>

Attach `FinOpsAgentAgentPolicy` to the agent role. AWS FinOps Agent assumes this role when it reads the cost, optimization, and infrastructure data that supports agent workflows.

For instructions on setting up the agent role, see [Agent permissions policy](setting-up.md#setting-up-agent-policy).

For more information about the current policy document, see [FinOpsAgentAgentPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/FinOpsAgentAgentPolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: FinOpsAgentOperatorPolicy
<a name="security-iam-awsmanpol-FinOpsAgentOperatorPolicy"></a>

Attach `FinOpsAgentOperatorPolicy` to the operator role. AWS FinOps Agent assumes this role to perform web application operations, including conversations, tasks, automations, context files, and reports.

For instructions on setting up the operator role, see [Operator permissions policy](setting-up.md#setting-up-operator-policy).

For more information about the current policy document, see [FinOpsAgentOperatorPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/FinOpsAgentOperatorPolicy.html) in the *AWS Managed Policy Reference*.