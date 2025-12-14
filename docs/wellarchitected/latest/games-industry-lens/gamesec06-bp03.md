# GAMESEC06-BP03 Use insights from system-level logs to

continuously improve your infrastructure protection strategy

Capture and store system-level logs from relevant services, such
as [S3
server access logs](../../../AmazonS3/latest/userguide/ServerLogs.md "../../../AmazonS3/latest/userguide/ServerLogs.md"),
[CloudFront
access logs](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md"), and
[ALB
access](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md")
[logs](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md").
These logs can be stored in an S3 bucket in your account and are
useful for associating your player usage information from within
the game with system-level information including connection
details such as IP addresses, request headers, and relevant
request manipulation and filtering that you may have configured
within your game backend. You can send these logs to the same
logging solutions mentioned earlier, and you can
[analyze
them using SQL queries with Amazon Athena](../../../athena/latest/ug/application-load-balancer-logs.md "../../../athena/latest/ug/application-load-balancer-logs.md") without requiring
the logs to be moved out of Amazon S3.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Access
Analyzer for S3](../../../AmazonS3/latest/userguide/access-analyzer.md "../../../AmazonS3/latest/userguide/access-analyzer.md") is a feature that monitors your bucket
access policies, making sure that the policies provide only the
intended access to your Amazon S3 resources. Access Analyzer for
S3 evaluates your bucket access policies and allows you to
discover and swiftly remediate buckets with potentially unintended
access.

### Implementation steps

- Use AWS services for threat detection and incident response
  to automate aspects of your infrastructure protection
  strategy.
- Gain insights into your infrastructure protection through
  system-level logs and AWS services for artificial
  intelligence and machine learning.

## Data protection

When developing and architecting your game, consider what type of
data your studio is gathering and how you have decided to approach
protecting it. Topics to explore within this aspect of security
include:

- How you have chosen to identify and classify your data
- How you are protecting data at rest
- How you are protecting data in transit

There are no data protection best practices specific to the Games
Lens. Refer to the Well-Architected Framework whitepaper for best
practices
in [data
protection](../security-pillar/data-protection.md "../security-pillar/data-protection.md") for security.
