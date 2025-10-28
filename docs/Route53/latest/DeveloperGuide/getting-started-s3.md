# Use your domain for a static website in an Amazon S3 bucket

This tutorial shows you how to use Amazon Route 53 to route DNS traffic for your domain to an
Amazon Simple Storage Service bucket that hosts a static website. You'll create alias records that point your
domain to the S3 website endpoint.

This tutorial is part of a complete static website setup workflow. For general information
about routing traffic to any S3 bucket, see [Routing traffic to a website that is hosted in an
Amazon S3 bucket](RoutingToS3Bucket.md "RoutingToS3Bucket.md").

When you're finished, visitors can access your static website using your custom domain
name.

###### Note

You can also transfer an existing domain to Route 53, but the process is more complex and
time-consuming than registering a new domain. For more information, see [Transferring registration for a domain to
Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md").

## Prerequisites

Before you begin, complete these steps:

- Complete the steps in [Set up Amazon Route 53](setting-up-route-53.md "setting-up-route-53.md").
- Register a domain name using Amazon Route 53. For more information, see [Registering a new domain](domain-register.md "domain-register.md").
- Configure an Amazon Simple Storage Service bucket for static website hosting. For complete
  instructions, see [Tutorial: Configuring a static website using a custom domain registered
  with Route 53](../../../AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.md "../../../AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.md") in the _Amazon Simple Storage Service User Guide_.

When you complete the Amazon Simple Storage Service tutorial, you'll have:

- Amazon S3 buckets configured for website hosting and redirect (if using www
  subdomain)
- Website content uploaded to your bucket
- Public access configured for your website bucket

## Step 1: Route DNS traffic for your domain

to your website bucket

Now that you have an Amazon Simple Storage Service bucket configured for static website hosting, use
Amazon Route 53 to route DNS traffic for your domain to the bucket. This enables visitors to
access your website using your custom domain name.

###### To route traffic to your

website

1. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted zones**.

###### Note

When you registered your domain, Amazon Route 53 automatically created a hosted
zone with the same name. A hosted zone contains information about how you
want Route 53 to route traffic for the domain. 3. In the list of hosted zones, choose the name of your domain. 4. Choose **Create record**. 5. Specify the following values:

**Record name**

Leave blank to create a record for your root domain.

**Record type**

Choose **A ‐ Routes traffic to an IPv4 address and
some AWS resources**.

**Alias**

Turn on **Alias**.

**Route traffic to**

Choose **Alias to S3 website endpoint**.

Choose the Region where you created your S3 bucket.

Choose your S3 bucket. The bucket name should match the name of
your domain. In the list, the bucket name appears with the Amazon S3
website endpoint for the Region where the bucket was created, for
example, `s3-website-us-west-1.amazonaws.com
 (example.com)`.

If your bucket does not appear in the list, enter the Amazon S3 website
endpoint for the Region where the bucket was created, for example,
`s3-website-us-west-2.amazonaws.com`. For a
complete list of Amazon S3 website endpoints, see [Amazon S3
Website endpoints](../../../general/latest/gr/s3.md#s3_website_region_endpoints "../../../general/latest/gr/s3.md#s3_website_region_endpoints").

**Evaluate target health**

Accept the default value of **No**. 6. Choose **Create records**.

###### (Optional) To add an alias record for your subdomain

(`www.example.com`)

If you created a bucket for your subdomain, add an alias record for it
also.

1. Choose **Create record**.
2. Specify the following values:

**Record name**

Enter `www`.

**Record type**

Choose **A ‐ Routes traffic to an IPv4 address and
some AWS resources**.

**Alias**

Turn on **Alias**.

**Route traffic to**

Choose **Alias to S3 website endpoint**.

Choose the Region where you created your S3 bucket.

Choose your S3 bucket for the subdomain, for example,
`s3-website-us-west-2.amazonaws.com
 (www.example.com)`.

**Evaluate target health**

Accept the default value of **No**. 3. Choose **Create records**.

## Step 2: Test your website

To verify that the website is working correctly, open a web browser and browse to the
following URLs:

- http://`your-domain-name`, for example,
  `example.com` – Displays the index document in the
  `your-domain-name` bucket
- http://www.`your-domain-name` for example,
  `www.example.com` – Redirects your request to the
  `your-domain-name` bucket

In some cases, you might need to clear the cache to see the expected behavior.

For more advanced information about routing your internet traffic, see [Configuring Amazon Route 53 as your DNS service](dns-configuring.md "dns-configuring.md"). For information about
routing your internet traffic to AWS resources, see [Routing internet traffic to your AWS resources](routing-to-aws-resources.md "routing-to-aws-resources.md").

###### Note

Amazon S3 does not support HTTPS access to the website. If you want to use HTTPS, you
can use Amazon CloudFront to serve a static website hosted on Amazon S3. For more information, see
[Use an Amazon CloudFront distribution to serve
a static website](getting-started-cloudfront-overview.md "getting-started-cloudfront-overview.md").
