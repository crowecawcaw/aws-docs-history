# Step 4: Manually upload objects to your S3 Express One Zone

directory bucket

You can also manually upload objects to your directory bucket.

###### To manually upload objects

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the upper right corner of the page, choose the
   name of the currently displayed AWS Region. Next, choose the Region associated
   with the Availability Zone in which your directory bucket is located.
3. In the left navigation pane, choose **Directory buckets**.
4. Choose the name of the bucket that you want to upload your folders or
   files to.

###### Note

If you chose the same directory bucket that you used in previous
steps of this tutorial, your directory bucket will contain the objects that
were uploaded from the Import tool. Notice that these objects are now stored
in the S3 Express One Zone storage class. 5. In the **Objects** list, choose **Upload**. 6. On the **Upload** page, do one of the following:

    * Drag and drop files and folders to the dotted upload area.
    * Choose **Add files** or **Add
     folder**, choose the files or folders to upload, and
     then choose **Open** or
     **Upload**.

7. Under **Checksums**, choose the **Checksum
   function** that you want to use.

###### Note

We recommend using CRC32 and CRC32C for the best performance with the S3 Express One Zone
storage class. For more information, see [S3 additional checksum best practices](s3-express-optimizing-performance-design-patterns.md#s3-express-optimizing--checksums.html "s3-express-optimizing-performance-design-patterns.md#s3-express-optimizing--checksums.html").

(Optional) If you're uploading a single object that's less than 16 MB in
size, you can also specify a pre-calculated checksum value. When you provide a
pre-calculated value, Amazon S3 compares it with the value that it calculates by
using the selected checksum function. If the values don't match, the upload
won't start. 8. The options in the **Permissions** and
**Properties** sections are automatically set to default settings
and can't be modified. Block Public Access is automatically enabled, and S3 Versioning
and S3 Object Lock can't be enabled for directory buckets.

(Optional) If you want to add metadata in key-value pairs to your objects, expand the
**Properties** section, and then in the
**Metadata** section, choose **Add
metadata**. 9. To upload the listed files and folders, choose **Upload**.

Amazon S3 uploads your objects and folders. When the upload is finished, you see a success
message on the **Upload: status** page.

You have successfully created a directory bucket and uploaded objects to your
bucket.
