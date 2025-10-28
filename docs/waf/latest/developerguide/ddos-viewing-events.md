**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Visibility into DDoS events with Shield Advanced

AWS Shield provides visibility into the following categories of events and event activities:

- **Global** – All customers can access an aggregated
  view of global threat activity over the last two weeks. You can see this information
  under the **Getting Started** and **Global threat
  dashboard** pages of the AWS Shield console. For more information, see
  [Viewing AWS Shield global and account activity](ddos-standard-event-visibility.md "ddos-standard-event-visibility.md").
- **Account** – All customers can access a summary of the
  events for their account over the prior year. You can see this information
  under the **Getting Started** page of the AWS Shield console. For more
  information, see [Viewing AWS Shield global and account activity](ddos-standard-event-visibility.md "ddos-standard-event-visibility.md").
  When you subscribe to Shield Advanced and add protections to your resources, you gain access to
  additional information about the events and DDoS attacks on the protected resources:

- **Events on protected resources** – Shield Advanced
  provides detailed information for each event through the **Events**
  page of the AWS Shield console. For more information, see [Viewing AWS Shield Advanced events](ddos-events.md "ddos-events.md").
- **Event metrics for protected resources** – Shield Advanced
  publishes detection, mitigation, and top contributor Amazon CloudWatch metrics for all
  resources that it protects. You can use these metrics to configure CloudWatch dashboards
  and alarms. For more information, see [AWS Shield Advanced metrics](shield-metrics.md "shield-metrics.md").
- **Cross-account event visibility for protected
  resources** – If you use AWS Firewall Manager to manage your Shield Advanced
  protections, you can enable visibility into protections across multiple accounts by
  using Firewall Manager combined with AWS Security Hub. For more information, see [Viewing Shield Advanced events across multiple AWS accounts with AWS Firewall Manager and AWS Security Hub](ddos-viewing-multiple-accounts.md "ddos-viewing-multiple-accounts.md").
  If you enable automatic application layer DDoS mitigation for an application layer protection,
  Shield Advanced adds a rule group to your protection pack (web ACL) that it uses to manage automated protections. This rule
  group generates AWS WAF metrics, but they are not available to view. This is the same as for
  any other rule groups that you use in your protection pack (web ACL) but do not own, such as AWS Managed Rules rule groups.
  For more information about AWS WAF metrics, see [AWS WAF metrics and dimensions](waf-metrics.md "waf-metrics.md"). For information
  about this Shield Advanced protection option, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .

###### Topics

- [Viewing AWS Shield global and account activity](ddos-standard-event-visibility.md "ddos-standard-event-visibility.md")
- [Viewing AWS Shield Advanced events](ddos-events.md "ddos-events.md")
- [Viewing Shield Advanced events across multiple AWS accounts with AWS Firewall Manager and AWS Security Hub](ddos-viewing-multiple-accounts.md "ddos-viewing-multiple-accounts.md")
