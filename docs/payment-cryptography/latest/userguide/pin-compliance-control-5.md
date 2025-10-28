# Control Objective 5: Keys are used in a manner that prevents or detects their unauthorized usage.

_Requirement 17:_ The service provides mechanisms, such as tags and aliases, for keys that enable
tracking of key sharing relationships. Additionally, key check values should be kept separately to demonstrate that known
or default key values are not used when keys are shared.

_Requirement 18:_ The service provides key integrity checks, via
[GetKey](../APIReference/API_GetKey.md "../APIReference/API_GetKey.md") and
[ListKeys](../APIReference/API_ListKeys.md "../APIReference/API_ListKeys.md"), and key management events, via
AWS CloudTrail, that can be used to detect unauthorized substitution or monitor synchronization of keys between parties. The
service stores keys exclusively in key blocks. You are responsible for key storage and use prior to import to and after export
from AWS Payment Cryptography.

You should have procedures in place for an immediate investigation should any discrepancy occur during processing of
PIN based transactions or unexpected key management events.

_Requirement 19:_ The service uses keys exclusively in key blocks, enforcing
KeyUsage, KeyModeOfUse, and other
[key attributes](../APIReference/API_KeyAttributes.md "../APIReference/API_KeyAttributes.md") for all operations. This
includes restriction on private key operations. You should use your public keys for a single purpose e:g encryption or digital
signature verification but not both. You should use separate accounts for production and test/development systems.

_Requirement 20:_ You retain responsibility for this requirement.
