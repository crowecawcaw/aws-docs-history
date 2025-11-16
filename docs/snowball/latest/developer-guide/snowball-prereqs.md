AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Prerequisites for using Snowball Edge

Before you get started with a Snowball Edge, you need to sign up for an AWS account if you don't have one. We also recommend learning how to configure your data and compute instances for use with Snowball Edge.

AWS Snowball Edge is a region-specific service. So before you plan your job, be sure that
the service is available in your AWS Region.
Ensure that your location and Amazon S3 bucket are within the same AWS Region or
the same country because it will impact your ability to order the device.

To use Amazon S3 compatible storage on Snowball Edge with compute optimized devices for local edge compute and storage jobs, you need to provision S3 capacity on the device or devices when you order. Amazon S3 compatible storage on Snowball Edge supports local bucket management, so you can create S3 buckets on the device or cluster after you receive the device or devices.

As part of the order process, you create an AWS Identity and Access Management (IAM) role and an AWS Key Management Service
(AWS KMS) key. The KMS key is used to encrypt the unlock code for your job. For more information about creating IAM roles and KMS keys, see
[Creating a job to order a Snowball Edge device](create-job-common.md "create-job-common.md").

###### Note

In the Asia Pacific (Mumbai) AWS Region service is provided by Amazon on Internet
Services Private Limited (AISPL). For information on signing up for Amazon Web Services in
the Asia Pacific (Mumbai) AWS Region, see [Signing
Up for AISPL](../../../awsaccountbilling/latest/aboutv2/manage-account-payment-aispl.md#aisplsignup "../../../awsaccountbilling/latest/aboutv2/manage-account-payment-aispl.md#aisplsignup").

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [About your environment](#sbe-before-questions "#sbe-before-questions")
- [Working with filenames that contain
  special characters](#sbe-before-data-format "#sbe-before-data-format")
- [Amazon S3 encryption with AWS KMS](#s3-kms-encryption "#s3-kms-encryption")
- [Amazon S3 encryption with server-side encryption](#s3-sse-encryption "#s3-sse-encryption")
- [Prerequisites for using Amazon S3 adapter on Snowball Edge for import and export jobs](#s3-prereqs "#s3-prereqs")
- [Prerequisites for using Amazon S3 compatible storage on Snowball Edge](#s3-on-snowprereqs "#s3-on-snowprereqs")
- [Prerequisites for using compute instances on Snowball Edge](#compute-prereqes "#compute-prereqes")

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## About your environment

Understanding your dataset and how the local environment is set up will help you
complete your data transfer. Consider the following before placing your order.

**What data are you transferring?**

Transferring a large number of small files does not work well with
AWS Snowball Edge. This is because Snowball Edge Edge encrypts each individual
object. Small files include files under 1 MB in size. We recommend that you
zip them up before transferring them onto the AWS Snowball Edge device. We
also recommend that you have no more than 500,000 files or directories
within each directory.

**Will the data be accessed during the transfer?**

It is important to have a static dataset, (that is, no users or systems
are accessing the data during transfer). If not, the file transfer can fail
due to a checksum mismatch. The files won't be transferred and the files
will be marked as `Failed`.

To prevent corrupting your data, don't disconnect an AWS Snowball Edge
device or change its network settings while transferring data. Files should
be in a static state while being written to the device. Files that are
modified while they are being written to the device can result in read/write
conflicts.

**Will the network support AWS Snowball Edge data transfer?**

Snowball Edge supports the _RJ45_,
_SFP+_, or _QSFP+_ networking adapters. Verify that your switch is a
gigabit switch. Depending on the brand of switch, it might say
**gigabit** or **10/100/1000**.
Snowball Edge devices do not support a megabit switch, or 10/100
switch.

## Working with filenames that contain

special characters

It's important to note that if the names of your objects contain special characters, you might
encounter errors. Although Amazon S3 allows special characters, we highly recommend that you
avoid the following characters:

- Backslash ("\")
- Left curly brace ("{")
- Right curly brace ("}")
- Left square bracket ("[")
- Right square bracket ("]")
- 'Less Than' symbol ("<")
- 'Greater Than' symbol (">")
- Non-printable ASCII characters (128–255 decimal characters)
- Caret ("^")
- Percent character ("%")
- Grave accent / back tick ("`")
- Quotation marks
- Tilde ("~")
- 'Pound' character ("#")
- Vertical bar / pipe ("|")

If your files have one or more of these characters in object names, rename the objects before you copy them
to the AWS Snowball Edge device. Windows users who have spaces in their file names
should be careful when copying individual objects or running a recursive command.
In commands, surround the names of objects that include spaces in the names with quotation marks. The
following are examples of such files.

| Operating system | File name: test file.txt                         |
| ---------------- | ------------------------------------------------ |
| Windows          | `“C:\Users\<username>\desktop\test<br>file.txt”` |
| iOS              | `/Users/<username>/test\ file.txt`               |
| Linux            | `/home/<username>/test\ file.txt`                |

###### Note

The only object metadata that is transferred is the object name and size.

## Amazon S3 encryption with AWS KMS

You can use the default AWS managed or customer managed encryption keys to protect
your data when importing or exporting data.

### Using Amazon S3 default bucket encryption with AWS KMS managed

keys

###### To enable AWS managed encryption with AWS KMS

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the Amazon S3 bucket that you want to encrypt.
3. In the wizard that appears on the right side, choose **Properties**.
4. In the **Default encryption** box, choose **Disabled**
   (this option is grayed out) to enable default encryption.
5. Choose **AWS-KMS** as the encryption method, and then choose
   the KMS key that you want to use. This key is used to encrypt objects that
   are PUT into the bucket.
6. Choose **Save**.

After the Snowball Edge job is created, and before the data is imported, add a
statement to the existing IAM role policy. This is the role you created during the
ordering process. Depending on the job type, the default role name looks similar to
`Snowball-import-s3-only-role` or
`Snowball-export-s3-only-role`.

The following are examples of such a statement.

**For importing data**

If you use server-side encryption with AWS KMS managed keys (SSE-KMS) to encrypt the
Amazon S3 buckets associated with your import job, you also need to add the following
statement to your IAM role.

###### Example Snowball import IAM role

```
{
    "Effect": "Allow",
    "Action": [
        "kms: GenerateDataKey",
	"kms: Decrypt"
    ],
    "Resource":"arn:aws:kms:us-west-2:123456789012:key/abc123a1-abcd-1234-efgh-111111111111"
}
```

**For exporting data**

If you use server-side encryption with AWS KMS managed keys to encrypt the Amazon S3 buckets
associated with your export job, you also must add the following statement to your
IAM role.

###### Example Snowball export IAM role

```
{
    "Effect": "Allow",
    "Action": [
        "kms:Decrypt"
    ],
    "Resource":"arn:aws:kms:us-west-2:123456789012:key/abc123a1-abcd-1234-efgh-111111111111"
}
```

### Using S3 default bucket encryption with AWS KMS customer

keys

You can use the default Amazon S3 bucket encryption with your own KMS keys to protect data you
are importing and exporting.

**For importing data**

###### To enable customer managed encryption with AWS KMS

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the left navigation pane, choose **Customer managed keys**, and then
   choose the KMS key associated with the buckets that you want to use.
4. Expand **Key Policy** if it is not already expanded.
5. In the **Key Users** section, choose **Add** and search for
   the IAM role. Choose the IAM role, and then choose
   **Add**.
6. Alternatively, you can choose **Switch to Policy view** to display the key
   policy document and add a statement to the key policy. The following is an
   example of the policy.

###### Example of a policy for the AWS KMS customer managed key

```
{
  "Sid": "Allow use of the key",
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "arn:aws:iam::111122223333:role/snowball-import-s3-only-role"
    ]
  },
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "*"
}
```

After this policy has been added to the AWS KMS customer managed key, it is also needed
to update the IAM role associated with the Snowball job. By default, the role is
`snowball-import-s3-only-role`.

###### Example of the Snowball import IAM role

```
{
  "Effect": "Allow",
  "Action": [
    "kms: GenerateDataKey",
    "kms: Decrypt"
  ],
  "Resource": "arn:aws:kms:us-west-2:123456789012:key/abc123a1-abcd-1234-efgh-111111111111"
}
```

For more information, see [Using Identity-Based Policies
(IAM Policies) for AWS Snowball Edge](access-control-managing-permissions.md "access-control-managing-permissions.md").

The KMS key that is being used looks like the following:

`“Resource”:“arn:aws:kms:`region`:`AccoundID`:key/*”`

**For exporting data**

###### Example of a policy for the AWS KMS customer managed key

```
{
  "Sid": "Allow use of the key",
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "arn:aws:iam::111122223333:role/snowball-import-s3-only-role"
    ]
  },
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "*"
}
```

After this policy has been added to the AWS KMS customer managed key, it is also needed to
update the IAM role associated with the Snowball job. By default, the role looks
like the following:

`snowball-export-s3-only-role`

###### Example of the Snowball export IAM role

```
{
  "Effect": "Allow",
  "Action": [
    "kms: GenerateDataKey",
    "kms: Decrypt"
  ],
  "Resource": "arn:aws:kms:us-west-2:123456789012:key/abc123a1-abcd-1234-efgh-111111111111"
}
```

After this policy has been added to the AWS KMS customer managed key, it is also needed
to update the IAM role associated with the Snowball job. By default, the role is
`snowball-export-s3-only-role`.

## Amazon S3 encryption with server-side encryption

AWS Snowball Edge supports server-side encryption with Amazon S3 managed encryption keys (SSE-S3).
Server-side encryption is about protecting data at rest, and SSE-S3 has strong,
multifactor encryption to protect your data at rest in Amazon S3. For more information about
SSE-S3, see [Protecting Data
Using Server-Side Encryption with Amazon S3-Managed Encryption Keys (SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") in
the _Amazon Simple Storage Service User Guide_.

###### Note

Currently, AWS Snowball Edge doesn't support server-side encryption with
customer-provided keys (SSE-C). However, you might want to use that SSE type to
protect data that has been imported, or you might already use it on data you want to
export. In these cases, keep the following in mind:

- **Import** – If you want to use SSE-C
  to encrypt the objects that you've imported into S3, copy those objects into
  another bucket that has SSE-KMS or SSE-S3 encryption established as a part
  of that bucket's bucket policy.
- **Export** – If you want to export
  objects that are encrypted with SSE-C, first copy those objects to another
  bucket that either has no server-side encryption, or has SSE-KMS or SSE-S3
  specified in that bucket's bucket policy.

## Prerequisites for using Amazon S3 adapter on Snowball Edge for import and export jobs

You can use S3 adapter on Snowball Edge when you are using the devices to move data from on-premises data sources to the cloud or from the cloud to on-premises data storage. For more information, see [Transferring files using the Amazon S3 adapter for data migration to or from Snowball Edge](using-adapter.md "using-adapter.md").

The Amazon S3 bucket associated with the job must use the Amazon S3 standard storage class.
Before creating your first job, keep the following in mind.

For jobs that import data into Amazon S3, follow these steps:

- Confirm that the files and folders to transfer are named according to the
  [object key
  naming guidelines](../../../AmazonS3/latest/userguide/UsingMetadata.md#object-key-guidelines "../../../AmazonS3/latest/userguide/UsingMetadata.md#object-key-guidelines") for Amazon S3. Any files or folders with names that
  don't meet these guidelines aren't imported into Amazon S3.
- Plan what data you want to import into Amazon S3. For more information, see [Planning your large transfer with Snowball Edge](LargeDataMigration.md#copy-general-planning "LargeDataMigration.md#copy-general-planning").

Before exporting data from Amazon S3, follow these steps:

- Understand what data is exported when you create your job. For more
  information, see [Using Amazon S3 object keys when exporting data to a Snowball Edge device](exporttype.md#ranges "exporttype.md#ranges").
- For any files with a colon (`:`) in the file name, change the file
  names in Amazon S3 before you create the export job to get these files. Files with a
  colon in the file name fail export to Microsoft Windows Server.

## Prerequisites for using Amazon S3 compatible storage on Snowball Edge

You use Amazon S3 compatible storage on Snowball Edge when you are storing data on the device at your edge location and using the data for local compute operations. Data used for local compute operations will not be imported to Amazon S3 when the device is returned.

When ordering a Snow device for local compute and storage with Amazon S3 compatible storage, keep the following in mind.

- You will provision Amazon S3 storage capacity when you order the device. So consider your storage need before ordering a device.
- You can create Amazon S3 buckets on the device after you receive it rather than while ordering a Snowball Edge device.
- You will need to download the latest version of the AWS CLI (v2.11.15 or higher), Snowball Edge client, or AWS OpsHub and install it on your computer to use Amazon S3 compatible storage on Snowball Edge.
- After receiving your device, configure, start, and use Amazon S3 compatible storage on Snowball Edge according to [Using Amazon S3 compatible storage on Snowball Edge](s3compatible-on-snow.md "s3compatible-on-snow.md") in this guide.

## Prerequisites for using compute instances on Snowball Edge

You can run Amazon EC2-compatible compute instances hosted on a AWS Snowball Edge with the
`sbe1`, `sbe-c`, and `sbe-g` instance types:

- The `sbe1` instance type works on devices with the Snowball Edge Edge
  Storage Optimized option.
- The `sbe-c` instance type works on devices with the Snowball Edge Edge
  Compute Optimized option.

All the compute instance types supported on Snowball Edge Edge device options are unique to
AWS Snowball Edge devices. Like their cloud-based counterparts, these instances require
Amazon Machine Images (AMIs) to launch. You choose the AMI for an instance before you
create your Snowball Edge Edge job.

To use a compute instance on a Snowball Edge Edge, create a job to order a Snowball Edge device and specify your AMIs. You
can do this using the AWS Snowball Edge Management Console, the AWS Command Line Interface (AWS CLI), or one of the
AWS SDKs. Typically, to use your instances, there are some housekeeping prerequisites that
you must perform before creating your job.

For jobs using compute instances, before you can add any AMIs to your job, you must have an AMI in your AWS account
and it must be a supported image type. Currently, supported AMIs are based on these operating systems:

- [Amazon Linux 2](https://aws.amazon.com/marketplace/pp/B08Q76DLTM "https://aws.amazon.com/marketplace/pp/B08Q76DLTM")
- [CentOS 7 (x86_64) - with Updates HVM](https://aws.amazon.com/marketplace/pp/B00O7WM7QW "https://aws.amazon.com/marketplace/pp/B00O7WM7QW")
- Ubuntu 16.04 LTS - Xenial (HVM)
- [Ubuntu 20.04 LTS - Focal](https://aws.amazon.com/marketplace/pp/prodview-iftkyuwv2sjxi "https://aws.amazon.com/marketplace/pp/prodview-iftkyuwv2sjxi")
- [Ubuntu 22.04 LTS - Jammy](https://aws.amazon.com/marketplace/pp/prodview-f2if34z3a4e3i "https://aws.amazon.com/marketplace/pp/prodview-f2if34z3a4e3i")
- [Microsoft Windows Server 2012 R2](https://aws.amazon.com/marketplace/pp/prodview-g3y27m7b55tag "https://aws.amazon.com/marketplace/pp/prodview-g3y27m7b55tag")
- [Microsoft Windows Server 2016](https://aws.amazon.com/marketplace/pp/prodview-fsarquezghuic "https://aws.amazon.com/marketplace/pp/prodview-fsarquezghuic")
- [Microsoft Windows Server 2019](https://aws.amazon.com/marketplace/pp/prodview-bd6o47htpbnoe "https://aws.amazon.com/marketplace/pp/prodview-bd6o47htpbnoe")

###### Note

Ubuntu 16.04 LTS - Xenial (HVM) images are no longer supported in the AWS Marketplace, but still supported for use on Snowball Edge devices through Amazon EC2 VM Import/Export and running locally in AMIs.

You can get these images from [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

If you're using SSH to connect to the instances running on a Snowball Edge, you can use your own key pair or you can create one on the Snowball Edge. To use AWS OpsHub to create a key pair on the device, see [Working with key pairs for EC2-compatible instances in AWS OpsHub](working-with-key-pair.md "working-with-key-pair.md"). To use the AWS CLI to create a key pair on the device, see `create-key-pair` in [List of supported EC2-compatible AWS CLI
commands on a Snowball Edge](using-ec2-endpoint.md#list-cli-commands-ec2-edge "using-ec2-endpoint.md#list-cli-commands-ec2-edge").
For more information on key pairs and Amazon Linux 2, see [Amazon EC2 key pairs and Linux instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the Amazon EC2 User Guide.

For information specific to using compute instances on a device, see [Using Amazon EC2-compatible compute instances on Snowball Edge](using-ec2.md "using-ec2.md").
