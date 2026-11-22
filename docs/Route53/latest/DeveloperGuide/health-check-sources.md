

# Health check sources

A health check source is a resource in your VPC that Route 53 health checkers use to reach private endpoints in that VPC.

To create a source, you choose an AWS Region, a VPC in that Region, and three subnets in three different Availability Zones. For each subnet, you choose one or more security groups (up to 10). Private endpoint health checks that use the source run from that Region.

**Note**  
In US West (N. California), which has two Availability Zones, choose two subnets.

Keep the following characteristics in mind when you work with health check sources:
+ Each health check source supports up to 200 health checks. To run more health checks, create additional sources.
+ You can create up to 5 health check sources per AWS account.
+ Health checks that use a health check source count toward the quota of 200 health checks per AWS account. For more information, see [Quotas on health checks](DNSLimitations.md#limits-api-entities-health-checks).
+ You can associate health checks that use a source only with records in the same AWS account as the source.
+ After you create a health check source, you can't change its network configuration (VPC, subnets, or security groups). You can still change its name and tags, and edit the health checks that use it. To change the network configuration, create a new source, reassociate your health checks to the new source, and then delete the old source.
+ Creating a source can take a few minutes. A source must be in the **Available** status before you can use it in a health check.
+ A health check source covers three Availability Zones. If your VPC spans more than three Availability Zones, you can create additional health check sources to cover target endpoints in the other Availability Zones.
+ To create or delete a health check source, you need the `iam:CreateServiceLinkedRole` permission for the service-linked role `AWSServiceRoleForRoute53PrivateHealthChecks` (service principal `route53healthchecks.amazonaws.com`). Route 53 makes this call with your credentials on every `CreateHealthCheckSource` and `DeleteHealthCheckSource` request, even after the role exists, so keep the permission in place.

  The AWS managed policy `AmazonRoute53FullAccess` already includes it. For a custom policy, scope it with the condition `iam:AWSServiceName = route53healthchecks.amazonaws.com`. If the permission is missing, the request fails immediately with `AccessDenied` (HTTP 403), and Route 53 doesn't create a source.