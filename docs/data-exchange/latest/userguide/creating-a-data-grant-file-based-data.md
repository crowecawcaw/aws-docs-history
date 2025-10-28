# Creating a data grant on AWS Data Exchange containing

file-based data

The following topics describe the process of creating a data set and a new data grant
containing file-based data on AWS Data Exchange by using the AWS Data Exchange console. The process has the following
steps:

###### Steps

- [Step 1: Create assets](#data-grant-create-assets "#data-grant-create-assets")
- [Step 2: Create a data set](#data-grant-create-dataset "#data-grant-create-dataset")
- [Step 3: Create a revision](#data-grant-create-revision "#data-grant-create-revision")
- [Step 4: Import assets to a revision](#data-grant-import-assets "#data-grant-import-assets")
- [Step 5: Create a new data grant](#data-grant-creation-steps "#data-grant-creation-steps")

## Step 1: Create assets

Assets are the _data_ in AWS Data Exchange. For more information,
see [Assets](data-sets.md#assets "data-sets.md#assets").

Before you create a new file-based data grant, you must:

1. Create your files.

AWS Data Exchange supports all file types. 2. Store your files as objects in Amazon Simple Storage Service (Amazon S3) or on your local computer.

For more information about storing files in Amazon S3, see the [Amazon S3 User
Guide](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md").

## Step 2: Create a data set

Data sets in AWS Data Exchange are dynamic and are versioned using revisions, with each revision
containing at least one asset. For more information, see [Data in AWS Data Exchange](data-sets.md "data-sets.md").

###### To create a data set

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **My data**, choose
   **Owned data sets**.
3. In **Owned data sets**, choose **Create data set**
   to open the **Data set creation steps** wizard.
4. In **Select data set type**, choose \***\*Files\*\***.
5. In **Define data set**, enter a **Name** and
   **Description** for your data set. For more information, see [Data set best practices](data-sets.md#data-set-best-practices "data-sets.md#data-set-best-practices").
6. (Optional) Under **Add tags – optional**, add tags.
7. Choose **Create data set**.

## Step 3: Create a revision

In the following procedure, you create a revision after you’ve created a data set in the
AWS Data Exchange console. For more information, see [Revisions](data-sets.md#revisions "data-sets.md#revisions").

###### To create a revision

1. On the **Data set overview** section of the data set details
   page:
   1. (Optional) Choose **Edit name** to edit information about your
      data set.
   2. (Optional) Choose **Delete** to delete the data set.

2. In the **Revisions** section, choose **Create
   revision**.
3. Under **Define revision**, provide an optional comment for your
   revision that describes the purpose of the revision.
4. (Optional) Under **Add tags – optional**, add tags
   associated with the resource.
5. Choose **Create revision**.
6. Review, edit, or delete your changes from the previous step.

## Step 4: Import assets to a revision

In the following procedure, you import data assets, and then finalize the revision in
the AWS Data Exchange console. For more information, see [Assets](data-sets.md#assets "data-sets.md#assets").

###### To import assets to the revision

1. Under the **Jobs** section of the data set details page, choose
   either **Import from Amazon S3** or **Upload** (to upload
   from your computer), depending on where the data assets for the data set are currently
   stored.
2. Follow the prompts, depending on your selection. A job is started to import your
   asset into your data set.
3. After the job is finished, the **State** field in the
   **Jobs** section is updated to **Completed.**
4. If you have more data to add, repeat Step 1.
5. In **Revision overview**, review your revision and its
   assets.
6. Choose **Finalize revision**.

You have successfully finalized a revision for a data set.

You can edit or delete a revision before you add it to a product.

###### Topics

- [Edit a revision](#data-grant-edit-revision "#data-grant-edit-revision")
- [Delete a revision](#data-grant-delete-revision "#data-grant-delete-revision")

### Edit a revision

###### To edit the revision after you’ve finalized it

1. In **Revision overview**, choose
   **De-finalize**.

You see a message that the revision is no longer in the finalized state. 2. To edit the revision, from **Revision overview**, choose
**Actions**, **Edit**. 3. Make your changes, and then choose **Update**. 4. Review your changes, and then choose **Finalize**.

### Delete a revision

###### To delete the revision after you’ve finalized it

1. In **Revision overview**, choose
   **Delete**.
2. Type `Delete` in the **Delete revision**
   dialog box, and then choose **Delete**.

###### Warning

This deletes the revision and all of its assets. This action cannot be
undone.

## Step 5: Create a new data grant

After you've created at least one data set and finalized a revision with assets, you're
ready to use that data set as a part of a data grant.

###### To create a new data grant

1. In the left navigation pane of the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange"), under **Exchanged data grants**, choose
   **Sent data grants**.
2. From **Sent data grants**, choose **Create data
   grant** to open the **Define data grant** wizard.
3. In the **Select owned data set** section, select the check box next
   to the data set you want to add.

###### Note

The data set you choose must have a finalized revision. Data sets without finalized
revisions can't be added to data grants.

Unlike with data sets included in data products which are shared on AWS Marketplace, data
sets added to data grants have no revision access rules, meaning a recipient of a data
grant, once the data grant is approved, will have access to all finalized revisions of
a given data set (including historical revisions finalized prior to the data grant
creation). 4. In the **Grant overview** section, enter information the recipient
will see about your data grant, including the **Data grant name** and
**Data grant description**. 5. Choose **Next**.

For more information, see [Product best practices in AWS Data Exchange](product-details.md "product-details.md"). 6. In the **Recipient access information** section, under
**AWS account ID**, enter the AWS account ID of the recipient
account who should receive the data grant. . 7. Under **Access end date**, select a specific end date for when the
data grant should expire or, if the grant should exist in perpetuity, select
**No end date**. 8. Choose **Next**. 9. In the **Review and send** section, review your data grant
information. 10. If you're sure that you want to create the data grant and send it to the chosen
recipient, choose **Create and send data grant**.

You've now completed the manual portion of creating a data grant. The data grant will show on the **Sent data
grants** tab on the **Sent data grants** page showing its status
as **Pending acceptance** until the recipient account accepts it.
