# Preventative security best practice for agents

The following best practices for Amazon Bedrock service can help prevent security incidents:

**Use secure connections**

Always use encrypted connections, such as those that begin with `https://` to keep sensitive information secure in transit.

**Implement least priviledge access to resources**

When you create custom policies for Amazon Bedrock resources, grant only the permissions required to perform a task. It's recommended to start with a
minimum set of permissions and grant additional permissions as needed. Implementing least privilege access is essential to reducing the risk
and impact that could result from errors or malicious attacks. For more information, see [Identity and access management for Amazon Bedrock](security-iam.md "security-iam.md").

**Do not include PII in any of the agent resources containing customer data**

When creating, updating, and deleting agents resources (for example, when using [CreateAgent](../APIReference/API_agent_CreateAgent.md "../APIReference/API_agent_CreateAgent.md") )
do not include personally-identifiable information (PII) in any fields that do not support using customer managed key such as action group names and knowledgebase names.
For the list of fields that support using customer managed key, see [Encryption of agent resources with customer managed keys
(CMK)](cmk-agent-resources.md "cmk-agent-resources.md")
