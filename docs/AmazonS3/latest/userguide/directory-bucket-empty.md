# Emptying a directory bucket

You can empty an Amazon S3 directory bucket by using the Amazon S3 console. For more information
 about directory buckets, see [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

Before you empty a directory bucket, note the following:


* When you empty a directory bucket, you delete all the objects, but you keep the
 directory bucket.
* After you empty a directory bucket, the empty action can't be undone.
* Objects that are added to the directory bucket while the empty bucket action is
 in progress might be deleted.
If you also want to delete the bucket, note the following:


* All objects in the directory bucket must be deleted before the bucket itself can
 be deleted.
* In-progress multipart uploads in the directory bucket must be aborted before the
 bucket itself can be deleted.


###### Note

The `s3 rm` command through the AWS Command Line Interface (CLI), the `delete` operation
 through Mountpoint, and the **Empty** bucket option button
 through the AWS Management Console are unable to delete in-progress multipart uploads in a
 directory bucket. To delete these in-progress multipart uploads, use the
 `ListMultipartUploads` operation to list the in-progress
 multipart uploads in the bucket and use the `AbortMultipartUpload`
 operation to abort all the in-progress multipart uploads.
To delete a directory bucket, see [Deleting a directory bucket](directory-bucket-delete.md "directory-bucket-delete.md"). To abort an in-progress multipart upload, see
 [Aborting a multipart upload](abort-mpu.md "abort-mpu.md").

To empty a general purpose bucket, see [Emptying a general purpose bucket](empty-bucket.md "empty-bucket.md").

###### To empty a directory bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Directory buckets**.
3. Choose the option button next to the name of the bucket that you want to empty, and
 then choose **Empty**.
4. On the **Empty bucket** page, confirm that you want to empty the
 bucket by entering `permanently delete` in the text field, and then
 choose **Empty**.
5. Monitor the progress of the bucket emptying process on the **Empty bucket:
 status** page.
