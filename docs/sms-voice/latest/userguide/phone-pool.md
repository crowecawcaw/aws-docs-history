

# Phone pools in AWS End User Messaging SMS
<a name="phone-pool"></a>

A phone pool, also refereed to as just pool, is a collection of phone numbers or sender IDs that share the same settings that you can use to send messages. When you send messages through a phone pool, it chooses an appropriate origination identity to send the message as. If an origination identity in the phone pool fails, the phone pool will fail over to another origination identity if it is in the same phone pool. 

**Note**  
Phone pools can be associated with Notify configurations to use your own dedicated phone numbers alongside AWS-managed identities for templated messaging. For more information, see [Using dedicated numbers with Notify](notify-dedicated-numbers.md).

When you create a pool, you can configure a specified origination identity. This identity includes keywords, message type, opt-out list, two-way configuration, and self-managed opt-out configuration. For example, by using pools, you can associate a list of opted-out destination phone numbers with your phone number for a particular country. By doing so, you can prevent messages from being sent to users who have already opted out of receiving messages from you.

The configuration of every phone number that you add to a pool has to match the configuration of the first phone number that you specified when you created the pool. For example, if you create a pool that contains a phone number that has two-way messaging enabled, the other numbers that you add to the pool must also have two-way messaging enabled.

You can also add an AWS RCS Agent as an origination identity in a pool alongside your phone numbers and sender IDs. When an AWS RCS Agent is in a pool, the pool enables automatic RCS-to-SMS fallback — if RCS delivery fails, the service automatically retries the message via SMS using another origination identity in the same pool. For more information about configuring RCS fallback with pools, see [RCS to SMS fallback using phone pools](rcs-sms-fallback.md).

**Topics**
+ [Create a phone pool](phone-pool-create.md)
+ [Add a phone number or sender ID](phone-pool-add-number.md)
+ [View all phone pools](phone-pool-list.md)
+ [Delete a phone pool](phone-pool-delete.md)
+ [Change a pool''s opt-out list](phone-pool-manage-opt-out-list.md)
+ [Update shared routes](phone-pool-shared-routes.md)
+ [Using phone pool deletion protection](phone-pool-deletion-protection.md)
+ [Manage tags for phone pools](phone-pool-tags.md)
+ [List shared phone pools](phone-pool-shared.md)
+ [Managing AWS RCS Agents in pools](phone-pool-rcs-agents.md)