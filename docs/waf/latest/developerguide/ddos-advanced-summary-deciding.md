**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Deciding whether to subscribe to

AWS Shield Advanced and apply additional protections

Review the scenarios in this section for help deciding which accounts to subscribe to
AWS Shield Advanced and where to apply additional protections. With Shield Advanced, you pay one
monthly subscription fee for all accounts created under a consolidated billing
account, plus usage fees based on GB of data transferred out. For information about
Shield Advanced pricing, see [AWS Shield Advanced
Pricing](https://aws.amazon.com/shield/pricing/ "https://aws.amazon.com/shield/pricing/").

To protect an application and its resources with Shield Advanced, you subscribe the accounts that
manage the application to Shield Advanced and then you add protections to the application's
resources. For information about subscribing accounts and protecting resources, see
[Setting up AWS Shield Advanced](getting-started-ddos.md "getting-started-ddos.md").

###### Shield Advanced subscriptions and AWS WAF costs

Your Shield Advanced subscription covers the costs of using standard AWS WAF capabilities for resources that you protect with Shield Advanced. The standard AWS WAF fees that are covered by your Shield Advanced protections are the
cost per protection pack (web ACL), the cost per rule, and the base price per million requests for web request inspection, up to 1,500 WCUs and up to the default body size.

Enabling Shield Advanced automatic application layer DDoS mitigation adds a rule group to your protection pack (web ACL) that uses 150 web ACL capacity units
(WCUs). These WCUs count against the WCU usage in your protection pack (web ACL). For more information, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") , [Protecting the application layer with the Shield Advanced
rule group](ddos-automatic-app-layer-response-rg.md "ddos-automatic-app-layer-response-rg.md"), and [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md").

Your subscription to Shield Advanced does not cover the use of AWS WAF for resources that you do not protect using Shield Advanced. It also does not cover any additional non-standard AWS WAF costs for protected resources. Examples of non-standard AWS WAF costs are those for Bot Control, for the CAPTCHA rule action, for web ACLs that use more than 1,500 WCUs, and for inspecting the request body beyond the default body size. The full list is provided on the AWS WAF pricing page. Your subscription to Shield Advanced includes access to the Layer 7 Anti-DDoS Amazon Managed Rule group. As part of your subscription, you will get up to 50 billion requests to Shield Advanced protected AWS WAF resources in a calendar month. Requests beyond 50 billion will be billed as per the AWS Shield Advanced pricing page.

For full information and pricing examples, see [Shield Pricing](https://aws.amazon.com/shield/pricing/ "https://aws.amazon.com/shield/pricing/") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### Shield Advanced subscription billing

If you’re an AWS Channel Reseller, talk to your account team for information and guidance. This billing information is for customers that are not AWS Channel Resellers.

For all others, the following subscription and billing guidelines apply:

- For accounts that are members of an AWS Organizations organization, AWS bills the Shield Advanced
  subscriptions against the payer account for the organization, regardless of whether the payer
  account itself is subscribed.
- When you subscribe multiple accounts that are in the same [AWS Organizations
  consolidated billing account family](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md"), one subscription price covers all
  subscribed accounts in the family. The organization must own all of the AWS accounts
  and all of their resources.
- When you subscribe multiple accounts for multiple organizations, you can still pay one
  subscription fee across all of the organizations, accounts, and resources providing you
  own all of them. Contact your account manager or AWS support and request a fee waiver
  on the AWS Shield Advanced subscription charges for all but one of the organizations.
  For detailed pricing information and examples, see [AWS Shield Pricing](https://aws.amazon.com/shield/pricing/ "https://aws.amazon.com/shield/pricing/").

###### Identifying the applications to protect

Consider implementing Shield Advanced protections for applications where you need any of the following:

- Guaranteed availability for the users of the application.
- Rapid access to DDoS mitigation experts if the application is affected by a DDoS
  attack.
- Awareness by AWS that the application might be affected by a DDoS attack and
  notification of attacks from AWS and escalation to your security or
  operations teams.
- Predictability in your cloud costs, including when a DDoS attack affects your use of
  AWS services.
  If an application or its resources require any of the above, consider creating
  subscriptions for the related accounts.

###### Identifying the resources to protect

For each subscribed account, consider adding a Shield Advanced protection to each
resource that has any of the following characteristics:

- The resource serves external users on the internet.
- The resource is exposed to the internet and is also part of a critical application.
  Consider every exposed resource, regardless of whether you intend it to be
  accessed by users on the internet.
- The resource is protected by an AWS WAF web ACL.
  To learn more about creating and managing protections for your resources, see [Resource protections in AWS Shield Advanced](ddos-resource-protections.md "ddos-resource-protections.md").

Additionally, follow the recommendations in this guide to help ensure that you architect your application
for DDoS resiliency and that you have properly configured the features of
Shield Advanced for optimal protections.
