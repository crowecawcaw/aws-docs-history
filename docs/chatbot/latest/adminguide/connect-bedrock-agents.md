AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Invoking Amazon Bedrock Agents from chat channels using Amazon Q Developer in chat applications

You can invoke Amazon Bedrock Agents directly from your chat channels using Amazon Q Developer in chat applications.
Amazon Bedrock Agents are fully managed capabilities that make it easier for you to create generative AI-based applications that can complete complex tasks for a wide range of use cases and deliver up-to-date answers based on proprietary knowledge sources.
You can use agents to increase productivity, improve your customer experience, and automate workflows. For more information, see [Automate tasks in your application using conversational agents](../../../bedrock/latest/userguide/agents.md "../../../bedrock/latest/userguide/agents.md") in the _Amazon Bedrock User Guide_.

###### Topics

- [Setting up your chat channel](#bedrock-setup "#bedrock-setup")
- [Connecting Amazon Bedrock to chat channels](bedrock-connectors.md "bedrock-connectors.md")
- [Conversing with your Amazon Bedrock Agent connectors using Amazon Q Developer in chat applications](bedrock-converse.md "bedrock-converse.md")
- [Updating a connector using Amazon Q Developer in chat applications](bedrock-update.md "bedrock-update.md")
- [Quotas for Amazon Bedrock in Amazon Q Developer in chat applications](bedrock-limits.md "bedrock-limits.md")

## Setting up your chat channel

To invoke an agent from your chat channel with Amazon Q Developer in chat applications, you must ensure that both:

- The channel or user role has permission to invoke the agent.
- The channel guardrail policies include permission to invoke the agent.

###### Tip

The most minimal way to achieve this is to create a new IAM policy with just the required `InvokeAgent` permissions and add it to your channel guardrail policies.

The Amazon Q Developer in chat applications Bedrock Agent connector requires the [`bedrock:InvokeAgent`](../../../bedrock/latest/userguide/security_iam_id-based-policy-examples-agent.md#security_iam_id-based-policy-examples-perform-actions-agent "../../../bedrock/latest/userguide/security_iam_id-based-policy-examples-agent.md#security_iam_id-based-policy-examples-perform-actions-agent") IAM action.

### Example role policy

The following policy is a minimal policy statement with the permissions required to invoke a specific agent. This policy statement is added to the channel or user role
used to run AWS SDK commands in your Amazon Q Developer in chat applications channel.

```
{
  "Sid": "AllowInvokeBedrockAgent",
  "Effect": "Allow",
  "Action": "bedrock:InvokeAgent",
  "Resource": [
    "arn:aws:bedrock:aws-region:111122223333:agent-alias/AGENT12345/ALIAS12345"
  ]
}

```

###### Note

The Agent and Alias IDs are located on the Agent details page in the Amazon Bedrock console. For more information, see [View information about aliases of agents in Amazon Bedrock](../../../bedrock/latest/userguide/agents-alias-view.md "../../../bedrock/latest/userguide/agents-alias-view.md") in the _Amazon Bedrock User Guide_.
