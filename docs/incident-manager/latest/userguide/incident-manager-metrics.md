AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Monitoring metrics in Incident Manager with

Amazon CloudWatch

Incident Manager provides aggregate metrics that you can monitor in Amazon CloudWatch. You can use these
metrics to identify incident and response plan trends.

###### These metrics include:

- Number of incidents created over a given period of time
- The time to respond to and resolve those incidents
- Number of incidents resolved
  You can monitor Incident Manager metrics to better understand your operational health, and take
  meaningful actions to drive the operational excellence of your incident response.
  Incident Manager metrics are available in all Incident Manager Regions. Your metrics will be available
  to view in Amazon CloudWatch for all the Regions you specified in your replication set when
  on-boarding to Incident Manager. You can view the published metrics in the Region that actions
  for the incident were taken. There is no additional charge for these metrics.

###### On the CloudWatch console, you can build dashboards with these metrics to:

- Measure and review your existing incident load
- Track whether your incident load is increasing, decreasing, or remaining the
  same
- More effectively use Incident Manager to reduce the frequency, duration, and impact of
  your incidents
  This page describes the Incident Manager metrics available on the CloudWatch console.

###### Important

For a customer-generated event, if the [source](../APIReference/API_TriggerDetails.md#IncidentManager-Type-TriggerDetails-source "../APIReference/API_TriggerDetails.md#IncidentManager-Type-TriggerDetails-source") value in `TriggerDetails`is named using non-ASCII
characters, then metrics for the event won't be reported in Amazon CloudWatch metrics, which
doesn't support non-ASCII text. `source` can provided programatically only,
such as by using an SDK or the AWS CLI.

Incident Manager sends the following metrics to CloudWatch.

| Metric                       | Description                                                                                                                                                                                                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NumberOfCreateIncidents`    | Number of incidents created.<br>Valid Dimensions: [](Empty dimension), [`ResponsePlan`],<br>[`Impact`], [`Source`],<br>[`ResponsePlan`, `Impact`],<br>[`ResponsePlan`, `Source`]<br>Unit: Count                                                                                          |
| `NumberOfResolveIncidents`   | Number of incidents resolved.<br>Valid Dimensions: [](Empty dimension), [`ResponsePlan`],<br>[`Impact`], [`Source`],<br>[`ResponsePlan`, `Impact`],<br>[`ResponsePlan`, `Source`]<br>Unit: Count                                                                                         |
| `TimeToFirstAcknowledgement` | Time difference between the incident create time and the time the<br>first acknowledgment was made to the incident.<br>Valid Dimensions: [](Empty dimension), [`ResponsePlan`],<br>[`Impact`], [`Source`],<br>[`ResponsePlan`, `Impact`],<br>[`ResponsePlan`, `Source`]<br>Unit: Seconds |
| `TimeToResolveIncident`      | Time difference between when the incident was created and when it was<br>resolved.<br>Valid Dimensions: ](Empty dimension), [`ResponsePlan`],<br>[`Impact`], [`Source`],<br>[`ResponsePlan`, `Impact`],<br>[`ResponsePlan`, `Source`]<br>Unit: Seconds                                   |

## Viewing Incident Manager metrics on the CloudWatch

console

###### To view Incident Manager metrics in the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Select the `IncidentManager` namespace.
4. On the **Metrics** tab, choose a dimension, and then choose a
   metric.

For more information about working with CloudWatch metrics, see the following topics in the
_Amazon CloudWatch User Guide_:

- [Metrics](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric")
- [Using
  Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")

## Dimensions for

Metrics

Incident Manager metrics use the `IncidentManager` namespace and provide metrics
for the following dimension(s):

| Dimension                             | Description                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------ |
| `By Response Plan`                    | View aggregate metrics by response plan.                                                   |
| `By Impact Level`                     | View aggregate metrics by the level of severity.                                           |
| `By Source`                           | View metrics for incidents created manually, by CloudWatch alarm, or<br>EventBridge event. |
| `Across All Incidents`                | View aggregate metrics for all incidents in the current AWS<br>Region.                     |
| `Response Plan name and Source`       | View aggregate metrics for each combination of response plan and<br>source.                |
| `Response Plan Name and Impact Level` | View aggregate metrics for each combination of response plan and<br>level of severity.     |
