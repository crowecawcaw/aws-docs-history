# Step 1: Upload data to Amazon S3

Suppose you have data that you want to turn into Salesforce account records. You acquired
this data from a web form and used it to generate account records. You can upload this list
of additional accounts to Amazon Simple Storage Service (Amazon S3). Amazon AppFlow can transfer the data from Amazon S3 to
Salesforce to synchronize your customer relationship management (CRM) data.

To use Amazon S3 as your source for the flow, create a storage container, called a bucket, and
populate it with data. Amazon AppFlow can transfer the data within an S3 bucket to any of the
supported destinations. In this step, you create an S3 bucket, create a source folder within
the S3 bucket, and upload sample data to the source folder.

###### Topics

- [(Optional) Download sample data](#tutorial-download-data "#tutorial-download-data")
- [Create an S3 bucket](#tutorial-create-bucket "#tutorial-create-bucket")
- [Create a folder](#tutorial-create-folder "#tutorial-create-folder")
- [Upload data](#tutorial-upload-data "#tutorial-upload-data")
- [Additional resources](#tutorial-s3-additional-resources "#tutorial-s3-additional-resources")

## (Optional) Download sample data

If you have your own data that you want to use for this tutorial, you can skip this
step. Also, if you use a SaaS application other than Salesforce, this sample data may
not be useful.

The sample data includes nine account records. Download this sample data set.

###### To get the sample data

1. Download the zip file [tutorial-account-data.zip](samples/tutorial-account-data.md "samples/tutorial-account-data.md").
2. Extract the zip file. The unzipped file called `tutorial-account-data.csv` contains the sample data set.

## Create an S3 bucket

After you extract your sample data, use the AWS Management Console to create an S3 bucket to store
your data. Your S3 bucket must occupy the same AWS Region as the one where you want to
use Amazon AppFlow.

###### To create an S3 bucket

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** section, choose **Create bucket**.
3. For **Bucket name**, enter a descriptive name.
   The name must be globally unique. For example, enter
   ``username`-appflow-tutorial`.
4. For **AWS Region**, choose the same Region as
   your Amazon AppFlow console.

###### Warning

If your S3 bucket isn't in the same AWS Region as your console, your flow can't access it. 5. Keep the other settings at their default values. Choose **Create bucket**.

## Create a folder in an S3 bucket

Now that you have an S3 bucket, use the console to create a folder in the bucket where
you want to store the sample data. While a folder isn't essential, it's useful for
keeping your files organized.

###### To create a folder in Amazon S3

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** section, choose your S3 bucket from the list.
3. Under the **Objects** tab, choose **Create folder**.
4. For the folder name, enter `source`.
5. Choose **Create folder**.

## Upload data to Amazon S3

Now that you have set up your S3 bucket, upload the data.

###### To populate the S3 bucket with data

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** section, choose your S3 bucket from the
   list.
3. Choose the `source` folder. Then, under the **Objects** tab, choose **Upload**.
4. Choose **Add files**, and choose your data set. If
   you downloaded the sample data set, choose the
   `tutorial-account-data.csv` file.
5. Choose **Upload**.

You now have an S3 bucket with sample data in the `source`
folder.

## Additional resources

For more information on Amazon S3, see the following resources:

- [Amazon S3](s3.md "s3.md") in the _Amazon AppFlow User Guide_.
- [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") in the _Amazon S3 User Guide_.
