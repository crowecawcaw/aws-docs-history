# Access an AWS Data Exchange data set containing Amazon S3 data

access

**Overview for recipients**

AWS Data Exchange for Amazon S3 allows recipients to access third-party data files directly from data owners’
Amazon S3 buckets.

As a recipient, after you are entitled to an AWS Data Exchange for Amazon S3 data set, you can start your
data analysis with AWS services such as Amazon Athena, SageMaker AI Feature Store, or Amazon EMR directly using
the data owner’s data in their Amazon S3 buckets.

###### Consider the following:

- Data owners have the option to enable **Requester Pays**, an Amazon S3
  feature, on the Amazon S3 bucket hosting the data oﬀered. If enabled, recipients pay to read, use,
  transfer, export, or copy data into theirAmazon S3 buckets. For more information, see [Using
  Requester Pays buckets for storage transfers and usage](../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md") in the _Amazon Simple Storage Service User Guide_.
- When you accept a data grant to an AWS Data Exchange for Amazon S3 data product, AWS Data Exchange automatically
  provisions an Amazon S3 access point and updates its resource policies to grant you read-only
  access. Amazon S3 access points is a feature of Amazon S3 that simplifies data sharing to an Amazon S3 bucket.
  For more information, see [Managing data
  access with Amazon S3 access points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md") in the _Amazon Simple Storage Service User
  Guide_.
- Before you use the Amazon S3 access point Amazon Resource Name (ARN) or alias to access the
  shared data, you must update your IAM permissions. You can verify that the current role and its
  associated policy allows GetObject and ListBucket calls to the provider’s Amazon S3 bucket and the
  Amazon S3 access point provided by AWS Data Exchange.
  The following sections describe the complete process of accessing an AWS Data Exchange for Amazon S3 data set
  after accepting a data grant by using the AWS Data Exchange console.

You can run queries to analyze the data in-place without setting up your own Amazon S3 buckets,
copying data files into Amazon S3 buckets, or paying associated storage fees. You access the same Amazon S3
objects that the data owner maintains allowing you to use the most current data available.

###### With a data grant, you can do the following:

- Analyze data without setting up individual Amazon S3 buckets, copying files, or paying storage
  fees.
- Access the latest provider data as soon as the data owner updates it.

###### To view the data sets, revisions, and assets

1. Open your web browser and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **My data**, choose
   **Entitled data sets**.
3. On the **Entitled data sets** page, choose a data set.
4. View the **Data set overview**.

###### Note

The data provided is stored in the data owner’s Amazon S3 bucket. When accessing this data,
you’ll be responsible for the cost of the request and the data downloaded from the owner’s
Amazon S3 bucket, unless the owner specifies otherwise. 5. Before getting started, your role must have IAM permissions to use your entitled Amazon S3
data access. On the **Data set overview** page, on the **Amazon S3 data
access** tab, select **Verify IAM permissions** to determine if
your role has the correct permissions to access your data. 6. If you have the necessary IAM permissions, choose **Next** on the
**IAM Policy** prompt displayed. If you don't have the needed permissions,
follow the prompt to embed the JSON policy in the user or role. 7. Review your **Shared locations** to view the Amazon S3 bucket or prefixes and
objects shared by the data owner. Review the data access information for Amazon S3 access point
information to determine if the data owner enabled **Requester Pays**. 8. Choose **Browse shared Amazon S3 locations** to view and explore the data
owner’s Amazon S3 bucket, prefixes, and objects shared. 9. Use the Access Point alias anywhere you use Amazon S3 bucket names to access your entitled data
programmatically. For more information, see [Using access points with compatible Amazon S3 operations](../../../AmazonS3/latest/userguide/access-points-usage-examples.md "../../../AmazonS3/latest/userguide/access-points-usage-examples.md") in the _Amazon Simple Storage Service User Guide_. 10. (Optional) When you gain an entitlement to an Amazon S3 data access data set that contains data
encrypted with a data owner’s AWS KMS key, you can view the KMS key ARN in your console.
AWS Data Exchange creates an AWS KMS grant on the key for you, so you can access the encrypted data. You must
obtain `kms:Decrypt`IAM permission on the AWS KMS key to read encrypted data
from the Amazon S3 Access Point from which you’ve gained entitlement. You can choose between the
following IAM policy statements:

    1. IAM policy allowing users to decrypt or encrypt data with any KMS key.



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [{

     "Effect": "Allow",
     "Action": ["kms:Decrypt"],
     "Resource": ["*"]
     }
     ]
    }`

    ```
    2. IAM policy allowing users to specify the exact KMS key ARNs visible in the recipient
     console.



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

    ```

###### Note

AWS KMS grants can take up to 5 minutes for the operation to achieve eventual consistency.
You might not have access to the Amazon S3 data access data set until this is complete. For more
information, see [Grants in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the _AWS KMS key Management Service
Developer Guide_.
