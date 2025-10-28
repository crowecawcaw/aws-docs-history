# Set up Amazon S3 as the configuration source

When you set up _Customizations for AWS Control Tower_, it stores an initial
configuration file, called `_custom-control-tower-configuration.zip` file in an
Amazon Simple Storage Service (Amazon S3) bucket, named `custom-control-tower-configuration-`account-ID`-`region``.

###### Note

If you choose to download and modify this file, remember to zip the changes, save as a new file
named `custom-control-tower-configuration.zip`, and then upload it back to
the same Amazon S3 bucket.

The Amazon S3 bucket is the default source of the pipeline. When default settings are in place, uploading a configuration zip file without the underscore prefix in the file name to the S3 bucket will initiate the pipeline automatically.

The zip file is protected by [Server-Side Encryption](../../../AmazonS3/latest/dev/UsingKMSEncryption.md "../../../AmazonS3/latest/dev/UsingKMSEncryption.md") (SSE) with AWS Key Management Service (AWS KMS), and [denial of use](../../../kms/latest/developerguide/determining-access.md "../../../kms/latest/developerguide/determining-access.md") of the KMS key. For access to the zip file, you must update the KMS Key Policy to specify the role(s) that should be granted access. The role may be an administrator role, a user, or both. Follow this procedure:

1. Navigate to the [AWS Key Management Service console](https://console.aws.amazon.com/kms/home "https://console.aws.amazon.com/kms/home").
2. In **Customer Managed Keys**, select **CustomControlTowerKMSKey**.
3. Select the **Key policy** tab. Then, select **Edit**.
4. In the **Edit key policy** page, find the **Allow Use of the key** section in the code, and add one of the following permissions:
   - To add an administration role:

   `arn:aws:iam::`<account-ID>`:role/`<administrator-role>``
   - To add a user::

   `arn:aws:iam::`<account-ID>`:user/`<username>``

5. Select **Save Changes**.
6. Navigate to the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home"), find
   the S3 bucket containing the configuration zip file, and select download.
7. Make the necessary configuration changes to the manifest file and template files. For information about customizing the manifest and template files, see [CfCT customization guide](cfct-customizations-dev-guide.md "cfct-customizations-dev-guide.md").
8. Upload your changes:
   1. Zip the modified configuration files, and name the file: `custom-control-tower-configuration.zip`.
   2. Upload the file to Amazon S3 using SSE with the AWS KMS master-key: `CustomControlTowerKMSKey`.
