

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Considerations for managing body inspection in AWS WAF
<a name="web-acl-setting-body-inspection-limit"></a>

The body inspection size limit is the maximum request body size that AWS WAF can inspect. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to AWS WAF for inspection. 
+ For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
+ For CloudFront, API Gateway, Amazon Cognito, App Runner, Verified Access, and Amazon Bedrock AgentCore Gateway, the default limit is 16 KB (16,384 bytes), and you can increase the limit for any of the resource types by increments of 16 KB, up to 64 KB. The setting options are 16 KB, 32 KB, 48 KB, and 64 KB. 

**Important**  
AWS WAF does not support request body inspection rules for gRPC traffic. If you enabled these rules on the protection pack (web ACL) for a CloudFront distribution or Application Load Balancer, any request that uses gRPC will ignore the request body inspection rules. All other AWS WAF rules will still apply. For more information, see [Enable AWS WAF for distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/WAF-one-click.html) in the *Amazon CloudFront Developer Guide*. 

**Oversize body handling**  
If your web traffic includes bodies that are larger than the limit, your configured oversize handling will apply. For information about the options for oversize handling, see [Oversize web request components in AWS WAF](waf-oversize-request-components.md). 

**Pricing considerations for increasing the limit setting**  
AWS WAF charges a base rate for inspecting traffic that's within the default limit for the resource type. 

For CloudFront, API Gateway, Amazon Cognito, App Runner, Verified Access, and Amazon Bedrock AgentCore Gateway resources, if you increase the limit setting, the traffic that AWS WAF can inspect includes body sizes up to your new limit. You're charged extra only for the inspection of requests that have body sizes larger than the default 16 KB. For more information about pricing, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

**Options for modifying the body inspection size limit**  
You can configure the body inspection size limit for CloudFront, API Gateway, Amazon Cognito, App Runner, Verified Access, or Amazon Bedrock AgentCore Gateway resources. 

When you create or edit a protection pack (web ACL), you can modify the body inspection size limits in the resource association configuration. For the API, see the protection pack (web ACL)'s association configuration at [AssociationConfig](https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociationConfig.html). For the console, see the configuration on the page where you specify the protection pack (web ACL)'s associated resources. For guidance on the console configuration, see [Viewing web traffic metrics in AWS WAF](web-acl-working-with.md). 

## AWS WAF inspection controls for HTTP/2 traffic on Application Load Balancer
<a name="web-acl-http2-body-inspection"></a>

You can configure how AWS WAF inspects HTTP/2 request bodies on your (Application Load Balancer) when routing to HTTP/2 targets. Adjusting the inspection timing allows you to balance security coverage with your application's communication patterns.

To modify this setting, edit your target group attributes for the HTTP/2 target. You can find this setting in the Application Load Balancer target group console under **WAF HTTP/2 traffic inspection behavior**. For more information, see [ALB documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/waf-http2-inspection.html).

The attributes for **WAF HTTP/2 traffic inspection behavior** are:

**Inspect immediately** (default)  
AWS WAF inspects each HTTP/2 request immediately using the available request data.  
Choose this option for bidirectional streaming applications where clients expect server responses before completing their request transmission. This prevents timeouts in applications that require real-time bidirectional communication.

**Inspect after sufficient data**  
AWS WAF inspection begins only after receiving sufficient HTTP/2 data frames from the client, ensuring complete request inspection for enhanced security.  
Choose this option for standard request-response applications where clients send all request data before expecting a server response. This is the recommended setting for most use cases.