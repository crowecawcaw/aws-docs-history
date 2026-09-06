

# Control Objective 5: Keys are used in a manner that prevents or detects their unauthorized usage.
<a name="pin-compliance-control-5"></a>

*Requirement 17:* The service provides mechanisms, such as tags and aliases, for keys that enable tracking of key sharing relationships. Additionally, key check values should be kept separately to demonstrate that known or default key values are not used when keys are shared.

*Requirement 18:* The service provides key integrity checks, via [GetKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey) and [ListKeys](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys), and key management events, via AWS CloudTrail, that can be used to detect unauthorized substitution or monitor synchronization of keys between parties. The service stores keys exclusively in key blocks. You are responsible for key storage and use prior to import to and after export from AWS Payment Cryptography. 

You should have procedures in place for an immediate investigation should any discrepancy occur during processing of PIN based transactions or unexpected key management events. 

*Requirement 19:* The service uses keys exclusively in key blocks, enforcing KeyUsage, KeyModeOfUse, and other [key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_KeyAttributes) for all operations. This includes restriction on private key operations. You should use your public keys for a single purpose e:g encryption or digital signature verification but not both. You should use separate accounts for production and test/development systems.

*Requirement 20:* You retain responsibility for this requirement.