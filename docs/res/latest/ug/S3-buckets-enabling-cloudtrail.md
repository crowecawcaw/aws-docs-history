

End of development notice: AWS is discontinuing development of Research and Engineering Studio on AWS (RES). 2026.09 is the final release, supported through September 30, 2027. RES remains open source and keeps running in your account. For more information, see [RES end of support](res-end-of-support.md).

# Enabling CloudTrail
<a name="S3-buckets-enabling-cloudtrail"></a>

To enable CloudTrail in your account using the CloudTrail console, follow the instructions provided in [ Creating a trail with the CloudTrail console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*. CloudTrail will log the access to S3 buckets by recording the IAM role that accessed it. This can be linked back to an instance ID, which is linked to a project or user.