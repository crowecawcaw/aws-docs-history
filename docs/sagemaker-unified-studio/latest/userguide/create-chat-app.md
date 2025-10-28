# Build a chat agent app with Amazon Bedrock

An Amazon Bedrock in SageMaker Unified Studio chat agent app allows users to chat with an Amazon Bedrock model through a
conversational interface, typically by sending text messages and receiving responses. The model analyzes the user's input, formulate an appropriate response,
and carries on a dialogue with the user. You can use a chat agent apps for various
purposes, such as providing customer service, answering questions, offering recommendations,
or engaging in open-ended conversations on a wide range of topics.
You can enhance a chat agent app app by integrating the following Amazon Bedrock features:

- **[Data sources](data-sources.md "data-sources.md")**
  — Enrich model responses by including context generated from an Amazon Bedrock knowledge base.
- **[Guardrails](guardrails.md "guardrails.md")** —
  Lets you implement safeguards for your chat agent app based on your use cases and responsible
  AI policies.
- **[Functions](functions.md "functions.md")** — Lets
  a model call a function to access a specific capability when handling a prompt.
  When you first create an chat agent app, you have a working draft of the app. Changes
  you make to your chat agent app apply to the working draft. You iterate on your
  working draft until you're satisfied with the behavior of your app. At any time you can save your
  chat agent app.

Once you create and save chat agent app, you can do the following:

- [Share the chat agent app](app-share.md "app-share.md") with other users.
- [Export the chat agent app](app-export.md "app-export.md") for use outside of Amazon SageMaker Unified Studio.
- Use the chat agent app as an agent node in a flow app.
  To use a chat agent app in a flow app you need to
  [deploy](app-deploy-app.md "app-deploy-app.md") the app. Amazon Bedrock in SageMaker Unified Studio deploys the app for
  you whenever you share the app with other users.

In this section you learn how to create chat agent app that uses Amazon Bedrock in SageMaker Unified Studio
components such as a [data source](data-sources.md "data-sources.md") and a [guardrail](guardrails.md "guardrails.md"). You also learn how to share your app with other
users.

###### Topics

- [Create a chat agent app with Amazon Bedrock](create-chat-app-with-components.md "create-chat-app-with-components.md")
- [Deploy an Amazon Bedrock chat agent app](app-deploy.md "app-deploy.md")
- [Share an Amazon Bedrock chat agent app](app-share.md "app-share.md")
