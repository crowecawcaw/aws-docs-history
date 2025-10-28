# Subscribing to and accessing an AWS Data Exchange product

containing Amazon S3 data access

AWS Data Exchange for Amazon S3 allows data subscribers to access third-party data files directly from
data providers' Amazon S3 buckets.

As a data subscriber, after you are entitled to an AWS Data Exchange for Amazon S3 data set, you can
start your data analysis with AWS services such as Amazon Athena, SageMaker AI Feature Store, or
Amazon EMR directly using the provider's data in their Amazon S3 buckets.

Consider the following:

- Providers have the option to enable **Requester Pays**, an Amazon S3
  feature, on the Amazon S3 bucket hosting the data offered. If enabled, subscribers pay to
  read, use, transfer, export, or copy data into their Amazon S3 buckets. For more information,
  see [Using Requester Pays buckets
  for storage transfers and usage](../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md") in the _Amazon Simple Storage Service User Guide_.
- When you subscribe to an AWS Data Exchange for Amazon S3 data product, AWS Data Exchange automatically provisions
  an Amazon S3 access point and updates its resource policies to grant you read-only access.
  Amazon S3 access points is a feature of Amazon S3 that simplifies data sharing to an Amazon S3 bucket.
  For more information, see [Managing data access with Amazon S3
  access points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md") in the _Amazon Simple Storage Service User Guide_.
- Before you use the Amazon S3 access point Amazon Resource Name (ARN) or alias to access
  the shared data, you must update your IAM permissions. You can verify that the current
  role and its associated policy allows `GetObject` and `ListBucket`
  calls to the provider’s Amazon S3 bucket and the Amazon S3 access point provided by AWS Data Exchange.
  The following sections describe the complete process of becoming an AWS Data Exchange for Amazon S3
  subscriber by using the AWS Data Exchange console.

The process has the following steps:

###### Steps

- [Step 1: Subscribing to products
  containing Amazon S3 data access](#subscribe-s3-data-access-product "#subscribe-s3-data-access-product")
- [Step 2: Accessing a product containing Amazon S3
  data access](#use-S3-data-access-product "#use-S3-data-access-product")

## Step 1: Subscribing to products

containing Amazon S3 data access

If you subscribe to a paid product, you're billed on your AWS bill. You get access
to all data sets included in the product. For more information, see [Subscribing to AWS Data Exchange data products on AWS Data Exchange](subscribe-to-data-sets.md "subscribe-to-data-sets.md").

###### To subscribe to a product containing access to Amazon S3

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **Discover data
   products**, choose **Browse catalog**.

For more information, see [Browse the catalog](subscriber-getting-started.md#browse-catalog "subscriber-getting-started.md#browse-catalog"). 3. Under **Refine results**, use the **Data set
type** filter and select **Access to Amazon S3** to find
products containing access to Amazon S3 data.

For more information, see [Browse the catalog](subscriber-getting-started.md#browse-catalog "subscriber-getting-started.md#browse-catalog"). 4. Select a product and view its product detail page.

The information on the product detail page includes a product description, the
provider's contact information, and the details of the product's public offer. The
public offer information includes price and duration, the data subscription agreement
(DSA), and the refund policy. You can view the names of the data sets included in the
product and the AWS Regions in which they are available. You can also continue to
browse other product detail pages by choosing a product under **Similar
products**.

If the provider has issued a custom offer to your account (for example, a [private offer](subscribe-to-private-offer.md "subscribe-to-private-offer.md") or [Bring Your Own Subscription (BYOS) offer)](subscribe-to-byos-offer.md "subscribe-to-byos-offer.md"),
you see those details, too. 5. In the top right corner, choose **Continue to subscribe**. 6. Review the **Product offer**, the **Subscription
terms**, the **Data sets** that are included in the offer,
and the **Support information**. 7. Choose whether enable **Offer auto-renewal** for the
subscription

###### Note

Some products require subscription verification. For more information, see [Subscription verification for subscribers in
AWS Data Exchange](subscription-verification-sub.md "subscription-verification-sub.md"). 8. Choose **Subscribe**.

###### Note

If you subscribe to a paid product, you're prompted to confirm your decision to
subscribe. 9. Under **Data sets included with your subscription**, view the
listed **Data sets**.

After the subscription finishes processing, you can choose a data set to access
your entitled data or choose **View subscription** to view your
subscription.

## Step 2: Accessing a product containing Amazon S3

data access

You can run queries to analyze the data in-place without setting up your own Amazon S3
buckets, copying data files into Amazon S3 buckets, or paying associated storage fees. You
access the same Amazon S3 objects that the data provider maintains allowing you to use the most
current data available.

With a subscription, you can do the following:

- Analyze data without setting up individual Amazon S3 buckets, copying files, or paying
  storage fees.
- Access the latest provider data as soon as the provider updates it.

###### To view the data sets, revisions, and assets

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left navigation pane, under **My subscriptions**, choose
   **Entitled data**.
3. On the **Entitled data page**, expand a product and choose a data
   set.
4. View the **Data set overview**.

###### Note

The data provided is stored in the provider's Amazon S3 bucket. When accessing this
data, you’ll be responsible for the cost of the request and the data downloaded from
the provider’s Amazon S3 bucket, unless the provider specifies otherwise. 5. Before getting started, your role must have IAM permissions to use your entitled
Amazon S3 data access. On the **Data set overview** page, on the
**Amazon S3 data access** tab, select **Verify IAM
permissions** to determine if your role has the correct permissions to
access your data. 6. If you have the necessary IAM permissions, choose **Next** on
the **IAM Policy** prompt displayed. If you don't have the needed
permissions, follow the prompt to embed the JSON policy in the user or role. 7. Review your **Shared locations** to view the Amazon S3 bucket or
prefixes and objects shared by the provider. Review the data access information for
Amazon S3 Access Point information to determine if the provider enabled **Requester
Pays**. 8. Choose **Browse shared Amazon S3 locations** to view and
explore the provider's Amazon S3 bucket, prefixes, and objects shared. 9. Use the **Access Point** alias anywhere you use Amazon S3 bucket names
to access your entitled data programmatically. For more information, see [Using access
points with compatible Amazon S3 operations](../../../AmazonS3/latest/userguide/access-points-usage-examples.md "../../../AmazonS3/latest/userguide/access-points-usage-examples.md") in the _Amazon Simple Storage Service User Guide_. 10. (Optional) When you gain an entitlement to an Amazon S3 data access data set that
contains data encrypted with a provider’s AWS KMS key, you can view the KMS key
ARN in your subscriber console. AWS Data Exchange creates an AWS KMS grant on the key for you, so
you can access the encrypted data. You must obtain `kms:Decrypt` IAM
permission on the KMS key to read encrypted data from the Amazon S3 Access
Point from which you’ve gained entitlement. You can choose between the following IAM
policy statements:

    1. IAM policy allowing users to decrypt or encrypt data with any
     KMS key.



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "kms:Decrypt"
     ],
     "Resource": [
     "*"
     ]
     }
     ]
    }`

    ```
    2. IAM policy allowing users to specify the exact KMS key ARNs visible in the
     subscriber console.



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "kms:Decrypt"
     ],
     "Resource": [
     "arn:aws:kms:`us-east-1`:`111122223333`:key/`KeyId`"
     ]
     }
     ]
    }`

    ```###### Note

AWS KMS grants can take up to 5 minutes for the operation to achieve eventual
consistency. You might not have access to the Amazon S3 data access data set
until this is complete. For more information, see [Grant in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the
_AWS Key Management Service Developer Guide_.

For more information about how to subscribe to an Amazon S3 data set, see Subscribing to and accessing an AWS Data Exchange product
containing Amazon S3 data access.
