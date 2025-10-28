# View information about versions of a prompt in Prompt management

To learn how to view information about a version of your prompt, choose the tab for your preferred method, and then follow the steps:

Console

###### To view information about a version of your prompt

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Select **Prompt management** from the left navigation pane. Then, choose a prompt in the **Prompts** section.
3. In the **Prompt versions** section, choose a version.
4. In the **Version details** page, you can see information about the version, the prompt message, and its configurations. For more information about testing a version of the prompt, see [Test a prompt using Prompt management](prompt-management-test.md "prompt-management-test.md").

API
To get information about a version of your prompt, send a [GetPrompt](../APIReference/API_agent_GetPrompt.md "../APIReference/API_agent_GetPrompt.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the ARN or ID of the prompt as the `promptIdentifier`. In the `promptVersion` field, specify the version number.
