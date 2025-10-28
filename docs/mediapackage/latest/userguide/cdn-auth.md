# Secure MediaPackage content with CDN authorization

AWS Elemental MediaPackage CDN authorization helps you protect your streaming content from unauthorized
access and direct origin requests. When you configure CDN authorization, MediaPackage only fulfills
playback requests that include valid authorization headers from your content delivery
network, preventing users from bypassing your CDN to access content directly.

If you use Amazon CloudFront for your CDN, you can configure access to MediaPackage resources with [AWS Signature Version 4 (SigV4)
authentication](sig-v4-authenticating-requests.md "sig-v4-authenticating-requests.md").

If your CDN doesn't support SigV4, use the following instructions to set up authorization
headers between your CDN and MediaPackage.

## How it works

You configure your CDN to include a _custom HTTP header_ in content
requests to MediaPackage.

The custom HTTP header must use the exact name
`X-MediaPackageV2-CDNIdentifier` with a value that is 8-256
characters long. We strongly recommend using the [UUID version 4](https://www.ietf.org/rfc/rfc4122.txt "https://www.ietf.org/rfc/rfc4122.txt") format for the
value, which produces a 36-character string that is both unique and
unpredictable.

###### Example header

The following example shows the required header format.

```
X-MediaPackageV2-CDNIdentifier: `9ceebbe7-9607-4552-8764-876e47032660`
```

You store the header value as a _secret_ in
AWS Secrets Manager. When your CDN sends a playback request, MediaPackage verifies the custom HTTP header
value. MediaPackage compares this value with the stored secret. An AWS Identity and Access Management permissions policy
and role grant MediaPackage permission to read the secret.

If the values match, MediaPackage serves the content along with an HTTP `200 OK`
status code. If the values don't match, or if the authorization request fails, MediaPackage
doesn't serve the content and returns an HTTP `403 Unauthorized` status
code.

The following image shows successful CDN authorization using Amazon CloudFront.

![This diagram illustrates the CDN authorization workflow: 1. A playback device requests content from Amazon CloudFront 2. CloudFront includes the X-MediaPackageV2-CDNIdentifier header in its request to MediaPackage 3. MediaPackage retrieves the secret value from AWS Secrets Manager (requires IAM permissions) 4. MediaPackage compares the header value with the stored secret 5. When values match, MediaPackage returns HTTP 200 OK with video content 6. CloudFront delivers the content to the playback device When values don't match, MediaPackage returns HTTP 403 Unauthorized.](images/cdn_auth.png)

Complete the following procedures to configure CDN authorization with MediaPackage.

###### Topics

- [Configure MediaPackage CDN authorization setup](cdn-auth-setup.md "cdn-auth-setup.md")
- [Rotate MediaPackage CDN authorization secrets](cdn-auth-rotate.md "cdn-auth-rotate.md")
- [Troubleshoot MediaPackage CDN authorization
  errors](cdn-auth-troubleshooting.md "cdn-auth-troubleshooting.md")
- [Optimize MediaPackage CDN authorization
  security](cdn-auth-best-practices.md "cdn-auth-best-practices.md")
