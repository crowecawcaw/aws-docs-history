# Deploying an application to Amplify without a Git

repository

Manual deployments enable you to publish your web app with Amplify Hosting without
connecting a Git provider. You can drag and drop a zipped folder from your desktop and host
your site in seconds. Alternatively, you can reference assets in an Amazon S3 bucket or specify a
public URL to the location where your files are stored.

###### Note

Manual deployments have a maximum .zip file size limit of 5GB due to Amazon S3 copy
operation constraints. If any of your build artifacts exceed this size, consider breaking
them into smaller archives or using an alternative deployment method.

For Amazon S3, you can also set up AWS Lambda triggers to update your site each time new assets
are uploaded. See the [Deploy files stored on Amazon S3, Dropbox, or your Desktop to the AWS Amplify
console](https://aws.amazon.com/blogs/mobile/deploy-files-s3-dropbox-amplify-console/ "https://aws.amazon.com/blogs/mobile/deploy-files-s3-dropbox-amplify-console/") blog post for more details about setting up this scenario.

Amplify Hosting does not support manual deploys for server-side rendered (SSR) apps. For
more information, see [Deploying server-side rendered applications with
Amplify Hosting](server-side-rendering-amplify.md "server-side-rendering-amplify.md").

## Drag and drop manual deployments

###### To manually deploy an app using drag and drop

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. In the upper right corner, choose **Create new app**.
3. On the **Start building with Amplify** page, choose
   **Deploy without Git**. Then, choose
   **Next**.
4. On the **Start a manual deployment** page, for **App
   name**, enter the name of your app.
5. For **Branch name**, enter a meaningful name, such as
   `development` or `production`.
6. For **Method**, choose **Drag and drop**.
7. Either drag and drop a folder from your desktop onto the drop zone or use
   **Choose .zip folder** to select the file from your computer. The
   file that you drag and drop or select must be a a zipped folder that contains the
   contents of your build output.
8. Choose **Save and deploy**.

## Amazon S3 or URL manual deployment

###### Note

If you are deploying a static website from S3, the following procedure
requires that you upload a zipped folder with the contents of your build output to your
S3 bucket. We recommend that you deploy a static website directly from
S3 using the bucket name and prefix. For more information about this
simplified process, see [Deploying a static website to Amplify from an
Amazon S3 bucket](deploy-website-from-s3.md "deploy-website-from-s3.md").

###### To manually deploy an app from Amazon S3 or a public URL

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. In the upper right corner, choose **Create new app**.
3. On the **Start building with Amplify** page, choose
   **Deploy without Git**. Then, choose
   **Next**.
4. On the **Start a manual deployment** page, for **App
   name**, enter the name of your app.
5. For **Branch name**, enter a meaningful name, such as
   `development` or `production`.
6. For **Method**, choose either **Amazon S3** or
   **Any URL**.
7. The procedure for uploading your files depends on the upload method.
   - Amazon S3
     1. For **S3 location of objects to
        host**, choose **Browse
        S3**. Then, select the name of the Amazon S3 bucket
        from the list. Access control lists (ACLs) must be enabled for the bucket
        you select. For more information, see [Troubleshooting Amazon S3 bucket access
        for manual deployments](#troubleshooting-s3-bucket-access "#troubleshooting-s3-bucket-access").
     2. Select the name of the .zip file to deploy.
     3. Choose **Choose prefix**.

   - Any URL
     1. For **Resource URL**, enter the URL to the .zip file
        to deploy.

8. Choose **Save and deploy**.

###### Note

When you create the zipped folder, make sure you zip the contents of your build
output and not the top level folder. For example, if your build output generates a
folder named “build” or “public”, first navigate into that folder, select all of the
contents, and zip it from there. If you do not do this, you will see an “Access Denied”
error because the site's root directory will not be initialized properly.

### Troubleshooting Amazon S3 bucket access

for manual deployments

When you create an Amazon S3 bucket, you use its Amazon S3 Object Ownership setting to control
whether access control lists (ACLs) are enabled or disabled for the bucket. To manually
deploy an app to Amplify from an Amazon S3 bucket, ACLs must be enabled on the
bucket.

If you get an `AccessControlList` error when you deploy from an Amazon S3
bucket, the bucket was created with ACLs disabled and you must enable them in the Amazon S3
console. For instructions, see [Setting Object Ownership on an existing bucket](../../../AmazonS3/latest/userguide/object-ownership-existing-bucket.md "../../../AmazonS3/latest/userguide/object-ownership-existing-bucket.md") in the
_Amazon Simple Storage Service User Guide_.
