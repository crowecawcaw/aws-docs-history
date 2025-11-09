# Monitor KMS keys with Amazon CloudWatch

You can monitor your AWS KMS keys using [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md"), an
AWS service that collects and processes raw data from AWS KMS into readable, near real-time
metrics. These data are recorded for a period of two weeks so that you can access historical
information and gain a better understanding of the usage of your KMS keys and their changes
over time.

You can use Amazon CloudWatch to alert you to important events, such as the following ones.

- The imported key material in a KMS key is nearing its expiration date.
- A KMS key that is pending deletion is still being used.
- The key material in a KMS key was automatically rotated.
- A KMS key was deleted.
  You can also create an [Amazon CloudWatch](../../../AmazonCloudWatch/latest/DeveloperGuide.md "../../../AmazonCloudWatch/latest/DeveloperGuide.md") alarm that alerts you when
  your request rate reaches a certain percentage of a quota value. For details, see [Manage your AWS KMS API request rates using Service Quotas and Amazon CloudWatch](https://aws.amazon.com/blogs/security/manage-your-aws-kms-api-request-rates-using-service-quotas-and-amazon-cloudwatch/ "https://aws.amazon.com/blogs/security/manage-your-aws-kms-api-request-rates-using-service-quotas-and-amazon-cloudwatch/") in
  the _AWS Security Blog_.

## AWS KMS metrics and dimensions

AWS KMS predefines Amazon CloudWatch metrics to make it easier for you to monitor critical data and
create alarms. You can view the AWS KMS metrics using the AWS Management Console and the Amazon CloudWatch API.

This section lists each AWS KMS metrics and the dimensions for each metric, and provides
some basic guidance for creating CloudWatch alarms based on these metrics and dimensions.

###### Note

**Dimension group name**:

To view a metric in the Amazon CloudWatch console, in the **Metrics** section,
select the dimension group name. Then you can filter by the **Metric
name**. This topic includes the metric name and dimension group name for each AWS KMS
metric.

You can view AWS KMS metrics using the AWS Management Console and the Amazon CloudWatch API. For more
information, see [View available
metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md") in the _Amazon CloudWatch User Guide_.

###### Topics

- [SuccessfulRequest](#key-level-api-usage-metric "#key-level-api-usage-metric")
- [SecondsUntilKeyMaterialExpiration](#key-material-expiration-metric "#key-material-expiration-metric")
- [CloudHSMKeyStoreThrottle](#metric-throttling-cloudhsm "#metric-throttling-cloudhsm")
- [ExternalKeyStoreThrottle](#metric-throttling "#metric-throttling")
- [XksProxyCertificateDaysToExpire](#metric-xks-proxy-certificate-days-to-expire "#metric-xks-proxy-certificate-days-to-expire")
- [XksProxyCredentialAge](#metric-xks-proxy-credential-age "#metric-xks-proxy-credential-age")
- [XksProxyErrors](#metric-xks-proxy-errors "#metric-xks-proxy-errors")
- [XksExternalKeyManagerStates](#metric-xks-ekm-states "#metric-xks-ekm-states")
- [XksProxyLatency](#metric-xks-proxy-latency "#metric-xks-proxy-latency")

### SuccessfulRequest

The number of successful requests for cryptographic operations on a specific KMS key. By using
the `SuccessfulRequest` metric, you can apply key-level filtering to AWS KMS API
usage in CloudWatch. The `Sum` statistic for this metric defines the total number of
successful requests during the period.

Use this metric to identify which KMS keys consume the largest portion of your
request quota or contribute the most to API charges. You can also create a CloudWatch alarm
based on the `SuccesfulRequest` metric to notify you of anomalous AWS KMS
API usage patterns. These alerts can help identify inefficient workflows that might unintentionally
exceed your request quotas or incur unexpected charges.

**Dimensions for `SuccessfulRequest`**

| Dimension | Description                                                                                 |
| --------- | ------------------------------------------------------------------------------------------- |
| KeyArn    | Value for each KMS key.                                                                     |
| Operation | Value for each AWS KMS API operation. This metric applies only to cryptographic operations. |

For [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md") operations, the
`SuccessfulRequest` metric includes dimensions for both the source and
destination KMS keys.

| Dimension         | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| SourceKeyArn      | Value for the KMS key that decrypted the ciphertext.           |
| DestinationKeyArn | Value for the KMS key that re-encrypted the data.              |
| Operation         | Value for each AWS KMS API operation, in this case, ReEncrypt. |

### SecondsUntilKeyMaterialExpiration

The number of seconds remaining until the earliest-expiring [imported key
material](importing-keys.md "importing-keys.md") in a KMS key. This metric is valid only for KMS keys with imported key material (a
[key material origin](create-keys.md#key-origin "create-keys.md#key-origin") of `EXTERNAL`) and an expiration date.

Use this metric to track how much time is left before your earliest-expiring imported key material expires.
When that time falls below a threshold that you define, you should reimport the key material with a new
expiration date to keep the KMS key usable. The `SecondsUntilKeyMaterialExpiration`
metric is specific to a KMS key. You cannot use this metric to monitor multiple KMS keys
or KMS keys that you might create in the future. For help with creating a CloudWatch alarm to
monitor this metric, see [Create a CloudWatch alarm for expiration of
imported key material](imported-key-material-expiration-alarm.md "imported-key-material-expiration-alarm.md").

The most useful statistic for this metric is `Minimum`, which tells you the
smallest amount of time remaining for all data points in the specified statistical period.
The only valid unit for this metric is `Seconds`.

**Dimension group name**: **Per-Key
Metrics**

| Dimensions for `SecondsUntilKeyMaterialExpiration` | Dimension               | Description; related to AWS |
| -------------------------------------------------- | ----------------------- | --------------------------- |
| KeyId                                              | Value for each KMS key. |

When you [schedule deletion](deleting-keys.md "deleting-keys.md") of a KMS key, AWS KMS
enforces a waiting period before deleting the KMS key. You can use the waiting period to
ensure that you don't need the KMS key now or in the future. You can also configure a CloudWatch
alarm to warn you if a person or application attempts to use the KMS key in a [cryptographic operation](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations") during the waiting
period. If you receive a notification from such an alarm, you might want to cancel deletion
of the KMS key.

For instructions, see [Create an alarm that detects use of a
KMS key pending deletion](deleting-keys-creating-cloudwatch-alarm.md "deleting-keys-creating-cloudwatch-alarm.md").

### CloudHSMKeyStoreThrottle

The number of requests for cryptographic operations on KMS keys in each AWS CloudHSM key
store that AWS KMS throttles (responds with a `ThrottlingException`). This metric
applies only to AWS CloudHSM key stores.

The `CloudHSMKeyStoreThrottle` metric applies only to KMS keys in an AWS CloudHSM
key store and only to requests for [cryptographic
operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations"). AWS KMS [throttles these requests](throttling.md "throttling.md") when
the request rate exceeds the [custom key store request quota](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores") for your AWS CloudHSM key store. This metric also includes throttling by the AWS CloudHSM cluster.

**Dimension group name**: **Keystore Throttle
Metrics**

| Dimension        | Description                                                                                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CustomKeyStoreId | Value for each AWS CloudHSM key store.                                                                                                                                              |
| KmsOperation     | Value for each AWS KMS API operation. This metric applies only to cryptographic<br>operations on KMS keys in an AWS CloudHSM<br>key store.                                          |
| KeySpec          | Value for each type of KMS key. The only supported [key spec](create-keys.md#key-spec "create-keys.md#key-spec") for KMS keys in an AWS CloudHSM key store is<br>SYMMETRIC_DEFAULT. |

### ExternalKeyStoreThrottle

The number of requests for cryptographic operations on KMS keys in each external key
store that AWS KMS throttles (responds with a `ThrottlingException`). This metric applies only to [external key stores](keystore-external.md "keystore-external.md").

The `ExternalKeyStoreThrottle` metric applies only to KMS keys in an
external key store and only to requests for [cryptographic operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations"). AWS KMS [throttles these
requests](throttling.md "throttling.md") when the request rate exceeds the [custom
key store request quota](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores") for your external key store. This metric does not include
throttling by your external key store proxy or external key manager.

Use this metric to review and adjust the value of your custom key store request quota.
If this metric indicates that AWS KMS is frequently throttling your requests for these
KMS keys, you might consider requesting an increase in your custom key store request quota
value. For help, see [Requesting a
quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

If you are getting very frequent `KMSInvalidStateException` errors with a
message that explains that the request was rejected "due to a very high request rate" or the
request was rejected "because the external key store proxy did not respond in time," it
might indicate that your external key manager or external key store proxy cannot keep pace
with the current request rate. If possible, lower your request rate. You might also consider
requesting a decrease in your custom key store request quota value. Decreasing this quota
value might increase throttling (and the `ExternalKeyStoreThrottle` metric
value), but it indicates that AWS KMS is rejecting excess requests quickly before they are
sent to your external key store proxy or external key manager. To request a quota decrease,
please visit the [AWS Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") and
create a case.

**Dimension group name**: **Keystore Throttle
Metrics**

| Dimension        | Description                                                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CustomKeyStoreId | Value for each external key store.                                                                                                                                              |
| KmsOperation     | Value for each AWS KMS API operation. This metric applies only to cryptographic<br>operations on KMS keys in an external<br>key store.                                          |
| KeySpec          | Value for each type of KMS key. The only supported [key spec](create-keys.md#key-spec "create-keys.md#key-spec") for KMS keys in an external key store is<br>SYMMETRIC_DEFAULT. |

### XksProxyCertificateDaysToExpire

The number of days until the TLS certificate for your [external key store proxy endpoint](create-xks-keystore.md#require-endpoint "create-xks-keystore.md#require-endpoint") (`XksProxyUriEndpoint`) expires.
This metric applies only to [external key stores](keystore-external.md "keystore-external.md").

Use this metric to create a CloudWatch alarm that notifies you about the upcoming expiration
of your TLS certificate. When the certificate expires, AWS KMS cannot communicate with the
external key store proxy. All data protected by KMS keys in your external key store
becomes inaccessible until you renew the certificate.

A certificate alarm prevents certificate expiration that might prevent you from
accessing your encrypted resources. Set the alarm to give your organization time to renew
the certificate before it expires.

**Dimension group name**: **XKS Proxy Certificate
Metrics**

| Dimension        | Description                               |
| ---------------- | ----------------------------------------- |
| CustomKeyStoreId | Value for each external key store.        |
| CertificateName  | Subject name (CN) in the TLS certificate. |

You can create CloudWatch alarms based on the metrics for external key stores and KMS keys
in external key stores. For instructions, see [Monitor external key stores](xks-monitoring.md "xks-monitoring.md").

### XksProxyCredentialAge

The number of days since the current external key store [proxy authentication credential](keystore-external.md#concept-xks-credential "keystore-external.md#concept-xks-credential")
(`XksProxyAuthenticationCredential`) was associated with the external key
store. This count begins when you enter the authentication credential as part of creating or
updating your external key store. This metric applies only to [external key stores](keystore-external.md "keystore-external.md").

This value is designed to remind you about the age of your authentication credential.
However, because we begin the count when you associate the credential with your external key
store, not when you create your authentication credential on your external key store proxy,
this might not be an accurate indicator of the credential age on the proxy.

Use this metric to create a CloudWatch alarm that reminds you to rotate your external key
store proxy authentication credential.

**Dimension group name**: **Per-Keystore
Metrics**

| Dimension        | Description                        |
| ---------------- | ---------------------------------- |
| CustomKeyStoreId | Value for each external key store. |

You can create CloudWatch alarms based on the metrics for external key stores and KMS keys
in external key stores. For instructions, see [Monitor external key stores](xks-monitoring.md "xks-monitoring.md").

### XksProxyErrors

The number of exceptions related to AWS KMS requests to your [external key store proxy](keystore-external.md#concept-xks-proxy "keystore-external.md#concept-xks-proxy"). This count includes
exceptions that the external key store proxy returns to AWS KMS and timeout errors that occur
when the external key store proxy does not respond to AWS KMS within the 250 millisecond
timeout interval. This metric applies only to [external key stores](keystore-external.md "keystore-external.md").

Use this metric to track the error rate of KMS keys in your external key store. It
reveals the most frequent errors, so you can prioritize your engineering effort. For
example, KMS keys that are generating high rates of non-retryable errors might indicate a
problem with the configuration of your external key store. To view your external key store
configuration, see [View external key stores](view-xks-keystore.md "view-xks-keystore.md"). To
edit your external key store settings, see [Edit external key store properties](update-xks-keystore.md "update-xks-keystore.md").

**Dimension group name**: **XKS Proxy Error
Metrics**

| Dimension        | Description                                                                                                                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CustomKeyStoreId | Value for each external key store.                                                                                                                                                                                                                      |
| KmsOperation     | Value for each AWS KMS API operation that generated a request to the XKS<br>proxy.                                                                                                                                                                      |
| XksOperation     | Value for each [external key store proxy API<br>operation](keystore-external.md#concept-proxy-apis "keystore-external.md#concept-proxy-apis").                                                                                                          |
| KeySpec          | Value for each type of KMS key. The only supported [key spec](create-keys.md#key-spec "create-keys.md#key-spec") for KMS keys in an external key store is<br>SYMMETRIC_DEFAULT.                                                                         |
| ErrorType        | Values:<br>• Retryable errors: Likely to be transient, such as networking<br>errors.<br>• Non-retryable errors: Likely to indicate a problem with the custom key<br>store configuration or external components.<br>• N/A: Successful request; no errors |
| ExceptionName    | Values:<br>• Name of the exception<br>• None: Successful request; no errors                                                                                                                                                                             |

You can create CloudWatch alarms based on the metrics for external key stores and KMS keys
in external key stores. For instructions, see [Monitor external key stores](xks-monitoring.md "xks-monitoring.md").

### XksExternalKeyManagerStates

A count of the number of [external key manager
instances](keystore-external.md#concept-ekm "keystore-external.md#concept-ekm") in each of the following health states: `Active`,
`Degraded`, and `Unavailable`. The information for this metric comes
from the external key store proxy associated with each external key
store. This metric applies only to [external key stores](keystore-external.md "keystore-external.md").

The following are the health states for the external key manager instances associated
with an external key store. Each external key store proxy might use different indicators to
measure the health states of your external key manager. For details, see the documentation
for your external key store proxy.

- `Active`: The external key manager is healthy.
- `Degraded`: The external key manager is unhealthy, but can still serve
  traffic
- `Unavailable`: The external key manager cannot serve traffic.

Use this metric to create a CloudWatch alarm that alerts you to degraded and unavailable
external key manager instances. To determine which external key manager instances are in
each state, consult your external key store proxy logs.

**Dimension group name**: **XKS External Key
Manager Metrics**

| Dimension                  | Description                        |
| -------------------------- | ---------------------------------- |
| CustomKeyStoreId           | Value for each external key store. |
| XksExternalKeyManagerState | Value for each health state.       |

You can create CloudWatch alarms based on the metrics for external key stores and KMS keys
in external key stores. For instructions, see [Monitor external key stores](xks-monitoring.md "xks-monitoring.md").

### XksProxyLatency

The number of milliseconds it takes for an external key store proxy to respond to an
AWS KMS request. If the request timed out, the recorded value is the 250 millisecond timeout
limit. This metric applies only to [external key stores](keystore-external.md "keystore-external.md").

Use this metric to evaluate the performance of your external key store proxy and
external key manager. For example, if the proxy is frequently timing out on encryption and
decryption operations, consult your external proxy administrator.

Slow responses might also indicate that your external key manager cannot handle the
current request traffic. AWS KMS recommends that your external key manager be able to handle
up to 1800 requests for cryptographic operations per second. If your external key manager
cannot handle the 1800 requests per second rate, consider requesting a decrease in your
[request quota for KMS keys in a custom key store](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores").
Requests for cryptographic operations using the KMS keys in your external key store will
fail fast with a [throttling exception](throttling.md "throttling.md"), rather than being
processed and later rejected by your external key store proxy or external key
manager.

**Dimension group name**: **XKS Proxy Latency
Metrics**

| Dimension        | Description                                                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CustomKeyStoreId | Value for each external key store.                                                                                                                                              |
| KmsOperation     | Value for each AWS KMS API operation that generated a request to the XKS<br>proxy.                                                                                              |
| XksOperation     | Value for each [external key store proxy API<br>operation](keystore-external.md#concept-proxy-apis "keystore-external.md#concept-proxy-apis").                                  |
| KeySpec          | Value for each type of KMS key. The only supported [key spec](create-keys.md#key-spec "create-keys.md#key-spec") for KMS keys in an external key store is<br>SYMMETRIC_DEFAULT. |

You can create CloudWatch alarms based on the metrics for external key stores and KMS keys
in external key stores. For instructions, see [Monitor external key stores](xks-monitoring.md "xks-monitoring.md").
