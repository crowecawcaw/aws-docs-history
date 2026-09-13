

# Host a static site using a Lightsail bucket and distribution
<a name="amazon-lightsail-static-site-hosting-tutorial"></a>

## Overview
<a name="static-site-overview"></a>

In this tutorial, you create a static site hosted in an Amazon Lightsail bucket and served globally through a Lightsail distribution.

This setup walks you through configuring a static site with the following features:
+ **Global performance** – Lightsail caches content at edge locations worldwide, reducing latency for visitors.
+ **Security** – With private origin access enabled, your distribution serves private objects from your bucket. You do not need to configure your bucket as **public (read-only)** for your distribution to serve content.
+ **Custom error pages** – Show friendly, branded error pages instead of raw error messages when visitors encounter issues.
+ **Default root object** – Specify which object (for example, `index.html`) Lightsail serves when visitors request the root URL of your site.

## Prerequisites
<a name="static-site-prerequisites"></a>

Before you begin, make sure you have the following:
+ An AWS account. If you don't have one, see [Getting started with your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html).
+ Static site content files, including at least one HTML page to serve as your homepage (commonly named `index.html`).

**Tip**  
You can use an AI assistant of your choice to generate your static site content—including HTML pages, CSS stylesheets, and JavaScript files.

**Contents**
+ [Step 1: Create a Lightsail bucket](#static-site-create-bucket)
+ [Step 2: Upload your website files to the bucket](#static-site-upload-files)
+ [Step 3: Create a distribution with your bucket as the origin](#static-site-create-distribution)
+ [Step 4: Add a custom error response](#static-site-add-error-response)
+ [Step 5: (Optional) Configure a custom domain](#static-site-custom-domain)
+ [Troubleshooting](#static-site-troubleshooting)
+ [Next steps and related resources](#static-site-next-steps)

**Important**  
The resources you create in this tutorial will result in charges to your AWS account. For pricing information, see [Amazon Lightsail pricing](https://aws.amazon.com/lightsail/pricing/).

## Step 1: Create a Lightsail bucket
<a name="static-site-create-bucket"></a>

Create a bucket to store your static site files.

![The Storage page in the Lightsail console with the Create bucket button, the AWS Region and storage plan options, and the bucket name input field.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-static-site-create-bucket.png)


1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Storage**.

1. Choose **Create bucket**.

1. Choose the AWS Region closest to your primary audience.

1. Choose a storage plan.

1. Enter a name for your bucket (for example, **lightsail-static-site**).

1. Choose **Create bucket**.

For more information, see [Create a bucket](amazon-lightsail-creating-buckets.md).

For bucket pricing, see [Amazon Lightsail pricing](https://aws.amazon.com/lightsail/pricing/).

## Step 2: Upload your website files to the bucket
<a name="static-site-upload-files"></a>

Upload your static site files to the bucket you created.

![The Objects tab of the Lightsail bucket management page with the Upload button and a list of uploaded website files.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-static-site-upload-files.png)


1. Choose the **Objects** tab.

1. In the **Object list** area, choose **Upload**, and then select your website files. Alternatively, drag and drop your files directly into the **Object list** area.

1. If your site has subdirectories (for example, `css/`, `js/`, `images/`), drag and drop the entire folder to preserve its structure.

For more information, see [Upload files to a bucket](amazon-lightsail-uploading-files-to-a-bucket.md).

## Step 3: Create a distribution with your bucket as the origin
<a name="static-site-create-distribution"></a>

Create a Lightsail distribution and configure your bucket as its origin.

![The Create distribution page in the Lightsail console with the bucket selected as the origin and the Enable private origin access toggle turned on.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-static-site-create-distribution.png)


1. In the left navigation pane, choose **Networking**.

1. Choose **Create distribution**.

1. In the **Choose your origin** section, select the AWS Region where you created your bucket.

1. Choose your bucket as the origin.

1. Select **Enable private origin access**. With this option turned on, your distribution can serve private objects in your bucket. Your distribution always serves public objects, whether or not private origin access is turned on.  
![The private origin access toggle enabled for the distribution.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-static-site-private-origin-access.png)

1. (Optional) Under **Hosting settings**, enter a **Default root object** (for example, **index.html**). This is the object that your Lightsail distribution serves when a visitor navigates to the root URL of your distribution (for example, `https://abc123.cloudfront.net/`). If you do not specify a default root object, requests to the root URL return an error.

1. Choose a distribution plan.
**Note**  
The USD $2.50 distribution bundle includes 50 GB of outbound data transfer per month. As a rough guide, that's roughly 50,000 page views for a 1 MB page (about 25,000 for a heavier 2 MB page). Your actual reach depends on your page size—lighter pages and returning visitors, whose browsers cache your assets, stretch it further.

1. Enter a name for your distribution.

1. Choose **Create distribution**.

Lightsail creates your distribution after a few moments.

For distribution pricing, see [Amazon Lightsail pricing](https://aws.amazon.com/lightsail/pricing/).

**Note**  
With private origin access enabled, you do not need to change your bucket access permissions. Your bucket can remain set to "All objects are private"—only your distribution has read access.  
Private origin access controls how your distribution reaches your bucket—it does not make your website content private. Any object that your distribution serves is publicly accessible to anyone who has your distribution's URL. Store only content that you intend to publish in a bucket that you use for website hosting. Don't place private or sensitive objects in it.

After your distribution status changes to **Deployed**, your static site is live and accessible.

![The Lightsail distribution page showing the Deployed status and default domain URL.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-static-site-deployed.png)


Navigate to your distribution's management page to find your site's URL. The **Default domain** (for example, `abc123.cloudfront.net`) is the address where your static site is now accessible. Open this URL in your browser to view your site.

## Step 4: Add a custom error response
<a name="static-site-add-error-response"></a>

After you create your distribution, open its management page to add custom error responses. We recommend adding an error response for HTTP error code **403**. This is the most common error that visitors encounter when they request a page that doesn't exist in your bucket.

When you enable private origin access, your bucket returns HTTP 403 (Forbidden) for objects that don't exist, so configure your error response for the 403 error code.

1. In the left navigation pane, choose **Networking**, and then choose the distribution that you created.

1. On the distribution's details tab, locate the **Custom error responses** section and choose **Add error response**.

1. Add an error response for HTTP error code **403**. Specify the response page path to the object that you want to serve (for example, `/404.html`), and set the response code to **404**.  
![The Custom error responses section of the distribution's details tab with an error response added for HTTP error code 403.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-static-site-custom-error-responses.png)

## Step 5: (Optional) Configure a custom domain
<a name="static-site-custom-domain"></a>

To use your own domain (for example, `www.example.com`) instead of the default domain of your distribution:

1. **Create an SSL/TLS certificate** for your domain. For more information, see [Create SSL/TLS certificates for your distribution](amazon-lightsail-create-a-distribution-certificate.md).

1. **Enable custom domains** on your distribution. For more information, see [Enable custom domains for your distribution](amazon-lightsail-enabling-distribution-custom-domains.md).

1. **Add a DNS alias record** pointing your domain to your distribution. For more information, see [Point your domain to a distribution](amazon-lightsail-point-domain-to-distribution.md).

## Troubleshooting
<a name="static-site-troubleshooting"></a>

### My site shows "Access Denied" through the distribution
<a name="static-site-troubleshoot-access-denied"></a>
+ Verify that private origin access is enabled on your distribution.
+ Check that your distribution status is **Deployed** (not **InProgress**).
+ Confirm that the object you specified as the **Default root object** exists in your bucket at the exact path you provided. The object can be in a subfolder, as long as the path to it is correct (for example, `index.html` or `content/index.html`).

### My site still shows old content after uploading new files
<a name="static-site-troubleshoot-old-content"></a>
+ Lightsail distributions cache content at edge locations. Choose **Reset cache** on your distribution management page to clear all cached content. For more information, see [Reset the cache for your distribution](amazon-lightsail-resetting-distribution-cache.md).
+ Alternatively, wait for the cache lifespan (TTL) to expire. The default is 1 day.

### I disabled private origin access but I still see my content
<a name="static-site-troubleshoot-disabled-private-origin-access"></a>

Caching causes this. Your Lightsail distribution caches content at its edge locations, and your web browser also caches content locally. After you change your configuration, both caches can continue to serve the previous content until they are cleared.
+ To clear the distribution cache, choose **Reset cache** on your distribution's management page. You can also adjust how your distribution caches content on the **Caching** tab. For more information, see [Reset the cache for your distribution](amazon-lightsail-resetting-distribution-cache.md).
+ To clear your browser cache, hard refresh the page (press CommandShiftR on macOS, or CtrlShiftR on Windows and Linux).

## Next steps and related resources
<a name="static-site-next-steps"></a>
+ [Enable custom domains for your distribution](amazon-lightsail-enabling-distribution-custom-domains.md) – Use your own domain name with your static site.
+ [Monitor your distribution metrics](amazon-lightsail-viewing-distribution-health-metrics.md) – Track requests, data transfer, and error rates.
+ [Enable object versioning on your bucket](amazon-lightsail-managing-bucket-object-versioning.md) – Protect against accidental overwrites during deployments.
+ [Delete your distribution](amazon-lightsail-deleting-distribution.md) – Remove your distribution when you no longer need it.
+ [Content delivery network distributions](amazon-lightsail-creating-content-delivery-network-distribution.md)
+ [Lightsail object storage](amazon-lightsail-creating-buckets.md)
+ [Amazon Lightsail pricing](https://aws.amazon.com/lightsail/pricing/)