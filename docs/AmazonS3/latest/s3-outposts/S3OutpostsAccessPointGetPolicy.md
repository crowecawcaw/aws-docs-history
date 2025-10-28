# Viewing an access point policy for an S3 on Outposts access point

Access points have distinct permissions and network controls that Amazon S3 on Outposts
applies for any request that is made through that access point. Each access point enforces a customized access point
policy that works in conjunction with the bucket policy that is attached to the underlying
bucket. For more information, see [Access points](S3OutpostsWorkingBuckets.md#S3OutpostsAP "S3OutpostsWorkingBuckets.md#S3OutpostsAP").

For more information about working with access points in S3 on Outposts, see [Working with S3 on Outposts buckets](S3OutpostsWorkingBuckets.md "S3OutpostsWorkingBuckets.md").

The following topics show you how to view your S3 on Outposts access point policy by using the
AWS Management Console, AWS Command Line Interface (AWS CLI), and AWS SDK for Java.

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Outposts
   access points**.
3. Choose the Outposts access point that you want to view the policy for.
4. On the **Permissions** tab, review the S3 on Outposts access point policy.
5. To edit the access point policy, see [Adding or editing an access point policy](S3OutpostsAccessPointEditPolicy.md "S3OutpostsAccessPointEditPolicy.md").
   The following AWS CLI example gets a policy for an Outposts access point. To run this
   command, replace the `user input placeholders`
   with your own information.

```
aws s3control get-access-point-policy --account-id `123456789012` --name arn:aws:s3-outposts:`region`:`123456789012`:outpost/`op-01ac5d28a6a232904`/accesspoint/`example-outposts-access-point`
```

The following SDK for Java example gets a policy for an Outposts access point.

```
import com.amazonaws.services.s3control.model.*;

public void getAccessPointPolicy(String accessPointArn) {

    GetAccessPointPolicyRequest reqGetAccessPointPolicy = new GetAccessPointPolicyRequest()
            .withAccountId(AccountId)
            .withName(accessPointArn);

    GetAccessPointPolicyResult respGetAccessPointPolicy = s3ControlClient.getAccessPointPolicy(reqGetAccessPointPolicy);
    System.out.printf("GetAccessPointPolicy Response: %s%n", respGetAccessPointPolicy.toString());
    printWriter.printf("GetAccessPointPolicy Response: %s%n", respGetAccessPointPolicy.toString());

}
```
