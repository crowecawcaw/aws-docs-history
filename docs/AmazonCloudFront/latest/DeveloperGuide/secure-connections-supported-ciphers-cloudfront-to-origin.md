

# Supported protocols and ciphers between CloudFront and the origin
<a name="secure-connections-supported-ciphers-cloudfront-to-origin"></a>

If you choose to [require HTTPS between CloudFront and your origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginProtocolPolicy), you can decide [which SSL/TLS protocol to allow](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginSSLProtocols) for the secure connection, and CloudFront can connect to the origin using any of the ECDSA or RSA ciphers listed in the following table. Your origin must support at least one of these ciphers for CloudFront to establish an HTTPS connection to your origin.

OpenSSL and [s2n](https://github.com/awslabs/s2n) use different names for ciphers than the TLS standards use ([RFC 2246](https://tools.ietf.org/html/rfc2246), [RFC 4346](https://tools.ietf.org/html/rfc4346), [RFC 5246](https://tools.ietf.org/html/rfc5246), and [RFC 8446](https://tools.ietf.org/html/rfc8446)). The following table includes the OpenSSL and s2n name, and the RFC name, for each cipher.

For ciphers with elliptic curve key exchange algorithms, CloudFront supports the following elliptic curves:
+ prime256v1
+ secp384r1
+ X25519


<table>
<thead>
  <tr><th>OpenSSL and s2n cipher name</th><th>RFC cipher name</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>Supported ECDSA ciphers</b></td></tr>
  <tr><td>ECDHE-ECDSA-AES256-GCM-SHA384</td><td>TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA384</td><td>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA</td><td>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-GCM-SHA256</td><td>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA256</td><td>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA</td><td>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA</td></tr>
  <tr><td colspan="2"><b>Supported RSA ciphers</b></td></tr>
  <tr><td>ECDHE-RSA-AES256-GCM-SHA384</td><td>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384</td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA384</td><td>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384</td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA</td><td>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA</td></tr>
  <tr><td>ECDHE-RSA-AES128-GCM-SHA256</td><td>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256</td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA256</td><td>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256</td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA</td><td>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA</td></tr>
  <tr><td>AES256-SHA</td><td>TLS_RSA_WITH_AES_256_CBC_SHA</td></tr>
  <tr><td>AES128-SHA</td><td>TLS_RSA_WITH_AES_128_CBC_SHA</td></tr>
  <tr><td>DES-CBC3-SHA</td><td>TLS_RSA_WITH_3DES_EDE_CBC_SHA</td></tr>
  <tr><td>RC4-MD5</td><td>TLS_RSA_WITH_RC4_128_MD5</td></tr>
</tbody>
</table>


**Supported signature schemes between CloudFront and the origin**

CloudFront supports the following signature schemes for connections between CloudFront and the origin.
+ TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA256
+ TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA384
+ TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA512
+ TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA224
+ TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA256
+ TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA384
+ TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA512
+ TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA224
+ TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA1
+ TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA1