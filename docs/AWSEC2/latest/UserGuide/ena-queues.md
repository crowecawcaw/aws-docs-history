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
| **M8azn**           |
| `m8azn.medium`      | 1                                | 1                                | 3                               |
| `m8azn.large`       | 2                                | 2                                | 8                               |
| `m8azn.xlarge`      | 4                                | 4                                | 16                              |
| `m8azn.3xlarge`     | 4                                | 16                               | 48                              |
| `m8azn.6xlarge`     | 8                                | 32                               | 96                              |
| `m8azn.12xlarge`    | 8                                | 64                               | 192                             |
| `m8azn.24xlarge`    | 16                               | 128                              | 384                             |
| `m8azn.metal-12xl`  | 8                                | 64                               | 192                             |
| `m8azn.metal-24xl`  | 16                               | 128                              | 384                             |
| **M8gb**            |
| `m8gb.medium`       | 1                                | 1                                | 2                               |
| `m8gb.large`        | 2                                | 2                                | 6                               |
| `m8gb.xlarge`       | 4                                | 4                                | 16                              |
| `m8gb.2xlarge`      | 8                                | 8                                | 32                              |
| `m8gb.4xlarge`      | 8                                | 16                               | 64                              |
| `m8gb.8xlarge`      | 8                                | 32                               | 128                             |
| `m8gb.12xlarge`     | 16                               | 64                               | 192                             |
| `m8gb.16xlarge`     | 16                               | 64                               | 256                             |
| `m8gb.24xlarge`     | 16                               | 128                              | 384                             |
| `m8gb.48xlarge`     | 32                               | 128                              | 768 \*                          |
| `m8gb.metal-24xl`   | 32                               | 128                              | 768                             |
| `m8gb.metal-48xl`   | 32                               | 128                              | 768 \*                          |
| **M8gn**            |
| `m8gn.medium`       | 1                                | 1                                | 2                               |
| `m8gn.large`        | 2                                | 2                                | 6                               |
| `m8gn.xlarge`       | 4                                | 4                                | 16                              |
| `m8gn.2xlarge`      | 8                                | 8                                | 32                              |
| `m8gn.4xlarge`      | 8                                | 16                               | 64                              |
| `m8gn.8xlarge`      | 8                                | 32                               | 128                             |
| `m8gn.12xlarge`     | 16                               | 64                               | 192                             |
| `m8gn.16xlarge`     | 16                               | 64                               | 256                             |
| `m8gn.24xlarge`     | 16                               | 128                              | 384                             |
| `m8gn.48xlarge`     | 32                               | 128                              | 768 \*                          |
| `m8gn.metal-24xl`   | 32                               | 128                              | 768                             |
| `m8gn.metal-48xl`   | 32                               | 128                              | 768 \*                          |
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
| **M8id**            |
| `m8id.large`        | 2                                | 2                                | 6                               |
| `m8id.xlarge`       | 4                                | 4                                | 16                              |
| `m8id.2xlarge`      | 8                                | 8                                | 32                              |
| `m8id.4xlarge`      | 8                                | 16                               | 64                              |
| `m8id.8xlarge`      | 8                                | 32                               | 128                             |
| `m8id.12xlarge`     | 16                               | 64                               | 192                             |
| `m8id.16xlarge`     | 16                               | 64                               | 256                             |
| `m8id.24xlarge`     | 16                               | 128                              | 384                             |
| `m8id.32xlarge`     | 16                               | 128                              | 512                             |
| `m8id.48xlarge`     | 32                               | 128                              | 768                             |
| `m8id.96xlarge`     | 32                               | 128                              | 1536                            |
| `m8id.metal-48xl`   | 32                               | 128                              | 768                             |
| `m8id.metal-96xl`   | 32                               | 128                              | 1536                            |
| **M8i-flex**        |
| `m8i-flex.large`    | 1                                | 1                                | 3                               |
| `m8i-flex.xlarge`   | 2                                | 2                                | 8                               |
| `m8i-flex.2xlarge`  | 4                                | 4                                | 16                              |
| `m8i-flex.4xlarge`  | 4                                | 8                                | 32                              |
| `m8i-flex.8xlarge`  | 4                                | 16                               | 64                              |
| `m8i-flex.12xlarge` | 8                                | 32                               | 96                              |
| `m8i-flex.16xlarge` | 8                                | 32                               | 128                             |
| **M8in**            |
| `m8in.large`        | 2                                | 2                                | 8                               |
| `m8in.xlarge`       | 4                                | 4                                | 16                              |
| `m8in.2xlarge`      | 8                                | 8                                | 32                              |
| `m8in.4xlarge`      | 8                                | 16                               | 64                              |
| `m8in.8xlarge`      | 16                               | 32                               | 128                             |
| `m8in.12xlarge`     | 16                               | 64                               | 192                             |
| `m8in.16xlarge`     | 16                               | 64                               | 256                             |
| `m8in.24xlarge`     | 16                               | 128                              | 256                             |
| `m8in.32xlarge`     | 32                               | 128                              | 512                             |
| `m8in.48xlarge`     | 32                               | 128                              | 768                             |
| `m8in.96xlarge`     | 32                               | 128                              | 1536 \*                         |
| **M8idn**           |
| `m8idn.large`       | 2                                | 2                                | 8                               |
| `m8idn.xlarge`      | 4                                | 4                                | 16                              |
| `m8idn.2xlarge`     | 8                                | 8                                | 32                              |
| `m8idn.4xlarge`     | 8                                | 16                               | 64                              |
| `m8idn.8xlarge`     | 16                               | 32                               | 128                             |
| `m8idn.12xlarge`    | 16                               | 64                               | 192                             |
| `m8idn.16xlarge`    | 16                               | 64                               | 256                             |
| `m8idn.24xlarge`    | 16                               | 128                              | 256                             |
| `m8idn.32xlarge`    | 32                               | 128                              | 512                             |
| `m8idn.48xlarge`    | 32                               | 128                              | 768                             |
| `m8idn.96xlarge`    | 32                               | 128                              | 1536 \*                         |
| **M8ine**           |
| `m8ine.large`       | 2                                | 2                                | 8                               |
| `m8ine.xlarge`      | 4                                | 4                                | 16                              |
| `m8ine.2xlarge`     | 8                                | 8                                | 32                              |
| `m8ine.4xlarge`     | 16                               | 16                               | 128                             |
| `m8ine.8xlarge`     | 32                               | 32                               | 256                             |
| `m8ine.12xlarge`    | 32                               | 64                               | 384                             |
| **M8ib**            |
| `m8ib.large`        | 2                                | 2                                | 8                               |
| `m8ib.xlarge`       | 4                                | 4                                | 16                              |
| `m8ib.2xlarge`      | 8                                | 8                                | 32                              |
| `m8ib.4xlarge`      | 8                                | 16                               | 64                              |
| `m8ib.8xlarge`      | 16                               | 32                               | 128                             |
| `m8ib.12xlarge`     | 16                               | 64                               | 192                             |
| `m8ib.16xlarge`     | 16                               | 64                               | 256                             |
| `m8ib.24xlarge`     | 16                               | 128                              | 256                             |
| `m8ib.32xlarge`     | 32                               | 128                              | 512                             |
| `m8ib.48xlarge`     | 32                               | 128                              | 768                             |
| `m8ib.96xlarge`     | 32                               | 128                              | 1536 \*                         |
| **M8idb**           |
| `m8idb.large`       | 2                                | 2                                | 8                               |
| `m8idb.xlarge`      | 4                                | 4                                | 16                              |
| `m8idb.2xlarge`     | 8                                | 8                                | 32                              |
| `m8idb.4xlarge`     | 8                                | 16                               | 64                              |
| `m8idb.8xlarge`     | 16                               | 32                               | 128                             |
| `m8idb.12xlarge`    | 16                               | 64                               | 192                             |
| `m8idb.16xlarge`    | 16                               | 64                               | 256                             |
| `m8idb.24xlarge`    | 16                               | 128                              | 256                             |
| `m8idb.32xlarge`    | 32                               | 128                              | 512                             |
| `m8idb.48xlarge`    | 32                               | 128                              | 768                             |
| `m8idb.96xlarge`    | 32                               | 128                              | 1536 \*                         |

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
| `c8gb.48xlarge`     | 32                               | 128                              | 768 \*                          |
| `c8gb.metal-24xl`   | 32                               | 128                              | 768                             |
| `c8gb.metal-48xl`   | 32                               | 128                              | 768 \*                          |
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
| **C8id**            |
| `c8id.large`        | 2                                | 2                                | 6                               |
| `c8id.xlarge`       | 4                                | 4                                | 16                              |
| `c8id.2xlarge`      | 8                                | 8                                | 32                              |
| `c8id.4xlarge`      | 8                                | 16                               | 64                              |
| `c8id.8xlarge`      | 8                                | 32                               | 128                             |
| `c8id.12xlarge`     | 16                               | 64                               | 192                             |
| `c8id.16xlarge`     | 16                               | 64                               | 256                             |
| `c8id.24xlarge`     | 16                               | 128                              | 384                             |
| `c8id.32xlarge`     | 16                               | 128                              | 512                             |
| `c8id.48xlarge`     | 32                               | 128                              | 768                             |
| `c8id.96xlarge`     | 32                               | 128                              | 1536                            |
| `c8id.metal-48xl`   | 32                               | 128                              | 768                             |
| `c8id.metal-96xl`   | 32                               | 128                              | 1536                            |
| **C8i-flex**        |
| `c8i-flex.large`    | 1                                | 1                                | 3                               |
| `c8i-flex.xlarge`   | 2                                | 2                                | 8                               |
| `c8i-flex.2xlarge`  | 4                                | 4                                | 16                              |
| `c8i-flex.4xlarge`  | 4                                | 8                                | 32                              |
| `c8i-flex.8xlarge`  | 4                                | 16                               | 64                              |
| `c8i-flex.12xlarge` | 8                                | 32                               | 96                              |
| `c8i-flex.16xlarge` | 8                                | 32                               | 128                             |
| **C8in**            |
| `c8in.large`        | 2                                | 2                                | 8                               |
| `c8in.xlarge`       | 4                                | 4                                | 16                              |
| `c8in.2xlarge`      | 8                                | 8                                | 32                              |
| `c8in.4xlarge`      | 8                                | 16                               | 64                              |
| `c8in.8xlarge`      | 16                               | 32                               | 128                             |
| `c8in.12xlarge`     | 16                               | 64                               | 192                             |
| `c8in.16xlarge`     | 16                               | 64                               | 256                             |
| `c8in.24xlarge`     | 16                               | 128                              | 256                             |
| `c8in.32xlarge`     | 32                               | 128                              | 512                             |
| `c8in.48xlarge`     | 32                               | 128                              | 768                             |
| `c8in.96xlarge`     | 32                               | 128                              | 1536 \*                         |
| `c8in.metal-48xl`   | 32                               | 128                              | 768                             |
| `c8in.metal-96xl`   | 32                               | 128                              | 1536 \*                         |
| **C8ine**           |
| `c8ine.large`       | 2                                | 2                                | 8                               |
| `c8ine.xlarge`      | 4                                | 4                                | 16                              |
| `c8ine.2xlarge`     | 8                                | 8                                | 32                              |
| `c8ine.4xlarge`     | 16                               | 16                               | 128                             |
| `c8ine.8xlarge`     | 32                               | 32                               | 256                             |
| `c8ine.12xlarge`    | 32                               | 64                               | 384                             |
| **C8ib**            |
| `c8ib.large`        | 2                                | 2                                | 8                               |
| `c8ib.xlarge`       | 4                                | 4                                | 16                              |
| `c8ib.2xlarge`      | 8                                | 8                                | 32                              |
| `c8ib.4xlarge`      | 8                                | 16                               | 64                              |
| `c8ib.8xlarge`      | 16                               | 32                               | 128                             |
| `c8ib.12xlarge`     | 16                               | 64                               | 192                             |
| `c8ib.16xlarge`     | 16                               | 64                               | 256                             |
| `c8ib.24xlarge`     | 16                               | 128                              | 256                             |
| `c8ib.32xlarge`     | 32                               | 128                              | 512                             |
| `c8ib.48xlarge`     | 32                               | 128                              | 768                             |
| `c8ib.96xlarge`     | 32                               | 128                              | 1536 \*                         |
| `c8ib.metal-48xl`   | 32                               | 128                              | 768                             |
| `c8ib.metal-96xl`   | 32                               | 128                              | 1536 \*                         |

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
| `r8gb.48xlarge`     | 32                               | 128                              | 768 \*                          |
| `r8gb.metal-24xl`   | 32                               | 128                              | 768                             |
| `r8gb.metal-48xl`   | 32                               | 128                              | 768 \*                          |
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
| **R8id**            |
| `r8id.large`        | 2                                | 2                                | 6                               |
| `r8id.xlarge`       | 4                                | 4                                | 16                              |
| `r8id.2xlarge`      | 8                                | 8                                | 32                              |
| `r8id.4xlarge`      | 8                                | 16                               | 64                              |
| `r8id.8xlarge`      | 8                                | 32                               | 128                             |
| `r8id.12xlarge`     | 16                               | 64                               | 192                             |
| `r8id.16xlarge`     | 16                               | 64                               | 256                             |
| `r8id.24xlarge`     | 16                               | 128                              | 384                             |
| `r8id.32xlarge`     | 16                               | 128                              | 512                             |
| `r8id.48xlarge`     | 32                               | 128                              | 768                             |
| `r8id.96xlarge`     | 32                               | 128                              | 1536                            |
| `r8id.metal-48xl`   | 32                               | 128                              | 768                             |
| `r8id.metal-96xl`   | 32                               | 128                              | 1536                            |
| **R8i-flex**        |
| `r8i-flex.large`    | 1                                | 1                                | 3                               |
| `r8i-flex.xlarge`   | 2                                | 2                                | 8                               |
| `r8i-flex.2xlarge`  | 4                                | 4                                | 16                              |
| `r8i-flex.4xlarge`  | 4                                | 8                                | 32                              |
| `r8i-flex.8xlarge`  | 4                                | 16                               | 64                              |
| `r8i-flex.12xlarge` | 8                                | 32                               | 96                              |
| `r8i-flex.16xlarge` | 8                                | 32                               | 128                             |
| **R8in**            |
| `r8in.large`        | 2                                | 2                                | 8                               |
| `r8in.xlarge`       | 4                                | 4                                | 16                              |
| `r8in.2xlarge`      | 8                                | 8                                | 32                              |
| `r8in.4xlarge`      | 8                                | 16                               | 64                              |
| `r8in.8xlarge`      | 16                               | 32                               | 128                             |
| `r8in.12xlarge`     | 16                               | 64                               | 192                             |
| `r8in.16xlarge`     | 16                               | 64                               | 256                             |
| `r8in.24xlarge`     | 16                               | 128                              | 256                             |
| `r8in.32xlarge`     | 32                               | 128                              | 512                             |
| `r8in.48xlarge`     | 32                               | 128                              | 768                             |
| `r8in.96xlarge`     | 32                               | 128                              | 1536 \*                         |
| **R8idn**           |
| `r8idn.large`       | 2                                | 2                                | 8                               |
| `r8idn.xlarge`      | 4                                | 4                                | 16                              |
| `r8idn.2xlarge`     | 8                                | 8                                | 32                              |
| `r8idn.4xlarge`     | 8                                | 16                               | 64                              |
| `r8idn.8xlarge`     | 16                               | 32                               | 128                             |
| `r8idn.12xlarge`    | 16                               | 64                               | 192                             |
| `r8idn.16xlarge`    | 16                               | 64                               | 256                             |
| `r8idn.24xlarge`    | 16                               | 128                              | 256                             |
| `r8idn.32xlarge`    | 32                               | 128                              | 512                             |
| `r8idn.48xlarge`    | 32                               | 128                              | 768                             |
| `r8idn.96xlarge`    | 32                               | 128                              | 1536 \*                         |
| **R8ib**            |
| `r8ib.large`        | 2                                | 2                                | 8                               |
| `r8ib.xlarge`       | 4                                | 4                                | 16                              |
| `r8ib.2xlarge`      | 8                                | 8                                | 32                              |
| `r8ib.4xlarge`      | 8                                | 16                               | 64                              |
| `r8ib.8xlarge`      | 16                               | 32                               | 128                             |
| `r8ib.12xlarge`     | 16                               | 64                               | 192                             |
| `r8ib.16xlarge`     | 16                               | 64                               | 256                             |
| `r8ib.24xlarge`     | 16                               | 128                              | 256                             |
| `r8ib.32xlarge`     | 32                               | 128                              | 512                             |
| `r8ib.48xlarge`     | 32                               | 128                              | 768                             |
| `r8ib.96xlarge`     | 32                               | 128                              | 1536 \*                         |
| **R8idb**           |
| `r8idb.large`       | 2                                | 2                                | 8                               |
| `r8idb.xlarge`      | 4                                | 4                                | 16                              |
| `r8idb.2xlarge`     | 8                                | 8                                | 32                              |
| `r8idb.4xlarge`     | 8                                | 16                               | 64                              |
| `r8idb.8xlarge`     | 16                               | 32                               | 128                             |
| `r8idb.12xlarge`    | 16                               | 64                               | 192                             |
| `r8idb.16xlarge`    | 16                               | 64                               | 256                             |
| `r8idb.24xlarge`    | 16                               | 128                              | 256                             |
| `r8idb.32xlarge`    | 32                               | 128                              | 512                             |
| `r8idb.48xlarge`    | 32                               | 128                              | 768                             |
| `r8idb.96xlarge`    | 32                               | 128                              | 1536 \*                         |
| **X8aedz**          |
| `x8aedz.large`      | 2                                | 2                                | 8                               |
| `x8aedz.xlarge`     | 4                                | 4                                | 16                              |
| `x8aedz.3xlarge`    | 4                                | 16                               | 48                              |
| `x8aedz.6xlarge`    | 8                                | 32                               | 96                              |
| `x8aedz.12xlarge`   | 8                                | 64                               | 192                             |
| `x8aedz.24xlarge`   | 16                               | 128                              | 384                             |
| `x8aedz.metal-12xl` | 8                                | 64                               | 192                             |
| `x8aedz.metal-24xl` | 16                               | 128                              | 384                             |
| **X8i**             |
| `x8i.large`         | 2                                | 2                                | 6                               |
| `x8i.xlarge`        | 4                                | 4                                | 16                              |
| `x8i.2xlarge`       | 8                                | 8                                | 32                              |
| `x8i.4xlarge`       | 8                                | 16                               | 64                              |
| `x8i.8xlarge`       | 8                                | 32                               | 128                             |
| `x8i.12xlarge`      | 16                               | 64                               | 192                             |
| `x8i.16xlarge`      | 16                               | 64                               | 256                             |
| `x8i.24xlarge`      | 16                               | 128                              | 384                             |
| `x8i.32xlarge`      | 16                               | 128                              | 512                             |
| `x8i.48xlarge`      | 32                               | 128                              | 768                             |
| `x8i.64xlarge`      | 32                               | 128                              | 1024                            |
| `x8i.96xlarge`      | 32                               | 128                              | 1536                            |
| `x8i.metal-48xl`    | 32                               | 128                              | 768                             |
| `x8i.metal-96xl`    | 32                               | 128                              | 1536                            |

###### Note

\* These instance types feature multiple network cards. Other instance types feature a
single network card. For more information, see [Network cards](using-eni.md#network-cards "using-eni.md#network-cards").

## Modify the number of queues

You can modify the number of ENA queues using the AWS Management Console, AWS CLI, or PowerShell. In the
AWS Management Console, the ENA queues configuration is available under each **Network
interface** setting.

###### Note

- Your instance must be stopped before modifying the number of ENA
  queues.
- The value for ENA queues must be a power of 2, such as, 1, 2, 4,
  8, 16, 32, etc.
- The number of queues allocated to any single ENI cannot exceed the
  number of vCPUs available on your instance.

Before modifying the queue count, use the following command
to check your current queue count.

AWS CLI

```
aws ec2 describe-instances --instance-id `i-1234567890abcdef0`
```

PowerShell

```
(Get-EC2Instance -InstanceId i-`1234567890abcdef0`).Instances.NetworkInterfaces |
  Select-Object NetworkInterfaceId,
    @{N='DeviceIndex';E={$_.Attachment.DeviceIndex}},
    @{N='AttachmentId';E={$_.Attachment.AttachmentId}},
    @{N='EnaQueueCount';E={$_.Attachment.EnaQueueCount}}
```

### Attach a network interface with ENA queues

In the following example, 16 ENA queues are configured on an ENI.

AWS CLI

###### To attach a network interface with ENA queues

Use the [attach-network-interface](../../../cli/latest/reference/ec2/attach-network-interface.md "../../../cli/latest/reference/ec2/attach-network-interface.md") command.

```
aws ec2 attach-network-interface \
  --network-interface-id eni-`abcdef01234567890` \
  --instance-id `i-1234567890abcdef0` \
  --device-index 1 \
  --ena-queue-count 16
```

PowerShell

###### To attach a network interface with ENA queues

Use the [Add-EC2NetworkInterface](../../../powershell/latest/reference/items/Add-EC2NetworkInterface.md "../../../powershell/latest/reference/items/Add-EC2NetworkInterface.md") cmdlet.

```
Add-EC2NetworkInterface `
  -NetworkInterfaceId eni-`abcdef01234567890` `
  -InstanceId `i-1234567890abcdef0` `
  -DeviceIndex 1 `
  -EnaQueueCount 16
```

### Launch an instance with ENA queues

In the following example, 16 ENA queues each are configured on 3 ENIs.

AWS CLI

###### To launch an instance with ENA queues

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command.

```
aws ec2 run-instances \
  --image-id ami-`1234567890abcdef0` \
  --instance-type c8i.4xlarge \
  --network-interfaces \
    "[{\"DeviceIndex\":0,\"SubnetId\":\"subnet-`abcdef01234567890`\",\"EnaQueueCount\":16},
      {\"DeviceIndex\":1,\"SubnetId\":\"subnet-`abcdef01234567890`\",\"EnaQueueCount\":16},
      {\"DeviceIndex\":2,\"SubnetId\":\"subnet-`abcdef01234567890`\",\"EnaQueueCount\":16}]"
```

PowerShell

###### To launch an instance with ENA queues

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") cmdlet.

```
New-EC2Instance `
  -ImageId ami-`1234567890abcdef0` `
  -InstanceType c8i.4xlarge `
  -NetworkInterface @(
    @{DeviceIndex=0; SubnetId="subnet-`abcdef01234567890`"; EnaQueueCount=16},
    @{DeviceIndex=1; SubnetId="subnet-`abcdef01234567890`"; EnaQueueCount=16},
    @{DeviceIndex=2; SubnetId="subnet-`abcdef01234567890`"; EnaQueueCount=16}
  )
```

### Modify ENA queues on an existing network interface

In the following example, 16 ENA queues are configured on an ENI.

AWS CLI

###### To modify ENA queues on a network interface

Use the [modify-network-interface-attribute](../../../cli/latest/reference/ec2/modify-network-interface-attribute.md "../../../cli/latest/reference/ec2/modify-network-interface-attribute.md") command.

```
aws ec2 modify-network-interface-attribute \
  --network-interface-id eni-`1234567890abcdef0` \
  --attachment AttachmentId=eni-attach-`1234567890abcdef0`,EnaQueueCount=16
```

PowerShell

###### To modify ENA queues on a network interface

Use the [Edit-EC2NetworkInterfaceAttribute](../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md") cmdlet.

```
Edit-EC2NetworkInterfaceAttribute `
  -NetworkInterfaceId eni-`1234567890abcdef0` `
  -Attachment_AttachmentId eni-attach-`1234567890abcdef0` `
  -Attachment_EnaQueueCount 16
```

In the following example, the ENA count is reset to the default value.

AWS CLI

```
aws ec2 modify-network-interface-attribute \
  --network-interface-id eni-`1234567890abcdef0` \
  --attachment AttachmentId=eni-attach-`1234567890abcdef0`,DefaultEnaQueueCount=true
```

PowerShell

```
Edit-EC2NetworkInterfaceAttribute `
  -NetworkInterfaceId eni-`1234567890abcdef0` `
  -Attachment_AttachmentId eni-attach-`1234567890abcdef0` `
  -Attachment_DefaultEnaQueueCount $true
```
