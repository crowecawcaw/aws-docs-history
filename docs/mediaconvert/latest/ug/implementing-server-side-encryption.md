# Implementing server-side

encryption

Server-side encryption with Amazon S3 is one of the encryption options that you can use with
AWS Elemental MediaConvert.

You can protect your input and output files at rest by using server-side encryption with
Amazon S3:

- To protect your input files, set up server-side encryption as you would for any object
  in an Amazon S3 bucket. For more information, see [Protecting data using server-side
  encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the _Amazon Simple Storage Service User Guide_.
- To protect your output files, specify in your AWS Elemental MediaConvert job that Amazon S3 encrypts
  your output files as MediaConvert uploads them. By default, your output files are not
  encrypted. The rest of this topic provides more information about setting up your job to
  encrypt your output files.
  When you set up an AWS Elemental MediaConvert job output for server-side encryption, Amazon S3 encrypts
  it with a data key. As an additional security measure, the data key itself is encrypted with a
  master key.

You choose whether Amazon S3 encrypts the data key by using the default Amazon S3 managed key or a KMS
key that is managed by AWS Key Management Service (AWS KMS). Using the default Amazon S3 master key is simplest to set
up. If you prefer more control over your key, use an AWS KMSkey. For more information about the
different types of KMS keys managed with AWS KMS, see [What is AWS Key Management Service?](../../../kms/latest/developerguide.md#master_keys "../../../kms/latest/developerguide.md#master_keys") in the _AWS Key Management Service Developer Guide_.

If you choose to use an AWS KMS key, you can specify a customer managed key in your AWS
account. Otherwise, AWS KMS uses the AWS managed key for Amazon S3, which has the alias
`aws/s3`.

###### To set up your job outputs for server-side encryption

1.  Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert "https://console.aws.amazon.com/mediaconvert").
2.  Choose **Create job**.
3.  Set up your input, output groups, and outputs for video and audio, as described in
    [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md") and [Creating outputs](output-settings.md "output-settings.md").
4.  For each output group that has outputs that you want encrypted, set up server-side
    encryption:
    1. In the **Job** pane on the left, choose the output group.
    2. In the group settings section on the right, choose **Server-side
       encryption**. If you use the API or an SDK, you can find this setting in the JSON file of your job. The setting name is `S3EncryptionSettings`.
    3. For **Encryption key management**, choose the AWS service that
       protects your data key. If you use the API or an SDK, you can find this setting in the JSON file of your job. The setting name is
       `S3ServerSideEncryptionType`.

    If you choose **Amazon S3**, Amazon S3 encrypts your data key with a
    customer managed key that Amazon S3 stores securely. If you choose
    **AWS KMS**, Amazon S3 encrypts your data key with a KMS key that
    AWS Key Management Service (AWS KMS) stores and manages. 4. If you chose **AWS KMS** in the preceding step, optionally specify
    the ARN of one of your [What is
    AWS Key Management Service?](../../../kms/latest/developerguide/concept.md#customer-cmk "../../../kms/latest/developerguide/concept.md#customer-cmk"). If you do, AWS KMS will use that KMS key to encrypt the data key
    that Amazon S3 uses to encrypt your media files.

    If you don't specify a key for **AWS KMS**, Amazon S3 uses the [AWS managed key](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") in your
    AWS account that is used exclusively for Amazon S3. 5. If you chose **AWS KMS** for **Encryption key
    management**, grant `kms:Encrypt` and
    `kms:GenerateDataKey` permissions to your AWS Elemental MediaConvert AWS Identity and Access Management
    (IAM) role. This allows MediaConvert to encrypt your output files. If you also want
    to be able to use these outputs as inputs to another MediaConvert job, also grant
    `kms:Decrypt` permissions. To learn more, see these topics:

        * For more information about setting up an IAM role for AWS Elemental MediaConvert to
         assume, see [Setting up IAM permissions](iam-role.md "iam-role.md")  in the Getting
         Started chapter of this guide.
        * For more information about granting IAM permissions using an inline policy,
         see the procedure **To embed an inline policy for a user or
         role** in [Adding IAM identity permissions (Console)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") in the *IAM User Guide*.
        * For examples of IAM policies that grant AWS KMS permissions, including
         decrypting encrypted content, see [Customer managed
         policy examples](../../../kms/latest/developerguide/iam-policies.md#customer-managed-policies "../../../kms/latest/developerguide/iam-policies.md#customer-managed-policies") in the *AWS Key Management Service Developer Guide*.

5.  Run your AWS Elemental MediaConvert job as usual. If you chose **AWS KMS** for
    **Encryption key management**, remember to grant
    `kms:Decrypt` permissions to any user or role that you want to be able to
    access your outputs.
