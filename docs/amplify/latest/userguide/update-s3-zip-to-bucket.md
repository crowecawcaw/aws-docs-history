

# Updating an S3 deployment to use a bucket and prefix instead of a .zip file
<a name="update-s3-zip-to-bucket"></a>

If you already have an existing static website deployed to Amplify Hosting from a .zip file in an Amazon S3 general purpose bucket, you can update the application deployment to use the bucket name and prefix that contain the objects to host. This type of deployment eliminates the need to upload a separate file to your bucket that contains the zipped contents of the build output.

**To migrate a static website from a .zip file to the bucket contents**

1. Sign in to the AWS Management Console and open the Amplify console at [https://console.aws.amazon.com/amplify/](https://console.aws.amazon.com/amplify/).

1. On the **All apps** page, choose the name of the manually deployed app that you want to migrate from using a .zip file to using the application files directly.

1. On the application's **Overview** page, choose **Deploy updates**.

1. On the **Deploy updates** page, for **Method**, choose **Amazon S3**.

1. For the **S3 location of objects to host**, choose **Browse**. Select the bucket to use, then select **Choose prefix**.

1. Choose **Save and deploy**.