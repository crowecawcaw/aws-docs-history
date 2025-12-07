# AWS managed policies for Amazon Route 53

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy:

AmazonRoute53FullAccess

You can attach the `AmazonRoute53FullAccess` policy to your IAM
identities.

This policy grants full access to Route 53 resources, including domain
registration and health checking, but excluding VPC Resolver.

**Permissions details**

This policy includes the following permissions.

- `route53:*` – Lets you perform all Route 53 actions
  _except_ the following:
  - Create and update alias records for which the value of **Alias
    Target** is a CloudFront distribution, an ELB load balancer, an
    Elastic Beanstalk environment, or an Amazon S3 bucket. (With these permissions, you can
    create alias records for which the value of **Alias
    Target** is another record in the same hosted zone.)
  - Work with private hosted zones.
  - Work with domains.
  - Create, delete, and view CloudWatch alarms.
  - Render CloudWatch metrics in the Route 53 console.

- `route53domains:*`– Lets you work with domains.
- `cloudfront:ListDistributions` – Lets you create and update
  alias records for which the value of **Alias Target** is a CloudFront
  distribution.

This permission isn't required if you aren't using the Route 53 console. Route 53
uses it only to get a list of distributions to display in the console.

- `cloudfront:GetDistributionTenantByDomain` – Used to fetch the CloudFront multi-tenant distributions
  to let you create and update alias records for which the value of **Alias Target** is a CloudFront distribution tenant.
- `cloudfront:GetConnectionGroup` – Used to fetch the CloudFront multi-tenant distributions
  to let you create and update alias records for which the value of **Alias Target** is a CloudFront distribution tenant.
- `cloudwatch:DescribeAlarms` – Together with `sns:ListTopics` and
  `sns:ListSubscriptionsByTopic`, lets you create, delete, and
  view CloudWatch alarms.
- `cloudwatch:GetMetricStatistics` – Lets you create CloudWatch
  metric health checks.

These permissions aren't required if you aren't using the Route 53 console. Route 53
uses it only to get statistics to display in the console.

- `cloudwatch:GetMetricData` – Lets you display the status of your CloudWatch health check metrics.
- `ec2:DescribeVpcs` – Lets you display a list of VPCs.
- `ec2:DescribeVpcEndpoints` – Lets you display a list of VPC
  endpoints.
- `ec2:DescribeRegions` – Lets you display a list of
  Availability Zones.
- `elasticloadbalancing:DescribeLoadBalancers` – Lets you
  create and update alias records for which the value of **Alias
  Target** is an Elastic Load Balancing load balancer.

These permissions aren't required if you aren't using the Route 53 console. Route 53
uses it only to get a list of load balancers to display in the console.

- `elasticbeanstalk:DescribeEnvironments` – Lets you create
  and update alias records for which the value of **Alias
  Target** is an Elastic Beanstalk environment.

These permissions aren't required if you aren't using the Route 53 console. Route 53
uses it only to get a list of environments to display in the console.

- `es:ListDomainNames` – Lets you display the names of all Amazon OpenSearch Service domains owned by the current user in the active Region.
- `es:DescribeDomains` – Lets you get the domain configuration for the specified Amazon OpenSearch Service domains.
- `lightsail:GetContainerServices` – Lets you the Lightsail container services to let
  you create and update alias records for which the value of **Alias Target** is a Lightsail domain.
- `s3:ListBucket`, `s3:GetBucketLocation`, and
  `s3:GetBucketWebsite` – Let you create and update alias
  records for which the value of **Alias Target** is an Amazon S3
  bucket. (You can create an alias to an Amazon S3 bucket only if the bucket is
  configured as a website endpoint; `s3:GetBucketWebsite` gets the
  required configuration information.)

These permissions aren't required if you aren't using the Route 53 console. Route 53
uses these only to get a list of buckets to display in the console.

- `sns:ListTopics`, `sns:ListSubscriptionsByTopic`,
  `cloudwatch:DescribeAlarms` – Let you create, delete, and
  view CloudWatch alarms.
- `tag:GetResources` – Lets you display the tags in your resources. For example, names of your health checks.
- `apigateway:GET` – Lets you create and update alias records
  for which the value of **Alias Target** is an Amazon API Gateway
  API.

For more information about the permissions, see [Amazon Route 53 API permissions: Actions, resources,
and conditions reference](r53-api-permissions-ref.md "r53-api-permissions-ref.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "route53:*",
 "route53domains:*",
 "cloudfront:ListDistributions",
 "cloudfront:GetDistributionTenantByDomain",
 "cloudfront:GetConnectionGroup",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:GetMetricData",
 "ec2:DescribeVpcs",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeRegions",
 "elasticloadbalancing:DescribeLoadBalancers",
 "elasticbeanstalk:DescribeEnvironments",
 "es:ListDomainNames",
 "es:DescribeDomains",
 "lightsail:GetContainerServices",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "s3:GetBucketWebsite",
 "sns:ListTopics",
 "sns:ListSubscriptionsByTopic",
 "tag:GetResources"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "apigateway:GET",
 "Resource": "arn:aws:apigateway:*::/domainnames"
 }
 ]
}`

```

## AWS managed policy: AmazonRoute53ReadOnlyAccess

You can attach the `AmazonRoute53ReadOnlyAccess` policy to your IAM identities.

This policy grants read-only access to Route 53 resources, including domain
registration and health checking, but excluding VPC Resolver.

**Permissions details**

This policy includes the following permissions.

- `route53:Get*` – Gets the Route 53 resources.
- `route53:List*` – Lists the Route 53 resources.
- `route53:TestDNSAnswer` – Gets the value that Route 53
  returns in response to a DNS request.

For more information about the permissions, see [Amazon Route 53 API permissions: Actions, resources,
and conditions reference](r53-api-permissions-ref.md "r53-api-permissions-ref.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "route53:Get*",
 "route53:List*",
 "route53:TestDNSAnswer"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## AWS managed policy: AmazonRoute53DomainsFullAccess

You can attach the `AmazonRoute53DomainsFullAccess` policy to your IAM identities.

This policy grants full access to Route 53 domain registration resources.

**Permissions details**

This policy includes the following permissions.

- `route53:CreateHostedZone` – Lets you create a Route 53 hosted zone.
- `route53domains:*` – Lets you register domain names and perform related
  operations.

For more information about the permissions, see [Amazon Route 53 API permissions: Actions, resources,
and conditions reference](r53-api-permissions-ref.md "r53-api-permissions-ref.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "route53:CreateHostedZone",
 "route53domains:*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## AWS managed policy: AmazonRoute53DomainsReadOnlyAccess

You can attach the `AmazonRoute53DomainsReadOnlyAccess` policy to your IAM identities.

This policy grants read-only access to Route 53 domain registration resources.

**Permissions details**

This policy includes the following permissions.

- `route53domains:Get*` – Lets you retrieve a list of domains from
  Route 53.
- `route53domains:List*` – Lets you display a list of Route 53 domains.

For more information about the permissions, see [Amazon Route 53 API permissions: Actions, resources,
and conditions reference](r53-api-permissions-ref.md "r53-api-permissions-ref.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "route53domains:Get*",
 "route53domains:List*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## AWS managed policy: AmazonRoute53ResolverFullAccess

You can attach the `AmazonRoute53ResolverFullAccess` policy to your IAM identities.

This policy grants full access to Route 53 VPC Resolver resources.

**Permissions details**

This policy includes the following permissions.

- `route53resolver:*` – Lets you create and manage VPC Resolver resources on the
  Route 53 console.
- `ec2:DescribeSubnets` – Lets you list your Amazon VPC subnets.
- `ec2:CreateNetworkInterface`, `ec2:DeleteNetworkInterface`, and
  `ec2:ModifyNetworkInterfaceAttribute` – Let you create,
  modify, and delete network interfaces.
- `ec2:DescribeNetworkInterfaces` – Lets you display a list of network
  interfaces.
- `ec2:DescribeSecurityGroups` – Lets you display a list of all of your
  security groups.
- `ec2:DescribeVpcs` – Lets you display a list of VPCs.
- `ec2:DescribeAvailabilityZones` – Lets you list the zones that are available
  to you.

For more information about the permissions, see [Amazon Route 53 API permissions: Actions, resources,
and conditions reference](r53-api-permissions-ref.md "r53-api-permissions-ref.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonRoute53ResolverFullAccess",
 "Effect": "Allow",
 "Action": [
 "route53resolver:*",
 "ec2:DescribeSubnets",
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:ModifyNetworkInterfaceAttribute",
 "ec2:DescribeNetworkInterfaces",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeVpcs",
 "ec2:DescribeAvailabilityZones"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## AWS managed policy: AmazonRoute53ResolverReadOnlyAccess

You can attach the `AmazonRoute53ResolverReadOnlyAccess` policy to your IAM identities.

This policy grants read-only access to Route 53 VPC Resolver resources.

**Permissions details**

This policy includes the following permissions.

- `route53resolver:Get*` – Gets VPC Resolver resources.
- `route53resolver:List*` – Lets you display a list of VPC Resolver
  resources.
- `ec2:DescribeNetworkInterfaces` – Lets you display a list of network
  interfaces.
- `ec2:DescribeSecurityGroups` – Lets you display a list of all of your
  security groups.

For more information about the permissions, see [Amazon Route 53 API permissions: Actions, resources,
and conditions reference](r53-api-permissions-ref.md "r53-api-permissions-ref.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonRoute53ResolverReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "route53resolver:Get*",
 "route53resolver:List*",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## AWS managed policy: Route53ResolverServiceRolePolicy

You can't attach `Route53ResolverServiceRolePolicy` to your IAM entities.
This policy is attached to a service-linked role that allows Route 53 VPC Resolver to access AWS
services and resources that are used or managed by VPC Resolver. For more information, see
[Using Service-Linked Roles for
Amazon Route 53 Resolver](using-service-linked-roles.md "using-service-linked-roles.md").

## AWS managed policy: AmazonRoute53ProfilesFullAccess

You can attach the `AmazonRoute53ProfilesReadOnlyAccess` policy to your IAM identities.

This policy grants full access to Amazon Route 53 Profile resources.

**Permissions details**

This policy includes the following permissions.

- `route53profiles` – Lets you create and manage Profile resources on the Route 53 console.
- `ec2` – Allows principals to get information about VPCs.

For more information about the permissions, see [Amazon Route 53 API permissions: Actions, resources,
and conditions reference](r53-api-permissions-ref.md "r53-api-permissions-ref.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonRoute53ProfilesFullAccess",
 "Effect": "Allow",
 "Action": [
 "route53profiles:AssociateProfile",
 "route53profiles:AssociateResourceToProfile",
 "route53profiles:CreateProfile",
 "route53profiles:DeleteProfile",
 "route53profiles:DisassociateProfile",
 "route53profiles:DisassociateResourceFromProfile",
 "route53profiles:UpdateProfileResourceAssociation",
 "route53profiles:GetProfile",
 "route53profiles:GetProfileAssociation",
 "route53profiles:GetProfileResourceAssociation",
 "route53profiles:GetProfilePolicy",
 "route53profiles:ListProfileAssociations",
 "route53profiles:ListProfileResourceAssociations",
 "route53profiles:ListProfiles",
 "route53profiles:PutProfilePolicy",
 "route53profiles:ListTagsForResource",
 "route53profiles:TagResource",
 "route53profiles:UntagResource",
 "route53resolver:GetFirewallConfig",
 "route53resolver:GetFirewallRuleGroup",
 "route53resolver:GetResolverConfig",
 "route53resolver:GetResolverDnssecConfig",
 "route53resolver:GetResolverQueryLogConfig",
 "route53resolver:GetResolverRule",
 "ec2:DescribeVpcs",
 "route53:GetHostedZone"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## AWS managed policy: AmazonRoute53ProfilesReadOnlyAccess

You can attach the `AmazonRoute53ProfilesReadOnlyAccess` policy to your IAM identities.

This policy grants read-only access to Amazon Route 53 Profile resources.

**Permissions details**

For more information about the permissions, see [Amazon Route 53 API permissions: Actions, resources,
and conditions reference](r53-api-permissions-ref.md "r53-api-permissions-ref.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonRoute53ProfilesReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "route53profiles:GetProfile",
 "route53profiles:GetProfileAssociation",
 "route53profiles:GetProfileResourceAssociation",
 "route53profiles:GetProfilePolicy",
 "route53profiles:ListProfileAssociations",
 "route53profiles:ListProfileResourceAssociations",
 "route53profiles:ListProfiles",
 "route53profiles:ListTagsForResource",
 "route53resolver:GetFirewallConfig",
 "route53resolver:GetResolverConfig",
 "route53resolver:GetResolverDnssecConfig",
 "route53resolver:GetResolverQueryLogConfig"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Route 53 updates to AWS managed

policies

View details about updates to AWS managed policies for Route 53 since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Route 53 [Document history page](History.md "History.md").

| Change                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Date            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| [AmazonRoute53FullAccess](#security-iam-awsmanpol-AmazonRoute53FullAccess "#security-iam-awsmanpol-AmazonRoute53FullAccess") – Updated<br>policy                                     | Adds permissions for `cloudwatch:GetMetricData`<br>,`tag:GetResources`, `es:ListDomainNames`,<br>`es:DescribeDomains`,<br>`cloudfront:GetDistributionTenantByDomain`,<br>`cloudfront:GetConnectionGroup` and<br>`lightsail:GetContainerServices`. These permissions<br>enable you to fetch up to 500 CloudWatch health check metrics, up to 100<br>names of health checks, get the domain configuration for the<br>specified Amazon OpenSearch Service domains, and list the names of all Amazon OpenSearch Service<br>domains owned by the current user in the active Region, fetch the<br>CloudFront multi-tenant distributions and get the Lightsail container<br>services. | June 01, 2025   |
| [AmazonRoute53ProfilesFullAccess](#security-iam-awsmanpol-AmazonRoute53ProfilesFullAccess "#security-iam-awsmanpol-AmazonRoute53ProfilesFullAccess") – Updated<br>policy             | Adds permissions for `GetProfilePolicy` and `PutProfilePolicy`. These are permission-only IAM actions. If an IAM principal doesn't have these permissions granted,<br>an error will occur when attempting to share the Profile using the AWS RAM service.                                                                                                                                                                                                                                                                                                                                                                                                                      | August 27, 2024 |
| [AmazonRoute53ProfilesReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53ProfilesReadOnlyAccess "#security-iam-awsmanpol-AmazonRoute53ProfilesReadOnlyAccess") – Updated<br>policy | Adds permissions for `GetProfilePolicy`. This is a permission-only IAM action. If an IAM principal doesn't have this permission granted,<br>an error will occur attempting to access the Profile's policy using the AWS RAM service.                                                                                                                                                                                                                                                                                                                                                                                                                                           | August 27, 2024 |
| [AmazonRoute53ResolverFullAccess](#security-iam-awsmanpol-AmazonRoute53ResolverFullAccess "#security-iam-awsmanpol-AmazonRoute53ResolverFullAccess")– Updated<br>policy              | Added a statement id (Sid) to uniquely identity the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | August 5, 2024  |
| [AmazonRoute53ResolverReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53ResolverReadOnlyAccess "#security-iam-awsmanpol-AmazonRoute53ResolverReadOnlyAccess")– Updated<br>policy  | Added a statement id (Sid) to uniquely identity the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | August 5, 2024  |
| [AmazonRoute53ProfilesFullAccess](#security-iam-awsmanpol-AmazonRoute53ProfilesFullAccess "#security-iam-awsmanpol-AmazonRoute53ProfilesFullAccess") – New<br>policy                 | Amazon Route 53 added a new policy to allow full access to Amazon Route<br>53 Profile resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | April 22, 2024  |
| [AmazonRoute53ProfilesReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53ProfilesReadOnlyAccess "#security-iam-awsmanpol-AmazonRoute53ProfilesReadOnlyAccess") – New<br>policy     | Amazon Route 53 added a new policy to allow read-only access to Amazon<br>Route 53 Profile resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | April 22, 2024  |
| [Route53ResolverServiceRolePolicy](#security-iam-awsmanpol-Route53ResolverServiceRolePolicy "#security-iam-awsmanpol-Route53ResolverServiceRolePolicy")– New policy                  | Amazon Route 53 added a new policy that is attached to a service-linked<br>role that allows VPC Resolver to access AWS services and resources that<br>are used or managed by Resolver.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | July 14, 2021   |
| [AmazonRoute53ResolverReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53ResolverReadOnlyAccess "#security-iam-awsmanpol-AmazonRoute53ResolverReadOnlyAccess")– New policy         | Amazon Route 53 added a new policy to allow read-only access to VPC Resolver<br>resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | July 14, 2021   |
| [AmazonRoute53ResolverFullAccess](#security-iam-awsmanpol-AmazonRoute53ResolverFullAccess "#security-iam-awsmanpol-AmazonRoute53ResolverFullAccess")– New policy                     | Amazon Route 53 added a new policy to allow full access to VPC Resolver<br>resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | July 14, 2021   |
| [AmazonRoute53DomainsReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53DomainsReadOnlyAccess "#security-iam-awsmanpol-AmazonRoute53DomainsReadOnlyAccess")– New policy            | Amazon Route 53 added a new policy to allow read-only access to Route 53<br>domains resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | July 14, 2021   |
| [AmazonRoute53DomainsFullAccess](#security-iam-awsmanpol-AmazonRoute53DomainsFullAccess "#security-iam-awsmanpol-AmazonRoute53DomainsFullAccess")– New policy                        | Amazon Route 53 added a new policy to allow full access to Route 53 domains<br>resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | July 14, 2021   |
| [AmazonRoute53ReadOnlyAccess](#security-iam-awsmanpol-AmazonRoute53ReadOnlyAccess "#security-iam-awsmanpol-AmazonRoute53ReadOnlyAccess")– New policy                                 | Amazon Route 53 added a new policy to allow read-only access to Route 53<br>resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | July 14, 2021   |
| [AmazonRoute53FullAccess](#security-iam-awsmanpol-AmazonRoute53FullAccess "#security-iam-awsmanpol-AmazonRoute53FullAccess")– New policy                                             | Amazon Route 53 added a new policy to allow full access to Route 53<br>resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | July 14, 2021   |
| Route 53 started tracking changes                                                                                                                                                    | Route 53 started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | July 14, 2021   |
