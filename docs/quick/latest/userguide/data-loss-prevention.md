

# Data loss prevention
<a name="data-loss-prevention"></a>


|  | 
| --- |
|    Intended audience:  System administrators and Amazon Quick administrators  | 

Amazon Quick integrates with Microsoft Purview to enforce your organization's data loss prevention (DLP) policies. After you connect your Microsoft Purview tenant, Quick classifies and protects sensitive files shared through spaces, chat, and knowledge bases. Sensitive data stays within the boundaries that your organization's information governance policies define.

## Data loss prevention concepts
<a name="dlp-concepts"></a>

Before you configure DLP in Amazon Quick, familiarize yourself with the following concepts.

Sensitivity labels  
Sensitivity labels are classifications that you define in your Microsoft Purview tenant to describe the sensitivity level of content – for example, *Public*, *Confidential*, or *Highly Confidential*. You can organize labels hierarchically with parent labels and sub-labels (child labels).

Enforcement actions  
Enforcement actions define how Quick handles a file that carries a specific sensitivity label.  
+ **Block** – Quick rejects the file, and the file can't be shared or uploaded. You receive an error message.
+ **Warn** – In interactive capabilities, you see a warning message and can choose to proceed or cancel the upload.
+ **Allow** – Quick shares the file without restriction.

Default action  
The default action is the enforcement action that Quick applies to any file whose sensitivity label you haven't explicitly mapped to a specific action. You set the default action during configuration. The default action also covers new labels that you publish in Microsoft Purview after setup. Quick governs files that carry those labels right away, so nothing goes unprotected. To give a new label its own action, edit the configuration and map it explicitly.

Provider outage action  
The provider outage action determines how Quick handles files when the DLP provider (Microsoft Purview) is temporarily unavailable. You can set it to one of the following actions.  
+ **Block** – Quick rejects files until the provider is available again.
+ **Warn** – Quick permits files through and shows a warning during the outage.
+ **Allow** – Quick permits files through without restriction.

Capabilities  
Capabilities are the areas within Amazon Quick where Quick applies DLP enforcement.  
+ **Spaces** – Files that users upload to collaborative workspaces.
+ **Chat** – Files that users share through chat conversations.
+ **Knowledge bases** – Content synced through SharePoint, OneDrive, and other connectors.

Label inheritance  
In the label mapping configuration, you can assign a parent label an explicit action (Block or Warn) or leave it set to the default action. Sub-labels (child labels) inherit their parent label's action. A label that you haven't explicitly mapped follows its mapped parent label's action if one exists. Otherwise, your default action applies.

## Prerequisites
<a name="dlp-prerequisites"></a>

Prepare the following before you create a DLP configuration.

### Microsoft Purview sensitivity labels
<a name="dlp-prereq-labels"></a>

You must already publish your sensitivity labels (for example, *Public*, *Confidential*, and *Highly Confidential*) in your Microsoft Purview or Microsoft 365 tenant. Quick reads these labels live from your tenant.

### A Microsoft Entra ID app registration
<a name="dlp-prereq-app-registration"></a>

Register an application in Microsoft Entra ID (Azure AD) that Quick uses to read labels and classify files. Note the **Directory (tenant) ID** and **Application (client) ID**. Both are GUIDs that you need to create a client secret credential. You must grant the app registration the following API permissions.


| API permission | Type | Description | 
| --- | --- | --- | 
| UnifiedPolicy.Tenant.Read | Required | Read the unified data-protection policy for the tenant. | 
| SensitivityLabels.Read.All | Required | Read all sensitivity labels defined in the tenant. | 
| Files.Read.All | Optional | Required only if you use knowledge bases backed by SharePoint or OneDrive. | 

### An AWS Secrets Manager secret
<a name="dlp-prereq-secret"></a>

Store the Purview credentials in an AWS Secrets Manager secret in the same AWS account as your Quick account. Use the following JSON format for the secret value.

```
{
  "clientId": "abcdef12-3456-7890-abcd-ef1234567890",
  "clientSecret": "<client secret value>",
  "tenantId": "11111111-1111-1111-1111-111111111111"
}
```

**Note**  
Quick stores only the ARN of your secret. Quick reads your credentials at runtime and never displays them in the console, returns them from the API, or writes them to logs.

**Important**  
Use exactly these three key names: `clientId`, `clientSecret`, and `tenantId`. Quick looks up these keys verbatim, so a renamed or missing key causes validation to fail with a missing-fields error. Store the value as a single JSON object.

### Access for Quick to your secret
<a name="dlp-prereq-grant-access"></a>

Sign in to your AWS account as an administrator and open the Quick admin console. Then grant Quick permission to read your Secrets Manager secret.

1. Choose **Permissions**, and then choose **AWS resources**.

1. Select **AWS Secrets Manager** from the list of services.

1. Choose your secret.

1. Choose **Save**.

### Secrets encrypted with a customer managed KMS key
<a name="dlp-prereq-kms"></a>

If a customer managed KMS key encrypts your Secrets Manager secret, Quick also needs `kms:Decrypt` permission on that key, in addition to `secretsmanager:GetSecretValue`.

**Important**  
The **Permissions**, **AWS resources** page can't grant `kms:Decrypt`. Edit the Quick service role directly in IAM to add it. After you edit the role manually, you can no longer manage it from the **AWS resources** page in the admin console.

Add a statement like the following to the role. Replace the account ID, secret name, and key ID with your own.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [ "secretsmanager:GetSecretValue" ],
      "Resource": [
        "arn:aws:secretsmanager:<home-region>:<account-id>:secret:<secret-name>",
        "arn:aws:secretsmanager:<other-region>:<account-id>:secret:<secret-name>"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [ "kms:Decrypt" ],
      "Resource": [ "arn:aws:kms:<other-region>:<account-id>:key/<key-id>" ]
    }
  ]
}
```

### Replicating your secret across Regions
<a name="dlp-prereq-replicate"></a>

Quick reads your secret in every AWS Region where it evaluates files, so the secret must exist in each of those Regions. Replicate it by using **Replicate secret to other Regions** in the Secrets Manager console, and make sure the role grants access to every replica ARN.

If a customer managed KMS key doesn't encrypt the secret, replicating it is sufficient. If a customer managed KMS key encrypts the secret, use one of the following approaches.

**Option 1: Single-Region keys**

1. Replicate the secret to the other Region.

1. Detach the replica from the primary secret so that it becomes standalone.

1. Create a KMS key in the other Region.

1. Attach that key to the standalone secret.

1. Grant `kms:Decrypt` on the new key, as described in [Secrets encrypted with a customer managed KMS key](#dlp-prereq-kms).

**Option 2: Multi-Region key**

1. Create a multi-Region key in your home Region.

1. Set the multi-Region key as the encryption key on the secret.

1. Replicate the multi-Region key to the other Region.

1. Replicate the secret to that Region, and select the replicated multi-Region key as its encryption key.

1. Grant `kms:Decrypt` on the replica key, as described in [Secrets encrypted with a customer managed KMS key](#dlp-prereq-kms).

## Creating a DLP configuration
<a name="create-dlp-configuration"></a>

Sign in to the admin console. Choose **Governance**, choose **Data loss prevention**, and then choose **Create DLP configuration** to open the setup wizard. The wizard has four steps, listed in the navigation pane. The following table describes each step.


| Step | Name | Description | 
| --- | --- | --- | 
| 1 | Provider | Select the DLP provider (Microsoft Purview). | 
| 2 | Credentials | Name the configuration and connect to AWS Secrets Manager. | 
| 3 | Label mapping | Scope enforcement and map sensitivity labels to actions. | 
| 4 | Review | Confirm settings and activate the configuration. | 

### Step 1: Provider
<a name="dlp-step-provider"></a>

Select **Microsoft Purview** as the DLP provider, and then choose **Continue**.

### Step 2: Credentials
<a name="dlp-step-credentials"></a>

Enter the following information:
+ **Configuration name** – A descriptive name that the dashboard shows – for example, `Knowledge base DLP`.
+ **Secret ARN** – Paste the ARN of your Secrets Manager secret.
+ Choose **Validate** to connect to Purview with the secret and check the required read permissions.

**Note**  
Each required permission shows a green check when validation succeeds. If a permission is missing or the secret is invalid, Quick flags the issue inline so that you can correct it and retry.

**Important**  
You can't continue to the next step until validation succeeds. Verify that the app registration has all required API permissions and that the secret ARN is correct before you retry.

### Step 3: Label mapping
<a name="dlp-step-label-mapping"></a>

Map each sensitivity label to an action:
+ **Default action** – Choose the action that Quick applies to any label that you don't explicitly map. The options are **Block**, **Warn**, or **Allow**. A conservative starting point is **Block**.
+ **Sensitivity labels** – Quick loads the current list of labels from your Purview tenant. For each label, choose its action. Sub-labels inherit their parent's action. Choose **Refresh** if you recently changed labels in Purview and want to pull the latest list.
+ **Provider outage action** – Choose what Quick does when Purview is unreachable: **Block** (fail closed – safest), **Warn**, or **Allow** (fail open). For a knowledge base that holds sensitive material, **Block** is the recommended provider outage action.

Choose **Review**.

The following table describes the enforcement actions.

Allow  
The file proceeds normally. Quick applies no restrictions.

Warn  
The file proceeds, but Quick notifies you in interactive capabilities (Chat and Spaces) if it carries a sensitive label.

Block  
Quick rejects the file and doesn't ingest it into the Quick index.

### Step 4: Review
<a name="dlp-step-review"></a>

Review the summary – the provider, configuration name, authentication method, capabilities, the label-to-action breakdown, the default action, and the provider outage action. Choose the edit link next to any section to return to it.

Use the **Active** / **Inactive** toggle to set whether Quick enforces the configuration as soon as you create it (the default is **Active**). Quick saves an **Inactive** configuration but doesn't enforce it until you activate it. When you're ready, choose **Create**.

Your configuration now appears as a card on the **Data loss prevention** dashboard. If you leave it **Active**, Quick begins enforcing on new file uploads to your knowledge bases.

## How enforcement works
<a name="dlp-how-enforcement-works"></a>

When a file enters a Quick capability that an active DLP configuration protects, the following sequence occurs.

1. A file enters a protected Quick capability – for example, Quick ingests documents during a knowledge base sync.

1. Quick DLP retrieves the file's Microsoft Purview sensitivity label.

1. Quick matches the label against the label-to-action mapping in your configuration.

1. Quick applies the resulting action.
   + **Allow** – The file proceeds normally.
   + **Warn** – The file proceeds, but Quick notifies you in interactive capabilities (Chat and Spaces) if it carries a sensitive label.
   + **Block** – Quick rejects the file.

1. For a label that you haven't explicitly mapped, Quick checks for a mapped parent label. If a mapped parent exists, Quick uses that parent's action. Otherwise, it applies your **default action**. New labels that you publish in Purview after setup are also covered by the default action, so Quick governs them immediately. To give a new label its own action, edit the configuration and map it explicitly.

1. If Quick can't reach Purview, it applies your configured **provider outage action**.

**Tip**  
For a knowledge base that holds sensitive material, we recommend that you set both the default action and the provider outage action to **Block**. This prevents Quick from ingesting unlabeled files or files that arrive during a Purview outage.

## Enforcement by capability
<a name="dlp-enforcement-by-capability"></a>

DLP enforcement applies to three capabilities: **Chat**, **Spaces**, and **Knowledge bases**. The same actions apply in all three. What you see, and where Quick records the result, depends on whether Quick scans the file interactively or during a background sync.

### Interactive capabilities: Chat and Spaces
<a name="dlp-enforcement-interactive"></a>

Quick evaluates files as you share or upload them, while you wait for the result.
+ **Block** – Quick rejects the file, and you receive an error message.
+ **Warn** – You see a warning message and can choose to proceed or cancel.
+ **Allow** – Quick shares the file without restriction.

### Knowledge bases
<a name="dlp-enforcement-knowledge-bases"></a>

Quick evaluates files during ingestion, after a sync starts, so no user waits for the outcome. Two consequences follow.
+ **There is no warn prompt.** Quick ingests a file that carries a label mapped to **Warn**, and the **Warn** action has no user-visible effect on this capability.
+ **Results appear in the Quick Observability report.** To see what DLP did during a knowledge base sync, open the Quick Observability report for that sync. The report shows one status per file.

BLOCKED  
Quick didn't ingest the file into the index. A **BLOCKED** status can indicate DLP enforcement or an internal failure. The error message for internal failures is generic.

ADDED  
Quick ingested a new file. This status includes files that match **Warn** labels; the report doesn't show them separately.

MODIFIED  
Quick updated and re-ingested an existing file. Files that match **Warn** labels appear as **MODIFIED** if the file changed since the last sync.

## Testing your configuration
<a name="dlp-testing"></a>

From the configuration's card on the dashboard, choose the **Test** (file-scan) icon. Provide the Amazon S3 URI (for example, `s3://bucket/key`) of a labeled file, and confirm that it returns the expected Allow, Warn, or Block result before you rely on it in production.

**Note**  
The test action performs a dry run using the current label-to-action mapping. It doesn't modify the file or affect any live data.

## Managing configurations
<a name="dlp-managing-configurations"></a>

From each dashboard card, you can perform the following actions.
+ **Edit** (pencil icon) – Change credentials, capabilities, label mappings, the default action, or the provider outage action.
+ **Activate / Deactivate** (toggle) – Turn enforcement on or off. Deactivating asks for confirmation, because it stops protection for the covered capabilities.
+ **Delete** – Remove the configuration entirely (available from the edit view).

**Note**  
The dashboard card warns you when your Purview tenant has new labels that you haven't mapped yet. Until you map them, they follow your default action.

## Limits and validations
<a name="dlp-limits"></a>

The following limits apply to DLP in Amazon Quick.
+ **DLP configurations per account** – 10.
+ **Active DLP configurations per account** – 1.
+ **Maximum file size scanned** – 500 MB. Quick doesn't scan larger files.

### Supported file types
<a name="dlp-supported-file-types"></a>

Quick scans the file types that Microsoft Purview supports for labeling: Word, Excel, PowerPoint, PDF, Visio, Project, common image formats (JPEG, PNG, TIFF, DNG, PSD), XPS, Power BI (`.pbit`, `.pbix`), `.dwfx`, and email (`.msg`, `.eml`). For the authoritative list, see [supported file types](https://learn.microsoft.com/en-us/information-protection/develop/concept-supported-filetypes) on the Microsoft website.

One distinction matters when you read this list: only file types that Microsoft Purview supports *for labeling* are in scope. Quick doesn't scan files that require Azure Rights Management to decrypt, or file types that apply only to protected labels.

### Protected labels
<a name="dlp-protected-labels"></a>

If a file carries a label that has protection enabled, Quick doesn't scan the file and applies your default action instead. Protected labels don't appear in the label-mapping step in the admin console. You can still supply them through the `CreateDlpSetting` API, but the evaluation outcome is the same: the default action applies.

### When the default action applies
<a name="dlp-default-action-cases"></a>

Beyond labels that you haven't explicitly mapped, Quick falls back to your default action when any of the following is true:
+ The file carries no sensitivity label.
+ The file type isn't supported (see [Supported file types](#dlp-supported-file-types)).
+ The file exceeds the 500 MB size limit.
+ The file is empty (0 bytes).
+ The file carries a protected label.

**Note**  
In the public API, the default action is the `unmappedAction` field.

## Security best practices
<a name="dlp-security-best-practices"></a>
+ **Use a dedicated app registration for DLP.** Register a separate Microsoft Entra ID application for Quick DLP rather than reusing an app registration that serves other integrations. A dedicated registration lets you rotate or revoke its credentials independently and keeps its permission scope narrow.
+ **Grant only the permissions that DLP needs.** Scope the app registration to `SensitivityLabels.Read.All` and `UnifiedPolicy.Tenant.Read`. Add `Files.Read.All` only if you use knowledge bases backed by SharePoint or OneDrive; it isn't required to list or map labels.
+ **Keep credentials in Secrets Manager.** Quick stores only the ARN of your secret. Quick reads your credentials at runtime and never displays them in the console, returns them from the API, or writes them to logs.
+ **Monitor data loss prevention (DLP) activity.** Quick delivers a `DLP_LOGS` vended log to CloudWatch Logs, Amazon S3, or Firehose. Use it to audit DLP policy changes, including when enforcement was enabled or disabled and which principal made the change (`DLP_SETTING_*` events, `status`, and `last_updated_by`). You can also identify blocked, warned, or inspection-failed files by filtering on `event_type` and `failure_type`. For setup and the full schema, see [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md).

## API reference
<a name="dlp-api-reference"></a>

For programmatic management of DLP settings, see the Amazon Quick API Reference.

## Setting up Quick knowledge bases
<a name="dlp-setup-knowledge-bases"></a>

To set up Quick ingestion knowledge bases, follow the instructions for each connector:
+ [Google Drive knowledge base integration](google-drive-knowledge-base.md)
+ [Microsoft OneDrive knowledge base integration](onedrive-knowledge-base.md)
+ [Microsoft SharePoint knowledge base integration](sharepoint-knowledge-base.md)
+ [Web Crawler integration](web-crawler-integration.md)
+ [Amazon S3 integration](s3-integration.md)
+ [Atlassian Confluence Cloud knowledge base integration](confluence-knowledge-base.md)

## Troubleshooting
<a name="dlp-troubleshooting"></a>

The following table lists common issues and how to resolve them.

Validation fails with a permission error  
Verify that the app registration has `UnifiedPolicy.Tenant.Read` and `SensitivityLabels.Read.All` granted and admin-consented.

Secret ARN not found  
Confirm that the Secrets Manager secret exists in the same AWS account as Quick, and that you granted Quick access under **Permissions**, **AWS resources**.

The labels list is empty or outdated  
Use **Refresh** in Step 3 (Label mapping) to re-fetch the current label list from your Purview tenant.

Files are unexpectedly blocked during a knowledge base sync  
Check the Quick Observability report for the sync. A **BLOCKED** status can also indicate an internal failure rather than DLP enforcement. Check whether the file carries a label that you mapped to Block, whether the default action is Block, and the provider outage action if Purview was unreachable during the sync.