# Security checklist for marketplace distributions

E-commerce and marketplace applications handle sensitive data — customer sessions,
payment flows, and premium content. This checklist covers the security controls specific
to a CloudFront distribution with an ElastiCache (Valkey) caching layer. Apply these controls in addition
to the general CloudFront security best practices described in
[Configure secure access and restrict access to content](SecurityAndPrivateContent.md "SecurityAndPrivateContent.md").

## Signed URLs and cookies for premium content

Use signed URLs or signed cookies to restrict access to content that requires
authorization — premium product previews, purchased digital goods, time-limited
promotional content, or seller-specific assets.

Signed URL and signed cookie comparison| Method | Use when | E-commerce example |
| --- | --- | --- |
| Signed URL | Restricting access to individual files. Sharing download links.<br>Clients that do not support cookies. | One-time download link for a purchased digital product. Time-limited<br>access to a high-resolution product image for a verified seller. |
| Signed cookie | Providing access to multiple files (for example, all assets in a premium<br>tier). Avoiding URL changes for existing content. | Premium membership access to an entire catalog of digital content.<br>Subscriber-only product previews across multiple pages. |

Configuration requirements:

- Create a key group with an RSA public key (2048-bit minimum). Store the
  private key in AWS Secrets Manager for your application to generate signatures.
- Set the cache behavior's **Restrict viewer access** to
  **Yes** and associate the key group.
- Set an expiration time appropriate to the content type: minutes for
  download links, hours for browsing sessions, days for subscription access.
- Use a custom policy (not a canned policy) when you need to restrict by
  IP range or allow wildcard paths.

For implementation details, see
[Serve private content with signed URLs and signed cookies](PrivateContent.md "PrivateContent.md").

## Origin access control (OAC) for Amazon S3

Origin access control prevents users from bypassing CloudFront to access your Amazon S3 bucket
directly. Without OAC, anyone who discovers your bucket URL can access assets without
going through your signed URL/cookie enforcement, WAF rules, or geo-restrictions. For
full configuration steps, see
[Restrict access to an AWS origin](private-content-restricting-access-to-origin.md "private-content-restricting-access-to-origin.md").

**Enable OAC for all Amazon S3 origins**

Create an OAC and associate it with each Amazon S3 origin in your distribution. Update
the bucket policy to allow only the CloudFront service principal
(`cloudfront.amazonaws.com`) with a condition matching your distribution
ARN.

**Remove public access**

In the Amazon Simple Storage Service console, enable Amazon S3 Block Public Access on the bucket. This is an
Amazon S3 setting, not a CloudFront setting. The bucket policy grants access only
to CloudFront — no public ACLs or policies are needed. For more information, see
[Blocking
public access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the
_Amazon Simple Storage Service User Guide_.

**Use the Amazon S3 REST API endpoint**

Configure the origin using the bucket's REST API endpoint
(`bucket-name.s3.amazonaws.com`), not the Amazon S3 website endpoint. OAC only
works with the REST API endpoint.

## Encryption in transit

Encrypt all connections in the request path — viewer to CloudFront, CloudFront to origin, and
application to ElastiCache cache.

Encryption in transit configuration| Connection | Setting | Configuration |
| --- | --- | --- |
| Viewer → CloudFront | Viewer protocol policy: HTTPS only | Set viewer protocol policy to `redirect-to-https` or<br>`https-only` on all cache behaviors. Use a TLS 1.2 minimum security<br>policy (`TLSv1.2_2021`). |
| CloudFront → S3 origin | Origin protocol: HTTPS | S3 REST API endpoints support HTTPS by default. CloudFront uses HTTPS when<br>you configure the origin with the REST API endpoint and OAC. |
| CloudFront → ALB origin | Origin protocol: HTTPS only | Set origin protocol policy to `https-only`. Install a valid<br>TLS certificate on the ALB (use AWS Certificate Manager). CloudFront validates the certificate on<br>connection. |
| Application → ElastiCache | In-transit encryption: Enabled | In the ElastiCache console, enable `TransitEncryptionEnabled` on the<br>replication group. This is an ElastiCache setting. Use TLS connections from your application<br>code. Valkey and Redis OSS 6.0 and later support in-transit encryption natively. |

## VPC security groups for the cache cluster

The ElastiCache cluster runs in a VPC and must only accept connections from your application
servers. Use security group chaining to restrict access.

Security group configuration for ElastiCache| Security group | Inbound rule | Rationale |
| --- | --- | --- |
| Cache cluster SG | TCP 6379 from Application SG only | Only application servers can reach the cache. No internet access, no<br>access from other services. Use port 6379 (default Valkey/Redis port) or your<br>configured port. |
| Application SG | TCP 443 from ALB SG only | Application servers accept traffic only from the ALB. Combined with the<br>cache cluster SG, this creates a chain: CloudFront → ALB → App → Cache. |

Additional VPC hardening:

- Deploy the ElastiCache cluster in private subnets with no internet gateway route.
- Use a subnet group that spans at least 2 Availability Zones for high availability.
- Enable ElastiCache auth token (password) for an additional authentication layer beyond security groups.
- Disable public access to the ElastiCache cluster (default, but verify).

## Additional security controls

**Restrict ALB access to CloudFront only**

Add a custom origin header (`X-Origin-Verify`) that CloudFront sends with
every request. Configure the ALB or application to reject requests that do not include
this header. Store the header value in AWS Secrets Manager and rotate it periodically.
Alternatively, use the CloudFront managed prefix list to restrict ALB security group
inbound rules to CloudFront IP ranges.

**Enable AWS WAF on the distribution**

Associate an AWS WAF web ACL with rate-limiting rules to protect against cart
abuse, credential stuffing on login APIs, and inventory scraping. Use managed rule
groups for common threats (SQL injection, XSS) and custom rules for
application-specific patterns.

**Geo-restrictions for compliance**

If your marketplace operates in specific countries, enable geo-restriction to
block requests from regions where you do not have legal authority to sell or ship.
Apply at the distribution level. For per-path geo-restriction, use AWS WAF
geo-match conditions in a web ACL rule with a URL path condition.

**Access logging**

Enable CloudFront standard logging or real-time logging to detect abnormal access
patterns — sudden spikes in download link usage, access from unexpected regions,
or repeated failed auth attempts at API endpoints.
