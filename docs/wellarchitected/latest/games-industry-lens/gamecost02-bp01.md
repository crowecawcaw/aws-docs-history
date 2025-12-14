# GAMECOST02-BP01 Optimize the cost of data transfer across the

internet

While AWS primarily charges for outbound (egress) data transfer from
your AWS resources to the internet, game companies can face high
costs related to data transfer through AWS Direct Connect or AWS
Gateway load balancers, which may charge for both inbound (ingress)
and outbound data. Implement solutions that reduce the overall cost
of transferring data from your game's AWS backend to your players,
focusing on minimizing egress charges from your AWS resources as
well as evaluating options to manage ingress and egress fees through
AWS connectivity services.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use Amazon CloudFront to reduce the cost of content delivery and
public-facing web applications.

Game content and assets that are stored in the cloud are typically
stored in Amazon S3 and delivered to the game client either
directly from S3 or from web servers hosted in Amazon EC2 that
retrieve the content from Amazon S3 and deliver it to clients. To
reduce the data transfer costs of content downloads, consider
using Amazon CloudFront in front of your cloud storage to deliver
content to users.

Using CloudFront can reduce the cost of data transfer because it
costs less to deliver your content from CloudFront
points-of-presence than directly from Regions, and CloudFront does
not charge origin retrieval fees for AWS-based origins, such as
Amazon EC2 and Amazon S3. If your content is static and does not
change often, you can use CloudFront to cache that data closer to
end-users, which can further reduce costs.

CloudFront also improves the cost efficiency of front-facing
public-facing web applications and services, even if caching is
not used, since the cost of data transfer between your servers and
clients can be reduced by routing traffic through the AWS network.

[Amazon CloudWatch](../../../AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.md "../../../AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.md") can be used to monitor your Amazon CloudFront
usage. For use cases where you use multiple content delivery
networks (CDNs),
[Amazon CloudFront Origin Shield](../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md "../../../AmazonCloudFront/latest/DeveloperGuide/origin-shield.md") can provide an additional layer of
caching to consolidate and reduce the number of origin requests
from different providers.

To understand your game network traffic, you can enable
[VPC
Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") and
[Amazon CloudWatch Internet Monitor](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.md") to have end-to-end visibility
on player or game backend connections. That approach can identify
the causes for high data transfer cost and perform architectural
changes to optimize data transfer spend.

### Implementation steps

- Use Amazon CloudFront in front of Amazon S3 or EC2-based
  content origins to reduce data transfer costs by leveraging
  lower-cost delivery from CloudFront points-of-presence and
  removing origin retrieval fees.
- Enable VPC Flow Logs and Amazon CloudWatch Internet Monitor
  to analyze network traffic and identify architectural
  changes to optimize data transfer costs.
- Implement CloudFront Origin Shield to consolidate and reduce
  origin requests when using multiple CDNs for additional cost
  efficiency.

For more best practices for content delivery, see the
[Content
Delivery for Games whitepaper](https://d1.awsstatic.com/whitepapers/content-delivery-for-games.pdf "https://d1.awsstatic.com/whitepapers/content-delivery-for-games.pdf").
