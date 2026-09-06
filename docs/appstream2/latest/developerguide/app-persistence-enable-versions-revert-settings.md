

# Enable Amazon S3 Object Versioning and Revert a User's Application Settings
<a name="app-persistence-enable-versions-revert-settings"></a>

You can use Amazon S3 object versioning and lifecycle policies to manage your users’ application settings when your users change them. With Amazon S3 object versioning, you can preserve, retrieve, and restore every version of the settings VHD. This enables you to recover from both unintended user actions and application failures. When versioning is enabled, after each streaming session, a new version of the application settings VHD is synced to Amazon S3. The new version does not overwrite the previous version, so if an issue with your users' settings occurs, you can revert to a previous version of the VHD.

**Note**  
Each version of the application settings VHD is saved to Amazon S3 as a separate object and is charged accordingly.

Object versioning is not enabled by default in your S3 bucket, so you must explicitly enable it. 

**To enable object versioning for your application settings VHD**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the **Bucket name **list, choose the S3 bucket that contains the application settings VHD on which to enable object versioning.

1. Choose **Properties**.

1. Choose **Versioning**, **Enable versioning**, and then choose **Save**.

To expire older versions of your application settings VHDs, you can use Amazon S3 lifecycle policies. For information, see [How Do I Create a Lifecycle Policy for an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-lifecycle.html) in the *Amazon Simple Storage Service User Guide*.

**To revert a user's application settings VHD**

You can revert to a previous version of a user's application settings VHD by deleting newer versions of the VHD from the applicable S3 bucket. Do not do this when the user has an active streaming session.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the **Bucket name** list, choose the S3 bucket that contains the user's application settings VHD version to revert to.

1. Locate and select the folder that contains the VHD. For information about how to navigate the S3 bucket folder structure, see *Amazon S3 Bucket Storage* earlier in this topic.

   When you select the folder, the settings VHD and associated metadata file display.

1. To display a list of the VHD and metadata file versions, choose **Show**.

1. Locate the version of the VHD to revert to.

1. In the **Name** list, select the check boxes next to the newer versions of the VHD and associated metadata files, choose **More**, and then choose **Delete**.

1. Verify that the application settings VHD that you want to revert to and the associated metadata file are the newest versions of these files. 

The next time the user streams from a fleet on which application settings persistence is enabled with the applicable settings group, the reverted version of the user's settings displays.