# Modify an Amazon Bedrock prompt

You can modify the current draft of a prompt or modify previous versions of a prompt. To modify a
prompt, you select the version of the prompt (or current working draft prompt) that you want to
modify. You then work on a draft update of the prompt. You can change the configuration for
different versions of a prompt. For example, different versions of a prompt can use different
Amazon Bedrock in SageMaker Unified Studio models or use different inference parameters.

After testing the draft prompt, you can then save the draft as a new version of the prompt.
If you want to use a new version of a prompt in a flow app, update the version of the
prompt in the app configuration. For more information, see [Step 3: Add a prompt to your flow app](build-flow.md#build-flow-prompt "build-flow.md#build-flow-prompt").

Creating a new prompt version for an already shared prompt doesn't update the users that have access
to the prompt version.

For more information about the changes you can make, see [Create an Amazon Bedrock prompt](creating-a-prompt.md "creating-a-prompt.md").

###### To modify a prompt

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. In the left navigation pane, under **Generative AI**, choose **AI apps**.
4. From the project selector dropdown at the top of the page, choose the project that contains the prompt.
5. In the left pane, choose **Asset gallery** and then **My prompts**.
6. In **Prompts**, select the prompt that you want to modify.
7. In **Configs** make changes to the model and inference parameters.
8. For **Prompt message**, use the text box to make changes to the prompt
   message.
9. (Optional) Choose **Save** to save the draft of your prompt.
10. In **Test** enter values for the prompt variables and choose run to test
    your changes.
11. When you are satisfied with your changes, choose **Create version** to
    create a new version of your prompt.
