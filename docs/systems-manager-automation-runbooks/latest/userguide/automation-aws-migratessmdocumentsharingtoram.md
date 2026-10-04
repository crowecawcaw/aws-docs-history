

# `AWS-MigrateSSMDocumentSharingToRAM`
<a name="automation-aws-migratessmdocumentsharingtoram"></a>

The `AWS-MigrateSSMDocumentSharingToRAM` runbook migrates a Systems Manager document to an AWS Resource Access Manager (AWS RAM) resource share. The document moves from account-permission sharing, which you manage with the `ModifyDocumentPermission` API operation. The migration preserves the document's existing consumers. You can migrate a single document. You can also migrate every document in your account that uses account-permission sharing. To migrate all documents, specify `*` for the `DocumentName` parameter.

The runbook automatically rolls back the migration if it fails or is canceled, so your existing sharing configuration is restored.

We recommend that you complete the migration by using the **Migrate to RAM** page in the AWS Systems Manager console. This migration wizard selects the documents to migrate and sets the runbook parameters for you, which reduces the chance of error. For the steps, see [To migrate a document from its Permissions view (console)](#automation-aws-migratessmdocumentsharingtoram-wizard).

**Important**  
After a document is migrated to AWS RAM, the `ModifyDocumentPermission` and `DescribeDocumentPermission` API operations return a `4xx` error for that document. After migration, manage sharing for the document through AWS RAM.

**Note**  
Before you run this runbook, verify that the target document currently uses account-permission sharing and that you have configured the IAM permissions described in this topic.

**Note**  
You can't migrate a document that is shared publicly, because AWS RAM supports private sharing only. If you specify a publicly shared document for `DocumentName`, the runbook fails. If you migrate all documents by specifying `*`, the runbook skips publicly shared documents. To migrate a publicly shared document, first stop sharing it publicly, and then share it with the accounts, organizational units (OUs), or organization that you want.

Automation

Amazon
+ **DocumentName (Required):**
  + Description: (Required) The name of the Systems Manager document to migrate. Specify `*` to migrate all documents in the account that use account-permission sharing.
  + Type: `String`
+ **AutomationAssumeRole (Required):**
  + Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
  + Type: `String`
+ **OrganizationalUnits (Optional):**
  + Description: (Optional) A map of document name to a list of organizational unit IDs (`ou-*`) and organization IDs (`o-*`) to share the document with. Use the `*` key to set a default for documents that don't have their own entry. When you provide this parameter for a document, the migration grants access to the specified organizational units or organizations instead of enumerating individual accounts. This approach:
    + Keeps the resource share small.
    + Automatically grants access to accounts that later join the organizational unit or organization.
    + Helps you stay under the AWS RAM limit of 5,000 principal associations per resource share.
  + Type: `StringMap`

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-MigrateSSMDocumentSharingToRAM) 

The `AutomationAssumeRole` parameter requires a trust policy and a permissions policy. Attach the following trust policy so that Systems Manager Automation can assume the role.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ssm.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Attach the following permissions policy. The statements are organized into three groups so that you can grant only the permissions you need for your migration.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Group1AlwaysRequired",
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeDocumentPermission",
                "ssm:GetResourcePolicies",
                "ssm:PutResourcePolicy",
                "ssm:DeleteResourcePolicy",
                "ram:ListResources",
                "ram:GetResourceShares",
                "ram:PromoteResourceShareCreatedFromPolicy",
                "ram:DeleteResourceShare"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Group2BulkMigration",
            "Effect": "Allow",
            "Action": [
                "ssm:ListDocuments",
                "ssm:StartAutomationExecution",
                "ssm:GetAutomationExecution"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Group2BulkMigrationPassRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                }
            }
        },
        {
            "Sid": "Group3OrganizationalUnits",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization",
                "organizations:ListParents"
            ],
            "Resource": "*"
        }
    ]
}
```

**Note**  
**Group 1** is always required, for both single-document and bulk migration.
**Group 2** is required only for bulk migration (when you specify `*` for `DocumentName`). For bulk migration, the runbook lists your documents and starts one automation execution for each document, passing your role to each execution. Scope `iam:PassRole` to the `AutomationAssumeRole` role's own ARN as shown. Do not use `"Resource": "*"` for `iam:PassRole`. Replace `ACCOUNT_ID` and `ROLE_NAME` with your account ID and role name.
**Group 3** is required only when you use the `OrganizationalUnits` parameter to share with organizational units or organizations.

The **Migrate to RAM** page sets the runbook parameters for you.

1. Open the AWS Systems Manager console and, in the navigation pane, choose **Documents**.

1. Choose the document that you want to migrate.

1. Choose the **Details** tab.

1. In the **Permissions** section, choose **Migrate to RAM**. Systems Manager opens the **Migrate to RAM** page, which helps you set the parameters for the `AWS-MigrateSSMDocumentSharingToRAM` runbook.

1. For **Documents to migrate**, select the documents to migrate. Select individual documents, or choose **All documents** to migrate every document in the account that uses account-permission sharing. This sets the `DocumentName` parameter.

1. For **AutomationAssumeRole**, choose the IAM role that Systems Manager Automation assumes to run the migration. This sets the `AutomationAssumeRole` parameter.

1. (Optional) For **Organizational units**, add an organization ID or organizational unit (OU) ID to share the documents with. This sets the `OrganizationalUnits` parameter.

1. Choose **Start migration** to run the `AWS-MigrateSSMDocumentSharingToRAM` runbook.

**To run the automation (console)**

1. Open the AWS Systems Manager console and, in the navigation pane, choose **Automation**.

1. Choose **Execute automation**.

1. In the **Automation document** list, choose `AWS-MigrateSSMDocumentSharingToRAM`.

1. For the input parameters, enter values for `DocumentName` and `AutomationAssumeRole`, and optionally `OrganizationalUnits`.

1. Choose **Execute**.

**To run the automation (AWS CLI)**

```
aws ssm start-automation-execution \
    --document-name AWS-MigrateSSMDocumentSharingToRAM \
    --parameters '{"DocumentName":["MyDocument"],"AutomationAssumeRole":["arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME"]}'
```

**Note**  
Running this runbook uses Systems Manager Automation and incurs charges. For more information, see [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/).
+ [Sharing SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html)