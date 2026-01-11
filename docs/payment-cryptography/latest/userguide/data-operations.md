# Data operations

After you have established an AWS Payment Cryptography key, it can be used to perform cryptographic operations.
Different operations perform different types of activity ranging from encryption, hashing as well
as domain specific algorithms such as CVV2 generation.

Encrypted data cannot be decrypted without the matching decryption key (the symmetric key or
private key depending on the encryption type). Hashing and domain specific algorithms similarly cannot be verified without the
symmetric key or public key.

For information on valid key types for specific operations
please see [Valid keys for cryptographic operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md")

###### Note

We recommend using test data when in a non-production environment. Using production keys and data (PAN, BDK ID, etc.)
in a non-production environment may impact your compliance scope such as for PCI DSS and PCI P2PE.

###### Topics

- [Encrypt, Decrypt and Re-encrypt data](crypto-ops.md "crypto-ops.md")
- [Generate and verify card data](crypto-ops-carddata.md "crypto-ops-carddata.md")
- [Generate, translate and verify PIN data](data-operations.md "data-operations.md")
- [Verify auth request (ARQC) cryptogram](data-operations.md "data-operations.md")
- [Generate and verify MAC](crypto-ops-mac.md "crypto-ops-mac.md")
- [Valid keys for cryptographic operations](crypto-ops-validkeys-ops.md "crypto-ops-validkeys-ops.md")
