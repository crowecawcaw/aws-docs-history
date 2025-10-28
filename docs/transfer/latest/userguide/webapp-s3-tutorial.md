# Tutorial: Setting up AWS Transfer Family web app with selective

multi-bucket access

This tutorial guides you through configuring a Transfer Family web app with specific Amazon S3 bucket
permissions for a single user. You'll learn how to set up a solution that allows users to
download from one bucket and upload to another while maintaining security. This is an
advanced tutorial that builds on the concepts covered in the basic tutorial. If you're new
to AWS Transfer Family web apps, consider starting with [Tutorial: Setting up a basic Transfer Family web app](web-app-tutorial.md "web-app-tutorial.md").

## Prerequisites

Before you begin this tutorial, you need:

- IAM Identity Center configured in the same region as your AWS Transfer Family web app. Note that AWS
  allows only one instance of IAM Identity Center per AWS account for all Regions.
- At least one user configured in IAM Identity Center.
- Two S3 buckets: one for downloads and one for uploads.

###### Note

This tutorial shares many prerequisites with the basic web app tutorial. For more
information about setting up IAM Identity Center and creating users, see [Tutorial: Setting up a basic Transfer Family web app](web-app-tutorial.md "web-app-tutorial.md").

## Step 1: Create a Transfer Family web app

###### To create a Transfer Family web app

1. Sign in to the AWS Management Console and open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose **Web apps**.
3. Choose **Create web app**.

For authentication access, note that the service automatically finds the
AWS IAM Identity Center instance that you set up as a prerequisite. 4. In the **Permission type** pane, select **Create and
use a new service role**. The service creates the
identity bearer role for you. An identity bearer role includes an authenticated
user's identity in its sessions. 5. In the **Web app units** pane, accept the default value of 1,
or adjust to a higher value if needed. 6. Add a tag to help you organize your web apps. For the tutorial, enter
**Name** for the key and **Tutorial web
app** for the value.

###### Tip

You can edit the web app name directly from the **Web
apps** list page after you create it. 7. Choose **Next** to open the **Design web
app** page. On this screen, provide the following
information.

You can optionally provide a title for your web app. You can also upload image
files for your logo and favicon.

    * For the page title, customize the title for the browser tab that your
     users see when they connect to the web app. If you don't enter anything
     for the page title, it defaults to **Transfer Web
     App**.
    * For the logo, upload an image file. The maximum file size for your
     logo image is 50 KB.
    * For the favicon, upload an image file. The maximum file size for your
     favicon is 20 KB.

8. Choose **Next**, then choose **Create web
   app**.

## Step 2: Configure IAM roles for S3

access

You need to create two IAM roles: one with download-only access to the first bucket
and another with upload-only access to the second bucket.

### Trust policy for both

roles

Use the following trust policy for both IAM roles:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessGrantsTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "access-grants.s3.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetSourceIdentity",
 "sts:SetContext"
 ]
 }
 ]
}`

```

### IAM policy for download

bucket

Create an IAM role with the following policy for read-only access to your
download bucket:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ObjectLevelReadPermissions",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:GetObjectAcl",
 "s3:GetObjectVersionAcl",
 "s3:ListMultipartUploadParts",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "arn:aws:s3:::amzn-s3-demo-bucket1"
 ]
 }
 ]
}`

```

###### Important

Replace **amzn-s3-demo-bucket1** with the actual name of your
download bucket.

### IAM policy for upload

bucket

Create another IAM role with the following policy for write access to your
upload bucket:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ObjectLevelWritePermissions",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl",
 "s3:PutObjectVersionAcl",
 "s3:DeleteObject",
 "s3:DeleteObjectVersion",
 "s3:AbortMultipartUpload",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket2/*",
 "arn:aws:s3:::amzn-s3-demo-bucket2"
 ]
 }
 ]
}`

```

###### Important

Replace **amzn-s3-demo-bucket2** with the actual name of your
upload bucket.

## Step 3: Set up S3 Access

Grants

1. Open the S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Access Grants**.
3. Click **Create S3 Access Grants instance**.
4. Select the option **Add IAM Identity Center instance** and enter the
   identity center instance ARN.
5. Click **Next**, then click **Cancel** to
   finish creating the S3 Access Grants instance without proceeding with additional
   steps.

This step creates the S3 Access Grants instance. You'll now register locations and
create access grants.

## Step 4: Register S3 bucket

locations

Register both S3 buckets as locations with S3 Access Grants:

1. In the S3 Access Grants console, navigate to **Locations**
   and click **Register location**.
2. Under **Location scope**, choose the specific S3 bucket for
   downloads (amzn-s3-demo-bucket1).
3. When prompted to choose an IAM role, select the download IAM role you
   created earlier.
4. Complete the registration process.
5. Repeat the process to register the upload bucket (amzn-s3-demo-bucket2),
   selecting the upload IAM role when prompted.

## Step 5: Create Access Grants

Create two grants, one for each registered location:

1. In the S3 Access Grants console, navigate to **Grants** and
   click **Create grant**.
2. In **Location**, click **Browse location**
   and select the download bucket location (amzn-s3-demo-bucket1).
3. In **Subprefix** (optional), enter `*` to allow
   access to the entire bucket, or specify a path like
   `folder1/folder2/*` to restrict access to a specific
   prefix.

Using `*` will set the grant scope to
`s3://bucket-name/*`, allowing access to the entire bucket. To
allow access to only a specific prefix, enter a path like
`folder1/folder2/*`, which will set the grant scope to
`s3://bucket-name/folder1/folder2/*`. 4. Under **Permissions and access**, select
**Read** for the download bucket. 5. In **Grantee type**, choose **Directory identity from
IAM Identity Center**. 6. For **IAM principal type**, select
**User** and enter the User ID of your IAM Identity Center user. 7. Complete the grant creation process. 8. Repeat the process to create a grant for the upload bucket
(amzn-s3-demo-bucket2), but select **Read-write** for the
permissions.

## Step 6: Configure CORS policy for S3

buckets

Configure a CORS policy for both S3 buckets to allow access through your AWS Transfer Family
WebApp:

1. Open the S3 console and navigate to your download bucket
   (amzn-s3-demo-bucket1).
2. Select the **Permissions** tab.
3. Scroll down to the **Cross-origin resource sharing (CORS)**
   section and click **Edit**.
4. Add the following CORS configuration, replacing
   `WebAppEndpoint` with your actual WebApp endpoint
   URL:

You can find your web app endpoint URL in the AWS Transfer Family console under WebApps.
It will look similar to
**https://webapp-\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.transfer-webapp.us-west-2.on.aws**.

```
[
  {
    "AllowedHeaders": [
      "*"
    ],
    "AllowedMethods": [
      "GET",
      "PUT",
      "POST",
      "DELETE",
      "HEAD"
    ],
    "AllowedOrigins": [
      "https://`WebAppEndpoint`"
    ],
    "ExposeHeaders": [
      "last-modified",
      "content-length",
      "etag",
      "x-amz-version-id",
      "content-type",
      "x-amz-request-id",
      "x-amz-id-2",
      "date",
      "x-amz-cf-id",
      "x-amz-storage-class",
      "access-control-expose-headers"
    ],
    "MaxAgeSeconds": 3000
  }
]
```

5. Click **Save changes**.
6. Repeat the process for your upload bucket (amzn-s3-demo-bucket2).

## Step 7: Test the configuration

1. Open your AWS Transfer Family web app URL. You can find this URL in the AWS Transfer Family console
   under WebApps in the **Access endpoint** field.
2. Log in using the IAM Identity Center user credentials you configured with access
   grants.
3. After logging in, you should see both S3 locations on the home page.
4. Navigate to the download bucket (amzn-s3-demo-bucket1) and verify that you can
   download files but not upload.
5. Navigate to the upload bucket (amzn-s3-demo-bucket2) and verify that you can
   upload files.

## Conclusion

You have successfully configured AWS Transfer Family WebApp with selective S3 bucket access for a
single user. This setup allows the user to download from one bucket and upload to
another while maintaining security through IAM roles and S3 Access Grants.

This approach can be extended to multiple users by creating additional grants in S3
Access Grants for each user, allowing for granular control over bucket access
permissions. For information about the basic web app setup, see [Tutorial: Setting up a basic Transfer Family web app](web-app-tutorial.md "web-app-tutorial.md").
