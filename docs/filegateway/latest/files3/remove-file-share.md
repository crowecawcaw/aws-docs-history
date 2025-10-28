# Delete a file share

If you no longer need a file share, you can delete it from the Storage Gateway console. When
you delete a file share, the gateway is detached from the Amazon S3 bucket that the file
share maps to. However, the S3 bucket and its contents aren't deleted.

If your gateway is uploading data to a S3 bucket when you delete a file share, the
delete process doesn't complete until all the data is uploaded. The file share has
the DELETING status until the data is completely uploaded.

If you don't want to wait for your data to be completely uploaded, see the
**To forcibly delete a file share** procedure later in this
topic.

###### To delete a file share

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **File shares**, then select one or more file shares
   to delete.
3. For **Actions**, choose **Delete file
   share**. The confirmation dialog box appears.
4. Verify that you want to delete the specified file shares, then type the word
   _delete_ in the confirmation box and choose
   **Delete**.
   In certain cases, you might not want to wait until all the data written to files on
   the Network File System (NFS) file share is uploaded before deleting the file share. For
   example, you might want to intentionally discard data that was written but has not yet
   been uploaded, or the Amazon S3 bucket that backs the file share might have already been
   deleted, meaning that uploading the specified data is no longer possible.

In these cases, you can forcibly delete the file share by using the AWS Management Console or the
`DeleteFileShare` API operation. This operation stops the data upload
process. When it does, the file share enters the FORCE_DELETING status. To forcibly
delete a file share using the Storage Gateway console, see the procedure following.

###### To forcibly delete a file share

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. From the **File shares** list page, choose file share that
   you flagged for deletion in the procedure above to view its details. After a few
   seconds, a deletion notification message appears on the
   **Details** tab.
3. In the message that appears on the **Details** tab, verify
   the ID of the file share that you want to forcibly delete, select the
   confirmation box, and choose **Force delete now**.

###### Note

You cannot undo the force delete operation.

When you forcibly delete a file share, pieces of partially-transferred
files from multi-part uploads might remain on Amazon S3 where they can incur
storage charges. We recommend configuring an Amazon S3 bucket lifecycle rule to
delete these file parts automatically. For more information, see [Best practices: managing multipart uploads](best-practices-managing-multi-part-uploads.md "best-practices-managing-multi-part-uploads.md").
You can also use the [DeleteFileShare](../../../storagegateway/latest/APIReference/API_DeleteFileShare.md "../../../storagegateway/latest/APIReference/API_DeleteFileShare.md") API operation to forcibly delete the file share. Deleting a
file share using the API requires the `storagegateway:DeleteFileShare` IAM
policy permission.
