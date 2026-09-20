

# Set up routing in Connect Customer
<a name="connect-queues"></a>

In Connect Customer, routing consists of three parts: queues, routing profiles, and flows. This topic discusses queues and routing profiles. For information about flows, see [Flows in Connect Customer](connect-contact-flows.md).

A queue holds contacts waiting to be answered by agents. You can use a single queue to handle all incoming contacts, or you can set up multiple queues.

Queues are linked to agents through a routing profile. When you create a routing profile, you specify: 
+ Which queues will be in it.
+ Whether one queue should be prioritized over another.
+ What channels agents will handle in the Contact Control Panel (CCP).
+ How many contacts agents can handle simultaneously for each channel.
+ Whether individual queues are for all channels or specific ones.
+ What channel and queue combinations will an agent be able to manually prioritize work from.

Each agent is assigned to one routing profile.

**Topics**
+ [How routing works in Connect Customer](about-routing.md)
+ [Standard queues and agent queues in your Connect Customer contact center](concepts-queues-standard-and-agent.md)
+ [Queue priority and delay examples to help you load balance Connect Customer contacts](concepts-routing-profiles-priority.md)
+ [Queue-based routing to route customers to a specific contact center agent](concepts-queue-based-routing.md)
+ [Channels and concurrency for routing contacts in Connect Customer](channels-and-concurrency.md)
+ [Create a queue using the Connect Customer admin website](create-queue.md)
+ [Disable a queue temporarily using Connect Customer](disable-a-queue.md)
+ [Delete a queue from your Connect Customer instance](delete-queue.md)
+ [Set the limit of maximum contacts in a queue using Connect Customer](set-maximum-queue-limit.md)
+ [Route contacts based on queue capacity using Connect Customer](route-based-on-queue-capacity.md)
+ [Set the hours of operation and time zone for a queue using Connect Customer](set-hours-operation.md)
+ [Create a routing profile in Connect Customer to link queues to agents](routing-profiles.md)
+ [How Connect Customer uses routing profiles](concepts-routing.md)
+ [Delete a routing profile from a Connect Customer instance](delete-routing-profiles.md)
+ [Set up queue-based, or skills-based, routing in Connect Customer](set-up-queue-based-routing.md)
+ [Set up routing in Connect Customer based on agent proficiencies](proficiency-routing.md)