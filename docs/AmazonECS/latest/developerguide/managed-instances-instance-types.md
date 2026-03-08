# Amazon ECS Managed Instances instance types

Amazon ECS Managed Instances allows you to select specific EC2 instance types for your containerized
applications.

## Amazon ECS Managed Instances Instance Families

The following instance types are supported:

### General Purpose

- m5, m5a, m5ad, m5d, m5dn, m5n, m5zn: Balanced compute, memory, and networking
- m6a, m6g, m6gd, m6i, m6id, m6idn, m6in: Latest generation with improved performance
- m7a, m7g, m7gd, m7i, m7i-flex: Next generation general purpose instances
- m8g, m8gd: Latest generation ARM general purpose instances
- t3, t3a, t4g: Burstable performance instances (excluding nano and micro instance sizes)

### Compute Optimized

- c5, c5a, c5ad, c5d, c5n: High-performance processors for compute-intensive applications
- c6a, c6g, c6gd, c6i, c6id, c6in: Latest generation compute-optimized instances
- c7a, c7g, c7gd, c7gn, c7i, c7i-flex: Next generation compute optimized instances
- c8g, c8gd, c8gn: Latest generation ARM compute optimized instances
- hpc6a, hpc6id, hpc7a: High performance computing instances

### Memory Optimized

- r5, r5a, r5ad, r5b, r5d, r5dn, r5n: High memory-to-vCPU ratio for memory-intensive applications
- r6a, r6g, r6gd, r6i, r6id, r6idn, r6in: Latest generation memory-optimized instances
- r7a, r7g, r7gd, r7i, r7iz: Next generation memory optimized instances
- r8g, r8gd: Latest generation ARM memory optimized instances
- u-3tb1, u7i-6tb, u7i-8tb, u7i-12tb, u7in-24tb, u7in-32tb: High memory instances with up to 32 TB RAM
- x2gd, x2idn, x2iedn, x2iezn: Extreme memory for in-memory databases and analytics
- x8g: Latest generation extreme memory instances
- z1d: High frequency and NVMe SSD storage

### Storage Optimized

- d3, d3en: Dense HDD storage for distributed file systems
- i4g, i4i: Latest generation storage optimized instances
- i7i, i7ie, i8g: Next generation high-performance storage instances
- im4gn, is4gen: Network optimized storage instances

### Accelerated Computing

- g4dn: NVIDIA T4 GPUs for machine learning inference and graphics
- g5, g5g: NVIDIA A10G GPUs for high-performance graphics and ML
- g6, g6e, g6f: Latest generation GPU instances
- gr6, gr6f: GPU instances with NVIDIA L4 Tensor Core GPUs and 1:8 vCPU:RAM ratio for graphics workloads
- p3dn: NVIDIA V100 GPUs for deep learning training and HPC
- p4d: NVIDIA A100 GPUs for highest performance ML training
- p5: Latest generation with NVIDIA H100 GPUs
- p6-b200: Next generation with NVIDIA B200 GPUs

## Instance selection methods

Amazon ECS Managed Instances provides two methods for selecting instance types:

- _Specific instance type selection_: You explicitly specify the EC2 instance type to use for your tasks.
- _Attribute-based instance type selection_: You specify the attributes (such as vCPU, memory, and architecture) that your application requires, and Amazon ECS Managed Instances selects an appropriate instance type.

## Specific instance type selection

With specific instance type selection, you explicitly specify the EC2 instance type to use for your Amazon ECS Managed Instances tasks. This is useful when your application requires a specific instance type with particular hardware characteristics.

## Attribute-based instance type selection

With attribute-based instance type selection, you specify the attributes that your application requires, and Amazon ECS Managed Instances selects an appropriate instance type that meets those requirements. This provides more flexibility and can help ensure that your tasks are placed successfully even if specific instance types are not available.

When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.

The following attributes are supported for attribute-based instance type selection:

**cpuArchitecture**

The CPU architecture.

Valid values: `X86_64` | `ARM64`

**instanceGeneration**

Indicates whether current or previous generation instance types are included.

- For current generation instance types, specify `current`. The current generation includes EC2 instance types currently recommended for use. This typically includes the latest two to three generations in each instance family. For more information, see [Instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") in the _Amazon EC2 User Guide_.
- For previous generation instance types, specify `previous`.
- To include both current and previous generation instance types, specify `all`.

Valid values: `current` | `previous` | `all`

Default: Any current or previous generation.

**burstablePerformance**

Indicates whether burstable performance instance types are included, excluded, or required. For more information, see [Burstable performance instances](../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md "../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md") in the _Amazon EC2 User Guide_.

Valid values: `included` | `excluded` | `required`

Default: `excluded`

**cpuManufacturer**

Lists which specific CPU manufacturers to include.

- For instance types with Intel CPUs, specify `intel`.
- For instance types with AMD CPUs, specify `amd`.
- For instance types with AWS CPUs (such as AWS Graviton), specify `amazon-web-services`.

###### Note

Don't confuse the CPU hardware manufacturer with the CPU hardware architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify.

Valid values: `intel` | `amd` | `amazon-web-services`

Default: Any manufacturer.

**networkBandwidth**

The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).

Default: No minimum or maximum limits.

**networkInterfaceCount**

The minimum and maximum number of network interfaces.

Default: No minimum or maximum limits.

**localStorage**

Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, see [Amazon EC2 instance store](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md") in the _Amazon EC2 User Guide_.

Valid values: `included` | `excluded` | `required`

Default: `included`

**localStorageType**

Indicates the type of local storage that is required.

- For instance types with hard disk drive (HDD) storage, specify `hdd`.
- For instance types with solid state drive (SSD) storage, specify `ssd`.

Valid values: `hdd` | `ssd`

Default: Any local storage type.

## Billing and purchase options

Amazon ECS Managed Instances supports several features to help optimize the cost of your containerized workloads:

- _Savings Plans (SPs)_: Amazon ECS Managed Instances benefit from Savings Plans that you've purchased for the instance types used by your tasks. No additional configuration is required.
- _Reserved Instances (RIs)_: Amazon ECS Managed Instances tasks can benefit from RIs that you've purchased for the instance types used by your tasks. No additional configuration is required.
- _Spot Instances_: You can configure Amazon ECS Managed Instances capacity provider to use EC2 Spot instances by setting `capacityOptionType=Spot`
- _Capacity Reservations_: You can configure Amazon ECS Managed Instances capacity provider to use your EC2 Capacity Reservations by setting `capacityOptionType=Reserved` and providing a [capacity reservation group](../../../AWSEC2/latest/UserGuide/create-cr-group.md "../../../AWSEC2/latest/UserGuide/create-cr-group.md"). You can also specify following reservation preferences: use `reservations-only` to ensure instances launch exclusively in reserved capacity for maximum predictability, `reservations-first` to prefer reservations while maintaining flexibility to fall back to on-demand capacity when needed, or `reservations-excluded` to prevent your capacity provider from using reservations altogether.
