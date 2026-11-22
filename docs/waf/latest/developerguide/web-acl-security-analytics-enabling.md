

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Enabling security analytics for a protection pack (web ACL)

Each protection pack (web ACL) has an analytics configuration. To view the protection pack (web ACL)'s request log data from multiple AWS Regions in the security analytics dashboard, enable security analytics in the analytics configuration. For information about the dashboard, see [Security analytics for protection packs (web ACLs)](web-acl-security-analytics.md). 

For regional protection packs (web ACLs), security analytics is off by default, and you enable it in the analytics configuration. For protection packs (web ACLs) that protect Amazon CloudFront distributions (global protection packs (web ACLs)), security analytics is enabled by default. There is no additional charge for security analytics. 

**Important**  
When you enable security analytics, you authorize AWS to transfer and store full request logs outside your AWS Region. These logs are from your AWS WAF protection pack (web ACL) and might contain personal data. 

AWS retains transferred data for 30 days. When you disable security analytics, AWS WAF stops transferring logs. AWS deletes any previously stored log data after the retention period ends. 

To enable security analytics through the API, include `AnalyticsConfig` when you call `CreateWebACL` or `UpdateWebACL`, and set its `Mode` to `CROSS_REGION`. To disable it, set `Mode` to `DISABLED`. If you don't include `AnalyticsConfig`, security analytics stays disabled. 

The following JSON shows the `AnalyticsConfig` setting that enables cross-Region security analytics for a protection pack (web ACL). 

```
"AnalyticsConfig": {
    "Mode": "CROSS_REGION"
}
```

For more information, see [WebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html) in the *AWS WAF API Reference*. 