

# Permissions for AWS DevOps Agent
<a name="security-iam-devops-agent"></a>

If you set up AWS DevOps Agent for the **Operate** capabilities, your identity needs two kinds of permissions: read access so the IDE extension can show status, and permissions to create the access role and Agent Space.

To show the Agent Space status and its integrations, the IDE extension uses AWS DevOps Agent read permissions, including `aidevops:ListServices` and `aidevops:ListAssociations`.

Setting up AWS DevOps Agent requires permission to create an IAM role and an Agent Space. Your coding agent checks your permissions before setup. If anything is missing, it tells you what’s needed and gives you a note to send to your AWS administrator. For the permissions AWS DevOps Agent uses, see [DevOps Agent IAM permissions](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-devops-agent-iam-permissions.html) in the * AWS DevOps Agent User Guide*.

The access role trusts only the Agent Space in your account. Setup does not attach `AIDevOpsAgentActionsPolicy` and does not create an elevated role, so AWS DevOps Agent recommends fixes but does not apply them. AWS DevOps Agent actions are logged in AWS CloudTrail. To remove AWS DevOps Agent, delete the access role or the Agent Space. For more information about how AWS DevOps Agent uses IAM roles and Agent Spaces, see the [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/).