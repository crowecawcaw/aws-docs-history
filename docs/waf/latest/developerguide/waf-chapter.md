

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# AWS WAF
<a name="waf-chapter"></a>

AWS WAF is a web application firewall that lets you monitor the HTTP(S) requests that are forwarded to your protected web application resources. You can protect the following resource types: 
+ Amazon CloudFront distribution
+ Amazon API Gateway REST API
+ Application Load Balancer
+ AWS AppSync GraphQL API
+ Amazon Cognito user pool
+ AWS App Runner service
+ Amazon Bedrock AgentCore Gateway
+ AWS Verified Access instance
+ AWS Amplify

AWS WAF lets you control access to your content. Based on criteria that you specify, such as the IP addresses that requests originate from or the values of query strings, the service associated with your protected resource responds to requests either with the requested content, with an HTTP 403 status code (Forbidden), or with a custom response. 

**Note**  
You can also use AWS WAF to protect your applications that are hosted in Amazon Elastic Container Service (Amazon ECS) containers. Amazon ECS is a highly scalable, fast container management service that makes it easy to run, stop, and manage Docker containers on a cluster. To use this option, you configure Amazon ECS to use an Application Load Balancer that is enabled for AWS WAF to route and protect HTTP(S) layer 7 traffic across the tasks in your service. For more information, see [Service Load Balancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) in the *Amazon Elastic Container Service Developer Guide*.

**Topics**
+ [Get started with AWS WAF](getting-started.md)
+ [How AWS WAF works](how-aws-waf-works.md)
+ [Configuring protection in AWS WAF](web-acl.md)
+ [AWS WAF rules](waf-rules.md)
+ [AWS WAF rule groups](waf-rule-groups.md)
+ [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md)
+ [Oversize web request components in AWS WAF](waf-oversize-request-components.md)
+ [Supported regular expression syntax in AWS WAF](waf-regex-pattern-support.md)
+ [IP sets and regex pattern sets in AWS WAF](waf-referenced-set-managing.md)
+ [Customized web requests and responses in AWS WAF](waf-custom-request-response.md)
+ [Web request labeling in AWS WAF](waf-labels.md)
+ [Intelligent threat mitigation in AWS WAF](waf-managed-protections.md)
+ [AI traffic monetization](waf-ai-traffic-monetization.md)
+ [Data protection and logging for AWS WAF protection pack (web ACL) traffic](waf-data-protection-and-logging.md)
+ [Testing and tuning your AWS WAF protections](web-acl-testing.md)
+ [Using AWS WAF with Amazon CloudFront](cloudfront-features.md)
+ [Security in your use of the AWS WAF service](security.md)
+ [AWS WAF quotas](limits.md)
+ [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md)