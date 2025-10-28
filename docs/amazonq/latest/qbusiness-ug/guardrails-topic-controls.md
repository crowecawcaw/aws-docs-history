# Using topic-level controls in Amazon Q Business

You can use topic-level controls to specify special topics within your
application environment. You can configure rules to customize how Amazon Q Business
should respond when a chat message matches a special topic. To streamline your
application environment's response, you provide a name and a short description for how the
large language model (LLM) should respond based on the topic-specific guardrail
you're building. You can configure up to 2 topic-level controls.

Topic-level controls provide fine-grained customization for your application environment.
For example, you can define a global control guardrail that allows your
application environment to generate responses using model knowledge. You can also use a
content retrieval rule to limit response generation for specific topics to
enterprise content.

The following are the topic-level guardrails that you can customize:

###### Topic level guardrails

- [LLM prompt control](#guardrails-topic-controls-messages "#guardrails-topic-controls-messages")
- [Application behavior
  rules](#guardrails-topic-controls-app-rules "#guardrails-topic-controls-app-rules")
- [Creating topic
  controls](#guardrails-topic-controls-customizing "#guardrails-topic-controls-customizing")

## LLM prompt control

You can add up to 5 representative messages that you expect end users to
submit about this topic. You can also configure natural language descriptions to
define the boundaries of the topic. Amazon Q Business uses these messages
to check the responses that it generates for restricted content.

## Application behavior

rules

You can configure behavior rules that control how Amazon Q Business
responds for each special topic that you specify.

###### Note

You can specify up to 5 rules per special topic.

###### Rules

- [Answer using
  enterprise data](#guardrails-topic-controls-rules-data "#guardrails-topic-controls-rules-data")
- [Blocking special
  topics](#guardrails-topic-controls-rules-block "#guardrails-topic-controls-rules-block")

### Answer using

enterprise data

When your application environment encounters a special topic, you can choose to
allow it to answer from your enterprise data. If you allow responses from
your enterprise data, you can further restrict which data sources in your
application environment that your responses are generated from.

You can also choose to specify the specific users or groups within your
application environment to apply this rule to, using either an inclusion logic or an
exclusion logic. You can’t use both kinds of logic at once. If a user is a
member of a group with conflicting rules defined, Amazon Q Business
will apply the more restrictive rule to that user.

### Blocking special

topics

When your application environment encounters a special topic, you can choose to
block responses completely. If you do so, you can configure a custom message
to display to your end users in response to any mention of blocked topics
during chat. Use this message to inform your end users that the topic is
blocked and provide them with further guidance on next steps.

You can also choose to specify the specific groups within your
application environment to apply this rule to, using either an inclusion logic or an
exclusion logic. You can’t use both kinds of logic at once. If a user is a
member of a group with conflicting rules defined, Amazon Q Business
will apply the more restrictive rule to that user.

Not specifying an inclusion or exclusion logic will result in the rule
being applied to all users.

###### Note

User level rule creation is not currently supported for the following
IAM Identity Provider access management methods: SAML and OIDC.

## Creating topic

controls

To create an Amazon Q Business topic-level control for your web
experience chat, you can use AWS Management Console or the [UpdateChatControlConfiguration](../api-reference/API_UpdateChatControlsConfiguration.md "../api-reference/API_UpdateChatControlsConfiguration.md")
operation. The following tabs provide a procedure for the console and code
examples for the AWS CLI.

Console
**To create a topic control**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application environment from the list of applications.
3. From the left navigation menu, choose
   **Enhancements**, and then choose
   **Guardrails**.
4. For **Guardrails**, from **Topic
   specific controls**, choose **Create
   topic control**.
5. For **Create topic specific controls**,
   enter the following information:
   - **Name** – Enter a name
     for your topic-specific control.
   - **Description** – A
     natural language description for your topic control
     configuration. Use this to help the LLM better
     identify queries associated with the topic control
     you're configuring.

6. For **Example chat messages**, enter
   representative phrases that you expect a user to type to
   invoke this topic. You can add up to 5 messages.
7. (Optional) To configure a rule, choose **Add new
   rule**.
8. For **Rule 1**, enter the following
   information:
   - In **Behavior in response to
     guardrail**, for
     **Behavior** – Choose how
     Amazon Q Business will respond to blocked
     topics: **Answer using enterprise
     data** or **Block
     completely**.
   - If you choose **Block
     completely** – Choose to include a
     custom message to inform your end user of restricted
     topics from chat and suggest follow up
     actions.
   - If you choose **Answer using enterprise
     data**, **Data source
     requirements** – Choose data
     sources that Amazon Q Business will use to
     generate responses.

9. For **User handling**, specify the users
   or groups that this topic control rule applies to and any
   users or groups that are exempt from this rule.
10. Choose **Save**.

AWS CLI
**To create a topic control**

```

aws qbusiness update-chat-controls-configuration \
--application-id `application-id` \
--client-token `clientToken` \
--topic-configurations-to-create-or-update '[{"name":"`name`","description":"`description`","exampleChatMessages":["`message1`", "`message2`"],"rules":[{"includedUsersAndGroups":{"userIds":["`userId1`","`userId2`"],"userGroups":["`userGroup1`","`userGroup2`"]},"ruleType": "CONTENT_BLOCKER_RULE","ruleConfiguration":{"contentBlockerRule":{"systemMessageOverride":"`custom_message`"}}},{"excludedUsersAndGroups":{"userIds":["`id1`", "`id2`"],"userGroups":["`group1`", "`group2`"]}, "ruleType": "CONTENT_RETRIEVAL_RULE", "ruleConfiguration":{"contentRetrievalRule":{"eligibleDataSources":[{"indexId":"`index-id1`","dataSourceId":"`data-source-id1`"},{"indexId":"`index-id2`","dataSourceId":"`data-source-id2`"}]}}}]}]' \
--topic-configurations-to-delete '{"name":"`existing-topic-name`"}'

```

###### Note

The user IDs you add to configure topic controls must already
exist in your Identity Provider (IdP). You are responsible for
validating any user groups you add.
