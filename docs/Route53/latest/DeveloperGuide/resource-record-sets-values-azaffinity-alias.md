

# Values specific for AZ-affinity alias records

When you create AZ-affinity alias records, you specify the following values. For more information, see [Choosing between alias and non-alias records](resource-record-sets-choosing-alias-non-alias.md) and [AZ-affinity routing](routing-policy-azaffinity.md).

**Topics**
+ [Routing policy](#rrsets-values-azaffinity-alias-routing-policy)
+ [Record name](#rrsets-values-azaffinity-alias-name)
+ [Record type](#rrsets-values-azaffinity-alias-type)
+ [Value/Route traffic to](#rrsets-values-azaffinity-alias-alias-target)
+ [Location type](#rrsets-values-azaffinity-alias-location-type)
+ [Health check](#rrsets-values-azaffinity-alias-associate-with-health-check)
+ [Evaluate target health](#rrsets-values-azaffinity-alias-evaluate-target-health)
+ [Record ID](#rrsets-values-azaffinity-alias-set-identifier)

## Routing policy
<a name="rrsets-values-azaffinity-alias-routing-policy"></a>

Choose **AZ affinity**.

## Record name
<a name="rrsets-values-azaffinity-alias-name"></a>

Enter the name of the domain or subdomain that you want to route traffic for. The default value is the name of the hosted zone. 

**Note**  
If you're creating a record that has the same name as the hosted zone, don't enter a value (for example, an @ symbol) in the **Record name** field. 

Enter the same name for all of the records in the group of AZ-affinity records. 

For more information about record names, see [Record name](resource-record-sets-values-alias-common.md#rrsets-values-common-alias-name).

## Record type
<a name="rrsets-values-azaffinity-alias-type"></a>

The DNS record type. For more information, see [Supported DNS record types](ResourceRecordTypes.md).

Select the applicable value based on the AWS resource that you're routing traffic to. If you're routing traffic to another record in this hosted zone, select the type of that record. All types are supported except **NS** and **SOA**.

Select the same value for all of the records in the group of AZ-affinity records.

## Value/Route traffic to
<a name="rrsets-values-azaffinity-alias-alias-target"></a>

The value that you choose from the list or that you type in the field depends on the AWS resource that you're routing traffic to. You can route traffic to an AWS resource or to another record in this hosted zone. You can't route traffic to a record in a different hosted zone.

For information about what AWS resources you can target, see [common values for alias records for value/route traffic to](resource-record-sets-values-alias-common.md#rrsets-values-alias-common-target).

For more information about how to configure Route 53 to route traffic to specific AWS resources, see [Routing internet traffic to your AWS resources](routing-to-aws-resources.md).

## Location type
<a name="rrsets-values-azaffinity-alias-location-type"></a>

The level of the AWS location hierarchy that this record answers for: **Availability Zone**, **Zone Group**, **Region**, **Partition**, or **Global**. You specify the same values as for non-alias AZ-affinity records. For more information, see [Location type](resource-record-sets-values-azaffinity.md#rrsets-values-azaffinity-location-type).

If the matching record is unhealthy, Route 53 falls back to the record for the next less specific location that you created a record for, which contains the query's Availability Zone: its Zone Group, its Region, its partition, and then Global. For an alias record, Route 53 treats the record as unhealthy because of the alias target only if you set **Evaluate target health** to **Yes**. For more information, see [Evaluate target health](#rrsets-values-azaffinity-alias-evaluate-target-health).

You can't create non-AZ-affinity records that have the same values for **Record name** and **Record type** as AZ-affinity records.

## Health check
<a name="rrsets-values-azaffinity-alias-associate-with-health-check"></a>

Select a health check if you want Route 53 to check the health of a specified endpoint and to respond to DNS queries using this record only when the endpoint is healthy. 

For alias records, we recommend that you set **Evaluate target health** to **Yes** instead of associating a health check with the alias record. If you associate a health check with an alias record and also select **Yes** for **Evaluate target health**, both must evaluate to true. If the alias record references non-alias records in the same hosted zone, associate health checks with the referenced records. For more information, see [What happens when you associate a health check with an alias record?](dns-failover-complex-configs.md#dns-failover-complex-configs-hc-alias).

Route 53 doesn't check the health of the endpoint specified in the record. When you select a health check for a record, Route 53 checks the health of the endpoint that you specified in the health check. For information about how Route 53 determines whether an endpoint is healthy, see [How Amazon Route 53 determines whether a health check is healthy](dns-failover-determining-health-of-endpoints.md).

## Evaluate target health
<a name="rrsets-values-azaffinity-alias-evaluate-target-health"></a>

Select **Yes** if you want Route 53 to determine whether to respond to DNS queries using this record by checking the health of the alias target. If the alias target is unhealthy, Route 53 falls back to the record for the next less specific location.

If you select **No**, Route 53 doesn't check the health of the alias target, so it doesn't fall back past this record when the alias target is unhealthy. If you also associate a health check with this record, Route 53 falls back when that health check is unhealthy.

If the alias target is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see [What happens when you omit health checks?](dns-failover-complex-configs.md#dns-failover-complex-configs-hc-omitting).

Some AWS resources have special requirements for **Evaluate target health**. For more information, see `EvaluateTargetHealth` in [AliasTarget](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html) in the *Amazon Route 53 API Reference*.

## Record ID
<a name="rrsets-values-azaffinity-alias-set-identifier"></a>

Enter a value that uniquely identifies this record in the group of AZ-affinity records, such as a timestamp or a sequential number.