# Disable a multi-agent collaboration

You can disable multi-agent collaboration at any time. Before you disable multi-agent collaboration, make sure that you've [disassociated all collaborator agents](disassociate-collaborator-agent.md "disassociate-collaborator-agent.md")
that are associated with the supervisor agent.

You can disable multi-agent collaboration in the Amazon Bedrock console, using the APIs, using the AWS CLI, or by using the AWS SDK. To learn how to create a multi-agent collaboration, choose the tab for your preferred method, and then follow the steps:.

Console

###### To disable multi-agent collaboration,

1. If you're not already in the agent builder, do the following:
   1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
      [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
   2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
   3. Choose **Edit in Agent builder**.

2. In the **Agent builder**, scroll down to the **Multi-agent collaboration** section and choose **Edit**.
3. In the **Multi-agent collaboration** page, in the
   **Collaboration status** section, turn off
   **Multi-agent collaboration**. This agent is no
   longer associated with any other agents. You can continue to use
   this agent as a stand-alone agent.
4. After you've finished disabling multi-agent collaboration, choose **Save** and then **Prepare** to test your updated agent configurations.
   To learn how to test your updated agent configurations, see [Test and troubleshoot agent behavior](agents-test.md "agents-test.md").
5. To return to the **Agent Details** page, choose **Save and exit**.

API
To disable multi-agent collaboration, send an [UpdateAgent](../APIReference/API_agent_UpdateAgent.md "../APIReference/API_agent_UpdateAgent.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Because all fields will be overwritten, include both fields that you want to update as well as fields that you want to keep the same.

To apply the changes to the working draft, send a [PrepareAgent](../APIReference/API_agent_PrepareAgent.md "../APIReference/API_agent_PrepareAgent.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Include the `agentId` in the request. The changes apply to the `DRAFT` version, which the `TSTALIASID` alias points to.

You must minimally include the following fields:

| Field                | Use case                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| agentResourceRoleArn | To specify an ARN of the service role with permissions to call API operations on the agent                                            |
| foundationModel      | To specify a foundation model (FM) for the agent to orchestrate<br>with                                                               |
| instruction          | To provide instructions to tell the agent what to do. Used<br>in the $instructions$ placeholder of the orchestration prompt template. |
| agentCollaboration   | To disable multi-agent collaboration, set this field to `DISABLED`                                                                    |
