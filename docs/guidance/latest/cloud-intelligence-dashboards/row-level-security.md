

# Row Level Security
<a name="row-level-security"></a>

## Introduction
<a name="introduction"></a>

Cloud Intelligence Dashboards (CID) provide comprehensive visualization and analysis of AWS cost, usage, and operational data across your organization.

For enterprise customers implementing CID at organizational scale, maintaining the principle of least privilege is essential. Organizations need to ensure users can only access data from AWS accounts they are authorized to view. Amazon Quick [Row Level Security](https://docs.aws.amazon.com/quickSight/latest/user/restrict-access-to-a-data-set-using-row-level-security.html) (RLS) addresses this requirement by enabling fine-grained access control at the data level.

![RLS Overview](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/rls2/rls-overview.png)


This page covers a ready to use CID RLS solution, that you can install and easily configure for your needs. It also enables a wide range of customizations and integrations that you can build on top to adjust to your organization needs.

In the default configuration this solution allows:
+ Easily attribute permissions to Quick users and groups.
+ Use Account level granularity as well as setting permissions on the level of AWS Organization Unit.
+ Easily manage full visibility of permissions for users and groups (typically useful for FinOps and Security teams).

The solution also provides an RLS Dashboard that helps Amazon Quick Administrators easily evaluate and troubleshoot users permissions.

## RLS Dataset
<a name="rls-dataset"></a>

The RLS Dataset is a specialized dataset in Quick that controls data access based on user permissions. Users connect to dashboard as usual but if Dashboard Datasets are configured with RLS, RLS Dataset defines what data users will see on the dashboard.

![RLS Overview](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/rls2/rls-dataset.png)


RLS Dataset contains User and Group mapping to fields that are common in all datasets of the dashboard. In case of CID, by default we use `account_id` and `payer_id` as the common fields to establish Row Level permissions boundaries. You can fine tune this solution to use Tags or other fields but we recommend starting with the default.

For CID dashboards, RLS dataset requires four essential fields:
+  **UserName**: The Quick user identifier (must match exactly)
+  **GroupName**: The Quick group identifier
+  **account\_id**: Comma-separated list of AWS accounts the user/group can access
+  **payer\_account\_id**: Comma-separated list of billing accounts (management accounts)

CID provides ready to use RLS Dataset as a part of the RLS Dashboard, that helps you manage and control your RLS Dataset.

### Access Control Rules
<a name="access-control-rules"></a>

It is important to understand the RLS Dataset and how it works for different cases.
+  **No access**: Users not listed in the dataset will see empty dashboards
+  **Full access**: Users with empty `account_id` and `payer_account_id` fields have full data access (recommended for Security, FinOps and Platform teams)
+  **Organization access**: Users with empty `account_id` but populated `payer_account_id` have access to all accounts in the specified AWS Organization

You can create the RLS dataset manually in Quick or use the automated solution provided in this guide. Once created, use the CID-CMD tool to [apply RLS](#how-to-apply-rls) to all datasets of a specific dashboard.

## Source of RLS Data
<a name="source-of-rls-data"></a>

The RLS dataset maps users and groups to the AWS accounts they can access. This mapping information must be stored in a system that enables easy tracking and adjustment. CID supports three options:

1.  **AWS Organization Tags (Recommended)**: Stores access information in OU and Account Tags within your AWS Organization’s Management Account. Leverages existing AWS organizational structures but requires Management Account access. CID implements an “Hierarchical Tag” concept where Tags defined at higher levels of the OU hierarchy can be overridden by more specific Tag values at lower levels. This hierarchical approach enables flexible group ownership definition at high organizational levels while allowing for necessary exceptions that adapt to an existing organizational complexity.

1.  **Amazon Athena Inline Tables**: Create and edit tables directly within Athena as a low-effort option with significant flexibility. Does not require Management Account access.

1.  **CSV Files on Amazon S3**: Simple file-based mapping that doesn’t require Management Account access. Files can be generated as exports from existing Configuration Management Databases (CMDB) and identity providers.

## Architecture
<a name="architecture"></a>

![RLS Architecture](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/rls2/rls-archi.png)


The RLS implementation follows this workflow:

1.  **(Optional) Tag Configuration**: Organization Admin sets OU or Account Tags in AWS Console with the following Tag keys:

   1.  `cid_users`: Colon-separated (`:`) list of user emails (must match Quick exactly)

   1.  `cid_groups`: Colon-separated (`:`) list of Quick groups with access

   1. Users and groups with Management Account access inherit access to all organization accounts

1.  **(Optional) Organization Data Collection**: Lambda function in Data Collection Stack assumes a role in Management Account, retrieves account and OU information, and stores it in S3

1.  **Quick Sight Data Collection**: Lambda function collects user information from Amazon Quick in the local account and stores it in the same S3 bucket

1.  **RLS Dataset Formation**: Glue Tables and Athena Views create the RLS dataset based on AWS Organization Tags and Quick data

1.  **RLS Application**: CID Admin applies RLS to all datasets using the CID-CMD tool

1.  **Access Control**: Users see only data from accounts configured for their Quick group or user

1.  **(Optional) Admin Override**: CID Admin can manage full admin lists or override mapping using Athena Inline Tables

## How It Works Under the Hood
<a name="how-it-works-under-the-hood"></a>

CID constructs an RLS dataset from several sources.

### Click to learn more about how it works
<a name="collapsible-section-rls-1"></a>

![RLS Details](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/rls2/rls-views-details.png)


1.  **full\_access\_users** - is a view or a table that contains a list of emails of users who are supposed to have a full unrestricted access to protected datasets. This view can be edited in Athena directly (https://docs.aws.amazon.com/athena/latest/ug/views-managing.html) as an [inline table](https://prestodb.io/docs/current/sql/values.htm) or it can be replaced with tables that come from other sources (your identity management or a simple csv file on Amazon S3). We do not recommend using individual users for this and rather prioritize user management with groups, but it can be handy on the initial setup phase. Please make sure you put exactly the same email as you have in Quick.

1.  **full\_access\_groups** - is a view or a table that contains a list of Quick Groups with users who will to have a full unrestricted access to protected datasets. This view can be edited in Athena directly (https://docs.aws.amazon.com/athena/latest/ug/views-managing.html) as an [inline table](https://prestodb.io/docs/current/sql/values.htm) or it can be replaced with tables that come from other sources (your identity management or a simple csv file on Amazon S3).

1.  **account\_access** - a view or a table that has the following fields:

   1.  `account_id` - AWS Account Id (12 digits)

   1.  `payer_account_id` - an AWS Management Account Id. Users and groups that have access to the `account_id` == `payer_id` will have access to all accounts under the AWS Organization with this management account id. The tool supports multiple AWS Organizations.

   1.  `emails` - a list of emails of users who will have access to the account information (note that it is not a comma separated list but it must be Athena type `ARRAY<VARCHAR>`)

   1.  `groups` - a list of Quick Groups who will have access to the account information (note that it is not a comma separated list but it must be Athena type `ARRAY<VARCHAR>`)

1.  **permission view** - is a union of several sub tables based on **full\_access\_users**, **full\_access\_groups** and **account\_access**. It results in the following fields:

   1.  `email` - email of users

   1.  `group` - a Quick Group

   1.  `payer_account_id` - a comma separated list of accounts

   1.  `account_id` - a comma separated list of accounts

1.  **quickSight\_users** table contains emails and UserName of QS User.

1.  **rls\_view** is the final form and represents the same fields as **permission view** but instead of user email it will have the QS User Names needed for RLS Dataset.

**Note**  
if both `payer_account_id` and `account_id` are empty then the user or the group in this line will have a full access
if only `payer_account_id` is provided but `account_id` is empty, the user or the group will have access to all accounts in the AWS Organization of the given payer Account
If user/group is not present in the table, no access will be granted - user will see an empty dashboard

## Deployment
<a name="deployment"></a>

## Prerequisites
<a name="prerequisites"></a>

Before implementing RLS, ensure you have:

1.  **(Recommended) Quick Sight Configuration**: [Identity Source/SSO](sso-application-legacy.md) configured for your Quick environment

1.  **CID Foundation**: [Foundational dashboards](cudos-cid-kpi.md) already installed

1.  **Account Access**: Admin access to the Data Collection/Dashboard Account

1.  **Management Account Access** (Optional): Required only for AWS Organization Tags option. Alternative options available if not accessible

1.  **Data Collection Stack** (Recommended): Preferably installed, but minimal setup instructions provided if needed

## Step 1: Define Your RLS Data Source and Deploy
<a name="step-1-define-your-rls-data-source-and-deploy"></a>

Choose one of the three options described [above](#source-of-rls-data) to define your RLS data source:

### Option 1: Using AWS Organization Tags in Management Account(s)
<a name="collapsible-section-rls-8"></a>

If you already have the [CID Data Collection Stack](data-collection.md) you can just check if Quick Sight (IncludeQuickSightModule parameter) and OrganizationData (IncludeOrgDataModule parameter) modules are activated, and continue to the next step.

Here we will use the minimal setup for managing access from AWS Organization OU and Account Tags.

1. Login to Management Account(s) and install the Permission Stack by clicking Launch Stack below

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?&templateURL=https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-read-permissions.yaml&stackName=CidDataCollectionReadPermissionsStack&param_DataCollectionAccountID=REPLACE%20WITH%20DATA%20COLLECTION%20ACCOUNT%20ID%20OR%20EMPTY&param_AllowModuleReadInMgmt=no&param_OrganizationalUnitID=REPLACE%20WITH%20ORGANIZATIONAL%20UNIT%20ID%20OR%20EMPTY&param_IncludeBackupModule=no&param_IncludeBudgetsModule=no&param_IncludeComputeOptimizerModule=no&param_IncludeCostAnomalyModule=no&param_IncludeECSChargebackModule=no&param_IncludeInventoryCollectorModule=no&param_IncludeRDSUtilizationModule=no&param_IncludeRightsizingModule=no&param_IncludeTAModule=no&param_IncludeTransitGatewayModule=no&param_IncludeHealthEventsModule=no&param_IncludeCostOptimizationHubModule=no&param_IncludeLicenseManagerModule=no) 

1. Login to Data Collection/Dashboard Account and install the Data Collection Stack by clicking Launch Stack below. Put Management Account Ids parameter as a comma separated list of your Management Accounts. Make sure you’ve set to 'yes' Quick (IncludeQuickSightModule parameter) and OrganizationData (IncludeOrgDataModule parameter) modules.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?&templateURL=https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-collection.yaml&stackName=CidDataCollectionStack&param_ManagementAccountID=REPLACE%20WITH%20MANAGEMENT%20ACCOUNT%20ID&param_IncludeTAModule=no&param_IncludeRightsizingModule=no&param_IncludeCostAnomalyModule=no&param_IncludeInventoryCollectorModule=no&param_IncludeComputeOptimizerModule=no&param_IncludeECSChargebackModule=no&param_IncludeRDSUtilizationModule=no&param_IncludeOrgDataModule=yes&param_IncludeBudgetsModule=no&param_IncludeTransitGatewayModule=no&param_IncludeHealthEventsModule=no&param_IncludeQuickSightModule=yes) 

1. Once installed, you can go to AWS Organization in the Management Account and configure tags as follows:

   1.  `cid_groups` as colon-separated (`:`) Quick Groups.

   1. and/or `cid_users` as colon-separated (`:`) emails of individual users

1. After update you can launch execution of the data collection by triggering `CID-DC-organizations-StateMachine` and `CID-DC-quicksight-StateMachine` [StepFunctions](https://console.aws.amazon.com/states/home).

1. You can validate data using the following query:

   ```
   SELECT * FROM "optimization_data"."organization_data"
   SELECT * FROM "optimization_data"."quicksight_user_data"
   SELECT * FROM "optimization_data"."quicksight_group_data" -- can be empty if you don't have Quick groups
   SELECT * FROM "optimization_data"."quicksight_groupmembership_data" -- can be empty if you don't have Quick groups
   ```

### Option 2: Using Amazon Athena Inline Tables
<a name="collapsible-section-rls-9"></a>

The Data Collection is needed to collect data from local Quick account and store on the local S3 bucket.

1. Login to Data Collection/Dashboard Account and install the Data Collection Stack by clicking Launch Stack below. If you have already [CID Data Collection Stack](data-collection.md) you can just check if Quick and OrgData modules are activated, and continue to the next item.

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?&templateURL=https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-collection.yaml&stackName=CidDataCollectionStack&param_ManagementAccountID=&param_IncludeTAModule=no&param_IncludeRightsizingModule=no&param_IncludeCostAnomalyModule=no&param_IncludeInventoryCollectorModule=no&param_IncludeComputeOptimizerModule=no&param_IncludeECSChargebackModule=no&param_IncludeRDSUtilizationModule=no&param_IncludeOrgDataModule=no&param_IncludeBudgetsModule=no&param_IncludeTransitGatewayModule=no&param_IncludeHealthEventsModule=no&param_IncludeQuickSightModule=yes) 

1. Create an inline Athena Table that simulates Data Collection organization\_data, but can be edited directly in Athena to manage access.

   ```
   CREATE OR REPLACE VIEW "optimization_data"."organization_data" AS
   WITH accounts AS (
     SELECT *
     FROM (
       VALUES
         ROW ('1111111111111111', '1111111111111111', ARRAY['user11@e.mail', 'user12@e.mail'], ARRAY['group11', 'group12'])
       , ROW ('2222222222222222', '1111111111111111', ARRAY['user21@e.mail', 'user22@e.mail'], ARRAY['group21', 'group22'])
       , ROW ('3333333333333333', '1111111111111111', ARRAY['user31@e.mail', 'user32@e.mail'], ARRAY['group31', 'group32'])
     )  ignored_table_name ("account_id", "payer_account_id", "emails", "groups")
   )
   SELECT
     account_id as Id,
     payer_account_id as ManagementAccountId,
     ARRAY[
       CAST(ROW('cid_users', array_join("emails", ':')) AS ROW(key VARCHAR, value VARCHAR)),
       CAST(ROW('cid_groups', array_join("groups", ':')) AS ROW(key VARCHAR, value VARCHAR))
     ] as HierarchyTags
   FROM accounts
   ```

### Option 3: Use CSV file on Amazon S3
<a name="collapsible-section-rls-3"></a>

1. Login to Data Collection/Dashboard Account and install the Data Collection Stack by clicking Launch Stack below

    [![Launch Stack button](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?&templateURL=https://aws-managed-cost-intelligence-dashboards-us-east-1.s3.amazonaws.com/cfn/data-collection/deploy-data-collection.yaml&stackName=CidDataCollectionStack&param_ManagementAccountID=&param_IncludeTAModule=no&param_IncludeRightsizingModule=no&param_IncludeCostAnomalyModule=no&param_IncludeInventoryCollectorModule=no&param_IncludeComputeOptimizerModule=no&param_IncludeECSChargebackModule=no&param_IncludeRDSUtilizationModule=no&param_IncludeOrgDataModule=no&param_IncludeBudgetsModule=no&param_IncludeTransitGatewayModule=no&param_IncludeHealthEventsModule=no&param_IncludeQuickSightModule=yes) 

1. Create a CSV file (ex: `file.csv`):

   ```
   account_id, payer_account_id, emails, groups
   1111111111111111, 1111111111111111, user11@e.mail:user12@e.mail, group11:group12
   2222222222222222, 1111111111111111, user21@e.mail:user12@e.mail,
   3333333333333333, 1111111111111111,, group31:group32
   ```

1. Upload CSV file to an Amazon S3 Bucket. Please use an existing Bucket that Quick already has access to. Example: `cid-{account-id}-data-exports` or `cid-data-{account-id}`. You can use either the web interface or the command line:

   ```
   account_id=$(aws sts get-caller-identity --query "Account" --output text)
   aws s3 cp ./file.csv s3://cid-data-${account_id}/my_accounts/file.csv
   ```

1. Login to AWS Console, select Athena Service and Create a Table:

   ```
   CREATE EXTERNAL TABLE optimization_data.my_accounts (
       "account_id" string,
       "payer_account_id" string,
       "emails" string,
       "groups" string
   )
   ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
   WITH SERDEPROPERTIES (
       'separatorChar' = ',',
       'quoteChar' = '"',
       'escapeChar' = '\\'
   )
   STORED AS TEXTFILE
   LOCATION 's3://cid-data-${account_id}/my_accounts/' -- REPLACE ${account_id} WITH YOUR ACCOUNT ID
   TBLPROPERTIES (
       'has_encrypted_data'='false',
       'skip.header.line.count'='1'
   );
   ```

1. Verify the table

   ```
   SELECT * FROM "optimization_data"."my_accounts"
   ```

1. Create a view that simulates organization\_data table

   ```
   CREATE OR REPLACE VIEW "optimization_data"."organization_data" AS
   SELECT
     account_id as Id,
     payer_account_id as ManagementAccountId,
     ARRAY[
       CAST(ROW('cid_users',  "emails") AS ROW(key VARCHAR, value VARCHAR)),
       CAST(ROW('cid_groups', "groups") AS ROW(key VARCHAR, value VARCHAR))
     ] as HierarchyTags
   FROM "optimization_data"."my_accounts"
   ```

## Step 2: Install RLS Dashboard and Verify Configuration
<a name="step-2-install-rls-dashboard-and-verify-configuration"></a>

### Expand
<a name="collapsible-section-rls-4"></a>

1.  **Access Terminal**: Login to Amazon CloudShell or use your local terminal

1.  **Install CID-CMD Tool**:

   ```
   pip3 install -U cid-cmd
   ```

1.  **Deploy RLS Dashboard**:

   ```
   cid-cmd deploy --dashboard-id cid-rls
   ```

1.  **Verify Dashboard**: Check the dashboard in Quick. Ensure the dataset updates and displays data (may take several minutes after deployment)

1.  **Configure Admin Access**: Edit Athena views **full\_access\_users** and **full\_access\_groups** replace placeholders with your admin users and groups for full dashboard access. After modifying data, refresh the `rls_dataset` dataset.

## Step 3: Apply RLS to Dashboards
<a name="step-3-apply-rls-to-dashboards"></a>

### Expand
<a name="collapsible-section-rls-5"></a>

1.  **Access Terminal**: Login to Amazon CloudShell or use your local terminal

1.  **Install CID-CMD Tool** (if not already installed):

   ```
   pip3 install -U cid-cmd
   ```

1.  **Enable RLS**: Update dashboard with RLS enabled. The tool will guide you through selecting the dashboard and RLS dataset, then update all associated datasets:

   ```
   cid-cmd update --force --recursive --rls ENABLED
   ```

1.  **RLS Management Options**:
   + Disable RLS: `--rls DISABLED` 
   + Remove RLS: `--rls CLEAR` 

## FAQ / Operations Guide
<a name="faq-operations-guide"></a>

### How can I verify the access rights?
<a name="how-can-i-verify-the-access-rights"></a>
+  **Review RLS Dataset**: Open the RLS Dashboard and verify the content of the RLS dataset
+  **Test with Additional User**: Create an additional Quick user for testing (note: additional costs apply, delete after testing)

### How can I manage users and groups with full access?
<a name="how-can-i-manage-users-and-groups-with-full-access"></a>
+  **Athena Views**: Edit the **full\_access\_users** and **full\_access\_groups** views in Athena as inline tables
+  **Dataset Refresh**: After modifications, refresh the `cid_rls` dataset in Quick
+  **CSV Alternative**: Configure a CSV file on S3 for more flexibility (views remain customizable and won’t be overwritten during updates)

### How do I apply RLS to other dashboards?
<a name="how-to-apply-rls"></a>

Use the CID-CMD tool to enable RLS on any dashboard:

```
cid-cmd update --force --recursive --rls ENABLED
```

 **Management Options**: \* Disable: `--rls DISABLED` \* Remove: `--rls CLEAR` 

### How do I check the RLS status for all datasets?
<a name="how-do-i-check-the-rls-status-for-all-datasets"></a>

Use the CID-CMD status command:

```
cid-cmd status
```

### How can I configure mapping between user groups and business units?
<a name="how-can-i-configure-mapping-between-user-groups-and-business-units"></a>

This guide focuses on AWS Account ID-based access, but you can adapt it for [Organizational Taxonomy](add-org-taxonomy.md):
+ Use Account Tags or Resource Tags for business unit mapping
+ Create a custom RLS dataset with **UserName**, **GroupName**, and the same field configured as dashboard [Organizational Taxonomy](add-org-taxonomy.md) 

## Authors
<a name="authors"></a>
+ Stephanie Gooch, Sr. Commercial Architect, AWS OPTICS
+ Veaceslav Mindru, Sr. Technical Account Manager, AWS
+ Iakov Gan, Ex-Amazonian
+ Yin Lei, Sr. Technical Account Manager, AWS
+ Yuriy Prykhodko, Principal Technical Account Manager, AWS

## Feedback
<a name="feedback"></a>

Follow [Feedback & Support](feedback-support.md).