

# Optimize CPUs for RDS for SQL Server instances
<a name="SQLServer.Concepts.General.OptimizeCPU"></a>

With RDS for SQL Server, you can use Optimize CPU by specifying processor features to configure the vCPU count on your DB instance while maintaining the same memory and IOPS. You can achieve desired memory-to-CPU ratios for specific database workload requirements and reduce licensing costs for Microsoft Windows OS and SQL Server, which are based on vCPU count.

To specify processor feature, use the following parameters:

```
--processor-features "Name=coreCount,Value={{value}}" \ 
	"Name=threadsPerCore,Value={{value}}"
```
+ **coreCount** – Specify the number of CPU cores for the DB instance, to optimize licensing costs for DB instances. See [DB instance classes that support Optimize CPU](SQLServer.Concepts.General.OptimizeCPU.Support.md) to find the allowed values for core count for a selected instance type.
+ **threadsPerCore** – Specify the threads per core to define the number of threads per CPU core. See [DB instance classes that support Optimize CPU](SQLServer.Concepts.General.OptimizeCPU.Support.md) to find the allowed values for threads per core for a selected instance type.

Sample command to create an RDS for SQL Server instance with Optimize CPU settings:

```
aws rds create-db-instance \
    --engine sqlserver-ee \
    --engine-version 16.00 \
    --license-model license-included \
    --allocated-storage {{300}} \
    --master-username {{myuser}} \
    --master-user-password {{xxxxx}} \
    --no-multi-az \
    --vpc-security-group-ids myvpcsecuritygroup \
    --db-subnet-group-name mydbsubnetgroup \
    --db-instance-identifier my-rds-instance \
    --db-instance-class db.m7i.8xlarge \
    --processor-features "Name=coreCount,Value=8" "Name=threadsPerCore,Value=1"
```

In this example, you create a `db.m7i.8xlarge` instance, which by default has a coreCount of 16. By using Optimize CPU, you opt for a coreCount of 8, resulting in an effective vCPU count of 8.

If you create the instance without the `--processor-features` parameter, core count is set to 16 and threads per core is set to 1 by default, resulting in a default vCPU count of 16.

Some considerations to keep in mind while specifying processor features:
+ **Create** – Specify both the `coreCount` and `threadsPerCore` for the `processor-features` parameter from the allowed values. See [DB instance classes that support Optimize CPU](SQLServer.Concepts.General.OptimizeCPU.Support.md).
+ **Modify** – When modifying from one instance class configured with Optimize CPU settings to another one that supports Optimize CPU settings, you must specify the default processor settings using the `--use-default-processor-features` parameter or explicitly define the options during the modify request.
**Note**  
Changing the vCPU count can have implications for the licensing fee cost associated with the DB instance.
+ **Snapshot restore** – When restoring a snapshot to the same instance type as source, the restored DB instance inherits the Optimize CPU settings from the snapshot. If restoring to a different instance type, you need to define the Optimize CPU settings for the target instance or specify the `--use-default-processor-features` parameter.
+ **Point-in-time restore** – Point-in-time restore (PITR) involves restoring a specific snapshot based on the designated time for PITR and subsequently applying all transactional log backups to that snapshot, thereby bringing the instance to the specified point in time. For PITR, the Optimize CPU settings, `coreCount` and `threadsPerCore`, are derived from the source snapshot (not the point in time) unless custom values are specified during the PITR request. If the source snapshot being used is enabled with Optimize CPU settings and you are using a different instance type for PITR, you must define the Optimize CPU settings for the target instance or specify the `—-use-default-processor-features` parameter.

## Limitations
<a name="SQLServer.Concepts.General.OptimizeCPU.Limitations"></a>

The following limitations apply when using Optimize CPU:
+ Optimize CPU supports the following editions: Enterprise, Standard, and Web (License Included), and Enterprise, Standard, and Developer (Bring Your Own Media). Supported instance families include m7i, r7i, m8i, r8i, m8a, r8a, and x2m.
+ Optimize CPU offers different valid core settings depending on the instance class. For more details, see [DB instance classes that support Optimize CPU](SQLServer.Concepts.General.OptimizeCPU.Support.md).
+ Customizing the number of CPU cores is supported on instance sizes of `2xlarge` and above. With these instance types, the minimum number of vCPCU supported for Optimize CPU is 4.
+ Optimize CPU allows only 1 thread per core since Hyper-Threading is disabled for instances starting from 7th generation that support Optimize CPU.