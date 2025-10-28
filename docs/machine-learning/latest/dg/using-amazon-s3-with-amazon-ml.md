We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Using Amazon S3 with Amazon ML

Amazon Simple Storage Service (Amazon S3) is storage for the Internet. You can use Amazon S3 to store and retrieve any
amount of data at any time, from anywhere on the web. Amazon ML uses Amazon S3 as a primary data
repository for the following tasks:

- To access your input files to create datasource objects for training and evaluating
  your ML models.
- To access your input files to generate batch predictions.
- When you generate batch predictions by using your ML models, to output the prediction
  file to an S3 bucket that you specify.
- To copy data that you've stored in Amazon Redshift or Amazon Relational Database Service (Amazon RDS) into a .csv file and
  upload it to Amazon S3.
  To enable Amazon ML to perform these tasks, you must grant permissions to Amazon ML to access your
  Amazon S3 data.

###### Note

You cannot output batch prediction files to an S3 bucket that accepts only server-side
encrypted files. Make sure that your bucket policy allows uploading unencrypted files by
confirming that the policy does not include a `Deny` effect for the
`s3:PutObject` action when there is no `s3:x-amz-server-side-encryption`
header in the request. For more information about S3 server-side encryption bucket
policies, see [Protecting Data Using Server-Side
Encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the [_Amazon Simple Storage Service User Guide_](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").

## Uploading Your Data to Amazon S3

You must upload your input data to Amazon Simple Storage Service (Amazon S3) because Amazon ML reads data from Amazon S3
locations. You can upload your data directly to Amazon S3 (for example, from your computer), or
Amazon ML can copy data that you've stored in Amazon Redshift or Amazon Relational Database
Service (RDS) into a .csv file and upload it to Amazon S3.

For more information about copying your data from Amazon Redshift or Amazon RDS, see
[Using Amazon Redshift with Amazon ML](using-amazon-redshift-with-amazon-ml.md "using-amazon-redshift-with-amazon-ml.md") or [Using Amazon RDS with Amazon ML](using-amazon-rds-with-amazon-ml.md "using-amazon-rds-with-amazon-ml.md"), respectively.

The remainder of this section describes how to upload your input data directly from
your computer to Amazon S3. Before you begin the procedures in this section, you need to have
your data in a .csv file. For information about how to correctly format your .csv file so
that Amazon ML can use it, see [Understanding
the Data Format for Amazon ML](understanding-the-data-format-for-amazon-ml.md "understanding-the-data-format-for-amazon-ml.md").

###### To upload your data from your computer to Amazon S3

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3](https://console.aws.amazon.com/s3 "https://console.aws.amazon.com/s3").
2. Create a bucket or choose an existing bucket.
   1. To create a bucket, choose **Create Bucket**. Name your
      bucket, choose a region (you can choose any available region), and then choose
      **Create**. For more information, see [Create a
      Bucket](../../../AmazonS3/latest/gsg/CreatingABucket.md "../../../AmazonS3/latest/gsg/CreatingABucket.md") in the _Amazon Simple Storage Getting Started
      Guide_.
   2. To use an existing bucket, search for the bucket by choosing the bucket in the
      **All Buckets** list. When the bucket name appears, select it,
      and then choose **Upload**.

3. In the **Upload** dialog box, choose **Add
   Files**.
4. Navigate to the folder that contains your input data .csv file, and then choose
   **Open**.

## Permissions

To grant permissions for Amazon ML to access one of your S3 buckets, you must edit the bucket
policy.

For information about granting Amazon ML permission to read data from your bucket in Amazon S3, see
[Granting Amazon ML Permissions to Read Your Data from Amazon S3](granting-amazon-ml-permissions-to-read-your-data-from-amazon-s3.md "granting-amazon-ml-permissions-to-read-your-data-from-amazon-s3.md").

For information about granting Amazon ML permission to output the batch prediction results to
your bucket in Amazon S3, see [Granting Amazon ML Permissions to Output Predictions to Amazon S3](granting-amazon-ml-permissions-to-output-predictions-to-amazon-s3.md "granting-amazon-ml-permissions-to-output-predictions-to-amazon-s3.md")
.

For information about managing access permissions to Amazon S3 resources, see the [Amazon S3
Developer Guide](../../../AmazonS3/latest/dev/s3-access-control.md "../../../AmazonS3/latest/dev/s3-access-control.md").
