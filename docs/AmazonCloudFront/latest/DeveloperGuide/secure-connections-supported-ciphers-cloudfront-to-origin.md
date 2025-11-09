# Supported

protocols and ciphers between CloudFront and the origin

If you choose to [require HTTPS between CloudFront and your origin](distribution-web-values-specify.md#DownloadDistValuesOriginProtocolPolicy "distribution-web-values-specify.md#DownloadDistValuesOriginProtocolPolicy"), you can decide [which SSL/TLS protocol to allow](distribution-web-values-specify.md#DownloadDistValuesOriginSSLProtocols "distribution-web-values-specify.md#DownloadDistValuesOriginSSLProtocols") for the secure connection, and CloudFront can connect
to the origin using any of the ECDSA or RSA ciphers listed in the following table. Your
origin must support at least one of these ciphers for CloudFront to establish an HTTPS
connection to your origin.

OpenSSL and [s2n](https://github.com/awslabs/s2n "https://github.com/awslabs/s2n") use different names for
ciphers than the TLS standards use ([RFC
2246](https://tools.ietf.org/html/rfc2246 "https://tools.ietf.org/html/rfc2246"), [RFC 4346](https://tools.ietf.org/html/rfc4346 "https://tools.ietf.org/html/rfc4346"), [RFC 5246](https://tools.ietf.org/html/rfc5246 "https://tools.ietf.org/html/rfc5246"), and [RFC 8446](https://tools.ietf.org/html/rfc8446 "https://tools.ietf.org/html/rfc8446")). The following table
includes the OpenSSL and s2n name, and the RFC name, for each cipher.

For ciphers with elliptic curve key exchange algorithms,
CloudFront supports the following elliptic curves:

- prime256v1
- secp384r1
- X25519

| OpenSSL and s2n cipher name    | RFC cipher name                         |
| ------------------------------ | --------------------------------------- |
| **Supported ECDSA<br>ciphers** |
| ECDHE-ECDSA-AES256-GCM-SHA384  | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 |
| ECDHE-ECDSA-AES256-SHA384      | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 |
| ECDHE-ECDSA-AES256-SHA         | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA    |
| ECDHE-ECDSA-AES128-GCM-SHA256  | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 |
| ECDHE-ECDSA-AES128-SHA256      | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 |
| ECDHE-ECDSA-AES128-SHA         | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA    |
| **Supported RSA ciphers**      |
| ECDHE-RSA-AES256-GCM-SHA384    | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384   |
| ECDHE-RSA-AES256-SHA384        | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384   |
| ECDHE-RSA-AES256-SHA           | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA      |
| ECDHE-RSA-AES128-GCM-SHA256    | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256   |
| ECDHE-RSA-AES128-SHA256        | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256   |
| ECDHE-RSA-AES128-SHA           | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA      |
| AES256-SHA                     | TLS_RSA_WITH_AES_256_CBC_SHA            |
| AES128-SHA                     | TLS_RSA_WITH_AES_128_CBC_SHA            |
| DES-CBC3-SHA                   | TLS_RSA_WITH_3DES_EDE_CBC_SHA           |
| RC4-MD5                        | TLS_RSA_WITH_RC4_128_MD5                |

**Supported signature schemes between CloudFront and the
origin**

CloudFront supports the following signature schemes for connections between CloudFront and the
origin.

- TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA256
- TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA384
- TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA512
- TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA224
- TLS_SIGNATURE_SCHEME_ECDSA_SHA256
- TLS_SIGNATURE_SCHEME_ECDSA_SHA384
- TLS_SIGNATURE_SCHEME_ECDSA_SHA512
- TLS_SIGNATURE_SCHEME_ECDSA_SHA224
- TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA1
- TLS_SIGNATURE_SCHEME_ECDSA_SHA1
