# Create an EC2 Fleet

To create an EC2 Fleet, define the fleet configuration in a JSON file and reference the
file with the [create-fleet](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md")
command. In the JSON file, you must specify the total target capacity for the fleet,
separate target capacities for Spot Instances and On-Demand Instances, and a launch template that defines the
configuration for the instances in the fleet, such as an AMI, instance type, subnet or
Availability Zone, and one or more security groups. You can optionally specify
additional configurations, such as parameters to override the launch template
configuration, allocation strategies for selecting Spot Instances and On-Demand Instances from the EC2
capacity pools, and the maximum amount you're willing to pay for the fleet. For more
information, see [Configuration options for your EC2 Fleet or
Spot Fleet](ec2-fleet-configuration-strategies.md "ec2-fleet-configuration-strategies.md").

The EC2 Fleet launches On-Demand Instances when capacity is available, and launches Spot Instances when your
maximum price exceeds the Spot price and capacity is available.

If your fleet includes Spot Instances and is of type `maintain`, Amazon EC2 will attempt
to maintain your fleet target capacity when your Spot Instances are interrupted.

## EC2 Fleet limitations

The following limitations apply to EC2 Fleet:

- Creating an EC2 Fleet is available only through the [Amazon EC2 API](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md"),
  [AWS CLI](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md"),
  [AWS SDKs](../APIReference/API_CreateFleet.md#API_CreateFleet_SeeAlso "../APIReference/API_CreateFleet.md#API_CreateFleet_SeeAlso"), and [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.md").
- An EC2 Fleet request can't span AWS Regions. You need to create a separate
  EC2 Fleet for each Region.
- An EC2 Fleet request can't span different subnets from the same Availability
  Zone.

## Create an EC2 Fleet

To launch a fleet of instances using EC2 Fleet, you need only specify the following
parameters in your fleet request, and the fleet will use the default values for the
other parameters:

- `LaunchTemplateId` or `LaunchTemplateName` –
  Specifies the launch template to use (which contains the parameters for the
  instances to launch, such as the instance type and Availability Zone)
- `TotalTargetCapacity` – Specifies the total target
  capacity for the fleet
- `DefaultTargetCapacityType` – Specifies whether the
  default purchasing option is On-Demand or Spot

To override the parameters specified in the launch template, you can specify one
or more overrides. Each override can vary by instance type, Availability Zone,
subnet, and maximum price, and can include a different weighted capacity. As an alternative to specifying an instance type, you can specify
the attributes that an instance must have, and Amazon EC2 will identify all the
instance types with those attributes. For more information, see [Specify attributes for
instance type selection for EC2 Fleet or Spot Fleet](ec2-fleet-attribute-based-instance-type-selection.md "ec2-fleet-attribute-based-instance-type-selection.md").

For EC2 Fleets of type `instant`, you can specify a Systems Manager
parameter instead of the AMI ID. You can specify the Systems Manager parameter in
the override or in the launch template. For more information, see [Use a Systems Manager parameter
instead of an AMI ID](create-launch-template.md#use-an-ssm-parameter-instead-of-an-ami-id "create-launch-template.md#use-an-ssm-parameter-instead-of-an-ami-id").

You can specify the fleet parameters in a JSON file. For information about all the
possible parameters you can specify, see [View all the EC2 Fleet configuration
options](#ec2-fleet-cli-skeleton "#ec2-fleet-cli-skeleton").

For fleet configuration examples, see [Example CLI configurations for EC2 Fleet](ec2-fleet-examples.md "ec2-fleet-examples.md").

There is currently no console support for creating an EC2 Fleet.

###### To create an EC2 Fleet

Use the [create-fleet](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md") command to create the fleet and specify
the JSON file that contains the fleet configuration parameters.

```
aws ec2 create-fleet --cli-input-json file://`file_name.json`
```

The following is example output for a fleet of type `request` or
`maintain`.

```
{
    "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE"
}
```

The following is example output for a fleet of type `instant` that
launched the target capacity.

```
{
  "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE",
  "Errors": [],
  "Instances": [
    {
      "LaunchTemplateAndOverrides": {
        "LaunchTemplateSpecification": {
          "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE",
          "Version": "1"
        },
        "Overrides": {
          "InstanceType": "c5.large",
          "AvailabilityZone": "us-east-1a"
        }
      },
      "Lifecycle": "on-demand",
      "InstanceIds": [
        "i-1234567890abcdef0",
        "i-9876543210abcdef9"
      ],
      "InstanceType": "c5.large",
      "Platform": null
    },
    {
      "LaunchTemplateAndOverrides": {
        "LaunchTemplateSpecification": {
          "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE",
          "Version": "1"
        },
        "Overrides": {
          "InstanceType": "c4.large",
          "AvailabilityZone": "us-east-1a"
        }
      },
      "Lifecycle": "on-demand",
      "InstanceIds": [
        "i-5678901234abcdef0",
        "i-5432109876abcdef9"
      ]
  ]
}
```

The following is example output for a fleet of type `instant` that
launched part of the target capacity with errors for instances that were not
launched.

```
{
  "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE",
  "Errors": [
    {
      "LaunchTemplateAndOverrides": {
        "LaunchTemplateSpecification": {
          "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE",
          "Version": "1"
        },
        "Overrides": {
          "InstanceType": "c4.xlarge",
          "AvailabilityZone": "us-east-1a",
        }
      },
      "Lifecycle": "on-demand",
      "ErrorCode": "InsufficientInstanceCapacity",
      "ErrorMessage": ""
    },
  ],
  "Instances": [
    {
      "LaunchTemplateAndOverrides": {
        "LaunchTemplateSpecification": {
          "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE",
          "Version": "1"
        },
        "Overrides": {
          "InstanceType": "c5.large",
          "AvailabilityZone": "us-east-1a"
        }
      },
      "Lifecycle": "on-demand",
      "InstanceIds": [
        "i-1234567890abcdef0",
        "i-9876543210abcdef9"
      ]
  ]
}
```

The following is example output for a fleet of type `instant` that
launched no instances.

```
{
  "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE",
  "Errors": [
    {
      "LaunchTemplateAndOverrides": {
        "LaunchTemplateSpecification": {
          "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE",
          "Version": "1"
        },
        "Overrides": {
          "InstanceType": "c4.xlarge",
          "AvailabilityZone": "us-east-1a",
        }
      },
      "Lifecycle": "on-demand",
      "ErrorCode": "InsufficientCapacity",
      "ErrorMessage": ""
    },
    {
      "LaunchTemplateAndOverrides": {
        "LaunchTemplateSpecification": {
          "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE",
          "Version": "1"
        },
        "Overrides": {
          "InstanceType": "c5.large",
          "AvailabilityZone": "us-east-1a",
        }
      },
      "Lifecycle": "on-demand",
      "ErrorCode": "InsufficientCapacity",
      "ErrorMessage": ""
    },
  ],
  "Instances": []
}
```

## Create an EC2 Fleet that replaces unhealthy

Spot Instances

EC2 Fleet checks the health status of the instances in the fleet every two minutes. The
health status of an instance is either `healthy` or
`unhealthy`.

EC2 Fleet determines the health status of an instance by using the status checks
provided by Amazon EC2. An instance is determined as `unhealthy` when the
status of either the instance status check or the system status check is
`impaired` for three consecutive health status checks. For more
information, see [Status checks for Amazon EC2
instances](monitoring-system-instance-status-check.md "monitoring-system-instance-status-check.md").

You can configure your fleet to replace unhealthy Spot Instances. After setting
`ReplaceUnhealthyInstances` to `true`, a Spot Instance is replaced
when it is reported as `unhealthy`. The fleet can go below its target
capacity for up to a few minutes while an unhealthy Spot Instance is being replaced.

###### Requirements

- Health check replacement is supported only for EC2 Fleets that maintain a
  target capacity (fleets of type `maintain`), and not for fleets
  of type `request` or `instant`.
- Health check replacement is supported only for Spot Instances. This feature is not
  supported for On-Demand Instances.
- You can configure your EC2 Fleet to replace unhealthy instances only when you
  create it.
- Users can use health check replacement only if they have permission to
  call the `ec2:DescribeInstanceStatus` action.

###### To configure an EC2 Fleet to replace unhealthy Spot Instances

1. Use the information for creating an EC2 Fleet in [Create an EC2 Fleet](#create-ec2-fleet-procedure "#create-ec2-fleet-procedure").
2. To configure the fleet to replace unhealthy Spot Instances, in the JSON file, for
   `ReplaceUnhealthyInstances`, specify `true`.

## View all the EC2 Fleet configuration

options

To view the full list of EC2 Fleet configuration parameters, you can generate a JSON
file. For a description of each parameter, see [create-fleet](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md").

###### To generate a JSON file with all possible EC2 Fleet parameters

Use the [create-fleet](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md")
(AWS CLI) command and the `--generate-cli-skeleton` parameter to
generate an EC2 Fleet JSON file, and direct the output to a file to save it.

```
aws ec2 create-fleet \
    --generate-cli-skeleton input > `ec2createfleet.json`
```

The following is example output.

```
{
    "DryRun": true,
    "ClientToken": "",
    "SpotOptions": {
        "AllocationStrategy": "price-capacity-optimized",
        "MaintenanceStrategies": {
            "CapacityRebalance": {
                "ReplacementStrategy": "launch"
            }
        },
        "InstanceInterruptionBehavior": "hibernate",
        "InstancePoolsToUseCount": 0,
        "SingleInstanceType": true,
        "SingleAvailabilityZone": true,
        "MinTargetCapacity": 0,
        "MaxTotalPrice": ""
    },
    "OnDemandOptions": {
        "AllocationStrategy": "prioritized",
        "CapacityReservationOptions": {
            "UsageStrategy": "use-capacity-reservations-first"
        },
        "SingleInstanceType": true,
        "SingleAvailabilityZone": true,
        "MinTargetCapacity": 0,
        "MaxTotalPrice": ""
    },
    "ExcessCapacityTerminationPolicy": "termination",
    "LaunchTemplateConfigs": [
        {
            "LaunchTemplateSpecification": {
                "LaunchTemplateId": "",
                "LaunchTemplateName": "",
                "Version": ""
            },
            "Overrides": [
                {
                    "InstanceType": "r5.metal",
                    "MaxPrice": "",
                    "SubnetId": "",
                    "AvailabilityZone": "",
                    "WeightedCapacity": 0.0,
                    "Priority": 0.0,
                    "Placement": {
                        "AvailabilityZone": "",
                        "Affinity": "",
                        "GroupName": "",
                        "PartitionNumber": 0,
                        "HostId": "",
                        "Tenancy": "dedicated",
                        "SpreadDomain": "",
                        "HostResourceGroupArn": ""
                    },
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
                        "BareMetal": "included",
                        "BurstablePerformance": "required",
                        "RequireHibernateSupport": true,
                        "NetworkInterfaceCount": {
                            "Min": 0,
                            "Max": 0
                        },
                        "LocalStorage": "excluded",
                        "LocalStorageTypes": [
                            "ssd"
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
                            "inference"
                        ],
                        "AcceleratorCount": {
                            "Min": 0,
                            "Max": 0
                        },
                        "AcceleratorManufacturers": [
                            "amd"
                        ],
                        "AcceleratorNames": [
                            "a100"
                        ],
                        "AcceleratorTotalMemoryMiB": {
                            "Min": 0,
                            "Max": 0
                        }
                    }
                }
            ]
        }
    ],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": 0,
        "OnDemandTargetCapacity": 0,
        "SpotTargetCapacity": 0,
        "DefaultTargetCapacityType": "on-demand",
        "TargetCapacityUnitType": "memory-mib"
    },
    "TerminateInstancesWithExpiration": true,
    "Type": "instant",
    "ValidFrom": "1970-01-01T00:00:00",
    "ValidUntil": "1970-01-01T00:00:00",
    "ReplaceUnhealthyInstances": true,
    "TagSpecifications": [
        {
            "ResourceType": "fleet",
            "Tags": [
                {
                    "Key": "",
                    "Value": ""
                }
            ]
        }
    ],
    "Context": ""
}
```
