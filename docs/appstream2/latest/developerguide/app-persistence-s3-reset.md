# Reset a User's Application

Settings

To reset a user's application settings, you must find and delete the VHD and
associated metadata file from the S3 bucket in your AWS account. Make sure that
you do not do this during a user's active streaming session. After you delete the
user's VHD and the metadata file, the next time the user launches a session from a
streaming instance that has application settings persistence enabled, WorkSpaces Applications creates
a new settings VHD for that user.

###### To reset a user's application settings

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Bucket name** list, choose the S3 bucket that
   contains the application settings VHD that you want to reset.
3. Locate the folder that contains the VHD. For more information about how to
   navigate the S3 bucket folder structure, see _Amazon S3 Bucket
   Storage_ earlier in this topic.
4. In the **Name** list, select the check box next to the
   VHD and the REG, choose **More**, and then choose
   **Delete**.
5. In the **Delete objects** dialog box, verify that the VHD
   and the REG are listed, and then choose **Delete**.
   The next time the user streams from a fleet on which application settings
   persistence is enabled with the applicable settings group, a new application
   settings VHD is created. This VHD is saved to the S3 bucket at the end of the
   session.
