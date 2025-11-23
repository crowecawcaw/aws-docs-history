# CloudFront flat-rate pricing plans

CloudFront flat-rate pricing plans combine the Amazon CloudFront global content delivery network (CDN)
with multiple AWS services and features into a monthly price with no overage charges,
regardless of traffic spikes or attacks.

Flat-rate pricing plans include the following features for a simple monthly price:

- CloudFront CDN
- AWS WAF and DDoS protection
- Bot management and analytics
- Amazon Route 53 DNS
- Amazon CloudWatch Logs ingestion
- TLS certificate
- Serverless edge compute
- Amazon S3 storage credits each month
  Plans are available in Free, Pro, Business, and Premium tiers to match your application's
  needs. Plans do not require an annual commitment to get the best available rates. Start with
  the Free plan and upgrade to access more capabilities and larger usage allowances.

###### Topics

- [Benefits of CloudFront flat-rate pricing plans](#pricing-plan-benefits "#pricing-plan-benefits")
- [Features by pricing plan tier](#pricing-plan-features "#pricing-plan-features")
- [Monthly usage allowances](#usage-allowance "#usage-allowance")
- [Costs covered by your plan](#costs-covered-by-plan "#costs-covered-by-plan")
- [Reduce overall AWS costs with pricing
  plans](#pricing-plan-vs-payg "#pricing-plan-vs-payg")
- [Manage your flat-rate pricing plans](#manage-your-pricing-plans "#manage-your-pricing-plans")
- [Permissions](#prerequisites-pricing-plan "#prerequisites-pricing-plan")
- [Flat-rate pricing plan quotas](#pricing-plan-quotas "#pricing-plan-quotas")
- [Unsupported features](#pricing-plan-unsupported-features "#pricing-plan-unsupported-features")

## Benefits of CloudFront flat-rate pricing plans

The CloudFront pricing plan provides several key benefits:

- **Consolidated services and pricing**

Combine multiple AWS services and features into a single plan for one flat
rate. Designed to eliminate separate service purchases and upfront pricing
calculations.

- **No overages**

There are no overage charges regardless of traffic spikes or attacks.

- **Clear usage allowances**

Each plan includes published usage allowances designed for optimal performance
at that tier. Monitor your usage, receive proactive notifications, and upgrade
based on your application's needs, with no long-term commitments.

- **Protect against DDoS attacks**

CloudFront and AWS WAF absorb and block attacks before they reach your infrastructure.
Reserves your compute, database, and infrastructure utilization only for
legitimate traffic. Blocked DDoS attacks and requests blocked by AWS WAF never
count against your usage allowance.

- **Reduce your overall AWS costs**

Data transfer from AWS applications running on services such as Amazon S3, AWS
Application Load Balancer (ALB), or Amazon API Gateway to CloudFront continues
to be free. When you serve your AWS applications through CloudFront instead of
directly to the internet, your flat-rate plan covers the data transfer costs
between your applications and your viewers for a simple monthly price without
the worry of overages. Fewer requests reaching your origin also reduces your
costs on services that charge based on usage.

## Features by pricing plan tier

Each pricing plan covers one CloudFront distribution with up to one domain that combines
essential features and services into one monthly price. Each plan also includes
additional S3 storage credits.

Plans on higher tiers include all features from lower tier plans as well as additional
features.

- **Free** – For hobbyists, learners, and developers
  getting started.
- **Pro** – Launch and grow small websites, blogs, and
  applications.
- **Business** – Protect and accelerate business
  applications.
- **Premium** – Scale and protect business and
  mission-critical applications.

Select a plan tier that includes features and configurations that you need for your
applications. See the following features per pricing plan.

### Pricing plan features

The following table shows the CloudFront, AWS WAF and DDoS, Amazon Route 53, Amazon CloudWatch, and
Amazon S3 features included in each pricing plan tier.

| Performance and Delivery                                                                                                                                                                                                                                                                                                                                                           | Free       | Pro        | Business   | Premium    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | ---------- | ---------- |
| **Global CDN**<br>Use CloudFront's 750+ global edge locations as a massive,<br>distributed, single point of entry for your web application.<br>Accelerate static, dynamic, and non-cacheable<br>applications.                                                                                                                                                                      | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Content caching**<br>Store copies of your content in CloudFront's 750+ edge<br>locations worldwide, delivering it to users from the nearest<br>location. Reduces load times, protects your application from<br>traffic spikes, and saves costs by serving repeated requests<br>locally instead of from your application servers.                                                 | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Fast cache invalidations**<br>Remove or update cached content across all edge locations<br>within seconds.                                                                                                                                                                                                                                                                       | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Smart routing**<br>Intelligently routes users to the optimal edge location using<br>real-time network data, and connects to your AWS origin<br>through the AWS private network for better performance.                                                                                                                                                                           | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Tiered caching**<br>[Regional edge<br>caches](HowCloudFrontWorks.md#CloudFrontRegionaledgecaches "HowCloudFrontWorks.md#CloudFrontRegionaledgecaches") sit between edge locations and your<br>application to store content longer, reducing load on your<br>application and maintaining fast delivery.                                                                           | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Default caching rules**<br>Makes effective caching decisions to cache most web<br>applications without custom configuration.                                                                                                                                                                                                                                                     | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Custom caching rules**<br>Control how CloudFront caches content by specifying which request<br>values to use, optimizing for your application's performance,<br>personalization, and freshness needs using [cache<br>policies](controlling-the-cache-key.md "controlling-the-cache-key.md").                                                                                     |            |            | Yes<br>Yes | Yes<br>Yes |
| **High-speed origin routing**<br>With [Origin Shield](origin-shield.md "origin-shield.md"),<br>dynamic requests are routed from edge locations to your origin<br>using CloudFront's private network for high-performance path to<br>your origin.                                                                                                                                   |            |            |            | Yes<br>Yes |
| **Origin load reduction**<br>Adds an additional caching layer close to your web application<br>using [Origin Shield](origin-shield.md "origin-shield.md"). Origin<br>Shield consolidates requests from all edge locations, reducing<br>load on your application particularly during traffic<br>spikes.                                                                             |            |            |            | Yes<br>Yes |
| **Automatic origin failover**<br>Automatically routes traffic to a backup origin if your<br>primary origin fails, [maintaining high<br>availability](high_availability_origin_failover.md "high_availability_origin_failover.md") without disrupting users.                                                                                                                        |            |            |            | Yes<br>Yes |
| **Default origin request rules**<br>Control which information from viewer requests is<br>automatically included in requests to your origin, using [AWS<br>managed origin request policies](using-managed-origin-request-policies.md "using-managed-origin-request-policies.md") optimized for common<br>scenarios.                                                                 | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Default response header rules**<br>Use [AWS managed response header policies](using-managed-response-headers-policies.md "using-managed-response-headers-policies.md") to add or<br>remove HTTP headers in responses to viewers, preconfigured for<br>common security headers, CORS settings, and other standard use<br>cases.                                                   | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Custom origin request rules**<br>Create your own [origin request policies](controlling-origin-requests.md "controlling-origin-requests.md") to specify exactly which URL<br>query strings, headers, and cookies are forwarded to your<br>origin, enabling custom analytics and request handling.                                                                                 |            |            | Yes<br>Yes | Yes<br>Yes |
| **Custom response header rules**<br>Create your own [response header policies](modifying-response-headers.md "modifying-response-headers.md") to control exactly which<br>HTTP headers CloudFront adds or removes in responses to viewers, such<br>as security headers, Content Security Policy (CSP), CORS<br>settings, and custom application headers.                           |            |            | Yes<br>Yes | Yes<br>Yes |
| **Number of cache behaviors**<br>Configure [cache behaviors](DownloadDistValuesCacheBehavior.md "DownloadDistValuesCacheBehavior.md") to control how CloudFront handles requests<br>for specific URL patterns, including which origin serves the<br>content, how content is cached, and whether HTTPS or signed URLs<br>are required.                                              | 5          | 10         | 50         | 100        |
| **Security and<br>Protection**                                                                                                                                                                                                                                                                                                                                                     |            |            |            |            |
| **Always-on DDoS protection**<br>Protect against DDoS attacks that target your websites or<br>applications.                                                                                                                                                                                                                                                                        | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Advanced DDoS Protection**<br>Identify and block DDoS attacks in seconds using the [AntiDDoS AMR](../../../waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.md "../../../waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.md"). AWS learns your unique application<br>patterns to distinguish between attacks and natural surges from<br>legitimate users. |            |            | Yes<br>Yes | Yes<br>Yes |
| **Web Application Firewall (WAF)**<br>Protect against common application vulnerabilities and<br>potential threats based on Amazon internal threat intelligence.<br>Requests are blocked before reaching your servers.                                                                                                                                                              | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Number of WAF rules**<br>Total number of security rules you can create and enable in<br>your WAF configuration, including both custom rules and AWS<br>Managed Rules.                                                                                                                                                                                                            | 5          | 25         | 50         | 75         |
| **Protections for WordPress, PHP, and SQL databases**<br>Use-case based security rules to protect common applications<br>and operating systems like WordPress, PHP, SQL databases, Linux,<br>and Windows.                                                                                                                                                                          |            | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **IP-based rate limiting**<br>Automatically block IP addresses that exceed a configurable<br>number of requests over a 5-minute period, protecting against<br>HTTP flood attacks and Denial of Service (DoS) attempts.                                                                                                                                                             | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Geographic traffic blocking**<br>Block requests from selected countries or regions.                                                                                                                                                                                                                                                                                              | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Header-based threat filtering**<br>Create WAF security rules that filter threats based on HTTP<br>request headers.                                                                                                                                                                                                                                                               |            | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Regex-based threat filtering**<br>Create WAF security rules using regular expressions to match<br>URI paths and HTTP request attributes.                                                                                                                                                                                                                                         |            |            | Yes<br>Yes | Yes<br>Yes |
| **JavaScript challenge**<br>Block automated threats by requiring browsers to complete<br>JavaScript challenges that verify legitimate users.                                                                                                                                                                                                                                       |            |            | Yes<br>Yes | Yes<br>Yes |
| **Bot management and analytics**<br>Detect and analyze bot traffic with [AWS WAF<br>Bot Control](../../../waf/latest/developerguide/waf-bot-control.md "../../../waf/latest/developerguide/waf-bot-control.md") for common bots. Provides controls to<br>block, challenge, or allow unverified bots while identifying and<br>distinguishing verified bots like search engines.     |            |            | Yes<br>Yes | Yes<br>Yes |
| **Custom WAF response**<br>Set a specific HTTP status code and optional custom HTML,<br>plain text, or JSON response when requests are blocked by a<br>rule.                                                                                                                                                                                                                       |            | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Header Insertion**<br>Add custom HTTP headers to requests that pass WAF inspection,<br>enabling downstream applications to process requests differently<br>or flag them for analysis.                                                                                                                                                                                            | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Request body inspection**<br>Maximum size of HTTP request body content that can be<br>inspected by AWS WAF for threats and malicious patterns.                                                                                                                                                                                                                                   | 16 KB      | 16 KB      | 64 KB      | 64 KB      |
| **Private origins within VPC**<br>Enhance security by keeping your application in a VPC private<br>subnet, accessible only through your CloudFront distributions<br>and hidden from the public internet, using [VPC<br>origins](private-content-vpc-origins.md "private-content-vpc-origins.md").                                                                                  |            |            | Yes<br>Yes | Yes<br>Yes |
| **Origin Access Control (OAC)**<br>Maintain a private S3 bucket and only allow access through<br>your designated CloudFront distribution, ensuring your content is<br>protected by your WAF rules, rate limits, and other security<br>controls configured in your CloudFront distribution.                                                                                         | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Free TLS certificate**<br>Free TLS certificate for your domain with automatic renewal<br>through AWS Certificate Manager.                                                                                                                                                                                                                                                        | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Signed URLs**<br>Create secure URLs that provide temporary access to private<br>content for specific users. Commonly used to share private<br>documents with authorized users or grant secure access to<br>protected content after payment verification.                                                                                                                         | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Edge<br>Compute**                                                                                                                                                                                                                                                                                                                                                                |            |            |            |            |
| **Serverless edge compute**<br>Run lightweight JavaScript at the edge to modify URLs, HTTP<br>headers, and request/response elements in milliseconds using<br>[CloudFront<br>Functions](cloudfront-functions.md "cloudfront-functions.md").                                                                                                                                        | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Edge key-value store**<br>Store data at the edge using [KeyValueStore](kvs-with-functions.md "kvs-with-functions.md") for fast<br>and dynamic content customization with CloudFront Functions.                                                                                                                                                                                   |            | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Network and<br>Protocol Support**                                                                                                                                                                                                                                                                                                                                                |            |            |            |            |
| **IPv6**<br>Deliver content over both modern IPv6 and traditional IPv4<br>connections from CloudFront to viewers and origins. Enables end-to-end<br>IPv6 support for your applications.                                                                                                                                                                                            | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **HTTP/2**<br>Enable faster page loads through modern protocol features like<br>multiplexing, header compression, and stream prioritization.<br>Automatically used when supported by browsers and<br>clients.                                                                                                                                                                      | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **HTTP/3**<br>Deliver content using QUIC to browsers and clients that<br>support it, enabling faster connections and improved<br>performance. Particularly benefits mobile users and maintains<br>connections when network conditions change.                                                                                                                                      | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **TLS 1.3**<br>Deliver faster HTTPS connections through a handshake process<br>that requires one round-trip compared to two in TLS 1.2. Reduces<br>first byte latency by up to 33% compared to previous TLS<br>versions.                                                                                                                                                           | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **WebSockets**<br>Enable real-time, persistent two-way communication between<br>browsers and servers. Ideal for AI chat applications,<br>multi-player gaming, collaborative workspaces, and real-time<br>data feeds like financial trading platforms.                                                                                                                              | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Logging and<br>Monitoring**                                                                                                                                                                                                                                                                                                                                                      |            |            |            |            |
| **Access Logs**<br>Access detailed CloudFront [request logs](standard-logs-reference.md "standard-logs-reference.md") to<br>understand security and delivery traffic patterns, with Amazon CloudWatch<br>Logs ingestion is included at no extra cost.                                                                                                                              |            | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **WAF request logs**<br>Access detailed AWS WAF request logs to understand security and<br>delivery traffic patterns. Amazon CloudWatch Logs ingestion is included<br>at no extra cost.                                                                                                                                                                                            |            | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Security dashboard**<br>Monitor security events, investigate threats, and take<br>immediate blocking actions using visual analytics without<br>writing security rules. Pro and above includes visual log<br>analyzer to quickly understand traffic patterns without querying<br>logs.                                                                                            | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **DNS**                                                                                                                                                                                                                                                                                                                                                                            |            |            |            |            |
| **Amazon Route 53 DNS**<br>Fast, reliable public authoritative DNS service using<br>Route 53.                                                                                                                                                                                                                                                                                      | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Records per Hosted Zone**<br>The maximum number of DNS records allowed in the hosted<br>zone.                                                                                                                                                                                                                                                                                    | 50         | 100        | 1000       | 5000       |
| **DNSSEC**<br>Protect your domain against DNS spoofing and man-in-the-middle<br>attacks where attackers intercept DNS queries and redirect<br>visitors to fake websites. Secures DNS traffic by<br>cryptographically signing your DNS records.                                                                                                                                     | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Storage**                                                                                                                                                                                                                                                                                                                                                                        |            |            |            |            |
| **Amazon S3 storage**<br>Amazon S3 storage credits that offset any S3 Standard storage costs<br>in your AWS account. Not limited to CloudFront content or subject to<br>plan usage allowances.                                                                                                                                                                                     | 5 GB       | 50 GB      | 1 TB       | 5 TB       |
| **Support and<br>Reliability**                                                                                                                                                                                                                                                                                                                                                     |            |            |            |            |
| **24x7 account and billing support**<br>One-on-one responses to account and billing questions. If you have a paid support<br>plans, you're eligible to receive support on all flat-rate<br>plans.                                                                                                                                                                                  | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Documentation and AWS Support forums**<br>Access product documentation, technical papers, best practices<br>guides, AWS re:Post community forums, and service health<br>information to help plan and troubleshoot.                                                                                                                                                               | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes | Yes<br>Yes |
| **Uptime SLA**<br>Service Level Agreements (SLA) for Amazon CloudFront, AWS WAF, Amazon Route 53,<br>and Amazon CloudWatch provide service availability commitments. In the<br>event AWS does not meet the associated SLA's commitment, you<br>will be eligible to receive a service credit.                                                                                       |            |            | Yes<br>Yes | Yes<br>Yes |

## Monthly usage allowances

Each flat-rate plan includes a monthly usage allowance designed for optimal
performance at that tier. You can track your usage allowance in the CloudFront console at any
time. You will also receive automatic email notifications when you reach 50%, 80%, and
100% of your allowance.

If you exceed your allowance, you will not incur any overage charges. This allows you
to operate your application without worrying about costs from unexpected traffic spikes
or attacks. If you outgrow your plan, upgrade to the next tier to access more features
and increase your monthly usage allowance. If your usage exceeds the allowances in your
CloudFront flat-rate pricing plan, AWS may take appropriate action, which may include
reducing your performance (for example, throttling) or requiring a change to your
pricing structure.

| Monthly usage allowances per plan tier |        | Free  | Pro   | Business | Premium |
| -------------------------------------- | ------ | ----- | ----- | -------- | ------- |
| Requests                               | 1 M    | 10 M  | 125 M | 500 M    |
| Data transfer                          | 100 GB | 50 TB | 50 TB | 50 TB    |

###### Note

Blocked DDoS attacks and requests blocked by AWS WAF never count against your usage
allowance.

### Eligibility based on historical usage

Your historical CloudFront usage may affect your eligibility to sign up for or
downgrade to specific plan tiers. If your recent usage exceeds a plan tier's usage
allowances, you may need to select a higher tier that better aligns with your
workload.

## Costs covered by your plan

Your plan covers costs for:

- Your CloudFront distribution
- The AWS WAF web ACL associated with your distribution
- CloudWatch Logs ingestion for your distribution's CloudFront access logs and
  associated WAF logs
- The Route 53 hosted zone, DNS records, and DNS queries when attached to your
  distribution's plan

You will also receive S3 credits to offset S3 Standard storage usage in your payer
account, whether or not an S3 bucket is used as an origin for your CloudFront
distribution.

### Route 53 DNS management and your plan

If you use Route 53 for DNS and attach the zone to your plan, your flat-rate plan
can include your Route 53 hosted zone costs. You can attach the zone to your plan in
the **Manage Plan** section of your CloudFront
distribution. When your zone is attached to the plan, your plan covers your hosted
zone's standard costs, including the monthly hosted zone fee, DNS records, and DNS
query fees subject to respective allowances per tier, provided below. The hosted
zone must meet the following requirements:

- Exist in the same AWS account as your CloudFront distribution
- Maintain the number of records allowed per hosted zone for your plan
  tier
- Cover the domain used by your CloudFront distribution

#### Understanding

monthly DNS query allowances

When your hosted zone is attached to your plan, you get:

1. DNS queries to ALIAS records pointing to your CloudFront distribution
   and [other supported
   AWS services](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/")
2. An additional monthly allowance for other DNS record types

|                                                                                                                                                                              | Free     | Pro      | Business | Premium  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------- | -------- | -------- |
| DNS queries to ALIAS records (CloudFront and [other supported<br>AWS services](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/")) per month | No limit | No limit | No limit | No limit |
| Additional DNS query allowance per month                                                                                                                                     | 1 M      | 5 M      | 20 M     | 100 M    |

###### Note

To maximize your plan benefits, use ALIAS records to point to your CloudFront
distribution. ALIAS records pointing to CloudFront and [other supported AWS services](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/") don't count
against your monthly DNS query allowance. All other DNS queries, including CNAME
records to CloudFront, count against your DNS query allowance.

#### Exceeding DNS query

allowances

If your DNS query usage exceeds your plan's monthly allowance, AWS may
notify you. At that point, you can detach your hosted zone from the plan in the
**Manage Plan** section of your CloudFront
distribution to return the hosted zone to pay-as-you-go pricing. If you do not
detach your hosted zone after receiving this notification, AWS may
automatically transition the hosted zone to pay-as-you-go pricing. When a hosted
zone moves to pay-as-you-go pricing, you are responsible for all standard Route
53 costs. Your CloudFront distribution and all other plan benefits continue
unchanged.

## Reduce overall AWS costs with pricing

plans

CloudFront flat-rate pricing plans can reduce your overall AWS costs in three ways:

First, data transfer costs between CloudFront and your AWS applications running on
services such as Amazon S3, AWS Application Load Balancer (ALB), or Amazon API Gateway
are automatically waived. When you serve your AWS applications through CloudFront
instead of directly to the internet, your flat-rate plan covers the data transfer costs
between your applications and your viewers for a simple monthly price without the worry
of overages.

Second, CloudFront reduces your compute and database costs by protecting your
application infrastructure and reducing the number of requests reaching your origin. It
serves cached content from edge locations or regional edge caches, collapses duplicate
requests, and blocks malicious and unwanted traffic before it reaches your backend
services. This means fewer requests hitting your application servers, databases, and
other AWS services that charge based on usage, which reduces your costs.

Finally, each plan includes Amazon S3 Standard storage credits to offset storage usage
for your AWS account.

To maximize these savings, configure your AWS origins to only accept traffic from
CloudFront. For S3, use [Origin Access
Control OAC](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md") with private buckets to grant access to your designated CloudFront
distribution. For Application Load Balancer, Network Load Balancer, and Amazon EC2 instances
in private subnets, [restrict access to your
designated CloudFront distribution using VPC Origins](private-content-vpc-origins.md "private-content-vpc-origins.md").

## Manage your flat-rate pricing plans

Follow these procedures in the CloudFront console to subscribe, upgrade, downgrade, or
cancel a pricing plan for your distributions.

### Subscribe a new distribution to a pricing

plan

When you create a new distribution, you can subscribe to a pricing plan.

###### To subscribe a new distribution to a pricing plan

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, then
   follow the steps to create a distribution.
3. Choose your distribution's pricing plan. Note that some features are not
   available per pricing plan tier. Review the features per plan and choose the
   pricing plan that you need for your application.
4. Complete the steps to [create your distribution](distribution-web-creating-console.md "distribution-web-creating-console.md").

### Subscribe an existing distribution to

a pricing plan

When you update a distribution, you can subscribe to a pricing plan. Before
choosing a pricing plan, ensure that your distribution configuration is compatible
with the plan that you want.

###### Tip

If your current distribution uses any [unsupported features](#pricing-plan-unsupported-features "#pricing-plan-unsupported-features"), you
must disable those features before you can subscribe to the pricing plan. This
includes disabling features like Lambda@Edge or real-time access logs.

Once your distribution configuration is compatible, you can choose your desired
pricing plan while update a distribution.

###### To subscribe an existing distribution to a pricing plan

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, then
   follow the steps to update an existing distribution.
3. Choose your distribution's pricing plan. Note that some features are not
   available per pricing plan tier. Review the features per plan and choose the
   pricing plan that you need for your application.
4. Complete the steps to [update your
   distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").

### Upgrade a pricing plan

We recommend that you upgrade a plan if you're approaching or have exceeded your
monthly usage allowance, or if you want to enable a feature that is available in the
next tier.

When you upgrade to a higher plan tier, changes take effect immediately. Your
price and usage allowance are prorated. Your distribution and associated resources
will have access to the available features and higher usage allowance of your new
plan.

###### To upgrade a pricing plan

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**.
3. Choose your distribution that is subscribed to an existing pricing
   plan.
4. Follow the prompts to upgrade your distribution's pricing plan.
5. Complete the steps to [update an
   existing distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").

### Downgrade a pricing plan

We recommend that you downgrade to a lower plan tier if you don't need the
additional features on your existing tier. For example, you might downgrade if you
expect your application will experience lower traffic.

If you downgrade to a lower tier, your billing changes will take effect at the
beginning of the next billing cycle.

If your distribution currently exceeds the usage allowance for a plan, you can
downgrade once your usage is within the usage allowance for your desired tier. To
avoid being charged for your existing plan tier at the next billing cycle, downgrade
before the end of the month.

###### To downgrade a pricing plan

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**.
3. Choose your distribution that is subscribed to an existing pricing
   plan.
4. Follow the prompts to downgrade your distribution's pricing plan. If you
   have unsupported features, you must either remove the feature or resource
   from the distribution.
5. Complete the steps to [update an
   existing distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").

### Cancel a pricing plan

When you cancel a pricing plan, you will maintain your flat-rate price through the
end of your current billing cycle. Your distribution and all associated plan
resources will then switch to pay-as-you-go pricing at the start of the next billing cycle.

###### To cancel a pricing plan

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**.
3. Choose your distribution that is subscribed to an existing pricing
   plan.
4. Follow the prompts to cancel your distribution's pricing plan. If you have
   unsupported features, you must either remove the feature or resource from
   the distribution.
5. Complete the steps to [update an
   existing distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").

### Cancel a pending plan change

If you downgraded or canceled your flat-rate pricing plan, you must wait until the
end of the current billing cycle before your changes are in effect. To keep your
existing flat-rate pricing plan, upgrade, or downgrade your pricing plan again, you
must first cancel your pending plan change.

###### To cancel a pending pricing plan change

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**.
3. Choose your distribution that is subscribed to an existing pricing
   plan.
4. Follow the prompts to cancel your distribution's pending plan
   change.
5. Choose the pricing plan that you want for your distribution.
6. Complete the steps to update an existing distribution.

### Deleting a distribution with a pricing

plan

You can't delete a distribution that is subscribed to a pricing plan. You must
first cancel the pricing plan and then after the current billing cycle, delete the
distribution.

###### To delete a distribution with a pricing plan

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**.
3. Follow the previous steps to cancel the distribution's pricing
   plan.
4. Follow the steps to [delete the
   distribution](HowToDeleteDistribution.md "HowToDeleteDistribution.md").

###### Note

You can disable a distribution that is subscribed to a pricing plan, but you
will still incur charges for that plan. To stop incurring charges for your plan,
you must first cancel it.

## Permissions

To view or manage pricing plan subscriptions for your CloudFront distributions, you must
have the required permissions. For more information, see [AWS managed policy:
CloudFrontFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-cloudfront-full-access "security-iam-awsmanpol.md#security-iam-awsmanpol-cloudfront-full-access") and [AWS managed policy:
CloudFrontReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-cloudfront-read-only "security-iam-awsmanpol.md#security-iam-awsmanpol-cloudfront-read-only").

## Flat-rate pricing plan quotas

The following table shows the quotas and restrictions for CloudFront flat-rate pricing
plans.

###### Note

These quotas can't be increased for your AWS account.

| Account-level quotas          | Quotas |
| ----------------------------- | ------ |
| Pricing plans per AWS account | 100    |
| Free plans per AWS account    | 3      |
| Apex-level domains per plan   | 1      |

## Unsupported features

Before you can associate a distribution with a pricing plan, you must ensure that
certain features are disabled and associations are removed.

###### Notes

- If your distribution or account has any of these restrictions, you must
  resolve them before you can use pricing plans. After you make changes to
  your distribution, wait for the changes to propagate to all edge
  locations.
- You must have a AWS WAF Web ACL associated with your distribution if you're
  using a pricing plan. This resource cannot be removed or disassociated from
  your distribution unless you switch to pay-as-you-go pricing for that distribution.

### Unsupported features

You can't subscribe distributions to a pricing plan if their configuration
contains the following unsupported features. You can disable the unsupported feature
and use an alternative option, or keep pay-as-you-go for your distribution.

| Unsupported features                                                                                                                                                                                                                                                                  | Alternative options                                                                                                                                                                                                                                                                                | AWS service |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [Multi-tenant<br>distributions](distribution-config-options.md "distribution-config-options.md")                                                                                                                                                                                      | Use a [standard<br>distribution](Introduction.md#choose-standard-or-multi-tenant "Introduction.md#choose-standard-or-multi-tenant") or pay-as-you-go pricing                                                                                                                                       | CloudFront  |
| [Continuous<br>deployment](continuous-deployment.md "continuous-deployment.md") and [Staging<br>distributions](understanding-continuous-deployment.md#updating-staging-and-primary-distributions "understanding-continuous-deployment.md#updating-staging-and-primary-distributions") | Use pay-as-you-go pricing                                                                                                                                                                                                                                                                          | CloudFront  |
| [Anycast IP list](request-static-ips.md "request-static-ips.md")<br>configuration                                                                                                                                                                                                     | Use pay-as-you-go pricing                                                                                                                                                                                                                                                                          | CloudFront  |
| [Real-time access<br>logs](real-time-logs.md "real-time-logs.md")                                                                                                                                                                                                                     | Use [standard<br>access logs](DownloadDistValuesGeneral.md#DownloadDistValuesLoggingOnOff "DownloadDistValuesGeneral.md#DownloadDistValuesLoggingOnOff") or pay-as-you-go pricing                                                                                                                  | CloudFront  |
| [Lambda@Edge<br>functions](lambda-at-the-edge.md "lambda-at-the-edge.md")                                                                                                                                                                                                             | Use [CloudFront Functions or<br>pay-as-you-go pricing](cloudfront-functions.md "cloudfront-functions.md")                                                                                                                                                                                          | CloudFront  |
| Targeted Bots                                                                                                                                                                                                                                                                         | Use common bots or pay-as-you-go pricing                                                                                                                                                                                                                                                           | AWS WAF     |
| CAPTCHA                                                                                                                                                                                                                                                                               | Use challenge or pay-as-you-go pricing                                                                                                                                                                                                                                                             | AWS WAF     |
| Partner Managed Rules                                                                                                                                                                                                                                                                 | Use pay-as-you-go pricing                                                                                                                                                                                                                                                                          | AWS WAF     |
| Account Creation Fraud Prevention                                                                                                                                                                                                                                                     | Use pay-as-you-go pricing                                                                                                                                                                                                                                                                          | AWS WAF     |
| Account Takeover Protection                                                                                                                                                                                                                                                           | Use pay-as-you-go pricing                                                                                                                                                                                                                                                                          | AWS WAF     |
| Rule Groups                                                                                                                                                                                                                                                                           | Create individual rules (rule groups are shared AWS WAF rules<br>that can be applied to a web ACL, similar to policies on<br>CloudFront)                                                                                                                                                           | AWS WAF     |
| **Legacy features**                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                    |
| [ForwardedValues](../../../cloudfront/latest/APIReference/API_ForwardedValues.md "../../../cloudfront/latest/APIReference/API_ForwardedValues.md")<br>configuration                                                                                                                   | Use [Origin request<br>policies](controlling-origin-requests.md "controlling-origin-requests.md")                                                                                                                                                                                                  | CloudFront  |
| [Dedicated IP/SSL](cnames-and-https-switch-dedicated-to-sni.md "cnames-and-https-switch-dedicated-to-sni.md")                                                                                                                                                                         | Use pay-as-you-go pricing                                                                                                                                                                                                                                                                          | CloudFront  |
| [Field level<br>encryption](field-level-encryption.md "field-level-encryption.md")                                                                                                                                                                                                    | Use pay-as-you-go pricing                                                                                                                                                                                                                                                                          | CloudFront  |
| [AWS Identity and Access Management (IAM) server certificates](../../../IAM/latest/UserGuide/id_credentials_server-certs.md "../../../IAM/latest/UserGuide/id_credentials_server-certs.md")                                                                                           | Use AWS Certificate Manager (ACM) certificates                                                                                                                                                                                                                                                     | CloudFront  |
| [Origin access identity<br>(OAI)](private-content-restricting-access-to-s3.md#migrate-from-oai-to-oac "private-content-restricting-access-to-s3.md#migrate-from-oai-to-oac")                                                                                                          | Use [Origin access control (OAC)](private-content-restricting-access-to-origin.md "private-content-restricting-access-to-origin.md")                                                                                                                                                               | CloudFront  |
| Legacy cache settings                                                                                                                                                                                                                                                                 | Use [cache<br>policies](cache-key-understand-cache-policy.md "cache-key-understand-cache-policy.md") and [origin request policies](understanding-how-origin-request-policies-and-cache-policies-work-together.md "understanding-how-origin-request-policies-and-cache-policies-work-together.md"). | CloudFront  |

### Unsupported

associations

You can't subscribe a distribution to a pricing plan if the distribution is
already associated with any of the following resources that are _already
associated_ with other distributions. Resources that are associated to
a distribution that is subscribed to a pricing plan can only be used for that
distribution. For example, if you have a CloudFront function that is using a key value
store, neither the function nor the key value store can be shared for a distribution
that is on a pricing plan.

- CloudFront Functions
- CloudFront Functions associated with a key value store
- AWS WAF Web ACLs

To subscribe a distribution to a pricing plan, either remove the associated
resource or replace it with another one.

### Account-level constraints

AWS accounts are not eligible for pricing plans if they meet any of the
following conditions:

- You reached the maximum number of subscriptions allowed. See [Flat-rate pricing plan quotas](#pricing-plan-quotas "#pricing-plan-quotas").
- Your account is using AWS Free Tier.

### Resource-level constraints

Distributions are not eligible for pricing plans if they meet any of the following
conditions:

- Your distribution has enabled AWS Shield Advanced
- Your distribution has enabled the [Firewall Manager Service](../../../waf/latest/developerguide/fms-chapter.md "../../../waf/latest/developerguide/fms-chapter.md") for your web ACL. Firewall Manager won't manage
  your CloudFront distribution's WebACL in a pricing plan.

### Additional features that can affect

your pricing plan

Flat-rate pricing plans enable you to pay a flat-rate for your CloudFront
distribution and the features listed above that are both included in your plan and
associated with your CloudFront distribution. All other features may incur
additional charges, including but not limited to the following:

###### Route 53

- Route 53 DNSSEC has an AWS KMS cost
- Route 53 IP (CIDR) blocks (the first 1,000 are free per AWS account)
- Route 53 Health Checks (the first 50 are free per AWS account)

###### Logging features

- Route 53 DNS Query Logs, CloudFront Functions logs, and CloudFront Connection Function
  Logs
- AWS WAF log delivery to Amazon S3
- CloudFront or AWS WAF log delivery to Amazon Data Firehose
- Additional CloudWatch metrics for CloudFront
- CloudFront access logs in Parquet format

###### Note

Your plan includes Amazon CloudWatch Logs ingestion for CloudFront standard logs (access
logs) and WAF logs for no added costs. All other CloudWatch costs such as
storage and querying are not covered by your plan. All other logs are also
billed separately.

###### Note

Your plan includes public authoritative DNS from Route 53. When your Route 53
hosted zone is attached to your pricing plan, your plan covers your hosted
zone's standard costs, including the monthly hosted zone fee, DNS records, and
DNS query fees subject to respective allowances per tier. All other costs from
Route 53 usage and features not listed above as included in your plan are not
covered by your plan.

### Pricing plans vs. pay-as-you-go

pricing

Flat-rate plans and pay-as-you-go pricing offer different advantages based on your
needs. With flat-rate plans, you pay one price that includes multiple AWS services
like CloudFront, AWS WAF, Route 53, and CloudWatch Logs ingestion and never face
overage charges, even during traffic spikes or attacks.

With pay-as-you-go pricing, you're billed separately for each service and feature
based on your actual usage. While this provides complete flexibility in service
selection and configuration, your costs can vary month to month based on traffic
patterns, and you will need to monitor usage across multiple services to manage
costs.

Flat-rate plans are ideal if you want combined monthly billing, simplified service
configuration, and built-in security features without worrying about overage
charges. Pay-as-you-go pricing is a better choice if you need complete control over
individual service features, custom configurations, access to features not available
in flat-rate plans, or if you expect to handle large, predictable traffic spikes.
Amazon CloudFront flat-rate pricing plans may not be combined with any other offers,
promotions, or discounts.
