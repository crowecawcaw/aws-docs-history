# Viewing directory bucket properties

You can view and configure the properties for an Amazon S3 directory bucket by using the Amazon S3
console. For more information, see [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Directory buckets**.
3. In the **Directory buckets** list, choose the name of the bucket that
   you want to view the properties for.
4. Choose the **Properties** tab.
5. On the **Properties** tab, you can view the following properties for
   the bucket:
   - **Directory bucket overview** – You can see the
     AWS Region, Zone (Availability Zone or Local Zone), Amazon Resource Name (ARN), and creation date
     for the bucket.
   - **Server-side encryption settings** – Amazon S3 applies server-side
     encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for
     all S3 buckets. Amazon S3
     encrypts an object before saving it to a disk and decrypts the object when you
     download it. For more information, see [Setting and monitoring default encryption for directory buckets](s3-express-bucket-encryption.md "s3-express-bucket-encryption.md").

   For more information about supported features for directory buckets, see
   [Creating and using directory buckets](directory-buckets-overview.md#directory-buckets-working "directory-buckets-overview.md#directory-buckets-working").
