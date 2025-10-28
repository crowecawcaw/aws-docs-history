# Tutorial: Hosting on-demand

streaming video with Amazon S3, Amazon CloudFront, and Amazon Route 53

You can use Amazon S3 with Amazon CloudFront to host videos for on-demand viewing in a secure and
scalable way. Video on demand (VOD) streaming means that your video content is stored on a
server and viewers can watch it at any time.

CloudFront is a fast, highly secure, and programmable content delivery network (CDN) service.
CloudFront can deliver your content securely over HTTPS from all of the CloudFront edge locations around
the globe. For more information about CloudFront, see [What is Amazon CloudFront?](../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md "../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md")
in the _Amazon CloudFront Developer Guide_.

CloudFront caching reduces the number of requests that your origin server must respond to
directly. When a viewer
(end
user) requests a video that you serve with
CloudFront, the request is routed to a nearby edge location closer to where the viewer is located.
CloudFront serves the video from its cache, retrieving it from the S3 bucket only if it is not
already cached. This caching management feature accelerates the delivery of your video to
viewers globally with low latency, high throughput, and high transfer speeds. For more
information about CloudFront caching management, see [Optimizing caching
and availability](../../../AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.md "../../../AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.md") in the _Amazon CloudFront Developer Guide_.

![Diagram showing how the CloudFront caching mechanism works.](images/cf-example-image-global.png)

###### Objective

In this tutorial, you configure an S3 bucket to host on-demand video streaming using
CloudFront for delivery and Amazon Route 53 for Domain Name System (DNS) and custom domain
management.

###### Topics

- [Prerequisites: Register and configure a custom
  domain with Route 53](#cf-s3-prerequisites "#cf-s3-prerequisites")
- [Step 1: Create an S3 bucket](#cf-s3-step1 "#cf-s3-step1")
- [Step 2: Upload a video to the S3 bucket](#cf-s3-step2 "#cf-s3-step2")
- [Step 3: Create a CloudFront origin access identity](#cf-s3-step3 "#cf-s3-step3")
- [Step 4: Create a CloudFront
  distribution](#cf-s3-step4 "#cf-s3-step4")
- [Step 5: Access the video through the CloudFront
  distribution](#cf-s3-step5 "#cf-s3-step5")
- [Step 6: Configure your CloudFront distribution to use your
  custom domain name](#cf-s3-step6 "#cf-s3-step6")
- [Step 7: Access the S3 video through
  the CloudFront distribution with the custom domain name](#cf-s3-step7 "#cf-s3-step7")
- [(Optional) Step 8: View data about
  requests received by your CloudFront distribution](#cf-s3-step8 "#cf-s3-step8")
- [Step 9: Clean up](#cf-s3-step9 "#cf-s3-step9")
- [Next steps](#cf-s3-next-steps "#cf-s3-next-steps")

## Prerequisites: Register and configure a custom

domain with Route 53

Before you start this tutorial, you must register and configure a custom domain (for
example, `example.com`) with Route 53 so that you can configure your
CloudFront distribution to use a custom domain name later.

Without a custom domain name, your S3 video is publicly accessible and hosted through
CloudFront at a URL that looks similar to the following:

```
https://`CloudFront distribution domain name`/`Path to an S3 video`
```

For example,
`https://d111111abcdef8.cloudfront.net/sample.mp4`.

After you configure your CloudFront distribution to use a custom domain name configured with
Route 53, your S3 video is publicly accessible and hosted through CloudFront at a URL that looks
similar to the following:

```
https://`CloudFront distribution alternate domain name`/`Path to an S3 video`
```

For example, `https://www.example.com/sample.mp4`. A custom
domain name is simpler and more intuitive for your viewers to use.

######

To register a custom domain, see [Registering a new
domain using Route 53](../../../Route53/latest/DeveloperGuide/domain-register.md "../../../Route53/latest/DeveloperGuide/domain-register.md") in the _Amazon Route 53 Developer
Guide_.

When you register a domain name with Route 53, Route 53 creates the hosted zone for you,
which you will use later in this tutorial. This hosted zone is where you store
information about how to route traffic for your domain, for example, to an Amazon EC2
instance or a CloudFront distribution.

There are fees associated with domain registration, your hosted zone, and DNS queries
received by your domain. For more information, see [Amazon Route 53 Pricing](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").

###### Note

When you register a domain, it costs money immediately and it's irreversible. You
can choose not to auto-renew the domain, but you pay up front and own it for the
year. For more information, see [Registering a new
domain](../../../Route53/latest/DeveloperGuide/domain-register.md "../../../Route53/latest/DeveloperGuide/domain-register.md") in the _Amazon Route 53 Developer
Guide_.

## Step 1: Create an S3 bucket

Create a bucket to store the original video that you plan to stream.

###### To create a bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region in which you want to create a bucket.

###### Note

To minimize latency and costs and address regulatory requirements, choose a Region
close to you. Objects stored in a Region never leave that Region unless you explicitly
transfer them to another Region. For a list of Amazon S3 AWS Regions, see [AWS service endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the
_Amazon Web Services General Reference_. 3. In the left navigation pane, choose **General purpose buckets**. 4. Choose **Create bucket**. The **Create bucket** page opens. 5. For **Bucket name**, enter a name for your bucket (for
example, `tutorial-bucket`).

For more information about naming buckets in Amazon S3, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md"). 6. For **Region**, choose the AWS Region where you want the
bucket to reside.

If possible, you should pick the Region that is closest to the majority of
your viewers. For more information about the bucket Region, see [General purpose buckets overview](UsingBucket.md "UsingBucket.md"). 7. For **Block Public Access settings for this bucket**, keep
the default settings (**Block _all_ public access** is enabled).

Even with **Block _all_ public
access** enabled, viewers can still access the uploaded video
through CloudFront. This feature is a major advantage of using CloudFront to host a video
stored in S3.

We recommend that you keep all settings enabled unless you
need to turn off one or more of them for your use case. For
more information about blocking public access, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md"). 8. For the remaining settings, keep the defaults.

(Optional) If you want to configure additional bucket settings for your
specific use case, see [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md"). 9. Choose **Create bucket**.

## Step 2: Upload a video to the S3 bucket

The following procedure describes how to upload a video file to an S3 bucket by using
the console. If you're uploading many large video files to S3, you might want to use
[Amazon S3 Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration "https://aws.amazon.com/s3/transfer-acceleration")
to configure fast and secure file transfers. Transfer Acceleration can speed up video
uploading to your S3 bucket for long-distance transfer of larger videos. For more
information, see [Configuring fast, secure file transfers using
Amazon S3 Transfer Acceleration](transfer-acceleration.md "transfer-acceleration.md").

###### To upload a file to the bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the **General purpose buckets** list, choose the name of the bucket that
   you created in [Step 1](#cf-s3-step1 "#cf-s3-step1") (for example,
   `tutorial-bucket`) to upload your file to.
4. On the **Objects** tab for your bucket,
   choose **Upload**.
5. On the **Upload** page, under **Files and
   folders**, choose **Add files**.
6. Choose a file to upload, and then choose
   **Open**.

For example, you can upload a video file named
`sample.mp4`. 7. Choose **Upload**.

## Step 3: Create a CloudFront origin access identity

To restrict direct access to the video from your S3 bucket, create a special CloudFront user called an
origin access identity (OAI). You will associate the OAI with your distribution later in this tutorial.
By using an OAI, you make sure that viewers can't bypass CloudFront and get the video directly from the S3
bucket. Only the CloudFront OAI can access the file in the S3 bucket. For more information, see [Restrict
access to an Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the _Amazon CloudFront Developer Guide_.

###### Important

If the bucket that you're using to host your static website has been encrypted using server-side
encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you must use origin access control (OAC) instead of
origin access identity (OAI) to secure the origin. OAI doesn't support SSE-KMS, so you must use OAC
instead. For more information about OAC, see [Restrict
access to an Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the _Amazon CloudFront Developer Guide_.

###### To create a CloudFront OAI

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, under the **Security** section,
   choose **Origin access**.
3. Under the **Identities** tab, choose **Create origin access
   identity**.
4. Enter a name (for example, `S3-OAI`) for the new origin
   access identity.
5. Choose **Create**.

## Step 4: Create a CloudFront

distribution

To use CloudFront to serve and distribute the video in your S3 bucket, you must create a
CloudFront distribution.

###### Substeps

- [Create a CloudFront
  distribution](#cf-s3-step4-create-cloudfront "#cf-s3-step4-create-cloudfront")
- [Review the
  bucket policy](#cf-s3-step4-review-bucket-policy "#cf-s3-step4-review-bucket-policy")

### Create a CloudFront

distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, choose
   **Distributions**.
3. Choose **Create
   distribution**.
4. In the **Origin** section, for **Origin
   domain**, choose the domain name of your S3 origin, which
   starts with the name of the S3 bucket that you created in [Step 1](#cf-s3-step1 "#cf-s3-step1") (for example,
   `tutorial-bucket`).
5. For **Origin access**, choose
   **Legacy access identities**.
6. Under **Origin access identity**, choose the origin
   access identity that you created in [Step
   3](#cf-s3-step3 "#cf-s3-step3") (for example, `S3-OAI`).
7. Under **Bucket policy**, choose
   **Yes, update the bucket policy**.
8. In the **Default cache behavior** section, under
   **Viewer protocol policy**, choose **Redirect
   HTTP to HTTPS**.

When you choose this feature, HTTP requests are automatically redirected
to HTTPS to secure your website and protect your viewers' data. 9. For the other settings in the **Default cache behaviors**
section, keep the default values.

(Optional) You can control how long your file stays in a CloudFront cache before
CloudFront forwards another request to your origin. Reducing the duration allows
you to serve dynamic content. Increasing the duration means that your
viewers get better performance because your files are more likely to be
served directly from the edge cache. A longer duration also reduces the load
on your origin. For more information, see [Managing
how long content stays in the cache (expiration)](../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md "../../../AmazonCloudFront/latest/DeveloperGuide/Expiration.md") in the
_Amazon CloudFront Developer Guide_. 10. For the other sections, keep the remaining settings set to the defaults.

For more information about the different settings options, see [Values That You Specify When You Create or Update a
Distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md") in the _Amazon CloudFront Developer
Guide_. 11. At the bottom of the page, choose **Create
distribution**. 12. On the **General** tab for your CloudFront distribution, under
**Details**, the value of the **Last
modified** column for your distribution changes from
**Deploying** to the timestamp when the distribution
was last modified. This process typically takes a few minutes.

### Review the

bucket policy

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the name of the bucket
   that you used earlier as the origin of your CloudFront distribution (for example,
   `tutorial-bucket`).
4. Choose the **Permissions** tab.
5. In the **Bucket policy** section, confirm that you see a
   statement similar to the following in the bucket policy text:

```
{
    "Version": "2008-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Sid": "1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity `EH1HDMB1FH2TC`"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::`tutorial-bucket`/*"
        }
    ]
}
```

This is the statement that your CloudFront distribution added to your bucket
policy when you chose **Yes, update the bucket policy**
earlier.

This bucket policy update indicates that you successfully configured the
CloudFront distribution to restrict access to the S3 bucket. Because of this
restriction, objects in the bucket can be accessed only through your CloudFront
distribution.

## Step 5: Access the video through the CloudFront

distribution

Now, CloudFront can serve the video stored in your S3 bucket. To access your video through
CloudFront, you must combine your CloudFront distribution domain name with the path to the video in
the S3 bucket.

###### To create a URL to the S3 video using the CloudFront distribution

domain name

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, choose **Distributions**.
3. To get the distribution domain name, do the
   following:
   1. In the **Origins** column, find the correct CloudFront
      distribution by looking for its origin name, which starts with the S3
      bucket that you created in [Step 1](#cf-s3-step1 "#cf-s3-step1")
      (for example, `tutorial-bucket`).
   2. After finding the distribution in the list, widen the **Domain
      name** column to copy the domain name value for your CloudFront
      distribution.

4. In a new browser tab, paste the distribution domain name that you copied.
5. Return to the previous browser tab, and open the S3
   console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
6. In the left navigation pane, choose **Buckets**.
7. In the **Buckets** list, choose the name of the bucket that
   you created in [Step 1](#cf-s3-step1 "#cf-s3-step1") (for example,
   `tutorial-bucket`).
8. In the **Objects** list, choose the name of the video that
   you uploaded in [Step 2](#cf-s3-step2 "#cf-s3-step2") (for example,
   `sample.mp4`).
9. On the object detail page, in the **Object overview**
   section, copy the value of the **Key**. This value is the path
   to the uploaded video object in the S3 bucket.
10. Return to the browser tab where you previously pasted the distribution domain
    name, enter a forward slash (`/`) after the distribution
    domain name, and then paste the path to the video that you copied earlier (for
    example, `sample.mp4`).

Now, your S3 video is publicly accessible and hosted
through CloudFront at a URL that looks similar to the following:

```
https://`CloudFront distribution domain name`/`Path to the S3 video`
```

Replace `CloudFront distribution domain name` and
`Path to the S3 video` with the appropriate values.
An example URL is
`https://d111111abcdef8.cloudfront.net/sample.mp4`.

## Step 6: Configure your CloudFront distribution to use your

custom domain name

To use your own domain name instead of the CloudFront domain name in the URL to access the
S3 video, add an alternate domain name to your CloudFront distribution.

###### Substeps

- [Request an SSL certificate](#cf-s3-step6-create-SSL "#cf-s3-step6-create-SSL")
- [Add the alternate
  domain name to your CloudFront distribution](#cf-s3-step6-custom-domain "#cf-s3-step6-custom-domain")
- [Create a DNS record to route traffic from
  your alternate domain name to your CloudFront distribution's domain name](#cf-s3-step6-DNS-record "#cf-s3-step6-DNS-record")
- [Check whether IPv6 is enabled for your
  distribution and create another DNS record if needed](#s3-step6-ipv6 "#s3-step6-ipv6")

### Request an SSL certificate

To allow your viewers to use HTTPS and your custom domain name in the URL for your
video streaming, use AWS Certificate Manager (ACM) to request a Secure Sockets Layer (SSL)
certificate. The SSL certificate establishes an encrypted network connection to the
website.

1. Sign in to the AWS Management Console and open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/").
2. If the introductory page appears, under
   **Provision certificates**, choose
   **Get Started**.
3. On the **Request a certificate** page, choose
   **Request a public certificate**, and then choose
   **Request a certificate**.
4. On the **Add domain names** page, enter the fully
   qualified domain name (FQDN) of the site that you want to secure with an
   SSL/TLS certificate. You can use an asterisk (`*`) to request a
   wildcard certificate to protect several site names in the same domain. For
   this tutorial, enter `*` and the custom domain name
   that you configured in [Prerequisites](#cf-s3-prerequisites "#cf-s3-prerequisites"). For example, enter
   `*.example.com`, and then choose
   **Next**.

For more information, see [To request an ACM public certificate (console)](../../../acm/latest/userguide/gs-acm-request-public.md#request-public-console "../../../acm/latest/userguide/gs-acm-request-public.md#request-public-console") in the _AWS Certificate Manager User Guide_. 5. On the **Select validation method**
page, choose **DNS validation**. Then,
choose **Next**.

If you are able to edit your DNS configuration, we recommend that you use
DNS domain validation rather than email validation. DNS validation has
multiple benefits over email validation. For more information, see [Option 1: DNS validation](../../../acm/latest/userguide/dns-validation.md "../../../acm/latest/userguide/dns-validation.md") in the
_AWS Certificate Manager User Guide_. 6. (Optional) On the **Add tags** page, tag your certificate
with metadata. 7. Choose **Review**. 8. On the **Review** page, verify that the information under
**Domain name** and **Validation
method** are correct. Then, choose **Confirm and
request**.

The **Validation** page shows that your request is being
processed and that the certificate domain is being validated. The
certificate awaiting validation is in the **Pending
validation** status. 9. On the **Validation** page, choose the down arrow to the
left of your custom domain name, and then choose **Create record in
Route 53** to validate your domain ownership through
DNS.

Doing this adds a CNAME record provided by AWS Certificate Manager to your DNS
configuration. 10. In the **Create record in Route 53**
dialog box, choose **Create**.

The **Validation** page should display a status
notification of **Success** at the bottom. 11. Choose **Continue** to view the
**Certificates** list page.

The **Status** for your new certificate changes from
**Pending validation** to **Issued**
within 30 minutes.

### Add the alternate

domain name to your CloudFront distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, choose
   **Distributions**.
3. Choose the ID for the distribution that you created in
   [Step 4](#cf-s3-step3 "#cf-s3-step3").
4. On the **General** tab, go to the
   **Settings** section, and choose
   **Edit**.
5. On the **Edit settings** page, for **Alternate
   domain name (CNAME) - _optional_**, choose **Add item** to
   add the custom domain names that you want to use in the URL for the S3 video
   served by this CloudFront distribution.

In this tutorial, for example, if you want to route traffic for a
subdomain, such as `www.example.com`, enter the subdomain name
(`www`) with the domain name (`example.com`).
Specifically, enter `www.example.com`.

###### Note

The alternate domain name (CNAME) that you add
must be covered by the SSL certificate that you
previously attached to your CloudFront
distribution. 6. For **Custom SSL certificate - _optional_**, choose the SSL certificate that you
requested earlier (for example,
`*.example.com`).

###### Note

If you don't see the SSL certificate immediately after you request it,
wait
30
minutes, and then refresh the list until the SSL certificate is
available for you to select. 7. Keep the remaining settings set to the defaults.
Choose **Save changes**. 8. On the **General** tab for the distribution, wait for the
value of **Last modified** to change from
**Deploying** to the timestamp when the distribution
was last modified.

### Create a DNS record to route traffic from

your alternate domain name to your CloudFront distribution's domain name

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, choose **Hosted
   zones**.
3. On the **Hosted zones** page, choose the name of the
   hosted zone that Route 53 created for you in [Prerequisites](#cf-s3-prerequisites "#cf-s3-prerequisites") (for example,
   `example.com`).
4. Choose **Create record**, and then use the
   **Quick create record** method.
5. For **Record name**, keep the value for the record name
   the same as the alternate domain name of the CloudFront distribution that you
   added earlier.

In this tutorial, to route traffic to a subdomain,
such as `www.example.com`, enter the
subdomain name without the domain name. For example,
enter only `www` in the text field
before your custom domain name. 6. For **Record type**, choose
**A - Routes traffic to an IPv4 address
and some AWS resources**. 7. For **Value**, choose the **Alias**
toggle to enable the alias resource. 8. Under **Route traffic to**, choose **Alias to
CloudFront distribution** from the dropdown list. 9. In the search box that says **Choose distribution**,
choose the domain name of the CloudFront distribution that you created in [Step 4](#cf-s3-step4 "#cf-s3-step4").

To find the domain name of your CloudFront distribution, do
the following:

    1. In a new browser tab, sign in to the AWS Management Console
     and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v3/home](https://console.aws.amazon.com/cloudfront/v3/home "https://console.aws.amazon.com/cloudfront/v3/home").
    2. In the left navigation pane, choose
     **Distributions**.
    3. In the **Origins** column, find the correct CloudFront
     distribution by looking for its origin name, which starts with the
     S3 bucket that you created in [Step
     1](#cf-s3-step1 "#cf-s3-step1") (for example,
     `tutorial-bucket`).
    4. After finding the distribution in the list, widen the
     **Domain name** column to see the domain name
     value for your CloudFront distribution.

10. On the **Create record** page in the Route 53 console, for
    the remaining settings, keep the defaults.
11. Choose **Create records**.

### Check whether IPv6 is enabled for your

distribution and create another DNS record if needed

If IPv6 is enabled for your distribution, you must create another DNS record.

1. To check whether IPv6 is enabled for your
   distribution, do the following:
   1. Sign in to the AWS Management Console and open the CloudFront console at
      [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
   2. In the left navigation pane, choose
      **Distributions**.
   3. Choose the ID of the CloudFront distribution that you created in [Step 4](#cf-s3-step4 "#cf-s3-step4").
   4. On the **General** tab, under
      **Settings**, check whether
      **IPv6** is set to
      **Enabled**.

   If IPv6 is enabled for your distribution, you must create
   another DNS record.

2. If IPv6 is enabled for your distribution, do the
   following to create a DNS record:
   1. Sign in to the AWS Management Console and open the Route 53 console at
      [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
   2. In the left navigation pane, choose **Hosted
      zones**.
   3. On the **Hosted zones** page, choose the name of
      the hosted zone that Route 53 created for you in [Prerequisites](#cf-s3-prerequisites "#cf-s3-prerequisites") (for example,
      `example.com`).
   4. Choose **Create record**, and then use the
      **Quick create record** method.
   5. For **Record name**, in the text field before
      your custom domain name, type the same value that you typed when you
      created the IPv4 DNS record earlier. For example, in this
      tutorial, to route traffic for the subdomain
      `www.example.com`, enter only
      `www`.
   6. For **Record type**, choose
      **AAAA - Routes traffic to an
      IPv6 address and some AWS
      resources**.
   7. For **Value**, choose the
      **Alias** toggle to enable the alias resource.
   8. Under **Route traffic to**, choose
      **Alias to CloudFront distribution** from the
      dropdown list.
   9. In the search box that says **Choose
      distribution**, choose the domain name of the CloudFront
      distribution that you created in [Step
      4](#cf-s3-step4 "#cf-s3-step4").
   10. For the remaining settings, keep the defaults.
   11. Choose **Create
       records**.

## Step 7: Access the S3 video through

the CloudFront distribution with the custom domain name

To access the S3 video using the custom URL, you must combine your alternate domain
name with the path to the video in the S3 bucket.

###### To create a custom URL to access the S3 video through the

CloudFront distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, choose **Distributions**.
3. To get the alternate domain name of your CloudFront
   distribution, do the following:
   1. In the **Origins** column, find the correct CloudFront
      distribution by looking for its origin name, which starts with the S3
      bucket name for the bucket that you created in [Step 1](#cf-s3-step1 "#cf-s3-step1") (for example,
      `tutorial-bucket`).
   2. After finding the distribution in the list, widen the
      **Alternate domain names** column to copy the value
      of the alternate domain name of your CloudFront distribution.

4. In a new browser tab, paste the alternate domain name of the CloudFront
   distribution.
5. Return to the previous browser tab, and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
6. Find the path to your S3 video, as explained in [Step 5](#cf-s3-step5 "#cf-s3-step5").
7. Return to the browser tab where you previously pasted the alternate domain
   name, enter a forward slash (`/`), and then paste the path
   to your S3 video (for example, `sample.mp4`).

Now, your S3 video is publicly accessible and hosted
through CloudFront at a custom URL that looks similar to the
following:

```
https://`CloudFront distribution alternate domain name`/`Path to the S3 video`
```

Replace `CloudFront distribution alternate domain name` and
`Path to the S3 video` with the appropriate values.
An example URL is
`https://www.example.com/sample.mp4`.

## (Optional) Step 8: View data about

requests received by your CloudFront distribution

###### To view data about requests received by your CloudFront

distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, under **Reports &
   analytics**, choose the reports from the console, ranging from
   **Cache statistics**, **Popular Objects**,
   **Top Referrers**, **Usage**, and
   **Viewers**.

You can filter each report dashboard. For more information, see [CloudFront Reports in
the Console](../../../AmazonCloudFront/latest/DeveloperGuide/reports.md "../../../AmazonCloudFront/latest/DeveloperGuide/reports.md") in the _Amazon CloudFront Developer
Guide_. 3. To filter data, choose the ID of the CloudFront distribution
that you created in [Step
4](#cf-s3-step4 "#cf-s3-step4").

## Step 9: Clean up

If you hosted an S3 streaming video using CloudFront and Route 53 only as a learning exercise,
delete the AWS resources that you allocated so that you no longer accrue
charges.

###### Note

When you register a domain, it costs money immediately and it's irreversible. You
can choose not to auto-renew the domain, but you pay up front and own it for the
year. For more information, see [Registering a new
domain](../../../Route53/latest/DeveloperGuide/domain-register.md "../../../Route53/latest/DeveloperGuide/domain-register.md") in the _Amazon Route 53 Developer
Guide_.

###### Substeps

- [Delete the CloudFront
  distribution](#cf-s3-step9-delete-cf "#cf-s3-step9-delete-cf")
- [Delete the DNS
  record](#cf-s3-step9-delete-dns "#cf-s3-step9-delete-dns")
- [Delete the
  public hosted zone for your custom domain](#cf-s3-step9-delete-hosted-zone "#cf-s3-step9-delete-hosted-zone")
- [Delete the custom domain name from
  Route 53](#cf-s3-step9-delete-domain "#cf-s3-step9-delete-domain")
- [Delete the original
  video in the S3 source bucket](#cf-s3-step9-delete-video "#cf-s3-step9-delete-video")
- [Delete the S3 source
  bucket](#cf-s3-step9-delete-bucket "#cf-s3-step9-delete-bucket")

### Delete the CloudFront

distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the left navigation pane, choose
   **Distributions**.
3. In the **Origins** column, find the correct CloudFront
   distribution by looking for its origin name, which starts with the S3 bucket
   name for the bucket that you created in [Step
   1](#cf-s3-step1 "#cf-s3-step1") (for example, `tutorial-bucket`).
4. To delete the CloudFront distribution, you must disable it
   first.
   - If the value of the **Status** column is
     **Enabled** and the value of **Last
     modified** is the timestamp when the distribution was
     last modified, continue to disable the distribution before deleting
     it.
   - If the value of **Status** is
     **Enabled** and the value of **Last
     modified** is **Deploying**, wait
     until the value of **Status** changes to the
     timestamp when the distribution was last modified. Then continue to
     disable the distribution before deleting it.

5. To disable the CloudFront distribution, do the
   following:
   1. In the **Distributions** list, select the check
      box next to the ID for the distribution that you want to delete.
   2. To disable the distribution, choose **Disable**,
      and then choose **Disable** to confirm.

   If you disable a distribution that has an alternate domain name
   associated with it, CloudFront stops accepting traffic for that domain
   name (such as `www.example.com`), even if another
   distribution has an alternate domain name with a wildcard
   (`*`) that matches the same domain (such as
   `*.example.com`). 3. The value of **Status** immediately changes to
   **Disabled**. Wait until the value of
   **Last modified** changes from
   **Deploying** to the timestamp when the
   distribution was last modified.

   Because CloudFront must propagate this change to all
   edge locations, it might take a few minutes
   before the update is complete and the
   **Delete** option is
   available for you to delete the distribution.

6. To delete the disabled distribution, do the
   following:
   1. Choose the check box next to the ID for the distribution that you
      want to delete.
   2. Choose **Delete**, and then choose
      **Delete** to confirm.

### Delete the DNS

record

If you want to delete the public hosted zone for the domain (including the DNS
record), see [Delete the
public hosted zone for your custom domain](#cf-s3-step9-delete-hosted-zone "#cf-s3-step9-delete-hosted-zone") in the _Amazon Route 53 Developer Guide_. If you only want to delete the DNS record
created in [Step 6](#cf-s3-step6 "#cf-s3-step6"), do the following:

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, choose **Hosted
   zones**.
3. On the **Hosted zones** page, choose the name of the
   hosted zone that Route 53 created for you in [Prerequisites](#cf-s3-prerequisites "#cf-s3-prerequisites") (for example,
   `example.com`).
4. In the list of records, select the check box next to the records that you
   want to delete (the records that you created in [Step 6](#cf-s3-step6 "#cf-s3-step6")).

###### Note

You can't delete records that have a **Type** value
of **NS** or **SOA**. 5. Choose **Delete records**. 6. To confirm the deletion, choose **Delete**.

Changes to records take time to propagate to the Route 53 DNS servers.
Currently, the only way to verify that your changes have propagated is to
use the [GetChange API
action](../../../Route53/latest/APIReference/API_GetChange.md "../../../Route53/latest/APIReference/API_GetChange.md"). Changes usually propagate to all Route 53 name servers
within 60 seconds.

### Delete the

public hosted zone for your custom domain

###### Warning

If you want to keep your domain registration but stop routing internet traffic
to your website or web application, we recommend that you delete records in the
hosted zone (as described in the prior section) instead of deleting the hosted
zone.

If you delete a hosted zone, someone else can use the domain and route traffic
to their own resources using your domain name.

In addition, if you delete a hosted zone, you can't undelete it. You must
create a new hosted zone and update the name servers for your domain
registration, which can take up to 48 hours to take effect.

If you want to make the domain unavailable on the internet, you can first
transfer your DNS service to a free DNS service and then delete the Route 53 hosted
zone. This prevents future DNS queries from possibly being misrouted.

1. If the domain is registered with Route 53, see [Adding or changing name servers and glue records for a
   domain](../../../Route53/latest/DeveloperGuide/domain-name-servers-glue-records.md "../../../Route53/latest/DeveloperGuide/domain-name-servers-glue-records.md") in the _Amazon Route 53 Developer
   Guide_ for information about how to replace Route 53 name
   servers with name servers for the new DNS service.
2. If the domain is registered with another registrar, use the method
   provided by the registrar to change name servers for the domain.

###### Note

If you're deleting a hosted zone for a subdomain
(`www.example.com`), you don't need to change name servers
for the domain (`example.com`).

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the left navigation pane, choose **Hosted
   zones**.
3. On the **Hosted zones** page, choose
   the name of the hosted zone that you want to
   delete.
4. On the **Records** tab for your
   hosted zone, confirm that the hosted zone that you want
   to delete contains only an **NS** and
   an **SOA** record.

If it contains additional records, delete them first.

If you created any NS records for subdomains in the
hosted zone, delete those records too. 5. On the **DNSSEC signing** tab for your hosted zone,
disable DNNSSEC signing if it was enabled. For more information, see [Disabling DNSSEC signing](../../../Route53/latest/DeveloperGuide/dns-configuring-dnssec-disable.md "../../../Route53/latest/DeveloperGuide/dns-configuring-dnssec-disable.md") in the _Amazon Route 53 Developer Guide_. 6. At the top of the details page of the hosted zone, choose **Delete
zone**. 7. To confirm the deletion, enter `delete`, and then
choose **Delete**.

### Delete the custom domain name from

Route 53

For most top-level domains (TLDs), you can delete the registration if you no
longer want it. If you delete a domain name registration from Route 53 before the
registration is scheduled to expire, AWS does not refund the registration fee. For
more information, see [Deleting a domain name
registration](../../../Route53/latest/DeveloperGuide/domain-delete.md "../../../Route53/latest/DeveloperGuide/domain-delete.md") in the _Amazon Route 53 Developer Guide_.

###### Important

If you want to transfer the domain between AWS accounts or transfer the
domain to another registrar, don't delete the domain and expect to immediately
reregister it. Instead, see the applicable documentation in the
_Amazon Route 53 Developer Guide_:

- [Transferring a domain to a different AWS account](../../../Route53/latest/DeveloperGuide/domain-transfer-between-aws-accounts.md "../../../Route53/latest/DeveloperGuide/domain-transfer-between-aws-accounts.md")
- [Transferring a domain from Amazon Route 53 to another
  registrar](../../../Route53/latest/DeveloperGuide/domain-transfer-from-route-53.md "../../../Route53/latest/DeveloperGuide/domain-transfer-from-route-53.md")

### Delete the original

video in the S3 source bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Bucket name** list, choose the name of the
   bucket that you uploaded the video to in [Step
   2](#cf-s3-step2 "#cf-s3-step2") (for example, `tutorial-bucket`).
4. On the **Objects** tab, select the check box next to the
   name of the object that you want to delete (for example,
   `sample.mp4`).
5. Choose **Delete**.
6. Under **Permanently delete objects?**, enter
   `permanently delete` to confirm that you want to
   delete this object.
7. Choose **Delete objects**.

### Delete the S3 source

bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, select the option button next to
   the name of the bucket that you created in [Step
   1](#cf-s3-step1 "#cf-s3-step1") (for example, `tutorial-bucket`).
4. Choose **Delete**.
5. On the **Delete bucket** page, confirm that you want to
   delete the bucket by entering the bucket name in the text field, and then
   choose **Delete bucket**.

## Next steps

After you complete this tutorial, you can further explore the following related use
cases:

- Transcode S3 videos into streaming formats needed by a
  particular television or connected device before hosting
  these videos with a CloudFront distribution.

To use Amazon S3 Batch Operations, AWS Lambda and AWS Elemental MediaConvert to batch-transcode a
collection of videos to a variety of output media formats, see [Tutorial: Batch-transcoding
videos with S3 Batch Operations](tutorial-s3-batchops-lambda-mediaconvert-video.md "tutorial-s3-batchops-lambda-mediaconvert-video.md").

- Host other objects stored in S3, such as images, audio, motion graphics, style
  sheets, HTML, JavaScript, React apps, and so on, using CloudFront and Route 53.

For example, see [Tutorial: Configuring a static website using a
custom domain registered with Route 53](website-hosting-custom-domain-walkthrough.md "website-hosting-custom-domain-walkthrough.md") and [Speeding up your website with
Amazon CloudFront](website-hosting-cloudfront-walkthrough.md "website-hosting-cloudfront-walkthrough.md").

- Use [Amazon S3 Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration "https://aws.amazon.com/s3/transfer-acceleration") to configure fast and secure file transfers.
  Transfer Acceleration can speed up video uploading to your S3 bucket for long-distance
  transfer of larger videos. Transfer Acceleration
  improves
  transfer performance by routing traffic through the CloudFront globally distributed
  edge locations and over the AWS backbone networks. It also uses network
  protocol optimizations. For more information, see [Configuring fast, secure file transfers using
  Amazon S3 Transfer Acceleration](transfer-acceleration.md "transfer-acceleration.md").
