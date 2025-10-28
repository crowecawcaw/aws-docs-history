# Values specific for geoproximity

records

When you create geoproximity records, you specify the following values.

###### Topics

- [Routing policy](#rrsets-values-geoprox-routing-policy "#rrsets-values-geoprox-routing-policy")
- [Record name](#rrsets-values-geoprox-name "#rrsets-values-geoprox-name")
- [Record type](#rrsets-values-geoprox-type "#rrsets-values-geoprox-type")
- [TTL (seconds)](#rrsets-values-geoprox-ttl "#rrsets-values-geoprox-ttl")
- [Value/Route traffic to](#rrsets-values-geoprox-value "#rrsets-values-geoprox-value")
- [Endpoint location](#rrsets-values-geoprox-endpoint-location "#rrsets-values-geoprox-endpoint-location")
- [Bias](#rrsets-values-geoprox-bias "#rrsets-values-geoprox-bias")
- [Health check](#rrsets-values-geoprox-associate-with-health-check "#rrsets-values-geoprox-associate-with-health-check")
- [Record ID](#rrsets-values-geoprox-set-id "#rrsets-values-geoprox-set-id")

## Routing policy

Choose **Geoproximity**.

## Record name

Enter the name of the domain or subdomain that you want to route traffic for. The
default value is the name of the hosted zone.

###### Note

If you're creating a record that has the same name as the hosted zone, don't enter
a value (for example, an @ symbol) in the **Name** field.

Enter the same name for all of the records in the group of geoproximity records.

For more information about record names,
see [Record name](resource-record-sets-values-shared.md#rrsets-values-common-name "resource-record-sets-values-shared.md#rrsets-values-common-name").

## Record type

The DNS record type. For more information, see [Supported DNS record types](ResourceRecordTypes.md "ResourceRecordTypes.md").

Select the same value for all of the records in the group of geoproximity
records.

## TTL (seconds)

The amount of time, in seconds, that you want DNS recursive resolvers to cache
information about this record. If you specify a longer value (for example, 172800
seconds, or two days), you reduce the number of calls that DNS recursive resolvers must
make to Route 53 to get the latest information in this record. This has the effect of
reducing latency and reducing your bill for Route 53 service. For more information, see
[How Amazon Route 53 routes traffic for your domain](welcome-dns-service.md#welcome-dns-service-how-route-53-routes-traffic "welcome-dns-service.md#welcome-dns-service-how-route-53-routes-traffic").

However, if you specify a longer value for TTL, it takes longer for changes to the
record (for example, a new IP address) to take effect because recursive resolvers use
the values in their cache for longer periods before they ask Route 53 for the latest
information. If you're changing settings for a domain or subdomain that's already in
use, we recommend that you initially specify a shorter value, such as 300 seconds, and
increase the value after you confirm that the new settings are correct.

If you're associating this record with a health check, we recommend that you specify a
TTL of 60 seconds or less so clients respond quickly to changes in health status.

## Value/Route traffic to

Choose **IP address or another value depending on the record type**.
Enter a value that is appropriate for the value of **Record type**. For
all types except **CNAME**, you can enter more than one value. Enter
each value on a separate line.

You can route traffic to, or specify the following values:

- **A — IPv4 address**
- **AAAA — IPv6 address**
- **CAA — Certificate Authority Authorization**
- **CNAME — Canonical name**
- **MX — Mail exchange**
- **NAPTR — Name Authority Pointer**
- **PTR — Pointer**
- **SPF — Sender Policy Framework**
- **SRV — Service locator**
- **TXT — Text**

For more information about the above values, see [common values for Value/Route traffic to](resource-record-sets-values-shared.md#rrsets-values-common-value "resource-record-sets-values-shared.md#rrsets-values-common-value").

## Endpoint location

You can specify the resource endpoint location by using one of the following:

**Custom coordinates**
Specify the longitude and lattitude for a geopgraphic area.

**AWS Region**
Choose an available Region from the **Location** list.

For more information about the Regions, see
[AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

**AWS Local Zone Group**
Choose an available Local Zone Group from the **Location** list.

For more information about Local Zones, see
[Available Local Zones](../../../local-zones/latest/ug/available-local-zones.md "../../../local-zones/latest/ug/available-local-zones.md") in the
_AWS Local Zones User Guide_. A local Zone Group is usually the Local Zone without the ending character. For example,
if the Local Zone is `us-east-1-bue-1a` the Local Zone Group is `us-east-1-bue-1`.

You can also identify the Local Zones Group for a specific Local Zone by using the [describe-availability-zones](../../../cli/latest/reference/ec2/describe-availability-zones.md "../../../cli/latest/reference/ec2/describe-availability-zones.md") CLI command:

```
aws ec2 describe-availability-zones --region us-west-2 --all-availability-zones --query "AvailabilityZones[?ZoneName=='us-west-2-den-1a']" | grep "GroupName"
```

This command returns: `"GroupName": "us-west-2-den-1"`, specifying that the Local Zone `us-west-2-den-1a`
belongs to the Local Zone Group `us-west-2-den-1`.

You can't create non-geoproximity records that have the same values for
**Record name** and **Record type** as geoproximity
records.

You also can't create two geoproximity resource record sets that specify the same location for the same record name and record type.

## Bias

A bias either expands or shrinks a geographic area from which Route 53 routes traffic to a resource.
A positive bias expands the area, and a negative bias shrinks it. For more information, see
[How Amazon Route 53 uses bias to route traffic](routing-policy-geoproximity.md#routing-policy-geoproximity-bias "routing-policy-geoproximity.md#routing-policy-geoproximity-bias").

## Health check

Select a health check if you want Route 53 to check the health of a specified endpoint
and to respond to DNS queries using this record only when the endpoint is healthy.

Route 53 doesn't check the health of the endpoint specified in the record, for example,
the endpoint specified by the IP address in the **Value** field. When
you select a health check for a record, Route 53 checks the health of the endpoint that you
specified in the health check. For information about how Route 53 determines whether an
endpoint is healthy, see [How Amazon Route 53 determines
whether a health check is healthy](dns-failover-determining-health-of-endpoints.md "dns-failover-determining-health-of-endpoints.md").

Associating a health check with a record is useful only when Route 53 is choosing between
two or more records to respond to a DNS query, and you want Route 53 to base the choice in
part on the status of a health check. Use health checks only in the following
configurations:

- You're checking the health of all of the records in a group of records that
  have the same name, type, and routing policy (such as failover or weighted
  records), and you specify health check IDs for all the records. If the health
  check for a record specifies an endpoint that is not healthy, Route 53 stops
  responding to queries using the value for that record.
- You select **Yes** for **Evaluate Target
  Health** for an alias record or the records in a group of failover
  alias, geolocation alias, geoproximity alias, latency alias,
  IP-based
  alias, or weighted alias record. If the alias records
  reference non-alias records in the same hosted zone, you must also specify
  health checks for the referenced records. If you associate a health check with
  an alias record and also select **Yes** for **Evaluate
  Target Health**, both must evaluate to true. For more information,
  see [What happens when you associate a health check with an alias record?](dns-failover-complex-configs.md#dns-failover-complex-configs-hc-alias "dns-failover-complex-configs.md#dns-failover-complex-configs-hc-alias").

If your health checks specify the endpoint only by domain name, we recommend that you
create a separate health check for each endpoint. For example, create a health check for
each HTTP server that is serving content for www.example.com. For the value of
**Domain Name**, specify the domain name of the server (such as
us-east-2-www.example.com), not the name of the records (example.com).

###### Important

In this configuration, if you create a health check for which the value of
**Domain Name** matches the name of the records and then
associate the health check with those records, health check results will be
unpredictable.

For geoproximity records, if an endpoint is unhealthy, Route 53 looks for a closest endpoint that is still healthy.

## Record ID

Enter a value that uniquely identifies this record in the group of geoproximity
records.
