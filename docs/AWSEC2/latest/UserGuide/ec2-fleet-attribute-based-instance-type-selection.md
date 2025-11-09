# Specify attributes for

instance type selection for EC2 Fleet or Spot Fleet

When you create an EC2 Fleet or Spot Fleet, you must specify one or more instance types for
configuring the On-Demand Instances and Spot Instances in the fleet. As an alternative to manually specifying the
instance types, you can specify the attributes that an instance must have, and Amazon EC2 will
identify all the instance types with those attributes. This is known as _attribute-based instance type selection_. For example, you can
specify the minimum and maximum number of vCPUs required for your instances, and the fleet
will launch the instances using any available instance types that meet those vCPU
requirements.

Attribute-based instance type selection is ideal for workloads and frameworks that can be flexible about what instance types
they use, such as when running containers or web ﬂeets, processing big data, and
implementing continuous integration and deployment (CI/CD) tooling.

**Benefits**

Attribute-based instance type selection has the following benefits:

- **Easily use the right instance types** – With
  so many instance types available, finding the right instance types for your workload
  can be time consuming. When you specify instance attributes, the instance types will
  automatically have the required attributes for your workload.
- **Simplified configuration** – To manually
  specify multiple instance types for a fleet, you must create a separate launch
  template override for each instance type. But with attribute-based instance type selection, to provide multiple
  instance types, you need only specify the instance attributes in the launch template
  or in a launch template override.
- **Automatic use of new instance types** – When
  you specify instance attributes rather than instance types, your fleet can use newer
  generation instance types as they’re released, "future proofing" the fleet's
  configuration.
- **Instance type flexibility** – When you
  specify instance attributes rather than instance types, the fleet can select from a
  wide range of instance types for launching Spot Instances, which adheres to the
  [Spot best practice of instance type
  flexibility](spot-best-practices.md#be-instance-type-flexible "spot-best-practices.md#be-instance-type-flexible").

###### Topics

- [How attribute-based instance type selection works](#ec2fleet-abs-how-it-works "#ec2fleet-abs-how-it-works")
- [Price protection](#ec2fleet-abs-price-protection "#ec2fleet-abs-price-protection")
- [Performance protection](#ec2fleet-abis-performance-protection "#ec2fleet-abis-performance-protection")
- [Considerations](#ec2fleet-abs-considerations "#ec2fleet-abs-considerations")
- [Create an EC2 Fleet with attribute-based instance type selection](#abs-create-ec2-fleet "#abs-create-ec2-fleet")
- [Create a Spot Fleet with attribute-based instance type selection](#abs-create-spot-fleet "#abs-create-spot-fleet")
- [Examples of EC2 Fleet configurations that are
  valid and not valid](#ec2fleet-abs-example-configs "#ec2fleet-abs-example-configs")
- [Examples of Spot Fleet configurations that are
  valid and not valid](#spotfleet-abs-example-configs "#spotfleet-abs-example-configs")
- [Preview
  instance types with specified attributes](#ec2fleet-get-instance-types-from-instance-requirements "#ec2fleet-get-instance-types-from-instance-requirements")

## How attribute-based instance type selection works

To use attribute-based instance type selection in your fleet configuration, you replace the list of instance types with
a list of instance attributes that your instances require. EC2 Fleet or Spot Fleet will launch
instances on any available instance types that have the specified instance
attributes.

###### Topics

- [Types of instance
  attributes](#ef-abs-instance-attribute-types "#ef-abs-instance-attribute-types")
- [Where to configure attribute-based instance type selection](#ef-abs-where-to-configure "#ef-abs-where-to-configure")
- [How EC2 Fleet or Spot Fleet uses attribute-based instance type selection when provisioning a
  fleet](#how-ef-uses-abs "#how-ef-uses-abs")

### Types of instance

attributes

There are several instance attributes that you can specify to express your compute
requirements, such as:

- **vCPU count** – The minimum and
  maximum number of vCPUs per instance.
- **Memory** – The minimum and maximum
  GiBs of memory per instance.
- **Local storage** – Whether to use EBS
  or instance store volumes for local storage.
- **Burstable performance** – Whether to
  use the T instance family, including T4g, T3a, T3, and T2 types.

For a description of each attribute and the default values, see [InstanceRequirements](../APIReference/API_InstanceRequirements.md "../APIReference/API_InstanceRequirements.md") in the _Amazon EC2 API Reference_.

### Where to configure attribute-based instance type selection

Depending on whether you use the console or the AWS CLI, you can specify the
instance attributes for attribute-based instance type selection as follows:

In the console, you can specify the instance attributes in the following fleet
configuration components:

- In a launch template, and then reference the launch template in the fleet
  request
- (Spot Fleet only) In the fleet request

In the AWS CLI, you can specify the instance attributes in one or all of the
following fleet configuration components:

- In a launch template, and then reference the launch template in the fleet
  request
- In a launch template override

If you want a mix of instances that use different AMIs, you can specify
instance attributes in multiple launch template overrides. For example,
different instance types can use x86 and Arm-based processors.

- (Spot Fleet only) In a launch specification

### How EC2 Fleet or Spot Fleet uses attribute-based instance type selection when provisioning a

fleet

EC2 Fleet or Spot Fleet provisions a fleet in the following way:

- It identifies the instance types that have the specified
  attributes.
- It uses price protection to determine which instance types to
  exclude.
- It determines the capacity pools from which it will consider launching the
  instances based on the AWS Regions or Availability Zones that have
  matching instance types.
- It applies the specified allocation strategy to determine from which
  capacity pools to launch the instances.

Note that attribute-based instance type selection does not pick the capacity pools from which to provision
the fleet; that's the job of the [allocation
strategies](ec2-fleet-allocation-strategy.md "ec2-fleet-allocation-strategy.md").

If you specify an allocation strategy, the fleet will launch instances
according to the specified allocation strategy.

    + For Spot Instances, attribute-based instance type selection supports the **price capacity
     optimized**, **capacity optimized**,
     and **lowest price** allocation strategies. Note
     that we don't recommend the **lowest price** Spot
     allocation strategy because it has the highest risk of interruption
     for your Spot Instances.
    + For On-Demand Instances, attribute-based instance type selection supports the **lowest price**
     allocation strategy.

- If there is no capacity for the instance types with the specified instance
  attributes, no instances can be launched, and the fleet returns an
  error.

## Price protection

Price protection is a feature that prevents your EC2 Fleet or Spot Fleet from using instance
types that you would consider too expensive even if they happen to fit the attributes
that you specified. To use price protection, you set a price threshold. Then, when Amazon EC2
selects instance types with your attributes, it excludes instance types priced above
your threshold.

The way that Amazon EC2 calculates the price threshold is as follows:

- Amazon EC2 first identifies the lowest priced instance type from those that match
  your attributes.
- Amazon EC2 then takes the value (expressed as a percentage) that you specified for
  the price protection parameter and multiplies it with the price of the
  identified instance type. The result is the price that is used as the price
  threshold.

There are separate price thresholds for On-Demand Instances and Spot Instances.

When you create a fleet with attribute-based instance type selection, price protection is enabled by default. You can
keep the default values, or you can specify your own.

You can also turn off price protection. To indicate no price protection threshold,
specify a high percentage value, such as `999999`.

###### Topics

- [How the lowest priced
  instance type is identified](#ec2fleet-abs-price-protection-lowest-priced "#ec2fleet-abs-price-protection-lowest-priced")
- [On-Demand Instance price
  protection](#ec2fleet-abs-on-demand-price-protection "#ec2fleet-abs-on-demand-price-protection")
- [Spot Instance price protection](#ec2fleet-abs-spot-price-protection "#ec2fleet-abs-spot-price-protection")
- [Specify the price protection
  threshold](#ec2fleet-abs-specify-price-protection "#ec2fleet-abs-specify-price-protection")

### How the lowest priced

instance type is identified

Amazon EC2 determines the price to base the price threshold on by identifying the
instance type with the lowest price from those that match your specified attributes.
It does this in the following way:

- It first looks at the current generation C, M, or R instance types that
  match your attributes. If it finds any matches, it identifies the lowest
  priced instance type.
- If there is no match, it then looks at any current generation instance
  types that match your attributes. If it finds any matches, it identifies the
  lowest priced instance type.
- If there is no match, it then looks at any previous generation instance
  types that match your attributes, and identifies the lowest priced instance
  type.

### On-Demand Instance price

protection

The price protection threshold for On-Demand instance types is calculated
_as a percentage higher_ than the identified
lowest priced On-Demand instance type
(`OnDemandMaxPricePercentageOverLowestPrice`). You specify the
percentage higher that you're willing to pay. If you don't specify this parameter,
then a default value of `20` is used to calculate a price protection
threshold of 20% higher than the identified price.

For example, if the identified On-Demand instance price is `0.4271`,
and you specify `25`, then the price threshold is 25% more than
`0.4271`. It is calculated as follows: `0.4271 * 1.25 =
 0.533875`. The calculated price is the maximum you're willing to pay for
On-Demand Instances, and, in this example, Amazon EC2 will exclude any On-Demand instance types that
cost more than `0.533875`.

### Spot Instance price protection

By default, Amazon EC2 will automatically apply optimal Spot Instance price protection to
consistently select from a wide range of instance types. You can also manually set
the price protection yourself. However, letting Amazon EC2 do it for you can improve the
likelihood that your Spot capacity is fulfilled.

You can manually specify the price protection using one of the following options.
If you manually set the price protection, we recommend using the first
option.

- **A _percentage of_
  the identified lowest priced _On-Demand_ instance type**
  [`MaxSpotPriceAsPercentageOfOptimalOnDemandPrice`]

For example, if the identified On-Demand instance type price is
`0.4271`, and you specify `60`, then the price
threshold is 60% of `0.4271`. It is calculated as follows:
`0.4271 * 0.60 = 0.25626`. The calculated price is the
maximum you're willing to pay for Spot Instances, and, in this example, Amazon EC2 will
exclude any Spot instance types that cost more than
`0.25626`.

- **A _percentage higher
  than_ the identified lowest priced _Spot_ instance type**
  [`SpotMaxPricePercentageOverLowestPrice`]

For example, if the identified Spot instance type price is
`0.1808`, and you specify `25`, then the price
threshold is 25% more than `0.1808`. It is calculated as follows:
`0.1808 * 1.25 = 0.226`. The calculated price is the maximum
you're willing to pay for Spot Instances, and, in this example, Amazon EC2 will exclude
any Spot instance types that cost more than `0.266`. We do not
recommend using this parameter because Spot prices can fluctuate, and
therefore your price protection threshold might also fluctuate.

### Specify the price protection

threshold

###### To specify the price protection threshold using the AWS CLI

While creating an EC2 Fleet or Spot Fleet using the AWS CLI, configure the fleet for
attribute-based instance type selection, and then do the following:

- To specify the On-Demand Instance price protection threshold, in the JSON configuration
  file, in the `InstanceRequirements` structure, for
  `OnDemandMaxPricePercentageOverLowestPrice`, enter the price
  protection threshold as a percentage.
- To specify the Spot Instance price protection threshold, in the JSON configuration
  file, in the `InstanceRequirements` structure, specify _one_ of the following parameters:
  - For `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice`,
    enter the price protection threshold as a percentage.
  - For `SpotMaxPricePercentageOverLowestPrice`, enter the
    price protection threshold as a percentage.

For more information, see [Create an EC2 Fleet with attribute-based instance type selection](#abs-create-ec2-fleet "#abs-create-ec2-fleet") or [Create a Spot Fleet with attribute-based instance type selection](#abs-create-spot-fleet "#abs-create-spot-fleet").

###### (Spot Fleet only) To specify the price protection threshold using the

console

While creating a Spot Fleet in the console, configure the fleet for attribute-based
instance type selection, and then do the following:

- To specify the On-Demand Instance price protection threshold, under
  **Additional instance attribute**, choose
  **On-demand price protection**, choose **Add
  attribute**, and then enter the price protection threshold as a
  percentage.
- To specify the Spot Instance price protection threshold, **Additional
  instance attribute**, choose **Spot price
  protection**, choose **Add attribute**, choose
  a base value on which to base your price, and then enter the price
  protection threshold as a percentage.

###### Note

When creating the fleet, if you set `TargetCapacityUnitType` to
`vcpu` or `memory-mib`, the price protection threshold
is applied based on the per-vCPU or per-memory price instead of the per-instance
price.

## Performance protection

_Performance protection_ is a feature that ensures
your EC2 Fleet or Spot Fleet uses instance types that are similar to or exceed a specified
performance baseline. To use performance protection, you specify an instance family as a
baseline reference. The capabilities of the specified instance family establish the
lowest acceptable level of performance. When Amazon EC2 selects instance types for your
fleet, it considers your specified attributes and the performance baseline. Instance
types that fall below the performance baseline are automatically excluded from
selection, even if they match your other specified attributes. This ensures that all
selected instance types offer performance similar to or better than the baseline
established by the specified instance family. Amazon EC2 uses this baseline to guide instance
type selection, but there is no guarantee that the selected instance types will always
exceed the baseline for every application.

Currently, this feature only supports CPU performance as a baseline performance
factor. The CPU performance of the specified instance family's CPU processor serves as
the performance baseline, ensuring that selected instance types are similar to or exceed
this baseline. Instance families with the same CPU processors lead to the same filtering
results, even if their network or disk performance differs. For example, specifying
either `c6in` or `c6i` as the baseline reference would produce
identical performance-based filtering results because both instance families use the
same CPU processor.

###### Unsupported instance families

The following instance families are not supported for performance protection:

- `c1`
- `g3` | `g3s`
- `hpc7g`
- `m1` | `m2`
- `mac1` | `mac2` | `mac2-m1ultra` |
  `mac2-m2` | `mac2-m2pro`
- `p3dn` | `p4d` | `p5`
- `t1`
- `u-12tb1` | `u-18tb1` | `u-24tb1` |
  `u-3tb1` | `u-6tb1` | `u-9tb1` |
  `u7i-12tb` | `u7in-16tb` | `u7in-24tb` |
  `u7in-32tb`

If you enable performance protection by specifying a supported instance family, the
returned instance types will exclude the above unsupported instance families.

If you specify an unsupported instance family as a value for baseline performance, the
API returns an empty response for [GetInstanceTypesFromInstanceRequirements](../APIReference/API_GetInstanceTypesFromInstanceRequirements.md "../APIReference/API_GetInstanceTypesFromInstanceRequirements.md") and an exception for [CreateFleet](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md"), [RequestSpotFleet](../APIReference/API_RequestSpotFleet.md "../APIReference/API_RequestSpotFleet.md"),
[ModifyFleet](../APIReference/API_ModifyFleet.md "../APIReference/API_ModifyFleet.md"), and [ModifySpotFleetRequest](../APIReference/API_ModifySpotFleetRequest.md "../APIReference/API_ModifySpotFleetRequest.md").

###### Example: Set a CPU performance baseline

In the following example, the instance requirement is to launch with instance
types that have CPU cores that are as performant as the `c6i` instance
family. This will filter out instance types with less performant CPU processors,
even if they meet your other specified instance requirements such as the number of
vCPUs. For example, if your specified instance attributes include 4 vCPUs and 16 GB
of memory, an instance type with these attributes but with lower CPU performance
than `c6i` will be excluded from selection.

```
"BaselinePerformanceFactors": {
        "Cpu": {
            "References": [
                {
                    "InstanceFamily": "c6i"
                }
            ]
        }
```

## Considerations

- You can specify either instance types or instance attributes in an EC2 Fleet or
  Spot Fleet, but not both at the same time.

When using the CLI, the launch template overrides will override the launch
template. For example, if the launch template contains an instance type and the
launch template override contains instance attributes, the instances that are
identified by the instance attributes will override the instance type in the
launch template.

- When using the CLI, when you specify instance attributes as overrides, you
  can't also specify weights or priorities.
- You can specify a maximum of four `InstanceRequirements` structures
  in a request configuration.

## Create an EC2 Fleet with attribute-based instance type selection

You can configure an EC2 Fleet to use attribute-based instance type selection. It is not possible to create an EC2 Fleet using the
Amazon EC2 console.

The attributes for attribute-based instance type selection are specified in the `InstanceRequirements`
structure. When `InstanceRequirements` is included in the fleet
configuration, `InstanceType` and `WeightedCapacity` must be
excluded; they can't determine the fleet configuration at the same time as
instance attributes.

In the AWS CLI and PowerShell examples, the following attributes are specified:

- `VCpuCount` – A minimum of 2 vCPUs and a maximum of 4 vCPUs.
  If you don't need a maximum limit, you can omit the maximum value.
- `MemoryMiB` – A minimum of 8 GiB of memory and a maximum
  of 16 GiB. If you don't need a maximum limit, you can omit the maximum
  value.

This configuration identifies any instance types with 2 to 4 vCPUs and 8 to 16 GiB
of memory. However, price protection and the allocation strategy might exclude some
instance types when [EC2 Fleet provisions the
fleet](#how-ef-uses-abs "#how-ef-uses-abs").

AWS CLI

###### To create an EC2 Fleet with attribute-based instance type selection

Use the [create-fleet](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md")
command to create an EC2 Fleet. Specify the fleet configuration in a JSON file.

```
aws ec2 create-fleet \
    --region `us-east-1` \
    --cli-input-json file://`file_name`.json
```

The following example ``file_name`.json` file
contains the parameters that configure an EC2 Fleet to use attribute-based instance type
selection.

```
{
    "SpotOptions": {
        "AllocationStrategy": "`price-capacity-optimized`"
    },
    "LaunchTemplateConfigs": [{
        "LaunchTemplateSpecification": {
            "LaunchTemplateName": "`my-launch-template`",
            "Version": "`1`"
        },
        "Overrides": [{
            **"InstanceRequirements": {
 "VCpuCount": {
 "Min": `2`,
 "Max": `4`
 },
 "MemoryMiB": {
 "Min": `8192`,
 "Max": `16384`
 }
 }**
        }]
    }],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": `20`,
        "DefaultTargetCapacityType": "`spot`"
    },
    "Type": "`instant`"
}
```

PowerShell

###### To create an EC2 Fleet with attribute-based instance type selection

Use the [New-EC2Fleet](../../../powershell/latest/reference/items/New-EC2Fleet.md "../../../powershell/latest/reference/items/New-EC2Fleet.md")
cmdlet.

```
**$vcpuCount = New-Object Amazon.EC2.Model.VCpuCountRangeRequest
$vcpuCount.Min = `2`
$vcpuCount.Max = `4`
$memoryMiB = New-Object Amazon.EC2.Model.MemoryMiBRequest
$memoryMiB.Min = `8192`
$memoryMiB.Max = `16384`
$instanceRequirements = New-Object Amazon.EC2.Model.InstanceRequirementsRequest
$instanceRequirements.VCpuCount = $vcpuCount
$instanceRequirements.MemoryMiB = $memoryMiB**

$launchTemplateSpec = New-Object Amazon.EC2.Model.FleetLaunchTemplateSpecificationRequest
$launchTemplateSpec.LaunchTemplateName = "`my-launch-template`"
$launchTemplateSpec.Version = "`1`"
$override = New-Object Amazon.EC2.Model.FleetLaunchTemplateOverridesRequest
$override.InstanceRequirements = $instanceRequirements
$launchTemplateConfig = New-Object Amazon.EC2.Model.FleetLaunchTemplateConfigRequest
$launchTemplateConfig.LaunchTemplateSpecification = $launchTemplateSpec
$launchTemplateConfig.Overrides = @($override)

New-EC2Fleet `
    -SpotOptions_AllocationStrategy "`price-capacity-optimized`" `
    -LaunchTemplateConfig @($launchTemplateConfig) `
    -TargetCapacitySpecification_DefaultTargetCapacityType "`spot`" `
    -TargetCapacitySpecification_TotalTargetCapacity `20` `
    -Type "instant"
```

## Create a Spot Fleet with attribute-based instance type selection

You can configure a fleet to use attribute-based instance type selection.

The attributes for attribute-based instance type selection are specified in the `InstanceRequirements`
structure. When `InstanceRequirements` is included in the fleet
configuration, `InstanceType` and `WeightedCapacity` must be
excluded; they can't determine the fleet configuration at the same time as
instance attributes.

In the AWS CLI and PowerShell examples, the following attributes are specified:

- `VCpuCount` – A minimum of 2 vCPUs and a maximum of
  4 vCPUs. If you don't need a maximum limit, you can omit the maximum
  value.
- `MemoryMiB` – A minimum of 8 GiB of memory and a
  maximum of 16 GiB. If you don't need a maximum limit, you can omit the
  maximum value.

This configuration identifies any instance types that have 2 to 4 vCPUs and
8 to 16 GiB of memory. However, price protection and the allocation strategy
might exclude some instance types when [Spot Fleet
provisions the fleet](#how-ef-uses-abs "#how-ef-uses-abs").

Console

###### To configure a Spot Fleet for attribute-based instance type selection

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**, and
   then choose **Request Spot Instances**.
3. Follow the steps to create a Spot Fleet. For more information, see [Create a Spot Fleet request using defined
   parameters](create-spot-fleet.md#create-spot-fleet-advanced "create-spot-fleet.md#create-spot-fleet-advanced").

While creating the Spot Fleet, configure the fleet for attribute-based instance type selection as
follows:

    1. For **Instance type requirements**, choose
     **Specify instance attributes that match your compute
     requirements**.
    2. For **vCPUs**, enter the desired minimum and
     maximum number of vCPUs. To specify no limit, select **No
     minimum**, **No maximum**, or
     both.
    3. For **Memory (GiB)**, enter the desired minimum
     and maximum amount of memory. To specify no limit, select
     **No minimum**, **No
     maximum**, or both.
    4. (Optional) For **Additional instance
     attributes**, you can optionally specify one or more
     attributes to express your compute requirements in more detail. Each
     additional attribute adds further constraints to your
     request.
    5. (Optional) Expand **Preview matching instance
     types** to view the instance types that have your
     specified attributes.

AWS CLI

###### To configure a Spot Fleet for attribute-based instance type selection

Use the [request-spot-fleet](../../../cli/latest/reference/ec2/request-spot-fleet.md "../../../cli/latest/reference/ec2/request-spot-fleet.md") command to create a Spot Fleet. Specify the
fleet configuration in a JSON file.

```
aws ec2 request-spot-fleet \
    --region `us-east-1` \
    --spot-fleet-request-config file://`file_name`.json
```

The following example ``file_name`.json`
file contains the parameters that configure a Spot Fleet to use attribute-based instance type selection.

```
{
    "AllocationStrategy": "`priceCapacityOptimized`",
    "TargetCapacity": `20`,
    "Type": "`request`",
    "LaunchTemplateConfigs": [{
        "LaunchTemplateSpecification": {
            "LaunchTemplateName": "`my-launch-template`",
            "Version": "`1`"
        },
        "Overrides": [{
            **"InstanceRequirements": {
 "VCpuCount": {
 "Min": `2`,
 "Max": `4`
 },
 "MemoryMiB": {
 "Min": `8192`,
 "Max": `16384`
 }
 }**
        }]
    }]
}
```

PowerShell

###### To configure a Spot Fleet for attribute-based instance type selection

Use the [Request-EC2SpotFleet](../../../powershell/latest/reference/items/Request-EC2SpotFleet.md "../../../powershell/latest/reference/items/Request-EC2SpotFleet.md")
cmdlet.

```
**$vcpuCount = New-Object Amazon.EC2.Model.VCpuCountRange
$vcpuCount.Min = `2`
$vcpuCount.Max = `4`
$memoryMiB = New-Object Amazon.EC2.Model.MemoryMiB
$memoryMiB.Min = `8192`
$memoryMiB.Max = `16384`
$instanceRequirements = New-Object Amazon.EC2.Model.InstanceRequirements
$instanceRequirements.VCpuCount = $vcpuCount
$instanceRequirements.MemoryMiB = $memoryMiB**

$launchTemplateSpec = New-Object Amazon.EC2.Model.FleetLaunchTemplateSpecification
$launchTemplateSpec.LaunchTemplateName = "`my-launch-template`"
$launchTemplateSpec.Version = "`1`"
$override = New-Object Amazon.EC2.Model.LaunchTemplateOverrides
$override.InstanceRequirements = $instanceRequirements
$launchTemplateConfig = New-Object Amazon.EC2.Model.LaunchTemplateConfig
$launchTemplateConfig.LaunchTemplateSpecification = $launchTemplateSpec
$launchTemplateConfig.Overrides = @($override)

Request-EC2SpotFleet `
    -SpotFleetRequestConfig_AllocationStrategy "`PriceCapacityOptimized`" `
    -SpotFleetRequestConfig_TargetCapacity `20` `
    -SpotFleetRequestConfig_Type "`Request`" `
    -SpotFleetRequestConfig_LaunchTemplateConfig $launchTemplateConfig
```

## Examples of EC2 Fleet configurations that are

valid and not valid

If you use the AWS CLI to create an EC2 Fleet, you must make sure that your fleet
configuration is valid. The following examples show configurations that are valid and
not valid.

Configurations are considered not valid when they contain the following:

- A single `Overrides` structure with both
  `InstanceRequirements` and `InstanceType`
- Two `Overrides` structures, one with
  `InstanceRequirements` and the other with
  `InstanceType`
- Two `InstanceRequirements` structures with overlapping attribute
  values within the same `LaunchTemplateSpecification`

###### Example configurations

- [Valid configuration: Single launch template
  with overrides](#ef-abs-example-config1 "#ef-abs-example-config1")
- [Valid configuration: Single launch template
  with multiple InstanceRequirements](#ef-abs-example-config2 "#ef-abs-example-config2")
- [Valid configuration: Two launch templates,
  each with overrides](#ef-abs-example-config3 "#ef-abs-example-config3")
- [Valid configuration: Only
  InstanceRequirements specified, no overlapping attribute
  values](#ef-abs-example-config4 "#ef-abs-example-config4")
- [Configuration not valid:
  Overrides contain InstanceRequirements and
  InstanceType](#ef-abs-example-config5 "#ef-abs-example-config5")
- [Configuration not valid: Two
  Overrides contain InstanceRequirements and
  InstanceType](#ef-abs-example-config6 "#ef-abs-example-config6")
- [Configuration not valid: Overlapping
  attribute values](#ef-abs-example-config7 "#ef-abs-example-config7")

### Valid configuration: Single launch template

with overrides

The following configuration is valid. It contains one launch template and one
`Overrides` structure containing one
`InstanceRequirements` structure. A text explanation of the example
configuration follows.

```
{
        "LaunchTemplateConfigs": [
        {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "My-launch-template",
                "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 2,
                            "Max": 8
                        },
                        "MemoryMib": {
                            "Min": 0,
                            "Max": 10240
                        },
                        "MemoryGiBPerVCpu": {
                            "Max": 10000
                        },
                        "RequireHibernateSupport": true
                    }
                }
            ]
        }
    ],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": 5000,
        "DefaultTargetCapacityType": "spot",
        "TargetCapacityUnitType": "vcpu"
        }
    }
}
```

###### **`InstanceRequirements`**

To use attribute-based instance selection, you must include the
`InstanceRequirements` structure in your fleet configuration, and
specify the desired attributes for the instances in the fleet.

In the preceding example, the following instance attributes are specified:

- `VCpuCount` – The instance types must have a minimum of
  2 and a maximum of 8 vCPUs.
- `MemoryMiB` – The instance types must have a maximum of
  10240 MiB of memory. A minimum of 0 indicates no minimum limit.
- `MemoryGiBPerVCpu` – The instance types must have a
  maximum of 10,000 GiB of memory per vCPU. The `Min` parameter is
  optional. By omitting it, you indicate no minimum limit.

###### `**TargetCapacityUnitType**`

The `TargetCapacityUnitType` parameter specifies the unit for the
target capacity. In the example, the target capacity is `5000` and
the target capacity unit type is `vcpu`, which together specify a
desired target capacity of 5,000 vCPUs. EC2 Fleet will launch enough instances so
that the total number of vCPUs in the fleet is 5,000 vCPUs.

### Valid configuration: Single launch template

with multiple InstanceRequirements

The following configuration is valid. It contains one launch template and one
`Overrides` structure containing two
`InstanceRequirements` structures. The attributes specified in
`InstanceRequirements` are valid because the values do not
overlap—the first `InstanceRequirements` structure specifies a
`VCpuCount` of 0-2 vCPUs, while the second
`InstanceRequirements` structure specifies 4-8 vCPUs.

```
{
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                },
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 4,
                            "Max": 8
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            }
        ],
        "TargetCapacitySpecification": {
            "TotalTargetCapacity": 1,
            "DefaultTargetCapacityType": "spot"
        }
    }
}
```

### Valid configuration: Two launch templates,

each with overrides

The following configuration is valid. It contains two launch templates, each with
one `Overrides` structure containing one
`InstanceRequirements` structure. This configuration is useful for
`arm` and `x86` architecture support in the same
fleet.

```
{
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "armLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                },
                {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "x86LaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            }
        ],
         "TargetCapacitySpecification": {
            "TotalTargetCapacity": 1,
            "DefaultTargetCapacityType": "spot"
        }
    }
}
```

### Valid configuration: Only

`InstanceRequirements` specified, no overlapping attribute
values

The following configuration is valid. It contains two
`LaunchTemplateSpecification` structures, each with a launch template
and an `Overrides` structure containing an
`InstanceRequirements` structure. The attributes specified in
`InstanceRequirements` are valid because the values do not
overlap—the first `InstanceRequirements` structure specifies a
`VCpuCount` of 0-2 vCPUs, while the second
`InstanceRequirements` structure specifies 4-8 vCPUs.

```
{
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            },
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyOtherLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 4,
                            "Max": 8
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            }
        ],
        "TargetCapacitySpecification": {
            "TotalTargetCapacity": 1,
            "DefaultTargetCapacityType": "spot"
        }
    }
}
```

### Configuration not valid:

`Overrides` contain `InstanceRequirements` and
`InstanceType`

The following configuration is not valid. The `Overrides` structure
contains both `InstanceRequirements` and `InstanceType`. For
the `Overrides`, you can specify either `InstanceRequirements`
or `InstanceType`, but not both.

```
{
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                },
                {
                    "InstanceType": "m5.large"
                }
              ]
            }
        ],
        "TargetCapacitySpecification": {
            "TotalTargetCapacity": 1,
            "DefaultTargetCapacityType": "spot"
        }
    }
}

```

### Configuration not valid: Two

`Overrides` contain `InstanceRequirements` and
`InstanceType`

The following configuration is not valid. The `Overrides` structures
contain both `InstanceRequirements` and `InstanceType`. You
can specify either `InstanceRequirements` or `InstanceType`,
but not both, even if they're in different `Overrides` structures.

```
{
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            },
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyOtherLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceType": "m5.large"
                }
              ]
            }
        ],
         "TargetCapacitySpecification": {
            "TotalTargetCapacity": 1,
            "DefaultTargetCapacityType": "spot"
        }
    }
}
```

### Configuration not valid: Overlapping

attribute values

The following configuration is not valid. The two
`InstanceRequirements` structures each contain `"VCpuCount":
 {"Min": 0, "Max": 2}`. The values for these attributes overlap, which will
result in duplicate capacity pools.

```
{
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    },
                    {
                      "InstanceRequirements": {
                          "VCpuCount": {
                              "Min": 0,
                              "Max": 2
                          },
                          "MemoryMiB": {
                              "Min": 0
                          }
                      }
                  }
                }
              ]
            }
        ],
         "TargetCapacitySpecification": {
            "TotalTargetCapacity": 1,
            "DefaultTargetCapacityType": "spot"
        }
    }
}

```

## Examples of Spot Fleet configurations that are

valid and not valid

If you use the AWS CLI to create a Spot Fleet, you must make sure that your fleet
configuration is valid. The following examples show configurations that are valid and
not valid.

Configurations are considered not valid when they contain the following:

- A single `Overrides` structure with both
  `InstanceRequirements` and `InstanceType`
- Two `Overrides` structures, one with
  `InstanceRequirements` and the other with
  `InstanceType`
- Two `InstanceRequirements` structures with overlapping attribute
  values within the same `LaunchTemplateSpecification`

###### Example configurations

- [Valid configuration: Single launch template
  with overrides](#sf-abs-example-config1 "#sf-abs-example-config1")
- [Valid configuration: Single launch template
  with multiple InstanceRequirements](#sf-abs-example-config2 "#sf-abs-example-config2")
- [Valid configuration: Two launch templates,
  each with overrides](#sf-abs-example-config3 "#sf-abs-example-config3")
- [Valid configuration: Only
  InstanceRequirements specified, no overlapping attribute
  values](#sf-abs-example-config4 "#sf-abs-example-config4")
- [Configuration not valid:
  Overrides contain InstanceRequirements and
  InstanceType](#sf-abs-example-config5 "#sf-abs-example-config5")
- [Configuration not valid: Two
  Overrides contain InstanceRequirements and
  InstanceType](#sf-abs-example-config6 "#sf-abs-example-config6")
- [Configuration not valid: Overlapping
  attribute values](#sf-abs-example-config7 "#sf-abs-example-config7")

### Valid configuration: Single launch template

with overrides

The following configuration is valid. It contains one launch template and one
`Overrides` structure containing one
`InstanceRequirements` structure. A text explanation of the example
configuration follows.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "priceCapacityOptimized",
        "ExcessCapacityTerminationPolicy": "default",
        "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging-role",
        "LaunchTemplateConfigs": [
        {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "My-launch-template",
                "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 2,
                            "Max": 8
                        },
                        "MemoryMib": {
                            "Min": 0,
                            "Max": 10240
                        },
                        "MemoryGiBPerVCpu": {
                            "Max": 10000
                        },
                        "RequireHibernateSupport": true
                    }
                }
            ]
        }
    ],
        "TargetCapacity": 5000,
            "OnDemandTargetCapacity": 0,
            "TargetCapacityUnitType": "vcpu"
    }
}
```

###### **`InstanceRequirements`**

To use attribute-based instance selection, you must include the
`InstanceRequirements` structure in your fleet configuration, and
specify the desired attributes for the instances in the fleet.

In the preceding example, the following instance attributes are specified:

- `VCpuCount` – The instance types must have a minimum of
  2 and a maximum of 8 vCPUs.
- `MemoryMiB` – The instance types must have a maximum of
  10240 MiB of memory. A minimum of 0 indicates no minimum limit.
- `MemoryGiBPerVCpu` – The instance types must have a
  maximum of 10,000 GiB of memory per vCPU. The `Min` parameter is
  optional. By omitting it, you indicate no minimum limit.

###### `**TargetCapacityUnitType**`

The `TargetCapacityUnitType` parameter specifies the unit for the
target capacity. In the example, the target capacity is `5000` and
the target capacity unit type is `vcpu`, which together specify a
desired target capacity of 5,000 vCPUs. Spot Fleet will launch enough instances
so that the total number of vCPUs in the fleet is 5,000 vCPUs.

### Valid configuration: Single launch template

with multiple InstanceRequirements

The following configuration is valid. It contains one launch template and one
`Overrides` structure containing two
`InstanceRequirements` structures. The attributes specified in
`InstanceRequirements` are valid because the values do not
overlap—the first `InstanceRequirements` structure specifies a
`VCpuCount` of 0-2 vCPUs, while the second
`InstanceRequirements` structure specifies 4-8 vCPUs.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "priceCapacityOptimized",
        "ExcessCapacityTerminationPolicy": "default",
        "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging-role",
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                },
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 4,
                            "Max": 8
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            }
        ],
        "TargetCapacity": 1,
        "OnDemandTargetCapacity": 0,
        "Type": "maintain"
    }
}
```

### Valid configuration: Two launch templates,

each with overrides

The following configuration is valid. It contains two launch templates, each with
one `Overrides` structure containing one
`InstanceRequirements` structure. This configuration is useful for
`arm` and `x86` architecture support in the same
fleet.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "priceCapacityOptimized",
        "ExcessCapacityTerminationPolicy": "default",
        "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging-role",
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "armLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                },
                {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "x86LaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            }
        ],
        "TargetCapacity": 1,
        "OnDemandTargetCapacity": 0,
        "Type": "maintain"
    }
}
```

### Valid configuration: Only

`InstanceRequirements` specified, no overlapping attribute
values

The
following configuration is valid. It contains two
`LaunchTemplateSpecification` structures, each with a launch template
and an `Overrides` structure containing an
`InstanceRequirements` structure. The attributes specified in
`InstanceRequirements` are valid because the values do not
overlap—the first `InstanceRequirements` structure specifies a
`VCpuCount` of 0-2 vCPUs, while the second
`InstanceRequirements` structure specifies 4-8 vCPUs.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "priceCapacityOptimized",
        "ExcessCapacityTerminationPolicy": "default",
        "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging-role",
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            },
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyOtherLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 4,
                            "Max": 8
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            }
        ],
        "TargetCapacity": 1,
        "OnDemandTargetCapacity": 0,
        "Type": "maintain"
    }
}
```

### Configuration not valid:

`Overrides` contain `InstanceRequirements` and
`InstanceType`

The following configuration is not valid. The `Overrides` structure
contains both `InstanceRequirements` and `InstanceType`. For
the `Overrides`, you can specify either `InstanceRequirements`
or `InstanceType`, but not both.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "priceCapacityOptimized",
        "ExcessCapacityTerminationPolicy": "default",
        "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging-role",
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                },
                {
                    "InstanceType": "m5.large"
                }
              ]
            }
        ],
        "TargetCapacity": 1,
        "OnDemandTargetCapacity": 0,
        "Type": "maintain"
    }
}

```

### Configuration not valid: Two

`Overrides` contain `InstanceRequirements` and
`InstanceType`

The following configuration is not valid. The `Overrides` structures
contain both `InstanceRequirements` and `InstanceType`. You
can specify either `InstanceRequirements` or `InstanceType`,
but not both, even if they're in different `Overrides` structures.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "priceCapacityOptimized",
        "ExcessCapacityTerminationPolicy": "default",
        "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging-role",
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    }
                }
              ]
            },
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyOtherLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceType": "m5.large"
                }
              ]
            }
        ],
        "TargetCapacity": 1,
        "OnDemandTargetCapacity": 0,
        "Type": "maintain"
    }
}
```

### Configuration not valid: Overlapping

attribute values

The following configuration is not valid. The two
`InstanceRequirements` structures each contain `"VCpuCount":
 {"Min": 0, "Max": 2}`. The values for these attributes overlap, which will
result in duplicate capacity pools.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "priceCapacityOptimized",
        "ExcessCapacityTerminationPolicy": "default",
        "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging-role",
        "LaunchTemplateConfigs": [
            {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "MyLaunchTemplate",
                    "Version": "1"
                },
                "Overrides": [
                {
                    "InstanceRequirements": {
                        "VCpuCount": {
                            "Min": 0,
                            "Max": 2
                        },
                        "MemoryMiB": {
                            "Min": 0
                        }
                    },
                    {
                      "InstanceRequirements": {
                          "VCpuCount": {
                              "Min": 0,
                              "Max": 2
                          },
                          "MemoryMiB": {
                              "Min": 0
                          }
                      }
                  }
                }
              ]
            }
        ],
        "TargetCapacity": 1,
        "OnDemandTargetCapacity": 0,
        "Type": "maintain"
    }
}

```

## Preview

instance types with specified attributes

You can use the [get-instance-types-from-instance-requirements](../../../cli/latest/reference/ec2/get-instance-types-from-instance-requirements.md "../../../cli/latest/reference/ec2/get-instance-types-from-instance-requirements.md") command to preview
the instance types that match the attributes that you specify. This is especially useful
for working out what attributes to specify in your request configuration without
launching any instances. Note that the command does not consider available
capacity.

###### To preview a list of instance types by specifying attributes using the

AWS CLI

1. (Optional) To generate all of the possible attributes that can be specified,
   use the [get-instance-types-from-instance-requirements](../../../cli/latest/reference/ec2/get-instance-types-from-instance-requirements.md "../../../cli/latest/reference/ec2/get-instance-types-from-instance-requirements.md") command and the
   `--generate-cli-skeleton` parameter. You can optionally direct
   the output to a file to save it by using `input >
`attributes.json``.

```
aws ec2 get-instance-types-from-instance-requirements \
    --region us-east-1 \
    --generate-cli-skeleton input > `attributes.json`
```

Expected output

```
{
    "DryRun": true,
    "ArchitectureTypes": [
        "i386"
    ],
    "VirtualizationTypes": [
        "hvm"
    ],
    "InstanceRequirements": {
        "VCpuCount": {
            "Min": 0,
            "Max": 0
        },
        "MemoryMiB": {
            "Min": 0,
            "Max": 0
        },
        "CpuManufacturers": [
            "intel"
        ],
        "MemoryGiBPerVCpu": {
            "Min": 0.0,
            "Max": 0.0
        },
        "ExcludedInstanceTypes": [
            ""
        ],
        "InstanceGenerations": [
            "current"
        ],
        "SpotMaxPricePercentageOverLowestPrice": 0,
        "OnDemandMaxPricePercentageOverLowestPrice": 0,
        "BareMetal": "included",
        "BurstablePerformance": "included",
        "RequireHibernateSupport": true,
        "NetworkInterfaceCount": {
            "Min": 0,
            "Max": 0
        },
        "LocalStorage": "included",
        "LocalStorageTypes": [
            "hdd"
        ],
        "TotalLocalStorageGB": {
            "Min": 0.0,
            "Max": 0.0
        },
        "BaselineEbsBandwidthMbps": {
            "Min": 0,
            "Max": 0
        },
        "AcceleratorTypes": [
            "gpu"
        ],
        "AcceleratorCount": {
            "Min": 0,
            "Max": 0
        },
        "AcceleratorManufacturers": [
            "nvidia"
        ],
        "AcceleratorNames": [
            "a100"
        ],
        "AcceleratorTotalMemoryMiB": {
            "Min": 0,
            "Max": 0
        },
        "NetworkBandwidthGbps": {
            "Min": 0.0,
            "Max": 0.0
        },
        "AllowedInstanceTypes": [
            ""
        ]
    },
    "MaxResults": 0,
    "NextToken": ""
}
```

2. Create a JSON configuration file using the output from the previous step, and
   configure it as follows:

###### Note

You must provide values for `ArchitectureTypes`,
`VirtualizationTypes`, `VCpuCount`, and
`MemoryMiB`. You can omit the other attributes; when omitted,
the default values are used.

For a description of each attribute and their default values, see
[get-instance-types-from-instance-requirements](../../../cli/latest/reference/ec2/get-instance-types-from-instance-requirements.md "../../../cli/latest/reference/ec2/get-instance-types-from-instance-requirements.md").

    1. For `ArchitectureTypes`, specify one or more types of
     processor architecture.
    2. For `VirtualizationTypes`, specify one or more types of
     virtualization.
    3. For `VCpuCount`, specify the minimum and maximum number of
     vCPUs. To specify no minimum limit, for `Min`, specify
     `0`. To specify no maximum limit, omit the
     `Max` parameter.
    4. For `MemoryMiB`, specify the minimum and maximum amount of
     memory in MiB. To specify no minimum limit, for `Min`,
     specify `0`. To specify no maximum limit, omit the
     `Max` parameter.
    5. You can optionally specify one or more of the other attributes to
     further constrain the list of instance types that are returned.

3. To preview the instance types that have the attributes that you specified in
   the JSON file, use the [get-instance-types-from-instance-requirements](../../../cli/latest/reference/ec2/get-instance-types-from-instance-requirements.md "../../../cli/latest/reference/ec2/get-instance-types-from-instance-requirements.md") command, and
   specify the name and path to your JSON file by using the
   `--cli-input-json` parameter. You can optionally format the
   output to appear in a table format.

```
aws ec2 get-instance-types-from-instance-requirements \
    --cli-input-json file://`attributes.json` \
    --output table
```

Example `attributes.json` file

In this example, the required attributes are included in the JSON file. They
are `ArchitectureTypes`, `VirtualizationTypes`,
`VCpuCount`, and `MemoryMiB`. In addition, the
optional `InstanceGenerations` attribute is also included. Note that
for `MemoryMiB`, the `Max` value can be omitted to
indicate that there is no limit.

```
{

    "ArchitectureTypes": [
        "x86_64"
    ],
    "VirtualizationTypes": [
        "hvm"
    ],
    "InstanceRequirements": {
        "VCpuCount": {
            "Min": 4,
            "Max": 6
        },
        "MemoryMiB": {
            "Min": 2048
        },
        "InstanceGenerations": [
            "current"
        ]
    }
}
```

Example output

```
------------------------------------------
|GetInstanceTypesFromInstanceRequirements|
+----------------------------------------+
||             InstanceTypes            ||
|+--------------------------------------+|
||             InstanceType             ||
|+--------------------------------------+|
||  c4.xlarge                           ||
||  c5.xlarge                           ||
||  c5a.xlarge                          ||
||  c5ad.xlarge                         ||
||  c5d.xlarge                          ||
||  c5n.xlarge                          ||
||  d2.xlarge                           ||
...
```

4. After identifying instance types that meet your needs, make note of the
   instance attributes that you used so that you can use them when configuring your
   fleet request.
