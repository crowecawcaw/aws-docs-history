**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Associating or disassociating protection with an AWS resource

You can use AWS WAF to create the following associations between protection packs (web ACLs) and your resources:

- Associate a regional protection pack (web ACL) with any of the regional resources listed below. For this
  option, the protection pack (web ACL) must be in the same region as your resource.
  - Amazon API Gateway REST API
  - Application Load Balancer
  - AWS AppSync GraphQL API
  - Amazon Cognito user pool
  - AWS App Runner service
  - AWS Verified Access instance
  - AWS Amplify

- Associate a global protection pack (web ACL) with a Amazon CloudFront distribution. The global protection pack (web ACL) will have a hard-coded Region of
  US East (N. Virginia) Region.
  You can also associate a protection pack (web ACL) with a CloudFront distribution when you create or update the
  distribution itself. For information, see [Using AWS WAF to Control Access to
  Your Content](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.md") in the _Amazon CloudFront Developer Guide_.

###### Restrictions on multiple associations

You can associate a single protection pack (web ACL) with one or more AWS resources, according
to the following restrictions:

- You can associate each AWS resource with only one protection pack (web ACL). The
  relationship between protection pack (web ACL) and AWS resources is one-to-many.
- You can associate a protection pack (web ACL) with one or more CloudFront distributions. You cannot
  associate a protection pack (web ACL) that you have associated with a CloudFront distribution with any
  other AWS resource type.

###### Additional restrictions

The following additional restrictions apply to protection pack (web ACL) associations:

- You can only associate a protection pack (web ACL) to an Application Load Balancer within AWS Regions. For example, you cannot
  associate a protection pack (web ACL) to an Application Load Balancer that is on AWS Outposts.
- You can't associate an Amazon Cognito user pool with a protection pack (web ACL) that uses the AWS WAF Fraud Control account creation fraud prevention (ACFP) managed
  rule group `AWSManagedRulesACFPRuleSet` or the AWS WAF Fraud Control account takeover prevention (ATP) managed
  rule group `AWSManagedRulesATPRuleSet`. For information about account creation fraud
  prevention, see [AWS WAF Fraud Control account creation fraud prevention (ACFP)](waf-acfp.md "waf-acfp.md").
  For information about account takeover
  prevention, see [AWS WAF Fraud Control account takeover prevention (ATP)](waf-atp.md "waf-atp.md").

###### Production traffic risk

Before you deploy your protection pack (web ACL) for production traffic, test and tune it in a
staging or testing environment until you are comfortable with the potential
impact to your traffic. Then test and tune your rules in count mode with your
production traffic before enabling them. For guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").
