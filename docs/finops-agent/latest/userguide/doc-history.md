

AWS FinOps Agent is in preview release and is subject to change.

# Document history for AWS FinOps Agent

The following table describes the documentation releases for AWS FinOps Agent.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWS managed policy updates](security-iam-awsmanpol.md#security-iam-awsmanpol-updates) – New policy versions | Documented new versions of FinOpsAgentAgentPolicy and AWSFinOpsAgentServiceRolePolicy. The agent policy update adds data and resource-read permissions and Data Hub query permissions for account-scoped agents. The service-linked role policy update adds Data Hub query permissions and allows the AWS Organizations ListDelegatedAdministrators action only when a request specifies finops-agent.amazonaws.com. | November 19, 2026 | 
| Organization-wide access and Data Hub | Added [organization-wide access with a delegated administrator](setting-up-organization-access.md), the AWSServiceRoleForFinOpsAgent [service-linked role](using-service-linked-roles.md) and AWSFinOpsAgentServiceRolePolicy managed policy, and the Data Hub option for resource-level cost attribution. Updated the agent policy to the current FinOpsAgentAgentPolicy. | November 19, 2026 | 
| Documentation updates | Updated setup and identity guidance for Cost Optimization Hub, Slack and Jira integrations, and IAM access. | August 18, 2026 | 
| Public preview | This is the initial preview release of AWS FinOps Agent (preview). | June 9, 2026 | 