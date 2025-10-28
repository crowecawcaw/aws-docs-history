End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Messaging

The messaging API simplifies application to application communication within the
simulation. APIs to send and receive messages are part of the SimSpace Weaver app SDK. Messaging
currently uses a best effort approach to send and receive messages. SimSpace Weaver attempts
to send/receive messages on the next simulation tick, but there are no delivery, ordering,
or arrival time guarantees.

###### Topics

- [Use cases for messaging](#working-with_messaging_use-cases "#working-with_messaging_use-cases")
- [Using the messaging APIs](working-with_messaging_using.md "working-with_messaging_using.md")
- [When to use messaging](working-with_messaging_when-to-use.md "working-with_messaging_when-to-use.md")
- [Tips when working with messaging](working-with_messaging_tips.md "working-with_messaging_tips.md")
- [Messaging errors and
  troubleshooting](working-with_messaging_troubleshooting.md "working-with_messaging_troubleshooting.md")

## Use cases for messaging

###### Communicate between simulation applications

Use the messaging API to communicate between the applications in your simulation.
Use it to change the state of entities at a distance, change entity behavior, or
broadcast information to the entire simulation.

###### Acknowledge receipt of a message

Sent messages contain information about the sender in the message header. Use this
information to send back an acknowledgement reply on receipt of a message.

###### Forward data received by a custom app to other apps within the simulation

Messaging is not a replacement for how clients connect to custom apps running in
SimSpace Weaver. However, messaging does allow users a method of forwarding data from
custom apps receiving client data to other apps that do not have an external
connection. The message flow can also work in reverse, allowing apps with no
external connection to forward data to a custom app then to a client.
