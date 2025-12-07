# Get started with a CloudFront standard distribution

The procedures in this section show you how to use CloudFront to set up a standard distribution that does the following:

- Creates an S3 bucket to use as your distribution origin.
- Stores the original versions of your objects in an Amazon Simple Storage Service (Amazon S3)
  bucket.
- Uses origin access control (OAC) to send authenticated requests to your Amazon S3 origin. OAC sends requests through CloudFront to prevent viewers from accessing your S3 bucket directly. For more information about OAC, see [Restrict access to an Amazon S3
  origin](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md").
- Uses the CloudFront domain name in URLs for your objects (for example,
  `https://d111111abcdef8.cloudfront.net/index.html`).
- Keeps your objects in CloudFront edge locations for the default duration of 24 hours
  (the minimum duration is 0 seconds).
  Most of this is configured automatically for you when you create a CloudFront distribution.

###### Topics

- [Prerequisites](#GettingStartedSignup "#GettingStartedSignup")
- [Create an Amazon S3 bucket](#GettingStartedCreateBucket "#GettingStartedCreateBucket")
- [Upload the content to the
  bucket](#GettingStartedUploadContent "#GettingStartedUploadContent")
- [Create a CloudFront
  distribution that uses an Amazon S3 origin with OAC](#GettingStartedCreateDistribution "#GettingStartedCreateDistribution")
- [Access your content
  through CloudFront](#GettingStartedAccessingDistributions "#GettingStartedAccessingDistributions")
- [Clean up](#GettingStartedDistributionCleanup "#GettingStartedDistributionCleanup")
- [Enhance your basic distribution](#GettingStartedDistributionNotes "#GettingStartedDistributionNotes")

## Prerequisites

Before you begin, make sure that you’ve completed the steps in [Set up your AWS account](setting-up-cloudfront.md "setting-up-cloudfront.md").

## Create an Amazon S3 bucket

An Amazon S3 bucket is a container for files (objects) or folders. CloudFront can distribute
almost any type of file for you when an S3 bucket is the source. For example, CloudFront
can distribute text, images, and videos. There is no maximum for the amount of data
that you can store on Amazon S3.

For this tutorial, you create an S3 bucket with the provided sample
`hello world` files that you will use to create a basic
webpage.

**To create a bucket**

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. We recommend that you use our Hello World sample for this Getting started.
   Download the _hello world_ webpage: [hello-world-html.zip](samples/hello-world-html.md "samples/hello-world-html.md"). Unzip
   it and save the `css` folder and
   `index` file in a convenient location, such as the
   desktop where you are running your browser.
3. Choose **Create bucket**.
4. Enter a unique **Bucket name** that conforms to the
   [General purpose buckets naming rules](../../../AmazonS3/latest/userguide/bucketnamingrules.md#general-purpose-bucket-names "../../../AmazonS3/latest/userguide/bucketnamingrules.md#general-purpose-bucket-names") in the
   _Amazon Simple Storage Service User Guide_.
5. For **Region**, we recommend choosing an AWS Region
   that is geographically close to you. (This reduces latency and
   costs.)
   - Choosing a different Region works, too. You might do this to
     address regulatory requirements, for example.

6. Leave all other settings at their defaults, and then choose
   **Create bucket**.

## Upload the content to the

bucket

After you create your Amazon S3 bucket, upload the contents of the unzipped `hello world` file to it. (You downloaded and unzipped this file in [Create an Amazon S3 bucket](#GettingStartedCreateBucket "#GettingStartedCreateBucket").)

###### To upload the content to Amazon S3

1. In the **General purpose buckets** section, choose the name of your new bucket.
2. Choose **Upload**.
3. On the **Upload** page, drag the `css` folder and `index` file into the drop area.
4. Leave all other settings at their defaults, and then choose
   **Upload**.

## Create a CloudFront

distribution that uses an Amazon S3 origin with OAC

For this tutorial, you will create a CloudFront distribution that uses an Amazon S3 origin with origin access control (OAC). OAC helps you securely send authenticated requests to your Amazon S3 origin. For more information about OAC, see [Restrict access to an Amazon S3
origin](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md").

###### To create a CloudFront

distribution with an Amazon S3 origin that uses OAC

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose **Create distribution**.
3. Enter a **Distribution name** for the
   standard distribution. The name will appear as the value for the
   `Name` key as a tag. You can change this value later.
   You can add up to 50 tags for your standard distribution. For more
   information, see [Tag a distribution](tagging.md "tagging.md").
4. Choose **Single website or app**, **Next**.
5. Choose **Next**.
6. For **Origin type** page, select the
   **Amazon S3**.
7. For **S3 origin**, choose **Browse S3** and select the S3 bucket that you created for this tutorial.
8. For **Settings**, choose **Use recommended origin settings**. CloudFront will use the default
   recommended cache and origin settings for your Amazon S3 origin, including setting up Origin Access Control (OAC). For more information about the recommended settings,
   see [Preconfigured distribution settings reference](template-preconfigured-origin-settings.md "template-preconfigured-origin-settings.md").
9. Choose **Next**.
10. On the **Enable security protections** page, choose whether to
    enable AWS WAF security protections.
11. Choose **Next**.
12. Choose **Create distribution**. CloudFront updates the S3 bucket policy for you.
13. Review the **Details**
    section for your new distribution. When your distribution is done deploying,
    the **Last modified** field changes from
    **Deploying** to a date and time.
14. Record the domain name that CloudFront assigns to your distribution. It looks
    similar to the following: `d111111abcdef8.cloudfront.net`.

Before using the distribution and S3 bucket from this tutorial in a production
environment, make sure to configure it to meet your specific needs. For information
about configuring access in a production environment, see [Configure secure access and restrict access to
content](SecurityAndPrivateContent.md "SecurityAndPrivateContent.md").

## Access your content

through CloudFront

To access your content through CloudFront, combine the domain name for your CloudFront
distribution with the main page for your content. (You recorded your distribution domain name in [Create a CloudFront
distribution that uses an Amazon S3 origin with OAC](#GettingStartedCreateDistribution "#GettingStartedCreateDistribution").)

- Your distribution domain name might look like this:
  `d111111abcdef8.cloudfront.net`.
- The path to the main page of a website is typically
  `/index.html`.

Therefore, the URL to access your content through CloudFront might look like
this:

`https://d111111abcdef8.cloudfront.net/index.html`.

If you followed the previous steps and used the _hello world_ webpage, you should see a webpage that says **Hello world!**.

When you upload more content to this S3 bucket, you can access the content through
CloudFront by combining the CloudFront distribution domain name with the path to the object in
the S3 bucket. For example, if you upload a new file named
`new-page.html` to the root of your S3 bucket, the URL looks
like this:

`https://d111111abcdef8.cloudfront.net/new-page.html`.

## Clean up

If you created your distribution and S3 bucket only as a learning exercise, delete
them so that you no longer accrue charges. Delete the distribution first. For more
information, see the following links:

- [Delete a distribution](HowToDeleteDistribution.md "HowToDeleteDistribution.md")
- [Deleting a
  bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md")

## Enhance your basic distribution

This Get started tutorial provides a minimal framework for creating a distribution. We
recommend that you explore the following enhancements:

- You can use the CloudFront private content feature to restrict access to the
  content in the Amazon S3 buckets. For more information about distributing private
  content, see [Serve private content with signed URLs and signed
  cookies](PrivateContent.md "PrivateContent.md").
- You can configure your CloudFront distribution to use a custom domain name (for
  example, `www.example.com` instead of
  `d111111abcdef8.cloudfront.net`). For more information, see [Use custom URLs](CNAMEs.md "CNAMEs.md").
- This tutorial uses an Amazon S3 origin with origin access control (OAC). However, you can't use OAC if your origin is an S3 bucket configured as a [website endpoint](../../../AmazonS3/latest/userguide/WebsiteEndpoints.md "../../../AmazonS3/latest/userguide/WebsiteEndpoints.md"). If that's the case, you must set up your bucket with CloudFront as a custom origin. For more information, see [Use an Amazon S3 bucket that's
  configured as a website endpoint](DownloadDistS3AndCustomOrigins.md#concept_S3Origin_website "DownloadDistS3AndCustomOrigins.md#concept_S3Origin_website"). For more information about OAC, see [Restrict access to an Amazon S3
  origin](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md").
