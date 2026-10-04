

# Phone pools
<a name="nx-features-phone-pools"></a>

A phone pool, also referred to as just pool, is a collection of phone numbers or sender IDs that share the same settings that you can use to send messages. When you send messages through a phone pool, it chooses an appropriate origination identity to send the message as. If an origination identity in the phone pool fails, the phone pool will fail over to another origination identity if it is in the same phone pool. 

When you send messages through a pool that contains multiple origination identities, the service continuously monitors delivery receipts (DLRs) for each identity. If the service detects an increase in failed delivery receipts from one of your origination identities, it automatically deprioritizes the affected identity and routes your messages through the remaining healthy identities in the pool. When the affected identity recovers and delivery receipts return to normal, the service automatically resumes routing messages through it. This process does not require any configuration or manual intervention on your part.

To maximize delivery resilience, configure your pools with more than one origination identity. Pools that contain multiple number types — such as a short code and a toll-free number — provide the broadest failover coverage because each number type uses an independent delivery path.

**Note**  
Phone pools can be associated with Notify configurations to use your own dedicated phone numbers alongside AWS-managed identities for templated messaging.

When you create a pool, you can configure a specified origination identity. This identity includes keywords, message type, opt-out list, two-way configuration, and self-managed opt-out configuration. For example, by using pools, you can associate a list of opted-out destination phone numbers with your phone number for a particular country. By doing so, you can prevent messages from being sent to users who have already opted out of receiving messages from you.

**Important**  
When you update a phone number that is in a pool — for example, to add a keyword — make the change on the pool, not on the individual phone number.

The configuration of every phone number that you add to a pool has to match the configuration of the first phone number that you specified when you created the pool. For example, if you create a pool that contains a phone number that has two-way messaging enabled, the other numbers that you add to the pool must also have two-way messaging enabled.

You can also add an AWS RCS Agent as an origination identity in a pool alongside your phone numbers and sender IDs. When an AWS RCS Agent is in a pool, the pool enables automatic RCS-to-SMS fallback — if RCS delivery fails, the service automatically retries the message via SMS using another origination identity in the same pool.

You can manage keyword responses at the pool level so that the change applies to the origination identities in the pool. For more information, see [Keywords](nx-features-keywords.md). To control which destination phone numbers a pool can send to, you can associate the pool with an opt-out list. For more information, see [Opt-out lists](nx-features-opt-out-list.md).

**Topics**
+ [Create a phone pool](nx-features-phone-pools-create.md)
+ [Add a phone number, sender ID, or RCS agent](nx-features-phone-pools-add-number.md)
+ [View all phone pools](nx-features-phone-pools-list.md)
+ [Delete a phone pool](nx-features-phone-pools-delete.md)
+ [Using phone pool deletion protection](nx-features-phone-pools-deletion-protection.md)
+ [Update shared routes](nx-features-phone-pools-shared-routes.md)
+ [Manage tags for phone pools](nx-features-phone-pools-tags.md)
+ [List shared phone pools](nx-features-phone-pools-shared.md)