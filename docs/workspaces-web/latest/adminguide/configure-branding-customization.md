# Configuring branding customization for your portal

## How it works

When you configure branding customization:

- Visual and text elements are applied to both the sign-in screen and loading screen.
- The browser tab displays your custom favicon and title.
- End users will see your customization changes when starting a new session. In some cases, it may take a few minutes before your changes are visible.
- If terms of service is configured, end users must accept your terms of service before starting their streaming session. Note that they will be asked at the beginning of every session.

## Prerequisites

Before you begin:

- Ensure you have the necessary permissions to modify portal settings, see [AWS managed policies for WorkSpaces Secure Browser](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
- Prepare your branding assets (logo, favicon, wallpaper) according to the specifications in [Customization guidelines](customization-guideline.md "customization-guideline.md").

## Getting started

To configure branding customization, follow these steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/ "https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/").
2. Choose **WorkSpaces Secure Browser**, **Web portals**, and choose your web portal.
3. Select your portal and choose the **User settings** tab.
4. In the **Branding customization** section, choose **Edit**.
5. Configure the following sections as needed:
   - In the **Content editor** - Upload all visual elements (your company logo, your favicon, and an optional wallpaper) and select the color theme. You can upload the files either from your local computer or from an S3 bucket. For information about setting up S3 bucket permissions, see [Setting up S3 bucket permissions](#branding-s3-permissions "#branding-s3-permissions").
   - In the **Text editor** - Customize text that appears on the sign-in screen.
   - In the **Terms of service editor** - Optionally, add terms that users must acknowledge.

6. Choose **Save changes**.

For detailed instructions on each customization option, see [Customization guidelines](customization-guideline.md "customization-guideline.md").

## Setting up S3 bucket permissions

You can upload branding files directly from your computer or select existing objects from your S3 buckets. If you choose to upload the files for the visual elements (your company logo, your favicon, and a wallpaper) from an S3 bucket, make sure that you set up the proper permissions for the S3 bucket.

**Selecting S3 objects in the same account**

If your IAM user or role already has `s3:GetObject` permission for the bucket containing your branding assets, no additional configuration is required.

**Selecting S3 objects in another account**

To select an S3 bucket in a different AWS account, you need to configure both the bucket policy in the source account and the IAM policy in your admin account.

**Example bucket policy (in the source account):**

Apply this policy to the S3 bucket in the source account. Replace `123456789012` with your admin account ID and `source-account-bucket-name` with your actual bucket name.

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCrossAccountAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::`123456789012`:root"
      },
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::`source-account-bucket-name`",
        "arn:aws:s3:::`source-account-bucket-name`/*"
      ]
    }
  ]
}

```

**Example IAM policy (in your admin account):**

Attach this policy to the IAM user or role in your admin account. Replace `source-account-bucket-name` with the actual bucket name from the source account.

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCrossAccountS3Access",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::`source-account-bucket-name`",
        "arn:aws:s3:::`source-account-bucket-name`/*"
      ]
    }
  ]
}

```

For detailed information about cross-account access, see [S3 Access Grants cross-account access](../../../AmazonS3/latest/userguide/access-grants-cross-accounts.md "../../../AmazonS3/latest/userguide/access-grants-cross-accounts.md").
