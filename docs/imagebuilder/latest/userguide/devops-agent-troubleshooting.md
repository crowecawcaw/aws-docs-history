

# Troubleshoot failed builds with AI - Preview
<a name="devops-agent-troubleshooting"></a>

**Preview feature**  
This feature is in preview and is subject to change.

When EC2 Image Builder builds fail, the root cause can be time-consuming and complex to identify. The Troubleshoot feature in Image Builder, powered by AWS DevOps Agent, automates this process with AI-powered analysis. You can quickly identify the cause of complex build failures or detect patterns across multiple failed pipelines.

When a build fails, you can use Troubleshoot to analyze build logs, Amazon CloudWatch logs, workflow step executions, and related AWS resources. You receive a root cause analysis and remediation steps to resolve the issue.

You can troubleshoot a single failed pipeline build or analyze multiple failed pipelines to identify common patterns and shared root causes.

**Topics**
+ [Prerequisites](#devops-agent-troubleshooting-prereqs)
+ [Set up troubleshooting](#devops-agent-troubleshooting-setup)
+ [Troubleshoot a failed build](#devops-agent-troubleshooting-single)
+ [Troubleshoot multiple failed pipelines](#devops-agent-troubleshooting-aggregate)
+ [What Troubleshoot investigates](#devops-agent-troubleshooting-checks)
+ [Considerations](#devops-agent-troubleshooting-considerations)

## Prerequisites
<a name="devops-agent-troubleshooting-prereqs"></a>

Before you use the Troubleshoot feature, make sure that the IAM user or role that you use has the following permissions:
+ `aidevops:ListAgentSpaces` – Required to discover available agent spaces.
+ `aidevops:CreateChat` – Required to start troubleshooting sessions.
+ `aidevops:SendChatMessage` – Required to send messages during troubleshooting.
+ `aidevops:CreateAgentSpace` – Required only if you want Image Builder to create an agent space for you. You can omit this permission if you bring your own agent space.

For more information about IAM policies, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

## Set up troubleshooting
<a name="devops-agent-troubleshooting-setup"></a>

The Troubleshoot feature requires an AWS DevOps Agent agent space. You can use an existing agent space or have Image Builder create one for you:
+ **Bring your own agent space** – If you already have an agent space, Image Builder uses it for troubleshooting.
+ **Have Image Builder create one** – If you don't have an agent space, Image Builder creates and configures one when you start your first investigation. This option requires the `aidevops:CreateAgentSpace` permission.

To start troubleshooting, choose the **Troubleshooting** icon in the AWS Management Console header.

**Note**  
For more information about AWS DevOps Agent, see the [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/).

## Troubleshoot a failed build
<a name="devops-agent-troubleshooting-single"></a>

When an image build fails, you can start an AI-powered investigation from several entry points in the Image Builder AWS Management Console.

### Start a troubleshooting investigation
<a name="devops-agent-troubleshooting-start-single"></a>

Use one of the following methods to start troubleshooting a failed build:
+ **Pipelines table** – Choose the **Troubleshooting** icon next to a failed pipeline status in the **Image pipelines** list.
+ **Output images table** – Choose the **Troubleshooting** icon next to a failed image build in the output images list.
+ **Troubleshooting drawer** – In the AWS Management Console header, choose the **Troubleshooting** icon, then select the pipeline you want to investigate.

### During the investigation
<a name="devops-agent-troubleshooting-during-single"></a>

After you start troubleshooting, Troubleshoot investigates the failure. You can track real-time progress in the drawer as logs and resources are analyzed. The investigation typically completes in a few minutes. You can continue working in other AWS Management Console areas while the analysis runs. When the investigation completes, you receive:
+ Root cause analysis that identifies why the build failed
+ Remediation steps to resolve the issue
+ Commands or configuration changes to fix the problem

After you review the results, you can provide feedback on the response quality. To re-run the analysis against the same failed build, choose **Troubleshoot again**.

## Troubleshoot multiple failed pipelines
<a name="devops-agent-troubleshooting-aggregate"></a>

If you have multiple failed pipelines, you can analyze them together to identify common patterns and shared root causes.

### Start an aggregate investigation
<a name="devops-agent-troubleshooting-start-aggregate"></a>

Use one of the following methods to troubleshoot multiple pipelines:
+ In the **Image pipelines** table, select multiple failed pipelines and choose **Troubleshoot selected**.
+ Open the troubleshooting drawer and choose **Troubleshoot all** to analyze all failed pipelines.

### Aggregate analysis results
<a name="devops-agent-troubleshooting-aggregate-results"></a>

You receive a grouped analysis organized by root cause. For each group, you get:
+ Description of the shared root cause
+ Pipelines affected by that root cause
+ Remediation steps for the group

After the aggregate analysis, you can choose a drill-down prompt to investigate a specific pipeline in more detail.

## What Troubleshoot investigates
<a name="devops-agent-troubleshooting-checks"></a>

When you troubleshoot a failed build, the analysis covers the following areas:
+ **Build logs and Amazon CloudWatch logs** – Checks for errors, non-zero exit codes, timeouts, and stack traces.
+ **Workflow step executions** – Identifies the failed step and examines its details.
+ **Networking and permissions** – Reviews IAM instance profile permissions, security groups, subnet routing, NAT gateways, internet gateways, and VPC endpoints.
+ **Components and recipe configuration** – Checks for script errors, missing dependencies, broken URLs, and base AMI validity.
+ **Network connectivity** – Checks AWS Systems Manager (Systems Manager) Agent reachability, DNS resolution, and proxy configuration.
+ **Build history** – Reviews recent builds to distinguish persistent failures from intermittent issues.

## Considerations
<a name="devops-agent-troubleshooting-considerations"></a>

Note the following when using the Troubleshoot feature:
+ Troubleshoot performs read-only analysis. Your resources are not modified.
+ Troubleshooting is scoped to Image Builder build failures and related infrastructure such as IAM, VPC, and Systems Manager Agent.

**Note**  
AI generates these responses. Verify the analysis and recommendations before you modify your resources.

For more information about troubleshooting Image Builder pipeline builds, see [Troubleshoot pipeline builds](troubleshooting.md#troubleshooting-pipelines).