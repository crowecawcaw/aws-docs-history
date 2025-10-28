# Outbound campaign metrics in Amazon Connect

The following outbound campaign driven metrics are available on the [outbound campaigns performance
dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md") and by using the GetMetricDataV2 API.

## Average dials per minute

This metric measures the average
number of outbound campaign dials per minute for the specified
start time and end time.

**Metric type**: Double

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_DIALS_PER_MINUTE`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md"),
  Avg. dials per minute

**Notes**:

- This metric is available only for outbound campaigns that use the
  agent assisted voice and automated voice delivery modes.
- Data for this metric is available starting from June 25, 2024 0:00:00
  GMT.

## Average wait time after customer connection

This metric measures the average duration of total wait time by the customer after they answer the
outbound call through the Amazon Connect dialer.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AVG_WAIT_TIME_AFTER_CUSTOMER_CONNECTION`

**Notes**:

- This metric is available only for outbound campaigns that use the agent assisted
  voice and automated voice delivery modes.
- Data for this metric is available starting from June 25, 2024 0:00:00
  GMT.

## Campaign contacts abandoned after

X

This metric counts the outbound campaign calls that were connected to a live customer but did not get connected to an agent within X seconds.
The possible values for X are from 1 to 604800 inclusive.
This metric is only available with answering machine detection enabled. For more information about answering machine detection, see
[Best practices for answering machine detection](campaign-best-practices.md#machine-detection "campaign-best-practices.md#machine-detection").

**Metric type**: Integer

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `CAMPAIGN_CONTACTS_ABANDONED_AFTER_X`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md"),
  Campaign contacts abandoned after x seconds rate

**Notes**:

- This metric is available only for outbound campaigns using the agent assisted
  voice and automated voice delivery modes.
- Data for this metric is available starting from June 25, 2024 0:00:00
  GMT.

## Campaign contacts abandoned after X

rate

This metric measures the percentage of outbound campaign calls that were connected to a live customer
but did not get connected to an agent within X seconds divided by the count of contacts connected to a live customer in an outbound campaign.
The possible values for X are from 1 to 604800 inclusive.

**Metric type**: Percent

- Min value: 0.00%
- Min value: 100.00%

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `CAMPAIGN_CONTACTS_ABANDONED_AFTER_X_RATE`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md"),
  Campaign contacts abandoned rate

**Notes**:

- This metric is only available with answering machine detection enabled. For more information about answering machine detection, see
  [Best practices for answering machine detection](campaign-best-practices.md#machine-detection "campaign-best-practices.md#machine-detection"). This metric is available only for outbound campaigns using the agent
  assisted voice and automated voice delivery modes.
- Data for this metric is available starting from June 25, 2024 0:00:00
  GMT.

## Campaign interactions

This metric counts the outbound campaign
interactions after a successful delivery attempt.
Example interactions include `Open`, `Click`, and `Compliant`.

**Metric type**: Integer

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `CAMPAIGN_INTERACTIONS`

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md")

**Notes**:

- This metric is available only for outbound campaigns that use the email delivery mode.
- Data for this metric is available starting from November 6, 2024 0:00:00 GMT.

## Campaign progress rate

This metric measures the percentage of outbound campaign
recipients attempted for delivery, out of the total number of recipients targeted. This is calculated as: (Recipients attempted / Recipients targeted) \* 100.

**Metric type**: Percent

- Min value: 0.00%
- Max value: 100.00%

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `CAMPAIGN_PROGRESS_RATE`

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md")

**Notes**:

- This metric is only available for outbound campaigns initiated using a customer segment. It is not available for event triggered campaigns.
- Data for this metric is available starting from April 30, 2025 0:00:00 GMT.

## Campaign send attempts

This metric counts the outbound campaign
send requests sent by Amazon Connect for delivery.
A campaign send request represents a send attempt made to reach out to an recipient using email, SMS, or telephony delivery mode.

**Metric type**: Integer

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `CAMPAIGN_SEND_ATTEMPTS`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md"),
  Send attempts

**Notes**:

- Data for this metric is available starting from November 6, 2024 0:00:00 GMT.

## Campaign send exclusions

This metric measures the count of outbound campaign send attempts that were excluded from the targeted segment during a campaign execution. Example exclusion reasons: MISSING_TIMEZONE, MISSING_CHANNEL

**Metric type**: Integer

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `CAMPAIGN_SEND_EXCLUSIONS`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md"),
  Campaign send exclusions

**Notes**:

- For more details on the exclusion reasons, see campaign_event_type under [Outbound Campaign Events](data-lake.md#campaign-events "data-lake.md#campaign-events") in the Data Lake documentation.
- Data for this metric is available starting from April 30, 2025 0:00:00 GMT.

## Delivery attempts

This metric measures the delivery outcome of a campaign outreach attempt.
The count of outbound campaign contact outcomes from the Amazon Connect dialer, or the count of outbound campaign email
or SMS message outcomes that were successfully sent to Amazon Connect to be delivered.

**Metric type**: Integer

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `DELIVERY_ATTEMPTS`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md"), Delivery attempts

**Notes**:

- For details about telephony disposition definitions, see DisconnectReason
  for outbound campaigns and AnsweringMachineDetectionStatus in the
  [ContactTraceRecord](ctr-data-model.md#ctr-ContactTraceRecord "ctr-data-model.md#ctr-ContactTraceRecord").
  For details about email and SMS disposition definitions, see campaign_event_type
  in the [Outbound campaign events](data-lake-outbound-campaigns-data.md#data-lake-oc-events "data-lake-outbound-campaigns-data.md#data-lake-oc-events") table.
- Data for this metric is available starting from June 25, 2024 0:00:00 GMT for the Telephony delivery mode and
  November 6, 2024 0:00:00 GMT for the Email and SMS delivery modes.

## Delivery attempt disposition

rate

This metric measures the percentage of each delivery outcome from a campaign outreach.
The percent of call classification by answering machine detection or disconnect reason from outbound campaign contacts executed by the Amazon Connect dialer,
or the percent of outbound campaign email or SMS message outcomes that was successfully sent to Amazon Connect to be delivered.

**Metric type**: Percent

- Min value: 0.00%
- Max value: 100.00%

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `DELIVERY_ATTEMPT_DISPOSITION_RATE`

**Notes**:

- Dispositions for the agent assisted voice and automated
  voice delivery modes are available with answering machine detection enabled.
- Data for this metric is available starting from June 25, 2024 0:00:00 GMT for the Telephony delivery mode and
  November 6, 2024 0:00:00 GMT for the Email and SMS delivery modes.

## Human answered

This metric counts the outbound campaign calls that were connected to a live customer.
This metric is available only when answering machine detection is enabled.

**Metric type**: Integer

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `HUMAN_ANSWERED_CALLS`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md"),
  Human answered

**Notes**:

- This metric is available only for outbound campaigns that use the agent assisted
  voice and automated voice delivery modes.
- Data for this metric is available starting from June 25, 2024 0:00:00
  GMT.

## Recipients attempted

This metric measures the approximate count of outbound campaign recipients attempted for delivery.

**Metric type**: Integer

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `RECIPIENTS_ATTEMPTED`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md"),
  Recipients attempted

**Notes**:

- This metric is only available for outbound campaigns initiated using a customer segment. It is not available for event triggered campaigns.
- Data for this metric is available starting from April 30, 2025 0:00:00 GMT.

## Recipients interacted

This metric measures the approximate
count of outbound campaign recipients who interacted
with the engagement after a successful delivery attempt. Example interactions include: Open, Click, Complaint

**Metric type**: Integer

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `RECIPIENTS_INTERACTED`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md")

**Notes**:

- This metric is only available for outbound campaigns initiated using a customer segment. It is not available for event triggered campaigns.
- Data for this metric is available starting from April 30, 2025 0:00:00 GMT.

## Recipients targeted

This metric measures the count of outbound campaign recipients identified as the target audience for the campaign.

**Metric type**: Integer

**Metric category**: Outbound campaigns driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `RECIPIENTS_TARGETED`

**How to access using the Amazon Connect admin website**:

- Dashboard: [Outbound campaigns
  performance dashboard](outbound-campaigns-performance-dashboard.md "outbound-campaigns-performance-dashboard.md"),
  Recipients targeted

**Notes**:

- This metric is only available for outbound campaigns initiated using a customer segment. It is not available for event triggered campaigns.
- Data for this metric is available starting from April 30, 2025 0:00:00 GMT.
