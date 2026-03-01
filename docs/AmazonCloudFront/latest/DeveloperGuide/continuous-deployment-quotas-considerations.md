# Quotas and other considerations for continuous deployment

CloudFront continuous deployment is subject to the following quotas and other
considerations.

## Quotas

- Maximum number of staging distributions per AWS account: 20
- Maximum number of continuous deployment policies per AWS account:
  20
- Maximum percentage of traffic you can send to a staging distribution in a
  weight-based configuration: 15%
- Minimum and maximum values for session stickiness idle duration: 300–3600
  seconds

For more information, see [Quotas](cloudfront-limits.md "cloudfront-limits.md").

###### Note

When using continuous deployment and your primary distribution is set with OAC
for S3 bucket access, update your S3 bucket policy to allow access for the
staging distribution. For example S3 bucket policies, see [Grant CloudFront permission to access the S3 bucket](private-content-restricting-access-to-s3.md#oac-permission-to-access-s3 "private-content-restricting-access-to-s3.md#oac-permission-to-access-s3").

## AWS WAF web ACLs

If you enable continuous deployment for your distribution, the following
considerations apply for AWS WAF:

- You can't associate an AWS WAF web access control list (ACL) to the
  distribution if it's the first time that ACL has been associated with the distribution.
- You can't disassociate an AWS WAF web ACL from the distribution.

Before you can do the preceding tasks, you must delete the continuous deployment
policy for your production distribution. This also deletes the staging distribution.
For more information, see [Use AWS WAF protections](distribution-web-awswaf.md "distribution-web-awswaf.md").

## Cases when CloudFront sends all requests to the primary distribution

In certain cases, such as periods of high resource utilization, CloudFront might send
all requests to the primary distribution regardless of what's specified in the
continuous deployment policy.

CloudFront sends all requests to the primary distribution during peak traffic hours,
regardless of what's specified in the continuous deployment policy. Peak traffic
refers to the traffic on the _CloudFront service_, and not the traffic
on your distribution.

## HTTP/3

You cannot use continuous deployment with a distribution that supports
HTTP/3.
