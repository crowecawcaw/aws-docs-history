

# CloudFront flat-rate pricing plans
<a name="flat-rate-pricing-plan"></a>

CloudFront flat-rate pricing plans combine the Amazon CloudFront global content delivery network (CDN) with multiple AWS services and features into a monthly price with no overage charges, regardless of traffic spikes or attacks.

Flat-rate pricing plans include the following features for a simple monthly price:
+ CloudFront CDN
+ AWS WAF and DDoS protection
+ Bot management and analytics
+ Amazon Route 53 DNS
+ Amazon CloudWatch Logs ingestion
+ TLS certificate
+ Serverless edge compute
+ Amazon S3 storage credits each month

Plans are available in Free, Pro, Business, and Premium tiers to match your application's needs. Plans don't require an annual commitment to get the best available rates. Start with the Free plan and upgrade to access more capabilities and larger usage allowances.

**Topics**
+ [Benefits of CloudFront flat-rate pricing plans](#pricing-plan-benefits)
+ [Features by pricing plan tier](#pricing-plan-features)
+ [Monthly usage allowances](#usage-allowance)
+ [Costs covered by your plan](#costs-covered-by-plan)
+ [Reduce overall AWS costs with pricing plans](#pricing-plan-vs-payg)
+ [Manage your flat-rate pricing plans](#manage-your-pricing-plans)
+ [Permissions](#prerequisites-pricing-plan)
+ [Flat-rate pricing plan quotas](#pricing-plan-quotas)
+ [Unsupported features](#pricing-plan-unsupported-features)

## Benefits of CloudFront flat-rate pricing plans
<a name="pricing-plan-benefits"></a>

The CloudFront pricing plan provides several key benefits:
+  **Consolidated services and pricing** 

  Combine multiple AWS services and features into a single plan for one flat rate. Designed to eliminate separate service purchases and upfront pricing calculations.
+  **No overages** 

  There are no overage charges regardless of traffic spikes or attacks.
+  **Clear usage allowances** 

  Each plan includes published usage allowances designed for optimal performance at that tier. Monitor your usage, receive proactive notifications, and upgrade based on your application's needs, with no long-term commitments.
+  **Protect against DDoS attacks** 

  CloudFront and AWS WAF absorb and block attacks before they reach your infrastructure. Reserves your compute, database, and infrastructure utilization only for legitimate traffic. Blocked DDoS attacks and requests blocked by AWS WAF never count against your usage allowance.
+  **Reduce your overall AWS costs** 

  Data transfer from AWS applications running on services such as Amazon S3, AWS Application Load Balancer (ALB), or Amazon API Gateway to CloudFront continues to be free. When you serve your AWS applications through CloudFront instead of directly to the internet, your flat-rate plan covers the data transfer costs between your applications and your viewers for a simple monthly price without the worry of overages. Fewer requests reaching your origin also reduces your costs on services that charge based on usage. 

## Features by pricing plan tier
<a name="pricing-plan-features"></a>

Each pricing plan covers one CloudFront distribution with up to one apex (root) domain that combines essential features and services into one monthly price. Each plan also includes additional S3 storage credits. 

Plans on higher tiers include all features from lower tier plans as well as additional features.
+ **Free** – For hobbyists, learners, and developers getting started.
+ **Pro** – Launch and grow small websites, blogs, and applications.
+ **Business** – Protect and accelerate business applications.
+ **Premium** – Scale and protect business and mission-critical applications.

Select a plan tier that includes features and configurations that you need for your applications. See the following features per pricing plan.

### Pricing plan features
<a name="combined-pricing-plan-features"></a>

The following table shows the CloudFront, AWS WAF and DDoS, Amazon Route 53, Amazon CloudWatch, and Amazon S3 features included in each pricing plan tier.


| Performance and Delivery | Free | Pro | Business | Premium | 
| --- |--- |--- |--- |--- |
|  **Global CDN** <br />Use CloudFront's 750\+ global edge locations as a massive, distributed, single point of entry for your web application. Accelerate static, dynamic, and non-cacheable applications. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Content caching** <br />Store copies of your content in CloudFront's 750\+ edge locations worldwide, delivering it to users from the nearest location. Reduces load times, protects your application from traffic spikes, and saves costs by serving repeated requests locally instead of from your application servers. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Fast cache invalidations** <br />Remove or update cached content across all edge locations within seconds. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Invalidations by cache tag** <br />Assign custom tags to your content and remove all cached content sharing a specific tag, without tracking individual file paths. |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Smart routing** <br />Intelligently routes users to the optimal edge location using real-time network data, and connects to your AWS origin through the AWS private network for better performance. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Tiered caching** <br />[Regional edge caches](HowCloudFrontWorks.md#CloudFrontRegionaledgecaches) sit between edge locations and your application to store content longer, reducing load on your application and maintaining fast delivery. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Default caching rules** <br />Makes effective caching decisions to cache most web applications without custom configuration. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Custom caching rules** <br />Control how CloudFront caches content by specifying which request values to use, optimizing for your application's performance, personalization, and freshness needs using [cache policies](controlling-the-cache-key.md). |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **High-speed origin routing** <br />With [Origin Shield](origin-shield.md), dynamic requests are routed from edge locations to your origin using CloudFront's private network for high-performance path to your origin. |  |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Origin load reduction** <br />Adds an additional caching layer close to your web application using [Origin Shield](origin-shield.md). Origin Shield consolidates requests from all edge locations, reducing load on your application particularly during traffic spikes. |  |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Automatic origin failover** <br />Automatically routes traffic to a backup origin if your primary origin fails, [maintaining high availability](high_availability_origin_failover.md) without disrupting users. |  |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Default origin request rules** <br />Control which information from viewer requests is automatically included in requests to your origin, using [AWS managed origin request policies](using-managed-origin-request-policies.md) optimized for common scenarios. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Default response header rules** <br />Use [AWS managed response header policies](using-managed-response-headers-policies.md) to add or remove HTTP headers in responses to viewers, preconfigured for common security headers, CORS settings, and other standard use cases. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Custom origin request rules** <br />Create your own [origin request policies](controlling-origin-requests.md) to specify exactly which URL query strings, headers, and cookies are forwarded to your origin, enabling custom analytics and request handling. |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Custom response header rules** <br />Create your own [response header policies](modifying-response-headers.md) to control exactly which HTTP headers CloudFront adds or removes in responses to viewers, such as security headers, Content Security Policy (CSP), CORS settings, and custom application headers. |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Number of cache behaviors** <br />Configure [cache behaviors](DownloadDistValuesCacheBehavior.md) to control how CloudFront handles requests for specific URL patterns, including which origin serves the content, how content is cached, and whether HTTPS or signed URLs are required. | 5 | 10 | 50 | 100 | 
| **Security and Protection** |  |  |  |  | 
| --- |--- |--- |--- |--- |
|  **Always-on DDoS protection** <br />Protect against DDoS attacks that target your websites or applications. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Advanced DDoS Protection** <br />Identify and block DDoS attacks in seconds using the [AntiDDoS AMR](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.html). AWS learns your unique application patterns to distinguish between attacks and natural surges from legitimate users. |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Web Application Firewall (WAF)** <br />Protect against common application vulnerabilities and potential threats based on Amazon internal threat intelligence. Requests are blocked before reaching your servers. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Number of WAF rules** <br />Total number of security rules you can create and enable in your WAF configuration, including both custom rules and AWS Managed Rules. | 5 | 25 | 50 | 75 | 
|  **Protections for WordPress, PHP, and SQL databases** <br />Use-case based security rules to protect common applications and operating systems like WordPress, PHP, SQL databases, Linux, and Windows. |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **AI traffic analytics** <br />Monitor access patterns, request volumes, and popular paths of AI bots interacting with your content. AI bots are classified based on intent to detect activities like potentially unauthorized scraping used for training. |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **IP-based rate limiting** <br />Automatically block IP addresses that exceed a configurable number of requests over a 5-minute period, protecting against HTTP flood attacks and Denial of Service (DoS) attempts. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Geographic traffic blocking** <br />Block requests from selected countries or regions. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **CAPTCHA challenge** <br />Require requests matching specific security rules to solve a CAPTCHA puzzle to prove that a human being is sending the request. |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Header-based threat filtering** <br />Create WAF security rules that filter threats based on HTTP request headers. |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Regex-based threat filtering** <br />Create WAF security rules using regular expressions to match URI paths and HTTP request attributes. |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **JavaScript challenge** <br />Block automated threats by requiring browsers to complete JavaScript challenges that verify legitimate users. |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Bot management and analytics (\+AI bots)** <br />Detect and analyze bot traffic with [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html) for common bots. Provides controls to block, challenge, or allow unverified bots while identifying and distinguishing verified bots like search engines. Monitor AI bots and take action based on bot intent. |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Custom WAF response** <br />Set a specific HTTP status code and optional custom HTML, plain text, or JSON response when requests are blocked by a rule. |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Header Insertion** <br />Add custom HTTP headers to requests that pass WAF inspection, enabling downstream applications to process requests differently or flag them for analysis. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Request body inspection** <br />Maximum size of HTTP request body content that can be inspected by AWS WAF for threats and malicious patterns. | 16 KB | 16 KB | 64 KB | 64 KB | 
|  **Private origins within VPC** <br />Enhance security by keeping your application in a VPC private subnet, accessible only through your CloudFront distributions and hidden from the public internet, using [VPC origins](private-content-vpc-origins.md). |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Mutual TLS (origin)** <br />Restrict unauthorized access to your application (origin) using TLS-based client certificates, ensuring only your authorized CloudFront distributions can establish connections to your application. |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Origin Access Control (OAC)** <br />Maintain a private S3 bucket and only allow access through your designated CloudFront distribution, ensuring your content is protected by your WAF rules, rate limits, and other security controls configured in your CloudFront distribution. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Free TLS certificate** <br />Free TLS certificate for your domain with automatic renewal through AWS Certificate Manager. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Signed URLs** <br />Create secure URLs that provide temporary access to private content for specific users. Commonly used to share private documents with authorized users or grant secure access to protected content after payment verification. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Mutual TLS (mTLS)** <br />Restrict access to your application using mTLS authentication, ensuring only trusted clients with valid certificates can connect. |  |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
| **Edge Compute** |  |  |  |  | 
| --- |--- |--- |--- |--- |
|  **Serverless edge compute** <br />Run lightweight JavaScript at the edge to modify URLs, HTTP headers, and request/response elements in milliseconds using [CloudFront Functions](cloudfront-functions.md). Lambda@Edge can also be used with all plan tiers, but unlike CloudFront Functions, Lambda@Edge invocations are billed on a pay-as-you-go basis. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Edge key-value store** <br />Store data at the edge using [KeyValueStore](kvs-with-functions.md) for fast and dynamic content customization with CloudFront Functions. |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
| **Network and Protocol Support** |  |  |  |  | 
| --- |--- |--- |--- |--- |
|  **IPv6** <br />Deliver content over both modern IPv6 and traditional IPv4 connections from CloudFront to viewers and origins. Enables end-to-end IPv6 support for your applications. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **HTTP/2** <br />Enable faster page loads through modern protocol features like multiplexing, header compression, and stream prioritization. Automatically used when supported by browsers and clients. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **HTTP/3** <br />Deliver content using QUIC to browsers and clients that support it, enabling faster connections and improved performance. Particularly benefits mobile users and maintains connections when network conditions change. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **TLS 1.3** <br />Deliver faster HTTPS connections through a handshake process that requires one round-trip compared to two in TLS 1.2. Reduces first byte latency by up to 33% compared to previous TLS versions. Enabled end-to-end for your applications. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **WebSockets** <br />Enable real-time, persistent two-way communication between browsers and servers. Ideal for AI chat applications, multi-player gaming, collaborative workspaces, and real-time data feeds like financial trading platforms. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
| **Logging and Monitoring** |  |  |  |  | 
| --- |--- |--- |--- |--- |
|  **Access Logs** <br />Access detailed CloudFront [request logs](standard-logs-reference.md) to understand security and delivery traffic patterns, with Amazon CloudWatch Logs ingestion is included at no extra cost. |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **WAF request logs** <br />Access detailed AWS WAF request logs to understand security and delivery traffic patterns. Amazon CloudWatch Logs ingestion is included at no extra cost. |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Security dashboard** <br />Monitor security events, investigate threats, and take immediate blocking actions using visual analytics without writing security rules. Pro and above includes visual log analyzer to quickly understand traffic patterns without querying logs. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
| **DNS** |  |  |  |  | 
| --- |--- |--- |--- |--- |
|  **Amazon Route 53 DNS** <br />Fast, reliable public authoritative DNS service using Route 53. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Records per Hosted Zone** <br />The maximum number of DNS records allowed in the hosted zone. | 50 | 100 | 1000 | 5000 | 
|  **DNSSEC** <br />Protect your domain against DNS spoofing and man-in-the-middle attacks where attackers intercept DNS queries and redirect visitors to fake websites. Secures DNS traffic by cryptographically signing your DNS records. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
| **Storage** |  |  |  |  | 
| --- |--- |--- |--- |--- |
|  **Amazon S3 storage** <br />Amazon S3 storage credits that offset any S3 Standard storage costs in your AWS account. Not limited to CloudFront content or subject to plan usage allowances. | 5 GB | 50 GB | 1 TB | 5 TB | 
| **Support and Reliability** |  |  |  |  | 
| --- |--- |--- |--- |--- |
|  **24x7 account and billing support** <br />One-on-one responses to account and billing questions.<br />If you have a paid support plan, you're eligible to receive support on all flat-rate plans. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Documentation and AWS Support forums** <br />Access product documentation, technical papers, best practices guides, AWS re:Post community forums, and service health information to help you plan and troubleshoot. | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 
|  **Uptime SLA** <br />Service Level Agreements (SLA) for Amazon CloudFront, AWS WAF, Amazon Route 53, and Amazon CloudWatch provide service availability commitments. In the event AWS does not meet the associated SLA's commitment, you will be eligible to receive a service credit. |  |  | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | Yes<br />![Green circle with white checkmark icon.](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/images/icon-yes.png) | 

## Monthly usage allowances
<a name="usage-allowance"></a>

Each flat-rate plan includes a monthly usage allowance designed for optimal performance at that tier. **Usage allowances are not hard limits**—they represent the baseline usage your plan is designed to support. You can track your usage in the CloudFront console at any time and will receive automatic email notifications when you reach 50%, 80%, and 100% of your allowance.


**Monthly usage allowances per plan tier**  

|  | Free | Pro | Business | Premium | 
| --- | --- | --- | --- | --- | 
| Requests | 1 M | 10 M | 125 M | 500 M (configurable up to 6 B for a new flat-rate price) | 
| Data transfer | 100 GB | 50 TB | 50 TB | 50 TB (configurable up to 600 TB for a new flat-rate price) | 

### What counts toward your usage allowance
<a name="what-counts-toward-usage"></a>

 **Blocked DDoS attacks and requests blocked by AWS WAF never count against your usage allowance.** Only traffic that makes it past your AWS WAF security rules counts towards your allowance. This means attacks and unwanted traffic won't count against you, and you maintain the ability to define exactly what traffic your application blocks or allows.

### What happens when usage exceeds the allowance
<a name="usage-exceeds-allowance"></a>

Plans are designed to be flexible and accommodate real-world traffic patterns like traffic variability, organic growth, and viral events. **Most importantly: you will not incur overage charges, regardless of how much you exceed your allowance.** If your usage exceeds your allowance through sustained growth over multiple months or through unusually high usage in a single month, we may adjust how we deliver your traffic. **Most customers never experience performance adjustments.**

Here's how it works:
+  **Your first traffic spike up to 3x your monthly allowance won't affect your service that month.** This one-time accommodation handles unexpected events like viral content or successful product launches without penalizing your success.
+  **Sustained usage above your allowance is evaluated over 2-3 months or more, not immediately.** Minor fluctuations and moderate growth are expected and accommodated. Only substantial, sustained excess usage indicate your application has outgrown your tier.
+  **You'll receive notifications each month as you approach and exceed your allowance.** If your usage consistently and significantly exceeds your plan, we recommend upgrading to a tier that matches your growth and ensures optimal performance as you scale. You control your performance by upgrading when your baseline usage patterns change.
+  **If you continue to substantially exceed your plan's usage allowance without upgrading, we may adjust how we deliver your traffic.** For example, we might serve your traffic from fewer or more distant edge locations or adjust performance. The degree of adjustment is proportional—small excess usage sees minimal changes, larger sustained excess sees more noticeable changes. Upgrading restores full performance.

 **Most customers never experience performance adjustments. Plans are designed to accommodate normal growth patterns.** 

### Configurable usage allowances on the Premium plan
<a name="configurable-usage-allowances"></a>

The Premium plan offers configurable monthly usage allowances per distribution. When you subscribe to or manage a Premium plan, you can select a higher monthly usage allowance from the following levels:


**Premium usage levels**  

| Premium usage level | Monthly data transfer | Monthly requests | Flat-rate price per month | 
| --- | --- | --- | --- | 
| Premium (default) | 50 TB | 500 M | $1,000 | 
| Premium | 75 TB | 750 M | $1,450 | 
| Premium | 125 TB | 1.25 B | $2,250 | 
| Premium | 200 TB | 2 B | $3,500 | 
| Premium | 350 TB | 3.5 B | $6,000 | 
| Premium | 600 TB | 6 B | $10,000 | 

When you select a higher usage level, your monthly price increases and your monthly usage allowance increases accordingly. The features and services included in the Premium plan remain the same at every usage level. You are only changing your usage allowance and flat-rate price. The same usage allowance policies apply at all usage levels. For details, see [What happens when usage exceeds the allowance](#usage-exceeds-allowance).

You can change your usage level at any time in the CloudFront console. When you increase your usage level, changes take effect immediately. Your price and usage allowance are prorated. When you decrease your usage level, the change takes effect at the beginning of the next billing cycle.

If your application's baseline usage exceeds 6 B requests or 600 TB per month, [contact us](https://aws.amazon.com/contact-us/sales-support/?pg=cloudfrontprice/?GLBL-FY25-CloudFrontWebPageInquiry-ContactUs) for custom pricing.

**Note**  
Configurable usage allowances are available only on the Premium plan. Usage allowances on Free, Pro, and Business plans are not configurable.

### Eligibility based on historical usage
<a name="historical-usage"></a>

Your historical CloudFront usage may affect your eligibility to sign up for or downgrade to specific plan tiers. If your recent usage exceeds a plan tier's usage allowances, you may need to select a higher tier that better aligns with your workload.

## Costs covered by your plan
<a name="costs-covered-by-plan"></a>

Your plan covers costs for:
+ Your CloudFront distribution
+ The AWS WAF web ACL, custom rules, AWS Managed Rules, and request fees for the web ACL associated with your distribution
+ CloudWatch Logs ingestion for your distribution's CloudFront access logs and associated WAF logs
+ The Route 53 hosted zone, DNS records, and DNS queries when attached to your distribution's plan

You will also receive S3 credits to offset S3 Standard storage usage in your payer account, whether or not an S3 bucket is used as an origin for your CloudFront distribution.

### Route 53 DNS management and your plan
<a name="route-53-dns-coverage"></a>

If you use Route 53 for DNS and attach the zone to your plan, your flat-rate plan can include your Route 53 hosted zone costs. You can attach the zone to your plan in the **Manage Plan** section of your CloudFront distribution. When your zone is attached to the plan, your plan covers your hosted zone's standard costs, including the monthly hosted zone fee, DNS records, and DNS query fees subject to respective allowances per tier, provided below. The hosted zone must meet the following requirements:
+ Exist in the same AWS account as your CloudFront distribution
+ Maintain the number of records allowed per hosted zone for your plan tier
+ Cover the domain used by your CloudFront distribution

If your hosted zone is not attached to your plan, it will remain on pay-as-you-go pricing, where you're responsible for all standard Route 53 costs.

#### Understanding monthly DNS query allowances
<a name="understanding-monthly-DNS-query-allowances"></a>

When your hosted zone is attached to your plan, you get:

1. DNS queries to ALIAS records pointing to your CloudFront distribution and [other supported AWS services](https://aws.amazon.com/route53/pricing/)

1. An additional monthly allowance for other DNS record types



|  | Free | Pro | Business | Premium | 
| --- | --- | --- | --- | --- | 
| DNS queries to ALIAS records (CloudFront and [other supported AWS services](https://aws.amazon.com/route53/pricing/)) per month | No limit | No limit | No limit | No limit | 
| Additional DNS query allowance per month | 1 M | 5 M | 20 M | 100 M | 

**Note**  
To maximize your plan benefits, use ALIAS records to point to your CloudFront distribution. ALIAS records pointing to CloudFront and [other supported AWS services](https://aws.amazon.com/route53/pricing/) don't count against your monthly DNS query allowance. All other DNS queries, including CNAME records to CloudFront, count against your DNS query allowance.

#### Exceeding DNS query allowances
<a name="exceed-dns-query-allowances"></a>

If your DNS query usage exceeds your plan's monthly allowance, AWS may notify you. At that point, you can detach your hosted zone from the plan in the **Manage Plan** section of your CloudFront distribution to return the hosted zone to pay-as-you-go pricing. If you do not detach your hosted zone after receiving this notification, AWS may automatically transition the hosted zone to pay-as-you-go pricing. When a hosted zone moves to pay-as-you-go pricing, you are responsible for all standard Route 53 costs. Your CloudFront distribution and all other plan benefits continue unchanged.

## Reduce overall AWS costs with pricing plans
<a name="pricing-plan-vs-payg"></a>

CloudFront flat-rate pricing plans can reduce your overall AWS costs in three ways:

First, data transfer costs between CloudFront and your AWS applications running on services such as Amazon S3, AWS Application Load Balancer (ALB), or Amazon API Gateway are automatically waived. When you serve your AWS applications through CloudFront instead of directly to the internet, your flat-rate plan covers the data transfer costs between your applications and your viewers for a simple monthly price without the worry of overages.

Second, CloudFront reduces your compute and database costs by protecting your application infrastructure and reducing the number of requests reaching your origin. It serves cached content from edge locations or regional edge caches, collapses duplicate requests, and blocks malicious and unwanted traffic before it reaches your backend services. This means fewer requests hitting your application servers, databases, and other AWS services that charge based on usage, which reduces your costs.

Finally, each plan includes Amazon S3 Standard storage credits to offset storage usage for your AWS account.

To maximize these savings, configure your AWS origins to only accept traffic from CloudFront. For S3, use [Origin Access Control OAC](private-content-restricting-access-to-s3.md) with private buckets to grant access to your designated CloudFront distribution. For Application Load Balancer, Network Load Balancer, and Amazon EC2 instances in private subnets, [restrict access to your designated CloudFront distribution using VPC Origins](private-content-vpc-origins.md).

## Manage your flat-rate pricing plans
<a name="manage-your-pricing-plans"></a>

You can manage your CloudFront flat-rate pricing plans using the CloudFront console, or programmatically using the AWS Command Line Interface (AWS CLI) or the PricingPlanManager API. This section describes how to subscribe distributions to pricing plans, change plan tiers, and cancel subscriptions using the CloudFront console.

For information about managing pricing plans programmatically, see [Getting started with the PricingPlanManager API](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/plan-management.html).

### Subscribe a new distribution to a pricing plan
<a name="pricing-plan-setup-new"></a>

When you create a new distribution, you can subscribe to a pricing plan.

**To subscribe a new distribution to a pricing plan**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Distributions**, then follow the steps to create a distribution.

1. Choose your distribution's pricing plan. Note that some features are not available per pricing plan tier. Review the features per plan and choose the pricing plan that you need for your application.

1. Complete the steps to [create your distribution](distribution-web-creating-console.md).

### Subscribe an existing distribution to a pricing plan
<a name="pricing-plan-setup-existing"></a>

When you update a distribution, you can subscribe to a pricing plan. Before choosing a pricing plan, ensure that your distribution configuration is compatible with the plan that you want.

**Tip**  
If your current distribution uses any [unsupported features](#pricing-plan-unsupported-features), you must disable those features before you can subscribe to the pricing plan. This includes disabling features like real-time access logs.

Once your distribution configuration is compatible, you can choose your desired pricing plan while update a distribution.

**To subscribe an existing distribution to a pricing plan**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Distributions**, then follow the steps to update an existing distribution.

1. Choose your distribution's pricing plan. Note that some features are not available per pricing plan tier. Review the features per plan and choose the pricing plan that you need for your application.

1. Complete the steps to [update your distribution](HowToUpdateDistribution.md).

### Upgrade a pricing plan
<a name="pricing-plan-upgrade"></a>

We recommend that you upgrade a plan if you're approaching or have exceeded your monthly usage allowance, or if you want to enable a feature that is available in the next tier.

When you upgrade to a higher plan tier, changes take effect immediately. Your price and usage allowance are prorated. Your distribution and associated resources will have access to the available features and higher usage allowance of your new plan.

**To upgrade a pricing plan**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Distributions**.

1. Choose your distribution that is subscribed to an existing pricing plan.

1. Follow the prompts to upgrade your distribution's pricing plan.

1. Complete the steps to [update an existing distribution](HowToUpdateDistribution.md).

### Change your Premium plan usage level
<a name="pricing-plan-change-usage-level"></a>

If you are on the Premium plan, you can change your usage level to increase or decrease your usage allowance.

When you increase your usage level, the change takes effect immediately and your price is prorated. When you decrease your usage level, the change takes effect at the beginning of the next billing cycle.

**To change your Premium plan usage level**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Distributions**.

1. Choose your distribution that is subscribed to a Premium pricing plan.

1. Choose the **Manage Plan** button.

1. In the **Manage plan** section, choose **Change plan**.

1. Follow the prompts to change your usage level for the Premium pricing plan. The console displays the available usage levels and corresponding monthly prices.

### Downgrade a pricing plan
<a name="pricing-plan-downgrade"></a>

We recommend that you downgrade to a lower plan tier if you don't need the additional features on your existing tier. For example, you might downgrade if you expect your application will experience lower traffic.

If you downgrade to a lower tier, your billing changes will take effect at the beginning of the next billing cycle.

If your distribution currently exceeds the usage allowance for a plan, you can downgrade once your usage is within the usage allowance for your desired tier. To avoid being charged for your existing plan tier at the next billing cycle, downgrade before the end of the month.

**To downgrade a pricing plan**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Distributions**.

1. Choose your distribution that is subscribed to an existing pricing plan.

1. Follow the prompts to downgrade your distribution's pricing plan. If you have unsupported features, you must either remove the feature or resource from the distribution.

1. Complete the steps to [update an existing distribution](HowToUpdateDistribution.md).

### Cancel a pricing plan
<a name="pricing-plan-cancel"></a>

When you cancel a paid pricing plan, you will maintain your flat-rate price through the end of your current billing cycle. Your distribution and all associated plan resources will then switch to pay-as-you-go pricing at the start of the next billing cycle. Free plans are cancelled immediately.

**To cancel a pricing plan**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Distributions**.

1. Choose your distribution that is subscribed to an existing pricing plan.

1. Follow the prompts to cancel your distribution's pricing plan.

1. Complete the steps to [update an existing distribution](HowToUpdateDistribution.md).

### Cancel a pending plan change
<a name="pricing-plan-cancel-pending"></a>

If you downgraded or canceled your flat-rate pricing plan, you must wait until the end of the current billing cycle before your changes are in effect. To keep your existing flat-rate pricing plan, upgrade, or downgrade your pricing plan again, you must first cancel your pending plan change.

**To cancel a pending pricing plan change**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Distributions**.

1. Choose your distribution that is subscribed to an existing pricing plan.

1. Follow the prompts to cancel your distribution's pending plan change.

1. Choose the pricing plan that you want for your distribution.

1. Complete the steps to update an existing distribution.

### Deleting a distribution with a pricing plan
<a name="pricing-plan-delete"></a>

You can't delete a distribution that is subscribed to a pricing plan. You must first cancel the pricing plan. Paid pricing plan cancellations take effect after the current billing cycle. Free plans are cancelled immediately. Once the plan is canceled, you can delete the distribution.

**To delete a distribution with a pricing plan**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Distributions**.

1. Follow the previous steps to cancel the distribution's pricing plan.

1. Follow the steps to [delete the distribution](HowToDeleteDistribution.md).

**Note**  
You can disable a distribution that is subscribed to a pricing plan, but you will still incur charges for that plan. To stop incurring charges for your plan, you must first cancel it.

## Permissions
<a name="prerequisites-pricing-plan"></a>

To view or manage pricing plan subscriptions for your CloudFront distributions, you must have the required permissions. For more information, see [AWS managed policy: CloudFrontFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-cloudfront-full-access) and [AWS managed policy: CloudFrontReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-cloudfront-read-only).

## Flat-rate pricing plan quotas
<a name="pricing-plan-quotas"></a>

The following table shows the quotas and restrictions for CloudFront flat-rate pricing plans.

**Note**  
These quotas can't be increased for your AWS account.


| Account-level quotas  | Quotas | 
| --- | --- | 
| Pricing plans per AWS account | 100 | 
| Free plans per AWS account | 3 | 
| Apex-level domains per plan | 1 | 

## Unsupported features
<a name="pricing-plan-unsupported-features"></a>

Before you can associate a distribution with a pricing plan, you must ensure that certain features are disabled and associations are removed.

**Notes**  
If your distribution or account has any of these restrictions, you must resolve them before you can use pricing plans. After you make changes to your distribution, wait for the changes to propagate to all edge locations.
You must have a AWS WAF Web ACL associated with your distribution if you're using a pricing plan. This resource cannot be removed or disassociated from your distribution unless you switch to pay-as-you-go pricing for that distribution.

### Unsupported features
<a name="pricing-plan-disallowed-features"></a>

You can't subscribe distributions to a pricing plan if their configuration contains the following unsupported features. You can disable the unsupported feature and use an alternative option, or keep pay-as-you-go for your distribution.



<table>
<thead>
  <tr><th>Unsupported features</th><th>Alternative options</th><th>AWS service</th></tr>
</thead>
<tbody>
  <tr><td> <a href="distribution-config-options.md">Multi-tenant distributions</a> </td><td>Use a <a href="Introduction.md#choose-standard-or-multi-tenant">standard distribution </a>or pay-as-you-go pricing</td><td>CloudFront</td></tr>
  <tr><td><a href="continuous-deployment.md">Continuous deployment</a> and <a href="understanding-continuous-deployment.md#updating-staging-and-primary-distributions">Staging distributions</a></td><td>Use pay-as-you-go pricing</td><td>CloudFront</td></tr>
  <tr><td><a href="request-static-ips.md">Anycast IP list</a> configuration</td><td>Use pay-as-you-go pricing</td><td>CloudFront</td></tr>
  <tr><td> <a href="real-time-logs.md">Real-time access logs</a> </td><td>Use <a href="DownloadDistValuesGeneral.md#DownloadDistValuesLoggingOnOff">standard access logs</a> or pay-as-you-go pricing</td><td>CloudFront</td></tr>
  <tr><td>Targeted Bots</td><td>Use common bots or pay-as-you-go pricing</td><td>AWS WAF</td></tr>
  <tr><td>Partner Managed Rules</td><td>Use pay-as-you-go pricing</td><td>AWS WAF</td></tr>
  <tr><td>Account Creation Fraud Prevention</td><td>Use pay-as-you-go pricing</td><td>AWS WAF</td></tr>
  <tr><td>Account Takeover Protection</td><td>Use pay-as-you-go pricing</td><td>AWS WAF</td></tr>
  <tr><td>Rule Groups</td><td>Create individual rules (rule groups are shared AWS WAF rules that can be applied to a web ACL, similar to policies on CloudFront)</td><td>AWS WAF</td></tr>
  <tr><td colspan="2"> <b>Legacy features</b> </td><td></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ForwardedValues.html">ForwardedValues</a> configuration</td><td>Use <a href="controlling-origin-requests.md">Origin request policies</a></td><td>CloudFront</td></tr>
  <tr><td> <a href="cnames-and-https-switch-dedicated-to-sni.md">Dedicated IP/SSL</a> </td><td>Use pay-as-you-go pricing</td><td>CloudFront</td></tr>
  <tr><td> <a href="field-level-encryption.md">Field level encryption</a> </td><td>Use pay-as-you-go pricing</td><td>CloudFront</td></tr>
  <tr><td> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html">AWS Identity and Access Management (IAM) server certificates</a> </td><td>Use AWS Certificate Manager (ACM) certificates</td><td>CloudFront</td></tr>
  <tr><td> <a href="private-content-restricting-access-to-s3.md#migrate-from-oai-to-oac">Origin access identity (OAI)</a> </td><td>Use <a href="private-content-restricting-access-to-origin.md">Origin access control (OAC)</a></td><td>CloudFront</td></tr>
  <tr><td>Legacy cache settings</td><td>Use <a href="cache-key-understand-cache-policy.md">cache policies</a> and <a href="understanding-how-origin-request-policies-and-cache-policies-work-together.md">origin request policies</a>.</td><td>CloudFront</td></tr>
</tbody>
</table>


### Unsupported associations
<a name="pricing-plan-disallowed-associations"></a>

You can't subscribe a distribution to a pricing plan if the distribution is already associated with any of the following resources that are *already associated* with other distributions. Resources that are associated to a distribution that is subscribed to a pricing plan can only be used for that distribution. For example, if you have a CloudFront function that is using a key value store, neither the function nor the key value store can be shared for a distribution that is on a pricing plan. 
+ CloudFront Functions
+ CloudFront Functions associated with a key value store
+ AWS WAF Web ACLs

To subscribe a distribution to a pricing plan, either remove the associated resource or replace it with another one.

### Account-level constraints
<a name="pricing-plan-account-constraints"></a>

AWS accounts are not eligible for pricing plans if they meet any of the following conditions:
+ You reached the maximum number of subscriptions allowed. See [Flat-rate pricing plan quotas](#pricing-plan-quotas).
+ Your account is using AWS Free Tier.

### Resource-level constraints
<a name="resource-level-constraints"></a>

Distributions are not eligible for pricing plans if they meet any of the following conditions:
+ Your distribution has enabled AWS Shield Advanced
+ Your distribution has enabled the [Firewall Manager Service](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) for your web ACL. Firewall Manager won't manage your CloudFront distribution's WebACL in a pricing plan.

### Additional features that can affect your pricing plan
<a name="features-affect-pricing-plan"></a>

Flat-rate pricing plans enable you to pay a flat-rate for your CloudFront distribution and the features listed above that are both included in your plan and associated with your CloudFront distribution. All other features may incur additional charges, including but not limited to the following:

 

**CloudFront**
+ Lambda@Edge function invocations

**AWS WAF**
+ CAPTCHA puzzles created using the [JavaScript API ](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-captcha-api.html)are billed using pay-as-you-go pricing. CAPTCHA responses configured in your AWS WAF rules (the most common use case) are included in your plan at no additional charge.

**Route 53**
+ Route 53 DNSSEC has an AWS KMS cost
+ Route 53 IP (CIDR) blocks (the first 1,000 are free per AWS account)
+ Route 53 Health Checks (the first 50 are free per AWS account)

**Logging features**
+ Route 53 DNS Query Logs, CloudFront Functions logs, and CloudFront Connection Function Logs
+ AWS WAF log delivery to Amazon S3
+ CloudFront or AWS WAF log delivery to Amazon Data Firehose
+ Additional CloudWatch metrics for CloudFront
+ CloudFront access logs in Parquet format

**Note**  
Your plan includes Amazon CloudWatch Logs ingestion for CloudFront standard logs (access logs) and WAF logs for no added costs. All other CloudWatch costs such as storage and querying are not covered by your plan. All other logs are also billed separately.

**Note**  
Your plan includes public authoritative DNS from Route 53. When your Route 53 hosted zone is attached to your pricing plan, your plan covers your hosted zone's standard costs, including the monthly hosted zone fee, DNS records, and DNS query fees subject to respective allowances per tier. All other costs from Route 53 usage and features not listed above as included in your plan are not covered by your plan.

### Pricing plans vs. pay-as-you-go pricing
<a name="pricing-plan-vs-pay-as-you-go"></a>

Flat-rate plans and pay-as-you-go pricing offer different advantages based on your needs. With flat-rate plans, you pay one price that includes multiple AWS services like CloudFront, AWS WAF, Route 53, and CloudWatch Logs ingestion and never face overage charges, even during traffic spikes or attacks. 

With pay-as-you-go pricing, you're billed separately for each service and feature based on your actual usage. While this provides complete flexibility in service selection and configuration, your costs can vary month to month based on traffic patterns, and you will need to monitor usage across multiple services to manage costs. 

Flat-rate plans are ideal if you want combined monthly billing, simplified service configuration, and built-in security features without worrying about overage charges. Pay-as-you-go pricing is a better choice if you need complete control over individual service features, custom configurations, access to features not available in flat-rate plans, or if you expect to handle large, predictable traffic spikes. Amazon CloudFront flat-rate pricing plans may not be combined with any other offers, promotions, or discounts. 