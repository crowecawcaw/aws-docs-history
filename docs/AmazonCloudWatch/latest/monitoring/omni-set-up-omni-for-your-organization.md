

# Set up Omni for your organization
<a name="omni-set-up-omni-for-your-organization"></a>

Use this guide to set up CloudWatch Omni across an AWS Organization. An administrator creates an Organization domain once from the management account, and then any member account can create its own space, automatically linked to the domain.

This provides a single sign-in URL for your organization and centralized identity provider configuration, and removes the need for each account to configure its own domain.

If you operate in a single AWS account, see [Set up Omni for a single account](omni-set-up-omni-for-a-single-account.md) instead.

**Note**  
Enabling Omni does not change or disable anything in CloudWatch. Your existing metrics, logs, alarms, dashboards, and Logs Insights queries keep working.

**Who does what**

Organization domain setup involves two roles:


| Role | What they do | 
| --- | --- | 
| Organization administrator | Creates the domain from the AWS Organizations management account. Chooses the domain name and configures the identity provider. | 
| Account owner (member account) | Creates a space in their own account and Region. The space is automatically linked to the Organization domain. Each member account does this independently. | 

**Part 1: Create the domain (Organization administrator)**

**Prerequisites**
+ Access to the AWS Organizations **management account** with permission to enable Omni and create a domain.
+ **Trusted access** between AWS Organizations and CloudWatch, enabled for your organization. Enabling trusted access requires the `organizations:EnableAWSServiceAccess` and `iam:CreateServiceLinkedRole` permissions. See [Amazon CloudWatch and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudwatch.html).
+ The AWS Region you want to work in.
+ **Note:** If you plan to use IAM Identity Center, the Organization domain must be created in the same Region as the primary Region of IAM Identity Center. If your member accounts need to create spaces in other Regions, enable [IAM Identity Center multi-Region replication](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html) to include your desired Regions.

**Choose your domain name**

Your domain name becomes part of a URL your whole team uses, and it identifies your organization in Omni.

The name must meet these requirements:
+ 3–63 characters using lowercase letters, numbers, and hyphens.
+ Must start and end with a letter or number.
+ Cannot contain consecutive hyphens.
+ Certain names are reserved, including AWS service names, Region-like names, and names beginning with `aws-`, `amazon-`, `cloudwatch-`, or `omni-`.
+ Must be unique across all CloudWatch domains.

After you create the domain, it is reachable at `https://<domain-name>.cloudwatch-omni.global.app.aws`.

**Create the domain**

1. Sign in to the **AWS Organizations management account**.

1. Open the Omni setup page in the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/home\#settings:/omni](https://console.aws.amazon.com/cloudwatch/home#settings:/omni).

1. Choose **Get started**.

1. Select **Organization domain**.

1. Enter your domain name.

1. Complete the permissions step. Omni creates the IAM roles it needs on your behalf.

1. When domain creation finishes, record your **domain name** and **domain URL**.

**Connect your identity provider**

You configure sign-in for your domain through AWS IAM Identity Center, so your team uses the identities you already manage, including an external provider such as Okta or Microsoft Entra ID connected to IAM Identity Center. You configure this at the domain, not per space.

**Important**  
Your IAM Identity Center instance and your domain must be in the **same AWS Region**. If they are not, you cannot configure sign-in for the domain. Enable [IAM Identity Center multi-Region replication](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html) to include the Region in which your Omni space is hosted.

If you do not connect an identity provider, your team can sign in to Omni using an IAM user or IAM role (for example, through a deep link from the CloudWatch console).

**Share the domain with your team**

Domain setup is complete. Member accounts can now create their own spaces. Each space is automatically linked to this domain. Share the domain URL (`https://<domain-name>.cloudwatch-omni.global.app.aws`) with account owners who need to create spaces.

**Part 2: Create a space in a member account**

This section is for **account owners** in member accounts. You create a space in your account and Region; the space is automatically linked to the Organization domain.

Only **one space** can exist in a given account and Region combination.

**Prerequisites**
+ An Organization domain must already exist for your AWS Organization. If it does not, ask your Organization administrator to create one (see Part 1).
+ Permission to create a space. Grant this to administrators only.
+ The AWS Region you want to work in. A space belongs to one Region, and your IAM Identity Center instance must be in that same Region. If your IAM Identity Center instance is in a different Region, enable [IAM Identity Center multi-Region replication](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html) to include your desired space Region.

**Create a space**

1. Open the Omni setup page in the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/home\#settings:/omni](https://console.aws.amazon.com/cloudwatch/home#settings:/omni).

1. Choose **Create space**.

1. Enter a space name and confirm the account and Region.

1. Complete the setup. Omni enables the capabilities described in the following section for your account and Region.

**Capabilities enabled when you create a space**

Setting up a space turns on the following CloudWatch capabilities in your account and Region. These are telemetry features, not permissions. For the IAM roles that space setup creates, see the "IAM roles created during space setup" section of this page.


| Capability | What it does | Learn more | 
| --- | --- | --- | 
| CloudWatch Dataset integration | Enables forwarding of your logs and traces to the CloudWatch Dataset, which makes them queryable and correlated together in Omni. You do not manage a separate store or change how you manage existing CloudWatch resources such as log groups. | [CloudWatch Omni](cloudwatch-omni.md) | 
| OTel metrics enrichment | Enriches AWS metrics with resource attributes in OpenTelemetry format and makes them queryable with PromQL. | [CloudWatch OTel metrics enrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTelEnrichment.html) | 
| OTel span ingestion | Enables trace and span ingestion so Omni can receive and correlate distributed traces. | [Enable CloudWatch transaction search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html) | 

These capabilities apply to telemetry received after you complete space setup. Enabling these capabilities does not incur charges on its own. Costs begin when telemetry flows through them. See [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

On the first enablement, Omni backfills your space with up to 7 days of existing CloudWatch logs and traces. Telemetry older than 7 days, and data encrypted with a customer managed AWS KMS key, are not included in the backfill.

**IAM roles created during space setup**

Space setup creates the following IAM roles in your account. Omni uses these roles to read and correlate your telemetry.


| IAM role | Purpose | 
| --- | --- | 
| CloudWatchOmniOperatorRole | Assumed by Omni to manage your space, query telemetry, and configure integrations. | 
| CloudWatchOmniDatasetIntegrationExecutionRole | Assumed by CloudWatch to make your telemetry available in Omni through the Dataset. | 
| AgentCoreEvaluationRole | Assumed by Amazon Bedrock AgentCore to run online AI agent evaluations on your telemetry. This role is optional: during setup you keep the default role, choose an existing role, or opt out. See [Online evaluations](omni-agents-online-evaluations.md). | 

**Centralize telemetry across accounts and Regions**

If your workloads span several AWS accounts, you can aggregate telemetry from those accounts into the account and Region that hosts your space. After centralization, you can monitor and investigate your telemetry across all of the source accounts and Regions from the same space.

You aggregate telemetry by creating [CloudWatch centralization rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html). A centralization rule specifies the **source accounts** and **source Regions** to collect from, and the **destination account** and Region to replicate into. Set the destination to the account and Region that hosts your space. Centralization rules require AWS Organizations and must be created from the management account or by a delegated administrator.

You can create centralization rules before or after you create the space. Centralized telemetry is available in the space after both the space and the rule are active.

For setup instructions, see [Cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) and [Cross-account cross-Region metrics centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatchMetrics_Centralization.html).

**What centralization adds to your space**
+ **Logs and metrics from all source accounts and Regions in one place** — Analyze and act on telemetry across all your accounts and Regions from the centralized account. See [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md) and [Alerts](omni-alerts.md).
+ **Application map spans accounts** — The application map includes services discovered from all source accounts (when Context Graph is enabled as part of your centralization rules), so you see cross-account dependencies. See [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md).

**What to know**
+ **Centralization does not backfill** — Only telemetry generated after the centralization rule is active is replicated to the destination.
+ **Cross-space queries are not supported** — Each space sees the telemetry centralized into its own account and Region. If you need to query across accounts, centralize their telemetry into one account rather than creating separate spaces.
+ **Trace centralization requires Transaction Search enablement for each source account** — To centralize traces, enable Transaction Search in all your source accounts. Trace centralization then happens automatically when logs centralization is enabled.
+ **Costs** — Centralization replicates telemetry into the destination account. Standard CloudWatch pricing applies to the replicated data. See [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Configure encryption (optional)**

By default, Omni manages the encryption of the data it stores for your space. To control encryption with your own key, configure a customer managed AWS KMS key on the space (when you create the space, or later by updating the space's encryption configuration).

The key must meet these requirements:
+ A symmetric encryption key (`ENCRYPT_DECRYPT` key usage), and enabled.
+ In the same AWS account and Region as the space.
+ The identity attaching the key must have `kms:Decrypt` and `kms:GenerateDataKey` permission on it. Both are checked when you attach the key, so a key granting only one is rejected at attach time rather than failing later on reads or writes. The error names the missing permission.

Data Omni stores for your space, such as dashboards, is encrypted under the key.

The key's own key policy must also allow CloudWatch Omni to use the key. For the statements the service needs and a complete sample key policy, see [Data encryption in CloudWatch Omni](omni-data-encryption-in-cloudwatch-omni.md).

**Next steps**
+ **Send telemetry** from your applications or agents. See [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).
+ **Add your team** and choose what each person can do. See [Control access to your space](omni-control-access-to-your-space.md).