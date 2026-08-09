# Chat agent customization in Amazon Quick

When a user account subscribes to Quick, the service automatically creates a
system default chat agent. This agent powers the default chat experience, allowing
Amazon Quick users to leverage all chat functionalities (such as uploading files to chat,
using large language model (LLM) parametric knowledge, and answering from
their enterprise data) out of the box. The system default chat agent can be updated in the
Amazon Quick agent section by a select set of users who are designated as owners for the
agent by the admin.

Amazon Quick uses multiple safety controls for chat interactions in the
Amazon Quick web experience. You can configure blocked words and phrases under
**Guardrails and safety controls**. For information about built-in
safeguards and blocked words and phrases, see [AI guardrails in Amazon Quick](guardrails.md "guardrails.md").

Admins can also configure whether URLs in chat responses appear as clickable hyperlinks or plain text. This setting applies across all chat agents and flows in your instance, allowing you to control how links are presented to users.

###### Note

Admins can also control permissions for whether users can create and use chat agents
and flows. For instructions on how to do that, see [Custom permissions](../../../quicksuite/latest/userguide/create-custom-permissions-profile.md "../../../quicksuite/latest/userguide/create-custom-permissions-profile.md").

The following sections outline how to edit the system default agent and configure
clickable external links in chat responses.

###### Topics

- [Grant user permissions to edit system default chat agent](#edit-default-agent-permissions "#edit-default-agent-permissions")
- [Edit system chat agent settings](#edit-default-agent "#edit-default-agent")
- [Configure clickable external links in chat responses](#configure-clickable-links "#configure-clickable-links")

## Grant user permissions to edit system default chat agent

The system default chat agent can be edited by users the admin designates as owners to
this agent in the admin console. The following procedure shows you how to grant admin
permissions to a user so that they can edit the system default agent.

###### To grant permissions to edit system default agent

1. Log in to the Amazon Quick console.
2. Select **Manage Quick** from the Amazon Quick
   admin console.
3. From the admin console left navigation menu, select
   **Account**, and then select **Manage
   assets**.
4. In **Manage assets**, select **Chat
   agents**.
5. Select **My Assistant** from the list of chat agents shown.
   Then, from the **Actions** menu, select
   **Share**.
6. In the **Share assets** modal, use the **User or
   Group** search bar to find the user or group you want to designate
   as owners for the system agent.
7. Then, from **Permissions**, choose
   **Owner**. Then, select **Share**.

## Edit system chat agent settings

To customize your system chat agent, users designated as owners need to login to
Amazon Quick and visit the agent library page. Admins can directly access this page by
clicking on the **Go to agent** link in admin console under
**Chat agent customization**. Once in Amazon Quick, follow these
steps to edit your system default chat agent's properties. You can preview and test how
your system agent works as you configure it.

###### To update system chat agent settings

1. Log in to the Amazon Quick console.
2. Select **Manage Quick** from the Amazon Quick
   admin console.
3. From the admin console left navigation menu, select
   **Customization**, and then select **Chat agent
   customization**.
4. In **Chat agent customization**, in **System chat
   agent**, select **Go to chat agent**.
5. In the **My Assistant** page, in **Configure chat
   agent**, customize the following sections:

   1. In **Chat agent persona**, configure your chat
      agent's personality, identity, tone, and response style. For detailed
      information about agent customization options, see [Working with chat agents](../../../quicksuite/latest/userguide/working-with-agents.md "../../../quicksuite/latest/userguide/working-with-agents.md") in the
      _Amazon Quick User Guide_.

   ###### Note

   This agent powers default chat interactions across all users of
   this account with chat feature access. Ensure that your instructions
   (e.g. identity and response style) work well for all users of this
   account. 2. In **Reference documents**, upload files that remain
   active in your chat agent's memory to guide all interactions. For
   detailed information about file upload options, see [Working with chat agents](../../../quicksuite/latest/userguide/working-with-agents.md "../../../quicksuite/latest/userguide/working-with-agents.md") in the
   _Amazon Quick User Guide_.

   ###### Note

   Since this agent is meant for broad use, this is a place to upload
   enterprise-level response templates and guides.

   The system default agent isn't linked to specific knowledge
   sources, actions, or spaces to ensure it works for all users
   regardless of their access permissions. This setting can't be
   changed.

6. In **Customization**, configure details to help recognize the
   chat agent. For detailed information about customization options, see [Working with chat agents](../../../quicksuite/latest/userguide/working-with-agents.md "../../../quicksuite/latest/userguide/working-with-agents.md") in the
   _Amazon Quick User Guide_.

## Configure clickable external links in chat responses

Admins can configure whether URLs in chat agent responses appear as clickable hyperlinks. The following procedure shows you how to enable clickable hyperlinks for all chat agents in your Amazon Quick instance.

###### To enable clickable external links

1. Log in to the Amazon Quick console.
2. Select **Manage Quick** from the Amazon Quick
   admin console.
3. From the admin console left navigation menu, select
   **Customization**, and then select **Chat agent
   customization**.
4. Under **Clickable external links**, turn the toggle on.
