# Check value in CloudHSM CLI

The *check value* in CloudHSM CLI is a 3-byte hash or
 checksum of a key that is generated when the HSM imports or generates a key. You can also calculate a check value outside
 of the HSM, such as after you export a key. You can then compare the check value values to confirm
 the identity and integrity of the key. To get the check value of a key, use [key list](cloudhsm_cli-key-list.md "cloudhsm_cli-key-list.md") with the verbose flag.

AWS CloudHSM uses the following standard methods to generate a check value:


* **Symmetric keys**: First 3 bytes of the result of
 encrypting a zero-block with the key.
* **Asymmetric key pairs**: First 3 bytes of the
 SHA-1 hash of the public key.
* **HMAC keys**: KCV for HMAC keys is not supported at this time.
