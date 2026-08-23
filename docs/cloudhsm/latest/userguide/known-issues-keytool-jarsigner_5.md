# Known issues for AWS CloudHSM integration Java Keytool and Jarsigner using Client SDK 5

The following list provides the current list of known issues for integrations with
AWS CloudHSM and Java Keytool and Jarsigner using Client SDK 5.

1. We do not support non-Ed25519 EC keys with Keytool and Jarsigner.
2. We do not support ML-DSA key generation through keytool. Use `KeyPairGenerator` or the CloudHSM CLI to generate ML-DSA key pairs.
3. ML-DSA signature algorithms with jarsigner require JDK 26 or later.
