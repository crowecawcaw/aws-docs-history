# Identity-based policy examples for Amazon Bedrock Agents

Select a topic to see example IAM policies that you can attach to an IAM role to provision permissions for actions in [Automate tasks in your application using AI agents](agents.md "agents.md").

###### Topics

- [Required permissions for Amazon Bedrock Agents](#iam-agents-ex-all "#iam-agents-ex-all")
- [Allow users to view information about and invoke an agent](#security_iam_id-based-policy-examples-perform-actions-agent "#security_iam_id-based-policy-examples-perform-actions-agent")

## Required permissions for Amazon Bedrock Agents

For an IAM identity to use Amazon Bedrock Agents, you must configure it with the necessary permissions. You can attach the [AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess") policy to grant the proper permissions to the role.

To restrict permissions to only actions that are used in Amazon Bedrock Agents, attach the following identity-based policy to an IAM role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AgentPermissions",
 "Effect": "Allow",
 "Action": [
 "bedrock:ListFoundationModels",
 "bedrock:GetFoundationModel",
 "bedrock:TagResource",
 "bedrock:UntagResource",
 "bedrock:ListTagsForResource",
 "bedrock:CreateAgent",
 "bedrock:UpdateAgent",
 "bedrock:GetAgent",
 "bedrock:ListAgents",
 "bedrock:DeleteAgent",
 "bedrock:CreateAgentActionGroup",
 "bedrock:UpdateAgentActionGroup",
 "bedrock:GetAgentActionGroup",
 "bedrock:ListAgentActionGroups",
 "bedrock:DeleteAgentActionGroup",
 "bedrock:GetAgentVersion",
 "bedrock:ListAgentVersions",
 "bedrock:DeleteAgentVersion",
 "bedrock:CreateAgentAlias",
 "bedrock:UpdateAgentAlias",
 "bedrock:GetAgentAlias",
 "bedrock:ListAgentAliases",
 "bedrock:DeleteAgentAlias",
 "bedrock:AssociateAgentKnowledgeBase",
 "bedrock:DisassociateAgentKnowledgeBase",
 "bedrock:ListAgentKnowledgeBases",
 "bedrock:GetKnowledgeBase",
 "bedrock:ListKnowledgeBases",
 "bedrock:PrepareAgent",
 "bedrock:InvokeAgent",
 "bedrock:AssociateAgentCollaborator",
 "bedrock:DisassociateAgentCollaborator",
 "bedrock:GetAgentCollaborator",
 "bedrock:ListAgentCollaborators",
 "bedrock:UpdateAgentCollaborator"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can further restrict permissions by omitting [actions](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions") or specifying [resources](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources") and [condition keys](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys"). An IAM identity can call API operations on specific resources. For example, the
[UpdateAgent](../APIReference/API_agent_UpdateAgent.md "../APIReference/API_agent_UpdateAgent.md") operation can only be used on agent resources and the
[InvokeAgent](../APIReference/API_agent-runtime_InvokeAgent.md "../APIReference/API_agent-runtime_InvokeAgent.md") operation can only be used on alias resources. For API operations that aren't used on a specific resource type (such as [CreateAgent](../APIReference/API_agent_CreateAgent.md "../APIReference/API_agent_CreateAgent.md")),
specify \* as the `Resource`. If you specify an API operation that can't be used on
the resource specified in the policy, Amazon Bedrock returns an error.

## Allow users to view information about and invoke an agent

The following is a sample policy that you can attach to an IAM role to allow it to view information about or edit an agent with the ID `AGENT12345` and to interact with its alias with the ID `ALIAS12345`. For example, you could attach this policy to a role that you want to only have permissions to troubleshoot an agent and update it.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetAndUpdateAgent",
 "Effect": "Allow",
 "Action": [
 "bedrock:GetAgent",
 "bedrock:UpdateAgent"
 ],
 "Resource": "arn:aws:bedrock:us-east-1:123456789012:agent/AgentId"
 },
 {
 "Sid": "InvokeAgent",
 "Effect": "Allow",
 "Action": [
 "bedrock:InvokeAgent"
 ],
 "Resource": "arn:aws:bedrock:us-east-1:123456789012:agent-alias/AgentId/AgentAliasId"
 }
 ]
}`

```
