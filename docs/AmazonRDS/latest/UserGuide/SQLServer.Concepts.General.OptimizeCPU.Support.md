

# DB instance classes that support Optimize CPU
<a name="SQLServer.Concepts.General.OptimizeCPU.Support"></a>

RDS for SQL Server supports Optimize CPU beginning with the 7th Generation instance class type. Additionally, RDS provides a detailed billing breakdown of RDS DB instance and third-party licensing fees, starting from the 7th Generation instance class type, regardless of whether the Optimize CPU feature is enabled.

RDS for SQL Server provides support for Optimize CPU on specific instance sizes, with the smallest instance size supported being `2xlarge`. The minimum configuration supported is 4 vCPUs. The table below outlines the DB instance classes that support the Optimize CPU, including their default and valid values for CPU cores, CPU threads per core and vCPUs: 

**Intel instances**


**General purpose instances**  

| Instance type | Default vCPUs | Default CPU cores | Valid CPU cores | Valid threads per core | 
| --- | --- | --- | --- | --- | 
| `m7i.large, m8i.large` | 2 | 1 | 1 | 2 | 
| `m7i.xlarge, m8i.xlarge` | 4 | 2 | 1,2 | 2 | 
| `m7i.2xlarge, m8i.2xlarge` | 4 | 4 | 1,2,3,4 | 1 | 
| `m7i.4xlarge, m8i.4xlarge` | 8 | 8 | 1,2,3,4,5,6,7,8 | 1 | 
| `m7i.8xlarge, m8i.8xlarge` | 16 | 16 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 | 1 | 
| `m7i.12xlarge, m8i.12xlarge` | 24 | 24 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24 | 1 | 
| `m7i.16xlarge, m8i.16xlarge` | 32 | 32 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32 | 1 | 
| `m7i.24xlarge` | 48 | 48 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48 | 1 | 
| `m8i.24xlarge` | 48 | 48 | 4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48 | 1 | 
| `m8i.32xlarge` | 64 | 64 | 4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64 | 1 | 
| `m7i.48xlarge` | 96 | 96 | 4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96 | 1 | 
| `m8i.48xlarge` | 96 | 96 | 6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96 | 1 | 
| `m8i.96xlarge` | 192 | 192 | 12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120,126,132,138,144,150,156,162,168,174,180,186,192 | 1 | 


**Memory optimized instances**  

| Instance type | Default vCPUs | Default CPU cores | Valid CPU cores | Valid threads per core | 
| --- | --- | --- | --- | --- | 
| `r7i.large, r8i.large` | 2 | 1 | 1 | 2 | 
| `r7i.xlarge, r8i.xlarge` | 4 | 2 | 1,2 | 2 | 
| `r7i.2xlarge, r8i.2xlarge` | 4 | 4 | 1,2,3,4 | 1 | 
| `r7i.4xlarge, r8i.4xlarge` | 8 | 8 | 1,2,3,4,5,6,7,8 | 1 | 
| `r7i.8xlarge, r8i.8xlarge` | 16 | 16 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 | 1 | 
| `r7i.12xlarge, r8i.12xlarge` | 24 | 24 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24 | 1 | 
| `r7i.16xlarge, r8i.16xlarge` | 32 | 32 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32 | 1 | 
| `r7i.24xlarge` | 48 | 48 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48 | 1 | 
| `r8i.24xlarge` | 48 | 48 | 4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48 | 1 | 
| `r8i.32xlarge` | 64 | 64 | 4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64 | 1 | 
| `r7i.48xlarge` | 96 | 96 | 4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96 | 1 | 
| `r8i.48xlarge` | 96 | 96 | 6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96 | 1 | 
| `r8i.96xlarge` | 192 | 192 | 12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120,126,132,138,144,150,156,162,168,174,180,186,192 | 1 | 

**X2M instances**

Amazon RDS for SQL Server launched memory-optimized X2M database instances based on the Amazon EC2 X2iedn instance. Hyper-threading is disabled on RDS SQL Server for instance sizes 2xlarge and above for X2m database instances. This results in the total number of vCPUs available being half of that supported by the corresponding EC2 instance. For example, the EC2 instance type `x2m.2xlarge` (`x2iedn.2xlarge`) by default supports 4 cores and 2 threadsPerCore, resulting in a total of 8 vCPUs. In contrast, the RDS for SQL Server `x2m.2xlarge` (`x2iedn.2xlarge`) instance, with hyper-threading disabled, results in 4 cores and 1 threadsPerCore, overall 4 vCPUs.

With unbundled pricing, database costs are calculated with separate charges for instance price (price per CPU hour) and licensing (price per vCPU hour). For more details about pricing, please refer to [Amazon RDS for SQL Server Pricing](https://aws.amazon.com/rds/sqlserver/pricing/). The table below outlines X2M instance classes that support the Optimize CPU, including their default and valid values for CPU cores, CPU threads per core and vCPUs.


**Memory optimized instances**  

| Instance type | Default vCPUs | Default CPU cores | Valid CPU cores | Valid threads per core | 
| --- | --- | --- | --- | --- | 
| `x2m.xlarge` | 4 | 2 | 1,2 | 2 | 
| `x2m.2xlarge` | 4 | 4 | 1,2,3,4 | 1 | 
| `x2m.4xlarge` | 8 | 8 | 1,2,3,4,5,6,7,8 | 1 | 
| `x2m.8xlarge` | 16 | 16 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 | 1 | 
| `x2m.16xlarge` | 32 | 32 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32 | 1 | 
| `x2m.24xlarge` | 48 | 48 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48 | 1 | 
| `x2m.32xlarge` | 64 | 64 | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64 | 1 | 

**AMD instances**

Unlike equivalent Intel instances, each vCPU in AMD instances corresponds to a physical CPU core, designed to deliver consistent per-core performance.

For AMD instances that are 2xlarge and larger, Amazon RDS disables 50% of the CPU cores by default. This configuration helps reduce Windows and SQL Server software licensing costs while maintaining workload performance. To enable additional CPU capacity, you can use the Optimize CPU feature to enable up to 100% of the available cores. Because the instance price remains the same regardless of the core configuration, you can customize the vCPU count to balance performance requirements against licensing costs without impacting your compute charges.

For AMD instances that are xlarge and smaller, those with 4 vCPU or fewer, 100% of the cores are enabled by default and core count customization is not available. This is because Microsoft charges for a minimum of 4 vCPUs for the SQL Server licenses, so you are unable to reduce the number of vCPUs for these instances.

With unbundled pricing, database costs are calculated with separate charges for instance price (price per CPU hour) and licensing (price per vCPU hour). For more details about pricing, please refer to [Amazon RDS for SQL Server Pricing](https://aws.amazon.com/rds/sqlserver/pricing/). The table below outlines AMD instance classes that support the Optimize CPU, including their default and valid values for CPU cores, CPU threads per core and vCPUs.


**General purpose instances**  

| Instance type | Default vCPUs | Default CPU cores | Valid CPU cores | Valid threads per core | 
| --- | --- | --- | --- | --- | 
| `m8a.large` | 2 | 2 | 1,2 | 1 | 
| `m8a.xlarge` | 4 | 4 | 1,2,3,4 | 1 | 
| `m8a.2xlarge` | 4 | 4 | 1,2,3,4,5,6,7,8 | 1 | 
| `m8a.4xlarge` | 8 | 8 | 1,2,4,6,8,10,12,14,16 | 1 | 
| `m8a.8xlarge` | 16 | 16 | 1,2,3,4,8,12,16,20,24,28,32 | 1 | 
| `m8a.12xlarge` | 24 | 24 | 1,2,3,4,5,6,12,18,24,30,36,42,48 | 1 | 
| `m8a.16xlarge` | 32 | 32 | 1,2,3,4,5,6,7,8,16,24,32,40,48,56,64 | 1 | 


**Memory optimized instances**  

| Instance type | Default vCPUs | Default CPU cores | Valid CPU cores | Valid threads per core | 
| --- | --- | --- | --- | --- | 
| `r8a.large` | 2 | 2 | 1,2 | 1 | 
| `r8a.xlarge` | 4 | 4 | 1,2,3,4 | 1 | 
| `r8a.2xlarge` | 4 | 4 | 1,2,3,4,5,6,7,8 | 1 | 
| `r8a.4xlarge` | 8 | 8 | 1,2,4,6,8,10,12,14,16 | 1 | 
| `r8a.8xlarge` | 16 | 16 | 1,2,3,4,8,12,16,20,24,28,32 | 1 | 
| `r8a.12xlarge` | 24 | 24 | 1,2,3,4,5,6,12,18,24,30,36,42,48 | 1 | 
| `r8a.16xlarge` | 32 | 32 | 1,2,3,4,5,6,7,8,16,24,32,40,48,56,64 | 1 | 