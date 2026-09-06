

# Removing AWS DevOps Agent
<a name="support-devops-agent-removing"></a>

To remove the resources that were created when you enabled AWS DevOps Agent from the Support Center Console, see [Deleting an agent space](https://docs.aws.amazon.com/devopsagent/latest/userguide/deleting-an-agent-space.html) in the *AWS DevOps Agent User Guide*. The procedures cover deleting the agent space, the two IAM roles, and any customer-managed policies that start with `AIDevOps`. The procedure also documents how to re-enable AWS DevOps Agent later and what to watch out for when you do.

**Note**  
The AWS-managed policies attached to the IAM roles (`AIDevOpsAgentAccessPolicy` and `AIDevOpsOperatorAppAccessPolicy`) are detached but not deleted, because these policies are owned by AWS.

When you follow that procedure, note that your resources have the names listed in [Resources created for AWS DevOps Agent activated from AWS Support](support-devops-agent-resources.md), and they are all in `us-east-1`.