

# Create a routing profile in Connect Customer to link queues to agents
<a name="routing-profiles"></a>

This topic is for administrators and contact center managers. It explains how to create routing profiles using the Connect Customer admin website. For the APIs used to create and manage routing profiles programmatically, see [APIs to create and manage routing profiles](#apis-routing-profiles). 

While queues are a 'waiting area' for contacts, a routing profile links queues to agents. When you create a routing profile, you specify: 
+ Channels: Which channels—voice, chat, task, and email—are routed to this group of agents; whether to allow channels concurrently.
+ Queues: Which queues are in the routing profile; whether one queue should be prioritized over another.

Each agent is assigned to one routing profile. For more information about routing profiles and queues, see [How Connect Customer uses routing profiles](concepts-routing.md).

**How many routing profiles can I create?** To view your quota of **Routing profiles per instance**, open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

**To create a routing profile**

1. On the navigation menu, choose **Users**, **Routing profiles**, **Add routing profile**.

1. In the **Routing Profile Details** section, in the **Name** box, enter a searchable display name. In the **Description** box, enter what the profile is used for. 

1. In the **Channel Settings** section, enter or choose the following information:


<table>
<thead>
  <tr><th>Item</th><th>Description</th><th></th></tr>
</thead>
<tbody>
  <tr><td><b>Channel availability</b></td><td>Choose which types of contacts will be routed to agents who are assigned to this routing profile.</td><td></td></tr>
  <tr><td><b>Maximum contacts per agent</b></td><td>For chat, task, and email channels, specify how many contacts that an agent can handle simultaneously, up to 10.<br />For emails, this field defines how many emails agents can receive, and double that number is how many outbound emails agents can initiate. For example, if you set <b>Maximum contacts per agent</b> to 5, agents can receive up to 5 emails and create up to 10 agent-initiated outbound emails.</td><td></td></tr>
  <tr><td><b>Cross-channel concurrency</b></td><td>Choose one of the following options:<ul><li> <b>No other channels while agent is on {{channel}}</b>. For example, while an agent is on a chat, they will not receive a voice contact, email, or a task.  </li><li> <b>Allow other channel concurrently</b>. For example, while an agent is on a voice contact, they can be offered contacts from any other channels enabled in the routing profile, such as chats, emails, and tasks. </li></ul><br />See <a href="#example-routing-concurrency">Example of how a contact is routed with cross-channel concurrency</a>. </td><td></td></tr>
  <tr><td><b>Workload type concurrency</b></td><td>(Task and Email channels only) Toggle this on to configure agent capacity per workload type instead of a single channel-level number. When enabled, the <b>Maximum contacts per agent</b> field is disabled for that channel, and you configure capacity through individual workload type rows instead. For more information, see <a href="channels-and-concurrency.md">Channels and concurrency for routing contacts in Connect Customer</a>.</td><td></td></tr>
</tbody>
</table>


1. (Optional) Configure workload type concurrency.

   If you enabled workload type concurrency for a channel in the **Channel Settings** section, configure the individual workload type rows:

   1. Under the channel (for example, **TASK**), choose **Add workload type**.

   1. For each workload type row, configure the following:


<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Workload Type</b></td><td>Select a workload type value from the dropdown. These values come from the system predefined attribute <code>connect:WorkloadType</code>. You must create workload type values before they appear here. For more information, see <a href="predefined-attributes.md">Create predefined attributes for routing contacts to agents</a>.</td></tr>
  <tr><td><b>Concurrency</b></td><td>Enter the number of contacts of this workload type the agent can handle simultaneously (1–10).</td></tr>
  <tr><td><b>Cross-channel behavior</b></td><td>Choose how this workload type interacts with other channels: <b>No other channels or workload types</b>, <b>Only allow other workload types of the same channel</b>, or <b>Allow other channels concurrently</b>.</td></tr>
</tbody>
</table>


   1. Repeat for each workload type the agent should handle on this channel.

   1. Choose **Save**.

   Rules and validations:
   + You can add up to 5 workload types per channel in a single routing profile.
   + The sum of concurrency values across all workload types for a channel cannot exceed the channel's maximum concurrency limit (10).
   + You cannot have both channel-level concurrency and workload-type concurrency active for the same channel. Enabling one disables the other.
   + Every workload type assigned to contacts (through flows or APIs) that route to this profile must have a corresponding row here. Missing entries cause contacts to queue indefinitely.
**Important**  
When you enable workload type concurrency for a channel, the channel-level **Maximum contacts per agent** and **Cross-channel concurrency** fields for that channel become inactive. All capacity and cross-channel settings are managed per workload type.

1. In the **Queues** section, enter the following information:


<table>
<thead>
  <tr><th>Item</th><th>Description</th><th></th></tr>
</thead>
<tbody>
  <tr><td><b>Name</b></td><td>Use the dropdown menu or text field to choose a queue that you've already set up. You can add multiple queues to a routing profile.</td><td></td></tr>
  <tr><td><b>Channels</b></td><td>Choose whether the queue is for chat, voice, email, task, or all of them. The channel that you specify here must also be specified in the <b>Channel Settings</b> section. If it isn't, contacts from that channel won't be routed to agents. </td><td></td></tr>
  <tr><td><b>Priority</b></td><td>Specify the order in which contacts are to be handled for that queue. For example, a contact in a queue with a priority of 2 would be a lower priority than a contact in a queue with a priority of 1.</td><td></td></tr>
  <tr><td><b>Delay (in seconds)</b></td><td>Enter the minimum amount of time a contact should be in the queue before they are routed to an available agent.<br />To learn more about how Priority and Delay work together, see <a href="concepts-routing-profiles-priority.md">Queue priority and delay examples to help you load balance Connect Customer contacts</a>.</td><td></td></tr>
  <tr><td><b>Default outbound queue</b></td><td>Choose a queue to be associated with outbound calls or emails initiated by the agents. Outbound contacts respect the settings from the default outbound queue, such as caller ID and "From" email address. For more information, see <a href="create-queue.md">Create a queue using the Connect Customer admin website</a>.</td><td></td></tr>
  <tr><td><b>Set routing order</b></td><td>By default Connect Customer routes new contacts to agents that have been in <b>Available</b> status the longest. You can customize this behavior, for example, to change the impact that outbound contacts have on the assignment of new inbound contacts.</td><td></td></tr>
  <tr><td><b>Outbound calls should not impact routing order</b></td><td>Use this setting if you don't want agents who make outbound contacts to move to the bottom of the list for receiving inbound contacts.<br />By default new contacts are routed to the agent who has been in <b>Available</b> status longest. By making an outbound contact, the agent drops to the bottom of the list waiting for inbound contacts. You can use this setting to override that default logic and make sure that agents making outbound contacts still get their fair share of inbound contacts. </td><td></td></tr>
</tbody>
</table>


1. Add queue and channel combinations in the **Manual Assignment** section. Manual assignment supports tasks, emails, and chats.

   For more information about routing with manual assignment, see [How routing works with manual assignment](about-routing.md#routing-profile-manual-assignment-works).

1. Optionally, add tags to identify, organize, search for, filter, and control who can access this routing profile. For more information, see [Add tags to resources in Connect Customer](tagging.md).

1. Choose **Save**.

## Tips for setting up channels and concurrency
<a name="routing-profile-concurrency"></a>
+ Use **Channel availability** to toggle on and off whether agents assigned to a profile get voice, chat, task, and email contacts.

  For example, there are 20 queues assigned to a profile. All of the queues are enabled for voice, chat, task, and email. By removing the **Voice** option at the routing profile level, you can stop all voice calls to these agents, across all queues in the profile. When you want to restart voice contacts for these agents again, select **Voice**. 
+ When using **Cross-channel concurrency**, Connect Customer checks which contact to offer the agent as follows: 

  1. It checks what contacts/channels the agent is currently handling.

  1. Based on what channels they are currently handling, and the cross-channel configuration in the agent's routing profile, it determines whether the agent can be routed the next contact.

  1. Connect Customer prioritizes the longest waiting contact if Priority and Delay are equal. Even though it's evaluating multiple channels at the same time, First-In First-Out is still respected.

  See [Example of how a contact is routed with cross-channel concurrency](#example-routing-concurrency).
+ For each queue in the profile, choose whether it's for voice, chat, task, email, or all channels. 
+ If you want a queue to handle voice, chat, task, and email but want to assign a different priority to each channel, add the queue twice. For example, in the following image, voice is priority 1 but chat, task, and email are priority 2.   
![Queue configuration showing two BasicQueue entries with different channel and priority settings.](https://docs.aws.amazon.com/connect/latest/adminguide/images/set-channels-and-concurrency-2.png)
+ When using workload type concurrency, cross-channel behavior is set per workload type, not per channel. A "Fraud Investigation" workload type might block all other channels, while a "Password Reset" on the same task channel might allow concurrent chats.
+ If a contact's workload type doesn't match any entry in the routing profile, the contact stays in queue. Audit your flows to ensure alignment between assigned workload types and routing profile entries.

## Example of how a contact is routed with cross-channel concurrency
<a name="example-routing-concurrency"></a>

For example, assume an agent is assigned to the routing profile that has the channel settings shown in the following image. They can be routed voice, chat, task, and email contacts. They can receive cross-channel contacts when on tasks. 

![The create routing profile page, channel settings section.](https://docs.aws.amazon.com/connect/latest/adminguide/images/routing-profile-cross-channel-concurrency.png)


The agent will experience the following routing behavior:

1. Assume the agent is fully idle. Next, the agent accepts a chat and begins working on it. Meanwhile, a task comes into queue.
   + Chat is set to **No other channels allowed**. 
   + So even though there is a task in queue, it will not be offered to this agent.

1. Next, there is a chat in queue.
   + The agent's maximum chat concurrency is 2, so they are routed another chat for total of 2 chats. The agent continues working on both of the chats.

1. There are no other chats in queue. The agent finishes both chats (closes ACW). 
   + There is still a task waiting in queue.
   + At this point, the task is offered to the agent because they are fully idle again. The agent begins working the task.

1. Another chat comes into queue.
   + Tasks is set to **Allow other channels concurrently**. So, even though the agent is already working on a task, they can still be offered the chat. 
   + The chat gets routed to the agent, who now works on both the 1 chat and 1 task concurrently.

1. Now there is a Voice call in queue.
   + The agent is still working on 1 chat and 1 task. 
   + Even though **Task** is set to **Allow other channels concurrently**, the agent is still working on 1 chat, and **Chat** is set to **No other channels while agent is on a Chat contact**. So, the voice call is not routed to the agent. The agent continues working on both the chat and the task.

1. The agent completes the chat, but still works on the task.
   + Now, because the only contact still assigned to the agent is a task, and **Tasks** are set to **Allow other channels concurrently**, this means that the agent can be offered the voice call. 
   + The agent picks up the voice call and is now working concurrently on both the voice call and the task. 

1. Now there is another task in queue.
   + The agent is currently working on a voice call AND a task. Once again, Connect Customer checks the cross channel settings and Voice is set to **No other channels while agent is on a Voice contact**. 
   + Because the agent is working on a voice call, they cannot be offered any tasks until they are done with the voice call. 
   + Also, because **Task** is set to **Maximum contacts per agent** is 1, even after the agent handles the voice call, they still won't be offered the task until they finish their current task. 

## APIs to create and manage routing profiles
<a name="apis-routing-profiles"></a>

Use the following APIs to create and manage routing profiles programmatically:
+ [CreateRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateRoutingProfile.html)
+ [DescribeRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html)
+ [UpdateRoutingProfileConcurrency](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateRoutingProfileConcurrency.html)
+ [UpdateRoutingProfileQueues](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateRoutingProfileQueues.html)
+ [UpdateRoutingProfileDefaultOutboundQueue](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateRoutingProfileDefaultOutboundQueue.html)