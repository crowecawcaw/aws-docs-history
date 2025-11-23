# Key management in AWS IoT SiteWise

## AWS IoT SiteWise cloud key management

By default, AWS IoT SiteWise uses AWS managed keys to protect your data in
the AWS Cloud. You can update your settings to use a customer managed key to encrypt some
data in AWS IoT SiteWise. You can create, manage, and view your encryption key through AWS Key Management Service
(AWS KMS).

AWS IoT SiteWise supports server-side encryption with customer managed keys stored in AWS KMS to
encrypt the following data:

- Asset property values
- Aggregate values

###### Note

Other data and resources are encrypted using the default encryption with keys managed
by AWS IoT SiteWise. This key is stored in the
AWS IoT SiteWise
account.

For more information, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the
_AWS Key Management Service Developer Guide_.

### Enable encryption using customer managed keys

To
use
customer managed keys with AWS IoT SiteWise, you need to update your AWS IoT SiteWise
settings.

###### To enable encryption using KMS keys

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com//iotsitewise/ "https://console.aws.amazon.com//iotsitewise/").
2. Choose
   **Account
   Settings** and choose **Edit** to open
   the **Edit account settings** page.
3. For **Encryption key type**, choose **Choose a different
   AWS KMS key**. This enables encryption with customer managed keys stored in
   AWS KMS.

###### Note

Currently, you can only use customer managed key encryption for asset property
values and aggregate values. 4. Choose your KMS key with one of the following options:

    * **To use an existing KMS key** – Choose your KMS key
     alias from the list.
    * **To create a new KMS key** – Choose
     **Create an AWS KMS key**.


    ###### Note

    This opens the AWS KMS
     dashboard.
     For more information about creating a KMS key, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
     *AWS Key Management Service Developer Guide*.

5. Choose **Save** to update your settings.

## SiteWise Edge gateway key management

SiteWise Edge gateways run on AWS IoT Greengrass, and AWS IoT Greengrass core devices use public and private keys to
authenticate with the AWS Cloud and encrypt local secrets, such as OPC UA authentication
secrets. For more information, see [Key
management](../../../greengrass/v1/developerguide/key-management.md "../../../greengrass/v1/developerguide/key-management.md") in the _AWS IoT Greengrass Version 1 Developer Guide_.
