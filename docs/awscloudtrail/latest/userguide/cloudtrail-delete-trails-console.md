# Deleting a trail with the CloudTrail console

You can delete trails with the CloudTrail console. If an organization's management account or delegated administrator 
 account deletes an organization trail, the trail is removed from all member accounts of the organization.

###### Important


 While deleting a CloudTrail trail is an irreversible action, CloudTrail does not
 delete log files in the Amazon S3 bucket for that trail, the Amazon S3 bucket itself, or the
 CloudWatch log group to which the trail delivers events. Deleting a multi-Region trail
 will stop logging of events in all AWS Regions enabled in your AWS account. Deleting a
 single-Region trail will stop logging of events in that Region only. It will not stop
 logging of events in other Regions even if the trails in those other Regions have
 identical names to the deleted trail.
 

For information about account closure and deletion of CloudTrail trails, see [AWS account closure and trails](cloudtrail-account-closure.md "cloudtrail-account-closure.md").

If you've enabled CloudTrail management events in Amazon Security Lake, you are required to maintain at least one
 organizational trail that is multi-Region and logs both `read` and
 `write` management events. You cannot delete a trail if it is the only trail
 you have that meets this requirement, unless you turn off CloudTrail management events in Security Lake.

###### To delete a trail with the CloudTrail console

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. Open the **Trails** page of the CloudTrail console.
3. Choose the trail name.
4. At the top of the trail details page, choose **Delete**.
5. When you are prompted to confirm, choose **Delete** to delete the
 trail permanently. The trail is removed from the list of trails. Log files that were
 already delivered to the Amazon S3 bucket are not deleted and continue to incur S3 charges.


###### Note

Content delivered to Amazon S3 buckets might contain customer content. 
 For more information about removing sensitive data, see [Emptying a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html") 
 and [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html") in the *Amazon S3 User Guide*.
