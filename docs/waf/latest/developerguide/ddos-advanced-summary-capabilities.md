**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS Shield Advanced capabilities and options

AWS Shield Advanced subscription includes the following capabilities and options. These supplement
the DDoS detection and mitigation capabilities that you already receive with AWS.

- **AWS WAF integration** – Shield Advanced uses AWS WAF web ACLs,
  rules, and rule groups as part of its application layer protections. For more information about AWS WAF, see [How AWS WAF works](how-aws-waf-works.md "how-aws-waf-works.md").

###### Note

Your Shield Advanced subscription covers the costs of using standard AWS WAF capabilities for resources that you protect with Shield Advanced. The standard AWS WAF fees that are covered by your Shield Advanced protections are the
cost per protection pack (web ACL), the cost per rule, and the base price per million requests for web request inspection, up to 1,500 WCUs and up to the default body size.

Enabling Shield Advanced automatic application layer DDoS mitigation adds a rule group to your protection pack (web ACL) that uses 150 web ACL capacity units
(WCUs). These WCUs count against the WCU usage in your protection pack (web ACL). For more information, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") , [Protecting the application layer with the Shield Advanced
rule group](ddos-automatic-app-layer-response-rg.md "ddos-automatic-app-layer-response-rg.md"), and [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md").

Your subscription to Shield Advanced does not cover the use of AWS WAF for resources that you do not protect using Shield Advanced. It also does not cover any additional non-standard AWS WAF costs for protected resources. Examples of non-standard AWS WAF costs are those for Bot Control, for the CAPTCHA rule action, for web ACLs that use more than 1,500 WCUs, and for inspecting the request body beyond the default body size. The full list is provided on the AWS WAF pricing page. Your subscription to Shield Advanced includes access to the Layer 7 Anti-DDoS Amazon Managed Rule group. As part of your subscription, you will get up to 50 billion requests to Shield Advanced protected AWS WAF resources in a calendar month. Requests beyond 50 billion will be billed as per the AWS Shield Advanced pricing page.

For full information and pricing examples, see [Shield Pricing](https://aws.amazon.com/shield/pricing/ "https://aws.amazon.com/shield/pricing/") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

- **Automatic application layer DDoS mitigation** – You
  can configure Shield Advanced to
  respond automatically to mitigate application layer (layer 7) attacks against
  your protected resources. With automatic mitigation, Shield Advanced
  enforces AWS WAF rate limiting on requests from known DDoS sources,
  and it automatically adds and manages custom AWS WAF protections
  in response to detected DDoS attacks. You can configure
  automatic mitigation to count or block the web requests that are part of an
  attack.

For more information, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .

- **Health-based detection** – You can
  use Amazon Route 53 health checks with Shield Advanced to inform event detection and
  mitigation. Health checks monitor your application according to your
  specifications, reporting healthy when your specifications are met and
  unhealthy when they aren't. Using health checks with Shield Advanced helps prevent
  false positives and provides faster detection and mitigation when a
  protected resource is unhealthy. You can use health-based detection for any
  resource type except Route 53 hosted zones. Shield Advanced proactive engagement is
  available only for resources that have health-based detection enabled.

For more information, see [Health-based detection using
health checks with Shield Advanced and Route 53](ddos-advanced-health-checks.md "ddos-advanced-health-checks.md").

- **Protection groups** – You can use protection groups
  to create logical groupings of your protected resources, for enhanced
  detection and mitigation of the group as a whole. You can define the criteria for membership in a
  protection group so that newly protected resources are automatically included.
  A protected resource can belong to multiple protection groups.

For more information, see [Grouping your AWS Shield Advanced protections](ddos-protection-groups.md "ddos-protection-groups.md").

- **Enhanced visibility into DDoS events and attacks**
  – Shield Advanced gives you access to advanced, real-time metrics and
  reports for extensive visibility into events and attacks on your protected
  AWS resources. You can access this information through the Shield Advanced API
  and console, and through Amazon CloudWatch metrics.

For more information, see [Visibility into DDoS events with Shield Advanced](ddos-viewing-events.md "ddos-viewing-events.md").

- **Centralized management of Shield Advanced protections by
  AWS Firewall Manager** – You can use Firewall Manager to automatically apply
  Shield Advanced protections to your new accounts and resources and to deploy AWS WAF
  rules to your web ACLs. Firewall Manager Shield Advanced protection policies are included at
  no additional charge for Shield Advanced customers. You can also centralize your
  Shield Advanced monitoring activities for your accounts by using Firewall Manager with an
  Amazon Simple Notification Service (SNS) topic or AWS Security Hub CSPM.

For more information about using Firewall Manager to manage Shield Advanced protections, see [AWS Firewall Manager](fms-chapter.md "fms-chapter.md")
and [Using AWS Shield Advanced policies in Firewall Manager](shield-policies.md "shield-policies.md"). For
information about Firewall Manager pricing, see [AWS Firewall Manager Pricing](https://aws.amazon.com/firewall-manager/pricing/ "https://aws.amazon.com/firewall-manager/pricing/").

- **AWS Shield Response Team (SRT)** – The SRT has deep experience
  in protecting AWS, Amazon.com, and its subsidiaries. As an AWS Shield Advanced
  customer, you can contact the SRT at any time for assistance during a DDoS
  attack that affects the availability of your application. You can also work
  with the SRT to create and manage custom mitigations for your resources.
  To use the services of the SRT, you must also be subscribed to the [Business
  Support plan](https://aws.amazon.com/premiumsupport/business-support/ "https://aws.amazon.com/premiumsupport/business-support/") or the [Enterprise Support plan](https://aws.amazon.com/premiumsupport/enterprise-support/ "https://aws.amazon.com/premiumsupport/enterprise-support/").

For more information, see [Managed DDoS event response with Shield Response Team (SRT) support](ddos-srt-support.md "ddos-srt-support.md").

- **Proactive engagement** – With proactive engagement,
  the Shield Response Team (SRT) contacts you directly if the Amazon Route 53 health check that
  you have associated with your protected resource becomes unhealthy during an
  event that's detected by Shield Advanced. This gives you quicker engagement with
  experts when the availability of your application might be affected by a
  suspected attack.

For more information, see [Setting up proactive engagement for the SRT to contact you directly](ddos-srt-proactive-engagement.md "ddos-srt-proactive-engagement.md").

- **Cost protection opportunities** – Shield Advanced offers some
  cost protection against spikes in your AWS bill that
  might result from a DDoS attack against your protected resources. This can include
  coverage for spikes in Shield Advanced data transfer out (DTO) usage fees. Shield Advanced provides any
  cost protection in the form of Shield Advanced service credits.

For more information,
see [Requesting a credit in AWS Shield Advanced after an attack](ddos-request-service-credit.md "ddos-request-service-credit.md").
