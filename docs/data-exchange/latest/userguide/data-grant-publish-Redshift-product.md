# Create a data grant on AWS Data Exchange containing

Amazon Redshift data sets

An Amazon Redshift data set contains AWS Data Exchange datashares for Amazon Redshift. When customers subscribe to a product
containing datashares, they are granted read-only access to the tables, views, schemas, and
user-defined functions that a data owner adds to the datashare.

As a data owner, you create an AWS Data Exchange for Amazon Redshift datashare in your cluster. Then, you add to
the datashare the schemas, tables, views, and user-defined functions that you want the
recipient to access. You then import the datashare to AWS Data Exchange, create a data set, add it to a
data grant. Recipients are granted access to the datashare upon acceptance of the data grant
request.

After you have set up your Amazon Redshift datashare in Amazon Redshift, you can create a new Amazon Redshift data set in
AWS Data Exchange. You can then create a revision, and add Amazon Redshift datashare assets. This allows requests to
the AWS Data Exchange endpoint to proxy through to your Amazon Redshift datashare. You can then add this data set to
a data grant.

The following topics describe the process of creating an Amazon Redshift data set and a data grant
containig it using the AWS Data Exchange console. The process has the following steps:

###### Steps

- [Step 1: Create an Amazon Redshift datashare asset](#data-grant-create-RS-asset "#data-grant-create-RS-asset")
- [Step 2: Create an Amazon Redshift data set](#data-grant-create-RS-data-set "#data-grant-create-RS-data-set")
- [Step 3: Create a revision](#data-grant-create-RS-revision "#data-grant-create-RS-revision")
- [Step 4: Add Amazon Redshift datashare assets to a
  revision](#data-grant-add-RS-assets "#data-grant-add-RS-assets")
- [Step 5: Create a new data grant](#data-grant-publish-RS-product "#data-grant-publish-RS-product")

## Step 1: Create an Amazon Redshift datashare asset

Assets are the data in AWS Data Exchange. For more information, see [Assets](data-sets.md#assets "data-sets.md#assets").

###### To create an Amazon Redshift datashare asset

1. Create a datashare within your Amazon Redshift cluster.

For more information about how to create a datashare, see _Working with AWS Data Exchange datashares as a producer_ in the [Amazon Redshift Database Developer
Guide](../../../redshift/latest/dg/welcome.md "../../../redshift/latest/dg/welcome.md").

###### Note

We recommend setting your datashare as publicly accessible. If you do not,
customers with publicly accessible clusters will not be able to consume your
data. 2. [Step 2: Create an Amazon Redshift data set](publish-Redshift-product.md#create-RS-data-set "publish-Redshift-product.md#create-RS-data-set").

## Step 2: Create an Amazon Redshift data set

An Amazon Redshift data set includes AWS Data Exchange datashares for Amazon Redshift. For more information, see [Amazon Redshift data set](data-sets.md#RS-data-set-type "data-sets.md#RS-data-set-type").

###### To create an Amazon Redshift data set

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. On the left side navigation pane, under **My data**, choose
   **Owned data sets**.
3. In **Owned data sets**, choose **Create data set**
   to open the **Data set creation steps** wizard.
4. In **Select data set type**, choose **Amazon Redshift
   datashare**.
5. In **Define data set**, enter a **Name** and
   **Description** for your data set. For more information, see [Data set best practices](data-sets.md#data-set-best-practices "data-sets.md#data-set-best-practices").
6. Under **Add tags – optional**, add tags.
7. Choose **Create**.

## Step 3: Create a revision

In the following procedure, you create a revision after you’ve created a data set in the
AWS Data Exchange console. For more information, see [Revisions](data-sets.md#revisions "data-sets.md#revisions").

###### To create a revision

1. On the **Data set overview** section of the data set details
   page:
   1. (Optional) Choose **Edit name** to edit information about your
      data set.
   2. (Optional) Choose **Delete** to delete the data set.

2. On the **Revisions** section, choose **Create
   revision**.
3. Under **Define revision**, provide an optional comment for your
   revision that describes the purpose of the revision.
4. Under **Add tags – optional**, add tags associated with the
   resource.
5. Choose **Create**.
6. Review, edit, or delete your changes from the previous step.

## Step 4: Add Amazon Redshift datashare assets to a

revision

In the following procedure, you add Amazon Redshift datashare assets to a revision, and then
finalize the revision in the AWS Data Exchange console. For more information, see [Assets](data-sets.md#assets "data-sets.md#assets").

###### To add assets to the revision

1. Under the **AWS Data Exchange datashares for Amazon Redshift** section of the data set
   details page, choose **Add datashares**.
2. Under **AWS Data Exchange datashares for Amazon Redshift**, select the datashares and then
   choose **Add datashare(s)**.

###### Note

You can add up to 20 datashares to a revision.

A job is started to import your assets into your revision. 3. After the job is finished, the **State** field in the
**Jobs** section is updated to **Completed.** 4. If you have more data to add, repeat Step 1. 5. Under **Revision overview**, review your revision and its assets. 6. Choose **Finalize**.

You have successfully finalized a revision for a data set.

You can [edit](publish-data-product.md#edit-revision "publish-data-product.md#edit-revision") or [delete a revision](publish-data-product.md#delete-revision "publish-data-product.md#delete-revision") before you add it to a data grant.

## Step 5: Create a new data grant

After you've created at least one data set and finalized a revision with assets, you're
ready to use that data set as a part of a data grant.

###### To create a new data grant

1. From the left navigation pane of the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange"), under **Exchanged data grants**, choose
   **Sent data grants**.
2. From **Sent data grants**, choose **Create data
   grant** to open the **Define data grant** wizard.
3. In the **Select owned data set** section, select the check box next
   to the data set you want to add.

###### Note

The data sets you choose must have a finalized revision. Data sets without
finalized revisions won't be added to data grants.

Unlike with data sets included in data products which are shared on AWS Marketplace, data
sets added to data grants have no revision access rules, meaning a recipient of a data
grant, once the data grant is approved, will have access to all finalized revisions of
a given data set (including historical revisions finalized prior to the data grant
creation). 4. In the **Grant overview** section, enter information the recipient
will see regarding your data grant, including the **Data grant name**,
and **Data grant description**. 5. Choose **Next**.

For more information, see [Product best practices in AWS Data Exchange](product-details.md "product-details.md"). 6. In the **Recipient access information** section, under
**AWS account ID**, enter the AWS account ID of the data grant
receiver account. 7. In the **Recipient access information** section, under
**Access end date**, choose whether the data grant should run in
perpetuity, selecting **No end date**, or if it should have an end
date, selecting **Specific end date**, and choosing the desired end
date. 8. Choose **Next**. 9. In the **Review and send** section, review your data grant
information. 10. If you're sure that you want to create the data grant and send it to the chosen
recipient, choose **Create and send data grant**.

You've now completed the manual portion of creating a data grant. The data grant will
show on the **Sent data grants** tab on the **Sent data
grants** page showing its status as **Pending
acceptance** until the recipient account accepts it.
