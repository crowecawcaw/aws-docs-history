# Troubleshooting in Amazon SageMaker Unified Studio

## Troubleshooting issues related to

subscriptions in Amazon SageMaker Unified Studio

This topic contains troubleshooting instructions for issues that you might have
when subscribing to assets in Amazon SageMaker Unified Studio.

| Error message                                                                                                                        | Resolution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unable to assume the IAM role `role-arn`.                                                                                            | This error occurs when Amazon SageMaker Unified Studio cannot assume the IAM role needed for creating<br>permissions to grant access to assets. To fix the issue, go to the AWS Identity and Access Management console in<br>the account where your data asset exists and ensure the IAM role in the error message<br>has a trust relationship with Amazon DataZone service principal as shown<br>in the following policy.<br>``<br>{<br>"Effect": "Allow",<br>"Principal": {<br>"Service": "datazone.amazonaws.com"<br>},<br>"Action": [<br>"sts:AssumeRole",<br>"sts:SetContext"<br>],<br>"Condition": {<br>"StringEquals": {<br>"aws:SourceAccount": `accountID`<br>}<br>}<br>}<br>``                                                                                                                                                                        |
| The IAM role `role-arn` does not have the necessary permissions to read the metadata<br>of the asset you are trying to subscribe to. | This error occurs when Amazon SageMaker Unified Studio is able to assume the IAM role but the<br>role does not have the necessary permissions. To fix this issue, go to the IAM<br>console in the account where your data asset exists and make sure that the role you<br>see in the error message has the [SageMakerStudioProjectUserRolePolicy](../adminguide/security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md "../adminguide/security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md")<br>attached to it.                                                                                                                                                                                                                                                                                                                               |
| Asset is a resource link. Amazon SageMaker Unified Studio does not support subscriptions to resource links.                          | This error occurs because you cannot subscribe to AWS Glue table resource links in<br>Amazon SageMaker Unified Studio. Choose a different asset type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Asset is not managed by Lake Formation.                                                                                              | This error occurs when the AWS Lake Formation permissions are not enforced<br>on the asset you are trying to publish. This happens because the Amazon S3 location<br>of the asset is not registered in Lake Formation.<br>• To fix the issue, log into the Lake Formation console in the account<br>where the table exists.<br>• Register the Amazon S3 location in **Lake Formation mode**<br>or **Hybrid mode**.<br>• Ensure that the `IAMAllowedPrincipals` group is not added in the table's<br>Lake Formation permissions.<br>NoteIf you use encrypted Amazon S3 buckets or cross-account setups, you may<br>need to adjust your AWS KMS and S3 settings. For more information, see [Adding<br>an Amazon S3 location to your data lake](../../../lake-formation/latest/dg/register-data-lake.md "../../../lake-formation/latest/dg/register-data-lake.md") |
| IAM role `role-name` does not have necessary<br>Lake Formation permissions to grant access to this asset.                            | This error occurs when the IAM role in the error message does not have<br>the necessary permissions for Amazon SageMaker Unified Studio to manage permissions<br>on the published table. You can resolve the issue by granting the following<br>AWS Lake Formation permissions to the the IAM role on the table<br>you are looking to publish.<br>1. `Grant Describe` and `Describe Grantable` on<br>the database where the tables exist.<br>2. `Describe`, `Select`, `Describe Grantable`,<br>and `Select Grantable` on the all the tables in the above database<br>that you want Amazon SageMaker Unified Studio to manage access on your behalf.                                                                                                                                                                                                             |

## Amazon EBS Volume Depletion with Local Notebook Execution

**Question**

“Enhance the StartExecution API response when throttling occurs due to low disk space,
instructing the user to delete files from the jobs folder."

**Answer**

1. Navigate to JupyterLab
2. In the Jobs folder, select the folder and files
3. Select delete

##

Domain

**Question**

From IAM SSO access portal URL, SAmazon SageMaker Unified Studio is not listed. When I click on Amazon DataZone, Amazon DataZone portal is shown.
I clicked on SIGN IN WITH SSO, it failed due to Invalid redirectUri provided.

**Answer**

Visit DAmazon DataZone console, choose your domain, then click the Amazon SageMaker Unified Studio URL.

##

SAML Identity Provider Email Issue

**Question**

When using 3rd party SAML identity providers, the domain creation flow does not identify my email address.

**Answer**

This happens because during the user provisioning step, the email field was not populated in your local SSO instance. When sync-ing with 3rd party SAML identity providers, modify the default mapping to ensure it includes the "email" field and re-do the sync.

##

Project Creation Failure

**Question**

When I configure a project profile with resources pointing to another region/account, and try to create a new project using the project profile, it failed due to the error Project creation failed because one or more resources could not be provisioned.

**Answer**

Make sure that you complete following configurations:

1. Domain owner account: In the Domains menu, choose your domain. Under the Account associations tab, verify that domain is associated with the target account, and the status is Associated.
2. Target account: In the Associated domains menu, choose the associated domain. Choose your blueprint. Under the Regions tab, verify that the target region is added. Under the Authorization tab, verify that the target domain unit is shown.
3. Domain owner account: In the Domain details, under the Project profiles tab, choose your project profile. Under the Blueprint deployment settings tab, choose Name of your blueprint, under Deployment order, verify that Account ID and Region are configured correctly. Under the Authorized users and groups, verify that your SSO user is added.

##

Data Explorer Visibility Issue

**Question**

On the data explorer, I cannot see my existing databases and tables on Glue Data Catalog. How can I query them?

**Answer**

Amazon SageMaker Unified Studio configures AWS IAM permissions and permission boundaries. You can optionally remove the permission boundaries to allow access to the existing databases and tables.

##

Data Catalog Visibility Issue

**Question**

On the data catalog, I cannot see my existing databases and tables on Glue Data Catalog. How can I view them?

**Answer**

1. On your project page, choose Data sources.
2. Choose CREATE DATA SOURCE to add the existing databases and tables as a data source.
3. For Data source type, choose AWS Glue, and choose NEXT.
4. Configure how to select your databases and tables here.
5. Once everything is filled, choose NEXT and go ahead to register the data sources.

##

Connection to Amazon RDS MySQL in Existing VPC

**Question**

I want to connect to my Amazon RDS MySQL database instance that exists in my existing VPC. When I add a connection, I do not see any settings about VPC. How can I configure the reachability?

**Answer**

Amazon SageMaker Unified Studio uses the VPC and subnets that are specified in the domain creation. If you have the data source in a separate VPC, you can configure network reachability between the domain VPC and the data source VPC using VPC peering or Transit Gateway, or alternatively you can create a new domain using the data source VPC.

##

Visual ETL Flow Column Selection

**Question**

I created a data source, and now I am adding a new transform on top of it. But I cannot choose the columns for the transform.

**Answer**

When you start authoring a visual ETL flow, the data preview is also started. Once the preview is completed, then schema is automatically collected and available for further transforms.

## Invalid or expired auth token when accessing an IDE

**Question**

When I tried to access an IDE in Amazon SageMaker Unified Studio I got an invalid or expired auth token error message. How do I resolve this?

**Answer**

This issue often occurs when third-party cookies are blocked. Amazon SageMaker Unified Studio uses the third-party cookies for
authenticating into a Amazon SageMaker Unified Studio IDE since the IDE is hosted in a separate domain from the primary site.
To help resolve this issue, ensure that third-party cookies are allowed in your browser.

###### Note

To do this in Safari, go to **Preferences** or **Settings** and ensure that on the **Privacy** page,
the box next to **Prevent cross-site tracking** is unchecked.

For more information, see the following sites:

- For Firefox, see [Third-party cookies and Firefox tracking protection](https://support.mozilla.org/en-US/kb/third-party-cookies-firefox-tracking-protection "https://support.mozilla.org/en-US/kb/third-party-cookies-firefox-tracking-protection").
- For Safari, see [Prevent cross-site tracking in Safari on Mac](https://support.apple.com/en-kz/guide/safari/sfri40732/mac "https://support.apple.com/en-kz/guide/safari/sfri40732/mac").
- For Chrome, see [Delete, allow and manage cookies in Chrome](https://support.google.com/chrome/answer/95647?sjid=9420235265489401566-NC "https://support.google.com/chrome/answer/95647?sjid=9420235265489401566-NC").
- For Edge, see [Manage cookies in Microsoft Edge: View, allow, block, delete and use](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_blockthirdpartycookies "https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_blockthirdpartycookies").

##

JupyterLab Configure Magic Error

**Question**

When I ran %%configure magic, it returned the error Connection name cannot be empty.

**Answer**

The magic syntax is different from Glue Interactive Session's existing kernel. Instead, run the magic with following syntax:

```

%%configure --name (compute) (-f)
{
"key": "value"
}

```

For example, if you want to change the default Spark SQL catalog name for project default Spark connection, run following magic:

```

%%configure --name project.spark --f
{
"--conf": "spark.sql.defaultCatalog=glue_catalog"
}

```
