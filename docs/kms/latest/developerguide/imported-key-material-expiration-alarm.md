# Create a CloudWatch alarm for expiration of

imported key material

You can create a CloudWatch alarm that notifies you when the imported key material in a
KMS key is approaching its expiration time. For example, the alarm can notify you when the
time to expire is less than 30 days away.

When you [import key material into a KMS key](importing-keys.md "importing-keys.md"), you
can optionally specify a date and time when the key material expires. When the key material
expires, AWS KMS deletes the key material and the KMS key becomes unusable. To use the
KMS key again, you must [reimport the key
material](importing-keys-import-key-material.md#reimport-key-material "importing-keys-import-key-material.md#reimport-key-material"). However, if you reimport the key material before it expires, you can
avoid disrupting processes that use that KMS key.

This alarm uses the [SecondsUntilKeyMaterialExpires metric](monitoring-cloudwatch.md#key-material-expiration-metric "monitoring-cloudwatch.md#key-material-expiration-metric") that AWS KMS publishes to
CloudWatch for KMS keys with imported key material that expires. Each alarm uses this metric to
monitor the imported key material for a particular KMS key. You cannot create a single
alarm for all KMS keys with expiring key material or an alarm for KMS keys that you
might create in the future.

**Requirements**

The following resources are required for a CloudWatch alarm that monitors the expiration of
imported key material.

- A KMS key with imported key material that expires.
- An Amazon SNS topic. For details, see [Creating an
  Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") in the _Amazon CloudWatch User Guide_.
  **Create the alarm**

Follow the instructions in [Create a
CloudWatch alarm based on a static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") using the following required values.
For other fields, accept the default values and provide names as requested.

| Field          | Value                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Select metric  | Choose **KMS**, then choose **Per-Key<br>Metrics**.<br>Choose the row with the KMS key and the<br>`SecondsUntilKeyMaterialExpires` metric. Then choose<br>**Select metric**.<br>The \*_Metrics_<br>• list displays the<br>`SecondsUntilKeyMaterialExpires` metric only for KMS keys with<br>imported key material that expires. If you don't have KMS keys with these<br>properties in the account and Region, this list is empty. |
| Statistic      | Minimum                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Period         | 1 minute                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Threshold type | Static                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Whenever ...   | **Whenever**<br>`metric-name` is \*_Greater_<br>• than<br>`1`                                                                                                                                                                                                                                                                                                                                                                      |
