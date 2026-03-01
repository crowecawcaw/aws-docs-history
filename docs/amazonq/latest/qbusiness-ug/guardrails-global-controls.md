# Using global controls in Amazon Q Business

You can use Amazon Q Business global controls to configure settings that
apply to conversations in your application environment.

###### Note

You can't create or delete guardrail global controls. You can only update
existing global controls in your application environment.

The following are the global features that you can customize:

###### Global controls

- [Response settings](#guardrails-global-response "#guardrails-global-response")
- [Chat orchestration settings](#guardrails-global-orchestration "#guardrails-global-orchestration")
- [Feature settings](#guardrails-global-feature "#guardrails-global-feature")
- [Blocked phrases](#guardrails-global-blocked "#guardrails-global-blocked")
- [Customizing global controls](#guardrails-global-controls-customizing "#guardrails-global-controls-customizing")

## Response settings

###### Important

If you're changing response settings for an Amazon Q Business
application environment created and deployed before 16 April, 2024, you need to update
your web experience service role. For information on service role
permissions needed, see [IAM role for an Amazon Q Business web
experience](iam-roles.md#deploy-experience-iam-role "iam-roles.md#deploy-experience-iam-role"). For information on how to update your web experience
service role, see [Updating a web experience](supported-exp-actions.md#update-web-experience "supported-exp-actions.md#update-web-experience").

###### Note

Displaying sample prompts to your end user using the Amazon Q Business
[Quick prompts](quick-prompts.md "quick-prompts.md") feature might not work if you
choose to restrict response generation to enterprise data.

When you update your application environment guardrails, you can use **Response
settings** to change this behavior in the following ways:

- **Allow end users to send queries directly to the
  LLM** – Give end users the option to either generate
  LLM-only responses or only generate responses from connected data
  sources. If you choose to activate this option, end users will be able
  to toggle between generating responses from either the data sources you
  have connected to your application environment or use only the LLM to generate
  responses.

If you choose to activate this feature for your end users, they will
see the option to turn **All data sources off** or
**Respond from approved sources** in their web
experience. If you turn this feature off, then this option won't be
available—or displayed—to end users in a web
experience.

###### Note

As of Oct 31, 2024, once you have created a new Amazon Q Business application environment, this setting will be
_enabled by default_, even if the Admin has
not yet connected any enterprise data sources.

For existing application environments, this setting will _remain as
previously configured_.

- **Allow Amazon Q Business to fall back to
  LLM knowledge** – Allow Amazon Q Business to
  use its LLM knowledge to generate responses when it can’t find responses
  from your connected data sources. If you choose to activate this mode,
  and haven't given your end users the option to choose how responses are
  generated, your application environment will default to producing responses using
  the LLM when it can't find information in your data sources.
- **Personalize responses** – Allow
  Amazon Q Business to customize chat responses to end users
  using metadata associated with them—specifically address and job
  related information—in your IAM Identity Center instance.

You must have already added this information in IAM Identity Center for response
personalization to work as intended. For more information on how to
configure your IAM Identity Center instance for personalization see [Personalizing chat responses](personalizing-chat-responses.md "personalizing-chat-responses.md").

- **Enable hallucination mitigation** – Allow
  Amazon Q Business to check the chat responses it generates for
  [hallucinations](concepts-terms.md#hallucination "concepts-terms.md#hallucination"). If a hallucination is
  detected with high confidence, Amazon Q Business corrects the
  inconsistencies in its response real-time during chat and generates a
  new, edited message.

The hallucination mitigation feature is only available for retrieval
augmented generation (RAG) responses from data connected to the
application—either through connected data sources, or files
uploaded during chat (up to 100,000 characters).

Hallucination mitigation isn't supported for the following use
cases:

    + Applications where [chat orchestration](guardrails-global-controls.md#guardrails-global-orchestration "guardrails-global-controls.md#guardrails-global-orchestration") is
     enabled.
    + [Plugin](plugins.md "plugins.md") workflows.
    + Responses generated from tabular data, or from transcripts of
     images, audio and video. Hallucination mitigation applies only
     to responses generated from textual data.

###### Important

Activating hallucination mitigation will increase chat response
latency.

Global controls apply to all supported conversation interactions, except when
it conflicts with a specific topic-level control. In that case, a topic-level
control takes precedence.

## Chat orchestration settings

You can use **Chat orchestration settings** to automatically
manage chat requests across configured plugins and data sources in your Amazon Q Business application. If you activate chat orchestration, Amazon Q Business automatically routes chat requests to [plugins](plugins.md "plugins.md"), integrating enterprise data and relevant actions within a
single chat response. Users get direct responses without manual plugin
selection.

###### Note

Chat orchestration is optimized to work for English language content. For
more details on language support in Amazon Q Business, see [Supported languages](supported-languages.md "supported-languages.md"). Additionally, the
[hallucination mitigation](hallucination-reduction.md "hallucination-reduction.md") feature won't work if chat
orchestration controls are enabled for your application.

The following are the key features of chat orchestration:

- **Unified response integration** –
  Lets Amazon Q Business combine its [retrieval augmented generation (RAG)
  workflow](concepts-terms.md#retrieval-augmented-generation "concepts-terms.md#retrieval-augmented-generation") with plugin actions. This allows Amazon Q Business to provide comprehensive answers in natural language
  during conversations. For example, Amazon Q Business can explain
  paid time-off (PTO) policy from company data and create a time-off
  request at the same time.
- **Intelligent action detection** –
  Allows Amazon Q Business to automatically identify read-only chat
  requests (like checking ticket counts) and write actions (like creating
  a ticket) and present forms for user validation.
- **Smart plugin management** –
  Allows Amazon Q Business to automatically select appropriate
  plugins without manual user selection while managing multiple complex
  plugin interactions.
- **User driven experience** –
  Enables Amazon Q Business to ask for user clarification when
  multiple actions are possible, validating actions before taking them,
  and guiding the user through the information needed to perform an
  action.

If you deactivate chat orchestration, Amazon Q Business won't relay
queries across data sources and plugins. Users must manually select to use
plugin mode to invoke a plugin action from chat.

If you're using an [Quick plugin](quicksight-plugin.md "quicksight-plugin.md") (fully-integrated with
Amazon Q Business and not available for manual selection by users
during chat), activating chat orchestration affects its behavior. With chat
orchestration enabled, an Quick plugin only activates if:

- No other plugin actions (read or write requests requiring additional
  end user input through forms) are detected, or, in progress.
- No end user authentication requests are pending.

## Feature settings

You can control whether end users can upload files during chat to ask
questions based on the uploaded document. By default, your application environment allows
your end users to directly upload files in chat.

You can also choose whether to allow end users in a web experience to create
and use Amazon Q Apps. Amazon Q Apps relies on LLM knowledge to work.

## Blocked phrases

You can define blocked phrases for your application environment. Amazon Q Business
ensures that chat responses don't include these words. You can choose up to 20
words.

Additionally, you can optionally configure a custom message to be displayed to
your end users in response to any mention of blocked phrases during chat. You
can use this message to inform them that word is blocked and provide them with
further guidance on next steps.

By default, your application environment doesn't define any blocked words. You can
choose to add these words when you edit and update your global control
guardrails.

## Customizing global controls

When you create an Amazon Q Business application environment, it's assigned the
following default global controls:

- An option to generate responses from either enterprise data or
  LLMs.
- Response personalization is activated.
- Automatic orchestration of end user chat requests across any Amazon Q Business plugins and data sources you’ve configured.
- File upload by end user during chat is activated.
- Q Apps creation is activated.
- Hallucination mitigation is deactivated. To turn hallucination
  mitigation on, you must first deactivate chat orchestration.

To update global topic controls for your web experience chat, you can use the
AWS Management Console or the [UpdateChatControlsConfiguration](../api-reference/API_UpdateChatControlsConfiguration.md "../api-reference/API_UpdateChatControlsConfiguration.md")
API operation. The following tabs provide a procedure for the console and code
examples for the AWS CLI.

###### Note

You can't create or delete guardrail global controls. You can only update
existing global controls in your application environment.

Console
**To update a global control
guardrail**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application environment from the list of applications.
3. From the left navigation menu, choose
   **Enhancements**, and then choose
   **Guardrails**.
4. In **Guardrails**, from **Global
   controls**, choose
   **Edit**.
5. In **Application guardrails**, do the
   following:
   - For **Response settings** do the
     following:
     - **Allow end users to send queries directly
       to the LLM** – If you choose to
       activate this option, end users will be able to
       toggle between generating responses from either
       the data sources you have connected to your
       application environment or use only the LLM to generate
       responses.

     ###### Note

     If you choose to enable this option, your
     end users will have the option to generate
     LLM-only responses even if you don't allow Amazon Q to user LLM knowledge to generate
     responses.

     For more information, see [Using global controls in
     Amazon Q Business](guardrails-global-controls.md "guardrails-global-controls.md").
     - **Allow Amazon Q Business to fall
       back to LLM knowledge** – Choose
       this option if you want to generate responses from
       your application environment's LLM world knowledge when it
       can't find information in your connected data
       sources. The default is to restrict responses to
       enterprise data. For more information, see [Using global controls in
       Amazon Q Business](guardrails-global-controls.md "guardrails-global-controls.md").
     - **Personalize
       responses** – Allow Amazon Q Business to customize chat responses to end
       users using metadata associated with
       them—specifically address and job related
       information—in your IAM Identity Center instance.

     ###### Note

     You must have already added this information
     in IAM Identity Center for response personalization to work as
     intended. For more information on how to configure
     your IAM Identity Center instance for personalization see [Personalizing chat
     responses](personalizing-chat-responses.md "personalizing-chat-responses.md").
     - **Enable hallucination
       mitigation** – Allow Amazon Q Business to check the chat responses it
       generates for [hallucinations](concepts-terms.md#hallucination "concepts-terms.md#hallucination"). If a
       hallucination is detected with high confidence,
       Amazon Q Business corrects the
       inconsistencies in its response real-time during
       chat and generates a new, edited message.

     ###### Note

     You must deactivate **Chat
     orchestration settings** before you can
     activate hallucination mitigation.

6. For **Chat orchestration settings**,
   activate to automatically manage chat requests across
   configured plugins and data sources in your Amazon Q Business application. If you activate chat
   orchestration, Amazon Q Business automatically routes
   chat requests to [plugins](plugins.md "plugins.md"), integrating
   enterprise data and relevant actions within a single chat
   response. Users get direct responses without manual plugin
   selection.

###### Note

You must deactivate **Enable hallucination
mitigation** before you can activate chat
orchestration. 7. For **Feature settings**, choose whether
your end users will be allowed to upload files directly in
chat to ask questions based on file content and whether
Amazon Q Apps will be enabled for your application environment. 8. _ For **Blocked words** –
Define blocked words for the application environment. The
application environment will not respond to questions that
contain these words or mention them in any
responses.
_ For **Messaging shown for blocked
words** – Choose to create a
custom response for your end users informing them of
blocked word usage and any next steps to
take. 9. Choose **Save**.

AWS CLI
**To update a global control
guardrail**

```

aws qbusiness update-chat-controls-configuration \
--application-id `application-id` \
--blocked-phrases-configuration-update '{"blockedPhrasesToCreateOrUpdate":["`example phrase 1`", "`example phrase 2`"],"blockedPhrasesToDelete":["`example phrase 1`", "`example phrase 2`"],"systemMessageOverride":"user facing message when blocked phrase encountered"}' \
--client-token `clientToken` \
--response-scope `ENTERPRISE_CONTENT_ONLY` | `EXTENDED_KNOWLEDGE_ENABLED` \
--creator-mode-configuration creatorModeControl=`ENABLED` | `DISABLED` \
--orchestration-configuration orchestrationControl=`ENABLED` | `DISABLED` \
--hallucination-reduction-configuration '{"hallucinationReductionControl": "`ENABLED`" | "`DISABLED`"}'

```
