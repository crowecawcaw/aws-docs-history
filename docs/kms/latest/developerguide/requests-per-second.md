

# Request quotas
<a name="requests-per-second"></a>

AWS KMS establishes quotas for the number of API operations requested in each second. The request quotas differ with the API operation, the AWS Region, and other factors, such as the KMS key type. When you exceed an API request quota, AWS KMS [throttles the request](throttling.md).

All AWS KMS request quotas are adjustable, except for the [AWS CloudHSM key store request quota](#rps-key-stores). To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-increase.html) in the *Service Quotas User Guide*. To request a quota decrease, to change a quota that is not listed in Service Quotas, or to change a quota in an AWS Region where Service Quotas for AWS KMS is not available, please visit [AWS Support Center](https://console.aws.amazon.com/support/home) and create a case. 

If you are exceeding the request quota for the [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) operation, consider using the [data key caching](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/data-key-caching.html) feature of the AWS Encryption SDK. Reusing data keys might reduce the frequency of your requests to AWS KMS. 

In addition to request quotas, AWS KMS uses resource quotas to ensure capacity for all users. For details, see [Resource quotas](resource-limits.md).

To view trends in your request rates, use the [Service Quotas console](https://console.aws.amazon.com/servicequotas). You can also create an [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/) alarm that alerts you when your request rate reaches a certain percentage of a quota value. For details, see [Manage your AWS KMS API request rates using Service Quotas and Amazon CloudWatch](https://aws.amazon.com/blogs/security/manage-your-aws-kms-api-request-rates-using-service-quotas-and-amazon-cloudwatch/) in the *AWS Security Blog*.

**Topics**
+ [Request quotas for each AWS KMS API operation](#rps-table)
+ [Applying request quotas](#about-rate-limits)
+ [Shared quotas for cryptographic operations](#rps-shared-limit)
+ [API requests made on your behalf](#rps-from-service)
+ [Cross-account requests](#rps-cross-account)
+ [Custom key store request quotas](#rps-key-stores)

## Request quotas for each AWS KMS API operation
<a name="rps-table"></a>

This table lists the [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/) quota code and the default value for each AWS KMS request quota. All AWS KMS request quotas are adjustable, except for the [AWS CloudHSM key store request quota](#rps-key-stores).

**Note**  
You might need to scroll horizontally or vertically to see all of the data in this table.


| Quota name | Default value (requests per second) | 
| --- | --- | 
| `Cryptographic operations (symmetric) request rate`<br />Applies to:+  `Decrypt` <br />+  `Encrypt` <br />+  `GenerateDataKey` <br />+  `GenerateDataKeyWithoutPlaintext` <br />+  `GenerateMac` <br />+  `GenerateRandom` <br />+  `ReEncrypt` <br />+  `VerifyMac`  | These shared quotas vary with the AWS Region and the type of KMS key used in the request. Each quota is calculated separately.+  10,000 (shared) <br />+  20,000 (shared) in the following Regions:   US East (Ohio), us-east-2   Asia Pacific (Singapore), ap-southeast-1   Asia Pacific (Sydney), ap-southeast-2   Asia Pacific (Tokyo), ap-northeast-1   Europe (Frankfurt), eu-central-1   Europe (London), eu-west-2   <br />+  100,000 (shared) in the following Regions:   US East (N. Virginia), us-east-1   US West (Oregon), us-west-2   Europe (Ireland), eu-west-1    | 
| `Cryptographic operations (RSA) request rate`<br />Applies to:+  `Decrypt` <br />+  `Encrypt` <br />+  `ReEncrypt` <br />+  `Sign` <br />+  `Verify`  | 1,000 (shared) for RSA KMS keys | 
| `Cryptographic operations (ML-DSA) request rate`<br />Applies to:+ `Sign`<br />+ `Verify` | 1,000 (shared) for ML-DSA KMS keys | 
| `Cryptographic operations (ECC and SM2) request rate`<br />Applies to:+  `Decrypt`—only supported for SM2 (China Regions only) KMS keys <br />+  `DeriveSharedSecret` <br />+  `Encrypt`—only supported for SM2 (China Regions only) KMS keys <br />+  `ReEncrypt`—only supported for SM2 (China Regions only) KMS keys <br />+  `Sign` <br />+  `Verify`  | 1,000 (shared) for elliptic curve (ECC) and SM2 (China Regions only) KMS keys | 
| `Custom key store request quotas`<br />Applies to:+  `Decrypt` <br />+  `DeriveSharedSecret` <br />+  `Encrypt` <br />+  `GenerateDataKey` <br />+  `GenerateDataKeyWithoutPlaintext` <br />+  `GenerateRandom` <br />+  `ReEncrypt`  | [Custom key store request quotas](#rps-key-stores) are calculated separately for each custom key store+  1,800 (shared) for each AWS CloudHSM key store <br />+  1,800 (shared) for each external key store  | 
| `CancelKeyDeletion request rate` | 5 | 
| `ConnectCustomKeyStore request rate` | 5 | 
| `CreateAlias request rate` | 5 | 
| `CreateCustomKeyStore request rate` | 5 | 
| `CreateGrant request rate` | 50 | 
| `CreateKey request rate` | 5 | 
| `DeleteAlias request rate` | 15 | 
| `DeleteCustomKeyStore request rate` | 5 | 
| `DeleteImportedKeyMaterial request rate` | 15 | 
| `DescribeCustomKeyStores request rate` | 5 | 
| `DescribeKey request rate` | 2000 | 
| `DisableKey request rate` | 5 | 
| `DisableKeyRotation request rate` | 5 | 
| `DisconnectCustomKeyStore request rate` | 5 | 
| `EnableKey request rate` | 5 | 
| `EnableKeyRotation request rate` | 15 | 
| `GenerateDataKeyPair (ECC_NIST_P256) request rate`<br />Applies to:+  `GenerateDataKeyPair` <br />+   `GenerateDataKeyPairWithoutPlaintext`  | 100 | 
| `GenerateDataKeyPair (ECC_NIST_P384) request rate`<br />Applies to:+  `GenerateDataKeyPair` <br />+   `GenerateDataKeyPairWithoutPlaintext`  | 100 | 
| `GenerateDataKeyPair (ECC_NIST_P521) request rate`<br />Applies to:+  `GenerateDataKeyPair` <br />+   `GenerateDataKeyPairWithoutPlaintext`  | 100 | 
| `GenerateDataKeyPair (ECC_SECG_P256K1) request rate`<br />Applies to:+  `GenerateDataKeyPair` <br />+   `GenerateDataKeyPairWithoutPlaintext`  | 100 | 
| `GenerateDataKeyPair (ECC_NIST_EDWARDS25519) request rate`<br />Applies to:+  `GenerateDataKeyPair` <br />+   `GenerateDataKeyPairWithoutPlaintext`  | 100 | 
| `GenerateDataKeyPair (RSA_2048) request rate`<br />Applies to:+  `GenerateDataKeyPair` <br />+   `GenerateDataKeyPairWithoutPlaintext`  | This quota varies with the AWS Region.+  20 (all other Regions) <br />+  The limit is 1 in the following Regions:   China (Beijing), cn-north-1   China (Ningxia), cn-northwest-1    | 
| `GenerateDataKeyPair (RSA_3072) request rate`<br />Applies to:+  `GenerateDataKeyPair` <br />+   `GenerateDataKeyPairWithoutPlaintext`  | This quota varies with the AWS Region.+  4 (all other Regions) <br />+  The limit is 0.5 in the following Regions:   China (Beijing), cn-north-1   China (Ningxia), cn-northwest-1    | 
| `GenerateDataKeyPair (RSA_4096) request rate`<br />Applies to:+  `GenerateDataKeyPair` <br />+   `GenerateDataKeyPairWithoutPlaintext`  | This quota varies with the AWS Region.+  1 (all other Regions) <br />+  The limit is 0.1 in the following Regions:   China (Beijing), cn-north-1   China (Ningxia), cn-northwest-1    | 
| `GenerateDataKeyPair (SM2 — China Regions only) request rate`<br />Applies to:+  `GenerateDataKeyPair` <br />+   `GenerateDataKeyPairWithoutPlaintext`  | 25 | 
| `GetKeyLastUsage request rate` | 5 | 
| `GetKeyPolicy request rate` | 1000 | 
| `GetKeyRotationStatus request rate` | 1000 | 
| `GetParametersForImport request rate` | 1 | 
| `GetPublicKey request rate` | 2000 | 
| `ImportKeyMaterial request rate` | 15 | 
| `ListAliases request rate` | 500 | 
| `ListGrants request rate` | 100 | 
| `ListKeyPolicies request rate` | 100 | 
| `ListKeys request rate` | 500 | 
| `ListKeyRotations request rate` | 100 | 
| `ListResourceTags request rate` | 2000 | 
| `ListRetirableGrants request rate` | 100 | 
| `PutKeyPolicy request rate` | 15 | 
| ReplicateKey request rateA `ReplicateKey` operation counts as one `ReplicateKey` request in the primary key's Region and two `CreateKey` requests in the replica's Region. One of the `CreateKey` requests is a dry run to detect potential problems before creating the key.  | 5 | 
| `RetireGrant request rate` | 50 | 
| `RevokeGrant request rate` | 50 | 
| `RotateKeyOnDemand request rate` | 5 | 
| `ScheduleKeyDeletion request rate` | 15 | 
| `TagResource request rate` | 10 | 
| `UntagResource request rate` | 5 | 
| `UpdateAlias request rate` | 5 | 
| `UpdateCustomKeyStore request rate` | 5 | 
| `UpdateKeyDescription request rate` | 5 | 
| `UpdatePrimaryRegion request rate`<br />An `UpdatePrimaryRegion` operation counts as two `UpdatePrimaryRegion` requests; one request in each of the two affected Regions. | 5 | 

## Applying request quotas
<a name="about-rate-limits"></a>

When reviewing request quotas, keep in mind the following information.
+ Request quotas apply to both [customer managed keys](concepts.md#customer-mgn-key) and [AWS managed keys](concepts.md#aws-managed-key). The use of [AWS owned keys](concepts.md#aws-owned-key) does not count against request quotas for your AWS account, even when they are used to protect resources in your account.
+ Request quotas apply to requests sent to FIPS endpoints and non-FIPS endpoints. For a list of AWS KMS service endpoints, see [AWS Key Management Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/kms.html) in the AWS General Reference.
+ Throttling is based on all requests on KMS keys of all types in the Region. This total includes requests from all principals in the AWS account, including requests from AWS services on your behalf.
+ Each request quota is calculated independently. For example, requests for the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) operation have no effect on the request quota for the [CreateAlias](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateAlias.html) operation. If your `CreateAlias` requests are throttled, your `CreateKey` requests can still complete successfully. 
+ Although cryptographic operations share a quota, the shared quota is calculated independently of quotas for other operations. For example, calls to the [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) and [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) operations share a request quota, but that quota is independent of the quota for management operations, such as [EnableKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html). For example, in the Europe (London) Region, you can perform 10,000 cryptographic operations on symmetric KMS keys *plus* 5 `EnableKey` operations per second without being throttled.

## Shared quotas for cryptographic operations
<a name="rps-shared-limit"></a>

AWS KMS [cryptographic operations](kms-cryptography.md#cryptographic-operations) share request quotas. You can request any combination of the cryptographic operations that are supported by the KMS key, just so the total number of cryptographic operations doesn't exceed the request quota for that type of KMS key. The exceptions are [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair.html) and [GenerateDataKeyPairWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPairWithoutPlaintext.html), which share a separate quota. 

The quotas for different types of KMS keys are calculated independently. Each quota applies to all requests for these operations in the AWS account and Region with the given key type in each one-second interval.
+ *Cryptographic operations (symmetric) request rate* is the shared request quota for cryptographic operations using symmetric KMS keys in an account and region. This quota applies to cryptographic operations with symmetric encryption keys and HMAC keys, which are also symmetric.

  For example, you might be using [symmetric KMS keys](symm-asymm-choose-key-spec.md#symmetric-cmks) in an AWS Region with a shared quota of 10,000 requests per second. When you make 7,000 [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) requests per second and 2,000 [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) requests per second, AWS KMS doesn't throttle your requests. However, when you make 9,500 `GenerateDataKey` requests and 1,000 [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) and requests per second, AWS KMS throttles your requests because they exceed the shared quota.

  Cryptographic operations on the [symmetric encryption KMS keys](symm-asymm-choose-key-spec.md#symmetric-cmks) in a [custom key store](key-store-overview.md#custom-key-store-overview) count toward both the *Cryptographic operations (symmetric) request rate* for the account and the [custom key store request quota](#rps-key-stores) for the custom key store. 
+ *Cryptographic operations (RSA) request rate* is the shared request quota for cryptographic operations using [RSA asymmetric KMS keys](symm-asymm-choose-key-spec.md#key-spec-rsa). 

  For example, with a request quota of 1,000 operations per second, you can make 400 [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) requests and 200 [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) requests with RSA KMS keys that can encrypt and decrypt, plus 250 [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html) requests and 150 [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html) requests with RSA KMS keys that can sign and verify.
+ *Cryptographic operations (ECC) request rate* is the shared request quota for cryptographic operations using [elliptic curve (ECC) asymmetric KMS keys](symm-asymm-choose-key-spec.md#key-spec-ecc) and [SM asymmetric KMS keys](symm-asymm-choose-key-spec.md#key-spec-sm). 

  For example, with a request quota of 1,000 operations per second, you can make 400 Sign requests and 200 Verify requests with ECC KMS keys that can sign and verify, plus 250 [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html) requests and 150 [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html) requests with SM2 KMS keys that can sign and verify.
+ *Custom key store request quota* is the shared request quota for cryptographic operations on KMS keys in a custom key store. This quota is calculated separately for each custom key store. 

  Cryptographic operations on the [symmetric encryption KMS keys](symm-asymm-choose-key-spec.md#symmetric-cmks) in a [custom key store](key-store-overview.md#custom-key-store-overview) count toward both the *Cryptographic operations (symmetric) request rate* for the account and the [custom key store request quota](#rps-key-stores) for the custom key store. 

The quotas for different key types are also calculated independently. For example, in the Asia Pacific (Singapore) Region, if you use both symmetric and asymmetric KMS keys, you can make up to 10,000 calls per second with symmetric KMS keys (including HMAC keys) *plus* up to 500 additional calls per second with your RSA asymmetric KMS keys, *plus* up to 300 additional requests per second with your ECC-based KMS keys.

## API requests made on your behalf
<a name="rps-from-service"></a>

You can make API requests directly or by using an integrated AWS service that makes API requests to AWS KMS on your behalf. The quota applies to both kinds of requests.

For example, you might store data in Amazon S3 using server-side encryption with a KMS key (SSE-KMS). Each time you upload or download an S3 object that's encrypted with SSE-KMS, Amazon S3 makes a `GenerateDataKey` (for uploads) or `Decrypt` (for downloads) request to AWS KMS on your behalf. These requests count toward your quota, so AWS KMS throttles the requests if you exceed a combined total of 5,500 (or 10,000 or 50,000 depending upon your AWS Region) uploads or downloads per second of S3 objects encrypted with SSE-KMS.

## Cross-account requests
<a name="rps-cross-account"></a>

When an application in one AWS account uses a KMS key owned by a different account, it's known as a *cross-account request*. For cross-account requests, AWS KMS throttles the account that makes the requests, not the account that owns the KMS key. For example, if an application in account A uses a KMS key in account B, the KMS key use applies only to the quotas in account A.

## Custom key store request quotas
<a name="rps-key-stores"></a>

AWS KMS maintains request quotas for [cryptographic operations](kms-cryptography.md#cryptographic-operations) on the KMS keys in a [custom key store](key-store-overview.md#custom-key-store-overview). These request quotas are calculated separately for each custom key store.


| Custom key store request quota | Default value (requests per second) for each custom key store | Adjustable | 
| --- | --- | --- | 
| [AWS CloudHSM key store](keystore-cloudhsm.md) request quota | 1800 | No | 
| [External key store](keystore-external.md) request quota | 1800 | No | 

**Note**  
AWS KMS [custom key store request quotas](#rps-key-stores) do not appear in the Service Quotas console. You cannot view or manage these quotas by using Service Quotas API operations.  
If the AWS CloudHSM cluster associated with an AWS CloudHSM key store is processing numerous commands, including those unrelated to the custom key store, you might get an AWS KMS `ThrottlingException` at a lower-than-expected rate. If this occurs, lower your request rate to AWS KMS, reduce the unrelated load, or use a dedicated AWS CloudHSM cluster for your AWS CloudHSM key store.  
AWS KMS reports throttling of external key store requests in the [`ExternalKeyStoreThrottle`](monitoring-cloudwatch.md#metric-throttling) CloudWatch metric. You can use this metric to view throttling patterns, create alarms, and adjust your external key store request quota.

A request for a [cryptographic operation](kms-cryptography.md#cryptographic-operations) on a KMS key in a custom key store counts toward two quotas: 
+ Cryptographic operations (symmetric) request rate quota (per account)

  Requests for cryptographic operations on KMS keys in a custom key store count toward the `Cryptographic operations (symmetric) request rate` quota for each AWS account and Region. For example, in US East (N. Virginia) (us-east-1), each AWS account can have up to 100,000 requests per second on symmetric encryption KMS keys, including requests that use a KMS key in a custom key store.
+ Custom key store request quota (per custom key store)

  Requests for cryptographic operations on KMS keys in a custom key store also count toward a `Custom key store request quota` of 1,800 operations per second. These quotas are calculated separately for each custom key store. They might include requests from multiple AWS accounts that use KMS keys in the custom key store.

For example, an [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) operation on a KMS key in a custom key store (either type) in the US East (N. Virginia) (us-east-1) Region counts toward the `Cryptographic operations (symmetric) request rate` account-level quota (100,000 requests per second) for its account and Region, and toward a `Custom key store request quota` (1,800 requests per second) for its custom key store. However, a request for a management operation, such as [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html), on a KMS key in a custom key store applies only to its account-level quota (15 requests per second).