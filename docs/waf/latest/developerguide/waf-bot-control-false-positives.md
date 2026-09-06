

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Example scenarios of false positives with AWS WAF Bot Control
<a name="waf-bot-control-false-positives"></a>

 This section provides example situations where you might encounter false positives with AWS WAF Bot Control.

We have carefully selected the rules in the AWS WAF Bot Control managed rule group to minimize false positives. We test the rules against global traffic and monitor their impact on test protection packs (web ACLs). However, it's still possible to get false positives due to changes in traffic patterns. Additionally, some use cases are known to cause false positives and will require customization specific to your web traffic. 

Situations where you might encounter false positives include the following: 
+ Mobile apps typically have non-browser user agents, which the `SignalNonBrowserUserAgent` rule blocks by default. If you expect traffic from mobile apps, or any other legitimate traffic with non-browser user agents, you'll need to add an exception to allow it. 
+ You might rely on some specific bot traffic for things like uptime monitoring, integration testing, or marketing tools. If Bot Control identifies and blocks the bot traffic that you want to allow, you need to alter the handling by adding your own rules. While this isn't a false positive scenario for all customers, if it is for you, you will need to handle it the same as for a false positive. 
+ The Bot Control managed rule group verifies bots using the IP addresses from AWS WAF. If you use Bot Control and you have verified bots that route through a proxy or load balancer, you might need to explicitly allow them using a custom rule. For information about how to create a custom rule of this type, see [Using forwarded IP addresses in AWS WAF](waf-rule-statement-forwarded-ip-address.md). 
+ A Bot Control rule with a low global false positive rate might heavily impact specific devices or applications. For example, in testing and validation, we might not have observed requests from applications with low traffic volumes or from less common browsers or devices. 
+ A Bot Control rule that has a historically low false positive rate might have increased false positives for valid traffic. This might be due to new traffic patterns or request attributes that emerge with valid traffic, causing it to match the rule where it didn't before. These changes might be due to situations like the following:
  + Traffic details that are altered as traffic flows through network appliances, such as load balancers or content distribution networks (CDN).
  + Emerging changes in traffic data, for example new browsers or new versions for existing browsers.

**Important**  
If your mobile app uses a non-standard HTTP library, or if users access your site through in-app browsers (such as links opened from social media apps), these clients may trigger the `SignalNonBrowserUserAgent` rule. Standard native mobile frameworks are excluded from this rule, but other non-browser user agents are not. Plan to test and add exceptions before enabling Bot Control in block mode. For an example, see [Bot Control example: Creating an exception for a blocked user agent](waf-bot-control-example-user-agent-exception.md).

For information about how to handle false positives that you might get from the AWS WAF Bot Control managed rule group, see the guidance in the section that follows, [Testing and deploying AWS WAF Bot Control](waf-bot-control-deploying.md).