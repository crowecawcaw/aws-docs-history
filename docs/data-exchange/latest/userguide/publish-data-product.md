

# Publishing a product in AWS Data Exchange containing file-based data
<a name="publish-data-product"></a>

The following topics describe the process of creating a data set and publishing a new product in AWS Data Exchange containing file-based data on AWS Data Exchange by using the AWS Data Exchange console. The process has the following steps:

**Topics**
+ [Step 1: Create assets](#create-assets)
+ [Step 2: Create a data set](#create-dataset)
+ [Step 3: Create a revision](#create-revision)
+ [Step 4: Import assets to a revision](#import-assets)
+ [Step 5: Publish a new product](#publish-products)
+ [Step 6: (Optional) Copy a product](#copy-product)

## Step 1: Create assets
<a name="create-assets"></a>

Assets are the *data* in AWS Data Exchange. For more information, see [Assets](data-sets.md#assets).

Before you create and publish a new file-based data product, you must:

1. Create your files. 

   AWS Data Exchange supports all file types.

1. Store your files as objects in Amazon Simple Storage Service (Amazon S3) or on your local computer. 

   For more information about storing files in Amazon S3, see the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

## Step 2: Create a data set
<a name="create-dataset"></a>

Data sets in AWS Data Exchange are dynamic and are versioned using revisions, with each revision containing at least one asset. For more information, see [Data in AWS Data Exchange](data-sets.md).

**To create a data set**

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1.  In the left side navigation pane, under **Publish data**, choose **Owned data sets**.

1. In **Owned data sets**, choose **Create data set** to open the **Data set creation steps** wizard.

1. In **Select data set type**, choose ****Files****.

1. In **Define data set**, enter a **Name** and **Description** for your data set. For more information, see [Data set best practices](data-sets.md#data-set-best-practices). 

1. (Optional) Under **Add tags – optional**, add tags.

1. Choose **Create data set**. 

## Step 3: Create a revision
<a name="create-revision"></a>

In the following procedure, you create a revision after you’ve created a data set in the AWS Data Exchange console. For more information, see [Revisions](data-sets.md#revisions).

**To create a revision**

1. On the **Data set overview** section of the data set details page:

   1. (Optional) Choose **Edit name** to edit information about your data set.

   1. (Optional) Choose **Delete** to delete the data set.

1. In the **Revisions** section, choose **Create revision**.

1. Under **Define revision**, provide an optional comment for your revision that describes the purpose of the revision. 

1. (Optional) Under **Add tags – optional**, add tags associated with the resource.

1. Choose **Create revision**.

1. Review, edit, or delete your changes from the previous step. 

## Step 4: Import assets to a revision
<a name="import-assets"></a>

 In the following procedure, you import data assets, and then finalize the revision in the AWS Data Exchange console. For more information, see [Assets](data-sets.md#assets). 

**To import assets to the revision**

1. Under the **Jobs** section of the data set details page, choose either **Import from Amazon S3** or **Upload** (to upload from your computer), depending on where the data assets for the data set are currently stored.

1. Follow the prompts, depending on your selection. A job is started to import your asset into your data set. 

1. After the job is finished, the **State** field in the **Jobs** section is updated to **Completed.**

1. If you have more data to add, repeat Step 1.

1. In **Revision overview**, review your revision and its assets. 

1. Choose **Finalize revision**.

You have successfully finalized a revision for a data set. 

You can edit or delete a revision before you add it to a product. 

**Topics**
+ [Edit a revision](#edit-revision)
+ [Delete a revision](#delete-revision)

### Edit a revision
<a name="edit-revision"></a>

**To edit the revision after you’ve finalized it**

1. In **Revision overview**, choose **De-finalize**.

   You see a message that the revision is no longer in the finalized state.

1. To edit the revision, from **Revision overview**, choose **Actions**, **Edit**.

1. Make your changes, and then choose **Update**.

1. Review your changes, and then choose **Finalize**.

### Delete a revision
<a name="delete-revision"></a>

**To delete the revision after you’ve finalized it**

1. In **Revision overview**, choose **Delete**.

1. Type **Delete** in the **Delete revision** dialog box, and then choose **Delete**.

**Warning**  
This deletes the revision and all of its assets. This action cannot be undone.

## Step 5: Publish a new product
<a name="publish-products"></a>

After you've created at least one data set and finalized a revision with assets, you're ready to publish that data set as a part of a product. For more information, see [Product best practices in AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/product-details.html). Make sure that you have all required details about your product and offer.

**To create a new product listing**

1. Sign in to your seller AWS account and go to the [AWS Marketplace Management Portal](https://console.aws.amazon.com/marketplace).

1. In the top menu, go to **Products** and then choose **Data Products**.

1. Choose **Create data product**.

1. To get started with a data product, you'll initiate the listing process by setting the product name, adding optional resource tags for organization, and generating the product ID. The product ID is used to track your product throughout its lifecycle.

1. Under **Product name**, enter a unique product name that will be displayed to buyers at the top of the product listing page and in search results.

1. (Optional) Under **Tags**, enter any tags you want to associate with the product. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

1. Under **Product ID and code**, choose **Generate product ID and code**.

1. Choose **Continue to product details**. You'll start the process of adding detailed product information.

**To provide product information**

When listing your data product in AWS Marketplace, providing comprehensive and accurate product information is crucial. Use the **Provide product information** step to capture essential details about your offering such as product categories and support information.

1. Enter information about your product. For more details, see [AWS Data Exchange product details](https://docs.aws.amazon.com/data-exchange/latest/userguide/prod-details-over.html).

1. Choose **Next** to move to the next step.

**To add data sets**

1. Choose the AWS Region in which the data sets are located.

1. In the **Owned data sets** section, select the check boxes next to the data sets you want to add. The data sets you choose must have a finalized revision. Data sets without finalized revisions can't be added.

   1. Go to **Added data sets** to review your selections.

   1. You can review the **Name** of the data set, the **Type** of data set, and the timestamp of when the data set was **Last updated**.

   1. Go to **Revision access rule settings**, choose the revision access rules that you want to set for data sets included in this product. For more details, see [Revision access rules in AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/best-practices-revisions.html).

1. (Optional) In the **Data dictionaries** section, select a data set and choose **Add dictionary**.

   1. Choose **Upload data dictionary** to upload a new data dictionary.

      You can choose one data dictionary, in .csv format, with a maximum size of 1 MB.

   1. Choose a saved data dictionary from your computer, and then choose **Open**. Your data dictionary must conform to the AWS Data Exchange data dictionary template. If you don't have a saved data dictionary to upload, you can choose either the **blank data dictionary template** link or the **example data dictionary** link in the AWS Data Exchange console. For more details, see [Data dictionaries in AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/data-dictionaries-pro.html).

1. (Optional) Under **Data samples**, choose **Add sample** and select the data set to which you want to provide samples.

   1. Select **Upload data sample** and select a data set a sample from your computer, and then choose **Open**.

   1. (Optional) Enter a description for each sample that will be visible on the product detail page.

   1. Choose **Add sample**. You can upload up to 10 samples with a maximum size of 50 MB. Samples in .csv format can be previewed. For more details, see [Sample data in AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/samples-pro.html).

1. In the **Revision access rule settings** section, choose the revision access rules that you want to set for data sets included in this product. For more details, see [Revision access rules in AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/best-practices-revisions.html).

1. In the **Data sensitivity information settings** section, choose your product's **Sensitive information** configuration, and then choose **Next**. For more information, see [Sensitive categories of information in AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/sensitive-information.html).

**To configure allowlist**

Before submitting your product, you'll need to specify which AWS accounts can access it. This optional step controls the initial visibility of your product, limiting access to your own account and any specifically authorized AWS accounts you add to the allowlist.

1. Enter the AWS account IDs you want to access your product.

1. Choose **Submit** to submit your product. Your product will have the **Limited visibility** status and will only be visible to the AWS account that created the product and other allow-listed AWS accounts. You can view and test your product listing while it's in **Limited visibility** status.

For more information on statuses, see [Product visibility in AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/product-visibility.html).

## Step 6: (Optional) Copy a product
<a name="copy-product"></a>

After you have created your first product, you can copy its details and public offers to create a new product.

**Note**  
You can copy a public, private, published, or unpublished product. Custom oﬀers associated with the product will not be copied, but public oﬀers will be copied.

**To copy a product**

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. From the left navigation pane, under **Publish data**, choose **Products**.

1. From **Products**, choose the button next to the product you want to copy.

1. Select the **Actions** dropdown, and then choose **Create copy**.

1. Continue through the **Publish a new product** workflow, with details already filled in, based on the product you chose in Step 3. For more information, see [Step 5: Publish a new product](#publish-products).