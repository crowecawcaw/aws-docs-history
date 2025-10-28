# Create CloudWatch alarms that fit your business needs in Incident Detection and Response

When you create Amazon CloudWatch alarms, there are several steps that you can take to
make sure your alarms best fit your business needs.

###### Note

For examples of recommended CloudWatch alarms for AWS services to onboard to Incident Detection and Response, see [Incident Detection and Response Alarm Best Practices on AWS re:Post](https://repost.aws/selections/KP6FA7iQgVSVeSNq1jAcjwxg/incident-detection-and-response-idr "https://repost.aws/selections/KP6FA7iQgVSVeSNq1jAcjwxg/incident-detection-and-response-idr").

## Review your proposed CloudWatch alarms

Review your proposed alarms to make sure that they only enter the "Alarm" state when there is critical impact to the monitored workload (loss of revenue or degraded customer experience that significantly reduces performance). For example, do you consider this alarm critical enough that you must react immediately if it goes into the "Alarm" state?

The following are suggested metrics that might represent critical business impact, such as affecting your end users' experience with an application:

- **CloudFront:** For more information, see [Viewing CloudFront and edge function metrics](../../../AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.md "../../../AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.md").
- **Application Load Balancers:** It's a best practice that you create the following alarms for Application Load Balancers, if possible:

      + HTTPCode\_ELB\_5XX\_Count
      + HTTPCode\_Target\_5XX\_Count

  The preceding alarms allow you to monitor responses from targets that are behind the Application Load Balancer, or behind other resources. This makes it easier to identify the source of 5XX errors. For more information, see [CloudWatch metrics for your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.md "../../../elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.md").

- **Amazon API Gateway:** If you use WebSocket API in Elastic Beanstalk, then consider using the following metrics:

      + Integration error rates (filtered to 5XX errors)
      + Integration latency
      + Execution errors

  For more information, see [Monitoring WebSocket API execution with CloudWatch metrics](../../../apigateway/latest/developerguide/apigateway-websocket-api-logging.md "../../../apigateway/latest/developerguide/apigateway-websocket-api-logging.md").

- **Amazon Route 53:** Monitor the **EndPointUnhealthyENICount** metric. This metric is the number of elastic network interfaces in the **Auto-recovering** status. This status indicates attempts by the resolver to recover one or more of the Amazon Virtual Private Cloud network interfaces that are associated with the endpoint (specified by **EndpointId**). In the recovery process, the endpoint functions with limited capacity. The endpoint can't process DNS queries until it's fully recovered. For more information, see [Monitoring Amazon Route 53 Resolver endpoints with Amazon CloudWatch](../../../Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.md "../../../Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.md").

## Validate your alarm configurations

After you confirm that your proposed alarms fit your business needs, validate the configuration and history of the alarms:

- Validate the **Threshold** for the metric to enter the "Alarm" state against the metric's graph trend.
- Validate the **Period** used for polling data points. Polling data points at 60 seconds assist in early incident detection.
- Validate the **DatapointToAlarm** configuration. In most cases, it's a best practice to set this to 3 out of 3 or 5 out of 5. In an incident, the alarm triggers after 3 minutes when set as [60 second metrics with 3 out of 3 DatapointToAlarm] or 5 minutes when set as [60 second metrics with 5 out of 5 DatapointToAlarm]. Use this combination to eliminate noisy alarms.

###### Note

The preceding recommendations might vary depending on how you use a service. Each AWS service operates differently within a workload. And, the same service might operate differently when used in multiple places. You must be sure that you understand how your workload utilizes the resources that feed the alarm, as well as the upstream and downstream effects.

## Validate how your alarms handle missing

data

Some metric sources don't send data to CloudWatch at regular intervals. For these metrics, it's a best practice to treat missing data as **notBreaching**. For more information, see [Configuring how CloudWatch alarms treat missing data](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data") and [Avoiding premature transitions to alarm state](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#CloudWatch-alarms-avoiding-premature-transition "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#CloudWatch-alarms-avoiding-premature-transition").

For example, if a metric monitors an error rate, and there are no errors, then the metric reports no data (nil) data points. If you configure the alarm to treat missing data as **Missing**, then a single breaching data point followed by two no data (nil) data points causes the metric to go into the "Alarm" state (for 3 out of 3 data points). This is because the missing data configuration evaluates the last known data point in the evaluation period.

In cases where metrics monitor an error rate, in the absence of service degradation you can assume that no data is a good thing. It's a best practice to treat missing data as **notBreaching** so that missing data is treated as "OK" and the metric doesn't enter the "Alarm" state on a single data point.

## Review the history of each alarm

If an alarm's history shows that it frequently enters the "Alarm" state and then recovers quickly, then the alarm might become an issue for you. Make sure that you tune the alarm to prevent noise or false alarms.

## Validate metrics for underlying

resources

Make sure that your metrics look at valid underlying resources and use the correct statistics. If an alarm is configured to review invalid resource names, then the alarm might not be able to track the underlying data. This might cause the alarm to enter the "Alarm" state.

## Create composite alarms

If you provide Incident Detection and Response operations with a large number of alarms for onboarding, you might be asked to create composite alarms. Composite alarms reduce the total number of alarms that need to be onboarded.
