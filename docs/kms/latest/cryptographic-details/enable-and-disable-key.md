# Enabling and disabling keys

Disabling a KMS key prevents the key from being used in cryptographic operations. It
suspends the ability to use all HBKs that are associated with the KMS key. Enabling restores
use of the HBKs and the KMS key. [Enable](../APIReference/API_Enable.md "../APIReference/API_Enable.md")
and [Disable](../APIReference/API_Disable.md "../APIReference/API_Disable.md") are simple requests that take
only the key ID or key ARN of the KMS key.
