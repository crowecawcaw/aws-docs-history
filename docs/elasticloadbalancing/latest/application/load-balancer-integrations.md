# Integrations for your Application Load Balancer

You can optimize your Application Load Balancer architecture by integrating with several
other AWS services to enhance the performance, security, and
availability of your application.

###### Load balancer integrations

- [Amazon Application Recovery Controller (ARC)](#arc-integration "#arc-integration")
- [Amazon CloudFront + AWS WAF](#cloudfront-waf "#cloudfront-waf")
- [AWS Global Accelerator](#global-accelerator "#global-accelerator")
- [AWS Config](#config-integration "#config-integration")
- [AWS WAF](#load-balancer-waf "#load-balancer-waf")

## Amazon Application Recovery Controller (ARC)

Amazon Application Recovery Controller (ARC) helps you to shift traffic for your load balancer away from an
impaired Availability Zone to a healthy Availability Zone in the same Region.
Using zonal shift reduces the duration and severity that power outages,
hardware issues, or software issues in an Availability Zone can have on
your applications.

For more information, see [Zonal shift for your Application Load Balancer](zonal-shift.md "zonal-shift.md").

## Amazon CloudFront + AWS WAF

Amazon CloudFront is a web service that helps improve the performance, availability,
and security of your applications that use AWS. CloudFront acts as a distributed,
single point of entry for your web applications that use Application Load Balancers. It extends
your Application Load Balancer's reach globally, allowing it to serve users efficiently from
nearby edge locations, optimizing content delivery and reducing latency for
users worldwide. The automatic content caching at these edge locations
significantly reduces the load on your Application Load Balancer, improving its performance
and scalability.

The one-click integration available in the ELB console creates a CloudFront distribution
with the recommended AWS WAF security protections, and associates it to your Application Load Balancer.
The AWS WAF protections block against common web exploits before reaching your load
balancer. You can access the CloudFront distribution and its corresponding security dashboard
from the load balancer’s **Integrations** tab in the console. For
more information, see [Manage AWS WAF
security protections in the CloudFront security dashboard](../../../AmazonCloudFront/latest/DeveloperGuide/security-dashboard.md "../../../AmazonCloudFront/latest/DeveloperGuide/security-dashboard.md") in the
_Amazon CloudFront Developer Guide_ and
[Introducing
CloudFront Security Dashboard, a Unified CDN and Security Experience](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-cloudfront-security-dashboard-a-unified-cdn-and-security-experience/ "https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-cloudfront-security-dashboard-a-unified-cdn-and-security-experience/") at _aws.amazon.com/blogs_.

As a security best practice, configure your internet-facing Application Load Balancer's security groups
to allow inbound traffic only from the AWS-managed prefix list for CloudFront, and
remove any other inbound rules. For more information, see
[Use the CloudFront managed prefix
list](../../../AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.md "../../../AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.md"),
[Configure
CloudFront to add a custom HTTP header to requests](../../../AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.md#restrict-alb-add-custom-header.html "../../../AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.md#restrict-alb-add-custom-header.html") and
[Configure
an Application Load Balancer to only forward requests that contain a specific header](../../../AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.md#restrict-alb-route-based-on-header.html "../../../AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.md#restrict-alb-route-based-on-header.html") in the _Amazon CloudFront Developer Guide_>.

###### Note

CloudFront only supports ACM certificates in the US East (N. Virginia) us-east-1 region. If
your Application Load Balancer has an HTTPS listener configured with an ACM certificate in a region other than
us-east-1, you will need to either change the CloudFront origin connection from HTTPS to
HTTP, or provision an ACM certificate in the US East (N. Virginia) region and attach it to your CloudFront distribution.

## AWS Global Accelerator

To optimize application availability, performance, and security,
create an accelerator for your load balancer. The accelerator directs
traffic over the AWS global network to static IP addresses that serve
as fixed endpoints in the nearest Region to the client. AWS Global Accelerator
is protected by Shield Standard, which minimizes application
downtime and latency from DDoS attacks.

For more information, see [Adding
an accelerator when you create a load balancer](../../../global-accelerator/latest/dg/about-accelerators.md "../../../global-accelerator/latest/dg/about-accelerators.md") in the
_AWS Global Accelerator Developer Guide_.

## AWS Config

To optimize monitoring and compliance of your load balancer, set up
AWS Config. AWS Config provides a detailed view of the configuration of
AWS resources in your AWS account. This includes how the resources are
related to one another and how they were configured in the past so that
you can see how the configurations and relationships change over time.
AWS Config streamlines audits, compliance, and troubleshooting.

For more information, see the [AWS Config Developer Guide](../../../config/latest/developerguide.md "../../../config/latest/developerguide.md").

## AWS WAF

You can use AWS WAF with your Application Load Balancer to allow or block requests based on the rules in a
web access control list (web ACL).

By default, if the load balancer cannot get a response from AWS WAF, it returns an HTTP
500 error and does not forward the request. If you need your load balancer to forward
requests to targets even if it is unable to contact AWS WAF, you can enable AWS WAF fail open.

###### Pre-defined web ACLs

When enabling AWS WAF integration you can choose to automatically create a new web ACL
with pre-defined rules. The pre-defined web ACL includes three AWS managed rules which
offer protections against the most common security threats.

- `AWSManagedRulesAmazonIpReputationList` ‐ The Amazon IP reputation list
  rule group blocks IP addresses typically associated with bots or other threats. For more information,
  see [Amazon
  IP reputation list managed rule group](../../../waf/latest/developerguide/aws-managed-rule-groups-ip-rep.md#aws-managed-rule-groups-ip-rep-amazon "../../../waf/latest/developerguide/aws-managed-rule-groups-ip-rep.md#aws-managed-rule-groups-ip-rep-amazon") in the _AWS WAF Developer Guide_.
- `AWSManagedRulesCommonRuleSet` ‐ The core rule set (CRS) rule group provides
  protection against exploitation of a wide range of vulnerabilities, including some of the
  high risk and commonly occurring vulnerabilities described in OWASP publications such as
  [OWASP Top 10](https://owasp.org/www-project-top-ten/ "https://owasp.org/www-project-top-ten/"). For more information,
  see [Core
  rule set (CRS) managed rule group](../../../waf/latest/developerguide/aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-crs "../../../waf/latest/developerguide/aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-crs") in the _AWS WAF Developer Guide_.
- `AWSManagedRulesKnownBadInputsRuleSet` ‐ The Known bad inputs rule group
  blocks request patterns that are known to be invalid and are associated with exploitation
  or discovery of vulnerabilities. For more information, see
  [Known
  bad inputs managed rule group](../../../waf/latest/developerguide/aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-known-bad-inputs "../../../waf/latest/developerguide/aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-known-bad-inputs") in the _AWS WAF Developer Guide_.

For more information, see [Using web ACLs in AWS WAF](../../../waf/latest/developerguide/web-acl.md "../../../waf/latest/developerguide/web-acl.md") in the _AWS WAF Developer Guide_.
