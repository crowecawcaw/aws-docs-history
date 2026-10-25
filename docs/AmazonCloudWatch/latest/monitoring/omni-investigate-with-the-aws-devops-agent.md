

# Investigate with the AWS DevOps Agent
<a name="omni-investigate-with-the-aws-devops-agent"></a>

CloudWatch Omni uses AWS DevOps Agent as the native agent for root cause analysis and incident investigation. You must link CloudWatch Omni to a DevOps Agent space before you can start an investigation.

AWS DevOps Agent is an autonomous site reliability engineering (SRE) agent that supports release management and production operations across AWS, multi-cloud, and on-premises environments. For more information, see the [DevOps Agent documentation](https://docs.aws.amazon.com/devopsagent/latest/userguide/).

**Important**  
**Trust boundary and data access**  
AWS DevOps Agent and CloudWatch Omni operate under different trust boundaries. DevOps Agent investigates with the IAM role on its agent space. You configure this role in the AWS DevOps Agent console. DevOps Agent does not use your space's operator role, the CloudWatch Omni managed policies, or your members' grants. DevOps Agent reads CloudWatch Logs log groups and other sources directly, not through the CloudWatch Dataset. CloudWatch Omni then displays the results.  
Data scopes apply only to data read from the CloudWatch Dataset. They do not filter AWS DevOps Agent investigation results or any other data that comes from outside the Dataset.  
Any member whose grant includes the AWS DevOps Agent read actions can see every investigation for a connected agent space. This includes investigations that other members started. The read actions are `aidevops:GetBacklogTask`, `aidevops:ListBacklogTasks`, and `aidevops:ListJournalRecords`. The Viewer, Editor, and Space Admin permission levels all include these actions. Connecting an agent space is the access control for this integration. Connect only an agent space whose IAM role reaches data that every member of the space can already see.  
Only a Space Admin can connect, change, or remove the DevOps Agent integration. For more information about permission levels, see [Control access to your space](omni-control-access-to-your-space.md).

## Connect an agent space
<a name="omni-investigate-with-the-aws-devops-agent-connect-an-agent-space"></a>

### Deploy DevOps Agent
<a name="omni-investigate-with-the-aws-devops-agent-connect-an-agent-space-deploy-devops-agent"></a>
+ A DevOps Agent space must exist in the account you are accessing CloudWatch Omni from. To create one, see [Creating an agent space](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-creating-an-agent-space.html) in the AWS DevOps Agent User Guide.

**Note**  
Sign-in must match. If your Omni domain uses IAM Identity Center, configure your DevOps Agent space to use IAM Identity Center as well.

### Connect Omni to DevOps Agent
<a name="omni-investigate-with-the-aws-devops-agent-connect-an-agent-space-connect-omni-to-devops-agent"></a>

Before you connect, a space administrator must attach the [AIDevOpsAgentFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AIDevOpsAgentFullAccess.html) managed policy to your space's operator role. See [Set up Omni](omni-set-up-omni.md).

1. In CloudWatch Omni, navigate to **Settings** → **Integrations** → **AWS DevOps Agent**. Choose **Select Space**.

1. Choose the Region your agent space is in. Select your agent space. Choose **Connect**.

### Start an investigation
<a name="omni-investigate-with-the-aws-devops-agent-connect-an-agent-space-start-an-investigation"></a>
+ **From the Omni agent.** Describe the symptom in a thread and ask for an investigation. Omni automatically delegates questions related to root cause analysis to DevOps Agent.
+ **With the `/investigation` command.** In a thread, enter `/investigation new <description of issue>`.
+ **From an alert.** A firing alert offers an **Investigate** action. Investigations are manual: an alert never starts one automatically when it fires.