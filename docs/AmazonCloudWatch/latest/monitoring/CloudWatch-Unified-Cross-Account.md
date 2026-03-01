# CloudWatch cross-account observability

With Amazon CloudWatch cross-account observability, you can monitor and troubleshoot applications
that span multiple accounts within a Region. Seamlessly search, visualize, and analyze your metrics, logs, traces, Application Signals services and service level objectives (SLOs), Application Insights applications, and internet monitors in any of the linked accounts without account boundaries.

Set up one or more AWS accounts as _monitoring accounts_ and link
them with multiple _source accounts_. A monitoring account is a central
AWS account that can view and interact with observability data generated from source
accounts. A source account is an individual AWS account that generates observability data
for the resources that reside in it. Source accounts share their observability data with the
monitoring account. The shared observability data can include the following types of
telemetry:

- Metrics in Amazon CloudWatch. You can choose to share the metrics from all namespaces with the monitoring account, or filter to a subset of namespaces.
- Log groups in Amazon CloudWatch Logs. You can choose to share all log groups with the monitoring account, or filter to a subset of log groups.
- Traces in AWS X-Ray
- Services and Service level objectives (SLOs) in Application Signals
- Applications in Amazon CloudWatch Application Insights
- Monitors in CloudWatch Internet Monitor
  To create links between monitoring accounts and source accounts, you can use the CloudWatch
  console. Alternatively, use the _Observability Access Manager_ commands
  in the AWS CLI and API. For more information, see [Observability Access Manager API
  Reference](../../../OAM/latest/APIReference/Welcome.md "../../../OAM/latest/APIReference/Welcome.md").

A _sink_ is a resource that represents an attachment point in a
monitoring account. Source accounts can link to the sink to share observability data. Each account
can have one sink per Region. Each
sink is managed by the monitoring account where it is located. An _observability
link_ is a resource that represents the link established between a source
account and a monitoring account. Links are managed by the source account.

For a video demonstration of setting up CloudWatch cross-account observability,
see the following video.

The next topic explains how to set up CloudWatch cross-account observability in both monitoring
accounts and source accounts. For information about the cross-account cross-Region
CloudWatch dashboard, see [Cross-account cross-Region CloudWatch console](Cross-Account-Cross-Region.md "Cross-Account-Cross-Region.md").

**Use Organizations for source accounts**

There are two options for linking source accounts to your monitoring account. You can use
one or both options.

- Use AWS Organizations to link accounts in an organization or organizational unit to the
  monitoring account.
- Connect individual AWS accounts to the monitoring account.
  We recommend that you use Organizations so that new AWS accounts created later in the
  organization are automatically onboarded to cross-account observability as source accounts.

**Details about linking monitoring accounts and source
accounts**

- Each monitoring account can be linked to as many as 100,000 source
  accounts.
- Each source account can share data with as many as five monitoring accounts.
- You can set up a single account as both a monitoring account and a source account.
  If you do, this account sends only the observability data from itself to its
  linked monitoring account. It does not relay the data from its source accounts.
- A monitoring account specifies which telemetry types can be shared with it. A
  source account specifies which telemetry types it wants to share.
  - If there are more telemetry types selected in the _monitoring
    account_ than in the source account, the accounts are linked.
    Only the data types that are selected in both accounts are shared.
  - If there are more telemetry types selected in the _source
    account_ than in the monitoring account, the link creation fails
    and nothing is shared.
  - A metric name doesn't appear in the monitoring account console until that metric
    emits new data points after the link is created.

- To remove a link between accounts, do so from the source account.
- To delete a sink in a monitoring account, you must first remove all links to that sink the
  monitoring account.
  **Pricing**

Cross-account observability in CloudWatch comes with no extra cost for logs and metrics, Application Signals, and the first
trace copy is free. For more information about pricing, see [Amazon CloudWatch
Pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing").

###### Contents

- [Link monitoring accounts with source accounts](CloudWatch-Unified-Cross-Account-Setup.md "CloudWatch-Unified-Cross-Account-Setup.md")
  - [Necessary permissions](CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-permissions "CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-permissions")
    - [Permissions needed to create links](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-permissions-setup "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-permissions-setup")
    - [Permissions needed to monitor across accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-permissions-monitor "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-permissions-monitor")

  - [Setup overview](CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-overview "CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-overview")
  - [Step 1: Set up a monitoring account](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-ConfigureMonitoringAccount "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-ConfigureMonitoringAccount")
  - [Step 2: (Optional) Download an CloudFormation template or URL](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-TemplateOrURL "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-TemplateOrURL")
  - [Step 3: Link the source accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-ConfigureSourceAccount "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-Setup-ConfigureSourceAccount")
    - [Use an CloudFormation template to set up all accounts in an organization or an organizational unit as source accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-OrgTemplate "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-OrgTemplate")
    - [Use an CloudFormation template to set up individual source accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-SingleTemplate "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-SingleTemplate")
    - [Use a URL to set up individual source accounts](CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-SingleURL "CloudWatch-Unified-Cross-Account-Setup.md#Unified-Cross-Account-SetupSource-SingleURL")

- [Manage monitoring accounts and source accounts](Unified-Cross-Account-Manage.md "Unified-Cross-Account-Manage.md")
  - [Link more source accounts to an existing monitoring account](Unified-Cross-Account-Manage.md#Unified-Cross-Account-Setup-AddSourceAccounts "Unified-Cross-Account-Manage.md#Unified-Cross-Account-Setup-AddSourceAccounts")
  - [Remove the link between a monitoring account and source account](Unified-Cross-Account-Manage.md#Unified-Cross-Account-Setup-UnlinkAccount "Unified-Cross-Account-Manage.md#Unified-Cross-Account-Setup-UnlinkAccount")
  - [View information about a monitoring account](Unified-Cross-Account-Manage.md#Unified-Cross-Account-Setup-ManageMonitoringAccount "Unified-Cross-Account-Manage.md#Unified-Cross-Account-Setup-ManageMonitoringAccount")
