# Linux commands and OpenSSL for base64 encoding and encryption

You can use the following Linux command-line command and OpenSSL to hash and sign the policy statement,
base64-encode the signature, and replace characters that are not valid in URL query string parameters with characters
that are valid.

For information about OpenSSL, go to [https://www.openssl.org](https://www.openssl.org "https://www.openssl.org").

```
cat policy | tr -d "\n" | tr -d " \t\n\r" | openssl sha1 -sign private_key.pem | openssl base64 -A | tr -- '+=/' '-_~'
```

In the preceding command:

- `cat` reads the `policy` file.
- `tr -d "\n" | tr -d " \t\n\r"` removes the empty spaces and newline character that were added by
  `cat`.
- OpenSSL hashes the file using SHA-1 and signs it using the
  private key file `private_key.pem`. The private key signature can be either RSA 2048 or ECDSA 256.
- OpenSSL base64-encodes the hashed and signed policy statement.
- `tr` replaces characters that are not valid in URL query string parameters with characters that are
  valid.
  For more code examples that demonstrate creating a signature, see [Code examples for creating a signature for a signed URL](PrivateCFSignatureCodeAndExamples.md "PrivateCFSignatureCodeAndExamples.md").
