

# SMSEC01-BP02 Restrict content origin access to allow only authorized content distribution networks
<a name="smsec01-bp02"></a>

Even authenticated users can act maliciously with your workloads, so consider how to secure the data path of your video streams. Tokenization schemes such as signed-URLs, signed-cookies, or JWTs (JSON Web Tokens) should be used to grant only temporary access to content by approved frontend applications. Amazon CloudFront can protect access to content origin through signed URLs and signed cookies with a short duration to live, and Lambda@Edge can validate bearer tokens during viewer request.

**Desired outcome:**
+ Allow user access to only the minimum amount of data that they need to complete their tasks, so that users to don't access or share data that they should not have access to. Controlling access to content minimizes the risks of content leaks or unauthorized access

**Common anti-patterns:**
+ Organizations expose content origin servers directly to the internet without content delivery network (CDN)-based access controls, allowing anyone to retrieve streams by guessing or discovering origin URLs.
+ Teams configure signed URLs with excessively long expiration times, enabling link sharing and unauthorized redistribution of content access tokens.
+ Organizations fail to implement Origin Access Control between CloudFront and MediaPackage or S3, allowing direct origin bypass that circumvents geo-restrictions and token validation.
+ Teams use static shared secrets for origin authentication that are never rotated, increasing the risk of secret compromise over time.
+ Organizations don't validate bearer tokens at the edge using Lambda@Edge, allowing expired or revoked tokens to continue accessing content streams.

**Benefits of establishing this best practice:**
+ Blocks direct access to origin servers, removing the ability for unauthorized users to bypass CDN-enforced security controls such as geo-restrictions and token validation.
+ Limiting origin access to only CloudFront distributions removes the origin from public exposure, protecting against targeted scraping, credential stuffing, and volumetric attacks.
+ Short-lived signed URLs and cookies cause shared links to expire quickly, limiting the window for unauthorized redistribution of content access.
+ CDN-level access controls block circumvention of geographic content licensing restrictions that would be possible through direct origin access.
+ Token validation at the edge through Lambda@Edge processes authorization decisions close to viewers without adding latency or load to origin infrastructure.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

When using content distribution networks to accelerate distribution to viewers, help to protect your content origin from unauthorized origin access by validating a secret header injected by the CDN transmitted over TLS at the time of request and use a policy that blocks access from all other entities. CloudFront and other CDNs can also be configured to block access based on geographic location and enforce [encryption in transit](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html).

With AWS Elemental MediaPackage and Amazon CloudFront, you can create a CloudFront distribution that connects to the MediaPackage endpoint for live streaming. With CloudFront Origin Access Control (OAC) you can [restrict the endpoint so that only CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-mediapackage.html) or authorized users are able to access the stream.

For other services such as Amazon EC2, you can restrict access with [Identity and Access Management (IAM) Policy Conditions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html). Your CloudFront distribution can identify itself to the origin by injecting a user-agent header secret value during requests for objects. You can apply this secret check on the service itself and employ a web application firewall, such as AWS WAF, to perform the check on your behalf.

### Implementation steps
<a name="implementation-steps"></a>

1. **Implement token-based authorization:** Integrate token-based authorization for content access control.

1. **Configure signed URLs and cookies:** Configure signed URLs and cookies for CloudFront distributions and Lambda@Edge for real-time token validation.

1. **Create a CloudFront distribution for MediaPackage:** [Create a CloudFront distribution](https://docs.aws.amazon.com/mediapackage/latest/userguide/cdns.html) with a MediaPackage v2 (EMPv2) endpoint as the origin.

1. **Create an OAC policy:** [Create an OAC policy restricting access](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-mediapackage.html) to only CloudFront and apply to the EMPv2 endpoint.

1. **Configure OAC for Amazon S3:** Configure a CloudFront distribution with the S3 bucket as the origin and [apply an OAC](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC01-BP01 Use an identity provider to authenticate viewers and access policies to implement least privilege access to protected content](smsec01-bp01.html)
+ [SMSEC05-BP02 Restrict content origin access to only allow known entities](smsec05-bp02.html)

**Related documents**
+ [Restricting Access to MediaPackage with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-mediapackage.html)
+ [Live Streaming with Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/live-streaming.html)
+ [Amazon CloudFront IAM Security](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/security_iam_service-with-iam.html)

**Related services**
+ [AWS CloudFront](https://aws.amazon.com/cloudfront/)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)
+ [AWS IAM](https://aws.amazon.com/iam/)