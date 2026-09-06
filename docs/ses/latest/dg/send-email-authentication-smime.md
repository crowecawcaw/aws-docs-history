

# Authenticating email with S/MIME in Amazon SES
<a name="send-email-authentication-smime"></a>

*Secure/Multipurpose Internet Mail Extensions* (*S/MIME*) is a standard that uses a certificate-based digital signature. It proves that a message was sent by the holder of the From address and that its content was not altered in transit. For more information about the S/MIME message format, see [ RFC 8551: S/MIME Message Specification](https://www.rfc-editor.org/rfc/rfc8551) on the RFC Editor website.

S/MIME signing proves message authenticity and integrity at the individual sender level. Recipients can be confident that the message content has not been tampered with.

With Amazon SES, you can automatically apply an S/MIME signature without signing messages before submitting them. You manage the certificate in AWS Certificate Manager (ACM). Amazon SES is one of the services that integrate with ACM. For more information about services that integrate with ACM, see [Services integrated with ACM](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html).

**S/MIME and DKIM**  
S/MIME and DKIM operate at different levels and are complementary. DKIM proves that the sending domain authorized the message using keys published in DNS. S/MIME uses a certificate to assert a chain of trust back to a certificate authority. This proves that the specific email-address holder sent the message and that the content is intact. S/MIME is not a replacement for DKIM.

## Understanding the S/MIME signature
<a name="send-email-authentication-smime-signature"></a>

Amazon SES signs an outbound message when you send it through a configuration set that has S/MIME signing enabled. The resolved email identity must have an `ACTIVE` certificate for the From address. Amazon SES signs the message server-side at send time.

Amazon SES produces a detached signature using the `multipart/signed` format (clear-signing), as defined in [RFC 1847](https://www.rfc-editor.org/rfc/rfc1847) on the RFC Editor website. The original message remains readable by recipients whose mail clients do not support S/MIME. Amazon SES sends the signed content as the first MIME part. It carries the signature separately as a second part of media type `application/pkcs7-signature` (typically named `smime.p7s`). Amazon SES embeds your signing certificate and its certificate chain in the signature (a Cryptographic Message Syntax (CMS) SignedData object). Recipients can then build the chain of trust back to the issuing certificate authority and verify message integrity and origin.

The signed message uses standard S/MIME headers. These include a `Content-Type: multipart/signed` header with a `protocol` parameter of `"application/pkcs7-signature"` and a `micalg` parameter that names the digest algorithm (for example, `sha-256`). The following example shows the top-level Content-Type header of a signed message:

```
Content-Type: multipart/signed;
    protocol="application/pkcs7-signature";
    micalg=sha-256;
    boundary="----=_SmimeBoundary"
```

## S/MIME certificate considerations
<a name="send-email-authentication-smime-certificate-considerations"></a>

For a certificate to be usable for S/MIME signing in Amazon SES, it must meet all of the following requirements:
+ The certificate must be in ACM in the same AWS Region where you send email.
+ The email identity must be verified. Either domain verification (TXT record) or email-address verification is acceptable.
+ The certificate's Subject Alternative Name (SAN) must include an RFC822Name email address that matches the From address. For a domain identity, this means an address under that domain or a subdomain. For an email-address identity, this means an exact match.
+ The certificate key algorithm must use one of: RSA 2048, RSA 3072, RSA 4096, EC P-256, EC P-384, or EC P-521 (per [RFC 8550](https://www.rfc-editor.org/rfc/rfc8550) on the RFC Editor website).
+ The certificate must be currently valid (not expired).

**Certificate authority trust requirement**  
Recipients' mail clients must trust the certificate authority (CA) that issued your certificate to validate the signature. Certificates from a public CA are trusted by most mail clients and ISPs by default. If you use a private CA, recipients must have access to and trust your root CA. ISPs and mail clients do not trust private CAs by default.

For more information about certificate standards, see [RFC 5280: X.509 Certificate and CRL Profile](https://www.rfc-editor.org/rfc/rfc5280) and [RFC 8550: S/MIME Certificate Handling](https://www.rfc-editor.org/rfc/rfc8550) on the RFC Editor website.

**Topics**
+ [Understanding the S/MIME signature](#send-email-authentication-smime-signature)
+ [S/MIME certificate considerations](#send-email-authentication-smime-certificate-considerations)
+ [Attaching a certificate to an email identity](send-email-authentication-smime-associate.md)
+ [Enabling S/MIME signing on a configuration set](send-email-authentication-smime-enable.md)