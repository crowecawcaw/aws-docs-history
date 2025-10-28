Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Data Protection in AWS Snowball Edge Edge

AWS Snowball Edge conforms to the AWS [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), which includes regulations and guidelines for data protection. AWS is
responsible for protecting the global infrastructure that runs all the AWS services. AWS
maintains control over data hosted on this infrastructure, including the security
configuration controls for handling customer content and personal data. AWS customers and
APN partners, acting either as data controllers or data processors, are responsible for any
personal data that they put in the AWS Cloud.

For data protection purposes, we recommend that you protect AWS account credentials and
set up individual users with AWS Identity and Access Management (IAM), so that each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you secure your data
in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We recommend TLS 1.2 or later.

- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls within AWS
  services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing personal data that is stored in Amazon S3.
- If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more
  information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS)
  140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put sensitive identifying information, such as your
  customers' account numbers, into free-form fields such as a **Name** field. This includes when you work with AWS Snowball Edge or other AWS
  services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  AWS Snowball Edge or other services might get picked up for inclusion in diagnostic logs. When you
  provide a URL to an external server, don't include credentials information in the URL to
  validate your request to that server.

For more information about data protection, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS
Security Blog_.

###### Topics

- [Protecting Data in the Cloud](#data-protection-cloud "#data-protection-cloud")
- [Protecting Data On Your Device](#data-protection-device "#data-protection-device")

## Protecting Data in the Cloud

AWS Snowball Edge protects your data when you're importing or exporting data into Amazon S3, when
you create a job to order a Snowball Edge device, and when your device is updated. The following sections describe how you
can protect your data when you use Snowball Edge Edge and are online or interacting with AWS in
the cloud.

###### Topics

- [Encryption for AWS Snowball Edge](#encryption "#encryption")
- [AWS Key Management Service in AWS Snowball Edge](#kms "#kms")

### Encryption for AWS Snowball Edge

When you're using a Snowball Edge to import data into S3, all data transferred to a
device is protected by SSL encryption over the network. To protect data at rest,
AWS Snowball Edge uses server side-encryption (SSE).

#### Server-Side Encryption in AWS Snowball Edge

AWS Snowball Edge supports server-side encryption with Amazon S3–managed
encryption keys (SSE-S3). Server-side encryption is about protecting data at rest, and
SSE-S3 has strong, multifactor encryption to protect your data at rest in Amazon S3. For more
information on SSE-S3, see [Protecting Data Using Server-Side Encryption with Amazon S3-Managed Encryption Keys
(SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") in the _Amazon Simple Storage Service User Guide_.

Currently, AWS Snowball Edge doesn't offer server-side encryption with
customer-provided keys (SSE-C). Amazon S3 compatible storage on Snowball Edge offers SSE-C for local compute and storage jobs. However, you might want to use that SSE type to protect
data that has been imported, or you might already use it on data you want to export. In
these cases, keep the following in mind:

- **Import** –

If you want to use SSE-C to encrypt the objects that you've imported into Amazon S3,
you should consider using SSE-KMS or SSE-S3 encryption instead established as a part
of that bucket's bucket policy. However, if you have to use SSE-C to encrypt the
objects that you've imported into Amazon S3, then you will have to copy the object within
your bucket to encrypt with SSE-C. A sample CLI command to achieve this is shown
below:

```
aws s3 cp s3://amzn-s3-demo-bucket/object.txt s3://amzn-s3-demo-bucket/object.txt --sse-c --sse-c-key 1234567891SAMPLEKEY
```

or

```
aws s3 cp s3://amzn-s3-demo-bucket s3://amzn-s3-demo-bucket --sse-c --sse-c-key 1234567891SAMPLEKEY --recursive
```

- **Export** – If you want to export objects
  that are encrypted with SSE-C, first copy those objects to another bucket that
  either has no server-side encryption, or has SSE-KMS or SSE-S3 specified in that
  bucket's bucket policy.

##### Enabling SSE-S3 for Data Imported into Amazon S3 from a

Snowball Edge

Use the following procedure in the Amazon S3 Management Console to enable SSE-S3 for
data being imported into Amazon S3. No configuration is necessary in the AWS Snow Family Management Console or
on the Snowball device itself.

To enable SSE-S3 encryption for the data that you're importing into Amazon S3, simply
set the bucket policies for all the buckets that you're importing data into. You
update the policies to deny upload object (`s3:PutObject`) permission if
the upload request doesn't include the `x-amz-server-side-encryption`
header.

###### To enable SSE-S3 for data imported into Amazon S3

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket that you're importing data into from the list of
   buckets.
3. Choose **Permissions**.
4. Choose **Bucket Policy**.
5. In the **Bucket policy editor**, enter the following policy.
   Replace all the instances of `YourBucket` in
   this policy with the actual name of your bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PutObjPolicy",
 "Statement": [
 {
 "Sid": "DenyIncorrectEncryptionHeader",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`YourBucket`/*",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-server-side-encryption": "AES256"
 }
 }
 },
 {
 "Sid": "DenyUnEncryptedObjectUploads",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`YourBucket`/*",
 "Condition": {
 "Null": {
 "s3:x-amz-server-side-encryption": "true"
 }
 }
 }
 ]
}`

```

6. Choose **Save**.

You've finished configuring your Amazon S3 bucket. When your data is imported into this
bucket, it is protected by SSE-S3. Repeat this procedure for any other buckets, as
necessary.

### AWS Key Management Service in AWS Snowball Edge

AWS Key Management Service (AWS KMS) is a managed service that makes it easy for you to create and
control the encryption keys used to encrypt your data. AWS KMS uses hardware security
modules (HSMs) to protect the security of your keys. Specifically, the Amazon Resource
Name (ARN) for the AWS KMS key that you choose for a job in AWS Snowball Edge is associated
with a KMS key. That KMS key is used to encrypt the unlock code for your job. The unlock
code is used to decrypt the top layer of encryption on your manifest file. The encryption
keys stored within the manifest file are used to encrypt and de-encrypt the data on the
device.

In AWS Snowball Edge, AWS KMS protects the encryption keys used to protect data on each
AWS Snowball Edge device. When you create your job, you also choose an existing KMS key.
Specifying the ARN for an AWS KMS key tells AWS Snowball Edge which AWS KMS keys to
use to encrypt the unique keys on the AWS Snowball Edge device. For more information on
AWS Snowball Edge supported Amazon S3 server-side-encryption options , see [Server-Side Encryption in AWS Snowball Edge](#sse "#sse").

#### Using the Managed Customer AWS KMS keys for

Snowball Edge Edge

If you'd like to use the managed customer AWS KMS keys for Snowball Edge Edge created
for your account, follow these steps.

###### To select the AWS KMS keys for your job

1. On the AWS Snow Family Management Console, choose **Create job**.
2. Choose your job type, and then choose **Next**.
3. Provide your shipping details, and then choose **Next**.
4. Fill in your job's details, and then choose **Next**.
5. Set your security options. Under **Encryption**, for
   **KMS key** either choose the AWS managed key
   or a custom key that was previously created in AWS KMS, or choose
   **Enter a key ARN** if you need to enter a key
   that is owned by a separate account.

###### Note

The AWS KMS key ARN is a globally unique identifier for
customer managed keys. 6. Choose **Next** to finish selecting your AWS KMS key. 7. Give the Snow device IAM user access to the KMS key.

    1. In the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")), go to **Encryption Keys** and open the KMS key you chose to use to encrypt the data on the device.
    2. Under **Key Users**, select **Add**, search for the Snow device IAM user and select **Attach**.

#### Creating a Custom KMS Envelope Encryption

Key

You have the option of using your own custom AWS KMS envelope encryption key with
AWS Snowball Edge. If you choose to create your own key, that key must be created in the
same region that your job was created in.

To create your own AWS KMS key for a job, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
_AWS Key Management Service Developer Guide_.

## Protecting Data On Your Device

### Securing your AWS Snowball Edge

Following are some security points that we recommend you consider when using
AWS Snowball Edge, and also some high-level information on other security precautions that
we take when a device arrives at AWS for processing.

We recommend the following security approaches:

- When the device first arrives, inspect it for damage or obvious tampering. If you
  notice anything that looks suspicious about the device, don't connect it to your
  internal network. Instead, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/"), and a new device will be shipped to you.
- You should make an effort to protect your job credentials from disclosure. Any
  individual who has access to a job's manifest and unlock code can access the contents
  of the device sent for that job.
- Don't leave the device sitting on a loading dock. Left on a loading dock, it can
  be exposed to the elements. Although each AWS Snowball Edge device is rugged, weather
  can damage the sturdiest of hardware. Report stolen, missing, or broken devices as
  soon as possible. The sooner such an issue is reported, the sooner another one can be
  sent to complete your job.

###### Note

The AWS Snowball Edge devices are the property of AWS. Tampering with
a device is a violation of the AWS Acceptable Use Policy. For more
information, see [http://aws.amazon.com/aup/](http://aws.amazon.com/aup/ "http://aws.amazon.com/aup/").

We perform the following security steps:

- When transferring data with the Amazon S3 adapter, object metadata is not persisted. The
  only metadata that remains the same is `filename` and
  `filesize`. All other metadata is set as in the following example:
  `-rw-rw-r-- 1 root root [filesize] Dec 31 1969 [path/filename]`
- When transferring data with the NFS interface, object metadata is persisted.
- When a device arrives at AWS, we inspect it for any signs of
  tampering and to verify that no changes were detected by the Trusted Platform Module
  (TPM). AWS Snowball Edge uses multiple layers of security designed to protect your
  data, including tamper-resistant enclosures, 256-bit encryption, and an
  industry-standard TPM designed to provide both security and full chain of custody for
  your data.
- Once the data transfer job has been processed and verified, AWS
  performs a software erasure of the Snowball device that follows the National Institute
  of Standards and Technology (NIST) guidelines for media sanitization.

### Validating NFC Tags

Snowball Edge Compute Optimized and Snowball Edge Storage Optimized (for data
transfer) devices have NFC tags built into them. You can scan these tags with the
AWS Snowball Edge Verification App, available on Android. Scanning and validating these
NFC tags can help you verify that your device has not been tampered with before you use
it.

Validating NFC tags includes using the Snowball Edge client to generate a
device-specific QR code to verify that the tags you're scanning are for the right
device.

The following procedure describes how to validate the NFC tags on a Snowball Edge
device. Before you get started, make sure you've performed the following first five steps
of the getting started exercise:

1. Create your Snowball Edge job. For more information, see [Creating a job to order a Snowball Edge device](create-job-common.md "create-job-common.md")
2. Receive the device. For more information, see [Receiving the Snowball Edge](receive-device.md "receive-device.md").
3. Connect to your local network. For more information, see [Connecting a Snowball Edge to your local
   network](getting-started.md#getting-started-connect "getting-started.md#getting-started-connect").
4. Get your credentials and tools. For more information, see [Getting credentials to access a Snowball Edge](getting-started.md#get-credentials "getting-started.md#get-credentials").
5. Download and install the Snowball Edge client. For more information, see [Downloading and installing the Snowball Edge
   Client](using-client-commands.md#download-the-client "using-client-commands.md#download-the-client").

###### To validate the NFC tags

1. Run the `snowballEdge get-app-qr-code` Snowball Edge client command.
   If you run this command for a node in a cluster, provide the serial number
   (`--device-sn`) to get a QR code for a single node. Repeat this step for
   each node in the cluster. For more information on using this command, see [Getting a QR code to validate Snowball Edge NFC tags](using-client-commands.md#client-qr-code "using-client-commands.md#client-qr-code").

The QR code is saved to a location of your choice as a .png file. 2. Navigate to the .png file that you saved, and open it so that you can scan the QR
code with the app. 3. You can scan these tags using the AWS Snowball Edge Verification App on Android.

###### Note

The AWS Snowball Edge Verification App is not available to download, but if you have a device with the app already installed, you can use the app. 4. Start the app, and follow the on-screen instructions.

You've now successfully scanned and validated the NFC tags for your device.

If you encounter issues while scanning, try the following:

- Confirm that your device has the Snowball Edge Compute Optimized options.
- If you have the app on another device, try using that device.
- Move the device to an isolated area of the room, away from interference from other
  NFC tags, and try again.
- If issues persist, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
