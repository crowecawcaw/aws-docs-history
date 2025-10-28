# Conversational analytics metrics in

Amazon Connect

The following metrics are derived from Contact Lens conversational
analytics. These metrics are available only when [Contact Lens is enabled for your instance](enable-analytics.md#enable-cl "enable-analytics.md#enable-cl") and [conversational analytics](enable-analytics.md#enable-callrecording-speechanalytics "enable-analytics.md#enable-callrecording-speechanalytics")
is enabled on the contact.

These metrics are displayed on the Real-time and Historical metrics reports. For
instructions about how add these metrics to your report, see [How to create a
historical metrics report](create-historical-metrics-report.md#historical-reports-howto-create "create-historical-metrics-report.md#historical-reports-howto-create").

Also check out the [Contact Lens conversational analytics dashboard](contact-lens-conversational-analytics-dashboard.md "contact-lens-conversational-analytics-dashboard.md") for data
visualizations about the trends of contact drivers over time.

## Agent talk time percent

This metric measures the talk time by an agent in a voice conversation as a percent of the total
conversation duration.

**Metric type**: Percent

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `PERCENT_TALK_TIME_AGENT`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Agent talk time percent

**Calculation logic**:

- Sum all the intervals in which an agent was engaged
  in conversation (talk time agent).
- Divide the sum by the total conversation duration.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Average agent greeting

time

This metric provides the average first response time of agents on chat,
indicating how quickly they engage with customers after joining the chat.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_GREETING_TIME_AGENT`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Average agent greeting time

**Calculation logic**:

- This metric is calculated by dividing the total time it takes for an agent to initiate their
  first response by the number of chat contacts.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Average agent

interruptions

This metric quantifies the average frequency of agent interruptions during
customer interactions.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_INTERRUPTIONS_AGENT`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Average agent interruptions

**Calculation logic**:

- This metric is calculated by dividing the total number of agent interruptions by the
  total number of contacts.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Average agent

interruption time

This metric measures the average of total agent interruption time while talking to a contact.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_INTERRUPTION_TIME_AGENT`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Average agent interruption time

**Calculation logic**:

- Sum the interruption intervals within each
  conversation.
- Divide the sum the number of conversations that
  experienced at least one interruption.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Average agent talk

time

This metric measures the average time that was spent talking in a conversation by an agent.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_TALK_TIME_AGENT`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Average agent talk time

**Calculation logic**:

- Sum the durations of all intervals during which the agent
  was speaking.
- Divide the sum by the total number of contacts.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Average conversation

duration

This metric measures the average conversation duration of voice contacts with agents.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_CONVERSATION_DURATION`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Average conversation duration

**Calculation logic**:

- This metric is calculated by the total time from the start of the conversation until the last
  word spoken by either the agent or the customer.
- This value is then divided by
  the total number of contacts to provide an average representation of the
  conversation time spent on the call.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Average customer talk

time

This metric measures the average time that was spent talking in a
conversation by a customer.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_TALK_TIME_CUSTOMER`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Average customer talk time

**Calculation logic**:

- Sum the durations of all intervals during which the
  customer was speaking.
- Divide the sum by the total number of contacts.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Average non-talk time

This metric provides the average of total non-talk time in a voice conversation. Non-talk time refers
to the combined duration of hold time and periods of silence exceeding 3
seconds, during which neither the agent nor the customer is engaged in
conversation.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_NON_TALK_TIME`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Average non-talk time

**Calculation logic**:

- Sum all the intervals in which
  both participants remained silent.
- Divide the sum by the number of contacts.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Average talk time

This metric measures the average time that was spent talking during a voice contact across either the
customer or the agent.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_TALK_TIME`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Average talk time

**Calculation logic**:

- Sum all the intervals in
  which either an agent, a customer, or both were engaged in conversation.
- Divide the sum by the total number of contacts.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Customer talk time percent

This metric provides the talk time by a customer in a voice conversation as a percent of the total
conversation duration.

**Metric type**: Percent

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `PERCENT_TALK_TIME_CUSTOMER`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Customer talk time percent

**Calculation logic**:

- Sum all the intervals in which a customer was engaged in conversation.
- Divide the sum by the total conversation duration.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Non-talk time percent

This metric provides the non-talk time in a voice conversation as a percent of the total
conversation duration.

**Metric type**: Percent

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `PERCENT_NON_TALK_TIME`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Non-talk time percent

**Calculation logic**:

- Sum all the intervals in which participants remained silent (non-talk time).
- Divide the sum by the total conversation duration.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.

## Talk time percent

This metric provides the talk time in a voice conversation as a percent of the total conversation
duration.

**Metric type**: Percent

**Metric category**: Conversational analytics driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `PERCENT_TALK_TIME`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Talk time percent

**Calculation logic**:

- Sum all the intervals in which either an agent, a customer, or both were engaged in
  conversation (talk time).
- Divide the sum by the total conversation
  duration.

**Notes**:

- This metric is available only for contacts analyzed by Contact Lens conversational
  analytics.
