

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html)

1. (Optional) Configure workload type concurrency.

   If you enabled workload type concurrency for a channel in the **Channel Settings** section, configure the individual workload type rows:

   1. Under the channel (for example, **TASK**), choose **Add workload type**.

   1. For each workload type row, configure the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html)

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html)

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
![Queue configuration showing two BasicQueue entries with different channel and priority settings.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-channels-and-concurrency-2.png)
+ When using workload type concurrency, cross-channel behavior is set per workload type, not per channel. A "Fraud Investigation" workload type might block all other channels, while a "Password Reset" on the same task channel might allow concurrent chats.
+ If a contact's workload type doesn't match any entry in the routing profile, the contact stays in queue. Audit your flows to ensure alignment between assigned workload types and routing profile entries.

## Example of how a contact is routed with cross-channel concurrency
<a name="example-routing-concurrency"></a>

For example, assume an agent is assigned to the routing profile that has the channel settings shown in the following image. They can be routed voice, chat, task, and email contacts. They can receive cross-channel contacts when on tasks. 

![The create routing profile page, channel settings section.](http://docs.aws.amazon.com/connect/latest/adminguide/images/routing-profile-cross-channel-concurrency.png)


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