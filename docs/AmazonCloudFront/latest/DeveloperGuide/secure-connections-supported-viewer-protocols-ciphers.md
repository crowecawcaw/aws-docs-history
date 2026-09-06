

# Supported protocols and ciphers between viewers and CloudFront
<a name="secure-connections-supported-viewer-protocols-ciphers"></a>

When you [require HTTPS between viewers and your CloudFront distribution](DownloadDistValuesCacheBehavior.md#DownloadDistValuesViewerProtocolPolicy), you must choose a [security policy](DownloadDistValuesGeneral.md#DownloadDistValues-security-policy), which determines the following settings:
+ The minimum SSL/TLS protocol that CloudFront uses to communicate with viewers.
+ The ciphers that CloudFront can use to encrypt the communication with viewers.

To choose a security policy, specify the applicable value for [Security policy (minimum SSL/TLS version)](DownloadDistValuesGeneral.md#DownloadDistValues-security-policy). The following table lists the protocols and ciphers that CloudFront can use for each security policy.

A viewer must support at least one of the supported ciphers to establish an HTTPS connection with CloudFront. CloudFront chooses a cipher in the listed order from among the ciphers that the viewer supports. See also [OpenSSL, s2n, and RFC cipher names](#secure-connections-openssl-rfc-cipher-names).


<table>
<thead>
  <tr><th></th><th colspan="9">Security policy</th></tr>
  <tr><th></th><th>SSLv3</th><th>TLSv1</th><th>TLSv1_2016</th><th>TLSv1.1_2016</th><th>TLSv1.2_2018</th><th>TLSv1.2_2019</th><th>TLSv1.2_2021</th><th>TLSv1.2_2025</th><th>TLSv1.3_2025</th></tr>
</thead>
<tbody>
  <tr><td colspan="10"><b>Supported SSL/TLS protocols</b></td></tr>
  <tr><td>TLSv1.3</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLSv1.2</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>TLSv1.1</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>TLSv1</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>SSLv3</td><td>♦</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td colspan="10"><b>Supported TLSv1.3 ciphers</b></td></tr>
  <tr><td>TLS_AES_128_GCM_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_AES_256_GCM_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_CHACHA20_POLY1305_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td>♦</td></tr>
  <tr><td colspan="10"><b>Supported ECDSA ciphers</b></td></tr>
  <tr><td>ECDHE-ECDSA-AES128-GCM-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES256-GCM-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>ECDHE-ECDSA-CHACHA20-POLY1305</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td colspan="10"><b>Supported RSA ciphers</b></td></tr>
  <tr><td>ECDHE-RSA-AES128-GCM-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-RSA-AES256-GCM-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>ECDHE-RSA-CHACHA20-POLY1305</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES128-GCM-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES256-GCM-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES128-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES256-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES128-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>DES-CBC3-SHA</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>RC4-MD5</td><td>♦</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>


## OpenSSL, s2n, and RFC cipher names
<a name="secure-connections-openssl-rfc-cipher-names"></a>

OpenSSL and [s2n](https://github.com/awslabs/s2n) use different names for ciphers than the TLS standards use ([RFC 2246](https://tools.ietf.org/html/rfc2246), [RFC 4346](https://tools.ietf.org/html/rfc4346), [RFC 5246](https://tools.ietf.org/html/rfc5246), and [RFC 8446](https://tools.ietf.org/html/rfc8446)). The following table maps the OpenSSL and s2n names to the RFC name for each cipher.

CloudFront supports both classical and quantum-safe key exchanges. For classical key exchanges using elliptic curves, CloudFront supports the following:
+ `prime256v1`
+ `X25519`
+ `secp384r1`

For quantum-safe key exchanges, CloudFront supports the following:
+ `X25519MLKEM768`
+ `SecP256r1MLKEM768`
**Note**  
Quantum-safe key exchanges are only supported with TLS 1.3. TLS 1.2 and earlier versions do not support quantum-safe key exchanges.

  For more information, see the following topics:
  + [Post-Quantum Cryptography](https://aws.amazon.com/security/post-quantum-cryptography/)
  + [Cryptography algorithms and AWS services](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/aws-cryptography-services.html#algorithms)
  + [Hybrid key exchange in TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)

For more information about certificate requirements for CloudFront, see [Requirements for using SSL/TLS certificates with CloudFront](cnames-and-https-requirements.md).


<table>
<thead>
  <tr><th>OpenSSL and s2n cipher name</th><th>RFC cipher name</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>Supported TLSv1.3 ciphers</b></td></tr>
  <tr><td>TLS_AES_128_GCM_SHA256</td><td>TLS_AES_128_GCM_SHA256</td></tr>
  <tr><td>TLS_AES_256_GCM_SHA384</td><td>TLS_AES_256_GCM_SHA384</td></tr>
  <tr><td>TLS_CHACHA20_POLY1305_SHA256</td><td>TLS_CHACHA20_POLY1305_SHA256</td></tr>
  <tr><td colspan="2"><b>Supported ECDSA ciphers</b></td></tr>
  <tr><td>ECDHE-ECDSA-AES128-GCM-SHA256</td><td>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA256</td><td>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA</td><td>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-GCM-SHA384</td><td>TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384</td></tr>
  <tr><td>ECDHE-ECDSA-CHACHA20-POLY1305</td><td>TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA384</td><td>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA</td><td>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA</td></tr>
  <tr><td colspan="2"><b>Supported RSA ciphers</b></td></tr>
  <tr><td>ECDHE-RSA-AES128-GCM-SHA256</td><td>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256</td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA256</td><td>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 </td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA</td><td>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA</td></tr>
  <tr><td>ECDHE-RSA-AES256-GCM-SHA384</td><td>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 </td></tr>
  <tr><td>ECDHE-RSA-CHACHA20-POLY1305</td><td>TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256</td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA384</td><td>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 </td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA</td><td>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA</td></tr>
  <tr><td>AES128-GCM-SHA256</td><td>TLS_RSA_WITH_AES_128_GCM_SHA256</td></tr>
  <tr><td>AES256-GCM-SHA384</td><td>TLS_RSA_WITH_AES_256_GCM_SHA384</td></tr>
  <tr><td>AES128-SHA256</td><td>TLS_RSA_WITH_AES_128_CBC_SHA256</td></tr>
  <tr><td>AES256-SHA</td><td>TLS_RSA_WITH_AES_256_CBC_SHA</td></tr>
  <tr><td>AES128-SHA</td><td>TLS_RSA_WITH_AES_128_CBC_SHA</td></tr>
  <tr><td>DES-CBC3-SHA </td><td>TLS_RSA_WITH_3DES_EDE_CBC_SHA </td></tr>
  <tr><td>RC4-MD5</td><td>TLS_RSA_WITH_RC4_128_MD5</td></tr>
</tbody>
</table>


## Supported signature schemes between viewers and CloudFront
<a name="secure-connections-viewer-signature-schemes"></a>

CloudFront supports the following signature schemes for connections between viewers and CloudFront.


<table>
<thead>
  <tr><th></th><th colspan="9">Security policy</th></tr>
  <tr><th>Signature schemes</th><th>SSLv3</th><th>TLSv1</th><th>TLSv1_2016</th><th>TLSv1.1_2016</th><th>TLSv1.2_2018</th><th>TLSv1.2_2019</th><th> TLSv1.2_2021</th><th>TLSv1.2_2025</th><th>TLSv1.3_2025</th></tr>
</thead>
<tbody>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PSS_PSS_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PSS_PSS_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PSS_PSS_SHA512</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PSS_RSAE_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PSS_RSAE_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PSS_RSAE_SHA512</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA512</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA224</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_ECDSA_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_ECDSA_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_ECDSA_SHA512</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_ECDSA_SHA224</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_ECDSA_SECP256R1_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_ECDSA_SECP384R1_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_RSA_PKCS1_SHA1</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>TLS_SIGNATURE_SCHEME_ECDSA_SHA1</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>
