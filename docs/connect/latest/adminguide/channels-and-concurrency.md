# Channels and concurrency for routing contacts

in Amazon Connect

Agents can handle voice, chat, tasks and email in Amazon Connect. When you set up a routing
profile to handle multiple channels, you have two options:

- Option 1: Set up agents so they can handle contacts while already on another
  channel. This is called _cross-channel concurrency_.
- Option 2: Set up agents so they can be offered voice, chat, tasks, or email if
  they are fully idle, depending on what is in queue. When you choose this option,
  after the agent starts work on contacts from one channel they will no longer be
  offered contacts from any other channels.
  When using cross-channel concurrency, Amazon Connect checks which contact to offer the agent as
  follows:

1. It checks what contacts/channels the agent is currently handling.
2. Based on what channels they are currently handling, and the cross-channel
   configuration in the agent's routing profile, it determines whether the agent
   can be routed the next contact.
3. Amazon Connect prioritizes the longest waiting contact if Priority and Delay are equal.
   Even though it's evaluating multiple channels at the same time, First-In
   First-Out is still respected.
   For a detailed example of how Amazon Connect routes contacts when cross-channel concurrency is
   set up, see [Example of how a contact is routed
   with cross-channel concurrency](routing-profiles.md#example-routing-concurrency "routing-profiles.md#example-routing-concurrency").

To learn more about what the agent experiences in the Contact Control Panel when
handling multiple chats, see [Use the Contact Control Panel (CCP) in
Amazon Connect to chat with contacts](chat-with-connect-contacts.md "chat-with-connect-contacts.md").
