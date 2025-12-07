# Emptying a general purpose bucket

You can empty a general purpose bucket's contents using the Amazon S3 console, AWS SDKs, or AWS Command Line Interface
(AWS CLI). When you empty a general purpose bucket, you delete all the objects, but you keep the bucket. After
you empty a bucket, it cannot be undone. Objects added to the bucket while the empty bucket
action is in progress might be deleted. All objects (including all object versions and
delete markers) in the bucket must be deleted before the bucket itself can be
deleted.

When you empty a general purpose bucket that has S3 Versioning
enabled or suspended, all versions of all the objects in the bucket are deleted. For more
information, see [Working with objects in a
versioning-enabled bucket](manage-objects-versioned-bucket.md "manage-objects-versioned-bucket.md").

While emptying your bucket, we recommend that you also remove all incomplete multipart
uploads. You can use multipart uploads to upload very large objects (up to 50 TB) as a set
of parts for improved throughput and quicker recovery from network issues. In cases where
the multipart upload process doesn't finish, the incomplete parts remain in the bucket (in
an unusable state). These incomplete parts incur storage costs until the upload process is
finished, or until the incomplete parts are removed. For more information, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md").

As a best practice, we recommend configuring lifecycle rules to expire objects and incomplete
multipart uploads that are older than a specific number of days. When you create your
lifecycle rule to expire incomplete multipart uploads, we recommend 7 days as a good
starting point. For more information, see [Setting an S3 Lifecycle configuration on a
bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md").

Lifecycle expiration is an asynchronous process, so the rule might take some days to run
before your bucket is empty. After the first time that Amazon S3 runs the rule, all objects that
are eligible for expiration are marked for deletion. You're no longer charged for those
objects that are marked for deletion. For more information, see [How do I empty
an Amazon S3 bucket using a lifecycle configuration rule?](https://repost.aws/knowledge-center/s3-empty-bucket-lifecycle-rule "https://repost.aws/knowledge-center/s3-empty-bucket-lifecycle-rule").

You can use the Amazon S3 console to empty a general purpose bucket, which deletes all of the objects
in the bucket without deleting the bucket.

###### To empty an S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the bucket list, select the option next to
   the name of the bucket that you want to empty, and then choose
   **Empty**.
4. On the **Empty bucket** page, confirm that you want to
   empty the bucket by entering the bucket name into the text field, and then
   choose **Empty**.
5. Monitor the progress of the bucket emptying process on the **Empty
   bucket: Status** page.
   You can empty a general purpose bucket using the AWS CLI only if the bucket does not have Bucket
   Versioning enabled. If versioning is not enabled, you can use the `rm`
   (remove) AWS CLI command with the `--recursive` parameter to empty the
   bucket (or remove a subset of objects with a specific key name prefix).

The following `rm` command removes objects that have the key name
prefix `doc`, for example, `doc/doc1` and
`doc/doc2`.

```
`$` aws s3 rm s3://bucket-name/doc --recursive
```

Use the following command to remove all objects without specifying a
prefix.

```
`$` aws s3 rm s3://bucket-name --recursive
```

For more information, see [Using
high-level S3 commands with the AWS CLI](../../../cli/latest/userguide/using-s3-commands.md "../../../cli/latest/userguide/using-s3-commands.md") in the _AWS Command Line Interface User Guide_.

###### Note

You can't remove objects from a bucket that has versioning enabled. Amazon S3 adds
a delete marker when you delete an object, which is what this command does. For
more information about S3 Bucket Versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").

You can use the AWS SDKs to empty a general purpose bucket or remove a subset of objects that
have a specific key name prefix.

For an example of how to empty a bucket using AWS SDK for Java, see [Deleting a general purpose bucket](delete-bucket.md "delete-bucket.md"). The code deletes all
objects, regardless of whether the bucket has versioning enabled, and then it
deletes the bucket. To just empty the bucket, make sure that you remove the
statement that deletes the bucket.

For more information about using other AWS SDKs, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").

To empty a large general purpose bucket, we recommend that you
use an S3 Lifecycle configuration rule. Lifecycle expiration is an asynchronous process, so the rule might take some days
to run before the bucket is empty. After the first time that Amazon S3 runs the rule, all objects that are eligible for expiration are marked for deletion. You're no longer charged for those objects that are marked for deletion. For more information, see [How do I empty an Amazon S3 bucket using a lifecycle configuration rule?](https://repost.aws/knowledge-center/s3-empty-bucket-lifecycle-rule "https://repost.aws/knowledge-center/s3-empty-bucket-lifecycle-rule").

If you use a lifecycle configuration to empty your bucket, the configuration
should include [current versions,
non-current versions](versioning-workflows.md "versioning-workflows.md"), [delete markers](DeleteMarker.md "DeleteMarker.md"), and
[incomplete multipart uploads](mpu-abort-incomplete-mpu-lifecycle-config.md "mpu-abort-incomplete-mpu-lifecycle-config.md").

You can add lifecycle configuration rules to expire all objects or a subset of
objects that have a specific key name prefix. For example, to remove all objects in
a bucket, you can set a lifecycle rule to expire objects one day after
creation.

Amazon S3 supports a bucket lifecycle rule that you can use to stop multipart uploads
that don't complete within a specified number of days after being initiated. We
recommend that you configure this lifecycle rule to minimize your storage costs. For
more information, see [Configuring a bucket lifecycle
configuration to delete incomplete multipart uploads](mpu-abort-incomplete-mpu-lifecycle-config.md "mpu-abort-incomplete-mpu-lifecycle-config.md").

For more information about using a lifecycle configuration to empty a bucket, see
[Setting an S3 Lifecycle configuration on a
bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md") and [Expiring objects](lifecycle-expire-general-considerations.md "lifecycle-expire-general-considerations.md").

## Emptying a general purpose bucket with AWS CloudTrail configured

AWS CloudTrail tracks object-level data events in an Amazon S3 general purpose bucket, such as deleting
objects. If you use a general purpose bucket as a destination to log your CloudTrail events and are deleting
objects from that same bucket you may be creating new objects while emptying your
bucket. To prevent this, stop your AWS CloudTrail trails. For more information about stopping
your CloudTrail trails from logging events, see [Turning
off logging for a trail](../../../awscloudtrail/latest/userguide/cloudtrail-delete-trails-console.md "../../../awscloudtrail/latest/userguide/cloudtrail-delete-trails-console.md") in the _AWS CloudTrail User Guide_.

Another alternative to stopping CloudTrail trails from being added to the bucket is to add a
deny `s3:PutObject` statement to your bucket policy. If you want to store new
objects in the bucket at a later time you will need to remove this deny
`s3:PutObject` statement. For more information, see [Object operations](security_iam_service-with-iam.md#using-with-s3-actions-related-to-objects "security_iam_service-with-iam.md#using-with-s3-actions-related-to-objects") and [IAM JSON policy
elements: Effect](../../../IAM/latest/UserGuide/reference_policies_elements_effect.md "../../../IAM/latest/UserGuide/reference_policies_elements_effect.md") in the _IAM User Guide_.
