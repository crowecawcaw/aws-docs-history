# Data encryption in Amazon Personalize

The following information explains where Amazon Personalize uses
data encryption to protect your data.

## Encryption at

rest

Any data stored within Amazon Personalize is always encrypted at rest with
Amazon Personalize managed AWS Key Management Service (AWS KMS) keys. If you provide your own
AWS KMS key during resource creation, Amazon Personalize uses the key to
encrypt your data and store it. For example, if you provide a
AWS KMS ARN in the [CreateDatasetGroup](API_CreateDatasetGroup.md "API_CreateDatasetGroup.md") operation, Amazon Personalize
uses the key to encrypt and store data you import into any
datasets that you create in that dataset group.

You must grant Amazon Personalize and your Amazon Personalize IAM service role
permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").

For information about data encryption in Amazon S3 see [Protecting data using encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") in the _Amazon Simple Storage Service User Guide_. For information
about managing your own AWS KMS key, see [Managing
keys](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service Developer Guide_.

## Encryption in

transit

Amazon Personalize uses TLS with AWS certificates to encrypt
any data sent to other AWS services. Any communication with
other AWS services happens over HTTPS, and Amazon Personalize endpoints
support only secure connections over HTTPS.

Amazon Personalize copies data out of your account and processes it in an
internal AWS system. When processing data, Amazon Personalize encrypts
data with either a Amazon Personalize AWS KMS key or any AWS KMS key you
provide.

## Key management

AWS manages any default AWS KMS keys. It is your
responsibility to manage any AWS KMS keys that you own. You must grant Amazon Personalize and your Amazon Personalize IAM service role
permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").

For
information about managing your own AWS KMS key, see [Managing
keys](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service Developer Guide_.
