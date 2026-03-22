# DB instance classes that support Optimize CPU

RDS for SQL Server supports Optimize CPU beginning with the 7th Generation instance class type.
Additionally, RDS provides a detailed billing breakdown of RDS DB instance and third-party licensing fees,
starting from the 7th Generation instance class type, regardless of whether the Optimize CPU feature is enabled.

RDS for SQL Server provides support for Optimize CPU on specific instance sizes,
with the smallest instance size supported being `2xlarge`. The minimum configuration supported is 4 vCPUs.
The table below outlines the DB instance classes that support the Optimize CPU,
including their default and valid values for CPU cores, CPU threads per core and vCPUs:

| General purpose instances | Instance type | Default vCPUs | Default CPU cores                                                                      | Valid CPU cores | Valid threads per core |
| ------------------------- | ------------- | ------------- | -------------------------------------------------------------------------------------- | --------------- | ---------------------- |
| `m7i.large`               | 2             | 1             | 1                                                                                      | 2               |
| `m7i.xlarge`              | 4             | 2             | 2                                                                                      | 2               |
| `m7i.2xlarge`             | 4             | 4             | 1,2,3,4                                                                                | 1               |
| `m7i.4xlarge`             | 8             | 8             | 1,2,3,4,5,6,7,8                                                                        | 1               |
| `m7i.8xlarge`             | 16            | 16            | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16                                                 | 1               |
| `m7i.12xlarge`            | 24            | 24            | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24                         | 1               |
| `m7i.16xlarge`            | 32            | 32            | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32 | 1               |

| Memory optimized instances | Instance type | Default vCPUs | Default CPU cores                                                                      | Valid CPU cores | Valid threads per core |
| -------------------------- | ------------- | ------------- | -------------------------------------------------------------------------------------- | --------------- | ---------------------- |
| `r7i.large`                | 2             | 1             | 1                                                                                      | 2               |
| `r7i.xlarge`               | 4             | 2             | 2                                                                                      | 2               |
| `r7i.2xlarge`              | 4             | 4             | 1,2,3,4                                                                                | 1               |
| `r7i.4xlarge`              | 8             | 8             | 1,2,3,4,5,6,7,8                                                                        | 1               |
| `r7i.8xlarge`              | 16            | 16            | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16                                                 | 1               |
| `r7i.12xlarge`             | 24            | 24            | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24                         | 1               |
| `r7i.16xlarge`             | 32            | 32            | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32 | 1               |
