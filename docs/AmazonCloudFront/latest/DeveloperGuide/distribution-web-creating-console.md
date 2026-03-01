# Create a distribution

This topic explains how to use the CloudFront console to create a distribution.

###### Overview

1. Create one or more Amazon S3 buckets, or configure HTTP servers as your origin servers. An
   _origin_ is the location where you
   store the original version of your content. When CloudFront gets a request for
   your files, it goes to the origin to get the files that it distributes at
   edge locations. You can use any combination of Amazon S3 buckets and HTTP servers
   as your origin servers.
   - If you use Amazon S3, the name of your bucket must be all lowercase and cannot contain
     spaces.
   - If you use an Amazon EC2 server or another custom origin, review [Use Amazon EC2 (or another custom origin)](DownloadDistS3AndCustomOrigins.md#concept_CustomOrigin "DownloadDistS3AndCustomOrigins.md#concept_CustomOrigin").
   - For the current maximum number of origins that you can create for a distribution, or to
     request a higher quota, see [General quotas on distributions](cloudfront-limits.md#limits-web-distributions "cloudfront-limits.md#limits-web-distributions").

2. Upload your content to your origin servers. You make your objects publicly readable, or you can use CloudFront signed URLs to restrict access to
   your content.

###### Important

You are responsible for ensuring the security of your origin server. You must ensure
that CloudFront has permission to access the server and that the security settings safeguard your content. 3. Create your CloudFront distribution:

    * For a detailed procedure that creates a distribution in the CloudFront console,
     see [Create a CloudFront distribution in the console](#create-console-distribution "#create-console-distribution").
    * For information about creating a distribution using the CloudFront API, see
     [CreateDistribution](../../../cloudfront/latest/APIReference/API_CreateDistribution.md "../../../cloudfront/latest/APIReference/API_CreateDistribution.md") in the
     *Amazon CloudFront API Reference*.

4. (Optional) If you use the CloudFront console to create your distribution, create more cache
   behaviors or origins for the distribution. For more information about behaviors and origins, see [To update a multi-tenant distribution](HowToUpdateDistribution.md#HowToUpdateDistributionProcedure "HowToUpdateDistribution.md#HowToUpdateDistributionProcedure").
5. Test your distribution. For more information about testing, see [Test a distribution](distribution-web-testing.md "distribution-web-testing.md").
6. Develop your website or application to access your content using the domain name that
   CloudFront returned after you created your distribution in Step 3. For example, if
   CloudFront returns d111111abcdef8.cloudfront.net as the domain name for your distribution,
   the URL for the file `image.jpg` in an Amazon S3 bucket or in the root
   directory on an HTTP server is
   `https://d111111abcdef8.cloudfront.net/image.jpg`.

If you specified one or more alternate domain names (CNAMEs) when you created your
distribution, you can use your own domain name. In that case, the URL for
`image.jpg` might be
`https://www.example.com/image.jpg`.

Note the following:

    * If you want to use signed URLs to restrict access to your content, see [Serve private content with signed URLs and signed cookies](PrivateContent.md "PrivateContent.md").
    * If you want to serve compressed content, see [Serve compressed files](ServingCompressedFiles.md "ServingCompressedFiles.md").
    * For information about CloudFront request and response behavior for Amazon S3 and custom
     origins, see [Request and response behavior](RequestAndResponseBehavior.md "RequestAndResponseBehavior.md").

###### Topics

- [Create a CloudFront distribution in the console](#create-console-distribution "#create-console-distribution")
- [Values that CloudFront displays in the console](#distribution-web-values-returned "#distribution-web-values-returned")
- [Additional links](#distribution-helpful-links "#distribution-helpful-links")
- [Add a domain to your CloudFront standard distribution](add-domain-existing-distribution.md "add-domain-existing-distribution.md")

## Create a CloudFront distribution in the console

When you create a distribution, CloudFront configures your distribution settings for you, based on your content origin type. For more details about the preconfigured settings, see [Preconfigured distribution settings reference](template-preconfigured-origin-settings.md "template-preconfigured-origin-settings.md"). You can also create multi-tenant distributions with settings that can be reused across multiple distribution tenants. For more information, see [Understand how multi-tenant distributions work](distribution-config-options.md "distribution-config-options.md"). Alternatively, you can manually configure your own distribution settings.

Multi-tenant

###### To create a multi-tenant distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, then choose
   **Create distribution**.
3. Choose **Multi-tenant architecture**, **Next**.
4. Enter a **Distribution name** for the
   multi-tenant distribution. The name will appear as the value for the
   `Name` key. You can change this value later.
   You can add up to 50 tags for your multi-tenant distribution. For more
   information, see [Tag a distribution](tagging.md "tagging.md") .
5. (Optional) For **Wildcard certificate**, choose the AWS Certificate Manager (ACM)
   certificate that will cover all subdomains under the root
   domain, such as `*.example.com`. The
   certificate must be in the US East (N. Virginia) Region.
6. Choose **Next**.
7. On the **Specify origin** page, select the
   origin type that CloudFront will get your content from. CloudFront will
   use the recommended settings for that origin type for your
   multi-tenant distribution. For more information about the recommended settings,
   see [Preconfigured distribution settings reference](template-preconfigured-origin-settings.md "template-preconfigured-origin-settings.md").
8. For **Origin**, under the origin type that you selected, choose or enter the
   origin to use.
9. For **Origin path**, enter the forward slash
   (`/`) character, followed by the origin path.
10. (Optional) To add a parameter, choose **Insert parameter** for
    either the origin domain name or origin path. You can enter up
    to two parameters for each field.
    1. Choose **Create new
       parameter**.
    2. On the **Create new parameter**
       dialog box, for **Parameter name**,
       enter a unique name for the parameter and, optionally, a
       description.
    3. For **Required parameter**, select the checkbox to make this
       parameter value required at the distribution tenant level. If it's not required, enter a
       **Default value** that the distribution tenant
       will inherit.
    4. Choose **Create parameter**. This
       parameter appears in the corresponding field.

11. For **Options**, choose one of the following
    options:
    - **Use recommended origin settings** – Use the default
      recommended cache and origin settings for the origin
      type that you selected.
    - **Customize origin settings** – Customize the cache and
      origin settings. If you choose this option, specify your
      own values that appear.

12. Choose **Next**.
13. On the **Enable security protections** page, choose whether to
    enable AWS WAF security protections. You can customize the web
    ACL for specific distribution tenants later. For more information, see [Enable AWS WAF for a new distribution](WAF-one-click.md#enable-waf-new-distribution "WAF-one-click.md#enable-waf-new-distribution").
14. Choose **Next**, **Create distribution**.
15. On the **Distributions** page, your multi-tenant distribution appears in the list of
    resources. You can choose the **All
    distributions** dropdown to filter by standard distribution or
    multi-tenant distribution. You can also choose the **Type**
    column to filter by standard or multi-tenant distribution.

By default, CloudFront creates a connection group for you. The connection group controls how viewer
requests for content connect to CloudFront. You can customize some routing settings in
the connection group. For more information, see [Understand how multi-tenant distributions work](distribution-config-options.md "distribution-config-options.md").

You can create additional distribution tenants using the multi-tenant distribution as a
template.

###### To create a distribution tenant

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, do one of the following:
   - Choose **Distributions**, choose a
     multi-tenant distribution, and then choose **Create
     tenant**.
   - Choose **Distribution tenants** and then
     choose **Create tenant**.

3. For **Distribution tenant name**, enter the name. The
   name must be unique in your AWS account and can't be changed
   after you create it.
4. For **Template distribution**, choose a
   multi-tenant distribution ID from the list.
5. For **Manage tags**, add up to 50 key-value
   pairs for the distribution tenant. For more information, see [Tag a distribution](tagging.md "tagging.md").
6. Choose **Next**.
7. On the **Add domains** page, for
   **Certificate**, choose if you want a
   **Custom TLS certificate** for your
   distribution tenant. The certificate verifies whether you're authorized to
   use the domain name. The certificate must exist in the
   US East (N. Virginia) Region.
8. For **Domains**, enter your domain name.

###### Note

If you entered a domain name that isn't covered by a
certificate, you will need to verify that you own the
domain. You can still create the distribution tenant for now and verify
domain ownership later. For more information, see [Request certificates for your CloudFront distribution tenant](managed-cloudfront-certificates.md "managed-cloudfront-certificates.md"). 9. Choose **Next**. 10. On the **Define parameters** page, the
parameters that you specified in the multi-tenant distribution appear.
For required parameters, enter a value next to the parameter
name and save your changes. 11. To add another parameter, choose **Add
parameter** and enter a name and value. 12. Choose **Next**. 13. (Optional) For **Security customization**, if you choose to **Override distribution settings**, select the option for your use case. 14. (Optional) For **Geographic restrictions
customization**, if you choose to **Override distribution settings**, select the appropriate **Restriction type** and **Countries** for the distribution tenant. For more information, see [Restrict the geographic distribution of your content](georestrictions.md "georestrictions.md"). 15. Choose **Next**. 16. Choose **Create
distribution tenant**.

You can find all your distribution tenants on the
**Distribution tenants** page. You can filter by
the following:

###### Association

- Distribution ID
- Certificate ID
- Connection group ID
- Web ACL ID

###### Properties

- Name
- Domain

You can edit your distribution tenants to customize specific settings.
For more information, see [Distribution tenant customizations](tenant-customization.md "tenant-customization.md").

Standard

###### To create a standard distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, then choose
   **Create distribution**.
3. Enter a **Distribution name** for the
   standard distribution. The name will appear as the value for the
   `Name` key as a tag. You can change this value later.
   You can add up to 50 tags for your standard distribution. For more
   information, see [Tag a distribution](tagging.md "tagging.md").
4. Choose **Single website or app**, **Next**.
5. (Optional) For **Domain setup**, enter a domain that's already registered with Route 53 in your AWS account, or register a new domain. Complete the setup steps.
   - If your domain uses a DNS provider other than Route 53, you can still add the domain, but you'll need to do so after creating the distribution. Skip the domain setup for now to proceed with distribution creation. You must manually configure the domain and TLS certificate later. For more information, see [Add a domain to your CloudFront standard distribution](add-domain-existing-distribution.md "add-domain-existing-distribution.md").

6. Choose **Next**.
7. On the **Specify origin** page, select the
   origin type that CloudFront will get your content from. CloudFront will
   use the recommended settings for that origin type for your
   distribution. For more information about the recommended settings,
   see [Preconfigured distribution settings reference](template-preconfigured-origin-settings.md "template-preconfigured-origin-settings.md").
8. For **Origin**, choose or enter your
   origin.
9. For **Settings**, choose one of the following
   options:
   - **Use recommended origin settings** – Use the default
     recommended cache and origin settings for the origin
     type that you selected.
   - **Customize origin settings** – Customize the cache and
     origin settings. If you choose this option, specify your
     own values.

10. Choose **Next**.
11. On the **Enable security protections** page, choose whether to
    enable AWS WAF security protections.
12. Choose **Next**.
13. (Optional) If you are using Route 53 for your domain, you will see the **TLS certificate** page. If CloudFront can't find an existing AWS Certificate Manager (ACM) certificate for your domain in your AWS account in the `us-east-1` AWS Region, you can choose to automatically create a certificate or manually create it. After the certificate is created, choose **Next**.
14. Review your distribution details and choose **Create distribution**.
15. After CloudFront creates your distribution, the value of the **Status**
    column for your distribution will change from **Deploying** to
    the date and time that the distribution is deployed.

The domain name that CloudFront assigns to your distribution appears in the list of
distributions. (It also appears on the **General** tab for a selected
distribution.)

###### Tip

You can use an alternate domain name, instead of the name assigned to you by CloudFront,
by following the steps in [Use custom URLs by adding alternate domain names (CNAMEs)](CNAMEs.md "CNAMEs.md"). 16. When your distribution is deployed, confirm that you can access your content by using
your new CloudFront URL (d111111abcdef8.cloudfront.net) or the CNAME. For more information,
see [Test a distribution](distribution-web-testing.md "distribution-web-testing.md"). 17. Make sure to update your DNS records to point to CloudFront when you're ready to send traffic to your distribution. For more information, see [Point domains to CloudFront (standard distribution)](add-domain-existing-distribution.md#point-domains-standard "add-domain-existing-distribution.md#point-domains-standard").

## Values that CloudFront displays in the console

When you create a new distribution or update an existing distribution, CloudFront displays
the following information in the CloudFront console.

###### Note

Active trusted signers, the AWS accounts that have an active CloudFront key pair and can
be used to create valid signed URLs, are currently not visible in the CloudFront console.

### Distribution ID

When you perform an action on a distribution using the CloudFront API, you use the
distribution ID to specify which distribution to use, for
example, `EDFDVBD6EXAMPLE`. You can't change a distribution's distribution ID.

### Deploying and status

When you deploy a distribution, you see the **Deploying** status under
the **Last modified** column. Wait for the distribution to
finish deploying and make sure the **Status** column shows
**Enabled**. For more information, see [Distribution state](DownloadDistValuesGeneral.md#DownloadDistValuesEnabled "DownloadDistValuesGeneral.md#DownloadDistValuesEnabled").

### Last modified

The date and time that the distribution was last modified, using ISO 8601
format, for example, 2012-05-19T19:37:58Z. For more information, see [https://www.w3.org/TR/NOTE-datetime](https://www.w3.org/TR/NOTE-datetime "https://www.w3.org/TR/NOTE-datetime").

### Domain name

You use the distribution's domain name in the links to your objects. For example, if
your distribution's domain name is `d111111abcdef8.cloudfront.net`, the link to
`/images/image.jpg` would be
`https://d111111abcdef8.cloudfront.net/images/image.jpg`. You can't change the CloudFront
domain name for your distribution. For more information about CloudFront URLs for links to your
objects, see [Customize the URL format for files in CloudFront](LinkFormat.md "LinkFormat.md").

If you specified one or more alternate domain names (CNAMEs), you can use your own
domain names for links to your objects instead of using the CloudFront domain name. For more
information about CNAMEs, see [Alternate domain names (CNAMEs)](DownloadDistValuesGeneral.md#DownloadDistValuesCNAME "DownloadDistValuesGeneral.md#DownloadDistValuesCNAME").

###### Note

CloudFront domain names are unique. Your distribution's domain name was never used for a
previous distribution and will never be reused for another distribution in the
future.

## Additional links

For more information about creating a distribution, see the following links.

- To learn how to create a distribution that uses an Amazon Simple Storage Service (Amazon S3) bucket origin with origin access control (OAC), see [Get started with a CloudFront standard distribution](GettingStarted.md "GettingStarted.md").
- For information about using the CloudFront APIs to create a distribution, see [CreateDistribution](../../../cloudfront/latest/APIReference/API_CreateDistribution.md "../../../cloudfront/latest/APIReference/API_CreateDistribution.md") in the _Amazon CloudFront API Reference_.
- For information about updating a distribution (for example, to add cache behaviors to standard distributions, or to customize distribution tenants), see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").
- To see the current maximum number of distributions that you can create for each AWS
  account, or to request a higher quota (formerly known as limit), see [General quotas on distributions](cloudfront-limits.md#limits-web-distributions "cloudfront-limits.md#limits-web-distributions").
