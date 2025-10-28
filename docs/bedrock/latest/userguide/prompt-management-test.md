# Test a prompt using Prompt management

To learn how to test a prompt you created in Prompt management, choose the tab for your preferred method, and then follow the steps:

Console

###### To test a prompt in Prompt management

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Prompt management** from the left navigation pane. Then, choose a prompt in the **Prompts** section.
3. Choose **Edit in Prompt builder** in the **Prompt draft** section, or choose a version of the prompt in the **Versions** section.
4. (Optional) To provide values for variables in your prompt, you need to first select a model in the **Configurations** pane. Then, enter a **Test value** for each variable in the **Test variables** pane.

###### Note

These test values are temporary and aren't saved if you save your prompt. 5. To test your prompt, choose **Run** in the **Test window** pane. 6. Modify your prompt or its configurations and then run your prompt again as necessary. If you're satisfied with your prompt, you can choose **Create version** to create a snapshot of your prompt that can be used in production. For more information, see [Deploy a prompt to your application using versions in Prompt management](prompt-management-deploy.md "prompt-management-deploy.md").

You can also test the prompt in the following ways:

- To test the prompt in a flow, include a prompt node in the flow. For more information, see [Create and design a flow in Amazon Bedrock](flows-create.md "flows-create.md") and [Node types for your flow](flows-nodes.md "flows-nodes.md").
- If didn't configure your prompt with an agent, you can still test the prompt with an agent by importing it when testing an agent. For more information, see [Test and troubleshoot agent behavior](agents-test.md "agents-test.md").

API
You can test your prompt in the following ways:

- To run inference on the prompt, send an [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md"), [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"), or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") request with an [Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#br-rt "../../../general/latest/gr/bedrock.md#br-rt") and specify the ARN of the prompt in the `modelId` parameter.

###### Note

The following restrictions apply when you use a Prompt management prompt with `Converse` or `ConverseStream`:

    + You can't include the `additionalModelRequestFields`, `inferenceConfig`, `system`, or `toolConfig` fields.
    + If you include the `messages` field, the messages are appended after the messages defined in the prompt.
    + If you include the `guardrailConfig` field, the guardrail is applied to the entire prompt. If you include `guardContent` blocks in the [ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md") field, the guardrail will only be applied to those blocks.

- To test your prompt in a flow, create or edit a flow by sending a [CreateFlow](../APIReference/API_agent_CreateFlow.md "../APIReference/API_agent_CreateFlow.md") or [UpdateFlow](../APIReference/API_agent_UpdateFlow.md "../APIReference/API_agent_UpdateFlow.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). Include a SDK for JavaScript in Node.js of the `PromptNode` type and include the ARN of the prompt in the `promptArn` field. Then, send an [InvokeFlow](../APIReference/API_agent-runtime_InvokeFlow.md "../APIReference/API_agent-runtime_InvokeFlow.md") request with an [Agents for Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#bra-rt "../../../general/latest/gr/bedrock.md#bra-rt"). For more information, see [Create and design a flow in Amazon Bedrock](flows-create.md "flows-create.md") and [Node types for your flow](flows-nodes.md "flows-nodes.md").
- To test your prompt with an agent, use the Amazon Bedrock console (see the **Console** tab), or enter the text of the prompt into the `inputText` field of an [InvokeAgent](../APIReference/API_agent-runtime_InvokeAgent.md "../APIReference/API_agent-runtime_InvokeAgent.md") request.
