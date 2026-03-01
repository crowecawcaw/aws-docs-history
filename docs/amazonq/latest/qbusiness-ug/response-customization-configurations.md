# Managing response configurations

When you create an Amazon Q Business application, Amazon Q Business
applies default response settings to it. You can customize responses for a Amazon Q Business application using the AWS Management Console and the API.

###### Response customization management

- [Creating custom response settings](#create-response-configuration "#create-response-configuration")
- [Editing response customization settings](#edit-response-configuration "#edit-response-configuration")
- [Deleting existing response customization settings](#delete-response-configuration "#delete-response-configuration")
- [Listing response customization settings](#list-response-configurations "#list-response-configurations")

## Creating custom response settings

You can customize Amazon Q Business responses using the AWS Management Console or the
[CreateChatResponseConfiguration](../api-reference/API_CreateChatResponseConfiguration.md "../api-reference/API_CreateChatResponseConfiguration.md") API
operation. The following tabs provide a procedure for the console and code examples
for the AWS CLI.

###### Note

To optimize performance and accuracy, Amazon Q Business may pre-process
custom prompts before using them to generate responses.

Console
**To customize responses**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In the navigation pane, choose
   **Applications**, and then select your
   application.
3. Choose **Enhancements** from the navigation
   menu, and then select **Response
   customization**.
4. From **Response customization**, choose
   **Edit**.
5. In **Edit response settings**, in
   **Persona**, do the following:
   1. For **Define assistant's identity**,
      define the persona for your assistant. You can choose
      between selecting the default Amazon Q Business
      identity or defining a custom identity for your
      assistant.
   2. For **Describe assistant's
      perspective**, select the point of view for
      assistant responses. You can choose between selecting
      the default Amazon Q Business perspective or
      defining a custom role and perspective for your
      assistant.
   3. For **Describe assistant's
      audience**, specify the intended audience for
      responses. You can choose between selecting the default
      Amazon Q Business perspective or defining a
      specific audience that your assistant will be
      interacting with.

6. In **Edit response settings**, in
   **Response preference**, do the
   following:
   1. For **Set default response style**,
      choose the formatting style for responses. You can
      choose between selecting the default Amazon Q Business response style or defining a custom
      response style for your assistant.
   2. For **Set default response tone**,
      select the communication style for responses. You can
      choose between selecting the default Amazon Q Business response tone or defining a custom
      response tone for your assistant.
   3. For **Set response length**, choose
      the appropriate level of detail for responses. You can
      choose between selecting the default Amazon Q Business response length or defining a custom
      response length for your assistant.

7. For **Additional instructions –
   _Optional_**, enter any
   other specific guidance for response generation.
8. Choose **Save** to save your
   configuration.

AWS CLI
**To create a response
configuration**

```

aws qbusiness create-chat-response-configuration \
--application-id `application-id` \
--display-name `configuration-name` \
--client-token `client-token` \
--response-configurations '[
  {
    "instructionCollection": {
      "responseLength": "`DETAILED`",
      "targetAudience": "`TECHNICAL_EXPERTS`",
      "perspective": "`FIRST_PERSON`",
      "outputStyle": "`BULLET_POINTS`",
      "identity": "`ASSISTANT`",
      "tone": "`PROFESSIONAL`",
      "customInstructions": "`Provide detailed technical explanations with code examples when appropriate.`",
      "examples": "`Example 1: When asked about Lambda, explain the service, its key features, and include a simple code example.`"
    }
  }
]'
```

## Editing response customization settings

You can edit an existing response configuration using the AWS Management Console or the [UpdateChatResponseConfiguration](../api-reference/API_UpdateChatResponseConfiguration.md "../api-reference/API_UpdateChatResponseConfiguration.md") API
operation. The following tabs provide a procedure for the console and code examples
for the AWS CLI.

Console
**To edit response customization
settings**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In the navigation pane, choose
   **Applications**, and then select your
   application.
3. Choose **Enhancements** from the navigation
   menu, and then select **Response
   customization**.
4. From **Response customization**, choose
   **Edit**.
5. In **Edit response settings**, modify the
   configuration settings as needed.

###### Note

You can also reset an all existing customizations to the
default used by Amazon Q Business. To do so, select
**Reset to defaults**. 6. Choose **Save** to apply your changes.

AWS CLI
**To update a response
configuration**

```

aws qbusiness update-chat-response-configuration \
--application-id `application-id` \
--chat-response-configuration-id `configuration-id` \
--display-name `updated-name` \
--client-token `client-token` \
--response-configurations '[
  {
    "instructionCollection": {
      "responseLength": "`CONCISE`",
      "targetAudience": "`GENERAL_USERS`",
      "perspective": "`SECOND_PERSON`",
      "outputStyle": "`PARAGRAPHS`",
      "identity": "`EXPERT`",
      "tone": "`FRIENDLY`",
      "customInstructions": "`Provide clear, concise explanations suitable for general users.`",
      "examples": "`Example 1: When asked about Lambda, provide a brief overview in simple terms.`"
    }
  }
]'
```

## Deleting existing response customization settings

You can delete configured response customizations using the [DeleteChatResponseConfiguration](../api-reference/API_DeleteChatResponseConfiguration.md "../api-reference/API_DeleteChatResponseConfiguration.md") API
operation. If you're using the AWS Management Console, you can't reset the response
customizations you have configured to default. The following tabs provide a
procedure for the console and code examples for the AWS CLI.

Console
**To reset response customization settings to
default**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In the navigation pane, choose
   **Applications**, and then select your
   application.
3. Choose **Enhancements** from the navigation
   menu, and then select **Response
   customization**.
4. From **Response customization**, choose
   **Edit**.
5. In **Edit response settings**, select
   **Reset to defaults**. This resets all
   existing customizations to the default used by Amazon Q Business.
6. Choose **Save** to apply your changes.

AWS CLI
**To delete a response
configuration**

```

aws qbusiness delete-chat-response-configuration \
--application-id `application-id` \
--chat-response-configuration-id `configuration-id`
```

## Listing response customization settings

You can list all available response configurations for an application using the
AWS Management Console or the [GetChatResponseConfiguration](../api-reference/API_GetChatResponseConfiguration.md "../api-reference/API_GetChatResponseConfiguration.md") and
[ListChatResponseConfigurations](../api-reference/API_ListChatResponseConfigurations.md "../api-reference/API_ListChatResponseConfigurations.md") API
operations. The following tabs provide a procedure for the console and code examples
for the AWS CLI.

Console
**To list response customization
settings**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In the navigation pane, choose
   **Applications**, and then select your
   application.
3. Choose **Enhancements** from the navigation
   menu, and then select **Response
   customization**. You'll see a list of existing
   response customizations displayed on the page.

AWS CLI
**To list response
configurations**

```

aws qbusiness get-chat-response-configuration \
--application-id `application-id` \
--chat-response-configuration-id `chat-response-configuration-id`
```

```

aws qbusiness list-chat-response-configurations \
--application-id `application-id` \
--max-results `10` \
--next-token `next-token`
```
