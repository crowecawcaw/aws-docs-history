

AWS FinOps Agent is in preview release and is subject to change.

# Data protection in AWS FinOps Agent
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS FinOps Agent. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS FinOps Agent or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Data storage and encryption
<a name="data-protection-storage-encryption"></a>

Context files, memory files, and artifacts are stored in AWS-managed infrastructure encrypted with AWS KMS. At the start of each session, the agent loads these files into its agent runtime environment. The runtime environment is ephemeral and isolated per session.

Conversation history and task records (including the agent's reasoning traces, tool calls, and results) are stored in AWS-managed infrastructure alongside each conversation and task record.

## Data isolation across agents
<a name="data-protection-isolation"></a>

No content (context files, conversations, memory, artifacts, or task data) is shared across agents. Each agent is a fully isolated instance with its own IAM role, context files, memory, task queue, and artifacts. Information from one agent is not visible or accessible from another.

## Managing your data
<a name="data-protection-customer-controls"></a>

You control the data AWS FinOps Agent stores on your behalf. The web application supports the actions in the following table during preview. To remove every category at once, delete the agent from the AWS FinOps Agent console.


| Data type | How to remove or modify | 
| --- | --- | 
| Context files | Open the Context files workspace in the web application. Choose Delete to soft-delete a file, which removes it from the agent's active context. Choose Restore on a soft-deleted file to make it active again. | 
| Memory entries | Instruct the agent in chat to forget a specific preference, fact, or correction. The agent updates its memory in place. | 
| Conversations | Conversations are retained on the agent and cannot be deleted individually during preview. To remove all conversation history, delete the agent. | 
| Tasks | Cancel a running task from the task detail page. Tasks cannot be deleted individually during preview; task records remain on the agent until you delete the agent. | 
| Automations | Open the Automations workspace and delete the automation. Deleting an automation stops new tasks from being created on its schedule or trigger; tasks already created by the automation remain on the agent. | 
| Generated artifacts | Open the Artifacts workspace and choose Delete on the artifact you want to remove. | 
| The entire agent | From the AWS FinOps Agent console Agents page, select the agent and choose Delete. Deleting an agent removes the web application link and the previous interaction data the agent stored. | 

For the AWS Organizations opt-out that prevents your content from being used for service improvement, see [Service improvement](service-improvement.md).