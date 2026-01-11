# Custom metric primitives

Metric primitives are used for creating custom metrics, which are personalized
measurements that offer more flexibility than the standard out-of-the-box metrics. Metric
primitives utilize metric-level filters to make them more customizable and adaptable to
business needs. These metrics can be used with different statistics (such as SUM, AVG, MIN,
MAX) and can be combined using arithmetic operations to devise more comprehensive
measurements. The metric primitives are broadly categorized into two categories :

- **Contact**: Helps gain insights into customer
  interactions and tasks
- **Agent**: Helps gain insights into agent performance

## After contact work time

The total time that an agent spent doing After Contact Work (ACW) for a contact. In
some businesses, this is also known as Call Wrap Up time.

You specify the amount of time an agent has to do ACW in their [agent’s configuration settings](configure-agents.md "configure-agents.md"). When a conversation with a contact ends,
the agent is automatically allocated to do ACW for the contact. ACW ends for a contact
when the agent changes to an alternate state such as available or the configured timeout
is reached.

**Metric Primitive Name:**
`After contact work time`

**Metric Primitive Category**: Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Agent Active Time

This metric provides the time an agent spends on a customer interaction, including
Agent interaction time, Customer hold time, and After Contact Work (ACW) time. Active
Time includes time spent handling contacts while in a custom status.

Custom status = the agent's CCP status other than **Available** or **Offline**. For example,
Training would be a custom status.

**Metric Primitive Name:**
`Agent active time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Agent Interaction Time

The time that agents spent interacting with a customer during a contact. This does not
include After Contact Work Time, Customer Hold Time, Custom status time, or agent pause
duration (which applies only to tasks).

**Metric Primitive Name:**
`Agent interaction time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Contact Hold Time

This metric measures the total time that customers spent on hold after being connected
to an agent. This includes time spent on a hold when being transferred, but does not
include time spent in a queue.

**Metric Primitive Name:**
`Contact hold time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Agent Pause Time

This metric measures the total time an agent kept a task in a paused state after the
task was connected to them. It applies only to `TASK` channel contacts,
including both inbound and outbound tasks.

**Metric Primitive Name:**
`Agent pause time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Contact Duration

This metric measures the time a contact spends from the contact initiation timestamp
to disconnect timestamp.

**Metric Primitive Name:**
`Contact duration`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Contact Queue Time

The total time that a contact waited in a queue before being answered by an agent.
Also known as queue wait time.

**Metric Primitive Name:**
`Contact queue time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Contacts Abandoned

This metric counts the number of contacts that were disconnected by the customer while
waiting in the queue. Inbound contacts which disconnect because they requested a
callback are not counted as abandoned.

**Metric Primitive Name:**
`Contacts abandoned`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM

## Contacts Created

The number of contacts created during the specified time range. This includes all
inbound and outbound contacts regardless of how they were initiated.

**Metric Primitive Name:**
`Contacts created`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM

## Contacts Handled

This metric counts the contacts that were connected to an agent during a given time
period. It doesn't matter how the contact got to the agent.

**Metric Primitive Name:**
`Contacts handled`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM

## Contacts Hold Abandons

This metric counts the contacts that disconnected while the customer was on hold. This
includes both contacts disconnected by the agent and contacts disconnected by the
customer.

**Metric Primitive Name:**
`Contacts hold disconnect`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM

## Contacts Put On Hold

The number of contacts put on hold by an agent at least once. If a contact is put on
hold multiple times, it is counted only once.

**Metric Primitive Name:**
`Contacts put on hold`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM

## Contacts Queued

The number of contacts added to a queue during the specified time range. This includes
contacts whether they were handled, abandoned, or are still in the queue.

**Metric Primitive Name:**
`Contacts queued`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM

## Contacts Transferred Out

The number of contacts transferred out from queue to queue, and transferred out by an
agent using the CCP.

**Metric Primitive Name:**
`Contacts transferred out`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM

## Contact Handle Time

This metric measures the total time, from start to finish, that a contact is connected with an agent (handle time). It includes talk time, customerHoldDuration, after contact work (ACW) time, and agent pause duration (which applies only to tasks). It applies to both inbound and outbound contacts.

**Metric Primitive Name:**
`Contact handle time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM

## Contact Holds

The number of times voice contacts were put on hold while interacting with an agent.
Provides insights into how often agents need to put customers on hold during
interactions.

**Metric Primitive Name:**
`Contact holds`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Contact Resolution Time

The total time from when a contact enters the system until it is resolved. This
includes queue time, interaction time, hold time, and after contact work time.

**Metric Primitive Name:**
`Contact resolution time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Contact Flow Duration

This metric measures the total time a contact spent in a flow. It's the IVR time, the time from the start until contact is queued, transferred, or disconnected—whichever occurred first.
Outbound contacts don't start in a flow, so outbound contacts aren't included.

**Metric Primitive Name:**
`Contact flow duration`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Agent Greeting Time

The first response time of agents on chat, indicating how quickly they engage with
customers after joining the chat.

###### Note

This metric is available only for contacts analyzed by Contact Lens conversational
analytics, please refer to the following metric for more clarity: [Average agent greeting time](contact-lens-metrics.md#average-greeting-time-agent-hmetric "contact-lens-metrics.md#average-greeting-time-agent-hmetric")

**Metric Primitive Name:**
`Agent greeting time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Agent Interruption Time

The total agent interruption time while talking to a contact.

###### Note

This metric is available only for contacts analyzed by Contact Lens conversational
analytics, please refer to the following metric for more clarity: [Average agent interruptions time](contact-lens-metrics.md#average-interruption-time-agent-hmetric "contact-lens-metrics.md#average-interruption-time-agent-hmetric")

**Metric Primitive Name:**
`Agent interruption time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and
MAX

## Agent Interruptions

Quantifies the frequency of agent interruptions during customer interactions.

###### Note

This metric is available only for contacts analyzed by Contact Lens conversational
analytics, please refer to the following metric for more clarity: [Average agent interruptions](contact-lens-metrics.md#average-interruptions-agent-hmetric "contact-lens-metrics.md#average-interruptions-agent-hmetric")

**Metric Primitive Name:**
`Agent interruptions`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and
MAX

## Talk Time Agent

The time that was spent talking in a conversation by an agent.

###### Note

This metric is available only for contacts analyzed by Contact Lens conversational
analytics, please refer to the following metric for more clarity: [Average agent talk time](contact-lens-metrics.md#average-talk-time-agent-hmetric "contact-lens-metrics.md#average-talk-time-agent-hmetric")

**Metric Primitive Name:**
`Agent talk time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Talk Time Customer

The time that was spent talking in a conversation by a customer.

###### Note

This metric is available only for contacts analyzed by Contact Lens
conversational analytics, please refer to the following metric for more
clarity: [Average customer talk time](contact-lens-metrics.md#average-talk-time-customer-hmetric "contact-lens-metrics.md#average-talk-time-customer-hmetric")

Note:

**Metric Primitive Name:**
`Customer talk time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and
MAX

## Non-Talk Time

This metric provides the total non-talk time in a voice conversation. Non-talk time
refers to the combined duration of hold time and periods of silence exceeding 3 seconds,
during which neither the agent nor the customer is engaged in conversation.

###### Note

This metric is available only for contacts analyzed by Contact Lens conversational
analytics, please refer to the following metric for more clarity: [Average non-talk time](contact-lens-metrics.md#average-non-talk-time-hmetric "contact-lens-metrics.md#average-non-talk-time-hmetric")

**Metric Primitive Name:**
`Non-talk time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and
MAX

## Talk Time

The time that was spent talking during a voice contact across either the
customer or the agent.

###### Note

This metric is available only for contacts analyzed by Contact Lens
conversational analytics, please refer to the following metric for more
clarity: [Average talk time](contact-lens-metrics.md#average-talk-time-hmetric "contact-lens-metrics.md#average-talk-time-hmetric")

**Metric Primitive Name:**
`Talk time`

**Metric Primitive Category:** Contact

**Supported Statistics:** SUM, AVG, MIN, and
MAX

## Conversation Duration

The conversation duration of voice contacts with agents. Calculated by the total time
from the start of the conversation until the last word spoken by either the agent or the
customer.

###### Note

This metric is available only for contacts analyzed by Contact Lens
conversational analytics, please refer to the following metric for more clarity: [Average conversation duration](contact-lens-metric..md#average-conversation-duration-hmetric "contact-lens-metric..md#average-conversation-duration-hmetric")

**Metric Primitive Name:**
`Conversation duration`

**Metric Primitive Category:**Contact

**Supported Statistics:** SUM, AVG, MIN, and MAX

## Contacts Routed

This metric counts the number of contacts routed to an agent.

**Metric Primitive Name:**
`Contacts routed`

**Metric Primitive Category:** Agent

**Supported Statistics:** SUM

## Agent Contacts Missed

This metric counts the contacts routed to an agent but not answered by that agent,
including contacts abandoned by the customer.

If a contact is not answered by a given agent, Amazon Connect attempts to route it
to another agent to handle; the contact is not dropped. Because a single contact can
be missed multiple times (including by the same agent), it can be counted multiple
times: once for each time it is routed to an agent but not answered.

**Metric Primitive Name:**
`Agent contacts missed`

**Metric Primitive Category:** Agent

**Supported Statistics:** SUM

## Agent Idle Time

This metric measures the amount of time agent wasn’t handling contacts + any time
their contacts were in an Error state, after the agent sets their status in the CCP
to Available.

Agent idle time includes the amount of time from when Amazon Connect starts
routing the contact to the agent to when the agent picks up or declines the contact.
After an agent accepts the contact, the agent is no longer considered idle. This
metric can't be grouped or filtered by queue, phone number, or channels.

**Metric Primitive Name:**
`Agent idle time`

**Metric Primitive Category:** Agent

**Supported Statistics:** SUM

## Agent Contact Time

This is a measure of the total time that an agent spent on a contact, including
Customer Hold Time and After Contact Work Time. This does not include time spent on
a contact while in a custom status or Offline status. (Custom status = the agent's
CCP status is other than Available or Offline. For example, Training would be a
custom status.)

This metric can't be grouped or filtered by queue, phone number, or
channels.

**Metric Primitive Name:**
`Agent on contact time`

**Metric Primitive Category:** Agent

**Supported Statistics:** SUM

## Agent Online Time

This is a measures the total time that an agent spent with their CCP set to a
status other than **Offline**. This includes any time
spent in a custom status. This metric can't be grouped or filtered by queue, phone
number, or channels.

**Metric Primitive Name:**
`Agent online time`

**Metric Primitive Category:** Agent

**Supported Statistics:** SUM

## Agent Error Status Time

This is the measure of the total time contacts were in an error status. This
metric can't be grouped or filtered by queue, phone number, or channels.

**Metric Primitive Name:**
`Agent error status time`

**Metric Primitive Category:** Agent

**Supported Statistics:** SUM

## Agent Non-Productive Time

This measures the total time that agents spent in a custom status. That is, their
CCP status is other than **Available** or **Offline**. This metric doesn't mean that the agent was
spending their time unproductively. This metric can't be grouped or filtered by
queue, phone number, or channels.

**Metric Primitive Name:**
`Agent online time - non-productive`

**Metric Primitive Category:** Agent

**Supported Statistics:** SUM

## Current Contacts In Queue

This metric counts the contacts currently in the queue. This metric helps organizations
monitor queue load and make staffing decisions.

**Metric Primitive Name:**
`Contacts in queue`

**Metric Primitive Category:** Current Contact

**Supported Statistics:** SUM

## Current Contact Queue Time

The metric helps measures the length of time in the queue for the contact that has been in the queue the longest.

**Metric Primitive Name:**
`Contact queue time`

**Metric Primitive Category:** Current Contact

**Supported Statistics:** MAX

## Current Contacts Scheduled

This metric counts the number of scheduled callbacks, which will enter a queue in a future time.
For more information please refer to the:

- [Set up queued callback by creating flows, queues, and routing profiles](setup-queued-cb.md "setup-queued-cb.md") in Amazon Connect Administrator Guide
- [How Initial delay affects Scheduled and In queue metrics](scheduled-vs-inqueue.md "scheduled-vs-inqueue.md") in Amazon Connect Administrator Guide

**Metric Primitive Name:**
`Contacts Scheduled`

**Metric Primitive Category:** Current Contact

**Supported Statistics:** SUM

## Metric level filters supported per metric

primitive category

| Metric Category                                                                          | Metric Level Filter Key                                                                                                                                                                                                                                                             | Metric Level Filter Key Description                                                                                                                                                                                                                                                                            | Metric Level Filter Values                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Contact                                                                                  | Initiation method                                                                                                                                                                                                                                                                   | Indicates how the contact was initiated.                                                                                                                                                                                                                                                                       | Example: INBOUND, OUTBOUND, TRANSFER, QUEUE_TRANSFER, CALLBACK, API, etc.<br>Please refer to the InitiationMethod section of ContactTraceRecord in the Amazon Connect Administrator Guide for more filter values. |
| Disconnect reason                                                                        | Indicates how the contact was terminated.                                                                                                                                                                                                                                           | A few examples of filter values are AGENT_DISCONNECT, CUSTOMER_DISCONNECT, TRANSFER, THIRD_PARTY_DISCONNECT, BARGED, CONTACT_FLOW_DISCONNECT, etc.<br>Please refer to ContactTraceRecord in the Amazon Connect Administrator Guide for more filter values.                                                     |
| Channel                                                                                  | How the contact reached your contact center.                                                                                                                                                                                                                                        | Valid values: Voice, Chat, Task                                                                                                                                                                                                                                                                                |
| Feature                                                                                  | Identifies if Contact Lens conversational analytics is enabled on the flow.                                                                                                                                                                                                         | Contacts analyzed by conversational analytics                                                                                                                                                                                                                                                                  |
| Is abandoned                                                                             | This is true when the contact was abandoned by customer while waiting in queue, false otherwise.<br>Please note if a contact was scheduled for a callback it would not be considered as abandoned.                                                                                  | True or False                                                                                                                                                                                                                                                                                                  |
| Is resulted in callback                                                                  | This is true when the contact was scheduled for a callback, false otherwise.                                                                                                                                                                                                        |
| Is handled                                                                               | This is true when a contact is connected to an agent, false otherwise.                                                                                                                                                                                                              |
| Is put on hold                                                                           | This is true when a contact is put on hold by an agent, false otherwise.                                                                                                                                                                                                            |
| Is queued                                                                                | This is true when a contact gets queued, false otherwise.                                                                                                                                                                                                                           |
| Is transferred out                                                                       | This is true when the contact is transferred out from a queue to another queue, or transferred out by an agent, false otherwise.                                                                                                                                                    |
| After contact work time (ms)                                                             | Measures the total time that an agent spent doing ACW for a contact.                                                                                                                                                                                                                | Numeric input denoting time in milliseconds                                                                                                                                                                                                                                                                    |
| Agent active time (ms)                                                                   | Measures the time an agent spends on a customer interaction, including Agent interaction time, Customer hold time, and After contact work (ACW) time.                                                                                                                               |
| Agent interaction time (ms)                                                              | Measures the time that agents interacted with customers during inbound and outbound contacts.                                                                                                                                                                                       |
| Agent pause time (ms)                                                                    | Measures the time that an agent paused a contact after the contact was connected to the agent.                                                                                                                                                                                      |
| Contact duration (ms)                                                                    | Measures the time a contact spends from the contact initiation timestamp to disconnect timestamp                                                                                                                                                                                    |
| Contact flow duration (ms)                                                               | Measures the total time a contact spent in a flow. It's the IVR time, the time from the start until contact is queued.                                                                                                                                                              |
| Contact handle time (ms)                                                                 | Measures total time that an agent spent on contacts, including Customer Hold Time and After contact work time. This includes any time spent on contacts while in a custom status.                                                                                                   |
| Contact hold time (ms)                                                                   | Measures the total time that customers spent on hold after being connected to an agent.                                                                                                                                                                                             |
| Queue time (ms)                                                                          | Measures the average time that contacts waited in the queue before being answered by an agent.                                                                                                                                                                                      |
| Contact resolution time (ms)                                                             | Measures the average time, beginning from the time a contact was initiated to the time it resolved. The resolution time for a contact is defined as: beginning from InitiationTimestamp, and ending at AfterContactWorkEndTimestamp or DisconnectTimestamp, whichever one is later. |
| Agent greeting time (ms)                                                                 | Measures the first response time of agents on chat, indicating how quickly they engage with customers after joining the chat.                                                                                                                                                       |
| Agent interruption time (ms)                                                             | Measures the of total agent interruption time while talking to a contact.                                                                                                                                                                                                           |
| Talk time customer (ms)                                                                  | Measures the time that was spent talking in a conversation by a customer.                                                                                                                                                                                                           |
| Non talk time (ms)                                                                       | Measures the of total non-talk time in a voice conversation. Non-talk time refers to the combined duration of hold time and periods of silence exceeding 3 seconds, during which neither the agent nor the customer is engaged in conversation.                                     |
| Conversation duration (ms)                                                               | Measures the total conversation duration.                                                                                                                                                                                                                                           |
| Talk time (ms)                                                                           | Measures the time that was spent talking during a voice contact across either the customer or the agent.                                                                                                                                                                            |
| Talk time agent (ms)                                                                     | Measures the time that was spent talking in a conversation by an agent.                                                                                                                                                                                                             |
| Agent interruptions                                                                      | Quantifies the frequency of agent interruptions during customer interactions.                                                                                                                                                                                                       | Numeric input denoting count                                                                                                                                                                                                                                                                                   |
| Contact holds                                                                            | Measures the average number of times voice contacts were put on hold while interacting with an agent.                                                                                                                                                                               |
| Agent                                                                                    | Channel                                                                                                                                                                                                                                                                             | How the contact reached your contact center.                                                                                                                                                                                                                                                                   | Valid values: VOICE, CHAT, TASK, EMAIL                                                                                                                                                                            |
| Current Contact                                                                          | Channel                                                                                                                                                                                                                                                                             | How the contact reached your contact center.                                                                                                                                                                                                                                                                   | Valid values: VOICE, CHAT, TASK, EMAIL                                                                                                                                                                            |
| Initiation Method                                                                        | Indicates how the contact was initiated.                                                                                                                                                                                                                                            | Example: Inbound, Outbound, Transfer, Queue transfer, Callback, API, etc.<br>Please refer to the InitiationMethod section of<br>[ContactTraceRecord](ctr-data-model.md#ctr-ContactTraceRecord "ctr-data-model.md#ctr-ContactTraceRecord")<br>in the Amazon Connect Administrator Guide for more filter values. |
| ValidationTestType (Represented as \*_Contact Source_<br>• in the custom metric builder) | Represents the testing and simulation type. This field remains empty for non-simulated contacts. You can use this attribute in the analytics dashboard to filter out actual customer contacts or to identify whether a contact is simulated within your contact record object.      | Please refer to \*_connect:ValidationTestType_<br>• table row in the<br>[SegmentAttributes](connect-attrib-list.md#attribs-segment-attributes "connect-attrib-list.md#attribs-segment-attributes")<br>section for valid list of values.                                                                        |
| Subtype                                                                                  | Represents the subtype of the channel used for the contact.                                                                                                                                                                                                                         | Please refer to \*_connect:Subtype_<br>• table row in the<br>[SegmentAttributes](connect-attrib-list.md#attribs-segment-attributes "connect-attrib-list.md#attribs-segment-attributes")<br>section for valid list of values.                                                                                   |

## Groupings supported per metric primitive

category

| Metric Category                           | Grouping Key                | Grouping Dashboard Display Name |
| ----------------------------------------- | --------------------------- | ------------------------------- |
| Contact                                   | AGENT                       | Agent                           |
| AGENT_HIERARCHY_LEVEL_FIVE                | Agent hierarchy level five  |
| AGENT_HIERARCHY_LEVEL_FOUR                | Agent hierarchy level four  |
| AGENT_HIERARCHY_LEVEL_THREE               | Agent hierarchy level three |
| AGENT_HIERARCHY_LEVEL_TWO                 | Agent hierarchy level two   |
| AGENT_HIERARCHY_LEVEL_ONE                 | Agent hierarchy level one   |
| CHANNEL                                   | Channel                     |
| QUEUE                                     | Queue                       |
| Q_CONNECT_ENABLED                         | Amazon Q                    |
| ROUTING_PROFILE                           | Routing profile             |
| contact/segmentAttributes/connect:Subtype | Subtype                     |
| Agent                                     | AGENT                       | Agent                           |
| AGENT_HIERARCHY_LEVEL_FIVE                | Agent hierarchy level five  |
| AGENT_HIERARCHY_LEVEL_FOUR                | Agent hierarchy level four  |
| AGENT_HIERARCHY_LEVEL_THREE               | Agent hierarchy level three |
| AGENT_HIERARCHY_LEVEL_TWO                 | Agent hierarchy level two   |
| AGENT_HIERARCHY_LEVEL_ONE                 | Agent hierarchy level one   |
| CHANNEL                                   | Channel                     |
| QUEUE                                     | Queue                       |
| ROUTING_PROFILE                           | Routing profile             |
| Current Contact                           | CHANNEL                     | Channel                         |
| QUEUE                                     | Queue                       |
| ROUTING_PROFILE                           | Routing profile             |
| SUBTYPE                                   | Subtype                     |
| VALIDATION_TEST_TYPE                      | ValidationTestType          |

## Supported top-level metric filters per metric primitive category

| Metric Category                           | Top Level Filter Key        | Top Level Filter Dashboard Display Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Filter Key Description                 |
| ----------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Contact                                   | AGENT                       | Agent                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Valid input to this key is Agent ARNs  |
| AGENT_HIERARCHY_LEVEL_FIVE                | Agent hierarchy level five  | Valid input to this filter, is an Agent Hierarchy Level<br>ARN.<br>Read more about [Agent Hierarchy Level](agent-hierarchy.md#new-agent-hierarchy "agent-hierarchy.md#new-agent-hierarchy").                                                                                                                                                                                                                                                                                                                                                                                                        |
| AGENT_HIERARCHY_LEVEL_FOUR                | Agent hierarchy level four  |
| AGENT_HIERARCHY_LEVEL_THREE               | Agent hierarchy level three |
| AGENT_HIERARCHY_LEVEL_TWO                 | Agent hierarchy level two   |
| AGENT_HIERARCHY_LEVEL_ONE                 | Agent hierarchy level one   |
| CHANNEL                                   | Channel                     | Valid values: VOICE, CHAT, TASK, EMAIL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| QUEUE                                     | Queue                       | Valid inputs to this key are Queue ARNs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Q_CONNECT_ENABLED                         | Amazon Q                    | `TRUE` and `FALSE` are the only valid filter<br>values. This filter helps identify if or not Amazon Q in Connect<br>enabled as part of the flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ROUTING_PROFILE                           | Routing profile             | Valid input is Routing Profile ARNs. Please read below docs for<br>more details:<br>• [How Amazon Connect uses routing profiles](concepts-routing.md "concepts-routing.md")<br>• [Contact Trace Record Data Mode](ctr-data-model.md#ctr-Agent "ctr-data-model.md#ctr-Agent")                                                                                                                                                                                                                                                                                                                        |
| contact/segmentAttributes/connect:Subtype | Subtype                     | connect:Chat, connect:SMS, connect:Telephony, and connect:WebRTC<br>are a few valid filterValue examples, these are not the exhaustive<br>list of values                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| FEATURE                                   | N/A                         | Identifies if conversational analytics is enabled on the<br>flow.contact_lens_conversational_analytics is the only valid<br>value                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Agent                                     | AGENT                       | Agent                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Valid input to this key is Agent ARNs  |
| AGENT_HIERARCHY_LEVEL_FIVE                | Agent hierarchy level five  | Valid input to this filter, is an Agent Hierarchy Level<br>ARN.<br>Read more about [Agent Hierarchy Level](agent-hierarchy.md#new-agent-hierarchy "agent-hierarchy.md#new-agent-hierarchy").                                                                                                                                                                                                                                                                                                                                                                                                        |
| AGENT_HIERARCHY_LEVEL_FOUR                | Agent hierarchy level four  |
| AGENT_HIERARCHY_LEVEL_THREE               | Agent hierarchy level three |
| AGENT_HIERARCHY_LEVEL_TWO                 | Agent hierarchy level two   |
| AGENT_HIERARCHY_LEVEL_ONE                 | Agent hierarchy level one   |
| CHANNEL                                   | Channel                     | Valid values: VOICE, CHAT, TASK, EMAIL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| QUEUE                                     | Queue                       | Valid input to this key is Queue ARNs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ROUTING_PROFILE                           | Routing profile             | Valid input is Routing Profile ARNs. Please read below docs for<br>more details:<br>• [How Amazon Connect uses routing profiles](concepts-routing.md "concepts-routing.md")<br>• [Contact Trace Record Data Mode](ctr-data-model.md#ctr-Agent "ctr-data-model.md#ctr-Agent")                                                                                                                                                                                                                                                                                                                        |
| Current Contact                           | Channels                    | Channel                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Valid values: VOICE, CHAT, TASK, EMAIL |
| RoutingProfiles                           | Routing profile             | Valid input is Routing Profile ARNs. Please read below docs for<br>more details:<br>• [How Amazon Connect uses routing profiles](concepts-routing.md "concepts-routing.md")<br>• [Contact Trace Record Data Mode](ctr-data-model.md#ctr-Agent "ctr-data-model.md#ctr-Agent")                                                                                                                                                                                                                                                                                                                        |
| Queues                                    | Queue                       | Valid input to this key is Queue ARNs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RoutingStepExpressions                    | Routing step expression     | ROUTING_STEP_EXPRESSION is a valid filter key with a filter value up to 3000 length. This filter is case and order sensitive. JSON string fields must be sorted in ascending order and JSON array order should be kept as is.<br>Please read the below references for more info:<br>• [Routing step expression guide](../APIReference/API_Expression.md "../APIReference/API_Expression.md")<br>• [Routing step expression examples](../APIReference/API_GetCurrentMetricData.md#API_GetCurrentMetricData_Examples "../APIReference/API_GetCurrentMetricData.md#API_GetCurrentMetricData_Examples") |
| Subtypes                                  | Subtype                     | Please refer to connect:Subtype table row in the [SegmentAttributes](connect-attrib-list.md#attribs-segment-attributes "connect-attrib-list.md#attribs-segment-attributes") section for valid list of values.                                                                                                                                                                                                                                                                                                                                                                                       |
| ValidationTestTypes                       | Contact source              | Please refer to connect:ValidationTestType table row in the [SegmentAttributes](connect-attrib-list.md#attribs-segment-attributes "connect-attrib-list.md#attribs-segment-attributes") section for valid list of values.                                                                                                                                                                                                                                                                                                                                                                            |

## Guidelines for Metric Primitive creation

and usage with out-of-the-box metrics

### Creating Custom Metric from

Primitives

**Each metric primitive can use the same metric-level filter
only once**

Each metric primitive can only use a specific filter attribute once. If you apply
the same filter attribute again (even with a different value), it will overwrite
your previous condition.

**Metric primitives must be from the same
category**

Metric primitives are organized into categories based on what they measure (e.g.,
Contact metrics, Agent metrics, Queue metrics). You can only combine primitives
within the same category in a single custom metric. When selecting a metric
primitive, you'll see its category in the dropdown. If a metric appears disabled
(grayed out), hover over it to see the why, it must be from a different category
than your first selection.

- (e.g., Contact metrics, Agent metrics, Queue metrics). You can only
  combine primitives within the same category in a single custom metric. When
  selecting a metric primitive, you'll see its category in the dropdown. If a
  metric appears disabled (grayed out), hover over it to see why—typically
  because it's from a different category than your first selection.
- When selecting a metric primitive, you'll see its category in the
  dropdown. If a metric appears disabled (grayed out), hover over it to see
  why—typically because it's from a different category than your first
  selection.

**Arithmetic operations on metric primitives require
consistent filters**

When performing arithmetic operations (+, -, \*, /) on multiple metric primitives
within a single statistic, all primitives must use the same filter attribute.

Important: The filter values can differ; only the filter attribute must match.

Example: if the custom metric definition is of the form, SUM(Metric-1 + Metric-2),
here the Metric-1 and Metric-2 must utilize consistent filters

**Arithmetic operations on statistics operations support
metric primitive with different filters**

When performing arithmetic operations (+, -, \*, /) on multiple statistics
operations, you can combine metric primitive groups having different filters.

Example:

- Metric-1: a metric primitive from Contact category using Queue Time as a
  filter
- Metric-2: a metric primitive from Contact category using Contact Handle
  Time as a filter
- Valid custom metric definition: SUM(Metric-1) + SUM(Metric-2)

**Metrics only support specific statistics**

Not every metric primitive supports all statistic operations (SUM, AVG, MIN, MAX).
Using an unsupported statistic will cause an error.

Some metrics are only meaningful with certain calculations:

- **Count-based metrics** (e.g., Contacts
  Created): supports SUM, as AVG does not make sense
- **Duration metrics** (e.g., Contact Handle
  Time): support AVG, SUM, MIN, MAX

**A custom metric must have 1 to 5 components**

A component is each individual metric primitive you add to your custom metric
definition. If you're combining three different metrics, that's three
components.

- **Minimum**: 1 component (you must have at
  least one metric)
- **Maximum**: 5 components per custom
  metric

Please note: a custom metric utilizing a metric of **Current Contact** category can support at most 1 component.

**A statistic operation can support at most contain 10
elements (either components or constants)**

Each statistic operation (SUM, AVG, etc.) can contain a maximum of 10
elements.

**What Counts as an Element?**

Both of these count toward the 10-element limit:

- **Component identifiers** (e.g., Metric_1,
  Metric_2)
- **Constants/numbers** (e.g., 100, 0.5)

### Guidelines for using custom

metrics with out-of-the-box metrics

A custom metric can only be added to a dashboard widget if the metric's underlying
primitives support ALL filters and groupings applied to that widget.

Common Scenario: You create a custom metric using "Agent Idle Time" primitive, which does NOT
support "Channel" as a filter or grouping dimension.

Result: You cannot add this custom metric to any widget that:

- Filters by Channel, OR
- Groups data by Channel

Refer to the Metric Primitive definition section for supported filters and
groupings of metric primitives.
