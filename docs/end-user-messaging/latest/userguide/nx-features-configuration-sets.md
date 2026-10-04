

# Configuration sets
<a name="nx-features-configuration-sets"></a>

You can use the configurations in AWS End User Messaging to provision phone numbers or sender IDs to send SMS messages, MMS messages, or voice messages to your customers' mobile devices. AWS End User Messaging can send messages to recipients in over 200 countries and regions. In some countries and regions, you can also receive messages from your customers by using the two-way SMS feature. When you create a new AWS End User Messaging account, your account is placed in an SMS sandbox. This initially limits your monthly spending and who you can send messages to. For more information, see AWS End User Messaging sandbox. 

To receive text messages using AWS End User Messaging, you should first obtain a dedicated number, you can then enable two-way SMS for it. Finally, you can specify the messages that AWS End User Messaging sends to customers when it receives incoming messages. 

**Note**  
When you configure SMS channel settings in AWS End User Messaging, your changes apply to other AWS services that send SMS messages, such as Amazon SNS.

A *configuration set* is a set of rules that are applied when you send a message. For example, a configuration set can specify a destination for events related to a message. When SMS events occur (such as delivery or failure events), they are routed to the destination associated with the configuration set that you specified when you sent the message. You're not required to use configuration sets when you send messages, but we recommend that you do. If you don't specify a configuration set with an event destination, the API doesn't emit event records. These event records are a useful way to determine how many messages you sent, how much you paid for each one, and whether or not the message was received by the recipient.

Once you have created a configuration set you should add an [Event destinations in AWS End User Messaging](nx-features-configuration-sets-event-destinations.md) to help monitor your message send and receive events and a protect configuration to create allow rules to only send messages to the destinations you do business in. 

**Topics**
+ [Create a configuration set](nx-features-configuration-sets-create.md)
+ [Edit a configuration set](nx-features-configuration-sets-edit.md)
+ [Delete a configuration set](nx-features-configuration-sets-delete.md)
+ [View all configuration sets](nx-features-configuration-sets-list.md)
+ [Manage tags for a configuration set](nx-features-configuration-sets-tags.md)
+ [Edit a configuration set protect configuration](nx-features-configuration-sets-edit-protect.md)
+ [Event destinations](nx-features-configuration-sets-event-destinations.md)