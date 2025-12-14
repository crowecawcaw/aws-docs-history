# Define and configure alarms in Incident Detection and Response

AWS works with you to define metrics and alarms to provide visibility into the performance of your applications and their underlying
AWS infrastructure. We ask that alarms adhere to the following criteria when defining and configuring thresholds:

- Alarms only enter the "Alarm" state when there is critical impact to the monitored workload (loss of revenue or degraded
  customer experience that significantly reduces performance) that requires immediate operator attention.
- Alarms must also engage your specified resolvers for the workload at the same time, or prior to, engaging the incident management team.
  Incident management engineers should be collaborating with your specified resolvers in the mitigation process, not serve as a first line
  responder and then escalate to you.
- Alarm thresholds must be set to an appropriate threshold and duration so that any time an alarm fires, an investigation must take place.
  If an alarm is flapping between "Alarm" and "OK" state, sufficient impact is occurring to warrant operator response and attention.
  **Types of alarms**:

- Alarms that portray the level of business impact and pass relevant information for simple fault detection.
- Amazon CloudWatch canaries. For more information, see
  [Canaries and X-Ray tracing](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.md"), and
  [X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/").
- Aggregate alarming (monitoring of dependencies)
  The following table provides example alarms, all using the CloudWatch monitoring system.

| Metric name / Alarm threshold                                                                                            | Alarm ARN or resource ID                                             | If this alarm fires                             | If engaged, cut a Premium Support Case for these services |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------- |
| API errors /<br># of errors >= 10 for 10 datapoints                                                                      | arn:aws:cloudwatch:us-west-2:000000000000:alarm:E2MPmimLambda-Errors | Ticket cut to database administrator (DBA) team | Lambda, API Gateway                                       |
| ServiceUnavailable (Http status code 503)<br># of errors >=3 for 10 datapoints (different clients) in a 5 minute window  | arn:aws:cloudwatch:us-west-2:xxxxx:alarm:httperrorcode503            | Ticket cut to Service team                      | Lambda, API Gateway                                       |
| ThrottlingException (Http status code 400)<br># of errors >=3 for 10 datapoints (different clients) in a 5 minute window | arn:aws:cloudwatch:us-west-2:xxxxx:alarm:httperrorcode400            | Ticket cut to Service team                      | EC2, Amazon Aurora                                        |

For more details, see [AWS Incident Detection and Response monitoring and observability](observe-idr.md "observe-idr.md").

If you prefer to use automation tools to onboard alarms, the Incident Detection and Response Command Line Interface (CLI) helps you deploy and onboard your alarms. For more details, see [AWS Incident Detection and Response CLI](idr-cli.md "idr-cli.md").

**Key outputs:**

- Definition and configuration of alarms on your workloads.
- Completion of the alarm details on the onboarding questionnaire.

###### Topics

- [Create CloudWatch alarms](idr-alarms-fit-purpose.md "idr-alarms-fit-purpose.md")
- [Build CloudWatch alarms with CloudFormation templates](idr-create-alarms-with-cfn.md "idr-create-alarms-with-cfn.md")
- [Example use cases for CloudWatch alarms](idr-ex-alarm-use-cases.md "idr-ex-alarm-use-cases.md")
