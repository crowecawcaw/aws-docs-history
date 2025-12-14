**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS WAF Fraud Control account creation fraud prevention (ACFP)

This section explains what AWS WAF Fraud Control account creation fraud prevention (ACFP) does.

Account creation fraud is an online illegal activity in which an attacker tries to
create one or more fake accounts. Attackers use fake accounts for fraudulent activities
such as abusing promotional and sign up bonuses, impersonating someone, and cyberattacks like phishing.
The presence of fake accounts can negatively impact your business by damaging your reputation
with customers and exposure to financial fraud.

You can monitor and control account creation fraud attempts by implementing the ACFP
feature. AWS WAF offers this feature in the AWS Managed Rules rule group `AWSManagedRulesACFPRuleSet` with companion application
integration SDKs.

The ACFP managed rule group labels and manages requests
that might be part of malicious account creation attempts. The rule group does this by
inspecting account creation attempts that clients send to your application's account sign-up endpoint.

ACFP protects your account
sign-up pages by monitoring account sign-up requests for anomalous activity and by automatically
blocking suspicious
requests. The rule group uses request identifiers, behavioral analysis, and machine learning
to detect fraudulent requests.

- **Request inspection** – ACFP gives you visibility and control over anomalous account creation attempts and attempts
  that use stolen credentials, to prevent the creation of fraudulent accounts.
  ACFP checks email and password combinations against its stolen credential
  database, which is updated regularly as new leaked credentials are found on the dark web.
  ACFP evaluates the domains used in email addresses, and monitors the use of phone numbers
  and address fields to verify the entries and to detects fraudulent behavior.
  ACFP aggregates data by IP address and client session, to detect and block clients that send
  too many requests of a suspicious nature.
- **Response inspection** – For CloudFront distributions, in
  addition to inspecting incoming account creation requests, the ACFP rule
  group inspects your application's responses to account creation attempts,
  to track success and failure rates. Using this information, ACFP
  can temporarily block client sessions or IP addresses that have too many failed attempts.
  AWS WAF performs response inspection asynchronously, so this doesn't
  increase latency in your web traffic.

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### Note

The ACFP feature is not available for Amazon Cognito user pools.

###### Topics

- [AWS WAF ACFP components](waf-acfp-components.md "waf-acfp-components.md")
- [Using application integration SDKs with ACFP](waf-acfp-with-tokens.md "waf-acfp-with-tokens.md")
- [Adding the ACFP managed rule group to your web
  ACL](waf-acfp-rg-using.md "waf-acfp-rg-using.md")
- [Testing and deploying ACFP](waf-acfp-deploying.md "waf-acfp-deploying.md")
- [AWS WAF Fraud Control account creation fraud prevention (ACFP) examples](waf-acfp-control-examples.md "waf-acfp-control-examples.md")
