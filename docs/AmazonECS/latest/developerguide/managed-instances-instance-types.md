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

The following attributes are supported for attribute-based instance type selection:

- _cpuArchitecture_: The CPU architecture (X86_64 or ARM64).
- _instanceGeneration_: The instance generation (current, previous, or all).
- _burstablePerformance_: Whether to include burstable performance instances (included, excluded, or required).
- _cpuManufacturer_: The CPU manufacturer (intel, amd, or amazon-web-services).
- _networkBandwidth_: The minimum network bandwidth in Gbps.
- _networkInterfaceCount_: The minimum number of network interfaces.
- _localStorage_: Whether local storage is required (included, excluded, or required).
- _localStorageType_: The type of local storage (hdd or ssd).

## Cost optimization

Amazon ECS Managed Instances supports several features to help optimize the cost of your containerized workloads:

- _Reserved Instances (RIs)_: Amazon ECS Managed Instances tasks can benefit from RIs that you've purchased for the instance types used by your tasks.
- _Multi-task placement_: Amazon ECS Managed Instances places multiple tasks on a single general-purpose instance by default, optimizing resource utilization and cost.
