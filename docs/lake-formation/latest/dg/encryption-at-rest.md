# Encryption at Rest

AWS Lake Formation supports data encryption in the following areas:

- Data in your Amazon Simple Storage Service (Amazon S3) data lake.

Lake Formation supports data encryption with [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
(AWS KMS). Data is typically written to the data lake by means of AWS Glue extract, transform, and
load (ETL) jobs. For information about how to encrypt data written by AWS Glue jobs, see [Encrypting
Data Written by Crawlers, Jobs, and Development Endpoints](../../../glue/latest/dg/encryption-security-configuration.md "../../../glue/latest/dg/encryption-security-configuration.md") in the _AWS Glue Developer Guide_.

- The AWS Glue Data Catalog, which is where Lake Formation stores metadata tables that describe data in the data
  lake.

For more information, see [Encrypting Your Data Catalog](../../../glue/latest/dg/encrypt-glue-data-catalog.md "../../../glue/latest/dg/encrypt-glue-data-catalog.md") in
the _AWS Glue Developer Guide_.
To add an Amazon S3 location as storage in your data lake, you _register_ the
location with AWS Lake Formation. You can then use Lake Formation permissions for fine-grained access control to
AWS Glue Data Catalog objects that point to this location, and to the underlying data in the
location.

Lake Formation supports registering an Amazon S3 location that contains encrypted data. For more
information, see [Registering an encrypted Amazon S3 location](register-encrypted.md "register-encrypted.md").
