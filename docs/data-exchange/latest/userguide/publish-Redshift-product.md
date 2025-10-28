# Publishing a product in AWS Data Exchange containing Amazon Redshift

data sets

An Amazon Redshift data set contains AWS Data Exchange datashares for Amazon Redshift. When customers subscribe to a
product containing datashares, they are granted read-only access to the tables, views,
schemas, and user-defined functions that a data provider adds to the datashare.

As a data provider, you create an AWS Data Exchange for Amazon Redshift datashare in your cluster. Then, you
add to the datashare the schemas, tables, views, and user-defined functions that you
want the subscribers to access. You then import the datashare to AWS Data Exchange, create a data
set, add it to a product, and publish the product. Subscribers are granted access to the
datashare upon subscription.

After you have set up your Amazon Redshift datashare in Amazon Redshift, you can create a new Amazon Redshift data set
in AWS Data Exchange. You can then create a revision, and add Amazon Redshift datashare assets. This allows
requests to the AWS Data Exchange endpoint to proxy through to your Amazon Redshift datashare. You can then add
this data set to a product and add pricing. Then, prospective subscribers can view your
product and subscribe to it in the AWS Data Exchange catalog.

The following topics describe the process of creating an Amazon Redshift data set and publishing
a new product with Amazon Redshift data sets using the AWS Data Exchange console. The process has the following
steps:

###### Steps

- [Step 1: Create an Amazon Redshift datashare asset](#create-RS-asset "#create-RS-asset")
- [Step 2: Create an Amazon Redshift data set](#create-RS-data-set "#create-RS-data-set")
- [Step 3: Create a revision](#create-RS-revision "#create-RS-revision")
- [Step 4: Add Amazon Redshift datashare assets to a
  revision](#add-RS-assets "#add-RS-assets")
- [Step 5: Publish a new product containing Amazon Redshift
  data sets](#publish-RS-product "#publish-RS-product")
- [Step 6: (Optional) Copy a product](#copy-RS-product "#copy-RS-product")

## Step 1: Create an Amazon Redshift datashare asset

Assets are the data in AWS Data Exchange. For more information, see [Assets](data-sets.md#assets "data-sets.md#assets").

###### To create an Amazon Redshift datashare asset

1. Create a datashare within your Amazon Redshift cluster.

For more information about how to create a datashare, see _Working with AWS Data Exchange datashares as a producer_ in
the [Amazon Redshift
Database Developer Guide](../../../redshift/latest/dg/welcome.md "../../../redshift/latest/dg/welcome.md").

###### Note

We recommend setting your datashare as publicly accessible. If you do
not, customers with publicly accessible clusters will not be able to
consume your data. 2. [Step 2: Create an Amazon Redshift data set](#create-RS-data-set "#create-RS-data-set").

## Step 2: Create an Amazon Redshift data set

An Amazon Redshift data set includes AWS Data Exchange datashares for Amazon Redshift. For more information, see
[Amazon Redshift data set](data-sets.md#RS-data-set-type "data-sets.md#RS-data-set-type").

###### To create an Amazon Redshift data set

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. On the left side navigation pane, under **Publish
   data**, choose **Owned data sets**.
3. In **Owned data sets**, choose **Create data
   set** to open the **Data set creation steps**
   wizard.
4. In **Select data set type**, choose **Amazon Redshift
   datashare**.
5. In **Define data set**, enter a **Name**
   and **Description** for your data set. For more
   information, see [Data set best practices](data-sets.md#data-set-best-practices "data-sets.md#data-set-best-practices").
6. Under **Add tags – optional**, add tags.
7. Choose **Create**.

## Step 3: Create a revision

In the following procedure, you create a revision after you’ve created a data set
in the AWS Data Exchange console. For more information, see [Revisions](data-sets.md#revisions "data-sets.md#revisions").

###### To create a revision

1. On the **Data set overview** section of the data set
   details page:
   1. (Optional) Choose **Edit name** to edit
      information about your data set.
   2. (Optional) Choose **Delete** to delete the data
      set.

2. On the **Revisions** section, choose **Create
   revision**.
3. Under **Define revision**, provide an optional comment
   for your revision that describes the purpose of the revision.
4. Under **Add tags – optional**, add tags associated with
   the resource.
5. Choose **Create**.
6. Review, edit, or delete your changes from the previous step.

## Step 4: Add Amazon Redshift datashare assets to a

revision

In the following procedure, you add Amazon Redshift datashare assets to a revision, and then
finalize the revision in the AWS Data Exchange console. For more information, see [Assets](data-sets.md#assets "data-sets.md#assets").

###### To add assets to the revision

1. Under the **AWS Data Exchange datashares for Amazon Redshift** section of the
   data set details page, choose **Add datashares**.
2. Under **AWS Data Exchange datashares for Amazon Redshift**, select the
   datashares and then choose **Add datashare(s)**.

###### Note

You can add up to 20 datashares to a revision.

A job is started to import your assets into your revision. 3. After the job is finished, the **State** field in the
**Jobs** section is updated to
**Completed.** 4. If you have more data to add, repeat Step 1. 5. Under **Revision overview**, review your revision and its
assets. 6. Choose **Finalize**.

You have successfully finalized a revision for a data set.

You can [edit](publish-data-product.md#edit-revision "publish-data-product.md#edit-revision") or [delete a revision](publish-data-product.md#delete-revision "publish-data-product.md#delete-revision") before you add it to a
product.

## Step 5: Publish a new product containing Amazon Redshift

data sets

After you've created at least one data set and finalized a revision with assets,
you're ready to publish a product with Amazon Redshift data sets. For more information, see
[Product best practices in AWS Data Exchange](product-details.md "product-details.md"). Make sure
that you have all required details about your product and offer.

###### To publish a new product containing Amazon Redshift data sets

1. From the left navigation pane of the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange"), under **Publish
   data**, choose **Products**.
2. From **Products**, choose **Publish new
   product** to open the **Publish new product**
   wizard.
3. In the **Product visibility** section, choose your
   product's **Product visibility options** and
   **Sensitive information** configuration, and then
   choose **Next**. For more information, see [Product visibility in AWS Data Exchange](product-visibility.md "product-visibility.md") and
   [Sensitive categories of information in AWS Data Exchange](sensitive-information.md "sensitive-information.md").
4. In the **Add data** section, under **Owned data
   sets**, select the check boxes next to the data sets that you
   want to add, and then choose **Add selected**.

###### Note

The data sets you choose must have a finalized revision. Data sets
without finalized revisions won't be added.

    1. Go to **Selected data sets** to review your
     selections.


    You can review the **Name** of the data set, the
     **Type** of data set, and the timestamp of when
     the data set was **Last updated**.
    2. Go to **Select revision access rules**, choose
     the revision access rules that you want to set for data sets
     included in this product, and then choose **Next**.


    For more details, see [Revision access rules in AWS Data Exchange](best-practices-revisions.md "best-practices-revisions.md").

5. In the **Define product** section, under
   **Product overview**, enter information about your
   product, including the **Product name**, **Product
   logo**, **Support contact** information, and
   **Product categories**.

For more information, see [Product best practices in AWS Data Exchange](product-details.md "product-details.md"). 6. (Optional) In the **Define product** section, under
**Data dictionaries and samples – optional**, choose a
data set by selecting the option button next to the data set name and then
choose **Edit**.

For more information, see [Data dictionaries in AWS Data Exchange](data-dictionaries-pro.md "data-dictionaries-pro.md") and [Sample data in AWS Data Exchange](samples-pro.md "samples-pro.md").

    1. In the **Edit** dialog box, under
     **Upload data dictionary**, choose
     **Add file** to upload a new data dictionary.


    You can choose one data dictionary, in .csv format, with a maximum
     size of 1 MB.
    2. Choose a saved data dictionary from your computer and then choose
     **Open**.


    The data dictionary .csv file appears on the
     **Edit** dialog box.


    ###### Note

    Your data dictionary must conform to the AWS Data Exchange data dictionary
     template. If you don’t have a saved data dictionary to upload,
     you can choose either the **blank data dictionary
     template** link or the **example data
     dictionary** link in the AWS Data Exchange console.
    3. Choose **Data dictionary preview** to preview
     it.
    4. Under **Samples - optional**, choose
     **Upload samples**, choose a sample from your
     computer, and then choose **Open**.


     The samples appear on the **Edit** dialog
     box.


    ###### Note

    You can upload up to 10 samples with a maximum size of 50 MB.
     Samples in .csv format can be previewed.
    5. Enter a description for each sample that will be visible on the
     product detail page.
    6. Choose **Save**.

7. Under **Product definition**, enter a **Short
   description** and a **Long description** of
   your product.

If you want to use a template for your long description, select
**Apply template**, choose your template type, and then
fill out the template with your specific product details. 8. Choose **Next**. 9. Configure your offer.

    * If you are creating a public offer, in the **Add public
     offer** section, configure your offer. All AWS Data Exchange
     products with visibility set to **Public** require a public offer.




    	1. Choose your **Pricing and access
    	 duration** options for the subscription.
    	2. Choose your US sales tax settings, data subscription
    	 agreement (DSA), and refund policy.
    	3. (Optional) Set **Subscription
    	 verification**, which enables you to control
    	 who can subscribe to this product. For more information, see
    	 [Subscription verification for providers in
    	 AWS Data Exchange](subscription-verification-pro.md "subscription-verification-pro.md").
    	4. Choose your **Oﬀer auto-renewal** option.
    	 For more information, see [Creating an offer for AWS Data Exchange products](prepare-offers.md "prepare-offers.md").
    	5. Choose **Next**.


    * If you are creating a private offer, configure the offer details
     in the **Add custom offer** section.




    	1. In the **Subscriber account information**
    	 section, add at least one subscriber account to which you
    	 want to extend the offer.
    	2. Choose your **Pricing and access
    	 duration** options for the subscription.
    	3. Choose the **Offer expiration date** by
    	 which the subscriber must accept the offer.
    	4. Choose your US sales tax settings, data subscription
    	 agreement (DSA), and refund policy.
    	5. Choose your **Oﬀer auto-renewal** option.
    	 For more information, see [Creating an offer for AWS Data Exchange products](prepare-offers.md "prepare-offers.md").
    	6. Choose **Next**.

10. In the **Review & publish** section, review your
    product information and then expand the **Product page
    preview** to see how it will look after it’s published.
11. If you're sure that you want to make the product and public offer visible
    and available to everyone, choose **Publish**.

You've now completed the manual portion of publishing a data product with a public
offer. AWS Data Exchange prepares and publishes your product. On the **Product
overview** page, the status of your product is **Awaiting
approval** and then changes to **Published** after
it's published.

## Step 6: (Optional) Copy a product

After you have created your first product, you can copy its details and public
offers to create a new product.

###### Note

You can copy a public, private, published, or unpublished product. Custom
oﬀers associated with the product will not be copied, but public oﬀers will be
copied.

###### To copy a product

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. From the left navigation pane, under **Publish data**,
   choose **Products**.
3. From **Products**, choose the button next to the product
   you want to copy.
4. Select the **Actions** dropdown, and then choose
   **Create copy**.
5. Continue through the **Publish a product** workflow, with
   details already filled in, based on the product you chose in Step 3. For
   more information, see [Step 5: Publish a new product](publish-data-product.md#publish-products "publish-data-product.md#publish-products").
