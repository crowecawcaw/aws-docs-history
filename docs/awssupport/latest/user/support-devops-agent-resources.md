

# Resources created for AWS DevOps Agent activated from AWS Support
<a name="support-devops-agent-resources"></a>

Activation from the Support Center Console creates the following resources in `us-east-1`. Replace {{ACCOUNT\_ID}} with your 12-digit AWS account ID. The role suffix is a 12-character identifier derived from the agent space.


**Resources created when you enable AWS DevOps Agent from the Support Center Console**  

| AWS service | Resource type | Resource name | Trust scope | Permissions granted | 
| --- | --- | --- | --- | --- | 
| AWS DevOps Agent | Agent space | `DevOpsAgentSpace` | Not applicable | Container for the account association, operator web app configuration, and data the agent generates while it operates. | 
| AWS Identity and Access Management (IAM) | Role | `DevOpsAgentRole-AgentSpace-{{suffix}}` | Trusted by `aidevops.amazonaws.com` with `aws:SourceAccount` and `aws:SourceArn` conditions that scope the role to agent spaces in your own account (confused-deputy protection). | Grants the agent the read-only investigation permissions across AWS services that it needs to investigate resources in your account. Permissions come from the AWS-managed `AIDevOpsAgentAccessPolicy` attached at activation time. For the full list, see [`AIDevOpsAgentAccessPolicy`](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-devops-agent-iam-permissions.html#AIDevOpsAgentAccessPolicy) in the *AWS DevOps Agent User Guide*. The customer-managed `AIDevOpsAllowAwsSupportActionsPolicy-{{suffix}}` policy is also attached. | 
| AWS Identity and Access Management (IAM) | Role | `DevOpsAgentRole-WebappAdmin-{{suffix}}` | Trust policy scoped to a specific agent space, so only that agent space's operator web app can assume it. | Grants the operator web app the permissions it needs for chat, journal, recommendations, and Support integration. Permissions come from the AWS-managed `AIDevOpsOperatorAppAccessPolicy`. For the full list, see [`AIDevOpsOperatorAppAccessPolicy`](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-devops-agent-iam-permissions.html#AIDevOpsOperatorAppAccessPolicy) in the *AWS DevOps Agent User Guide*. | 
| AWS Identity and Access Management (IAM) | Customer-managed policy | `AIDevOpsAllowAwsSupportActionsPolicy-{{suffix}}` | Attached to the `DevOpsAgentRole-AgentSpace-{{suffix}}` role. | Grants `iam:CreateServiceLinkedRole`, scoped to the AWS Resource Explorer service-linked role ARN (`arn:aws:iam::{{ACCOUNT_ID}}:role/aws-service-role/resource-explorer-2.amazonaws.com/AWSServiceRoleForResourceExplorer`). This permission allows the agent to create the AWS Resource Explorer service-linked role on your behalf if it doesn't already exist, so the agent can use AWS Resource Explorer for topology discovery. | 

The Support Center Console activation doesn't create resources in any other AWS Region.