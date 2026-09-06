

# Amazon ECS Managed Instances instance types
<a name="managed-instances-instance-types"></a>

When you create an Amazon ECS Managed Instances capacity provider, you choose how Amazon ECS selects EC2 instance types for your tasks. You can let Amazon ECS choose automatically, specify exact instance types or families, or define hardware attributes that instances must meet.

## Instance selection methods
<a name="managed-instances-instance-selection-methods"></a>

Amazon ECS Managed Instances provides two methods for selecting instance types:
+ *Specific instance type or family*: You specify exact instance types (such as `m6i.xlarge`) or instance families using wildcards (such as `c6i.*` or `m6*.*`). Use `allowedInstanceTypes` to include specific types, or `excludedInstanceTypes` to exclude types you don't want.
+ *Attribute-based selection*: You define hardware requirements (such as vCPU count, memory, CPU manufacturer, or accelerator type) and Amazon ECS selects instance types that match all of your specified attributes.

If you don't specify instance types or attributes, Amazon ECS automatically selects the most cost-optimized instance types based on your task definition requirements.

## Specific instance type selection
<a name="managed-instances-specific-instance-types"></a>

With specific instance type selection, you control exactly which EC2 instance types Amazon ECS Managed Instances can use. You can specify individual instance types, entire instance families, or a combination of both.

Use the `allowedInstanceTypes` field to specify which types to include, or the `excludedInstanceTypes` field to exclude types you don't want. Both fields support wildcards:
+ `m6i.xlarge` — a specific instance type
+ `c6i.*` — all sizes in the c6i family
+ `m6*.*` — all m6 generation families (m6i, m6a, m6g, etc.)

## Attribute-based instance type selection
<a name="managed-instances-attribute-based-selection"></a>

With attribute-based instance type selection, you define hardware requirements and Amazon ECS selects instance types that meet those requirements. This provides flexibility and helps ensure that your tasks are placed successfully even if specific instance types are not available.

When you specify multiple attributes, Amazon ECS selects instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, Amazon ECS selects instance types that satisfy any of the specified values.

You can filter by attributes in the following categories:
+ *CPU and memory* — vCPU count, memory (MiB), memory per vCPU ratio, CPU manufacturers (Intel, AMD, or AWS Graviton), and instance generation (current or previous).
+ *Local storage* — Include, exclude, or require local storage. Filter by storage type (HDD or SSD) and total storage capacity.
+ *Network and performance* — Network bandwidth (Gbps), network interface count, baseline EBS bandwidth (Mbps), burstable performance support, and bare metal instances.
+ *Accelerators* — Accelerator count, manufacturers, chip names, accelerator types, and total accelerator memory.
+ *Price protection* — Maximum Spot price and On-Demand price as a percentage of the lowest priced instance type that matches your requirements.

For the complete list of attributes and valid values, see [InstanceRequirementsRequest](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InstanceRequirementsRequest.html) in the *Amazon ECS API Reference*.

## Billing and purchase options
<a name="managed-instances-instance-billing-and-purchase-options"></a>

You choose a provisioning model when you create a capacity provider. The provisioning model determines how Amazon ECS Managed Instances acquires EC2 instances for your tasks:

On-Demand  
Pay for compute capacity by the hour with no long-term commitments or upfront payments. This is the default.

Spot  
You use spare EC2 capacity at a reduced price. Spot Instances can be interrupted when EC2 needs the capacity back. Set `capacityOptionType` to `Spot` when creating your capacity provider.

Capacity Reservations  
You reserve EC2 capacity in a specific Availability Zone. Set `capacityOptionType` to `Reserved` and provide a [capacity reservation group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-cr-group.html). You can also specify a reservation preference: `reservations-only`, `reservations-first`, or `reservations-excluded`.

Amazon ECS Managed Instances also automatically benefits from AWS Savings Plans and Reserved Instances that you've purchased for the instance types used by your tasks. No additional configuration is required.

## Amazon ECS Managed Instances supported instance types
<a name="managed-instances-instance-families"></a>

Amazon ECS Managed Instances supports the following instance types.
+ **Compute optimized: **C5 \| C5a \| C5ad \| C5d \| C5n \| C6a \| C6g \| C6gd \| C6i \| C6id \| C6in \| C7a \| C7g \| C7gd \| C7gn \| C7i \| C7i-flex \| C8a \| C8g \| C8gb \| C8gd \| C8gn \| C8i \| C8ib \| C8id \| C8i-flex \| C8in \| C8ine
+ **General purpose: **M5 \| M5a \| M5ad \| M5d \| M5dn \| M5n \| M5zn \| M6a \| M6g \| M6gd \| M6i \| M6id \| M6idn \| M6in \| M7a \| M7g \| M7gd \| M7i \| M7i-flex \| M8a \| M8azn \| M8g \| M8gb \| M8gd \| M8gn \| M8i \| M8ib \| M8id \| M8idb \| M8idn \| M8i-flex \| M8in \| M8ine \| M9g \| M9gd \| T3 \| T3a \| T4g
+ **Memory optimized: **R5 \| R5a \| R5ad \| R5b \| R5d \| R5dn \| R5n \| R6a \| R6g \| R6gd \| R6i \| R6id \| R6idn \| R6in \| R7a \| R7g \| R7gd \| R7i \| R7iz \| R8a \| R8g \| R8gb \| R8gd \| R8gn \| U-3tb1 \| U7i-6tb \| U7i-8tb \| U7i-12tb \| U7in-24tb \| U7in-32tb \| X2gd \| X2idn \| X2iedn \| X2iezn \| X8g \| Z1d
+ **Storage optimized: **D3 \| D3en \| I3en \| I4g \| I4i \| I7i \| I7ie \| I8g \| I8ge \| Im4gn \| Is4gen
+ **Accelerated computing: **DL1 \| G4ad \| G4dn \| G5 \| G5g \| G6 \| G6e \| G6f \| G7e \| Gr6 \| Gr6f \| Inf1 \| Inf2 \| P3dn \| P4d \| P4de \| P5 \| P5en \| P6-B200 \| P6-B300 \| Trn1
+ **High-performance computing: **Hpc6a \| Hpc6id \| Hpc7a \| Hpc7g

Additionally, Amazon ECS Managed Instances only creates instances that meet the following requirements.
+ More than 1 vCPU
+ Instance size is not nano or micro

For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html).