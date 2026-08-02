# Use an Amazon CloudFront distribution to serve a static website

This topic shows you how to route DNS traffic for your domain to Amazon CloudFront distributions that
serve a static website. You create alias records that point your domain and subdomain to
your CloudFront distributions.

This topic is part of a static website setup workflow. For general information about routing
traffic to a CloudFront distribution, see [Routing traffic to an Amazon CloudFront distribution by using your domain name](routing-to-cloudfront-distribution.md "routing-to-cloudfront-distribution.md").

After you complete these steps, you have the following resources configured:

- An SSL/TLS certificate for your domain in AWS Certificate Manager
- Amazon S3 buckets configured for website hosting and redirect
- CloudFront distributions for both your root domain and subdomain
  Visitors can then reach your website at your custom domain name with HTTPS security from
  CloudFront.

## Prerequisites

Before you begin, complete these steps:

- Complete the steps in [Set up Amazon Route 53](setting-up-route-53.md "setting-up-route-53.md").
- Register a domain name using Amazon Route 53. For more information, see [Registering a new domain](domain-register.md "domain-register.md").
- Create a secure static website with Amazon CloudFront and Amazon Simple Storage Service. For
  instructions, see [Get started with a secure static website](../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md "../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md") in the
  _Amazon CloudFront Developer Guide_.

## Step 1: Route DNS traffic for your domain to your CloudFront distribution

Now that you have Amazon CloudFront distributions for your website, route DNS
traffic for your domain to those distributions. This lets visitors reach your
website at your custom domain name.

For more information about routing traffic to CloudFront distributions, see [Routing traffic to an Amazon CloudFront distribution by using your domain name](routing-to-cloudfront-distribution.md "routing-to-cloudfront-distribution.md").

###### To route traffic to your website

1. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted zones**.

###### Note

When you registered your domain, Amazon Route 53 created a hosted
zone with the same name. This hosted zone stores information about how
Route 53 routes traffic for the domain. 3. In the list of hosted zones, choose the name of your domain. 4. Choose **Create record**. 5. Specify the following values:

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

Choose your CloudFront distribution. The distribution name matches the value in the
**Domain name** column in the CloudFront console (for
example, `d111111abcdef8.cloudfront.net`).

**Evaluate target health**

Accept the default value of **No**. 6. Choose **Create records**.

###### To add an alias record for your root domain (`example.com`)

Add an alias record for your root domain too. Point it to the CloudFront
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

To check that your website works, open a web browser and go to
the following URLs:

- https://www.`your-domain-name`, for example,
  `www.example.com` – Displays the index document in the
  `www.your-domain-name` bucket
- https://`your-domain-name` for example,
  `example.com` – Redirects your request to the
  `www.your-domain-name` bucket

In some cases, you might need to clear the cache to see the expected
behavior.

For more information about routing internet traffic, see [Configuring Amazon Route 53 as your DNS service](dns-configuring.md "dns-configuring.md"). To route
traffic to AWS resources, see [Routing internet traffic to your AWS resources](routing-to-aws-resources.md "routing-to-aws-resources.md").
