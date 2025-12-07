# Enabling ABAC in general purpose buckets

Attribute-based access control (ABAC) is an authorization strategy that you use to define permissions based on attributes, i.e., tags. By default, ABAC is disabled for all Amazon S3 general purpose buckets. To use ABAC for general purpose buckets, you must enable it.

Before enabling ABAC for your general purpose bucket, we recommend that you first complete the tasks described in the following topics:

###### Topics

- [Auditing your policies before enabling ABAC](#buckets-tagging-enable-abac-audit "#buckets-tagging-enable-abac-audit")

## Auditing your policies before enabling ABAC

Before you enable ABAC for your bucket, if your bucket has tags, audit your access
control policies to review if tag-based conditions reference any of the existing tags on your
buckets. If they do, confirm that these policies are set up as intended and that enabling
tag-based access control does not create unintentional authorization changes to your Amazon S3
workflows. Doing so will help you ensure that your policies function as intended after ABAC is
enabled on your buckets. For examples of using attribute-based conditions with tags, see [Using tags with S3 general purpose buckets](buckets-tagging.md "buckets-tagging.md").

### Including the required permissions in your IAM policies

You need the following Amazon S3 permissions to enable ABAC for your bucket:

- `s3:PutBucketAbac` – Update the ABAC status for your general purpose bucket.
- `s3:GetBucketAbac` – View the ABAC status for your general purpose bucket

After you enable ABAC, the permissions you previously used to add tags to a bucket or delete
tags from a bucket, `PutBucketTagging` or `DeleteBucketTagging`, will
no longer work. Instead, use the `TagResource` and
_UntagResource_ APIs to perform these tasks.

We recommend you use `TagResource` and `UntagResource` APIs to
manage tagging before enabling ABAC on your buckets. The Amazon S3 Console and CloudFormation now use the
`TagResource` and `UntagResource` APIs by default. You can also
disable ABAC on your bucket by using the `PutBucketAbac` API. You can use
`GetBucketTagging` to list tags on your buckets. This API will continue to work
after you enable ABAC for your buckets. Alternatively you can also use
`ListTagsForResource` to list all tags on your buckets.

You will need the following permissions to apply tags to and remove them from general purpose buckets.

- `s3:TagResource` - Add tags to an AWS resource, such as an Amazon S3 general purpose bucket.
- `s3:UntagResource` - Remove tags from an AWS resource, such as an Amazon S3 general purpose bucket.
- `s3:ListTagsForResource` - View the tags applied to an AWS resource, such as an Amazon S3 general purpose bucket.

The following IAM policy grants the permission to enable ABAC and view its status for your bucket.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutBucketAbac",
        "s3:GetBucketAbac"
      ],
      "Resource": "arn:aws:s3:::my-s3-bucket/*"
    }
  ]
}
```

For more information on tagging general purpose buckets and example ABAC policies for general purpose buckets, see [Using tags with S3 general purpose buckets](buckets-tagging.md "buckets-tagging.md").

### Steps

If you have `s3:PutBucketAbac` permission for a general purpose bucket, you can enable ABAC for the bucket by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To enable ABAC for a general purpose bucket using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **buckets**.
3. Choose the bucket name.
4. Choose the **Properties** tab.
5. In the **Bucket ABAC** panel, and choose **Edit**.
6. Choose the **Enable** toggle.
7. Review and acknowledge the permissions you will need to manage tags after you enable ABAC: `TagResource`, `UntagResource`, and `ListTagsForResource`.
8. Choose **Save changes**.

SDK for Java 2.x
This example shows you how to add enable ABAC for a general purpose bucket by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information.

```
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.AbacStatus;
import software.amazon.awssdk.services.s3.model.GetBucketAbacRequest;
import software.amazon.awssdk.services.s3.model.GetBucketAbacResponse;
import software.amazon.awssdk.services.s3.model.PutBucketAbacRequest;
import software.amazon.awssdk.services.s3.model.PutBucketAbacResponse;
import software.amazon.awssdk.regions.Region;

public class BucketAbac {
    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        S3Client s3 = S3Client.builder()
            .region(region)
            .build();

        putBucketAbac(s3, "amzn-s3-demo-bucket", "Enabled");
        getBucketAbac(s3, "amzn-s3-demo-bucket");

        putBucketAbac(s3, "amzn-s3-demo-bucket", "Disabled");
        getBucketAbac(s3, "amzn-s3-demo-bucket");
    }

    /**
     * Sets the ABAC (Attribute-Based Access Control) status for a specified S3 bucket.
     *
     * @param s3 The S3Client instance to use for the API call
     * @param bucketName The name of the S3 bucket to update
     * @param status The desired ABAC status ("Enabled" or "Disabled")
    */
    public static void putBucketAbac(S3Client s3, String bucketName, String status) {
       try {
            AbacStatus abacStatus = AbacStatus.builder()
                .abacStatus(status)
                .build();
            PutBucketAbacReqquest request = PutBucketAbacRequest.builder()
                .bucket(bucketName)
                .abacStatus(abacStatus)
                .build();
            s3.putBucketAbac(request);
        } catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }

    /**
     * Retrieves the current ABAC (Attribute-Based Access Control) status for a specified S3 bucket.
     *
     * @param s3 The S3Client instance to use for the API call
     * @param bucketName The name of the S3 bucket to query
    */
    public static void getBucketAbac(S3Client s3, String bucketName) {
       try {
            GetBucketAbacReqquest request = GetBucketAbacRequest.builder()
                .bucket(bucketName)
                .build();
            GetBucketAbacResponse response = s3.getBucketAbac(request);
        } catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}

```

This example shows you how to add enable ABAC for a general purpose bucket by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information.

For information about the Amazon S3 REST API support for adding tags to a general purpose bucket, see the following section in the _Amazon Simple Storage Service API Reference_:

- [PutBucketAbac](../API/API_control_PutBucketABAC.md "../API/API_control_PutBucketABAC.md")

To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to enable ABAC for a general purpose bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

**Request:**

```
# Enable ABAC on a general purpose bucket

aws s3api put-bucket-abac --bucket amzn-s3-demo-bucket --abac-status Status=Enabled --region us-east-2

# Disable ABAC on a general purpose bucket

aws s3api put-bucket-abac --bucket amzn-s3-demo-bucket --abac-status Status=Disabled --region us-east-2

# Get ABAC status on a general purpose bucket

aws s3api get-bucket-abac --bucket amzn-s3-demo-bucket --region us-east-2

```
