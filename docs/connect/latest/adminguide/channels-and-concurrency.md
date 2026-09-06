

# Channels and concurrency for routing contacts in Connect Customer
<a name="channels-and-concurrency"></a>

Agents can handle voice, chat, tasks and email in Connect Customer. When you set up a routing profile to handle multiple channels, you have two options: 
+ Option 1: Set up agents so they can handle contacts while already on another channel. This is called *cross-channel concurrency*. 
+ Option 2: Set up agents so they can be offered voice, chat, tasks, or email if they are fully idle, depending on what is in queue. When you choose this option, after the agent starts work on contacts from one channel they will no longer be offered contacts from any other channels.

When using cross-channel concurrency, Connect Customer checks which contact to offer the agent as follows: 

1. It checks what contacts/channels the agent is currently handling.

1. Based on what channels they are currently handling, and the cross-channel configuration in the agent's routing profile, it determines whether the agent can be routed the next contact.

1. Connect Customer prioritizes the longest waiting contact if Priority and Delay are equal. Even though it's evaluating multiple channels at the same time, First-In First-Out is still respected.

For a detailed example of how Connect Customer routes contacts when cross-channel concurrency is set up, see [Example of how a contact is routed with cross-channel concurrency](routing-profiles.md#example-routing-concurrency). 

To learn more about what the agent experiences in the Contact Control Panel when handling multiple chats, see [Use the Contact Control Panel (CCP) in Connect Customer to chat with contacts](chat-with-connect-contacts.md).

## Workload-type concurrency
<a name="workload-type-concurrency"></a>

A workload type is a user-defined classification that differentiates contacts within the same channel. It is defined as a custom value of the system predefined attribute `connect:WorkloadType` (for example, "Tax Filing", "Document Review", or "VIP Callback"). You can use workload types to distinguish contacts by any dimension that is meaningful to their operation and that warrants different agent capacity treatment. You define workload type values in the admin console (see [Create predefined attributes for routing contacts to agents](predefined-attributes.md)) and assign them to contacts using the **Set contact attributes** flow block or the `UpdateContact` API. If no workload type is explicitly set, the contact defaults to its subtype.

For Task and Email channels, you can configure concurrency at the workload type level instead of the channel level. When enabled on a routing profile, each workload type gets its own concurrency limit (1–10) and cross-channel behavior setting. For example, an agent might handle 3 "Document Review" tasks but only 1 "Tax Filing" task. The cross-channel behavior options are: **No other channels or workload types**, **Only allow other workload types of the same channel**, and **Allow other channels concurrently**.

A routing profile cannot mix channel-level and workload-type concurrency on the same channel. Enabling one disables the other.

The following limits apply to workload-type concurrency:
+ Maximum of 5 workload types per channel per routing profile.
+ Sum of concurrency values per channel must not exceed 10 for Tasks and Emails.

**Important**  
If a contact's workload type has no matching entry in the agent's routing profile, the contact remains queued indefinitely. Ensure that every workload type used in flows or APIs has a corresponding routing profile entry.

When you switch a routing profile between concurrency models, existing contacts drain under the previous rules while new contacts follow the updated configuration. Expect a brief coexistence period.