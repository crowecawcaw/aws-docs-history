

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Sharing SSM documents
<a name="documents-ssm-sharing"></a>

You can share AWS Systems Manager (SSM) documents with other accounts in the same AWS Region in two ways. For new document sharing, we recommend using AWS Resource Access Manager (AWS RAM). With AWS RAM, you can share a document with an entire organization or organizational unit (OU) in AWS Organizations, or with individual AWS accounts. You can also manage all of your shares from the AWS RAM console. For more information, see [Share an SSM document using AWS RAM](#ssm-share-using-ram).

You can also share a document by using account permissions, the original sharing mechanism. With account permissions, you modify the document permissions directly to share a document privately with specific AWS account IDs, or publicly with everyone. Account-permission sharing remains supported. For more information, see [Share an SSM document using account permissions](#ssm-how-to-share).

If you already share documents by using account permissions, you can migrate those shares to AWS RAM. For more information, see [Migrate an existing shared document to AWS RAM](#migrate-shared-document-to-ram).

You can't share a document publicly and privately at the same time. You also can't use AWS RAM sharing and account-permission (`ModifyDocumentPermission`) sharing on the same document at the same time.

**Warning**  
Use shared SSM documents only from trusted sources. When using any shared document, carefully review the contents of the document before using it so that you understand how it will change the configuration of your instance. For more information about shared document best practices, see [Best practices for shared SSM documents](#best-practices-shared). 

**Limitations**  
As you begin working with SSM documents, be aware of the following limitations.
+ Only the owner can share a document.
+ Documents can be shared with other accounts in the same AWS Region only. Cross-Region sharing isn't supported.

**Important**  
In Systems Manager, an *Amazon-owned* SSM document is a document created and managed by Amazon Web Services itself. *Amazon-owned* documents include a prefix like `AWS-*` in the document name. The owner of the document is considered to be Amazon, not a specific user account within AWS. These documents are publicly available for all to use.

**Topics**
+ [Best practices for shared SSM documents](#best-practices-shared)
+ [Block public sharing for SSM documents](#block-public-access)
+ [Share an SSM document using AWS RAM](#ssm-share-using-ram)
+ [Share an SSM document using account permissions](#ssm-how-to-share)
+ [Using shared SSM documents](#using-shared-documents)

## Best practices for shared SSM documents
<a name="best-practices-shared"></a>

Review the following guidelines before you share or use a shared document. 

**Use AWS RAM to share documents (recommended)**  
For new document sharing, we recommend using AWS Resource Access Manager (AWS RAM) instead of the `ModifyDocumentPermission` API operation. When you share through AWS RAM, you can share a document with an entire organization or organizational unit (OU) in AWS Organizations instead of listing individual AWS account IDs. You can also manage access with a resource-based policy, and view and audit all of your shares in one place in the AWS RAM console. For steps, see [Share an SSM document using AWS RAM](#ssm-share-using-ram). Documents that you share with individual AWS account IDs by using `ModifyDocumentPermission` are still supported. To move a document that you already share to AWS RAM, see [Migrate an existing shared document to AWS RAM](#migrate-shared-document-to-ram).

**Remove sensitive information**  
Review your AWS Systems Manager (SSM) document carefully and remove any sensitive information. For example, verify that the document doesn't include your AWS credentials. If you share a document with specific individuals, those users can view the information in the document. If you share a document publicly, anyone can view the information in the document.

**Block public sharing for documents**  
Review all publicly shared SSM documents in your account and confirm whether you want to continue sharing them. To stop sharing a document with the public, you must modify the document permission setting as described in the [Modify permissions for a shared SSM document](#modify-permissions-shared) section of this topic. Turning on the block public sharing setting doesn't affect any documents you're currently sharing with the public. Unless your use case requires you to share documents with the public, we recommend turning on the block public sharing setting for your SSM documents in the **Preferences** section of the Systems Manager Documents console. Turning on this setting prevents unwanted access to your SSM documents. The block public sharing setting is an account level setting that can differ for each AWS Region.

**Restrict Run Command actions using an IAM trust policy**  
Create a restrictive AWS Identity and Access Management (IAM) policy for users who will have access to the document. The IAM policy determines which SSM documents a user can see in either the Amazon Elastic Compute Cloud (Amazon EC2) console or by calling `ListDocuments` using the AWS Command Line Interface (AWS CLI) or AWS Tools for Windows PowerShell. The policy also restricts the actions the user can perform with SSM documents. You can create a restrictive policy so that a user can only use specific documents. For more information, see [Customer managed policy examples](security_iam_id-based-policy-examples.md#customer-managed-policies).

**Use caution when using shared SSM documents**  
Review the contents of every document that is shared with you, especially public documents, to understand the commands that will be run on your instances. A document could intentionally or unintentionally have negative repercussions after it's run. If the document references an external network, review the external source before you use the document. 

**Send commands using the document hash**  
When you share a document, the system creates a Sha-256 hash and assigns it to the document. The system also saves a snapshot of the document content. When you send a command using a shared document, you can specify the hash in your command to make sure that the following conditions are true:  
+ You're running a command from the correct Systems Manager document
+ The content of the document hasn't changed since it was shared with you.
If the hash doesn't match the specified document or if the content of the shared document has changed, the command returns an `InvalidDocument` exception. The hash can't verify document content from external locations.

**Use the interpolation parameter to improve security**  
For `String` type parameters in your SSM documents, use the parameter and value `interpolationType": "ENV_VAR` to improve security against command injection attacks by treating parameter inputs as string literals rather than potentially executable commands. In this case, the agent creates an environment variable named `SSM_{{parameter-name}}` with the parameter's value. We recommend updating all your existing SSM documents that include `String` type parameters to include `"interpolationType": "ENV_VAR"`. For more information, see [Writing SSM document content](documents-creating-content.md#writing-ssm-doc-content).

## Block public sharing for SSM documents
<a name="block-public-access"></a>

Before you begin, review all publicly shared SSM documents in your AWS account and confirm whether you want to continue sharing them. To stop sharing an SSM document with the public, you must modify the document permission setting as described in the [Modify permissions for a shared SSM document](#modify-permissions-shared) section of this topic. Turning on the block public sharing setting doesn't affect any SSM documents you're currently sharing with the public. With the block public sharing setting enabled, you won’t be able to share any additional SSM documents with the public.

Unless your use case requires you to share documents with the public, we recommend turning on the block public sharing setting for your SSM documents. Turning on this setting prevents unwanted access to your SSM documents. The block public sharing setting is an account level setting that can differ for each AWS Region. Complete the following tasks to block public sharing for any SSM documents you're not currently sharing.

### Block public sharing (console)
<a name="block-public-access-console"></a>

**To block public sharing of your SSM documents**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Documents**.

1. Choose **Preferences**, and then choose **Edit** in the **Block public sharing** section.

1. Select the **Block public sharing** check box, and then choose **Save**. 

### Block public sharing (command line)
<a name="block-public-access-cli"></a>

Open the AWS Command Line Interface (AWS CLI) or AWS Tools for Windows PowerShell on your local computer and run the following command to block public sharing of your SSM documents.

------
#### [ Linux & macOS ]

```
aws ssm update-service-setting  \
    --setting-id /ssm/documents/console/public-sharing-permission \
    --setting-value Disable \
    --region '{{The AWS Region you want to block public sharing in}}'
```

------
#### [ Windows ]

```
aws ssm update-service-setting ^
    --setting-id /ssm/documents/console/public-sharing-permission ^
    --setting-value Disable ^
    --region "{{The AWS Region you want to block public sharing in}}"
```

------
#### [ PowerShell ]

```
Update-SSMServiceSetting `
    -SettingId /ssm/documents/console/public-sharing-permission `
    -SettingValue Disable `
    –Region {{The AWS Region you want to block public sharing in}}
```

------

Confirm the setting value was updated using the following command.

------
#### [ Linux & macOS ]

```
aws ssm get-service-setting   \
    --setting-id /ssm/documents/console/public-sharing-permission \
    --region {{The AWS Region you blocked public sharing in}}
```

------
#### [ Windows ]

```
aws ssm get-service-setting  ^
    --setting-id /ssm/documents/console/public-sharing-permission ^
    --region "{{The AWS Region you blocked public sharing in}}"
```

------
#### [ PowerShell ]

```
Get-SSMServiceSetting `
    -SettingId /ssm/documents/console/public-sharing-permission `
    -Region {{The AWS Region you blocked public sharing in}}
```

------

### Restricting access to block public sharing with IAM
<a name="block-public-access-changes-iam"></a>

You can create AWS Identity and Access Management (IAM) policies that restrict users from modifying the block public sharing setting. This prevents users from allowing unwanted access to your SSM documents. 

The following is an example of an IAM policy that prevents users from updating the block public sharing setting. To use this example, you must replace the example Amazon Web Services account ID with your own account ID.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "ssm:UpdateServiceSetting",
            "Resource": "arn:aws:ssm:*:{{444455556666}}:servicesetting/ssm/documents/console/public-sharing-permission"
        }
    ]
}
```

------

## Share an SSM document using AWS RAM
<a name="ssm-share-using-ram"></a>

AWS Resource Access Manager (AWS RAM) is the recommended way to share AWS Systems Manager (SSM) documents. With AWS RAM, you create a resource share that grants access to your document, and you manage all of your shares from the AWS RAM console. You can share an SSM document with the following three types of principals:
+ An entire organization in AWS Organizations.
+ An organizational unit (OU) in AWS Organizations.
+ Individual AWS accounts.

You can share a document only with accounts in the same AWS Region, and only the document owner can share a document. For more information about sharing with AWS RAM, see [Getting started with AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html) in the *AWS Resource Access Manager User Guide*.

**Important**  
When you share an SSM document by using AWS RAM, you share all versions of the document, not only the default version.

**Note**  
AWS RAM supports private sharing only. To share a document publicly, use the procedure in [Share an SSM document using account permissions](#ssm-how-to-share) instead.

**Note**  
When you share a document with an AWS account that is outside your organization, the consumer must accept the resource share invitation in AWS RAM before they can access the document. When you share within an organization that has AWS RAM sharing enabled, no invitation is required, and AWS RAM grants access automatically.

AWS RAM service quotas apply when you share SSM documents through AWS RAM. For more information, see [Service quotas for AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/service-quotas.html) in the *AWS Resource Access Manager User Guide*.

To manage an existing share (for example, to update principals or stop sharing a document that you shared through AWS RAM), see [Working with shared AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html) in the *AWS Resource Access Manager User Guide*.

### Share a document using AWS RAM (console)
<a name="ssm-share-using-ram-console"></a>

**To share a document using AWS RAM**

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/).

1. In the navigation pane, choose **Resource shares**, and then choose **Create resource share**.

1. For **Name**, enter a name for the resource share.

1. Under **Resources**, choose the resource type **SSM Documents**, and then select the document that you want to share.

1. (Optional) Under **Managed permissions**, review the managed permission that AWS RAM applies to the shared document.

1. Choose **Next**. Under **Principals**, add the organization, OUs, or AWS accounts that you want to share with. To share with your organization or an OU, you must enable sharing within AWS Organizations.

1. Choose **Next**, review your choices, and then choose **Create resource share**.

### Share a document using AWS RAM (command line)
<a name="ssm-share-using-ram-cli"></a>

Open the AWS Command Line Interface (AWS CLI) or AWS Tools for Windows PowerShell on your local computer and run the following command to share a document by creating an AWS RAM resource share. For the `--principals` parameter, specify an organization ARN, an OU ARN, or an AWS account ID.

------
#### [ Linux & macOS ]

```
aws ram create-resource-share \
    --name {{MyDocumentShare}} \
    --resource-arns arn:aws:ssm:{{region}}:{{account-id}}:document/{{document-name}} \
    --principals {{principal}}
```

------
#### [ Windows ]

```
aws ram create-resource-share ^
    --name {{MyDocumentShare}} ^
    --resource-arns arn:aws:ssm:{{region}}:{{account-id}}:document/{{document-name}} ^
    --principals {{principal}}
```

------

**Note**  
After you create a share, AWS RAM might take a few minutes to propagate the change before consuming accounts can see it.

### Migrate an existing shared document to AWS RAM
<a name="migrate-shared-document-to-ram"></a>

If you currently share a document by using account permissions (the `ModifyDocumentPermission` API operation), you can migrate it to an AWS RAM resource share by running the `AWS-MigrateSSMDocumentSharingToRAM` runbook. This AWS-owned AWS Systems Manager Automation runbook migrates a document from account-permission sharing to an AWS RAM resource share while preserving the document's existing consumers.

**Note**  
Running the `AWS-MigrateSSMDocumentSharingToRAM` runbook uses AWS Systems Manager Automation, which incurs charges. For more information, see [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/).

**Note**  
You can't migrate a document that is shared publicly, because AWS RAM supports private sharing only. If you specify a publicly shared document, the runbook fails. If you migrate all documents in the account, the runbook skips publicly shared documents. To migrate a publicly shared document, first stop sharing it publicly, and then share it with the accounts, organizational units (OUs), or organization that you want.

**Important**  
After you migrate a document, you manage sharing for that document through AWS RAM. The `ModifyDocumentPermission` and `DescribeDocumentPermission` API operations return a 4xx error for a migrated document. If the migration fails or is canceled, the runbook automatically rolls back the change.

**To migrate a document from its Permissions view (console)**

1. Open the AWS Systems Manager console and, in the navigation pane, choose **Documents**.

1. Choose the document that you want to migrate.

1. Choose the **Details** tab.

1. In the **Permissions** section, choose **Migrate to RAM**. Systems Manager opens the **Migrate to RAM** page, which helps you start the migration.

1. For **Documents to migrate**, select the documents to migrate. Select individual documents, or choose **All documents** to migrate every document in the account that uses account-permission sharing.

1. For **AutomationAssumeRole**, choose the IAM role that Systems Manager Automation assumes to run the migration.

1. (Optional) For **Organizational units**, add an organization ID or organizational unit (OU) ID to share the documents with.

1. Choose **Start migration**.

For the full list of parameters, the IAM permissions required for the `AutomationAssumeRole` role, and step-by-step instructions for running the runbook, see [AWS-MigrateSSMDocumentSharingToRAM](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-migratessmdocumentsharingtoram.html) in the AWS Systems Manager Automation runbook reference.

## Share an SSM document using account permissions
<a name="ssm-how-to-share"></a>

You can share AWS Systems Manager (SSM) documents by modifying the document permissions to grant access to specific AWS account IDs (private sharing) or to everyone (public sharing). You can share documents from the Systems Manager console, or programmatically by calling the `ModifyDocumentPermission` API operation using the AWS Command Line Interface (AWS CLI), AWS Tools for Windows PowerShell, or the AWS SDK. When you share documents from the console, you can share only the default version of the document. Before you share a document, get the AWS account IDs of the accounts that you want to share with. Specify these account IDs when you share the document.

**Note**  
For new document sharing, we recommend using AWS Resource Access Manager (AWS RAM) instead. With AWS RAM, you can share with an entire organization or OU and manage all of your shares in one place. For more information, see [Share an SSM document using AWS RAM](#ssm-share-using-ram).

**Limitations**  
Be aware of the following limitations when you share a document by using account permissions.
+ You must stop sharing a document before you can delete it. For more information, see [Modify permissions for a shared SSM document](#modify-permissions-shared).
+ You can share a document with a maximum of 1,000 AWS accounts. You can request an increase to this limit in the [Support Center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase). For **Limit type**, choose *EC2 Systems Manager* and describe your reason for the request.
+ You can publicly share a maximum of five SSM documents. You can request an increase to this limit in the [Support Center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase). For **Limit type**, choose *EC2 Systems Manager* and describe your reason for the request.

For more information about Systems Manager service quotas, see [AWS Systems Manager Service Quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm).

### Share a document (console)
<a name="share-using-console"></a>

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Documents**.

1. In the documents list, choose the document you want to share, and then choose **View details**. On the **Permissions** tab, verify that you're the document owner. Only a document owner can share a document.

1. Choose **Edit**.

1. To share the command publicly, choose **Public** and then choose **Save**. To share the command privately, choose **Private**, enter the AWS account ID, choose **Add permission**, and then choose **Save**. 

### Share a document (command line)
<a name="share-using-cli"></a>

The following procedure requires that you specify an AWS Region for your command line session.

1. Open the AWS CLI or AWS Tools for Windows PowerShell on your local computer and run the following command to specify your credentials. 

   In the following command, replace {{region}} with your own information. For a list of supported {{region}} values, see the **Region** column in [Systems Manager service endpoints](https://docs.aws.amazon.com/general/latest/gr/ssm.html#ssm_region) in the *Amazon Web Services General Reference*.

------
#### [ Linux & macOS ]

   ```
   aws config
   
   AWS Access Key ID: [{{your key}}]
   AWS Secret Access Key: [{{your key}}]
   Default region name: {{region}}
   Default output format [None]:
   ```

------
#### [ Windows ]

   ```
   aws config
   
   AWS Access Key ID: [{{your key}}]
   AWS Secret Access Key: [{{your key}}]
   Default region name: {{region}}
   Default output format [None]:
   ```

------
#### [ PowerShell ]

   ```
   Set-AWSCredentials –AccessKey {{your key}} –SecretKey {{your key}}
   Set-DefaultAWSRegion -Region {{region}}
   ```

------

1. Use the following command to view the permissions for the document.

------
#### [ Linux & macOS ]

   ```
   aws ssm describe-document-permission \
       --name {{document name}} \
       --permission-type Share
   ```

------
#### [ Windows ]

   ```
   aws ssm describe-document-permission ^
       --name {{document name}} ^
       --permission-type Share
   ```

------
#### [ PowerShell ]

   ```
   Get-SSMDocumentPermission `
       –Name {{document name}} `
       -PermissionType Share
   ```

------

1. Use the following command to modify the permissions for the document and share it. You must be the owner of the document to edit the permissions. Optionally, for documents shared with specific AWS account IDs, you can specify a version of the document you want to share using the `--shared-document-version` parameter. If you don't specify a version, the system shares the `Default` version of the document. If you share a document publicly (with `all`), all versions of the specified document are shared by default. The following example command privately shares the document with a specific individual, based on that person's AWS account ID.

------
#### [ Linux & macOS ]

   ```
   aws ssm modify-document-permission \
       --name {{document name}} \
       --permission-type Share \
       --account-ids-to-add {{AWS account ID}}
   ```

------
#### [ Windows ]

   ```
   aws ssm modify-document-permission ^
       --name {{document name}} ^
       --permission-type Share ^
       --account-ids-to-add {{AWS account ID}}
   ```

------
#### [ PowerShell ]

   ```
   Edit-SSMDocumentPermission `
       –Name {{document name}} `
       -PermissionType Share `
       -AccountIdsToAdd {{AWS account ID}}
   ```

------

1. Use the following command to share a document publicly.
**Note**  
If you share a document publicly (with `all`), all versions of the specified document are shared by default. 

------
#### [ Linux & macOS ]

   ```
   aws ssm modify-document-permission \
       --name {{document name}} \
       --permission-type Share \
       --account-ids-to-add 'all'
   ```

------
#### [ Windows ]

   ```
   aws ssm modify-document-permission ^
       --name {{document name}} ^
       --permission-type Share ^
       --account-ids-to-add "all"
   ```

------
#### [ PowerShell ]

   ```
   Edit-SSMDocumentPermission `
       -Name {{document name}} `
       -PermissionType Share `
       -AccountIdsToAdd ('all')
   ```

------

### Modify permissions for a shared SSM document
<a name="modify-permissions-shared"></a>

If you share a command, users can view and use that command until you either remove access to the AWS Systems Manager (SSM) document or delete the SSM document. However, you can't delete a document as long as it's shared. You must stop sharing it first and then delete it.

**Note**  
This section applies to documents that you shared by using account permissions. To manage a document that you shared through AWS RAM, see [Share an SSM document using AWS RAM](#ssm-share-using-ram).

#### Stop sharing a document (console)
<a name="unshare-using-console"></a>

**Stop sharing a document**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Documents**.

1. In the documents list, choose the document you want to stop sharing, and then choose the **Details**. In the **Permissions** section, verify that you're the document owner. Only a document owner can stop sharing a document.

1. Choose **Edit**.

1. Choose **X** to delete the AWS account ID that should no longer have access to the command, and then choose **Save**. 

#### Stop sharing a document (command line)
<a name="unshare-using-cli"></a>

Open the AWS CLI or AWS Tools for Windows PowerShell on your local computer and run the following command to stop sharing a document.

------
#### [ Linux & macOS ]

```
aws ssm modify-document-permission \
    --name {{document name}} \
    --permission-type Share \
    --account-ids-to-remove '{{AWS account ID}}'
```

------
#### [ Windows ]

```
aws ssm modify-document-permission ^
    --name {{document name}} ^
    --permission-type Share ^
    --account-ids-to-remove "{{AWS account ID}}"
```

------
#### [ PowerShell ]

```
Edit-SSMDocumentPermission `
    -Name {{document name}} `
    -PermissionType Share `
    –AccountIdsToRemove {{AWS account ID}}
```

------

## Using shared SSM documents
<a name="using-shared-documents"></a>

When you share an AWS Systems Manager (SSM) document, the system generates an Amazon Resource Name (ARN) and assigns it to the command. If you select and run a shared document from the Systems Manager console, you don't see the ARN. However, if you want to run a shared SSM document using a method other than the Systems Manager console, you must specify the full ARN of the document for the `DocumentName` request parameter. You're shown the full ARN for an SSM document when you run the command to list documents. 

**Note**  
You aren't required to specify ARNs for AWS public documents (documents that begin with `AWS-*`) or documents that you own.

### Use a shared SSM document (command line)
<a name="using-shared-documents-cli"></a>

 **To list all public SSM documents** 

------
#### [ Linux & macOS ]

```
aws ssm list-documents \
    --filters Key=Owner,Values=Public
```

------
#### [ Windows ]

```
aws ssm list-documents ^
    --filters Key=Owner,Values=Public
```

------
#### [ PowerShell ]

```
$filter = New-Object Amazon.SimpleSystemsManagement.Model.DocumentKeyValuesFilter
$filter.Key = "Owner"
$filter.Values = "Public"

Get-SSMDocumentList `
    -Filters @($filter)
```

------

 **To list private SSM documents that have been shared with you** 

------
#### [ Linux & macOS ]

```
aws ssm list-documents \
    --filters Key=Owner,Values=Private
```

------
#### [ Windows ]

```
aws ssm list-documents ^
    --filters Key=Owner,Values=Private
```

------
#### [ PowerShell ]

```
$filter = New-Object Amazon.SimpleSystemsManagement.Model.DocumentKeyValuesFilter
$filter.Key = "Owner"
$filter.Values = "Private"

Get-SSMDocumentList `
    -Filters @($filter)
```

------

 **To list all SSM documents available to you** 

------
#### [ Linux & macOS ]

```
aws ssm list-documents
```

------
#### [ Windows ]

```
aws ssm list-documents
```

------
#### [ PowerShell ]

```
Get-SSMDocumentList
```

------

 **To get information about an SSM document that has been shared with you** 

------
#### [ Linux & macOS ]

```
aws ssm describe-document \
    --name {{arn:aws:ssm:us-east-2:12345678912:document/documentName}}
```

------
#### [ Windows ]

```
aws ssm describe-document ^
    --name {{arn:aws:ssm:us-east-2:12345678912:document/documentName}}
```

------
#### [ PowerShell ]

```
Get-SSMDocumentDescription `
    –Name {{arn:aws:ssm:us-east-2:12345678912:document/documentName}}
```

------

 **To run a shared SSM document** 

------
#### [ Linux & macOS ]

```
aws ssm send-command \
    --document-name {{arn:aws:ssm:us-east-2:12345678912:document/documentName}} \
    --instance-ids {{ID}}
```

------
#### [ Windows ]

```
aws ssm send-command ^
    --document-name {{arn:aws:ssm:us-east-2:12345678912:document/documentName}} ^
    --instance-ids {{ID}}
```

------
#### [ PowerShell ]

```
Send-SSMCommand `
    –DocumentName {{arn:aws:ssm:us-east-2:12345678912:document/documentName}} `
    –InstanceIds {{ID}}
```

------