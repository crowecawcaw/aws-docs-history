# Listing Amazon S3 on Outposts

buckets

With Amazon S3 on Outposts, you can create S3 buckets on your AWS Outposts and easily store and
retrieve objects on premises for applications that require local data access, local data
processing, and data residency. S3 on Outposts provides a new storage class, S3 Outposts
(`OUTPOSTS`), which uses the Amazon S3 APIs, and is designed to store
data durably and redundantly across multiple devices and servers on your AWS Outposts. You communicate with your Outpost bucket
by using an access point
and endpoint connection over a virtual private cloud (VPC). You can use the same APIs and
features on Outpost buckets as you do on Amazon S3 buckets, including access policies, encryption, and tagging.
You can use S3 on Outposts through the AWS Management Console, AWS Command Line Interface (AWS CLI), AWS SDKs, or REST API. For more information, see [What is Amazon S3 on Outposts?](S3onOutposts.md "S3onOutposts.md")

For more information about working with buckets in S3 on Outposts, see [Working with S3 on Outposts buckets](S3OutpostsWorkingBuckets.md "S3OutpostsWorkingBuckets.md").

The following examples show you how to return a list of your S3 on Outposts buckets by using
the AWS Management Console, AWS CLI, and AWS SDK for Java.

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Outposts
   buckets**.
3. Under **Outposts buckets**, review your list of
   S3 on Outposts buckets.
   The following AWS CLI example gets a list of buckets in an Outpost. To use this
   command, replace each `user input placeholder`
   with your own information. For more information about this command, see [list-regional-buckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-regional-buckets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-regional-buckets.html") in the _AWS CLI
   Reference_.

```
aws s3control list-regional-buckets --account-id `123456789012` --outpost-id `op-01ac5d28a6a232904`
```

The following SDK for Java example gets a list of buckets in an Outpost. For more
information, see [ListRegionalBuckets](../API/API_control_ListRegionalBuckets.md "../API/API_control_ListRegionalBuckets.md") in the _Amazon Simple Storage Service API Reference_.

```
import com.amazonaws.services.s3control.model.*;

public void listRegionalBuckets() {

    ListRegionalBucketsRequest reqListBuckets = new ListRegionalBucketsRequest()
            .withAccountId(AccountId)
            .withOutpostId(OutpostId);

    ListRegionalBucketsResult respListBuckets = s3ControlClient.listRegionalBuckets(reqListBuckets);
    System.out.printf("ListRegionalBuckets Response: %s%n", respListBuckets.toString());

}
```
