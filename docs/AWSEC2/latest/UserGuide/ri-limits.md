# Reserved Instance quotas

You can purchase new Reserved Instances each month. The number of new Reserved Instances that you can purchase
each month is determined by your monthly quota, as follows:

| Quota description                                                                                | Default quota                      |
| ------------------------------------------------------------------------------------------------ | ---------------------------------- |
| New [regional](apply_ri.md#apply-regional-ri "apply_ri.md#apply-regional-ri") Reserved Instances | 20 per Region per month            |
| New [zonal](apply_ri.md#apply-zonal-ri "apply_ri.md#apply-zonal-ri") Reserved Instances          | 20 per Availability Zone per month |

For example, in a Region with three Availability Zones, the default quota is 80 new
Reserved Instances per month, calculated as follows:

- 20 regional Reserved Instances for the Region
- Plus 60 zonal Reserved Instances (20 for each of the three Availability Zones)
  Instances in the `running` state count toward your quota. Instances that
  are in the `pending`, `stopping`, `stopped`, and
  `hibernated` states do not count towards your quota.

## View the number of

Reserved Instances you have purchased

The number of Reserved Instances that you purchase is indicated by the **Instance
count** field (console) or the `InstanceCount` parameter
(AWS CLI). When you purchase new Reserved Instances, the quota is measured against the total
instance count. For example, if you purchase a single Reserved Instance configuration with an
instance count of 10, the purchase counts towards your quota as 10, not 1.

You can view how many Reserved Instances you have purchased by using the Amazon EC2 or the
AWS CLI.

Console

###### To view the number of Reserved Instances you have purchased

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Reserved Instances**.
3. Select a Reserved Instance configuration from the table, and check the
   **Instance count** field.

In the following screenshot, the selected line represents a
single Reserved Instance configuration for a `t3.micro` instance
type. The **Instance count** column in the
table view and the **Instance count** field in
the detail view (outlined in the screenshot) indicate that there
are 10 Reserved Instances for this configuration.

![This image shows the Reserved Instances screen in the Amazon EC2 console. The Instance count field is outlined in the screenshot.](images/ri-instance-count.png)

AWS CLI

###### To view the number of Reserved Instances you have purchased

Use the [describe-reserved-instances](../../../cli/latest/reference/ec2/describe-reserved-instances.md "../../../cli/latest/reference/ec2/describe-reserved-instances.md") command and specify the ID
of the Reserved Instance configuration.

```
aws ec2 describe-reserved-instances \
    --reserved-instances-ids `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
    --output table
```

The following is example output. The `InstanceCount` field
indicates that there are 10 Reserved Instances for this configuration.

```
-------------------------------------------------------------------
|                    DescribeReservedInstances                    |
+-----------------------------------------------------------------+
||                       ReservedInstances                       ||
|+----------------------+----------------------------------------+|
||  CurrencyCode        |  USD                                   ||
||  Duration            |  31536000                              ||
||  End                 |  2023-08-27T13:29:44+00:00             ||
||  FixedPrice          |  59.0                                  ||
||  **InstanceCount**       |  **10**                                    ||
||  InstanceTenancy     |  default                               ||
||  InstanceType        |  t3.micro                              ||
||  OfferingClass       |  standard                              ||
||  OfferingType        |  All Upfront                           ||
||  ProductDescription  |  Linux/UNIX                            ||
||  ReservedInstancesId |  a1b2c3d4-5678-90ab-cdef-EXAMPLE11111  ||
||  Scope               |  Region                                ||
||  Start               |  2022-08-27T13:29:45.938000+00:00      ||
||  State               |  active                                ||
||  UsagePrice          |  0.0                                   ||
|+----------------------+----------------------------------------+|
|||                      RecurringCharges                       |||
||+----------------------------------+--------------------------+||
|||  Amount                          |  0.0                     |||
|||  Frequency                       |  Hourly                  |||
||+----------------------------------+--------------------------+||
```

PowerShell

###### To view the number of Reserved Instances you have purchased

Use the [Get-EC2ReservedInstance](../../../powershell/latest/reference/items/Get-EC2ReservedInstance.md "../../../powershell/latest/reference/items/Get-EC2ReservedInstance.md") Cmdlet and specify the ID of
the Reserved Instance configuration.

```
Get-EC2ReservedInstance -ReservedInstancesId `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

The following is example output. The `InstanceCount` field
indicates that there are 10 Reserved Instances for this configuration.

```
AvailabilityZone    :
CurrencyCode        : USD
Duration            : 31536000
End                 : 1/12/2017 8:57:08 PM
FixedPrice          : 0
**InstanceCount**       : **10**
InstanceTenancy     : default
InstanceType        : t3.medium
OfferingClass       : standard
OfferingType        : All Upfront
ProductDescription  : Windows
RecurringCharges    : {}
ReservedInstancesId : a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
Scope               : Region
Start               : 10/12/2016 4:00:00 PM
State               : active
Tags                : {}
UsagePrice          : 0
```

## Considerations

A regional Reserved Instance applies a discount to a running On-Demand Instance. The default On-Demand Instance limit is 20. You cannot exceed your running On-Demand Instance limit by purchasing regional Reserved Instances. For
example, if you already have 20 running On-Demand Instances, and you purchase 20 regional Reserved Instances,
the 20 regional Reserved Instances are used to apply a discount to the 20 running On-Demand Instances. If you
purchase more regional Reserved Instances, you will not be able to launch more instances because
you have reached your On-Demand Instance limit.

Before purchasing regional Reserved Instances, make sure your On-Demand Instance limit matches or exceeds
the number of regional Reserved Instances you intend to own. If required, make sure you request
an increase to your On-Demand Instance limit _before_ purchasing
more regional Reserved Instances.

A zonal Reserved Instance—a Reserved Instance that is purchased for a specific Availability
Zone—provides a capacity reservation as well as a discount. You _can exceed_ your running On-Demand Instance limit by purchasing zonal
Reserved Instances. For example, if you already have 20 running On-Demand Instances, and you purchase 20 zonal
Reserved Instances, you can launch a further 20 On-Demand Instances that match the specifications of your
zonal Reserved Instances, giving you a total of 40 running instances.

## View your Reserved Instance quotas and request a quota

increase

The Amazon EC2 console provides quota information. You can also request an increase in
your quotas. For more information, see [View your current quotas](ec2-resource-limits.md#view-limits "ec2-resource-limits.md#view-limits") and [Request an increase](ec2-resource-limits.md#request-increase "ec2-resource-limits.md#request-increase").
