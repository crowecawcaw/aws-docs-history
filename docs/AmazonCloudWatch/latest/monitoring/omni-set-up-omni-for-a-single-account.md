

# Set up Omni for a single account
<a name="omni-set-up-omni-for-a-single-account"></a>

Use this guide to set up CloudWatch Omni in a single AWS account. You create an Account domain and a space together in one console session. When you finish, you have a working Omni space ready to receive telemetry.

If your organization uses multiple AWS accounts, see [Set up Omni for your organization](omni-set-up-omni-for-your-organization.md) instead.

**Prerequisites**
+ An AWS account with permission to access Amazon CloudWatch in the console.
+ Permission to enable Omni and create a domain and space. Grant this to administrators only.
+ Sign in to the AWS Region in which you want to enable Omni.
+ If you plan to use IAM Identity Center for sign-in, its instance must be in the same AWS Region as your domain.

**Choose your domain name**

Your domain name becomes part of a URL your whole team uses, and it identifies your organization in Omni.

The name must meet these requirements:
+ 3–63 characters using lowercase letters, numbers, and hyphens.
+ Must start and end with a letter or number.
+ Cannot contain consecutive hyphens.
+ Certain names are reserved, including AWS service names, Region-like names, and names beginning with `aws-`, `amazon-`, `cloudwatch-`, or `omni-`.
+ Must be unique across all CloudWatch domains.

After you create the domain, it is reachable at `https://<domain-name>.cloudwatch-omni.global.app.aws`.

**Set up your domain and space**

In the Account domain flow, domain creation and space creation happen together in one session.

1. Open the Omni setup page in the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/home\#settings:/omni](https://console.aws.amazon.com/cloudwatch/home#settings:/omni).

1. Choose **Get started**.

1. Select **Account domain**.

1. Enter your domain name.

1. Complete the permissions step. Omni creates the IAM roles it needs on your behalf.

1. When domain creation finishes, space setup continues automatically in the same flow.

1. Enter a space name and confirm the account and Region.

1. Complete the setup. Omni enables the capabilities described later on this page for your account and Region.

**Connect your identity provider (optional)**

You configure sign-in for your domain through AWS IAM Identity Center, so your team can use the identities you already manage, including an external provider such as Okta or Microsoft Entra ID connected to IAM Identity Center. You configure this at the domain, not per space.

**Important**  
Your IAM Identity Center instance and your domain must be in the **same AWS Region**. If they are not, you cannot configure sign-in for the domain. Enable [IAM Identity Center multi-Region replication](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html) to include the Region in which your Omni space is hosted.

If you do not connect an identity provider, your team can sign in to Omni using an IAM user or IAM role (for example, through a deep link from the CloudWatch console).

**Capabilities enabled when you create a space**

Setting up a space enables the following CloudWatch capabilities in your account and Region. You choose the optional capabilities during setup.


| Capability | What it does | Learn more | 
| --- | --- | --- | 
| CloudWatch Dataset integration | Enables forwarding of your logs and traces to the CloudWatch Dataset, which makes them queryable and correlated together in Omni. You do not manage a separate store or change how you manage existing CloudWatch resources such as log groups. | [CloudWatch Omni](cloudwatch-omni.md) | 
| OTel metrics enrichment | Enriches AWS metrics with resource attributes in OpenTelemetry format and makes them queryable with PromQL. | [CloudWatch OTel metrics enrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTelEnrichment.html) | 
| OTel span ingestion | Enables trace and span ingestion so Omni can receive and correlate distributed traces. | [Enable CloudWatch transaction search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html) | 

These capabilities apply to telemetry received after you complete space setup. Enabling OTel metrics enrichment and Transaction Search follows existing pricing for those capabilities. See [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

On the first enablement, Omni backfills your space with up to 7 days of existing CloudWatch logs and traces. Telemetry older than 7 days, and data encrypted with a customer managed AWS KMS key, are not included in the backfill.

**IAM roles created during setup**

Space setup creates the following IAM roles in your account. Omni uses these roles to read and correlate your telemetry.


| IAM role | Purpose | 
| --- | --- | 
| CloudWatchOmniOperatorRole | Assumed by Omni to manage your space, query telemetry, and configure integrations. | 
| CloudWatchOmniDatasetIntegrationExecutionRole | Assumed by CloudWatch to make your telemetry available in Omni through the Dataset. | 
| AgentCoreEvaluationRole | Assumed by Amazon Bedrock AgentCore to run online AI agent evaluations on your telemetry. This role is optional: during setup you keep the default role, choose an existing role, or opt out. See [Online evaluations](omni-agents-online-evaluations.md). | 

**Configure encryption (optional)**

By default, Omni manages the encryption of the data it stores for your space. To control encryption with your own key, configure a customer managed AWS KMS key on the space (when you create the space, or later by updating the space's encryption configuration).

The key must meet these requirements:
+ A symmetric encryption key (`ENCRYPT_DECRYPT` key usage), and enabled.
+ In the same AWS account and Region as the space.
+ The identity attaching the key must have `kms:Decrypt` and `kms:GenerateDataKey` permission on it. Both are checked when you attach the key, so a key granting only one is rejected at attach time rather than failing later on reads or writes. The error names the missing permission.

Data Omni stores for your space, such as dashboards, is encrypted under the key.

The key's own key policy must also allow CloudWatch Omni to use the key. For the statements the service needs and a complete sample key policy, see [Data encryption in CloudWatch Omni](omni-data-encryption-in-cloudwatch-omni.md).

**Next steps**

You now have a working Omni space.
+ **Send telemetry** from your applications or agents. See [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).
+ **Add your team** and choose what each person can do. See [Control access to your space](omni-control-access-to-your-space.md).