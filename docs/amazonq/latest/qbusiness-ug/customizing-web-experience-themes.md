# Customizing visual themes

This topic shows how to customize the visual theme using the Amazon Q Business console and
the AWS CLI.

###### Note

- The console only supports accessing customization artifacts stored in Amazon S3
  but the Amazon Q Business API supports accessing artifacts in both S3 and other
  data sources.
- Your web customization artifacts must be of one of the following supported
  content types.
  - Custom logo and favicons — `image/svg+xml`,
    `image/x-icon`, and `image/png`. Logo
    files must be 1 MB or smaller.
  - Custom fonts — `font/ttf`, `font/otf`,
    `font/woff`, and `font/woff2`.

###### Topics

- [Prerequisites for accessing your customization artifacts stored in Amazon S3](#customizing-web-experience-themes-requirements "#customizing-web-experience-themes-requirements")
- [Using the AWS Management Console](#customizing-visual-themes-using-aws-management-console "#customizing-visual-themes-using-aws-management-console")
- [Using the AWS CLI](#customizing-web-experience-themes-using-aws-cli "#customizing-web-experience-themes-using-aws-cli")

## Prerequisites for accessing your customization artifacts stored in Amazon S3

1.  All S3 URIs for files to read and folders to store must be located in the
    same AWS Region as the application environment of the web experience.
2.  You can use public or private Amazon S3 buckets to save and store your web
    experience customization.
    - ###### Prerequisites for public S3 buckets
      - Ensure all S3 URIs for files to read and folders to store
        are publicly accessible. For managing access to your S3
        files, see [Access Control in Amazon S3](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md").
      - Configure CORS to allow console and web app access to
        resources. For more information, see [Configuring cross-origin resource sharing
        (CORS)](../../../AmazonS3/latest/userguide/enabling-cors-examples.md "../../../AmazonS3/latest/userguide/enabling-cors-examples.md").

    - **Prerequisites for private S3
      buckets**

    To allow Amazon Q Business to access web customization artifacts from
    your private S3 buckets, you must do the following:

        + Disable [access
         control lists (ACLs)](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md"). For more information, see
         [Setting Object Ownership on an
         existing bucket](../../../AmazonS3/latest/userguide/object-ownership-existing-bucket.md "../../../AmazonS3/latest/userguide/object-ownership-existing-bucket.md").
        + If your Amazon S3 bucket is encrypted using AWS KMS Key instead
         of Amazon S3 managed key, a similar resource policy to the sample
         bucket policy below must be added to AWS KMS key.



        JSON





        ```
        `{
         "Version":"2012-10-17",
         "Statement": [{
         "Sid": "PolicyForAmazonQWebAccessForWebExperienceArtifacts",
         "Effect": "Allow",
         "Principal": {
         "Service": "application.qbusiness.amazonaws.com"
         },
         "Action": ["kms:Decrypt"],
         "Resource": ["arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"]
         }]
        }`

        ```
        + Create a bucket policy in your private bucket.

    ###### Note

    The value of "`aws:Referer"` cannot contain
    `"https://"` or end with `"/"`.

    ###### Example policy for giving Amazon Q Business access to your web experience artifacts

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "PolicyForAmazonQWebAccessForWebExperienceArtifacts",
     "Effect": "Allow",
     "Principal": {
     "Service": "application.qbusiness.amazonaws.com"
     },
     "Action": [
     "s3:GetObject"
     ],
     "Resource": [
     "arn:aws:s3:::amzn-s3-demo-bucket/`web-experience-object-key`",
     "arn:aws:s3:::amzn-s3-demo-bucket/`web-experience-object-key-2`"
     ],
     "Condition":{
     "StringLike":{
     "aws:Referer":[
     "`web-experience-domain-without-https`"
     ]
     },
     "Bool": {
     "aws:SecureTransport": "true"
     }
     }
     }
     ]
     }`

    ```

## Using the AWS Management Console

The following procedure shows how to customize visual themes using the
console.

1. Sign in to the AWS Management Console and find the Amazon Q Business
   console.
2. From the Amazon Q Business
   **Applications** page, select _your
   application_, then choose **Customize web
   experience**.
3. In the **Customize web experience** section,
   choose **Customize web experience** from the
   right navigation panel and choose **Theme**.
4. Choose either **Managed theming** (for direct
   input of colors and assets) or **Custom
   theming** (for using your own CSS).
   1. For **Managed theming**:
      - Enter colors for background, and primary title.
      - Provide the S3 URI for the logo file. Logo files must be 1
        MB or smaller.

   2. For **Custom theming**:
      - Enter your CSS snippet in the editor.

5. Enter the S3 URI to store your customization.
6. Choose **Save**.

## Using the AWS CLI

The following code snippet shows how to customize visual themes using the
AWS CLI.

```

aws qbusiness update-web-experience \
--application-id application-id \
--web-experience-id web-experience-id \
--customization-configuration {"customCSSUrl":"custom css url","logoUrl":"logo url","fontUrl":"font url","faviconUrl":"favicon url"}

```
