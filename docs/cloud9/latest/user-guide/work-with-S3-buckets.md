AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with Amazon S3 buckets

Every object you store in Amazon S3 resides in a bucket. You can use buckets to group related
objects in the same way that you use a directory to group files in a file system.

###### Topics

- [Creating an Amazon S3 bucket](#creating-s3-bucket "#creating-s3-bucket")
- [Adding a folder to an Amazon S3 bucket](#adding-folders "#adding-folders")
- [Deleting an Amazon S3 bucket](#deleting-s3-buckets "#deleting-s3-buckets")
- [Configuring the display of Amazon S3 items](#configuring-items-display "#configuring-items-display")

## Creating an Amazon S3 bucket

1. In the **AWS Explorer**, open the context (right-click) menu for
   the **S3** node, and then choose **Create Bucket**.
2. In the **Bucket Name** field, enter a valid name for the bucket.
   Press **Enter** to confirm.

The new bucket is displayed under the **S3** node.

###### Note

Because your S3 bucket can be used as a URL that's accessed publicly, the bucket
name that you choose must be globally unique. If some other account has already created
a bucket with the name that you chose, you must use another name.

If you can't create a bucket, you can check the **AWS Toolkit
Logs** in the **Output** tab. For example, if you use a
bucket name already in use, a `BucketAlreadyExists` error occurs. For more
information, see [Bucket restrictions
and limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md") in the _Amazon Simple Storage Service User Guide_.

After a bucket is created, you can copy its name and Amazon Resource Name (ARN) to the
clipboard. Open the context (right-click) menu for the bucket entry and select the
relevant option from the menu.

## Adding a folder to an Amazon S3 bucket

You organize a bucket's contents by grouping objects in folders. You can also create
folders within other folders.

1. In the **AWS Explorer**, choose the **S3** node
   to view the list of buckets.
2. Open the context (right-click) menu for a bucket or a folder, and then choose
   **Create Folder**.
3. Enter a **Folder Name**, and then press **Enter**.

The new folder is now displayed below the selected bucket and folder in the
**AWS Explorer** window.

## Deleting an Amazon S3 bucket

When you delete a bucket, you also delete the folders and objects that it contains. Before
the bucket is deleted, you're asked to confirm that you want to do this.

###### Note

[To delete only a folder](../../../AmazonS3/latest/userguide/delete-folders.md "../../../AmazonS3/latest/userguide/delete-folders.md"), not the
entire bucket, use the AWS Management Console.

1. In the **AWS Explorer**, choose the **S3** node to
   expand the list of buckets.
2. Open the context menu for the bucket to delete, and then choose **Delete**.
3. Enter the bucket's name to confirm that you want to delete it, and then press
   **Enter**.

###### Note

If the bucket contains objects, the bucket is emptied before you delete it. This can
take some time if it's necessary to delete every version of thousands of objects. A
notification is displayed after the delete process is complete.

## Configuring the display of Amazon S3 items

If you're working with a large number of Amazon S3 objects or folders, it's helpful to specify
how many are displayed at one time. When the maximum number is displayed, you can choose
**Load More** to display the next batch.

1. On the menu bar, choose **AWS Cloud9**, **Preferences**.
2. In the **Preferences** window, expand **Project
   Settings**, and go to the **EXTENSIONS** section to choose
   **AWS Configuration**.
3. In the **AWS Configuration** pane, go to the **AWS > S3: Max
   Items Per Page** setting.
4. Before choosing to load more, change the default value to the number of S3 items that
   you want displayed.

###### Note

The range of accepted values is between 3 and 1000. This setting applies only to the
number of objects or folders displayed at one time. All the buckets that you created are
displayed at once. By default, you can create up to 100 buckets in each of your
AWS accounts.
