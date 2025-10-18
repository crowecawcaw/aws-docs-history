# Manage AWS WAF security protections in the CloudFront security dashboard

CloudFront creates a security dashboard for each of your distributions. You use the dashboards in
 the CloudFront console. With
 the
 dashboards,
 you can use CloudFront and AWS WAF together in a single location to monitor and manage
 common security protections for your web applications. The dashboards provide the following tasks
 and data:


* **Security
 configuration** –
 You can enable and disable AWS WAF protections, and see any app-specific protections such as
 WordPress protections.
* **Security
 trends** –
 These
 include
 allowed and blocked requests, challenge and CAPTCHA requests, and top attack types. You can see traffic ratios and how they change over time. For example, if all requests increase by 3% but allowed requests increase by 14%, that means you allowed a larger portion of your traffic through in the current period.
* **Bot
 requests** –
 You can see how much traffic comes from bots, which types of bots (verified vs non-verified),
 and how the percentage allocations of bot types (verified vs non-verified) change over
 time. For more information about enabling bot control, see [Enable bot control](WAF-one-click.md#bot-traffic "WAF-one-click.md#bot-traffic").
* **Request
 logs** –
 Log data can help answer questions about security trends or bot requests. You can search your
 logs without writing queries, and view aggregate charts to help determine if a filtered set of
 logs is primarily being driven by a subset of HTTP methods, IP addresses, URI paths, or
 countries. You can hover over values in the charts and block IP addresses and countries. For more information, see [Enable AWS WAF logs](#understand-logging "#understand-logging").
* **Geographic restriction management** – CloudFront and AWS WAF provide geographic restriction features. CloudFront provides geographic restrictions for free, but metrics for CloudFront geographic restrictions aren't displayed in the security dashboard. To see request metrics for blocked country requests, you must use AWS WAF geographic restrictions. To do this, hover over a country bar in the security dashboard and block the country. For more information, see [Use CloudFront geographic restrictions](georestrictions.md#georestrictions-cloudfront "georestrictions.md#georestrictions-cloudfront").




	+ The **Block** option might not be available if you previously created a custom AWS WAF rule outside of the CloudFront console to block countries.
###### Topics

* [Prerequisites](#prerequisites "#prerequisites")
* [Enable AWS WAF logs](#understand-logging "#understand-logging")
## Prerequisites


You must enable AWS WAF if you want to view security metrics in the CloudFront **Security** dashboard. If you don't enable AWS WAF, you can 
 only use the **Security** dashboard to enable AWS WAF or configure CloudFront geographic restrictions.


 For more information about enabling AWS WAF, see [Enable AWS WAF for distributions](WAF-one-click.md "WAF-one-click.md").


## Enable AWS WAF logs


AWS WAF log data can help you isolate specific traffic patterns. For example, logs can show you where certain traffic comes from or what it does.


If you enable AWS WAF logging to CloudWatch, the CloudFront security dashboard queries, aggregates, and displays insights from the CloudWatch logs. 
 We don’t charge to use the security dashboard, but CloudWatch pricing applies to logs queried through the dashboard. For more information, see 
 [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").


###### To enable logs

1. Enter your expected request volume in the **Number of requests/month** box to estimate the costs of enabling logs.
2. Select the **Enable AWS WAF logs** check box.
3. Choose **Enable**.

CloudFront creates a CloudWatch logs group and updates your AWS WAF configuration to begin logging to
 CloudWatch.
 On first use, log data can take several minutes to appear. The **Requests**
 section of the chart lists each request. Below the individual requests, the bar charts aggregate
 data by HTTP method, top URI paths, top IP addresses, and top countries. The charts can help you
 find patterns. For example, you may see a disproportionate volume of requests from a single IP
 address, or data from a country that you haven't previously seen in your logs. You can filter
 requests based on
 **Country**,
 **Host
 Header**, and other attributes to help find unwanted traffic. Once you identify that
 traffic, hover over an individual request or chart item and block an IP address or
 country.


###### Note

Displayed metrics are based on web ACL. Therefore, if you associate the same web ACL to multiple distributions, you will see all metrics for your web ACL, not only the AWS WAF requests that are processed for that distribution.
