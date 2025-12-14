**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Considerations for managing body inspection in AWS WAF

The body inspection size limit is the maximum request body size that AWS WAF can
inspect. When a web request body is larger than the limit, the underlying host service
only forwards the contents that are within the limit to AWS WAF for inspection.

- For Application Load Balancer and AWS AppSync, the limit is fixed at
  8 KB (8,192 bytes).
- For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is
  16 KB (16,384 bytes), and you can increase the limit for
  any of the resource types by increments of 16 KB, up to 64 KB. The setting
  options are 16 KB, 32 KB, 48 KB, and 64 KB.

###### Important

AWS WAF does not support request body inspection rules for gRPC traffic. If you enabled these rules on the protection pack (web ACL)
for a CloudFront distribution or Application Load Balancer, any request that
uses gRPC will ignore the request body inspection rules. All other AWS WAF rules will still apply. For more information,
see [Enable AWS WAF for distributions](../../../AmazonCloudFront/latest/DeveloperGuide/WAF-one-click.md "../../../AmazonCloudFront/latest/DeveloperGuide/WAF-one-click.md") in the _Amazon CloudFront Developer Guide_.

###### Oversize body handling

If your web traffic includes bodies that are larger than the limit, your
configured oversize handling will apply. For information about the options for
oversize handling, see [Oversize web request components
in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").

###### Pricing considerations for increasing the limit setting

AWS WAF charges a base rate for inspecting traffic that's within the default limit
for the resource type.

For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access resources, if you increase the limit setting, the
traffic that AWS WAF can inspect includes body sizes up to your new limit. You're charged
extra only for the inspection of requests that have body sizes larger than the default
16 KB. For more information about pricing, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### Options for modifying the body inspection size limit

You can configure the body inspection size limit for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access
resources.

When you create or edit a protection pack (web ACL), you can modify the body inspection size limits in the
resource association configuration. For the API, see the protection pack (web ACL)'s association configuration at [AssociationConfig](../APIReference/API_AssociationConfig.md "../APIReference/API_AssociationConfig.md"). For the console, see the configuration on the page
where you specify the protection pack (web ACL)'s associated resources. For guidance on the console
configuration, see [Viewing web traffic metrics in AWS WAF](web-acl-working-with.md "web-acl-working-with.md").
