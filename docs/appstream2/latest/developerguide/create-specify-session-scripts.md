

# Create and Specify Session Scripts
<a name="create-specify-session-scripts"></a>

You can configure and specify session scripts for Always-on, On-demand, and Elastic fleets.

**To configure and specify session scripts for Always-on and On-demand fleets**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the navigation pane, choose **Images**, **Image Builder**.

1. Choose an image builder that is in the **Running** state, and choose **Connect**.

1. When prompted, choose **Administrator**.

1. Navigate to `C:\AppStream\SessionScripts`, and open the `config.json` configuration file.

   For information about session script parameters, see [Session Scripts Configuration File](session-script-configuration-file.md).

1. After you finish making your changes, save and close the `config.json` file.

1. On the image builder desktop, open **Image Assistant**.

1. (Optional) Specify any additional applications that you want to include in the image.

1. Follow the necessary steps in Image Assistant to finish creating your image.

   If the session scripts configuration can't be validated (for example, if the .json file is not correctly formatted), you are notified when you choose **Disconnect and create image**. 
**Note**  
To locate the session scripts configuration file for Linux-based image builders, navigate to `/opt/appstream/SessionScripts/config.json`.

**To configure and specify session scripts for Elastic fleets**

1. Create a zip file that contains the session scripts and config.json file. The scripts files will be copied to the following locations. You must use these locations for your config.json. 
   + For Windows, use `C:\AppStream\SessionScripts\{{SessionScript}}`.
   + For Linux, use `/opt/appstream/SessionScripts/{{SessionScript}}`.
**Note**  
In order to run the session script files, make sure that the .zip file only contains the session scripts and `config.json` files, and not the containing folder. For more information, see [Session Scripts Configuration File](session-script-configuration-file.md).

1. Upload the zip file to an Amazon S3 bucket in your account.
**Note**  
Your VPC must provide access to the Amazon S3 bucket. For more information, see [Using Amazon S3 VPC Endpoints for WorkSpaces Applications Features](managing-network-vpce-iam-policy.md).  
You must have your S3 bucket and WorkSpaces Applications fleet in the same AWS Region.  
You must have IAM permissions to perform the `S3:GetObject` action on the session scripts object in the Amazon S3 bucket. To learn more about storing the session scripts in an Amazon S3 bucket, see [Store Application Icon, Setup Script, Session Script, and VHD in an S3 Bucket](store-s3-bucket.md).

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the navigation pane, choose **Fleets**.

1. Choose an Elastic fleet that you want to update, and then choose **View Details**.

1. On the **Session scripts settings** tab, choose **Edit**.

1. For **Session scripts object in S3**, either enter the S3 URI that represents the session scripts object, or choose **Browse S3** to navigate to your S3 buckets and find the session scripts object.

1. After you finish making your changes, choose **Save Changes**.

1. At this point, session scripts are available for all fleet instances launched.
**Note**  
You can also configure the session scripts when you create a new Elastic fleet. 