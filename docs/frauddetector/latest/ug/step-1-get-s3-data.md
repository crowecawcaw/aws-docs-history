Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Get and upload example dataset

The example dataset you use in this tutorial provides details of online account registrations. The dataset is in a text
file that uses comma-separated value (CSV) in the UTF-8 format. The first row of the CSV dataset file contains the headers. The
header row is followed by multiple rows of data. Each of these rows consists of data elements from a single account registration. The data
is labeled for your convenience. A column in the dataset identifies whether the account registration is fraudulent.

###### To get and upload example dataset

1. Go to [Samples](https://github.com/aws-samples/aws-fraud-detector-samples/tree/master/data "https://github.com/aws-samples/aws-fraud-detector-samples/tree/master/data").

There are two data files that has online account registration data - _registration_data_20K_minimum.csv_
and _registration_data_20K_full.csv_. The file
`registration_data_20K_minimum` contains only two variables:
_ip_address_ and _email_address_. The
file `registration_data_20K_full` contains other variables.
These variables are for each event and they include _billing_address_,
_phone_number_, and _user_agent_. Both data files also
contain two mandatory fields:

    * EVENT\_TIMESTAMP – Defines when the event occurred
    * EVENT\_LABEL – Classifies the event as fraudulent or legitimate

You can use either one of the two files for this tutorial. Download the data file you want to use. 2. Create an Amazon Simple Storage Service (Amazon S3) bucket.

In this step, you create an external storage to store the dataset. This external storage is
Amazon S3 bucket. For more information about Amazon S3, see [What is Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")

    1. Sign in to the AWS Management Console and open the Amazon S3 console at
     [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
    2. In **Buckets**, choose **Create
     bucket**.
    3. For **Bucket name**, enter a bucket name. Make sure that you
     follow the bucket naming rules in the console, and provide a globally unique
     name. We recommend you use a name that describes the bucket's purpose.
    4. For **AWS Region**, choose the AWS Region where
     you want to create your bucket. The Region that you choose must support Amazon Fraud Detector. To reduce latency,
     choose the AWS Region that's closest to your geographic location. For
     a list of Regions that support Amazon Fraud Detector, see the [Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") in the *Global Infrastructure
     Guide*.
    5. Leave the default settings for **Object Ownership**,
     **Bucket settings for Block Public Access**,
     **Bucket Versioning**, and
     **Tags** for this tutorial.
    6. For **Default encryption**, choose
     **Disable** for this tutorial.
    7. Review your bucket configuration, and then choose **Create
     bucket**.

3. Upload example data file to Amazon S3 bucket.

Now that you have a bucket, upload one of the example files
that you downloaded previously to the Amazon S3 bucket that you just created.

    1. In the **Buckets**, your bucket name is listed. Choose your bucket.
    2. Choose **Upload**.
    3. In **Files and folders**, choose **Add
     files**.
    4. Choose one of the example data files that you downloaded on your computer, and then choose
     **Open**.
    5. Leave the default settings for **Destination**,
     **Permissions**, and
     **Properties**.
    6. Review configurations, and then choose
     **Upload**.
    7. The example data file is uploaded to Amazon S3 bucket. Make a note of the bucket location. In the **Objects**,
     choose the example data file that you just uploaded.
    8. In the **Object overview**, copy the location under
     **S3 URI**. This is the Amazon S3 location of your
     example data file. You use it later. You can additionally copy
     the **Amazon Resource Name (ARN)** of your
     S3 bucket and save it.
