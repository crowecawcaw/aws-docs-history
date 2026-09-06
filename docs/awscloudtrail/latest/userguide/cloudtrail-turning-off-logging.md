

# Turning off logging for a trail
<a name="cloudtrail-turning-off-logging"></a>

When you create a trail, logging is turned on automatically. You can turn off logging for a trail from the trail's details page.

**Note**  
When you turn off logging, existing logs are still stored in the trail's Amazon S3 bucket and continue to incur S3 charges. For information on S3 pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

**Event delivery after logging is stopped**  
After you turn off logging for a trail, the trail can still receive events that occurred before logging was turned off. Events can be delayed for a number of reasons, including high network traffic, connectivity issues, a service outage, or updates to existing events. CloudTrail uses the most recent time that logging was turned off to determine whether to deliver delayed events, rather than the logging state of the trail at the time the event occurred. As a result, delayed events that occurred before logging was last turned off can still be delivered to the trail. For more information about delayed event delivery, see the `addendum` field in [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md).  
Additionally, event selectors and advanced event selectors are not evaluated for delayed events delivered to a trail after logging is turned off. This means that a trail can receive any type of event that occurred before logging was turned off, regardless of the trail's event selector configuration.

**To turn off logging for a trail with the CloudTrail console**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, choose **Trails**, and then choose the name of the trail.

1. At the top of the trail details page, choose **Stop logging** to turn off logging for the trail.

1. When you are prompted to confirm, choose **Stop logging**. CloudTrail stops logging activity for that trail.

1. To resume logging for that trail, choose **Start logging** on the trail configuration page.