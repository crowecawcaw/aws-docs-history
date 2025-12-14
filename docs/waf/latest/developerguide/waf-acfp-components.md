**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS WAF ACFP components

The primary components of AWS WAF Fraud Control account creation fraud prevention (ACFP) are the following:

- **`AWSManagedRulesACFPRuleSet`** – The rules in this AWS Managed Rules rule group detect,
  label, and handle various types of fraudulent account creation activity. The
  rule group inspects HTTP `GET` text/html requests that clients send
  to the specified account registration endpoint and `POST` web
  requests that clients send to the specified account sign-up endpoint. For
  protected CloudFront distributions, the rule group also inspects the responses that
  the distribution sends back to account creation requests. For a list of this
  rule group's rules, see [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md"). You include this rule group
  in your protection pack (web ACL) using a managed rule group reference statement. For information
  about using this rule group, see [Adding the ACFP managed rule group to your web
  ACL](waf-acfp-rg-using.md "waf-acfp-rg-using.md").

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

- **Details about your application's account registration and creation
  pages** – You must provide information about your account
  registration and creation pages when you add the `AWSManagedRulesACFPRuleSet` rule group to your
  protection pack (web ACL). This lets the rule group narrow the scope of the requests it inspects
  and properly validate account creation web requests. The registration page must
  accept `GET` text/html requests. The account creation path must
  accept `POST` requests. The ACFP rule
  group works with usernames that are in email format. For more information, see
  [Adding the ACFP managed rule group to your web
  ACL](waf-acfp-rg-using.md "waf-acfp-rg-using.md").
- **For protected CloudFront distributions, details about how your application
  responds to account creation attempts** – You provide
  details about your application's responses to account creation attempts, and the
  ACFP rule group tracks and manages bulk account creation attempts from a
  single IP address or single client session. For information about configuring
  this option, see [Adding the ACFP managed rule group to your web
  ACL](waf-acfp-rg-using.md "waf-acfp-rg-using.md").
- **JavaScript and mobile application integration SDKs**
  – Implement the AWS WAF JavaScript and mobile SDKs with your ACFP
  implementation to enable the full set of capabilities that the rule group
  offers. Many of the ACFP rules use the information provided by the SDKs for
  session level client verification and behavior aggregation, required to separate
  legitimate client traffic from bot traffic. For more information about the SDKs,
  see [Client application
  integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md").
  You can combine your ACFP implementation with the following to help you monitor, tune,
  and customize your protections.

- **Logging and metrics** – You can monitor your traffic,
  and understand how the ACFP managed rule group affects it, by configuring and
  enabling logs, Amazon Security Lake data collection, and Amazon CloudWatch metrics for your protection pack (web ACL). The labels that `AWSManagedRulesACFPRuleSet`
  adds to your web requests are included in the data. For
  information about the options, see
  [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md"),
  [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"),
  and [What is Amazon Security Lake?](../../../security-lake/latest/userguide/what-is-security-lake.md "../../../security-lake/latest/userguide/what-is-security-lake.md").

Depending on your needs and the traffic that you see, you might want to customize your
`AWSManagedRulesACFPRuleSet` implementation. For example, you might want to exclude some traffic
from ACFP evaluation, or you might want to alter how it handles some of the
account creation fraud attempts that it identifies, using AWS WAF features like
scope-down statements or label matching rules.

- **Labels and label matching rules** – For any of the
  rules in `AWSManagedRulesACFPRuleSet`, you can switch the blocking behavior to count, and then match
  against the labels that are added by the rules. Use this approach to customize how
  you handle web requests that are identified by the ACFP managed rule group. For more
  information about labeling and using label match statements, see [Label match rule
  statement](waf-rule-statement-type-label-match.md "waf-rule-statement-type-label-match.md") and [Web request labeling in AWS WAF](waf-labels.md "waf-labels.md").
- **Custom requests and responses** – You can add custom
  headers to the requests that you allow and you can send custom responses for
  requests that you block. To do this, you pair your label matching with the AWS WAF
  custom request and response features. For more information about customizing
  requests and responses, see [Customized web requests and responses in
  AWS WAF](waf-custom-request-response.md "waf-custom-request-response.md").
