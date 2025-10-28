# How to set up S3 Object Lock for

immutable call recordings

You can use Amazon S3 Object Lock in combination with your recording bucket to
help prevent call recordings and IVR recordings from being deleted or overwritten for a
fixed amount of time, or indefinitely.

Object Lock adds another layer of protection against object changes and deletion. It
can also help meet regulatory requirements for Write-Once-Read-Many (WORM)
storage.

## Important things to know

- You can enable Amazon S3 Object Lock on new and existing
  buckets.
- You must enable versioning on your call recording bucket.
- After you enable Amazon S3 Object Lock, you cannot remove
  it.
- We recommend using a dedicated call recording bucket because all objects
  will be locked after the default Object Lock retention policy is
  applied.
- Ensure that your retention policy is appropriate for your requirements.
  After the policy is configured, your call recordings will be protected from
  deletion for the duration specified.
- We strongly recommended you thoroughly test the policy in a non-production
  environment before implementing it in production.

## Step 1: Create an S3 bucket with

Object Lock enabled

For a tutorial on creating a new S3 bucket with Object Lock enabled, see [Protect Data on Amazon S3 Against Accidental Deletion or Application
Bugs Using S3 Versioning, S3 Object Lock, and S3 Replication](https://aws.amazon.com/getting-started/hands-on/protect-data-on-amazon-s3/ "https://aws.amazon.com/getting-started/hands-on/protect-data-on-amazon-s3/").

## Step 1A: Enable Object Lock for an

existing Amazon S3 bucket

For information about enabling Object Lock on an existing bucket, see [Enable Object Lock on an existing Amazon S3 bucket](../../../AmazonS3/latest/userguide/object-lock-configure.md#object-lock-configure-existing-bucket "../../../AmazonS3/latest/userguide/object-lock-configure.md#object-lock-configure-existing-bucket"), in the
_Amazon S3 User Guide_.

## Step 2: Configure Amazon Connect to use the S3 bucket for call recordings

1. Open the Amazon Connect console at
   [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. On the instances page, choose the instance alias.

![The Amazon Connect virtual contact center instances page, the instance alias.](images/instance.png) 3. In the navigation pane, choose **Data storage**. 4. In the **Call recordings** section, choose
**Edit**. 5. Choose **Select an existing S3 bucket**, and then in the
**Name** dropdown box choose the bucket that you enable
Object Lock for. 6. Choose **Save**.

## Step 3: Test Object Lock is

enabled

1. Make a test call to your contact center to generate a call
   recording.
2. Log in to Amazon Connect at
   https://`your-instance`.my.connect.aws/home,
   with an Admin account, or an account that has [permissions to search for
   contacts](contact-search.md#required-permissions-search-contacts "contact-search.md#required-permissions-search-contacts").
3. Choose **Analytics and optimization**, **Contact
   search**. Search for your call recording to find the contact
   ID. Copy the contact ID. You're going to use it in the next step to locate
   the call recording in your S3 bucket.
4. Open the Amazon S3 console, select the bucket you created in Step
   1, and follow the path prefix. The path to the call recording includes the
   year, month, and day the recording was made. After you're in the correct
   path prefix, search for the contact ID of the call recording.

![The Amazon S3 console, the search box, the path prefix.](images/s3-objectlock-pathprefix.png) 5. Select the **Show versions** toggle next to the
**Search** box. This option allows you to attempt to
delete the object instead of only applying a delete marker. Applying a
delete marker is the standard behavior when you delete an object from an S3
bucket with versioning enabled. 6. Select the call recording (the box to the left of the recording name), and
then choose **Delete**. In the confirmation box, enter
**permanently delete** and select **Delete
objects**. 7. Review the **Delete objects: status** notification to
confirm that the delete operation has been blocked due to the Object Lock
policy.

![The Amazon S3 console, Delete objects status notification.](images/s3-objectlock-failed.png)
