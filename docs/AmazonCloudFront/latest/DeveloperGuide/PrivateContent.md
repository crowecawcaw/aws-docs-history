# Serve private content with signed URLs and signed

cookies

Many companies that distribute content over the internet want to restrict access to documents, business data, media
streams, or content that is intended for selected users, for example, users who have paid a fee. To securely serve this
private content by using CloudFront, you can do the following:

- Require that your users access your private content by using special CloudFront signed URLs or signed cookies.
- Require that your users access your content by using CloudFront URLs, not URLs that access content directly on
  the origin server (for example, Amazon S3 or a private HTTP server). Requiring CloudFront URLs isn't
  necessary, but we recommend it to prevent users from bypassing the restrictions that you specify in signed URLs or
  signed cookies.
  For more information, see [Restrict access to files](private-content-overview.md "private-content-overview.md").

## How to serve private content

To configure CloudFront to serve private content, do the following tasks:

1.  (Optional but recommended) Require your users to access your content only through CloudFront. The method that you
    use depends on whether you're using Amazon S3 or custom origins:

        * **Amazon S3** – See [Restrict access to an Amazon S3
         origin](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md").
        * **Custom origin** – See [Restrict access to files on custom
         origins](private-content-overview.md#forward-custom-headers-restrict-access "private-content-overview.md#forward-custom-headers-restrict-access").

    Custom origins include Amazon EC2, Amazon S3 buckets configured as website endpoints, ELB, and your own HTTP web
    servers.

2.  Specify the _trusted key groups_ or _trusted signers_ that you want to use to create signed
    URLs or signed cookies. We recommend that you use trusted key groups. For more
    information, see [Specify signers that can create signed
    URLs and signed cookies](private-content-trusted-signers.md "private-content-trusted-signers.md").
3.  Write your application to respond to requests from authorized users either with signed URLs or with
    `Set-Cookie` headers that set signed cookies. Follow the steps in one of the following topics:

        * [Use signed URLs](private-content-signed-urls.md "private-content-signed-urls.md")
        * [Use signed cookies](private-content-signed-cookies.md "private-content-signed-cookies.md")

    If you're not sure which method to use, see [Decide to use signed URLs or
    signed cookies](private-content-choosing-signed-urls-cookies.md "private-content-choosing-signed-urls-cookies.md").

###### Topics

- [Restrict access to files](private-content-overview.md "private-content-overview.md")
- [Specify signers that can create signed
  URLs and signed cookies](private-content-trusted-signers.md "private-content-trusted-signers.md")
- [Decide to use signed URLs or
  signed cookies](private-content-choosing-signed-urls-cookies.md "private-content-choosing-signed-urls-cookies.md")
- [Use signed URLs](private-content-signed-urls.md "private-content-signed-urls.md")
- [Use signed cookies](private-content-signed-cookies.md "private-content-signed-cookies.md")
- [Linux commands and OpenSSL for base64
  encoding and encryption](private-content-linux-openssl.md "private-content-linux-openssl.md")
- [Code examples for creating a signature for a
  signed URL](PrivateCFSignatureCodeAndExamples.md "PrivateCFSignatureCodeAndExamples.md")
