

# AZ-affinity routing

With AZ-affinity routing, you can route traffic to resources based on the Availability Zone (AZ) that the query comes from. This helps you reduce latency and inter-zone data transfer costs by keeping traffic within an Availability Zone, and still route traffic to another location when the closest resource is unhealthy. If you haven't created a record for that Availability Zone, or if the record is unhealthy, Amazon Route 53 falls back to a record for a less specific location.

To set up AZ-affinity routing, you create records that have the same name and type, one for each client location that you want to route traffic for. When Route 53 receives a query for an AZ-affinity record set, it responds with the first healthy record in the following order of location types, from most specific to least specific:

1. **Availability Zone** – The Availability Zone that the query comes from. Specify the [AZ ID](https://docs.aws.amazon.com/global-infrastructure/latest/regions/az-ids.html), such as `use1-az1`, not the Availability Zone name, such as `us-east-1a`. An Availability Zone name can map to a different Availability Zone in each AWS account.

1. **Zone Group** – Any Availability Zone in the Zone Group. Specify the Zone Group ID, such as `us-east-1-zg-1`.

1. **Region** – Any Availability Zone in the AWS Region. Specify the AWS Region code, such as `us-east-1`.

1. **Partition** – Any AWS Region in the AWS Partition. Specify the AWS Partition for your account, such as `aws`. Use a Partition record as the fallback for queries from any AWS Region.

1. **Global** – All other queries, such as queries from the internet. Specify `global`. If no record matches where the query comes from and you didn't create a Global record, Route 53 responds with no records (a NOERROR response that contains no answers, also known as NODATA). We recommend that you always create a Global record so that every query gets an answer.

You don't have to create a record for every location type. Route 53 skips a level when you didn't create a record for the location at that level.

You can use AZ-affinity routing for records in both public and private hosted zones. In a private hosted zone, Route 53 responds only to queries from VPCs that you associated with the hosted zone, the same as for other records in private hosted zones.

Route 53 routes each query based on where it comes from:
+ When a resource in a VPC, such as an Amazon EC2 instance, uses Route 53 VPC Resolver to resolve a DNS name, VPC Resolver tells Route 53 which Availability Zone the query comes from. This applies to both public and private hosted zones.
+ Queries that don't come through VPC Resolver match only the Global record. Examples are queries from the internet and queries from DNS resolvers that send queries directly to Route 53 name servers.

For information about values that you specify when you use the AZ-affinity routing policy to create records, see the following topics:
+ [Values specific for AZ-affinity records](resource-record-sets-values-azaffinity.md)
+ [Values specific for AZ-affinity alias records](resource-record-sets-values-azaffinity-alias.md)
+ [Values that are common for all routing policies](resource-record-sets-values-shared.md)
+ [Values that are common for alias records for all routing policies](resource-record-sets-values-alias-common.md)

## Finding AZ IDs and Zone Groups
<a name="routing-policy-azaffinity-locations"></a>

To find the AZ IDs for the Availability Zones in your account, check the **Service health** panel on the Amazon EC2 Dashboard, or use the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) CLI command. On an Amazon EC2 instance in an Availability Zone, you can also get the AZ ID of the instance from the instance metadata item `placement/availability-zone-id`. For more information, see [AZ IDs](https://docs.aws.amazon.com/global-infrastructure/latest/regions/az-ids.html).

To find the Zone Group of each Availability Zone in a Region, run the following command, replacing `us-east-1` with your Region. The output lists the AZ ID and the Zone Group (`GroupName`) of each Availability Zone.

```bash
aws ec2 describe-availability-zones \
    --region us-east-1 \
    --filters Name=zone-type,Values=availability-zone \
    --query "AvailabilityZones[].[ZoneId,GroupName]" \
    --output text
```

For `us-east-1`, the output includes a line that lists `use1-az1` and `us-east-1-zg-1`, which shows that the Availability Zone `use1-az1` is in the Zone Group `us-east-1-zg-1`.

If you omit the `zone-type` filter, the output can also include Local Zones and Wavelength Zones, which AZ-affinity routing doesn't support.

## Health checks and AZ-affinity routing
<a name="routing-policy-azaffinity-healthchecks"></a>

To have Route 53 fall back to a less specific location when a resource is unhealthy, associate a health check with each AZ-affinity record, or, for an alias record, set **Evaluate target health** to **Yes**. If a non-alias record doesn't have a health check, Route 53 always considers the record healthy, which will prevent falling back to a less specific location. If all the records that match where the query comes from are unhealthy, Route 53 responds with the most specific of those records, even though it's unhealthy.

If an AZ-affinity alias record routes traffic to non-alias records in the same hosted zone, also associate health checks with those records (see [Evaluate target health](resource-record-sets-values-azaffinity-alias.md#rrsets-values-azaffinity-alias-evaluate-target-health) in [Values specific for AZ-affinity alias records](resource-record-sets-values-azaffinity-alias.md)).

For more information, see the following topics:
+ [How Amazon Route 53 chooses records when health checking is configured](health-checks-how-route-53-chooses-records.md)
+ [Configuring failover in a private hosted zone](dns-failover-private-hosted-zones.md)
+ [Best practices for Amazon Route 53 DNS](best-practices-dns.md)

## Considerations for AZ-affinity routing
<a name="routing-policy-azaffinity-considerations"></a>

Note the following when you use AZ-affinity routing:
+ **Local Zones, Wavelength Zones, and Outposts** are not supported location types.
+ **Lowercase location IDs** – Location IDs are case sensitive. Specify them in lowercase, for example, `use1-az1`, `us-east-1-zg-1`, `aws`, and `global`.
+ **Not an access control** – AZ-affinity routing chooses which record to respond with, but it doesn't restrict who can get a record. Don't use it to keep a record's value private.
+ **Traffic Flow** – AZ-affinity routing isn't supported in traffic policies.
+ **Testing** – The DNS checking tool in the Route 53 console and the `TestDNSAnswer` API don't support AZ-affinity records. To test your configuration, run a command such as `dig` from Amazon EC2 instances in the Availability Zones that you created records for. Send the queries to VPC Resolver (the default DNS server for the VPC), not directly to the Route 53 name servers for the hosted zone.