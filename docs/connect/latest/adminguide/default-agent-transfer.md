# Default agent transfer flow in Amazon Connect:

"Transferring now"

This default transfer flow is what the "from" agent experiences when they transfer a
contact to another agent by using [Create quick connects in Amazon Connect](quick-connects.md "quick-connects.md"). The "from" agent hears a **Play
prompt** play the message "Transferring now." Then the **Transfer
to agent** block is used to transfer the contact to the agent.

When the contact is transferred, the "to" agent hears the [Default agent whisper](default-agent-whisper.md "default-agent-whisper.md").

###### Tip

The **Transfer to Agent** block is a beta feature and only works
for voice interactions. To transfer a chat contact to another agent, follow these
instructions: [Use contact attributes to route contacts
to a specific agent](transfer-to-agent.md#use-attribs-agent-queue "transfer-to-agent.md#use-attribs-agent-queue").

For instructions about how to override and change a default flow, see [Change a default flow in your Amazon Connect
contact center](change-default-contact-flow.md "change-default-contact-flow.md").

###### Tip

Wondering if a default flow has been changed? Use [flow version control](flow-version-control.md "flow-version-control.md") to view the original
version of the flow.
