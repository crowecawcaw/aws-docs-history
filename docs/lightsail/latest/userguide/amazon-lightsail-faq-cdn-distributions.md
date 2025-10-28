# Content delivery network

distributions

## What can I do with Lightsail CDN

distributions?

Lightsail content delivery network (CDN) distributions make it easy for you to
accelerate the delivery of content hosted on your Lightsail resources by storing and
serving it on Amazon’s global delivery network, powered by Amazon CloudFront. Distributions also help
you enable your website to support HTTPS traffic by providing simple SSL certificate
creation and hosting. Finally, distributions can help reduce the load on your Lightsail
resources and help your website handle large traffic spikes. Like all of Lightsail’s
features, setup can be completed with just a few clicks, and you pay a simple monthly
price.

## What types of resources can I use as

the origin of my distributions?

Lightsail distributions allow you to use your Lightsail instances and load balancers
as origins. Lightsail containers are not currently supported as origins. Resources outside
of Lightsail, such as S3 buckets, are not supported.

## Do I need to attach a static IPv4

address to my Lightsail instance in order to use it as an origin for my Lightsail
distribution?

Yes, static IPv4 addresses are required to be attached to instances that are specified
as origins. Lightsail distributions do not currently support IPv6.

## How do I setup a Lightsail

distribution with my WordPress website?

Create your distribution, select your WordPress instance as the origin, choose your
plan, and you’re all set. Lightsail distributions automatically configure your
distribution settings to optimize performance for most WordPress configurations.

## Can I attach multiple

origins?

Although you cannot attach multiple origins to your Lightsail distribution, you can
attach multiple instances to a Lightsail load balancer and specify it as the origin of
your distribution.

## Do Lightsail distributions support

certificate creation?

Yes. Lightsail distributions makes it easy to create, verify, and attach certificates
directly from your distribution’s management page.

## Is a certificate required?

A certificate is only required if you wish to use your custom domain name with your
distribution. All Lightsail distributions are created with a unique Amazon CloudFront domain name
that is HTTPS-enabled. However, if you wish to use your custom domain with your
distribution, then you need to attach a certificate for your custom domain to your
distribution.

## Is there a limit to the number of certificates

I can create?

Yes, refer to [Lightsail service quotas](../../../general/latest/gr/lightsail.md#limits_lightsail "../../../general/latest/gr/lightsail.md#limits_lightsail") for more information.

## How can I configure my

distribution to redirect HTTP requests to HTTPS?

Lightsail distributions automatically redirect all HTTP requests to HTTPS to ensure
that your content is served securely.

## How can I configure my apex domain

to point to my Lightsail distribution?

In order to point your apex domain to your CDN distribution, you must create an ALIAS
record in the domain name system (DNS) of your domain that maps your apex domain to your
distribution’s default domain. If your DNS hosting provider does not support ALIAS records,
you can use Lightsail DNS zones to easily configure your apex domain to point to your
distribution’s domain.

## What are the differences between Lightsail’s instance data transfer quotas and

distribution data transfer quotas?

While data transfer IN and OUT count toward your instance’s data transfer quota, only
data transfer OUT to your origin and to your viewers counts toward you distribution’s quota.
In addition, all data transfer OUT in excess of your distribution’s quota is charged an
overage fee, whereas some types of data transfer OUT are free for instances. Finally,
Lightsail distributions use a different regional overage model, though the majority of the
rates are the same as those charged for instance overage.

## Can I change the plan associated with my

distribution?

Yes, you can change your distribution's plan once per month. If you wish to change your
plan a second time, you must wait until the beginning of the following month to do
so.

## How do I know if my distribution is

working?

Lightsail distributions provide you with a variety of metrics that track the
performance of your distribution, including the total number of requests your distribution
has received, the amount of data your distribution has sent to clients and to your origin,
and the percentage of requests that have resulted in errors. Additionally, you can create
alerts that are linked to distribution metrics.

## Can I delete cached content on

my Lightsail distribution?

You can delete all cached content, but not specific files or folders.

## When should I use

Lightsail distributions versus Amazon CloudFront distributions?

Lightsail distributions are designed specifically for users who are hosting websites
or web applications on Lightsail resources, such as instances and load balancers. If
you’re using another service in AWS to host your website or app, have complex
configuration needs, or have a workload that involves a high number of requests per second
or large amount of video streaming, we recommend that you use Amazon CloudFront.

## Can I move my Lightsail content

delivery network (CDN) distribution to Amazon CloudFront?

Yes, you can move your Lightsail distribution by creating a similarly configured
distribution in Amazon CloudFront. All of the settings that can be configured in a Lightsail
distribution can also be configured in a CloudFront distribution. Complete the following steps to
move your distribution to CloudFront.

###### How to move your Lightsail distribution to CloudFront

- Take a snapshot of your Lightsail instance that is configured as your
  distribution's origin. Export the snapshot to Amazon EC2, and then create a new instance from
  the snapshot in Amazon EC2. For more information, see [Export snapshots to
  Amazon EC2](amazon-lightsail-exporting-snapshots.md "amazon-lightsail-exporting-snapshots.md").

###### Note

Create an application load balancer in Elastic Load Balancing if you need to load
balance your website or web application. For more information, see the [Elastic Load Balancing User Guide](../../../elasticloadbalancing/latest/application/introduction.md "../../../elasticloadbalancing/latest/application/introduction.md").

- Disable custom domains for your Lightsail distribution to detach certificates that
  you might have attached to it. For more information, see [Disabling custom
  domains for your Amazon Lightsail distributions](amazon-lightsail-disabling-distribution-custom-domains.md "amazon-lightsail-disabling-distribution-custom-domains.md").
- Using the AWS Command Line Interface (AWS CLI), run the get-distributions command to get a list of your
  Lightsail distribution’s settings. For more information, see [get-distributions](../../../cli/latest/reference/lightsail/get-distributions.md "../../../cli/latest/reference/lightsail/get-distributions.md") in the _AWS CLI Reference_.
- Sign in to the [CloudFront
  console](https://console.aws.amazon.com/cloudfront/ "https://console.aws.amazon.com/cloudfront/") and create a distribution with the same configuration settings as your
  Lightsail distribution. For more information, see [Creating a Distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md") in the _Amazon CloudFront Developer
  Guide_.
- Create a certificate in AWS Certificate Managerc (ACM) that you will attach to your CloudFront
  distribution. For more information, see [Request a Public Certificate](../../../acm/latest/userguide/gs-acm-request-public.md "../../../acm/latest/userguide/gs-acm-request-public.md") in the _ACM User
  Guide_.
- Update your CloudFront distribution to use the ACM certificate you created. For more
  information, see [Updating your CloudFront distribution](../../../AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.md#cnames-and-https-updating-cloudfront "../../../AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.md#cnames-and-https-updating-cloudfront") in the _CloudFront User
  Guide_.

## How is Lightsail CDN intended to be

used?

Lightsail CDN distributions are created using fixed-priced bundles of data transfer to
make the cost of using the service simple and predictable. Distribution bundles are designed
to cover a month’s worth of usage. Using distribution bundles in a way to avoid incurring
overage fees (including, but not limited to, frequently upgrading or downgrading bundles, or
using an excessively large number of distributions with a single origin) is beyond the
intended scope of use and is not permitted. In addition, workloads that involve a high
number of requests per second or large amount of video streaming are not permitted. Engaging
in these behaviors may result in throttling or suspension of your data services or
account.

## Do Lightsail CDN distributions support IPv6?

All Lightsail CDN distributions have IPv6 enabled by default. The distribution host
names resolve to both IPv4 and IPv6 addresses. IPv6 can be disabled by using a toggle on the
Networking tab of the CDN's management page.

## Do the origins need to be IPv6 enabled to work with

the Lightsail CDN distributions?

No. CDN distributions accept both IPv6 and IPv4 traffic, and seamlessly convert it to
IPv4 when communicating with the origins in the backend. Hence, origins behind a
distribution can either be dual-stack or IPv4 only.
