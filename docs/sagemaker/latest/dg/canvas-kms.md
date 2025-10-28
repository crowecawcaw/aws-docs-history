# Encrypt Your SageMaker Canvas Data with AWS KMS

You might have data that you want to encrypt while using Amazon SageMaker Canvas, such as your private
company information or customer data. SageMaker Canvas uses AWS Key Management Service to protect your data. AWS KMS is a
service that you can use to create and manage cryptographic keys for encrypting your data. For
more information about AWS KMS, see [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS KMS Developer Guide_.

Amazon SageMaker Canvas provides you with several options for encrypting your data. SageMaker Canvas provides
default encryption within the application for tasks such as building your model and generating
insights. You can also choose to encrypt data stored in Amazon S3 to protect your data at rest.
SageMaker Canvas supports importing encrypted datasets, so you can establish an encrypted workflow. The
following sections describe how you can use AWS KMS encryption to protect your data while
building models with SageMaker Canvas.

## Encrypt your data in SageMaker Canvas

With SageMaker Canvas, you can use two different AWS KMS encryption keys to encrypt your data in
SageMaker Canvas, which you can specify when [setting up your domain](gs-studio-onboard.md "gs-studio-onboard.md") using
the standard domain setup. These keys are specified in the following domain setup
steps:

- **Step 3: Configure Applications - (Optional)** – When
  configuring the **Canvas storage configuration** section, you can
  specify an **Encryption key**. This is a KMS key that SageMaker Canvas uses for
  long-term storage of model objects and datasets, which are stored in the provided Amazon S3
  bucket for your domain. If creating a Canvas application with the [CreateApp](../APIReference/API_CreateApp.md "../APIReference/API_CreateApp.md") API, use the `S3KMSKeyId` field to specify this
  key.
- **Step 6: Configure storage** – SageMaker Canvas uses one key for
  encrypting the Amazon SageMaker Studio private space that is created for your Canvas
  application, which includes temporary application storage, visualizations, and compute
  jobs (such as building models). You can use either the default AWS managed key or
  specify your own. If you specify your AWS KMS key, the data stored in the `/home/sagemaker-user` directory is encrypted with your key.
  If you don't specify an AWS KMS key, the data inside `/home/sagemaker-user` is encrypted with an AWS managed key. Regardless of whether you specify an AWS KMS key, all of the data outside of the working directory is encrypted with an AWS Managed Key.
  To learn more about the Studio space and your Canvas
  application storage, see [Store SageMaker Canvas application data in your own SageMaker AI
  space](canvas-spaces-setup.md "canvas-spaces-setup.md"). If creating a Canvas application with the
  [CreateApp](../APIReference/API_CreateApp.md "../APIReference/API_CreateApp.md") API, use the `KmsKeyID` field to specify this
  key.

The preceding keys can be the same or different KMS keys.

### Prerequisites

To use your own KMS key for either of the previously described purposes, you must
first grant your user's IAM role permission to use the key. Then, you can specify the
KMS key when setting up your domain.

The simplest way to grant your role permission to use the key is to modify the key
policy. Use the following procedure to grant your role the necessary permissions.

1. Open the [AWS KMS console](https://console.aws.amazon.com/kms/ "https://console.aws.amazon.com/kms/").
2. In the **Key Policy** section, choose **Switch to policy
   view**.
3. Modify the key's policy to grant permissions for the
   `kms:GenerateDataKey` and `kms:Decrypt` actions to the IAM
   role. Additionally, if you're modifying the key policy that encrypts your Canvas
   application storage in the Studio space, grant the `kms:CreateGrant`
   action. You can add a statement that's similar to the following:

```
{
  "Sid": "ExampleStmt",
  "Action": [
    "kms:CreateGrant", #this permission is only required for the key that encrypts your SageMaker Canvas application storage
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Effect": "Allow",
  "Principal": {
    "AWS": "`<arn:aws:iam::111122223333:role/Jane>`"
  },
  "Resource": "*"
}
```

4. Choose **Save changes**.

The less preferred method is to modify the user’s IAM role to grant the user
permissions to use or manage the KMS key. If you use this method, the KMS key policy
must also allow access management through IAM. To learn how to grant permission to a
KMS key through the user’s IAM role, see [Specifying KMS keys in IAM
policy statements](../../../kms/latest/developerguide/cmks-in-iam-policies.md "../../../kms/latest/developerguide/cmks-in-iam-policies.md") in the _AWS KMS Developer
Guide_.

### Encrypt your data in the SageMaker Canvas

application

The first KMS key you can use in SageMaker Canvas is used for encrypting application data
stored on Amazon Elastic Block Store (Amazon EBS) volumes and in the Amazon Elastic File System that SageMaker AI creates in your
domain. SageMaker Canvas encrypts your data with this key in the underlying application and
temporary storage systems created when using compute instances for building models and
generating insights. SageMaker Canvas passes the key to other AWS services, such as Autopilot,
whenever SageMaker Canvas initiates jobs with them to process your data.

You can specify this key by setting the `KmsKeyID` in the
`CreateDomain` API call or while doing the standard domain setup in the
console. If you don’t specify your own KMS key, SageMaker AI uses a default AWS managed
KMS key to encrypt your data in the SageMaker Canvas application.

To specify your own KMS key for use in the SageMaker Canvas application through the console,
first set up your Amazon SageMaker AI domain using the **Standard setup**. Use the
following procedure to complete the **Network and Storage Section** for
the domain.

1. Fill out your desired Amazon VPC settings.
2. For **Encryption key**, choose **Enter a KMS key
   ARN**.
3. For **KMS ARN**, enter the ARN for your KMS key, which should
   have a format similar to the following:
   `arn:aws:kms:example-region-1:123456789098:key/111aa2bb-333c-4d44-5555-a111bb2c33dd`

### Encrypt your SageMaker Canvas data saved in

Amazon S3

The second KMS key you can specify is used for data that SageMaker Canvas stores to Amazon S3. This
KMS key is specified in the `S3KMSKeyId` field in the
`CreateDomain` API call, or while doing the standard domain setup in the
SageMaker AI console. SageMaker Canvas saves duplicates of your input datasets, application and model data,
and output data to the Region’s default SageMaker AI S3 bucket for your account. The naming
pattern for this bucket is
`s3://sagemaker-`{Region}`-`{your-account-id}``,
 and SageMaker Canvas stores data in the `Canvas/` folder.

1. Turn on **Enable notebook resource sharing**.
2. For **S3 location for shareable notebook resources**, leave the
   default Amazon S3 path. Note that SageMaker Canvas does not use this Amazon S3 path; this Amazon S3 path is used
   for Studio Classic notebooks.
3. For **Encryption key**, choose **Enter a KMS key
   ARN**.
4. For **KMS ARN**, enter the ARN for your KMS key, which should
   have a format similar to the following:
   `arn:aws:kms:us-east-1:111122223333:key/111aa2bb-333c-4d44-5555-a111bb2c33dd`

## Import encrypted datasets from Amazon S3

Your users might have datasets that have been encrypted with a KMS key. While the
preceding section shows you how to encrypt data in SageMaker Canvas and data stored to Amazon S3, you must
grant your user's IAM role additional permissions if you want to import data from Amazon S3
that is already encrypted with AWS KMS.

To grant your user permissions to import encrypted datasets from Amazon S3 into SageMaker Canvas, add
the following permissions to the IAM execution role that you've used for the user
profile.

```

      "kms:Decrypt",
      "kms:GenerateDataKey"

```

To learn how to edit the IAM permissions for a role, see [Adding and removing
IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_. For more information about KMS keys, see [Key policies in
AWS Key Management Service](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS KMS Developer Guide_.

## FAQs

Refer to the following FAQ items for answers to commonly asked questions about SageMaker Canvas
AWS KMS support.

A: No. SageMaker Canvas may temporarily cache your key or pass it on to other AWS services
(such as Autopilot), but SageMaker Canvas does not retain your KMS key.

A: Your user’s IAM role may not have permissions to use that KMS key. To grant
your user permissions, see the [Prerequisites](#canvas-kms-app-data-prereqs "#canvas-kms-app-data-prereqs"). Another possible error is that you have
a bucket policy on your Amazon S3 bucket that requires the use of a specific KMS key that
doesn’t match the KMS key you specified in your domain. Make sure that you specify
the same KMS key for your Amazon S3 bucket and your domain.

A: The default Amazon S3 bucket follows the naming pattern
`s3://sagemaker-`{Region}`-`{your-account-id}``.
 The `Canvas/` folder in this bucket stores your SageMaker Canvas application
data.

A: No, SageMaker AI creates this bucket for you.

A: SageMaker Canvas uses the default SageMaker AI Amazon S3 bucket to store duplicates of your input
datasets, model artifacts, and model outputs.

A: With SageMaker Canvas, you can use your own encryption keys with AWS KMS for building
regression, binary and multi-class classification, and time series forecasting models,
as well as for batch inference with your model.
