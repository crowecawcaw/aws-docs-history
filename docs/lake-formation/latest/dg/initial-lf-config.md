

# Set up AWS Lake Formation
<a name="initial-lf-config"></a>

 The following sections provide information on setting up Lake Formation for the first time. Not all of the topics in this section are required to start using Lake Formation. You can use the instructions to set up the Lake Formation permissions model to manage your existing AWS Glue Data Catalog objects and data locations in Amazon Simple Storage Service (Amazon S3).

1. [Create a data lake administrator](#create-data-lake-admin)

1. [Change the default permission model or use hybrid access mode](#setup-change-cat-settings)

1. [Configure an Amazon S3 location for your data lake](#register-s3-location)

1. [Assign permissions to Lake Formation users](#permissions-lf-principal)

1. [Integrating IAM Identity Center](identity-center-integration.md)

1. [(Optional) External data filtering settings](#external-data-filter)

1. [(Optional) Grant access to the Data Catalog encryption key](#setup-encrypted-catalog)

1. [(Optional) Create an IAM role for workflows](#iam-create-blueprint-role)

This section shows you how to set up Lake Formation resources in two different ways:
+ Using an AWS CloudFormation template
+ Using the Lake Formation console

To set up Lake Formation using AWS console, go to [Create a data lake administrator](#create-data-lake-admin).

## Set up Lake Formation resources using CloudFormation template
<a name="lf-setup-cfn"></a>
**Note**  
The CloudFormation stack performs steps 1 to 6 of the above, except step 2 and 5. Perform [Change the default permission model or use hybrid access mode](#setup-change-cat-settings) and [Integrating IAM Identity Center](identity-center-integration.md) manually from the Lake Formation console.

1. Sign into the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/) as an IAM administrator in the US East (N. Virginia) Region.

1. Choose [Launch Stack](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://lf-public.s3.amazonaws.com/cfn/SettingUpLf.yaml).

1. Choose **Next** on the **Create stack** screen.

1. Enter a **Stack name.**

1. For **DatalakeAdminName** and **DatalakeAdminPassword**, enter your user name and password for data lake admin user.

1. For **DatalakeUser1Name** and **DatalakeUser1Password**, enter your user name and password for data lake analyst user.

1. For **DataLakeBucketName**, enter your new bucket name that will be created.

1. Choose **Next**.

1. On the next page, choose `I acknowledge that CloudFormation might create IAM resources with custom names` and choose **Next**.

1. Review the details on the final page and select **I acknowledge that AWS CloudFormation might create IAM resources.**

1. Choose **Create.**

   The stack creation can take up to two minutes.

**Clean up resources**

If you like to clean up the CloudFormation stack resources:

1. De-register the Amazon S3 bucket that your stack created and registered as a data lake location.

1. Delete the CloudFormation Stack. This will delete all the resources created by the stack.

## Create a data lake administrator
<a name="create-data-lake-admin"></a>

Data lake administrators are initially the only AWS Identity and Access Management (IAM) users or roles that can grant Lake Formation permissions on data locations and Data Catalog resources to any principal (including self). For more information about data lake administrator capabilities, see [Implicit Lake Formation permissions](implicit-permissions.md). By default, Lake Formation allows you to create upto 30 data lake administrators.

You can create a data lake administrator using the Lake Formation console or the `PutDataLakeSettings` operation of the Lake Formation API.

The following permissions are required to create a data lake administrator. The `Administrator` user has these permissions implicitly.
+ `lakeformation:PutDataLakeSettings`
+ `lakeformation:GetDataLakeSettings`

If you grant a user the `AWSLakeFormationDataAdmin` policy, that user will not be able to create additional Lake Formation administrator users.

**To create a data lake administrator (console)**

1. If the user who is to be a data lake administrator does not yet exist, use the IAM console to create it. Otherwise, choose an existing user who is to be the data lake administrator.
**Note**  
We recommend that you do not select an IAM administrative user (user with the `AdministratorAccess` AWS managed policy) to be the data lake administrator.

   Attach the following AWS managed policies to the user:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html)

1. Attach the following inline policy, which grants the data lake administrator permission to create the Lake Formation service-linked role. A suggested name for the policy is `LakeFormationSLR`.

   The service-linked role enables the data lake administrator to more easily register Amazon S3 locations with Lake Formation. For more information about the Lake Formation service-linked role, see [Using service-linked roles for Lake Formation](service-linked-roles.md).
**Important**  
In all the following policy, replace {{<account-id>}} with a valid AWS account number.

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "iam:CreateServiceLinkedRole",
               "Resource": "*",
               "Condition": {
                   "StringEquals": {
                       "iam:AWSServiceName": "lakeformation.amazonaws.com"
                   }
               }
           },
           {
               "Effect": "Allow",
               "Action": [
                   "iam:PutRolePolicy"
               ],
               "Resource": "arn:aws:iam::{{<account-id>}}:role/aws-service-role/lakeformation.amazonaws.com/AWSServiceRoleForLakeFormationDataAccess"
           }
       ]
   }
   ```

1. (Optional) Attach the following `PassRole` inline policy to the user. This policy enables the data lake administrator to create and run workflows. The `iam:PassRole` permission enables the workflow to assume the role `LakeFormationWorkflowRole` to create crawlers and jobs, and to attach the role to the created crawlers and jobs. A suggested name for the policy is `UserPassRole`.
**Important**  
Replace {{<account-id>}} with a valid AWS account number.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "PassRolePermissions",
               "Effect": "Allow",
               "Action": [
                   "iam:PassRole"
               ],
               "Resource": [
                   "arn:aws:iam::{{111122223333}}:role/LakeFormationWorkflowRole"
               ]
           }
       ]
   }
   ```

------

1. (Optional) Attach this additional inline policy if your account will be granting or receiving cross-account Lake Formation permissions. This policy enables the data lake administrator to view and accept AWS Resource Access Manager (AWS RAM) resource share invitations. Also, for data lake administrators in the AWS Organizations management account, the policy includes a permission to enable cross-account grants to organizations. For more information, see [Cross-account data sharing in Lake Formation](cross-account-permissions.md).

    A suggested name for the policy is `RAMAccess`.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "ram:AcceptResourceShareInvitation",
                   "ram:RejectResourceShareInvitation",
                   "ec2:DescribeAvailabilityZones",
                   "ram:EnableSharingWithAwsOrganization"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/) and sign in as a user with the `AdministratorAccess` AWS managed policy.

1. If a **Welcome to Lake Formation** window appears, choose the IAM user that you created or selected in Step 1, and then choose **Get started**.

1. If you do not see a **Welcome to Lake Formation** window, then perform the following steps to configure a Lake Formation Administrator.

   1. In the navigation pane, under **Administration**, choose **Administrative roles and tasks**. In the **Data lake administrators** section of the console page, choose **Add**. 

   1. In the **Add administrators** dialog box, under Access type, choose **Data lake administrator**. 

   1. For **IAM users and roles**, choose the IAM user that you created or selected in Step 1, and then choose **Save**.

## Change the default permission model or use hybrid access mode
<a name="setup-change-cat-settings"></a>

Lake Formation starts with the "Use only IAM access control" settings enabled for compatibility with existing AWS Glue Data Catalog behavior. This settings allows you to manage access to your data in the data lake and its metadata through IAM policies and Amazon S3 bucket policies. 

To ease the transition of data lake permissions from an IAM and Amazon S3 model to Lake Formation permissions, we recommend you to use hybrid access mode for Data Catalog. With the hybrid access mode, you have an incremental path where you can enable Lake Formation permissions for a specific set of users without interrupting other existing users or workloads.

For more information, see [Hybrid access mode](hybrid-access-mode.md).

Disable the default settings to move all existing users of a table to Lake Formation in a single step.

**Important**  
If you have existing AWS Glue Data Catalog databases and tables, do not follow the instructions in this section. Instead, follow the instructions in [Upgrading AWS Glue data permissions to the AWS Lake Formation model](upgrade-glue-lake-formation.md).

**Warning**  
If you have automation in place that creates databases and tables in the Data Catalog, the following steps might cause the automation and downstream extract, transform, and load (ETL) jobs to fail. Proceed only after you have either modified your existing processes or granted explicit Lake Formation permissions to the required principals. For information about Lake Formation permissions, see [Lake Formation permissions reference](lf-permissions-reference.md).

**To change the default Data Catalog settings**

1. Continue in the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/). Ensure that you are signed in as a user with the `AdministratorAccess` AWS managed policy.

1. Modify the Data Catalog settings:

   1. In the navigation pane, under **Administration**, choose **Data Catalog settings**.

   1. Clear both check boxes and choose **Save**.  
![The Data Catalog settings dialog box has the subtitle "Default permissions for newly created databases and tables," and has two check boxes, which are described in the text.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/settings-page.png)

1. Revoke `IAMAllowedPrincipals` permission for database creators.

   1. In the navigation pane, under **Administration**, choose **Administrative roles and tasks**.

   1. In the **Administrative roles and tasks** console page, in the **Database creators** section, select the `IAMAllowedPrincipals` group, and choose **Revoke**.

      The **Revoke** permissions dialog box appears, showing that `IAMAllowedPrincipals` has the **Create database** permission.

   1. Choose **Revoke**.

## Assign permissions to Lake Formation users
<a name="permissions-lf-principal"></a>

Create a user to have access to the data lake in AWS Lake Formation. This user has the least-privilege permissions to query the data lake.

For more information on creating users or groups, see [IAM identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the IAM User Guide.

**To attach permissions to a non-administrator user to access Lake Formation data**

1. Open the IAM console at [https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam) and sign in as a user with the `AdministratorAccess` AWS managed policy.

1. Choose **Users** or **User groups**. 

1. In the list, choose the name of the user or group to embed a policy in.

   Choose **Permissions**.

1. Choose **Add permissions**, and choose **Attach policies directly**. Enter `Athena` in the **Filter policies** text field. In the result list, check the box for `AmazonAthenaFullAccess`.

1. Choose the **Create policy** button. On the **Create policy** page, choose the **JSON** tab. Copy and paste the following code into the policy editor.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "lakeformation:GetDataAccess",
                   "glue:GetTable",
                   "glue:GetTables",
                   "glue:SearchTables",
                   "glue:GetDatabase",
                   "glue:GetDatabases",
                   "glue:GetPartitions",
                   "lakeformation:GetResourceLFTags",
                   "lakeformation:ListLFTags",
                   "lakeformation:GetLFTag",
                   "lakeformation:SearchTablesByLFTags",
                   "lakeformation:SearchDatabasesByLFTags"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Choose **Next** until you see the **Review policy** page. Enter a name for the policy, for example, `DatalakeUserBasic`. Choose **Create policy**, then close the **Policies** tab or browser window.

## Configure an Amazon S3 location for your data lake
<a name="register-s3-location"></a>

To use Lake Formation to manage and secure the data in your data lake, you must first register an Amazon S3 location. When you register a location, that Amazon S3 path and all folders under that path are registered, which enables Lake Formation to enforce storage level permissions. When the user requests data from an integrated engine like Amazon Athena, Lake Formation provides data access rather than using the users permissions.

When you register a location, you specify an IAM role that grants read/write permissions on that location. Lake Formation assumes that role when supplying temporary credentials to integrated AWS services that request access to data in the registered Amazon S3 location. You can specify either the Lake Formation service-linked role (SLR) or create your own role.

Use a custom role in the following situations:
+ You plan to publish metrics in Amazon CloudWatch Logs. The user-defined role must include a policy for adding logs in CloudWatch Logs and publishing metrics in addition to the SLR permissions. For an example inline policy that grants the necessary CloudWatch permissions, see [Requirements for roles used to register locations](registration-role.md).
+ The Amazon S3 location exists in a different account. For details, see [Registering an Amazon S3 location in another AWS account](register-cross-account.md).
+ The Amazon S3 location contains data encrypted with an AWS managed key. For details, see [Registering an encrypted Amazon S3 location](register-encrypted.md) and [Registering an encrypted Amazon S3 location across AWS accounts](register-cross-encrypted.md).
+ You plan to access the Amazon S3 location using Amazon EMR. For more information about the role requirements, see [IAM roles for Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-iam-role.html) in the *Amazon EMR Management Guide*.

The role that you choose must have the necessary permissions, as described in [Requirements for roles used to register locations](registration-role.md). For instructions on how to register an Amazon S3 location, see [Adding an Amazon S3 location to your data lake](register-data-lake.md).

## (Optional) External data filtering settings
<a name="external-data-filter"></a>

If you intend to analyze and process data in your data lake using third-party query engines, you must opt in to allow external engines to access data managed by Lake Formation. If you don't opt in, external engines will not be able to access data in Amazon S3 locations that are registered with Lake Formation.

Lake Formation supports column-level permissions to restrict access to specific columns in a table. Integrated analytic services like Amazon Athena, Amazon Redshift Spectrum, and Amazon EMR retrieve non-filtered table metadata from the AWS Glue Data Catalog. The actual filtering of columns in query responses is the responsibility of the integrated service. It's the responsibility of third-party administrators to properly handle permissions to avoid unauthorized access to data. 

**To opt in to allow third-party engines to access and filter data (console)**

1. Continue in the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/). Ensure that you are signed in as a principal that has the IAM permission on the Lake Formation `PutDataLakeSettings` API operation. The IAM administrator user that you created in [Sign up for an AWS account](getting-started-setup.md#sign-up-for-aws) has this permission.

1. In the navigation pane, under **Administration**, choose **Application integration settings**.

1. On the **Application integration settings** page, do the following:

   1. Check the box **Allow external engines to filter data in Amazon S3 locations registered with Lake Formation**.

   1.  Enter **Session tag values** defined for third-party engines. 

   1. For **AWS account IDs**, enter the account IDs from where third-party engines are allowed to access locations registered with Lake Formation. Press **Enter** after each account ID.

   1. Choose **Save**.

 To allow external engines to access data without session tag validation, see [Application integration for full table access](full-table-credential-vending.md) 

## (Optional) Grant access to the Data Catalog encryption key
<a name="setup-encrypted-catalog"></a>

If the AWS Glue Data Catalog is encrypted, grant AWS Identity and Access Management (IAM) permissions on the AWS KMS key to any principals who need to grant Lake Formation permissions on Data Catalog databases and tables.

For more information, see the *AWS Key Management Service Developer Guide*.

## (Optional) Create an IAM role for workflows
<a name="iam-create-blueprint-role"></a>

With AWS Lake Formation, you can import your data using *workflows* that are executed by AWS Glue crawlers. A workflow defines the data source and schedule to import data into your data lake. You can easily define workflows using the *blueprints*, or templates that Lake Formation provides.

When you create a workflow, you must assign it an AWS Identity and Access Management (IAM) role that grants Lake Formation the necessary permissions to ingest the data.

The following procedure assumes familiarity with IAM.

**To create an IAM role for workflows**

1. Open the IAM console at [https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam) and sign in as a user with the `AdministratorAccess` AWS managed policy.

1. In the navigation pane, choose **Roles**, then **Create role**.

1. On the **Create role** page, choose **AWS service**, and then choose **Glue**. Choose **Next**.

1. On the **Add permissions** page, search for the **AWSGlueServiceRole** managed policy, and select the checkbox next to the policy name in the list. Then complete the **Create role** wizard, naming the role `LFWorkflowRole`. To finish, choose **Create role**.

1. Back on the **Roles** page, search for `LFWorkflowRole`, and choose the role name.

1. On the role **Summary** page, under the **Permissions** tab, choose **Create inline policy**. On the **Create policy** screen, navigate to the JSON tab, and add the following inline policy. A suggested name for the policy is `LakeFormationWorkflow`.
**Important**  
In the following policy, replace {{<account-id>}} with a valid AWS account number.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                    "lakeformation:GetDataAccess",
                    "lakeformation:GrantPermissions"
                ],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": ["iam:PassRole"],
               "Resource": [
                   "arn:aws:iam::{{111122223333}}:role/LakeFormationWorkflowRole"
               ]
           }
       ]
   }
   ```

------

   The following are brief descriptions of the permissions in this policy:
   + `lakeformation:GetDataAccess` enables jobs created by the workflow to write to the target location.
   + `lakeformation:GrantPermissions` enables the workflow to grant the `SELECT` permission on target tables.
   + `iam:PassRole` enables the service to assume the role `LakeFormationWorkflowRole` to create crawlers and jobs (instances of workflows), and to attach the role to the created crawlers and jobs.

1. Verify that the role `LakeFormationWorkflowRole` has two policies attached.

1. If you are ingesting data that is outside the data lake location, add an inline policy granting permissions to read the source data.