

# Viewing directory bucket properties
<a name="directory-bucket-view"></a>

You can view and configure the properties for an Amazon S3 directory bucket by using the Amazon S3 console. For more information, see [Working with directory buckets](directory-buckets-overview.md).

## Using the S3 console
<a name="directory-bucket-view-console"></a>

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Directory buckets**.

1. In the **Directory buckets** list, choose the name of the bucket that you want to view the properties for.

1. Choose the **Properties** tab.

1. On the **Properties** tab, you can view the following properties for the bucket:
   + **Directory bucket overview** – You can see the AWS Region, Zone (Availability Zone or Local Zone), Amazon Resource Name (ARN), and creation date for the bucket.
   + **Server-side encryption settings** – Amazon S3 applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for all S3 buckets. Amazon S3 encrypts an object before saving it to a disk and decrypts the object when you download it. For more information, see [Setting and monitoring default encryption for directory buckets](s3-express-bucket-encryption.md).

     For more information about supported features for directory buckets, see [Creating and using directory buckets](directory-buckets-overview.md#directory-buckets-working).