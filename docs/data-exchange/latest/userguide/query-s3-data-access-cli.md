# Setting up and querying AWS Data Exchange for Amazon S3 (Test

Product)

The following procedure shows how to set up and query an Amazon S3 data access data set using
the AWS Command Line Interface (AWS CLI). Before querying, you must obtain the appropriate AWS Identity and Access Management (IAM)
permissions to attach policies to your user. To access data in a provider's bucket directly
through the Amazon S3 delivery method, embed the following JSON policy to the user or role.

###### To set up AWS Data Exchange for Amazon S3 (Test Product)

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. From the left navigation pane under **My subscriptions**, choose
   **Entitled data** in the AWS Region that hosts the data set. For the
   purposes of this tutorial, the Region is **us-east-1**.
3. From the list of **Products**, choose **AWS Data Exchange for Amazon S3 (Test
   Product)** and then choose the **Blockchain Transactions (Test
   Data)** data set.
4. Choose **Verify IAM permissions**.

###### Note

If you don't have the correct permissions, you'll receive a notification detailing
how to create and attach the IAM policy to your user or role. In the following
example, replace each `user input placeholder` with your own
information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": [
 "arn:aws:s3:`us-east-1:111122223333`:accesspoint/`my-access-point`",
 "arn:aws:s3:::`aws-data-exchange-s3-data-access-btc-demo-us-east-1`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": [
 "arn:aws:s3:`us-east-1:111122223333`:accesspoint/`my-access-point`/object/*",
 "arn:aws:s3:::`aws-data-exchange-s3-data-access-btc-demo-us-east-1`/*"
 ]
 }
 ]
}`

```

###### To allow querying on the AWS Data Exchange for Amazon S3 (Test Product) data access data set using the

AWS CLI

1. Open **AWS CloudShell** in **us-east-1**.
2. Choose the copy button next to the access point alias to copy and paste the code
   inside. After the command is added inAWS CloudShell with the correct access point alias, you can
   see the list of Amazon S3 objects included in this product.

###### Important

When a provider has enabled Requester Pays, the subscriber pays for the data
transfer and the request. The provider pays for the data storage. For more information,
see [Using Requester Pays buckets
for storage transfers and usage](../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md") in the _Amazon Simple Storage Service User Guide_. 3. (Optional) You can also copy an object to your local system using the following
command.

`aws s3api get-object --bucket <Access point alias> --key
 'v1.0/btc/transactions/date=2022-11-27/part-00000-03a88dba-27dd-4f59-a890-70a3d2c7ad26-c000.snappy.parquet'
 AWS_btc.snappy.parquet --request-payer requester`
