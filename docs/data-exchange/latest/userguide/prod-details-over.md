# AWS Data Exchange product details

The following topics provide best practices for the details of a product in AWS Data Exchange.

## Product name

Subscribers will search for the names of products in AWS Data Exchange, so make your product name
something meaningful.

## Product logo

The product logo appears in the AWS Data Exchange product catalog on the console and on AWS Marketplace. The
supported formats for the logo are .png, .jpg, and .jpeg.

## Support contact

As a provider, you must include valid contact information in AWS Data Exchange. This can be a managed
email alias or case management system link for customers to use to get help when they have
questions about your product. We strongly recommend that you don't use a personal email
address because the address is publicly visible.

## Product categories

All products fit into one or more categories in AWS Data Exchange. By specifying up to two categories
for your product, you help subscribers filter and find your products in AWS Data Exchange and
AWS Marketplace.

## Short description for products

The product short description text appears on the tiles in the product catalog portion of
the AWS Data Exchange console. We recommend that you provide a concise description of your product for
this field.

## Long description for products

Subscribers see the product long description in the product detail page after the product
is published in AWS Data Exchange. We recommend that you list the product's features, benefits, usage, and
other information specific to the product.

Product information in the description must accurately represent the data being provided
to subscribers. This includes data coverage (for example, 30,000 financial instruments or
10,000 location coordinates) and data set update frequency (for example, daily updates or
weekly updates).

###### Note

You can use Markdown templates as a starting point for the long description of a number
of popular product types. For more information, see [Product description templates in
AWS Data Exchange](product-description-templates.md "product-description-templates.md").

### Product description additional information

In order to make your product description compelling to prospective subscribers, we
recommend you add the following information to your product description:

- _Data due diligence questionnaire (DDQ)_ – Typically includes
  responses to questions regarding the firm selling a data set. Examples of the
  information in a DDQ includes the process that a provider goes through to collect the
  data, or quality control procedures and questions regarding regulatory
  compliance.
- _Data set schemas_ – Provide prospective users with detailed
  descriptions of the structure and format of your data sets. Examples of the information
  in a data set schema include the identification of a primary key, field names, field
  definitions, expected output types for each field (for example, string, integer), and
  acceptable enumerations for each field (for example, 0%–100%).
- _Trial product listings_ – Many prospective subscribers
  request trials of data sets before paying for a subscription. Trial products can be
  published on AWS Data Exchange for subscribers to subscribe to like regular paid products.
- _Sample files_ – Sample files are typically smaller versions,
  or older, out-of-date versions of full production data sets. These sample files give
  prospective users insights into the outputs they can expect before purchasing a
  subscription.
- _Product fact sheets_ – These can be documents, web links, or
  both to provide subscribers with more granular statistics on the coverage of your data
  sets, typical use cases for your data sets, and any other factors that differentiate
  your data sets.

For information about adding links in the description, see [Include links in your product
description](#best-practices-links-in-listing "#best-practices-links-in-listing").

### Include links in your product

description

The long description for an AWS Data Exchange product supports Markdown, which allows you to include
links in your product's details page. The following procedure shows you how to add links to
websites in your AWS Data Exchange product description.

###### To include embedded links in your product listing

1. Log into the AWS console and navigate to an [Amazon S3 bucket](https://console.aws.amazon.com/s3 "https://console.aws.amazon.com/s3") that your AWS Data Exchange user has
   access to. The contents of this bucket are publicly readable.
2. Upload the files (for example, documents such as PDF files or Microsoft Excel files)
   that you want to include in your product listing into the Amazon Simple Storage Service (Amazon S3) bucket. After
   the upload is complete, make sure you set the file or files to have public read access
   permissions.
3. Choose one of the uploaded files. In the **Overview** tab, you
   will see a URL for the file. Copy the URL to your clipboard.
4. Open the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
5. Choose the product you want to update, and then choose
   **Edit**.
6. From **Product Description**, use the following Markdown formats to
   link to relevant files (using the URL link you copied previously) or to another URL,
   like your website.
   - To link to a file stored in an S3 bucket:

   \*\*\_[`File name`](`Object URL from
 Amazon S3`)\_\*\*

   `Description of the object`.
   - To link to a trial product listing on AWS Data Exchange:

   \*\*\_[`Website
   Title]`(`URL`)\_\*\*

   `Description of the website`.

7. Choose **Save Changes**. After a few minutes your AWS Data Exchange product
   listing page should be updated with the new links.
