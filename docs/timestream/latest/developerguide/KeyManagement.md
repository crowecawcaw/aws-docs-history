For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Key management

You can manage keys for Amazon Timestream Live Analytics using the [AWS Key Management Service (AWS KMS)](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").
**Timestream Live Analytics requires the use of KMS to encrypt your data.**
You have the following options for key management, depending on how much control you require over your keys:

###### Database and table resources

- _Timestream Live Analytics-managed key:_
  If you do not provide a key, Timestream Live Analytics will create a `alias/aws/timestream` key using KMS.
- _Customer managed key:_
  KMS customer managed keys are supported.
  Choose this option if you require more control over the permissions and lifecycle of your keys, including the ability to have them automatically rotated on an annual basis.

###### Scheduled query resource

- _Timestream Live Analytics-owned key:_
  If you do not provide a key, Timestream Live Analytics will use its own a KMS key to encrypt the Query resource, this key is present in timestream account.
  See [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the KMS developer guide for more details.
- _Customer managed key:_
  KMS customer managed keys are supported.
  Choose this option if you require more control over the permissions and lifecycle of your keys, including the ability to have them automatically rotated on an annual basis.
  KMS keys in an external key store (XKS) are not supported.
