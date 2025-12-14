# GAMESEC04-BP02 Limit origin access to authorized content

delivery networks (CDNs)

Block users from circumventing your content delivery
networks to directly access content from your origin, such as your
Amazon S3 buckets. It is important to restrict access to your
origin to only your authorized CDNs, which reduces data transfer
costs from unnecessarily serving content out of the origin. It
also improves your security posture by flowing public access to
your origin content through the same entry point, where you can
deploy edge security controls such as AWS WAF layer 7 filtering,
injection and inspection of security-related HTTP request
parameters, and distributed denial of service (DDoS) protections.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To implement these controls for an Amazon S3 origin, you can use
an [Amazon CloudFront origin access identity (OAI)](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md"), which verifies
that requests to your S3 objects are originating from your
CloudFront distribution. Associate AWS WAF with your CloudFront
distribution to provide layer-7 filtering. However, if you are
serving content from additional CDNs, you can configure the CDN to
insert one or more custom HTTP headers into origin requests which
can be inspected by AWS WAF to verify that the incoming traffic
originated from your authorized CDN provider. 

This approach is also useful for helping prevent users from
circumventing your CDN providers when your origin is hosted behind
an [Application Load Balancer (ALB)](../../../AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.md "../../../AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.md"). ALBs can be associated with AWS WAF
for layer-7 protections. You can configure AWS WAF to insert a
custom HTTP header that will be inspected by your ALB to process
and inspect incoming traffic to the load balancer by AWS WAF.

**Customer example**

AnyCompany Games implements origin access restrictions to help
protect their game assets, downloadable content, and patch files
from unauthorized direct access that could enable players to
bypass security checks or obtain premium content without proper
authentication. This approach allows them to monitor content
access patterns through a centralized point, making it
straightforward for them to identify suspicious download behaviors
that might indicate the presence of coordinated attacks or
unauthorized content redistribution.

### Implementation steps

- Use Amazon CloudFront origin access identity (OAI) to
  restrict direct access to S3 objects
- Associate AWS WAF with CloudFront or ALB to provide layer-7
  filtering and help protect against DDoS attacks and
  malicious requests.
- Configure custom HTTP headers in Cloudfront to verify that
  incoming traffic originates from authorized sources.
