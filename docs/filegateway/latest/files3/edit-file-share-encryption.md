# Change the server-side encryption method

for an existing file share

The following procedure describes how to change the server-side encryption method for
an existing NFS or SMB file share using the Storage Gateway console. To perform this action
using the Storage Gateway API, see see [UpdateNFSFileShare](../../../storagegateway/latest/APIReference/API_UpdateNFSFileShare.md "../../../storagegateway/latest/APIReference/API_UpdateNFSFileShare.md") or [UpdateSMBFileShare](../../../storagegateway/latest/APIReference/API_UpdateSMBFileShare.md "../../../storagegateway/latest/APIReference/API_UpdateSMBFileShare.md") in the _AWS Storage Gateway API
Reference_.

###### Note

Updating the encryption method applies the new method to existing objects stored
in the Amazon S3 buckets after the update.

If you configure your File Gateway to use SSE-KMS for encryption, you must
manually add `kms:Encrypt`, `kms:Decrypt`,
`kms:ReEncrypt*`, `kms:GenerateDataKey`, and
`kms:DescribeKey` permissions to the IAM role associated with the
file share. For more information, see [Using
Identity-Based Policies (IAM Policies) for Storage Gateway](using-identity-based-policies.md "using-identity-based-policies.md").

###### To change the server-side encryption method for an NFS or SMB file share

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **File shares**, and then choose the file share for
   which you want to change the encryption method.
3. For **Actions**, choose **Edit file share
   encryption**.
4. For **Encryption**, choose the type of encryption you want to
   use for files at rest in Amazon S3:
   - To use server-side encryption managed with Amazon S3 (SSE-S3), choose
     **S3-Managed Keys (SSE-S3)**. For more information,
     see [Using
     server-side encryption with Amazon S3 managed keys](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") in the
     _Amazon Simple Storage Service User Guide_.
   - To use server-side encryption managed with AWS Key Management
     Service (SSE-KMS), choose **KMS-Managed Keys
     (SSE-KMS)**. For **Primary KMS key**,
     choose an existing AWS KMS key, or choose **Create a new KMS
     key** to create a new KMS key in the AWS Key Management
     Service (AWS KMS) console.

   For more information about AWS KMS, see [What is AWS Key
   Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service Developer
   Guide_.
   - To use dual-layer server-side encryption managed with AWS Key
     Management Service (DSSE-KMS), choose **Dual-layer server-side
     encryption with AWS Key Management Service keys (DSSE-KMS)**. For
     **Primary KMS key**, choose an existing AWS KMS
     key, or choose **Create a new KMS key** to create a new
     KMS key in the AWS Key Management Service (AWS KMS) console.

   For more information about DSSE-KMS, see [Using
   dual-layer server-side encryption with AWS KMS keys](../../../AmazonS3/latest/userguide/UsingDSSEncryption.md "../../../AmazonS3/latest/userguide/UsingDSSEncryption.md") in the
   _Amazon Simple Storage Service User Guide_.

   ###### Note

   There are additional charges for using DSSE-KMS and AWS KMS keys.
   For more information, see [AWS KMS
   pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

   To specify an AWS KMS key with an alias that is not listed or to use
   an AWS KMS key from a different AWS account, you must use the
   AWS Command Line Interface. Asymmetric KMS keys are not supported. For more
   information, see [CreateSMBFileShare](../../../storagegateway/latest/APIReference/API_CreateSMBFileShare.md "../../../storagegateway/latest/APIReference/API_CreateSMBFileShare.md") in the _AWS Storage Gateway API
   Reference_.

5. Choose **Save changes** when finished.
