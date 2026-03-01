# Using Amazon Q Business built-in plugins

After plugins have been configured, you can use them to perform supported actions in your
Amazon Q Business web experience chat. This topic provides an overview of how to
use plugins.

###### Important

Once configured, all authorized Amazon Q web experience end users can use
plugins to perform supported actions. If a plugin is activated for an application, end
users will see an option to **Use a plugin**. If a plugin is
deactivated, users won't see an option to use a plugin. If your [Admin
controls and guardrails](guardrails.md "guardrails.md") settings allow Amazon Q to automatically
orchestrate chat queries across plugins and data sources, your plugin actions can be
automatically selected by Amazon Q during chat. End user access to plugins
can't be customized.

###### Topics

- [Performing a plugin action](#end-user-plugin-flow "#end-user-plugin-flow")
- [Example plugin action prompts](#plugin-prompts "#plugin-prompts")

## Performing a plugin action

###### Note

If your [Admin controls and guardrails](guardrails.md "guardrails.md") settings allow
Amazon Q to automatically orchestrate end user chat queries across
plugins and data sources, plugin actions will be automatically activated by Amazon Q for your end user during chat. In that case, your end user won't
have to follow the steps below.

The following describes how to perform a plugin action from within a web experience
chat using both the console and the API.

Console
**Performing a plugin action**

1. Navigate to the deployed web experience URL and sign with your
   credentials on the login screen.
2. From conversation settings, choose **Use a
   plugin**.
3. You can choose to enact plugin actions in two ways:
   1. Ask to perform an action directly. For example: Create a
      Jira ticket for a broken mouse. See [Quick create](using-plugins.md#quick-create "using-plugins.md#quick-create") for more
      details.
   2. Start chatting in your web experience to find answers to
      your questions. Then choose to include the conversation
      context in any plugin action that you take. For example:
      Summarize this conversation and create a Jira ticket. For
      more information, see [Contextual create](using-plugins.md#contextual-create "using-plugins.md#contextual-create").

4. In response to your prompt for an action, Amazon Q
   displays a review form where you fill in the necessary information
   required to successfully complete an action.
5. To successfully complete the action, you need to submit it. Your
   web experience will display a success message if the action
   succeeds, or an error message if the action fails.

API
**Performing a plugin action**

```
aws qbusiness chat-sync --application-id '${application-id}' \
--user-message "Create an issue in Jira for broken button in web application" \
--clientToken '${user-oauth-token} ' \
--chat-mode PLUGIN_MODE \
--chat-mode-configuration '{
    "pluginConfiguration": {
        "pluginId":"${plugin-id}"
        }
    }'
```

## Example plugin action prompts

There are two ways you can choose to use plugins in your web experience chat,
_quick creation_ and _contextual
creation_.

###### Topics

- [Quick create](#quick-create "#quick-create")
- [Contextual create](#context-create "#context-create")

### Quick create

Using quick creation you can directly instruct your web experience to perform a
plugin action. For example:

- `Create a Zendesk ticket for a broken
mouse`
- `Log an incident in ServiceNow for network
outage`
- `Cut an issue in Jira for a broken link on a web
page`
- `Create a Salesforce case for a missing
invoice`

### Contextual create

Using contextual creation you can include conversation contexts to create tickets.
For example, consider the following example conversation flows:

###### Example contextual create actions

- [Example 1: Create a ServiceNow incident](#context-create-servicenow "#context-create-servicenow")
- [Example 2: Create a ZenDesk ticket](#context-create-zendesk "#context-create-zendesk")
- [Example 3: Create a Salesforce case](#context-create-salesforce "#context-create-salesforce")
- [Example 4: Create a Jira issue](#context-create-jira "#context-create-jira")

#### Example 1: Create a ServiceNow incident

- **User prompt 1** – `How to
resolve network issues`
- **Amazon Q response** –
  `Sample response`
- **User prompt 2** – `How to
reset my router`
- **Amazon Q response** –
  `Sample response`
- **User action request** –
  `Summarize this conversation and create a
ServiceNow incident`

#### Example 2: Create a ZenDesk ticket

- **User prompt 1** – `Compare
Amazon Kendra with OpenSearch`
- **Amazon Q response** –
  `Sample response`
- **User action request** –
  `Create a Zendesk ticket to migrate to
Amazon Kendra`

#### Example 3: Create a Salesforce case

- **User prompt 1** – `Where is
the IT office located`
- **Amazon Q response** –
  `Sample response`
- **User prompt 2** – `What
floor is the office located in`
- **Amazon Q response** –
  `Sample response`
- **User action request** –
  `Create a case in Salesforce summarizing this
conversation`

#### Example 4: Create a Jira issue

- **User prompt 1** – `How do I
enable auto-scaling in EC2`
- **Amazon Q response** –
  `Sample response`
- **User prompt 2** – `How do I
create an auto-scaling group`
- **Amazon Q response** –
  `Sample response`
- **User action request** –
  `Summarize this conversation and create an issue in
Jira`
