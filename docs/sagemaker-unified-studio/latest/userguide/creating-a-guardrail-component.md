# Create an Amazon Bedrock guardrail component

You can create a guardrail as a component in an Amazon Bedrock in SageMaker Unified Studio project. You can then add the guardrail
component to a chat agent app. You can also create a guardrail component while you are creating a chat agent app. For an
example, see [Step 2: Add a guardrail to your chat agent app](create-chat-app-with-components.md#chat-app-add-guardrail "create-chat-app-with-components.md#chat-app-add-guardrail").

###### To create a guardrail component

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. In the left navigation pane, under **Generative AI**, choose **AI apps**.
4. From the project selector dropdown at the top of the page, choose the project that you want to use.
5. In the left pane, choose **Asset gallery**.
6. Choose **My components**.
7. In the **Components** section, choose **Create
   component** and then **Guardrail**. The **Create
   guardrail** pane is shown.
8. For **Guardrail name**. enter a name for the guardrail.
9. For **Guardrail description** enter a description for the guardrail.
10. In **Content filters** do the following.
    1. Select **Enable content
       filters** to turn on content filtering.
    2. For **Filter for prompts**, choose the filters that you want
       to apply to prompts. For more information, see [Content filters](guardrails.md#guardrails-studio-content-filters "guardrails.md#guardrails-studio-content-filters").
    3. If you want the filter to apply to responses that the model generates, select
       **Apply the same filters for responses**.

11. In **Blocked messsaging** do the following:
    1. For **Blocked messaging for
       prompts** enter a message to display when the guardrail blocks content in the prompt.
    2. If you want to show a different message when the guardrail blocks content from a model's
       response, do the following:
       1. Clear **Apply the same message for blocked responses**.
       2. For **Blocked messaging for
          responses**, enter a message to display when the guardrail blocks content in the
          response from the model.

12. Add a denied topic filter by doing the following:
    1. Choose **Use advanced features**.
    2. Choose **Denied topics**.
    3. Choose **Add topic**.
    4. For **Name**, enter a name for the filter.
    5. For **Definition for
       topic**, enter a definition for the content that you want to deny.
    6. (Optional) To help guide the guardrail, do the folllowing:
       1. Choose **Sample phrases - optional**.
       2. For **Sample phrases**, enter a phrase.
       3. Choose **Add phrase**.
       4. Add up to four more phrases by repeating the previous two steps.
       5. Choose **Save**.For information about denied topics, see [Denied topics](guardrails.md#guardrails-topic-policies "guardrails.md#guardrails-topic-policies").

13. Choose **Create** to create the guardrail.
14. Add the guardrail component to a chat agent app by doing [Add an Amazon Bedrock guardrail component to a chat agent app](add-guardrail-component-chat-app.md "add-guardrail-component-chat-app.md").
