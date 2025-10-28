# Certificate import problems

You can import third-party certificates into ACM and associate them with [integrated services](acm-services.md "acm-services.md"). If you encounter
problems, review the [prerequisites](import-certificate-prerequisites.md "import-certificate-prerequisites.md") and [certificate format](import-certificate-format.md "import-certificate-format.md") topics. In particular, note the following:

- You can import only X.509 version 3 SSL/TLS certificates.
- Your certificate can be self–signed or it can be signed by a certificate
  authority (CA).
- If your certificate is signed by a CA, you must include an intermediate certificate
  chain that provides a path to the root of authority.
- If your certificate is self-signed, you must include the private key in
  plaintext.
- Each certificate in the chain must directly certify the one preceding.
- Do not include your end-entity certificate in the intermediate certificate
  chain.
- Your certificate, certificate chain, and private key (if any) must be
  PEM–encoded. In general, PEM encoding consists of blocks of Base64-encoded ASCII
  text that begin and end with plaintext header and footer lines. You must not add lines
  or spaces or make any other changes to a PEM file while copying or uploading it. You can
  verify certificate chains using the [OpenSSL verify
  utility](https://www.openssl.org/docs/manmaster/man1/openssl-verify.html "https://www.openssl.org/docs/manmaster/man1/openssl-verify.html").
- Your private key (if any) must not be encrypted. (Tip: if it has a passphrase, it's
  encrypted.)
- Services [integrated](acm-services.md "acm-services.md") with ACM
  must use ACM-supported algorithms and key sizes. See the AWS Certificate Manager User Guide and the
  documentation for each service to make sure that your certificate will work.
- Certificate support by integrated services might differ depending on whether the
  certificate is imported into IAM or into ACM.
- The certificate must be valid when it is imported.
- Detail information for all of your certificates is displayed in the console. By
  default, however, if you call the [ListCertificates](../APIReference/API_ListCertificates.md "../APIReference/API_ListCertificates.md") API or the [list-certificates](../../../cli/latest/reference/acm/list-certificates.md "../../../cli/latest/reference/acm/list-certificates.md") AWS CLI command without specifying the `keyTypes`
  filter, only `RSA_1024` or `RSA_2048` certificates are displayed.
