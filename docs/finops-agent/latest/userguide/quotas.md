

AWS FinOps Agent is in preview release and is subject to change.

# Quotas
<a name="quotas"></a>

The following table describes the quotas for AWS FinOps Agent.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Agents per account per Region | 1 | Yes | The default number of agents that you can create per account in each AWS Region. | 
| Artifact storage per agent | 100 MB | Yes | The default amount of storage for artifacts (such as cost reports and investigation outputs) that the agent retains per agent. | 
| Context file size per upload | 10 MB | No | The maximum size of a single context file that you can upload to an agent. | 
| Context file storage per agent | 100 MB | Yes | The default total storage for all context files uploaded to an agent. | 
| Jira integrations per account | 1 | No | The maximum number of Jira integrations (account-level connections to a Jira Cloud site) that you can register per account. | 
| Slack integrations per account | 1 | No | The maximum number of Slack integrations (account-level connections to a Slack workspace) that you can register per account. | 
| Jira connections per agent | 2 | No | The maximum number of Jira connections (agent-level bindings to a Jira project) that you can create per agent. | 
| Slack connections per agent | 2 | No | The maximum number of Slack connections (agent-level bindings to a Slack channel) that you can create per agent. | 

## Requesting a quota increase
<a name="quotas-request-increase"></a>

During preview, request a quota increase by opening an AWS Support case:

1. Open the [Create case](https://console.aws.amazon.com/support/home#/case/create) page in the AWS Support Center.

1. For **Service**, choose **AWS FinOps Agent**.

1. For **Category**, choose **General**.

1. Provide the quota name, your account ID, agent name and agent ID, the requested new value, and a brief justification.

1. Submit the case.