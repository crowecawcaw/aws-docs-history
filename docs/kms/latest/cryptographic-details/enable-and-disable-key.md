

# Enabling and disabling keys
<a name="enable-and-disable-key"></a>

Disabling a KMS key prevents the key from being used in cryptographic operations. It suspends the ability to use all HBKs that are associated with the KMS key. Enabling restores use of the HBKs and the KMS key. [Enable](https://docs.aws.amazon.com/kms/latest/APIReference/API_Enable.html) and [Disable](https://docs.aws.amazon.com/kms/latest/APIReference/API_Disable.html) are simple requests that take only the key ID or key ARN of the KMS key.