

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
+ [How routing works](about-routing.md)
+ [Queues: standard and agent](concepts-queues-standard-and-agent.md)
+ [Queues: priority and delay examples](concepts-routing-profiles-priority.md)
+ [Queue-based routing](concepts-queue-based-routing.md)
+ [Channels and concurrency](channels-and-concurrency.md)
+ [Create a queue](create-queue.md)
+ [Disable a queue temporarily](disable-a-queue.md)
+ [Delete a queue](delete-queue.md)
+ [Set queue capacity](set-maximum-queue-limit.md)
+ [Route contacts based on queue capacity](route-based-on-queue-capacity.md)
+ [Set the hours of operation](set-hours-operation.md)
+ [Create a routing profile](routing-profiles.md)
+ [How Connect Customer uses routing profiles](concepts-routing.md)
+ [Delete a routing profile](delete-routing-profiles.md)
+ [Set up queue-based routing](set-up-queue-based-routing.md)
+ [Set up routing based on agent proficiencies](proficiency-routing.md)