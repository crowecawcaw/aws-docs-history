

# SMSEC05-BP02 Restrict content origin access to only allow known entities
<a name="smsec05-bp02"></a>

Even for live streaming delivery, controlling who is allowed to request content is important. Configure origin access controls so that content can only be accessed by authorized content delivery networks and trusted entities.

**Desired outcome:**
+ Content can only be accessed by going through a content delivery network (CDN), which serves to protect your content from large scale requests and provide controls to limit who can access the content if there are streaming rights to consider
+ CDN security controls block direct origin access

**Common anti-patterns:**
+ Organizations leave content origin endpoints publicly accessible without restricting access to CDN IP ranges, allowing direct origin access that bypasses geo-restrictions, token validation, and rate limiting.
+ Teams configure AWS Elemental MediaPackage or Amazon EC2-based origins with security groups that allow inbound traffic from all sources rather than restricting to known Amazon CloudFront edge IP ranges.
+ Organizations don't update their allowed IP lists when CloudFront publishes new edge location addresses, causing legitimate CDN requests to fail while stale entries remain open.
+ Teams fail to configure S3 bucket policies with Origin Access Control, leaving video on demand (VOD) content buckets accessible to anyone with the bucket URL regardless of CloudFront distribution settings.
+ Organizations use a single origin endpoint for both CDN delivery and internal operations without network segmentation, exposing the content origin to a broader set of potential attackers.

**Benefits of establishing this best practice:**
+ Restricting access to known CDN IP ranges blocks direct origin access, so all viewer requests pass through CDN-enforced security controls including token validation and geo-restrictions.
+ Origins that only accept traffic from CloudFront edge locations are invisible to internet-wide scanning and can't be targeted directly by attackers.
+ All content requests must traverse the CDN layer where AWS WAF rules, signed URLs, and geographic restrictions are applied, blocking bypass of business logic controls.
+ Limiting origin access to CDN traffic blocks unauthorized bulk downloads or scraping that could overwhelm origin infrastructure and degrade service for legitimate viewers.
+ Routing all content delivery through CDN controls guarantees that geographic and temporal restrictions required by content licensing agreements can't be circumvented.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

To reduce the likelihood of impact on your content origin from a volumetric attack such as a distributed denial of service (DDoS) attack, limit the allowed traffic sources to trusted client IP addresses, such as the IP address ranges for your CDN.

When using AWS Elemental MediaPackage v2 or a content origin built on Amazon EC2, restrict requests to originate only from known IP addresses of the CDN points of presence (PoPs) and, if applicable, use security groups to restrict incoming traffic. To isolate access to known Amazon CloudFront IP addresses, AWS provides [a JSON resource](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html) that includes those address ranges, which is regularly updated.

When using S3 based origin with CloudFront, configure [origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) and configure S3 bucket policies to allow access only from CloudFront.

### Implementation steps
<a name="implementation-steps"></a>

1. **Determine allowed CloudFront locations:** Determine the list of [CloudFront locations and IPs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html) that you want to allow to access your content.

1. **Set up security access controls:** Set up security access to content in EC2, S3, or AWS MediaPackage v2 with Identity and Access Management (IAM).

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC05-BP01 Use DDoS protection service to maintain content availability](smsec05-bp01.html)
+ [SMSEC01-BP02 Restrict content origin access to allow only authorized content distribution networks](smsec01-bp02.html)

**Related documents**
+ [Amazon CloudFront Edge Server Locations](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html)
+ [Amazon EC2 IAM Security](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam.html)
+ [AWS Elemental MediaPackage Policies and Permissions](https://docs.aws.amazon.com/mediapackage/latest/userguide/policies-permissions.html)

**Related services**
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [AWS MediaPackage v2](https://aws.amazon.com/mediapackage/)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [AWS EC2](https://aws.amazon.com/ec2/)