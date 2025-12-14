# ENA queues

ENA queues are allocated to network interfaces with default static limits based on
the instance type and size. On supported instance types, you can dynamically
allocate these queues across Elastic Network Interfaces (ENIs). While the total
queue count per instance depends on its type and size, you can configure multiple
ENIs with ENA queues until you meet the maximum queue count for the ENI and the
instance.

Flexible ENA queue allocation optimizes resource distribution, enabling maximum
vCPU utilization. High network performance workloads typically require multiple ENA
queues. You can fine-tune network performance and packets per second (PPS) by
adjusting queue counts according to your specific workload needs. For example,
network-intensive applications may require more queues compared to CPU-intensive
applications.

###### Topics

- [Supported instances](#supported-instances "#supported-instances")
- [Modify the number of queues](#modify "#modify")

## Supported instances

The following instances support dynamic allocation of multiple ENA queues.

### General purpose

| Instance type       | Default ENA queues per interface | Maximum ENA queues per interface | Maximum ENA queues per instance |
| ------------------- | -------------------------------- | -------------------------------- | ------------------------------- |
| **M6i**             |
| `m6i.large`         | 2                                | 2                                | 6                               |
| `m6i.xlarge`        | 4                                | 4                                | 16                              |
| `m6i.2xlarge`       | 8                                | 8                                | 32                              |
| `m6i.4xlarge`       | 8                                | 16                               | 64                              |
| `m6i.8xlarge`       | 8                                | 32                               | 64                              |
| `m6i.12xlarge`      | 8                                | 32                               | 64                              |
| `m6i.16xlarge`      | 8                                | 32                               | 120                             |
| `m6i.24xlarge`      | 8                                | 32                               | 120                             |
| `m6i.32xlarge`      | 8                                | 32                               | 120                             |
| **M6id**            |
| `m6id.large`        | 2                                | 2                                | 6                               |
| `m6id.xlarge`       | 4                                | 4                                | 16                              |
| `m6id.2xlarge`      | 8                                | 8                                | 32                              |
| `m6id.4xlarge`      | 8                                | 16                               | 64                              |
| `m6id.8xlarge`      | 8                                | 32                               | 64                              |
| `m6id.12xlarge`     | 8                                | 32                               | 64                              |
| `m6id.16xlarge`     | 8                                | 32                               | 120                             |
| `m6id.24xlarge`     | 8                                | 32                               | 120                             |
| `m6id.32xlarge`     | 8                                | 32                               | 120                             |
| **M6idn**           |
| `m6idn.large`       | 2                                | 2                                | 6                               |
| `m6idn.xlarge`      | 4                                | 4                                | 16                              |
| `m6idn.2xlarge`     | 8                                | 8                                | 32                              |
| `m6idn.4xlarge`     | 8                                | 16                               | 64                              |
| `m6idn.8xlarge`     | 16                               | 32                               | 128                             |
| `m6idn.12xlarge`    | 16                               | 32                               | 128                             |
| `m6idn.16xlarge`    | 16                               | 32                               | 240                             |
| `m6idn.24xlarge`    | 32                               | 32                               | 480                             |
| `m6idn.32xlarge`    | 32                               | 32                               | 512 \*                          |
| **M6in**            |
| `m6in.large`        | 2                                | 2                                | 6                               |
| `m6in.xlarge`       | 4                                | 4                                | 16                              |
| `m6in.2xlarge`      | 8                                | 8                                | 32                              |
| `m6in.4xlarge`      | 8                                | 16                               | 64                              |
| `m6in.8xlarge`      | 16                               | 32                               | 128                             |
| `m6in.12xlarge`     | 16                               | 32                               | 128                             |
| `m6in.16xlarge`     | 16                               | 32                               | 240                             |
| `m6in.24xlarge`     | 32                               | 32                               | 480                             |
| `m6in.32xlarge`     | 32                               | 32                               | 512 \*                          |
| **M8a**             |
| `m8a.medium`        | 1                                | 1                                | 3                               |
| `m8a.large`         | 2                                | 2                                | 6                               |
| `m8a.xlarge`        | 4                                | 4                                | 16                              |
| `m8a.2xlarge`       | 8                                | 8                                | 32                              |
| `m8a.4xlarge`       | 8                                | 16                               | 64                              |
| `m8a.8xlarge`       | 8                                | 32                               | 128                             |
| `m8a.12xlarge`      | 16                               | 64                               | 192                             |
| `m8a.16xlarge`      | 16                               | 64                               | 256                             |
| `m8a.24xlarge`      | 16                               | 128                              | 384                             |
| `m8a.48xlarge`      | 32                               | 128                              | 768                             |
| `m8a.metal-24xl`    | 16                               | 128                              | 384                             |
| `m8a.metal-48xl`    | 32                               | 128                              | 768                             |
| **M8i**             |
| `m8i.large`         | 2                                | 2                                | 6                               |
| `m8i.xlarge`        | 4                                | 4                                | 16                              |
| `m8i.2xlarge`       | 8                                | 8                                | 32                              |
| `m8i.4xlarge`       | 8                                | 16                               | 64                              |
| `m8i.8xlarge`       | 8                                | 32                               | 128                             |
| `m8i.12xlarge`      | 16                               | 64                               | 192                             |
| `m8i.16xlarge`      | 16                               | 64                               | 256                             |
| `m8i.24xlarge`      | 16                               | 128                              | 384                             |
| `m8i.32xlarge`      | 16                               | 128                              | 512                             |
| `m8i.48xlarge`      | 32                               | 128                              | 768                             |
| `m8i.96xlarge`      | 32                               | 128                              | 1536                            |
| `m8i.metal-48xl`    | 32                               | 128                              | 768                             |
| `m8i.metal-96xl`    | 32                               | 128                              | 1536                            |
| **M8i-flex**        |
| `m8i-flex.large`    | 1                                | 1                                | 3                               |
| `m8i-flex.xlarge`   | 2                                | 2                                | 8                               |
| `m8i-flex.2xlarge`  | 4                                | 4                                | 16                              |
| `m8i-flex.4xlarge`  | 4                                | 8                                | 32                              |
| `m8i-flex.8xlarge`  | 4                                | 16                               | 64                              |
| `m8i-flex.12xlarge` | 8                                | 32                               | 96                              |
| `m8i-flex.16xlarge` | 8                                | 32                               | 128                             |

###### Note

\* These instance types feature multiple network cards. Other instance types feature a
single network card. For more information, see [Network cards](using-eni.md#network-cards "using-eni.md#network-cards").

### Compute optimized

| Instance type       | Default ENA queues per interface | Maximum ENA queues per interface | Maximum ENA queues per instance |
| ------------------- | -------------------------------- | -------------------------------- | ------------------------------- |
| **C6i**             |
| `c6i.large`         | 2                                | 2                                | 6                               |
| `c6i.xlarge`        | 4                                | 4                                | 16                              |
| `c6i.2xlarge`       | 8                                | 8                                | 32                              |
| `c6i.4xlarge`       | 8                                | 16                               | 64                              |
| `c6i.8xlarge`       | 8                                | 32                               | 64                              |
| `c6i.12xlarge`      | 8                                | 32                               | 64                              |
| `c6i.16xlarge`      | 8                                | 32                               | 120                             |
| `c6i.24xlarge`      | 8                                | 32                               | 120                             |
| `c6i.32xlarge`      | 8                                | 32                               | 120                             |
| **C6id**            |
| `c6id.large`        | 2                                | 2                                | 6                               |
| `c6id.xlarge`       | 4                                | 4                                | 16                              |
| `c6id.2xlarge`      | 8                                | 8                                | 32                              |
| `c6id.4xlarge`      | 8                                | 16                               | 64                              |
| `c6id.8xlarge`      | 8                                | 32                               | 64                              |
| `c6id.12xlarge`     | 8                                | 32                               | 64                              |
| `c6id.16xlarge`     | 8                                | 32                               | 120                             |
| `c6id.24xlarge`     | 8                                | 32                               | 120                             |
| `c6id.32xlarge`     | 8                                | 32                               | 120                             |
| **C6in**            |
| `c6in.large`        | 2                                | 2                                | 6                               |
| `c6in.xlarge`       | 4                                | 4                                | 16                              |
| `c6in.2xlarge`      | 8                                | 8                                | 32                              |
| `c6in.4xlarge`      | 8                                | 16                               | 64                              |
| `c6in.8xlarge`      | 16                               | 32                               | 128                             |
| `c6in.12xlarge`     | 16                               | 32                               | 128                             |
| `c6in.16xlarge`     | 16                               | 32                               | 240                             |
| `c6in.24xlarge`     | 32                               | 32                               | 480                             |
| `c6in.32xlarge`     | 32                               | 32                               | 512 \*                          |
| **C8a**             |
| `c8a.medium`        | 1                                | 1                                | 3                               |
| `c8a.large`         | 2                                | 2                                | 6                               |
| `c8a.xlarge`        | 4                                | 4                                | 16                              |
| `c8a.2xlarge`       | 8                                | 8                                | 32                              |
| `c8a.4xlarge`       | 8                                | 16                               | 64                              |
| `c8a.8xlarge`       | 8                                | 32                               | 128                             |
| `c8a.12xlarge`      | 16                               | 64                               | 192                             |
| `c8a.16xlarge`      | 16                               | 64                               | 256                             |
| `c8a.24xlarge`      | 16                               | 128                              | 384                             |
| `c8a.48xlarge`      | 32                               | 128                              | 768                             |
| `c8a.metal-24xl`    | 16                               | 128                              | 384                             |
| `c8a.metal-48xl`    | 32                               | 128                              | 768                             |
| **C8gb**            |
| `c8gb.medium`       | 1                                | 1                                | 2                               |
| `c8gb.large`        | 2                                | 2                                | 6                               |
| `c8gb.xlarge`       | 4                                | 4                                | 16                              |
| `c8gb.2xlarge`      | 8                                | 8                                | 32                              |
| `c8gb.4xlarge`      | 8                                | 16                               | 64                              |
| `c8gb.8xlarge`      | 8                                | 32                               | 128                             |
| `c8gb.12xlarge`     | 16                               | 64                               | 192                             |
| `c8gb.16xlarge`     | 16                               | 64                               | 256                             |
| `c8gb.24xlarge`     | 16                               | 128                              | 384                             |
| `c8gb.metal-24xl`   | 32                               | 128                              | 768                             |
| **C8gn**            |
| `c8gn.medium`       | 1                                | 1                                | 2                               |
| `c8gn.large`        | 2                                | 2                                | 6                               |
| `c8gn.xlarge`       | 4                                | 4                                | 16                              |
| `c8gn.2xlarge`      | 8                                | 8                                | 32                              |
| `c8gn.4xlarge`      | 8                                | 16                               | 64                              |
| `c8gn.8xlarge`      | 8                                | 32                               | 128                             |
| `c8gn.12xlarge`     | 16                               | 64                               | 192                             |
| `c8gn.16xlarge`     | 16                               | 64                               | 256                             |
| `c8gn.24xlarge`     | 16                               | 128                              | 384                             |
| `c8gn.48xlarge`     | 32                               | 128                              | 768 \*                          |
| `c8gn.metal-24xl`   | 32                               | 128                              | 768                             |
| `c8gn.metal-48xl`   | 32                               | 128                              | 768 \*                          |
| **C8i**             |
| `c8i.large`         | 2                                | 2                                | 6                               |
| `c8i.xlarge`        | 4                                | 4                                | 16                              |
| `c8i.2xlarge`       | 8                                | 8                                | 32                              |
| `c8i.4xlarge`       | 8                                | 16                               | 64                              |
| `c8i.8xlarge`       | 8                                | 32                               | 128                             |
| `c8i.12xlarge`      | 16                               | 64                               | 192                             |
| `c8i.16xlarge`      | 16                               | 64                               | 256                             |
| `c8i.24xlarge`      | 16                               | 128                              | 384                             |
| `c8i.32xlarge`      | 16                               | 128                              | 512                             |
| `c8i.48xlarge`      | 32                               | 128                              | 768                             |
| `c8i.96xlarge`      | 32                               | 128                              | 1536                            |
| `c8i.metal-48xl`    | 32                               | 128                              | 768                             |
| `c8i.metal-96xl`    | 32                               | 128                              | 1536                            |
| **C8i-flex**        |
| `c8i-flex.large`    | 1                                | 1                                | 3                               |
| `c8i-flex.xlarge`   | 2                                | 2                                | 8                               |
| `c8i-flex.2xlarge`  | 4                                | 4                                | 16                              |
| `c8i-flex.4xlarge`  | 4                                | 8                                | 32                              |
| `c8i-flex.8xlarge`  | 4                                | 16                               | 64                              |
| `c8i-flex.12xlarge` | 8                                | 32                               | 96                              |
| `c8i-flex.16xlarge` | 8                                | 32                               | 128                             |

###### Note

\* These instance types feature multiple network cards. Other instance types feature a
single network card. For more information, see [Network cards](using-eni.md#network-cards "using-eni.md#network-cards").

### Memory optimized

| Instance type       | Default ENA queues per interface | Maximum ENA queues per interface | Maximum ENA queues per instance |
| ------------------- | -------------------------------- | -------------------------------- | ------------------------------- |
| **R6i**             |
| `r6i.large`         | 2                                | 2                                | 6                               |
| `r6i.xlarge`        | 4                                | 4                                | 16                              |
| `r6i.2xlarge`       | 8                                | 8                                | 32                              |
| `r6i.4xlarge`       | 8                                | 16                               | 64                              |
| `r6i.8xlarge`       | 8                                | 32                               | 64                              |
| `r6i.12xlarge`      | 8                                | 32                               | 64                              |
| `r6i.16xlarge`      | 8                                | 32                               | 120                             |
| `r6i.24xlarge`      | 8                                | 32                               | 120                             |
| `r6i.32xlarge`      | 8                                | 32                               | 120                             |
| **R6id**            |
| `r6id.large`        | 2                                | 2                                | 6                               |
| `r6id.xlarge`       | 4                                | 4                                | 16                              |
| `r6id.2xlarge`      | 8                                | 8                                | 32                              |
| `r6id.4xlarge`      | 8                                | 16                               | 64                              |
| `r6id.8xlarge`      | 8                                | 32                               | 64                              |
| `r6id.12xlarge`     | 8                                | 32                               | 64                              |
| `r6id.16xlarge`     | 8                                | 32                               | 120                             |
| `r6id.24xlarge`     | 8                                | 32                               | 120                             |
| `r6id.32xlarge`     | 8                                | 32                               | 120                             |
| **R6idn**           |
| `r6idn.large`       | 2                                | 2                                | 6                               |
| `r6idn.xlarge`      | 4                                | 4                                | 16                              |
| `r6idn.2xlarge`     | 8                                | 8                                | 32                              |
| `r6idn.4xlarge`     | 8                                | 16                               | 64                              |
| `r6idn.8xlarge`     | 16                               | 32                               | 128                             |
| `r6idn.12xlarge`    | 16                               | 32                               | 128                             |
| `r6idn.16xlarge`    | 16                               | 32                               | 240                             |
| `r6idn.24xlarge`    | 32                               | 32                               | 480                             |
| `r6idn.32xlarge`    | 32                               | 32                               | 512 \*                          |
| **R6in**            |
| `r6in.large`        | 2                                | 2                                | 6                               |
| `r6in.xlarge`       | 4                                | 4                                | 16                              |
| `r6in.2xlarge`      | 8                                | 8                                | 32                              |
| `r6in.4xlarge`      | 8                                | 16                               | 64                              |
| `r6in.8xlarge`      | 16                               | 32                               | 128                             |
| `r6in.12xlarge`     | 16                               | 32                               | 128                             |
| `r6in.16xlarge`     | 16                               | 32                               | 240                             |
| `r6in.24xlarge`     | 32                               | 32                               | 480                             |
| `r6in.32xlarge`     | 32                               | 32                               | 512 \*                          |
| **R8a**             |
| `r8a.medium`        | 1                                | 1                                | 3                               |
| `r8a.large`         | 2                                | 2                                | 6                               |
| `r8a.xlarge`        | 4                                | 4                                | 16                              |
| `r8a.2xlarge`       | 8                                | 8                                | 32                              |
| `r8a.4xlarge`       | 8                                | 16                               | 64                              |
| `r8a.8xlarge`       | 8                                | 32                               | 128                             |
| `r8a.12xlarge`      | 16                               | 64                               | 192                             |
| `r8a.16xlarge`      | 16                               | 64                               | 256                             |
| `r8a.24xlarge`      | 16                               | 128                              | 384                             |
| `r8a.48xlarge`      | 32                               | 128                              | 768                             |
| `r8a.metal-24xl`    | 16                               | 128                              | 384                             |
| `r8a.metal-48xl`    | 32                               | 128                              | 768                             |
| **R8gb**            |
| `r8gb.medium`       | 1                                | 1                                | 2                               |
| `r8gb.large`        | 2                                | 2                                | 6                               |
| `r8gb.xlarge`       | 4                                | 4                                | 16                              |
| `r8gb.2xlarge`      | 8                                | 8                                | 32                              |
| `r8gb.4xlarge`      | 8                                | 16                               | 64                              |
| `r8gb.8xlarge`      | 8                                | 32                               | 128                             |
| `r8gb.12xlarge`     | 16                               | 64                               | 192                             |
| `r8gb.16xlarge`     | 16                               | 64                               | 256                             |
| `r8gb.24xlarge`     | 16                               | 128                              | 384                             |
| `r8gb.metal-24xl`   | 32                               | 128                              | 768                             |
| **R8gn**            |
| `r8gn.medium`       | 1                                | 1                                | 2                               |
| `r8gn.large`        | 2                                | 2                                | 6                               |
| `r8gn.xlarge`       | 4                                | 4                                | 16                              |
| `r8gn.2xlarge`      | 8                                | 8                                | 32                              |
| `r8gn.4xlarge`      | 8                                | 16                               | 64                              |
| `r8gn.8xlarge`      | 8                                | 32                               | 128                             |
| `r8gn.12xlarge`     | 16                               | 64                               | 192                             |
| `r8gn.16xlarge`     | 16                               | 64                               | 256                             |
| `r8gn.24xlarge`     | 16                               | 128                              | 384                             |
| `r8gn.48xlarge`     | 32                               | 128                              | 768 \*                          |
| `r8gn.metal-24xl`   | 32                               | 128                              | 768                             |
| `r8gn.metal-48xl`   | 32                               | 128                              | 768 \*                          |
| **R8i**             |
| `r8i.large`         | 2                                | 2                                | 6                               |
| `r8i.xlarge`        | 4                                | 4                                | 16                              |
| `r8i.2xlarge`       | 8                                | 8                                | 32                              |
| `r8i.4xlarge`       | 8                                | 16                               | 64                              |
| `r8i.8xlarge`       | 8                                | 32                               | 128                             |
| `r8i.12xlarge`      | 16                               | 64                               | 192                             |
| `r8i.16xlarge`      | 16                               | 64                               | 256                             |
| `r8i.24xlarge`      | 16                               | 128                              | 384                             |
| `r8i.32xlarge`      | 16                               | 128                              | 512                             |
| `r8i.48xlarge`      | 32                               | 128                              | 768                             |
| `r8i.96xlarge`      | 32                               | 128                              | 1536                            |
| `r8i.metal-48xl`    | 32                               | 128                              | 768                             |
| `r8i.metal-96xl`    | 32                               | 128                              | 1536                            |
| **R8i-flex**        |
| `r8i-flex.large`    | 1                                | 1                                | 3                               |
| `r8i-flex.xlarge`   | 2                                | 2                                | 8                               |
| `r8i-flex.2xlarge`  | 4                                | 4                                | 16                              |
| `r8i-flex.4xlarge`  | 4                                | 8                                | 32                              |
| `r8i-flex.8xlarge`  | 4                                | 16                               | 64                              |
| `r8i-flex.12xlarge` | 8                                | 32                               | 96                              |
| `r8i-flex.16xlarge` | 8                                | 32                               | 128                             |
| **X8aedz**          |
| `x8aedz.large`      | 2                                | 2                                | 8                               |
| `x8aedz.xlarge`     | 4                                | 4                                | 16                              |
| `x8aedz.3xlarge`    | 4                                | 16                               | 48                              |
| `x8aedz.6xlarge`    | 8                                | 32                               | 96                              |
| `x8aedz.12xlarge`   | 8                                | 64                               | 192                             |
| `x8aedz.24xlarge`   | 16                               | 128                              | 384                             |
| `x8aedz.metal-12xl` | 8                                | 64                               | 192                             |
| `x8aedz.metal-24xl` | 16                               | 128                              | 384                             |

###### Note

\* These instance types feature multiple network cards. Other instance types feature a
single network card. For more information, see [Network cards](using-eni.md#network-cards "using-eni.md#network-cards").

## Modify the number of queues

You can modify the number of ENA queues using AWS Management Console or AWS CLI. In the
AWS Management Console, the ENA queues configuration is available under each **Network interface** setting.

To modify the number of ENA queues using the AWS CLI, use either one of the
following commands. Before modifying the queue count, use the following command
to check your current queue count.

```
aws ec2 describe-instances --instance-id i-`1234567890abcdef0`
```

###### Note

- Your instance must be stopped before modifying the number of ENA
  queues.
- The value for ENA queues must be a power of 2, such as, 1, 2, 4,
  8, 16, 32, etc.
- The number of queues allocated to any single ENI cannot exceed the
  number of vCPUs available on your instance.

`**attach-network-interface**`

In the following example, 32 ENA queues are configured on an ENI.

```
aws ec2 attach-network-interface \
  --network-interface-id eni-`001aa1bb223cdd4e4` \
  --instance-id `i-1234567890abcdef0` \
  --device-index 1 \
  --ena-queue-count 32
```

`**run-instances**`

In the following example, 2 ENA queues each are configured on 3 ENIs.

```
aws ec2 run-instances \
  --image-id ami-`12ab3c30` \
  --instance-type c6i.large \
  --min-count 1 \
  --max-count 1 \
  --network-interfaces \
    "[{\"DeviceIndex\":0,\"SubnetId\":\"subnet-`123456789012a345a`\",\"EnaQueueCount\":2},
      {\"DeviceIndex\":1,\"SubnetId\":\"subnet-`123456789012a345a`\",\"EnaQueueCount\":2},
      {\"DeviceIndex\":2,\"SubnetId\":\"subnet-`123456789012a345a`\",\"EnaQueueCount\":2}]"
```

`**modify-network-interface-attribute**`

In the following example, 32 ENA queues are configured on an ENI.

```
aws ec2 modify-network-interface-attribute \
--network-interface-id eni-`1234567890abcdef0` \
--attachment AttachmentId=eni-attach-`12345678`,EnaQueueCount=32
```

In the following example, the ENA count is reset to the default value.

```
aws ec2 modify-network-interface-attribute \
--network-interface-id eni-`1234567890abcdef0` \
--attachment AttachmentId=eni-attach-`12345678`,DefaultEnaQueueCount=true
```
