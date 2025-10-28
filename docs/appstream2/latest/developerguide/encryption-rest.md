# Encryption at Rest

AppStream 2.0 fleet instances are ephemeral in nature. After a user's streaming session is
finished, the underlying instance and its associated Amazon Elastic Block Store (Amazon EBS) volume are terminated.
In addition, AppStream 2.0 periodically recycles unused instances for freshness.

When you enable [application settings
persistence](how-it-works-app-settings-persistence.md "how-it-works-app-settings-persistence.md"), [home folders](home-folders-admin.md "home-folders-admin.md"), [session scripts](enable-S3-bucket-storage-session-script-logs.md "enable-S3-bucket-storage-session-script-logs.md"), or [usage reports](enable-usage-reports.md "enable-usage-reports.md") your users, the data that is generated
by your users and stored in Amazon Simple Storage Service buckets is encrypted at rest. AWS Key Management Service is a service that
combines secure, highly available hardware and software to provide a key management system
scaled for the cloud. Amazon S3 uses [AWS Managed
CMKs](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") to encrypt your Amazon S3 object data.
