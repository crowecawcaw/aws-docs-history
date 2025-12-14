**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# IP reputation rule

groups

IP reputation rule groups block requests based on
their source IP address.

###### Note

These rules use the source IP address from the web request origin.
If you have traffic that goes through one or more proxies or load balancers, the web request origin
will contain the address of the last proxy, and not the originating address of the client.

Choose one
or more of these rule groups if you want to reduce your exposure to bot
traffic or exploitation attempts, or if you are enforcing geographic
restrictions on your content. For bot management, see also [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md").

The rule groups in this category don't provide versioning or SNS update notifications.

## Amazon IP reputation list managed rule group

VendorName: `AWS`, Name:
`AWSManagedRulesAmazonIpReputationList`, WCU: 25

###### Note

The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you
with what you need to use the rules without giving
bad actors what they need to circumvent the rules.

If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

The Amazon IP reputation list rule group contains rules that are based on
Amazon internal threat intelligence. This is useful if you would like to
block IP addresses typically associated with bots or other threats. Blocking
these IP addresses can help mitigate bots and reduce the risk of a malicious
actor discovering a vulnerable application.

This managed rule group adds labels to the web requests that
it evaluates, which are available to rules that run after this rule group in your protection pack (web ACL). AWS WAF
also records the labels to Amazon CloudWatch metrics. For general information about labels and label metrics, see [Web request labeling](waf-labels.md "waf-labels.md")
and [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label").

| Rule name                      | Description and label                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWSManagedIPReputationList`   | Inspects for IP<br>addresses that have been identified as actively<br>engaging in malicious activities. AWS WAF<br>collects the IP address list from<br>various sources, including MadPot, a threat<br>intelligence tool that Amazon uses to protect<br>customers from cybercrime. For more information<br>about MadPot, see [https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime](https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime "https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:amazon-ip-list:AWSManagedIPReputationList` |
| `AWSManagedReconnaissanceList` | Inspects for connections from IP addresses that<br>are performing reconnaissance against AWS<br>resources.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:amazon-ip-list:AWSManagedReconnaissanceList`                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `AWSManagedIPDDoSList`         | Inspects for IP addresses that have been identified as<br>actively engaging in DDoS activities.<br>Rule action: Count<br>Label:<br>`awswaf:managed:aws:amazon-ip-list:AWSManagedIPDDoSList`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Anonymous IP list managed rule group

VendorName: `AWS`, Name:
`AWSManagedRulesAnonymousIpList`, WCU: 50

###### Note

The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you
with what you need to use the rules without giving
bad actors what they need to circumvent the rules.

If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

The Anonymous IP list rule group contains rules to block requests from services that
permit the obfuscation of viewer identity. These include requests from
VPNs, proxies, Tor nodes, and web hosting providers. This rule group is
useful if you want to filter out viewers that might be trying to hide
their identity from your application. Blocking the IP addresses of these
services can help mitigate bots and evasion of geographic
restrictions.

This managed rule group adds labels to the web requests that
it evaluates, which are available to rules that run after this rule group in your protection pack (web ACL). AWS WAF
also records the labels to Amazon CloudWatch metrics. For general information about labels and label metrics, see [Web request labeling](waf-labels.md "waf-labels.md")
and [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label").

| Rule name               | Description and label                                                                                                                                                                                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AnonymousIPList`       | Inspects for a list of IP addresses of sources<br>known to anonymize client information, like TOR<br>nodes, temporary proxies, and other masking<br>services.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:anonymous-ip-list:AnonymousIPList`                       |
| `HostingProviderIPList` | Inspects for a list of IP addresses from web hosting and<br>cloud providers, which are less likely to source end-user<br>traffic. The IP list does not include AWS IP addresses.<br>Rule action: Block<br>Label: `awswaf:managed:aws:anonymous-ip-list:HostingProviderIPList` |
