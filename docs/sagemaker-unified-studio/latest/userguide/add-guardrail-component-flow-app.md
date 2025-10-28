# Add an Amazon Bedrock guardrail component to a flow app

In this procedure, you add a guardrail component to the [knowledge
base](nodes.md#flow-node-kb "nodes.md#flow-node-kb") node that you create in step 2 of [Create a flow app with Amazon Bedrock](build-flow.md "build-flow.md"). You
can also add a guardrail to a [prompt](nodes.md#flow-node-prompt "nodes.md#flow-node-prompt") node. To add a guardrail to a prompt node,
use the following steps. For step 7, select the prompt node (**Playlist_generator_node**).

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. If the project that you want to use isn't already open, do the following:
   1. Choose the current project at the top of the page. If a project isn't already open, choose **Select a project**.
   2. Select **Browse all projects**.
   3. In **Projects** select the project that you want
      to use.

4. Choose the **Build** menu option at the top of the page.
5. In **MACHINE LEARNING & GENERATIVE AI** choose **My apps**.
6. open the flow app that you created in [Create a flow app with Amazon Bedrock](build-flow.md "build-flow.md").
7. In the canvas, select the knowledge base node (**Local_bands_knowledge_base**).
8. In the **flow builder** pane, choose the configure tab.
9. In the **Guardrail details** section do one of the following:
   - Select an existing guardrail to use
   - Choose **Create a new guardrail** to create a new guardrail. Then do the following:
     1. For **Guardrail name**. enter a name for the guardrail.
     2. For **Guardrail description** enter a description for the guardrail.
     3. In **Content filters** do the following.
        1. Select **Enable content
           filters** to turn on content filtering.
        2. For **Filter for prompts**, choose the filters that you want
           to apply to prompts. For more information, see [Content filters](guardrails.md#guardrails-studio-content-filters "guardrails.md#guardrails-studio-content-filters").
        3. If you want the filter to apply to responses that the model generates, select
           **Apply the same filters for responses**.

     4. In **Blocked messsaging** do the following:
        1. For **Blocked messaging for
           prompts** enter a message to display when the guardrail blocks content in the prompt.
        2. If you want to show a different message when the guardrail blocks content, do the following:
           1. Clear **Apply the same message for blocked responses**.
           2. For **Blocked messaging for
              responses**, enter a message to display when the guardrail blocks content in the
              response from the model.

     5. Add a denied topic filter by doing the following:
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

     6. Choose **Create** to create the guardrail.
     7. Add the guardrail component to a chat agent app by doing [Add an Amazon Bedrock guardrail component to a chat agent app](add-guardrail-component-chat-app.md "add-guardrail-component-chat-app.md").

10. Choose **Save** to save your changes to your flow app.
11. Test your prompt by doing the following:
    1. On right side of the app flow page, choose
       **<** to open the test pane.
    2. In **Enter prompt**, enter a phrase that violates your guardrail.
    3. Press Enter on the keyboard or choose the run button to test the prompt.
    4. In the response you should see the text **guardrail applied** under the
       affected prompt. Choose the prompt to see the reason why the guardrail rejected the prompt.
