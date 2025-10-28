# Calculate the Spot placement score

You can calculate a Spot placement score based on target capacity and compute requirements. For more
information, see [How Spot placement score works](how-sps-works.md "how-sps-works.md").

###### Required permissions

Ensure that you have the required permissions. For more information, see [Required permissions for Spot placement score](sps-iam-permission.md "sps-iam-permission.md").

###### Options

- [Calculate using instance
  attributes](#sps-specify-instance-attributes-console "#sps-specify-instance-attributes-console")
- [Calculate using instance
  types](#sps-specify-instance-types-console "#sps-specify-instance-types-console")
- [Calculate using the AWS CLI](#calculate-sps-cli "#calculate-sps-cli")
  **Looking for an automated solution?** Instead of following the
  manual steps in this user guide, you can build a Spot placement score tracker dashboard that
  automatically captures and stores the scores in Amazon CloudWatch. For more information, see
  [Guidance for Building a Spot Placement Score Tracker Dashboard on
  AWS](https://aws.amazon.com/solutions/guidance/building-a-spot-placement-score-tracker-dashboard-on-aws/ "https://aws.amazon.com/solutions/guidance/building-a-spot-placement-score-tracker-dashboard-on-aws/").

## Calculate using instance

attributes

###### To calculate a Spot placement score by specifying instance attributes

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Choose the down arrow next to **Request Spot Instances** and choose
   **Calculate Spot Placement Score**.
4. Choose **Enter requirements**.
5. For **Target capacity**, enter your desired capacity in
   terms of the number of **instances** or
   **vCPUs**, or the amount of **memory
   (MiB)**.
6. For **Instance type requirements**, to specify your
   compute requirements and let Amazon EC2 identify the optimal instance types with
   these requirements, choose **Specify instance attributes that match
   your compute requirements**.
7. For **vCPUs**, enter the desired minimum and maximum
   number of vCPUs. To specify no limit, select **No
   minimum**, **No maximum**, or both.
8. For **Memory (GiB)**, enter the desired minimum and
   maximum amount of memory. To specify no limit, select **No
   minimum**, **No maximum**, or both.
9. For **CPU architecture**, select the required instance
   architecture.
10. (Optional) For **Additional instance attributes**, you
    can optionally specify one or more attributes to express your compute
    requirements in more detail. Each additional attribute adds a further
    constraint to your request. You can omit the additional attributes; when
    omitted, the default values are used. For a description of each attribute
    and their default values, see [get-spot-placement-scores](../../../cli/latest/reference/ec2/get-spot-placement-scores.md "../../../cli/latest/reference/ec2/get-spot-placement-scores.md").
11. (Optional) To view the instance types with your specified attributes,
    expand **Preview matching instance types**. To exclude
    instance types from being used in the placement evaluation, select the
    instances and then choose **Exclude selected instance
    types**.
12. Choose **Load placement scores**, and review the results.
13. (Optional) To display the Spot placement score for specific Regions, for
    **Regions to evaluate**, select the Regions to
    evaluate, and then choose **Calculate placement
    scores**.
14. (Optional) To display the Spot placement score for the Availability Zones in the
    displayed Regions, select the **Provide placement scores per
    Availability Zone** checkbox. A list of scored Availability
    Zones is useful if you want to launch all of your Spot capacity into a
    single Availability Zone.
15. (Optional) To edit your compute requirements and get a new placement
    score, choose **Edit**, make the necessary adjustments, and
    then choose **Calculate placement scores**.

## Calculate using instance

types

###### To calculate a Spot placement score by specifying instance types

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Choose the down arrow next to **Request Spot Instances** and
   choose **Calculate Spot Placement Score**.
4. Choose **Enter requirements**.
5. For **Target capacity**, enter your desired capacity in
   terms of the number of **instances** or
   **vCPUs**, or the amount of **memory
   (MiB)**.
6. For **Instance type requirements**, to specify the
   instance types to use, choose **Manually select instance
   types**.
7. Choose **Select instance types**, select the instance
   types to use, and then choose **Select**. To quickly find
   instance types, you can use the filter bar to filter the instance types by
   different properties.
8. Choose **Load placement scores**, and review the results.
9. (Optional) To display the Spot placement score for specific Regions, for
   **Regions to evaluate**, select the Regions to
   evaluate, and then choose **Calculate placement
   scores**.
10. (Optional) To display the Spot placement score for the Availability Zones in the
    displayed Regions, select the **Provide placement scores per
    Availability Zone** checkbox. A list of scored Availability
    Zones is useful if you want to launch all of your Spot capacity into a
    single Availability Zone.
11. (Optional) To edit the list of instance types and get a new placement
    score, choose **Edit**, make the necessary adjustments, and
    then choose **Calculate placement scores**.

## Calculate using the AWS CLI

###### To calculate the Spot placement score

1. (Optional) To generate all of the possible parameters that can be
   specified for the Spot placement score configuration, use the [get-spot-placement-scores](../../../cli/latest/reference/ec2/get-spot-placement-scores.md "../../../cli/latest/reference/ec2/get-spot-placement-scores.md") command and the
   `--generate-cli-skeleton` parameter.

```
aws ec2 get-spot-placement-scores \
    --region `us-east-1` \
    --generate-cli-skeleton
```

The following is example output.

```
{
    "InstanceTypes": [
        ""
    ],
    "TargetCapacity": 0,
    "TargetCapacityUnitType": "vcpu",
    "SingleAvailabilityZone": true,
    "RegionNames": [
        ""
    ],
    "InstanceRequirementsWithMetadata": {
        "ArchitectureTypes": [
            "x86_64_mac"
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
                "amd"
            ],
            "MemoryGiBPerVCpu": {
                "Min": 0.0,
                "Max": 0.0
            },
            "ExcludedInstanceTypes": [
                ""
            ],
            "InstanceGenerations": [
                "previous"
            ],
            "SpotMaxPricePercentageOverLowestPrice": 0,
            "OnDemandMaxPricePercentageOverLowestPrice": 0,
            "BareMetal": "excluded",
            "BurstablePerformance": "excluded",
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
                "fpga"
            ],
            "AcceleratorCount": {
                "Min": 0,
                "Max": 0
            },
            "AcceleratorManufacturers": [
                "amd"
            ],
            "AcceleratorNames": [
                "vu9p"
            ],
            "AcceleratorTotalMemoryMiB": {
                "Min": 0,
                "Max": 0
            }
        }
    },
    "DryRun": true,
    "MaxResults": 0,
    "NextToken": ""
}

```

2.  Create a JSON configuration file using the output from the previous step,
    and configure it as follows:
    1. For `TargetCapacity`, enter your desired Spot capacity
       in terms of the number of instances or vCPUs, or the amount of
       memory (MiB).
    2. For `TargetCapacityUnitType`, enter the unit for the
       target capacity. If you omit this parameter, it defaults to
       `units`.

    Valid values: `units` (which translates to number of
    instances) | `vcpu` | `memory-mib` 3. For `SingleAvailabilityZone`, specify `true`
    for a response that returns a list of scored Availability Zones. A
    list of scored Availability Zones is useful if you want to launch
    all of your Spot capacity into a single Availability Zone. If you
    omit this parameter, it defaults to `false`, and the
    response returns a list of scored
    Regions. 4. (Optional) For `RegionNames`, specify the Regions to use as a filter. You must specify the Region
    code, for example, `us-east-1`.

    With a Region filter, the response returns only the Regions that you specify. If you specified
    `true` for `SingleAvailabilityZone`, the
    response returns only the Availability Zones in the specified
    Regions. 5. You can include either `InstanceTypes` or
    `InstanceRequirements`, but not both in the same
    configuration.

    Specify one of the following in your JSON configuration:

        * To specify a list of instance types, specify the instance
         types in the `InstanceTypes` parameter. Specify
         at least three different instance types. If you specify only
         one or two instance types, Spot placement score returns a low score. For
         the list of instance types, see [Amazon EC2 Instance
         Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").
        * To specify the instance attributes so that Amazon EC2 will
         identify the instance types that match those attributes,
         specify the attributes that are located in the
         `InstanceRequirements` structure.


        You must provide values for `VCpuCount`,
         `MemoryMiB`, and
         `CpuManufacturers`. You can omit the other
         attributes; when omitted, the default values are used. For a
         description of each attribute and their default values, see
         [get-spot-placement-scores](../../../cli/latest/reference/ec2/get-spot-placement-scores.md "../../../cli/latest/reference/ec2/get-spot-placement-scores.md").

    For example configurations, see [Example configurations](#sps-example-configs "#sps-example-configs").

3.  To get the Spot placement score for the requirements that you specified in the JSON file,
    use the [get-spot-placement-scores](../../../cli/latest/reference/ec2/get-spot-placement-scores.md "../../../cli/latest/reference/ec2/get-spot-placement-scores.md") command, and specify the name and
    path to your JSON file by using the `--cli-input-json`
    parameter.

```
aws ec2 get-spot-placement-scores \
    --region `us-east-1` \
    --cli-input-json file://`file_name`.json
```

Example output if `SingleAvailabilityZone` is set to
`false` or omitted (if omitted, it defaults to
`false`) – a scored list of
Regions is
returned.

```
"SpotPlacementScores": [
    {
        "Region": "us-east-1",
        "Score": 7
    },
    {
        "Region": "us-west-1",
        "Score": 5
    },
   ...
```

Example output if `SingleAvailabilityZone` is set to
`true` – a scored list of Availability Zones is
returned.

```
"SpotPlacementScores": [
    {
        "Region": "us-east-1",
        "AvailabilityZoneId": "use1-az1",
        "Score": 8
    },
    {
        "Region": "us-east-1",
        "AvailabilityZoneId": "usw2-az3",
        "Score": 6
    },
   ...
```

### Example configurations

When using the AWS CLI, you can use the following example configurations.

###### Example configurations

- [Example: Specify
  instance types and target capacity](#example-config-instance-type-override "#example-config-instance-type-override")
- [Example:
  Specify instance types, and target capacity in terms of memory](#example-config-instance-type-memory-unit-override "#example-config-instance-type-memory-unit-override")
- [Example: Specify attributes for attribute-based instance type
  selection](#example-config-attribute-based-instance-type-selection "#example-config-attribute-based-instance-type-selection")
- [Example: Specify attributes
  for attribute-based instance type selection and return a scored list of
  Availability Zones](#example-config-sps-singleAZ "#example-config-sps-singleAZ")

#### Example: Specify

instance types and target capacity

The following example configuration specifies three different instance
types and a target Spot capacity of 500 Spot Instances.

```
{
    "InstanceTypes": [
        "m5.4xlarge",
        "r5.2xlarge",
        "m4.4xlarge"
    ],
    "TargetCapacity": 500
}
```

#### Example:

Specify instance types, and target capacity in terms of memory

The following example configuration specifies three different instance
types and a target Spot capacity of 500,000 MiB of memory, where the number
of Spot Instances to launch must provide a total of 500,000 MiB of memory.

```
{
    "InstanceTypes": [
        "m5.4xlarge",
        "r5.2xlarge",
        "m4.4xlarge"
    ],
    "TargetCapacity": 500000,
    "TargetCapacityUnitType": "memory-mib"
}
```

#### Example: Specify attributes for attribute-based instance type

selection

The following example configuration is configured for attribute-based
instance type selection, and is followed by a text explanation of the
example configuration.

```
{
    "TargetCapacity": 5000,
    "TargetCapacityUnitType": "vcpu",
    "InstanceRequirementsWithMetadata": {
        "ArchitectureTypes": ["arm64"],
        "VirtualizationTypes": ["hvm"],
        "InstanceRequirements": {
            "VCpuCount": {
                "Min": 1,
                "Max": 12
            },
            "MemoryMiB": {
                "Min": 512
            }
        }
    }
}
```

###### **`InstanceRequirementsWithMetadata`**

To use attribute-based instance type selection, you must include the
`InstanceRequirementsWithMetadata` structure in your
configuration, and specify the desired attributes for the Spot Instances.

In the preceding example, the following required instance attributes are
specified:

- `ArchitectureTypes` – The architecture type of
  the instance types must be `arm64`.
- `VirtualizationTypes` – The virtualization type
  of the instance types must be `hvm`.
- `VCpuCount` – The instance types must have a
  minimum of 1 and a maximum of 12 vCPUs.
- `MemoryMiB` – The instance types must have a
  minimum of 512 MiB of memory. By omitting the `Max`
  parameter, you are indicating that there is no maximum limit.

Note that there are several other optional attributes that you can
specify. For the list of attributes, see [get-spot-placement-scores](../../../cli/latest/reference/ec2/get-spot-placement-scores.md "../../../cli/latest/reference/ec2/get-spot-placement-scores.md").

###### `**TargetCapacityUnitType**`

The `TargetCapacityUnitType` parameter specifies the unit
for the target capacity. In the example, the target capacity is
`5000` and the target capacity unit type is
`vcpu`, which together specify a desired target capacity
of 5000 vCPUs, where the number of Spot Instances to launch must provide a total
of 5000 vCPUs.

#### Example: Specify attributes

for attribute-based instance type selection and return a scored list of
Availability Zones

The following example configuration is configured for attribute-based
instance type selection. By specifying `"SingleAvailabilityZone":
 true`, the response will return a list of scored Availability
Zones.

```
{
    "TargetCapacity": 1000,
    "TargetCapacityUnitType": "vcpu",
    "SingleAvailabilityZone": true,
    "InstanceRequirementsWithMetadata": {
        "ArchitectureTypes": ["arm64"],
        "VirtualizationTypes": ["hvm"],
        "InstanceRequirements": {
            "VCpuCount": {
                "Min": 1,
                "Max": 12
            },
            "MemoryMiB": {
                "Min": 512
            }
        }
    }
}
```
