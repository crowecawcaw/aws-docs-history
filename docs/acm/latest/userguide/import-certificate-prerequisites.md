# Prerequisites for importing ACM certificates

To import a self–signed SSL/TLS certificate into ACM, you must provide both
the certificate and its private key. To import a certificate signed by a non-AWS
certificate authority (CA), you must also include the private and public keys of
certificate. Your certificate must satisfy all of the criteria described in this
topic.

For all imported certificates, you must specify a cryptographic algorithm and a key
size. ACM supports the following algorithms (API name in parentheses):

- RSA 1024 bit (`RSA_1024`)
- RSA 2048 bit (`RSA_2048`)
- RSA 3072 bit (`RSA_3072`)
- RSA 4096 bit (`RSA_4096`)
- ECDSA 256 bit (`EC_prime256v1`)
- ECDSA 384 bit (`EC_secp384r1`)
- ECDSA 521 bit (`EC_secp521r1`)
  Note also the following additional requirements:

- ACM [integrated services](acm-services.md "acm-services.md")
  allow only the algorithms and key sizes that they support to be associated with
  their resources. For example, CloudFront only supports 1024-bit RSA, 2048-bit RSA,
  3072-bit RSA, 4096-bit RSA, and Elliptic Prime Curve 256-bit keys, while Application Load Balancer
  supports all of the algorithms available from ACM. For more information, see
  the documentation for the service you are using.
- A certificate must be an SSL/TLS X.509 version 3 certificate. It must contain
  a public key, the fully qualified domain name (FQDN) or IP address for your
  website, and information about the issuer.
- A certificate can be self-signed by a private key that you own, or signed by
  the private key of an issuing CA. You must provide the private key, which may be
  no larger than 5 KB (5,120 bytes) and must be unencrypted.
- If the certificate is signed by a CA, and you choose to provide the
  certificate chain, the chain must be PEM–encoded.
- A certificate must be valid at the time of import. You cannot import a
  certificate before its validity period begins or after it expires. The
  `NotBefore` certificate field contains the validity start date,
  and the `NotAfter` field contains the end date.
- All of the required certificate materials (certificate, private key, and
  certificate chain) must be PEM–encoded. Uploading DER–encoded
  materials results in an error. For more information and examples, see [Certificate and key format for importing](import-certificate-format.md "import-certificate-format.md").
- When you renew (reimport) a certificate, you cannot add a
  `KeyUsage` or `ExtendedKeyUsage` extension if the
  extension was not present in the previously imported certificate

**Exception:** You can reimport a certificate
missing the Client Authentication ExtendedKeyUsage when compared to the previous
certificate. This accommodates industry changes where certificate authorities no
longer issue certificates with ClientAuth EKU to comply with Chrome's root
program requirements.

###### Important

If you require Client Authentication functionality, you must implement
additional validations on your side, as ACM does not support rollback to
previously imported certificates.

- AWS CloudFormation does not support the import of certificates into ACM.
