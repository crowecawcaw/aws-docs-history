**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Traffic overview dashboards for protection packs (web ACLs)

This section describes the protection pack (web ACL) traffic overview dashboards in the AWS WAF console. After
you associate a protection pack (web ACL) with one or more AWS resources and enable metrics for the protection pack (web ACL), you can access summaries
of the web traffic that the protection pack (web ACL) evaluates by going to the protection pack (web ACL)'s
**Traffic overview** tab in the AWS WAF console. The dashboards
include near real-time summaries of the Amazon CloudWatch metrics that AWS WAF collects when it
evaluates your application web traffic.

###### Note

If you don't see anything on the dashboards, make sure you have metrics enabled for the protection pack (web ACL).

The protection pack (web ACL)'s **Traffic overview** tab contains tabbed dashboards with the
following categories of information:

- **Top security insights** – Insights into your AWS WAF protections that AWS WAF
  obtains by directly querying the Amazon CloudWatch logs. The rest of the dashboard uses the CloudWatch metrics.
  These insights provide richer information, but incur the added costs of querying the
  CloudWatch logs. For information about the additional costs, see
  [Amazon CloudWatch Logs Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
- **All traffic** – All web requests that the protection pack (web ACL) evaluates.

The dashboard focus is on terminating actions, but you can view the matches for count
rules in the following locations:

    + **Top 10 rules** pane of this dashboard. Toggle **Switch to
     count action** to show count rule matches.
    + **Sampled requests** tab of the protection pack (web ACL) page. This new tab includes a
     graph of all rule matches. For information, see [Viewing a sample of web requests](web-acl-testing-view-sample.md "web-acl-testing-view-sample.md").

- **Anti-DDoS** – Web requests that the protection pack (web ACL) evaluates using the `AntiDDoSRuleSet` Anti-DDoS managed rule group.

This tab is only available if you're using this rule group in your protection pack (web ACL).

- **Bot Control** – Web requests that the protection pack (web ACL) evaluates using the
  Bot Control managed rule group.
- If you aren't using this rule group in your protection pack (web ACL), this tab shows the results of
  evaluating a sampling of your web traffic against the Bot Control rules. This
  gives you an idea of the bot traffic that your application receives and it's
  free of charge.

This rule group is part of the intelligent threat
mitigation options that AWS WAF offers. For more information, see [AWS WAF Bot Control](waf-bot-control.md "waf-bot-control.md") and [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md").

- **Account takeover prevention** – Web requests that the protection pack (web ACL) evaluates
  using the AWS WAF Fraud Control account takeover prevention (ATP) managed rule group. This tab is only
  available if you're using this rule group in your protection pack (web ACL).

The ATP rule group is part of the AWS WAF
intelligent threat mitigation offerings. For more information, see [AWS WAF Fraud Control account takeover prevention (ATP)](waf-atp.md "waf-atp.md") and [AWS WAF Fraud Control account takeover prevention (ATP) rule group](aws-managed-rule-groups-atp.md "aws-managed-rule-groups-atp.md").

- **Account creation fraud prevention** – Web requests that the protection pack (web ACL) evaluates
  using the AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group. This tab is only
  available if you're using this rule group in your protection pack (web ACL).

The ACFP rule group is part of the AWS WAF
intelligent threat mitigation offerings. For more information, see [AWS WAF Fraud Control account creation fraud prevention (ACFP)](waf-acfp.md "waf-acfp.md") and [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md").
The dashboards are based on the protection pack (web ACL)'s CloudWatch metrics, and the graphs provide access to
the corresponding metrics in CloudWatch. For the intelligent threat mitigation dashboards,
like Bot Control, the metrics used are primarily the label metrics.

- For a list of the metrics that AWS WAF provides, see [AWS WAF metrics and dimensions](waf-metrics.md "waf-metrics.md").
- For information about CloudWatch metrics,
  see the [Amazon CloudWatch User
  Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").
  The dashboards provide summaries of your traffic patterns for the terminating actions and
  date range that you select. The intelligent threat mitigation dashboards include
  requests that the corresponding managed rule group evaluated, regardless of whether
  the managed rule group itself applied the terminating action. For example, if
  Block is selected, the **Account takeover prevention** dashboard
  includes information for all web requests that were both evaluated by the ATP
  managed rule group and blocked at some point during the protection pack (web ACL) evaluation. The
  requests can be blocked by the ATP managed rule group, by a rule that ran after
  the rule group in the protection pack (web ACL), or by the protection pack (web ACL) default action.
