

# Creating a data grant on AWS Data Exchange containing AWS Lake Formation data permission data sets (Preview)
<a name="data-grant-publish-LF-data-product"></a>

If you're interested in creating data grants containing AWS Lake Formation data permission data sets during this Preview, contact [AWS Support](https://console.aws.amazon.com/support/home#/case/create%3FissueType=customer-service).

An AWS Lake Formation data permission data set contains a set of LF-tags and permissions for data managed by AWS Lake Formation. When customers accept data grants containing Lake Formation data permissions, they are granted read-only access to the databases, tables, and columns associated with the LF-tags added to the data set.

As a data owner, you start by creating LF-tags in AWS Lake Formation and associating those tags with the data you want to make available to recipients. For more information about tagging your resources in Lake Formation, see [Lake Formation Tag-based access control](https://docs.aws.amazon.com/lake-formation/latest/dg/tag-based-access-control.html) in the *AWS Lake Formation Developer Guide*. Then you import those LF-tags and a set of data permissions into AWS Data Exchange as an asset. Recipients are granted access to the data associated with those LF-tags upon acceptance of the data grant.

The following topics describe the process of creating a data grant containing AWS Lake Formation data permissions. The process has the following steps:

**Topics**
+ [Step 1: Create an AWS Lake Formation data set (Preview)](#data-grant-create-LF-data-set)
+ [Step 2: Create an AWS Lake Formation data permission (Preview)](#data-grant-create-LF-data-permission)
+ [Step 3: Review and finalize](#data-grant-review-and-finalize-LF)
+ [Step 4: Create a revision](#data-grant-create-revision-LF)
+ [Step 5:Create a new data grant containing AWS Lake Formation data sets (Preview)](#data-grant-publish-LF-product)
+ [Considerations when creating data grants containing an AWS Lake Formation data permission data set (Preview)](#data-grant-considerations-LF-data-product)

## Step 1: Create an AWS Lake Formation data set (Preview)
<a name="data-grant-create-LF-data-set"></a>

**To create an AWS Lake Formation data set**

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. From the left navigation pane, under **My data**, choose **Products**.

1. In **Owned data sets**, choose **Create data set** to open the **Data set creation steps** wizard.

1. In **Select data set type**, choose **AWS Lake Formation data permission**.

1. In **Define data set**, enter a **Name** and **Description** for your data set. For more information, see [Data set best practices](data-sets.md#data-set-best-practices).

1. Under **Add tags – optional**, choose **Add new tag**.

1. Choose **Create data set** and continue.

## Step 2: Create an AWS Lake Formation data permission (Preview)
<a name="data-grant-create-LF-data-permission"></a>

AWS Data Exchange uses LF-Tags to grant data permissions. Choose the LF-Tags that are associated with the data you want to share to grant recipients permissions to the data.

**To create AWS Lake Formation data permission**

1. On the **Create Lake Formation data permission** page, choose **Add LF-Tag**.

1. Enter the **Key** and choose your LF-Tag **Values**.

1. Choose **Preview resource(s)** to view how your LF-Tags are interpreted.

   1. From **Preview resource(s)**, select your **Associated data catalog resource(s)**.
**Note**  
Make sure to revoke `IAMAllowedPrincipals` group on the following resources. For more information, see [Revoking IAM role temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html) in the *IAM User Guide*.

1. Review the interpretation of the LF-Tag expression in the dialog box below and **Permissions** associated with the data set.

1. For **Service access**, select your existing service role that allows AWS Data Exchange to assume the role and access, grant, and revoke entitlements to Lake Formation data permissions on your behalf. Then choose **Create Lake Formation data permission**. For more information about creating a role for an AWS service, see [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html).

## Step 3: Review and finalize
<a name="data-grant-review-and-finalize-LF"></a>

After creating your AWS Lake Formation data permission (Preview), you can **Review** and **finalize** your data set. 

**To review and finalize**

1. Review your **Data set details** and **Tags** in **Step 1** for accuracy.

1. Review your **LF-Tag expression(s)**, **Add another Lake Formation data permission** (optional), **Associated data catalog resource(s)**, and job details.
**Note**  
Job are deleted 90 days after they’re created.

1. Choose **Finalize**. 

## Step 4: Create a revision
<a name="data-grant-create-revision-LF"></a>

**To create a revision**

1. From the **Owned data sets** section, choose the data set for which you want to add a revision.

1. Choose the **Revisions** tab.

1. In the **Revisions** section, choose **Create revision**.

1. On the **Revise Lake Formation data permission** page, choose **Add LF-Tag**.

1. Review the **Permissions** for **Database** and **Table**.

1. From **Service access**, select an existing service role and then choose **Create Lake Formation data permission**. 

## Step 5:Create a new data grant containing AWS Lake Formation data sets (Preview)
<a name="data-grant-publish-LF-product"></a>

After you've created at least one data set and finalized a revision with assets, you're ready to create a data grant with an AWS Lake Formation data permission data set.

**To create a new data grant**

1. In the left navigation pane of the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange), under **Exchanged data grants**, choose **Sent data grants**.

1. From **Sent data grants**, choose **Create data grant** to open the **Define data grant** wizard.

1. In the **Select owned data set** section, select the check box next to the data set you want to add.
**Note**  
The data set you choose must have a finalized revision. Data sets without finalized revisions can't be added to data grants.  
Unlike with data sets included in data products which are shared on AWS Marketplace, data sets added to data grants have no revision access rules, meaning a recipient of a data grant, once the data grant is approved, will have access to all finalized revisions of a given data set (including historical revisions finalized prior to the data grant creation).

1. In the **Grant overview** section, enter information the recipient will see about your data grant, including the **Data grant name** and **Data grant description**.

1. Choose **Next**. 

   For more information, see [Product best practices in AWS Data Exchange](product-details.md).

1. In the **Recipient access information** section, under **AWS account ID**, enter the AWS account ID of the recipient account who should receive the data grant. .

1. Under **Access end date**, select a specific end date for when the data grant should expire or, if the grant should exist in perpetuity, select **No end date**. 

1. Choose **Next**.

1. In the **Review and send** section, review your data grant information.

1. If you're sure that you want to create the data grant and send it to the chosen recipient, choose **Create and send data grant**.

You've now completed the manual portion of creating a data grant. The data grant will show on the **Sent data grants** tab on the **Sent data grants** page showing its status as **Pending acceptance** until the recipient account accepts it.

## Considerations when creating data grants containing an AWS Lake Formation data permission data set (Preview)
<a name="data-grant-considerations-LF-data-product"></a>

To ensure an optimal receiver experience, we strongly advise against making any of the following modifications to any permissions where your product contains AWS Data Exchange for Lake Formation data sets (Preview).
+ We recommend not deleting or modifying IAM roles passed to AWS Data Exchange in active data grants containing AWS Lake Formation data sets. If you delete or modify such IAM roles, the following issues occur: 
  + AWS accounts that have access to the Lake Formation data permissions might retain access indefinitely.
  + AWS accounts that are the receivers of your data grant but have not yet received access to the Lake Formation data permissions will fail to receive access.

  AWS Data Exchange will not be liable for any IAM roles that you delete or modify. 
+ We recommend that you don’t revoke granted AWS Lake Formation data permissions from IAM roles passed to AWS Data Exchange in data grants containing AWS Lake Formation data sets. If you revoke granted data permissions from such IAM roles, the following issues occur:
  + AWS accounts that have access to the Lake Formation data permissions might retain access indefinitely.
  + AWS accounts that subscribe to your product but have not yet received access to the Lake Formation data permissions will fail to receive access.
+ We recommend not revoking granted AWS Lake Formation data permissions from AWS accounts with active data grants containing AWS Lake Formation data sets. If you revoke granted data permissions from AWS accounts which are the receivers of your data grant, those accounts will lose access, creating a poor customer experience.
+ We recommend setting the cross account version in your AWS Glue Data Catalog to version 3 when creating data grants containing AWS Lake Formation data sets. If you downgrade the cross account version of your Data Lake Catalog while having active data grants containing AWS Lake Formation data sets, the AWS accounts that are the receivers of your data grant, but have not yet received access to the Lake Formation data permissions, may fail to get access to the data.