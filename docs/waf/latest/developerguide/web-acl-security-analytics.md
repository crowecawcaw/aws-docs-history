

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Security analytics for protection packs (web ACLs)

The security analytics dashboard in the AWS WAF console shows AWS WAF request log data from multiple AWS Regions in a single view. Use it to monitor and tune your protections without switching between Regions. 

With the dashboard, you can view statistics and time series for your web requests. At the bottom of the dashboard, you can filter requests and view the metadata of individual requests. You can't export log data from the dashboard. 

With the dashboard, you can view your requests grouped by action. It also shows a traffic breakdown that groups requests by attributes such as country, AWS Region, protection pack (web ACL), resource, rule, label, client IP address, Autonomous System Number (ASN), JA4 fingerprint, path, and host.

**Features by pricing plan**  
How far back you can look and which features you can use depend on your pricing plan. The look-back period applies to both statistics and request search. 


| Pricing plan | Look-back period | Filter fields | Request search and detections | 
| --- | --- | --- | --- | 
| Free flat-rate pricing plan | 7 days | Limited | Not included | 
| Pro flat-rate pricing plan or higher | 30 days | All | Included | 
| Pay-as-you-go | 21 days | All | Included | 

For information about flat-rate pricing plans, see [Using AWS WAF with CloudFront Flat-Rate Pricing Plans](cloudfront-features.md#waf-cf-pricing-plans). 

**Enabling security analytics**  
To include a protection pack (web ACL) in the dashboard, enable security analytics in the analytics configuration of the protection pack (web ACL). Security analytics is off by default for regional protection packs (web ACLs). When you enable it, AWS transfers and stores full request logs outside your AWS Region for aggregation and processing. For more information, see [Enabling security analytics for a protection pack (web ACL)](web-acl-security-analytics-enabling.md). 

**Required permissions**  
To view the dashboard, you need permissions for the console-only APIs that security analytics uses. For more information, see [Console-only APIs](security_iam_id-based-policy-examples.md#waf-security-iam-console-only-apis). 

**To view the security analytics dashboard**

1. Sign in to the AWS Management Console and open the AWS WAF console at [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2). 

1. In the navigation pane, choose **Security analytics**.