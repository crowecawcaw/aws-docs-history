# Getting started as a subscriber in AWS Data Exchange

The following topics describe the complete process of becoming a data product subscriber on
AWS Data Exchange using the AWS Data Exchange console. The process has the following steps:

###### Steps

- [Step 1: Set up AWS Data Exchange](#subscriber-prereqs "#subscriber-prereqs")
- [Step 2: Browse the catalog](#browse-catalog "#browse-catalog")
- [Step 3: (Optional) Request a recommendation for a data
  product](#request-new-products "#request-new-products")
- [Step 4: (Optional) Evaluate products containing data
  dictionaries and samples](#evaluate-products "#evaluate-products")
- [Step 5: Subscribe to and access a product](#subscribe-to-product "#subscribe-to-product")

## Step 1: Set up AWS Data Exchange

Before you can use AWS Data Exchange, you must sign up for AWS and create a user. For more
information, see [Setting up AWS Data Exchange](setting-up.md "setting-up.md").

###### To set up AWS Data Exchange

1. Sign up for an AWS account. For more information, see [Sign up for an AWS account](setting-up.md#setting-up-aws-sign-up "setting-up.md#setting-up-aws-sign-up").
2. Create a user. For more information, see [Create a user](setting-up.md#setting-up-create-iam-user "setting-up.md#setting-up-create-iam-user").

## Step 2: Browse the catalog

You can find products and review the associated public or custom oﬀers and product details
on both AWS Marketplace and AWS Data Exchange.

If the provider has issued a private oﬀer to your account, the product is available on the
**My product oﬀers page** of the AWS Data Exchange console. For more information, see
[Subscribing to AWS Data Exchange data products on AWS Data Exchange](subscribe-to-data-sets.md "subscribe-to-data-sets.md").

###### To browse the catalog

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **Discover data products**,
   choose **Browse catalog**.
3. Enter a term or phrase in the **Search** bar and then choose
   **Search**.
4. (Optional) Under **Browse catalog**, enter in a word or phrase and
   then choose **Search** to view results matching your query.
5. (Optional) Under **Refine results**, choose from one of the specific
   **Categories** to browse specific data products.
6. (Optional) Under **Refine results**, use the **Data set
   type** filter and select from the following options to find products:
   - **Files (Amazon S3 Objects)** – Products containing file-based
     data
   - **Amazon Redshift** – Products containing Amazon Redshift datashares
   - **API** – Products containing APIs
   - **Access to Amazon S3** – Products containing Amazon S3 data
     access
   - **AWS Lake Formation**
     – Products containing AWS Lake Formation data permissions
     (Preview)

7. Select a product from the list of returned results, and review its product details
   page.

## Step 3: (Optional) Request a recommendation for a data

product

If you're unable to find a product in the catalog, you can request personalized
recommendations from the [AWS Data Exchange Data Discovery Team](https://aws.amazon.com/data-exchange/discover-data/ "https://aws.amazon.com/data-exchange/discover-data/").

###### To request a data product recommendation

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **Discover data products**,
   choose **Request data product**.
3. On the **Request data product** page, for
   **Details**, enter a **Data description**.
4. (Optional) Expand **Additional details - optional** and complete the
   fields as directed.
   1. Select one or more **Product categories**.
   2. Enter an **Example data product URL**.
   3. For **Data set type**, choose from **Files (Amazon S3
      Objects)**, **Amazon API Gateway API**, **Amazon Redshift
      datashare**, **AWS Lake Formation data permissions (Preview)** or
      **Amazon S3 data access**.
   4. Enter specific details about the product you want including **Delivery
      cadence**, **Example data product URL**,
      **Subscription start date**, **Subscription
      length**, and **Subscription budget**.
   5. If the **Data set type** you chose is **Amazon API Gateway
      API**, under **Subscription budget**, select
      **Including metered costs**.

5. For **Data providers**, choose from a list of **Existing
   providers** or enter the name of **Other providers**. Then
   indicate whether you have an existing relationship with the providers.
6. Choose **Submit**.

You should receive a response from the AWS Data Exchange Data Discovery Team within 2 business
days.

## Step 4: (Optional) Evaluate products containing data

dictionaries and samples

A provider might include a data dictionary and samples of the data set with their product.
To help you determine if the product’s data set will meet your needs, you can view and
download the data dictionary and samples before you subscribe. For more information, see [Data dictionaries and samples](product-subscriptions.md#dictionaries-and-samples "product-subscriptions.md#dictionaries-and-samples").

You can perform the following actions to help with your evaluation of a product’s data
sets:

- [View a data dictionary](#view-data-dictionary "#view-data-dictionary")
- [Download a data dictionary](#download-data-dictionary "#download-data-dictionary")
- [View and download all data
  dictionaries](#view-download-all-dictionaries "#view-download-all-dictionaries") (for products containing multiple data sets)
- [Preview a sample](#preview-sample "#preview-sample")
- [Download a sample](#download-sample "#download-sample")

### Viewing a data dictionary

A provider can add one data dictionary per data set that you can view.

###### To view a data dictionary

1. On the product detail page, choose the **Data dictionary and
   samples** tab.
2. View the data dictionary in one of the following ways:
   - Scroll down to the product **Overview** section to see the data
     dictionary under **View data dictionaries**.
   - Choose the **Data dictionaries and samples** tab, expand a data
     set row, choose the option button next to a data dictionary, and then choose
     **View all data dictionaries**.

3. (Optional) Enter a keyword or phrase into the **Search** bar to
   search across all data sets and all tables.
4. (Optional) Modify your search and filters as necessary.

### Downloading a data dictionary

A provider can add one data dictionary per data set that you can download.

###### To download a data dictionary

1. On the product detail page, choose the **Data dictionary and
   samples** tab.
2. Expand the data set row by choosing the expand icon (plus icon to the left of the
   data set name).
3. Choose the option button next to a data dictionary name.
4. Choose **Download**.

The data dictionary file is downloaded to your computer.

### Viewing and downloading all data

dictionaries

If the product has multiple data sets, the provider might add a data dictionary for each
data set. To evaluate all the data sets, you might want to view and download all data
dictionaries.

###### To view and download all data dictionaries

1. On the product detail page, choose the **Data dictionary and
   samples** tab.
2. Choose **View all data dictionaries**.
3. In the **View data dictionaries** dialog box, choose the
   **Download (CSV)** to download the .csv file.

The .csv file is downloaded to your computer. 4. Choose **Close** to close the dialog box.

### Previewing a sample

###### To preview a sample

1. On the product detail page, choose the **Data dictionary and
   samples** tab.
2. Expand the data set by choosing the expand icon (plus icon to the left of the data
   set name)
3. Choose the option button next to a sample name.
4. Choose **Preview sample (CSV only)** to preview the sample.
   1. (Optional) In the preview dialog box, choose **Download** to
      download the .csv file.

   The .csv file is downloaded to your computer. 2. Choose **Close** to close the dialog box.

### Downloading a sample

###### To download a sample

1. On the product detail page, choose the **Data dictionary and
   samples** tab.
2. Expand the data set by choosing the expand icon (plus icon to the left of the data
   set name)
3. Choose the option button next to a sample name.
4. Choose **Download**.

The sample is downloaded to your computer.

## Step 5: Subscribe to and access a product

After you discover a product in the AWS Data Exchange catalog and determine that it meets your needs,
you can subscribe to the product and then access the product.

If you subscribe to a paid product, you are billed on your AWS bill. You get access to
the entitled data set. For more information, see [Subscribing to AWS Data Exchange data products on AWS Data Exchange](subscribe-to-data-sets.md "subscribe-to-data-sets.md").

For more information about how to subscribe to products containing different types of data
sets, see the following:

- [Subscribing to and accessing an AWS Data Exchange product containing
  file-based data](subscribing-to-data-product.md "subscribing-to-data-product.md")
- [Subscribing to and accessing an AWS Data Exchange product
  containing APIs](subscribing-to-API-product.md "subscribing-to-API-product.md")
- [Subscribing to and accessing an AWS Data Exchange
  product containing Amazon Redshift data sets](subscribing-to-Redshift-product.md "subscribing-to-Redshift-product.md")
- [Subscribing to and accessing an AWS Data Exchange product
  containing Amazon S3 data access](subscribing-to-S3-data-access.md "subscribing-to-S3-data-access.md")
- [Subscribing to and accessing an AWS Data Exchange
  product containing AWS Lake Formation data sets (Preview)](subscribing-to-LakeFormation-product.md "subscribing-to-LakeFormation-product.md")
