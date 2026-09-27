

# Investigate with the AWS DevOps Agent
<a name="omni-investigate-with-the-aws-devops-agent"></a>

CloudWatch Omni uses AWS DevOps Agent as the native agent for root cause analysis and incident investigation. You must link CloudWatch Omni to a DevOps Agent space before you can start an investigation.

AWS DevOps Agent is an autonomous site reliability engineering (SRE) agent that supports release management and production operations across AWS, multi-cloud, and on-premises environments. For more information, see the [DevOps Agent documentation](https://docs.aws.amazon.com/devopsagent/latest/userguide/).

**Connect an agent space**

Deploy DevOps Agent
+ A DevOps Agent space must exist in the account you are accessing CloudWatch Omni from. To create one, see [Creating an agent space](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-creating-an-agent-space.html) in the AWS DevOps Agent User Guide.

**Note**  
Sign-in must match. If your Omni domain uses IAM Identity Center, configure your DevOps Agent space to use IAM Identity Center as well.

Connect Omni to DevOps Agent

Before you connect, a space administrator must attach the [AIDevOpsAgentFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AIDevOpsAgentFullAccess.html) managed policy to your space's operator role, `CloudWatchOmniOperatorRole`. See [Set up Omni](omni-set-up-omni.md).

1. In CloudWatch Omni, navigate to **Settings** → **Integrations** → **AWS DevOps Agent**. Choose **Select Space**.

1. Choose the Region your agent space is in. Select your agent space. Choose **Connect**.

Start an investigation
+ **From the Omni agent.** Describe the symptom in a thread and ask for an investigation. Omni automatically delegates questions related to root cause analysis to DevOps Agent.
+ **With the `/investigation` command.** In a thread, enter `/investigation new <description of issue>`.
+ **From an alert.** A firing alert offers an **Investigate** action. Investigations are manual: an alert never starts one automatically when it fires.