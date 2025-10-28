# Use an Amazon CloudFront distribution to serve

a static website

This tutorial shows you how to use Amazon Route 53 to route DNS traffic for your domain to
Amazon CloudFront distributions that serve a static website. You'll create alias records that point
your domain and subdomain to CloudFront distributions.

This tutorial is part of a complete static website setup workflow. For general information
about routing traffic to any CloudFront distribution, see [Routing traffic to an Amazon CloudFront
distribution by using your domain name](routing-to-cloudfront-distribution.md "routing-to-cloudfront-distribution.md").

When you're finished, visitors can access your website using your custom domain name with
HTTPS security provided by CloudFront.

## Prerequisites

Before you begin, complete these steps:

- Complete the steps in [Set up Amazon Route 53](setting-up-route-53.md "setting-up-route-53.md").
- Register a domain name using Amazon Route 53. For more information, see [Registering a new domain](domain-register.md "domain-register.md").
- Create a secure static website using Amazon CloudFront and Amazon Simple Storage Service. For complete
  instructions, see [Get started with a secure static website](../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md "../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md") in the
  _Amazon CloudFront Developer Guide_.

When you complete the Amazon CloudFront tutorial, you'll have:

- An SSL/TLS certificate for your domain in AWS Certificate Manager
- Amazon S3 buckets configured for website hosting and redirect
- CloudFront distributions for both your root domain and subdomain

## Step 1: Route DNS traffic for

your domain to your CloudFront distribution

Now that you have Amazon CloudFront distributions for your website, use Amazon Route 53 to route DNS
traffic for your domain to the distributions. This enables visitors to access your
website using your custom domain name.

For more information about routing traffic to CloudFront distributions, see [Routing traffic to an Amazon CloudFront
distribution by using your domain name](routing-to-cloudfront-distribution.md "routing-to-cloudfront-distribution.md").

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

For your subdomain record, enter
`www`.

**Record type**

Choose **A ‐ Routes traffic to an IPv4 address and
some AWS resources**.

**Alias**

Turn on **Alias**.

**Route traffic to**

Choose **Alias to CloudFront distribution**.

Choose the us-east-1 Region.

Choose your CloudFront distribution. The distribution name should match
the name that appears in the **Domain name** column
in the CloudFront console, for example,
`dddjjjkkk.cloudfront.net`.

**Evaluate target health**

Accept the default value of **No**. 6. Choose **Create records**.

###### To add an alias record for your root domain (`example.com`)

Add an alias record for your root domain also, so it points to the CloudFront
distribution that redirects traffic to `www.example.com`.

1. Choose **Create record**.
2. Specify the following values:

**Record name**

Leave blank to create a record for your root domain.

**Record type**

Choose **A ‐ Routes traffic to an IPv4 address and
some AWS resources**.

**Alias**

Turn on **Alias**.

**Route traffic to**

Choose **Alias to CloudFront distribution**.

Choose the us-east-1 Region.

Choose your root domain CloudFront distribution.

**Evaluate target health**

Accept the default value of **No**. 3. Choose **Create records**.

### Step 2: Test your website

To verify that the website is working correctly, open a web browser and browse to
the following URLs:

- https://www.`your-domain-name`, for example,
  `www.example.com` – Displays the index document in the
  `www.your-domain-name` bucket
- https://`your-domain-name` for example,
  `example.com` – Redirects your request to the
  `www.your-domain-name` bucket

In some cases, you might need to clear the cache to see the expected
behavior.

For more advanced information about routing your internet traffic, see [Configuring Amazon Route 53 as your DNS service](dns-configuring.md "dns-configuring.md"). For information
about routing your internet traffic to AWS resources, see [Routing internet traffic to your AWS resources](routing-to-aws-resources.md "routing-to-aws-resources.md").
