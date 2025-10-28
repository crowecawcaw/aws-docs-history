# Values specific for simple alias

records

When you create alias records, you specify the following values. For more information, see [Choosing between alias and non-alias records](resource-record-sets-choosing-alias-non-alias.md "resource-record-sets-choosing-alias-non-alias.md").

###### Note

If you are using Route 53 in the AWS GovCloud (US) Region, this feature has some restrictions. For more information, see the [Amazon Route 53 page](../../../govcloud-us/latest/UserGuide/govcloud-r53.md "../../../govcloud-us/latest/UserGuide/govcloud-r53.md") in the _AWS GovCloud (US) User Guide_.

###### Topics

- [Routing policy](#rrsets-values-alias-routing-policy "#rrsets-values-alias-routing-policy")
- [Record name](#rrsets-values-alias-name "#rrsets-values-alias-name")
- [Value/route traffic to](#rrsets-values-alias-alias-target "#rrsets-values-alias-alias-target")
- [Record type](#rrsets-values-alias-type "#rrsets-values-alias-type")
- [Evaluate target
  health](#rrsets-values-alias-evaluate-target-health "#rrsets-values-alias-evaluate-target-health")

## Routing policy

Choose **Simple routing**.

## Record name

Enter the name of the domain or subdomain that you want to route traffic for. The default value is the name of the hosted zone.

###### Note

If you're creating a record that has the same name as the hosted zone, don't enter a value (for example, an @ symbol) in the
**Name** field.

For more information about record names, see [Record name](resource-record-sets-values-alias-common.md#rrsets-values-common-alias-name "resource-record-sets-values-alias-common.md#rrsets-values-common-alias-name").

## Value/route traffic to

The value that you choose from the list or that you type in the field depends on the AWS resource that you're routing traffic to.

For information about what AWS resources you can target, see [common values for alias records for value/route traffic to](resource-record-sets-values-alias-common.md#rrsets-values-alias-common-target "resource-record-sets-values-alias-common.md#rrsets-values-alias-common-target").

For more information about how to configure Route 53 to route traffic to specific AWS resources, see
[Routing internet traffic to your AWS resources](routing-to-aws-resources.md "routing-to-aws-resources.md").

## Record type

The DNS record type. For more information, see [Supported DNS record types](ResourceRecordTypes.md "ResourceRecordTypes.md").

Select the applicable value based on the AWS resource that you're routing traffic to:

**API Gateway custom regional API or edge-optimized API**

Select **A — IPv4 address**.

**Amazon VPC interface endpoints**

Select **A — IPv4 address**.

**CloudFront distribution**

Select **A — IPv4 address**.

If IPv6 is enabled for the distribution, create two records, one with a value of **A — IPv4 address** for
**Type**, and one with a value of **AAAA — IPv6 address**.

**App Runner service**

Select **A — IPv4 address**

**Elastic Beanstalk environment that has regionalized subdomains**

Select **A — IPv4 address**

**ELB load balancer**

Select **A — IPv4 address** or **AAAA — IPv6 address**

**Amazon S3 bucket**

Select **A — IPv4 address**

**OpenSearch Service**

Select **A — IPv4 address** or **AAAA — IPv6 address**

**Another record in this hosted zone**

Select the type of the record that you're creating the alias for. All types are supported except **NS** and
**SOA**.

###### Note

If you're creating an alias record that has the same name as the hosted zone (known as the _zone apex_), you
can't route traffic to a record for which the value of **Type** is **CNAME**. This is because the
alias record must have the same type as the record you're routing traffic to, and creating a CNAME record for the zone apex isn't
supported even for an alias record.

## Evaluate target

health

When the value of **Routing policy** is **Simple**,
you can choose either **No** or the default **Yes**
because **Evaluate target health** has no effect for
**Simple** routing. If you have only one record that has a given
name and type, Route 53 responds to DNS queries by using the values in that record
regardless of whether the resource is healthy.

For other routing policies, **Evaluate target health** determines
whether Route 53 checks the health of the resource that the alias record refers to:

- **Services where Evaluate target health provides
  operational benefit**: For load balancers (ELB) and AWS Elastic Beanstalk
  environments with load balancers, setting **Evaluate target
  health** to **Yes** allows Route 53 to route traffic
  away from unhealthy resources.
- **Highly available services**: For services like
  Amazon S3 buckets, VPC interface endpoints, Amazon API Gateway, AWS Global Accelerator, Amazon OpenSearch Service, and
  Amazon VPC Lattice, **Evaluate target health** provides no
  operational benefit because these services are designed for high availability.
  For failover scenarios with these services, use [Route 53 health
  checks](dns-failover.md "dns-failover.md") instead.

For detailed information about how **Evaluate target health** works
with different AWS services, see the [EvaluateTargetHealth](../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth "../APIReference/API_AliasTarget.md#Route53-Type-AliasTarget-EvaluateTargetHealth") documentation in the API reference.
