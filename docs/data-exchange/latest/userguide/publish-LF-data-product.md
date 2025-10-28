# Publishing a product in AWS Data Exchange containing

AWS Lake Formation data permission data sets (Preview)

If you're interested in publishing products containing AWS Lake Formation data permission data
sets during this Preview, contact [AWS Support](https://console.aws.amazon.com/support/home#/case/create%3FissueType=customer-service "https://console.aws.amazon.com/support/home#/case/create%3FissueType=customer-service").

An AWS Lake Formation data permission data set contains a set of LF-tags and permissions for
data managed by AWS Lake Formation. When customers subscribe to a product containing Lake Formation data
permissions, they are granted read-only access to the databases, tables, and columns
associated with the LF-tags added to the data set.

As a data provider, you start by creating LF-tags in AWS Lake Formation and associating those
tags with the data you want to make available to subscribers. For more information about
tagging your resources in Lake Formation, see [Lake Formation Tag-based access
control](../../../lake-formation/latest/dg/tag-based-access-control.md "../../../lake-formation/latest/dg/tag-based-access-control.md") in the _AWS Lake Formation Developer Guide_.
Then you import those LF-tags and a set of data permissions into AWS Data Exchange as an asset.
Subscribers are granted access to the data associated with those LF-tags upon
subscription.

The following topics describe the process of publishing a product containing AWS Lake Formation
data permissions. The process has the following steps:

###### Steps

- [Step 1: Create an AWS Lake Formation data set
  (Preview)](#create-LF-data-set "#create-LF-data-set")
- [Step 2: Create an AWS Lake Formation data
  permission (Preview)](#create-LF-data-permission "#create-LF-data-permission")
- [Step 3: Review and finalize](#review-and-finalize-LF "#review-and-finalize-LF")
- [Step 5: (Optional) Create a revision](#create-revision-LF "#create-revision-LF")
- [Step 6: Publish a new product containing
  AWS Lake Formation data sets (Preview)](#publish-LF-product "#publish-LF-product")
- [Considerations when publishing an
  AWS Lake Formation data permission data set (Preview)](#considerations-LF-data-product "#considerations-LF-data-product")

## Step 1: Create an AWS Lake Formation data set

(Preview)

###### To create an AWS Lake Formation data set

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. From the left navigation pane, under **Publish data**,
   choose **Products**.
3. In **Owned data sets**, choose **Create data
   set** to open the **Data set creation steps**
   wizard.
4. In **Select data set type**, choose **AWS Lake Formation
   data permission**.
5. In **Define data set**, enter a **Name**
   and **Description** for your data set. For more
   information, see [Data set best practices](data-sets.md#data-set-best-practices "data-sets.md#data-set-best-practices").
6. Under **Add tags – optional**, choose **Add new
   tag**.
7. Choose **Create data set** and continue.

## Step 2: Create an AWS Lake Formation data

permission (Preview)

AWS Data Exchange uses LF-Tags to grant data permissions. Choose the LF-Tags that are
associated with the data you want to share to grant subscriber permissions to the
data.

###### To create AWS Lake Formation data permission

1. On the **Create Lake Formation data permission** page,
   choose **Add LF-Tag**.
2. Enter the **Key** and choose your LF-Tag
   **Values**.
3. Choose **Preview resource(s)** to view how your LF-Tags
   are interpreted.
   1. From **Preview resource(s)**, select your
      **Associated data catalog resource(s)**.

   ###### Note

   Make sure to revoke `IAMAllowedPrincipals` group on
   the following resources. For more information, see [Revoking IAM role temporary security credentials](../../../IAM/latest/UserGuide/id_roles_use_revoke-sessions.md "../../../IAM/latest/UserGuide/id_roles_use_revoke-sessions.md")
   in the _IAM User Guide_.

4. Review the interpretation of the LF-Tag expression in the dialog box below
   and **Permissions** associated with the data set.
5. For **Service access**, select your existing service role
   that allows AWS Data Exchange to assume the role and access, grant, and revoke
   entitlements to Lake Formation data permissions on your behalf. Then choose
   **Create Lake Formation data permission**. For more information
   about creating a role for an AWS service, see [Creating a
   role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").
6. In the **Define product** section, under
   **Product overview**, enter information about your
   product, including the **Product name**, **Product
   logo**, **Support contact** information, and
   **Product categories**.

For more information, see [Product best practices in AWS Data Exchange](product-details.md "product-details.md"). 7. (Optional) In the **Define product** section, under
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
    3. Choose **Data dictionary preview** to preview the
     data dictionary.
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

8. Under **Product definition**, enter a **Short
   description** and a **Long description** of
   your product.

If you want to use a template for your long description, select
**Apply template**, choose your template type, and then
provide your specific product details in the template. 9. Choose **Next**. 10. Configure your offer.

    * If you're creating a public offer, in the **Add public
     offer** section, configure your offer. All AWS Data Exchange
     products with visibility set to **Public** require a public offer.




    	1. Choose your **Pricing and access
    	 duration** options for the subscription.
    	2. Choose your US sales tax settings, data subscription
    	 agreement (DSA), and refund policy.
    	3. (Optional) Set **Subscription
    	 verification** to control who can subscribe to
    	 this product. For more information, see [Subscription verification for providers in
    	 AWS Data Exchange](subscription-verification-pro.md "subscription-verification-pro.md").
    	4. Choose your **Oﬀer auto-renewal** option.
    	 For more information, see [Creating an offer for AWS Data Exchange products](prepare-offers.md "prepare-offers.md").
    	5. Choose **Next**.


    * If you're creating a private offer, configure the offer details in
     the **Add custom offer** section.




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

11. In the **Review & publish** section, review your
    product information and then expand the **Product page
    preview** to see how it will look after it’s published.
12. If you're sure that you want to make the product and public offer visible
    and available to everyone, choose **Publish**.

You've now completed the manual portion of publishing a data product with a public
offer. AWS Data Exchange prepares and publishes your product. On the **Product
overview** page, the status of your product is **Awaiting
approval**. The status changes to **Published** after
the product is published.

## Step 3: Review and finalize

After creating your AWS Lake Formation data permission (Preview), you can
**Review** and **finalize** your data set.

###### To review and finalize

1. Review your **Data set details** and
   **Tags** in **Step 1** for
   accuracy.
2. Review your **LF-Tag expression(s)**, **Add
   another Lake Formation data permission** (optional),
   **Associated data catalog resource(s)**, and job
   details.

###### Note

Job are deleted 90 days after they’re created. 3. Choose **Finalize**.

## Step 5: (Optional) Create a revision

###### To create a revision

1. From the **Owned data sets** section, choose the data set
   for which you want to add a revision.
2. Choose the **Revisions** tab.
3. In the **Revisions** section, choose **Create
   revision**.
4. On the **Revise Lake Formation data permission** page, choose
   **Add LF-Tag**.
5. Review the **Permissions** for
   **Database** and **Table**.
6. From **Service access**, select an existing service role
   and then choose **Create Lake Formation data permission**.

## Step 6: Publish a new product containing

AWS Lake Formation data sets (Preview)

After you've created at least one data set and finalized a revision with assets,
you're ready to publish a product with AWS Lake Formation data sets. For more information, see
[Product best practices in AWS Data Exchange](product-details.md "product-details.md"). Make sure that you have all required details
about your product.

###### To publish a new product containing AWS Lake Formation data sets (Preview)

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. From the left navigation pane, under **Publish data**,
   choose **Products**.
3. From **Products**, choose **Publish new product** to open the **Publish new product**
   wizard.
4. In the **Product visibility** section, choose your
   product's **Product visibility options** and
   **Sensitive information** configuration, and then choose
   **Next**. For more information, see [Product visibility in AWS Data Exchange](product-visibility.md "product-visibility.md") and [Sensitive categories of information in AWS Data Exchange](sensitive-information.md "sensitive-information.md").
5. In the **Add data** section, under **Owned data
   sets**, select the check boxes next to the data sets that you
   want to add, and then choose **Add selected**.

###### Note

The data sets you choose must have a finalized revision. Data sets
without finalized revisions aren't added.

    1. Go to **Selected data sets** to review your
     selections.


    You can review the **Name** of the data set, the
     **Type** of data set, and the timestamp of when
     the data set was **Last updated**.
    2. Go to **Select revision access rules**, choose
     the revision access rules that you want to set for data sets
     included in this product, and then choose **Next**.


    For more details, see [Revision access rules in AWS Data Exchange](best-practices-revisions.md "best-practices-revisions.md").

## Considerations when publishing an

AWS Lake Formation data permission data set (Preview)

To ensure an optimal subscriber experience, we strongly advise against making any
of the following modifications to any permissions where your product contains AWS Data Exchange
for Lake Formation data sets (Preview) with active subscribers to that product.

- We recommend not deleting or modifying IAM roles passed to AWS Data Exchange in
  published products containing AWS Lake Formation data sets. If you delete or modify
  such IAM roles, the following issues occur:

      + AWS accounts that have access to the Lake Formation data permissions might
       retain access indefinitely.
      + AWS accounts that subscribe to your product but have not yet
       received access to the Lake Formation data permissions will fail to receive
       access.

  AWS Data Exchange will not be liable for any IAM roles that you delete or modify.

- We recommend that you don’t revoke granted AWS Lake Formation data permissions from
  IAM roles passed to AWS Data Exchange in published product containing AWS Lake Formation data
  sets. If you revoke granted data permissions from such IAM roles, the
  following issues occur:
  - AWS accounts that have access to the Lake Formation data permissions might
    retain access indefinitely.
  - AWS accounts that subscribe to your product but have not yet
    received access to the Lake Formation data permissions will fail to receive
    access.

- We recommend not revoking granted AWS Lake Formation data permissions from
  AWS accounts with active subscriptions to published products containing
  AWS Lake Formation data sets. If you revoke granted data permissions from
  AWS accounts subscribed to your product, those accounts will lose access,
  creating a poor customer experience.
- We recommend setting the cross account version in your AWS Glue Data Catalog to
  version 3 when publishing products containing AWS Lake Formation data sets. If you
  downgrade the cross account version of your Data Lake Catalog while having
  published products containing AWS Lake Formation data sets, the AWS accounts that
  subscribe to your product but have not yet received access to the Lake Formation data
  permissions may fail to get access to the data.
