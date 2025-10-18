# Turning off logging for a trail

When you create a trail, logging is turned on automatically. You can turn off logging for
 a trail from the trail's details page.

###### Note

When you turn off logging, existing logs are still stored in the trail's Amazon S3 bucket and continue to incur S3 charges. 
 For information on S3 pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### To turn off logging for a trail with the CloudTrail console

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Trails**, and then choose the
 name of the trail.
3. At the top of the trail details page, choose **Stop logging** to
 turn off logging for the trail.
4. When you are prompted to confirm, choose **Stop logging**. CloudTrail
 stops logging activity for that trail.
5. To resume logging for that trail, choose **Start logging** on the
 trail configuration page.
