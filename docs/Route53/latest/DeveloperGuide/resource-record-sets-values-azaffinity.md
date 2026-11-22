

# Values specific for AZ-affinity records

When you create AZ-affinity records, you specify the following values. For more information, see [AZ-affinity routing](routing-policy-azaffinity.md).

**Topics**
+ [Routing policy](#rrsets-values-azaffinity-routing-policy)
+ [Record name](#rrsets-values-azaffinity-name)
+ [Record type](#rrsets-values-azaffinity-type)
+ [TTL (seconds)](#rrsets-values-azaffinity-ttl)
+ [Value/Route traffic to](#rrsets-values-azaffinity-value)
+ [Location type](#rrsets-values-azaffinity-location-type)
+ [Health check](#rrsets-values-azaffinity-associate-with-health-check)
+ [Record ID](#rrsets-values-azaffinity-set-identifier)

## Routing policy
<a name="rrsets-values-azaffinity-routing-policy"></a>

Choose **AZ affinity**.

## Record name
<a name="rrsets-values-azaffinity-name"></a>

Enter the name of the domain or subdomain that you want to route traffic for. The default value is the name of the hosted zone. 

**Note**  
If you're creating a record that has the same name as the hosted zone, don't enter a value (for example, an @ symbol) in the **Record name** field. 

Enter the same name for all of the records in the group of AZ-affinity records. 

For more information about record names, see [Record name](resource-record-sets-values-shared.md#rrsets-values-common-name).

## Record type
<a name="rrsets-values-azaffinity-type"></a>

The DNS record type. For more information, see [Supported DNS record types](ResourceRecordTypes.md).

Select the same value for all of the records in the group of AZ-affinity records.

## TTL (seconds)
<a name="rrsets-values-azaffinity-ttl"></a>

The amount of time, in seconds, that you want DNS recursive resolvers to cache information about this record. If you specify a longer value (for example, 172800 seconds, or two days), you reduce the number of calls that DNS recursive resolvers must make to Route 53. This reduces latency and lowers your bill for Route 53 service. For more information, see [How Amazon Route 53 routes traffic for your domain](welcome-dns-service.md#welcome-dns-service-how-route-53-routes-traffic).

However, if you specify a longer value for TTL, it takes longer for changes to the record (for example, a new IP address) to take effect, and it takes longer for clients to stop using a record that Route 53 has stopped responding with because it's unhealthy.

If you're associating this record with a health check, see [Best practices for Amazon Route 53 DNS](best-practices-dns.md) for TTL recommendations.

Specify the same value for **TTL** for all of the records in this group of AZ-affinity records.

## Value/Route traffic to
<a name="rrsets-values-azaffinity-value"></a>

Choose **IP address or another value depending on the record type**. Enter a value that is appropriate for the value of **Record type**. For all types except **CNAME**, you can enter more than one value. Enter each value on a separate line.

You can route traffic to, or specify the following values:
+ **A — IPv4 address**
+ **AAAA — IPv6 address**
+ **CAA — Certificate Authority Authorization**
+ **CNAME — Canonical name**
+ **MX — Mail exchange**
+ **NAPTR — Name Authority Pointer**
+ **PTR — Pointer**
+ **SPF — Sender Policy Framework**
+ **SRV — Service locator**
+ **TXT — Text**

For more information about the above values, see [common values for Value/Route traffic to](resource-record-sets-values-shared.md#rrsets-values-common-value).

To route traffic to an AWS resource, create an AZ-affinity alias record instead. For more information, see [Values specific for AZ-affinity alias records](resource-record-sets-values-azaffinity-alias.md).

## Location type
<a name="rrsets-values-azaffinity-location-type"></a>

The level of the AWS location hierarchy that this record answers for. Route 53 responds to each query with the most specific record that matches where the query comes from. Choose one of the following values, listed from most specific to least specific:

****Availability Zone****  
Answers queries from one Availability Zone. Specify the AZ ID, such as `use1-az1`, not the Availability Zone name, such as `us-east-1a`.

****Zone Group****  
Answers queries from any Availability Zone in a Zone Group, such as `us-east-1-zg-1`. You can specify only Zone Groups of Availability Zones, not Zone Groups of Local Zones or Wavelength Zones.

****Region****  
Answers queries from any Availability Zone in a Region, such as `us-east-1`.

****Partition****  
Answers queries from any AWS Region. Use it as the fallback for queries that come from AWS, and use a Global record for queries from the internet. In the API, specify `Partition` for `LocationType` and the partition name in lowercase, such as `aws`, for `LocationId`.

****Global****  
Answers all other queries, such as queries from the internet. We recommend that you always create a Global record so that every query gets an answer. If no record matches a query and you didn't create a Global record, Route 53 responds with no answer (NODATA).

If the matching record is unhealthy, Route 53 falls back to the record for the next less specific location that you created a record for, which contains the query's Availability Zone: its Zone Group, its Region, its partition, and then Global.

You also choose a location that the record answers for. In the console, you choose the location from a list. In the API, you specify a location ID. For the ID formats, see [AZ-affinity routing](routing-policy-azaffinity.md). To find the AZ IDs and Zone Groups for your account, see [Finding AZ IDs and Zone Groups](routing-policy-azaffinity.md#routing-policy-azaffinity-locations).

You can't create non-AZ-affinity records that have the same values for **Record name** and **Record type** as AZ-affinity records.

## Health check
<a name="rrsets-values-azaffinity-associate-with-health-check"></a>

Select a health check if you want Route 53 to check the health of a specified endpoint and to respond to DNS queries using this record only when the endpoint is healthy. When the endpoint is unhealthy, Route 53 falls back to the record for the next less specific location.

If you don't select a health check, Route 53 always considers the record healthy and doesn't fall back past it to a less specific record. We recommend that you associate a health check with each AZ-affinity record.

Route 53 doesn't check the health of the endpoint specified in the record, for example, the endpoint specified by the IP address in the **Value** field. When you select a health check for a record, Route 53 checks the health of the endpoint that you specified in the health check. For information about how Route 53 determines whether an endpoint is healthy, see [How Amazon Route 53 determines whether a health check is healthy](dns-failover-determining-health-of-endpoints.md).

If your health checks specify the endpoint only by domain name, create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of **Domain name**, specify the domain name of the server (such as us-east-2-www.example.com), not the name of the records (example.com).

**Important**  
In this configuration, if you create a health check for which the value of **Domain name** matches the name of the records and then associate the health check with those records, health check results will be unpredictable.

## Record ID
<a name="rrsets-values-azaffinity-set-identifier"></a>

Enter a value that uniquely identifies this record in the group of AZ-affinity records, such as a timestamp or a sequential number.