

# Securing Custom Origins with AWS WAF
<a name="securing-custom-origins-waf"></a>

Publication date: **July 26, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to protect any endpoint against common web vulnerabilities. You use AWS WAF with custom origins and custom secret headers in Amazon CloudFront.

## Securing Custom Origins with AWS WAF
<a name="diagram1"></a>

![Architecture diagram showing how to secure custom origins with AWS WAF and Amazon CloudFront.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/securing-custom-origins-waf/images/securing-custom-origins-waf.png)


1. Users make a request to the web application. DNS records direct the user to the closest CloudFront edge location.

1. AWS WAF inspects the traffic by using both custom and managed rules. It checks for common web exploit attacks. AWS WAF logs traffic for future analysis and can block malicious traffic.

1. CloudFront injects a secret custom header into the request and redirects it to the on-premises web application.

1. The web application drops or blocks any request without the secret custom header. This ensures AWS WAF inspects all traffic.

1. Users receive the response to their request from CloudFront. Data caches at the edge location for the next request.

1. An [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) workflow orchestrates the secret header rotation and deployment process on a configurable schedule.

1. The Step Functions workflow generates a new secret for the custom header value. It stores the value in [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) Parameter Store.

1. The new header value is distributed to one or more web app servers through [SSM](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) Agent and Automation Runbooks. After finalization, the workflow deploys the new header to CloudFront.

1. The on-premises firewall updates to allow only CloudFront IP addresses to the web application as an additional protection layer.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS WAF product page](https://aws.amazon.com/waf/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | July 26, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.