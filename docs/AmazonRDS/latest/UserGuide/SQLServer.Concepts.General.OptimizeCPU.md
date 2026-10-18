

# Optimize CPUs for RDS for SQL Server instances
<a name="SQLServer.Concepts.General.OptimizeCPU"></a>

With RDS for SQL Server, you can use Optimize CPU to configure the vCPU count on your DB instance. This keeps the same memory, network, and storage performance. Windows Server and SQL Server licensing costs are based on vCPU count. Reducing the vCPU count reduces those costs. You can also achieve the memory-to-CPU ratio that your workload requires.

To specify processor features, use the [ProcessorFeature](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ProcessorFeature.html) parameters `coreCount` and `threadsPerCore`.
+ **coreCount** – Specify the number of CPU cores for the DB instance, to optimize licensing costs for DB instances.
+ **threadsPerCore** – Specify the threads per core to define the number of threads per CPU core.

For the allowed values for each instance class, see [DB instance classes that support Optimize CPU](SQLServer.Concepts.General.OptimizeCPU.Support.md).

For example, the `db.r8i.8xlarge` instance class has 16 vCPUs by default. With Optimize CPU, you can set `coreCount` to 12, which results in 12 vCPUs. This reduces licensing costs if you don't need the additional processing power.

For the AWS Management Console, AWS CLI, and AWS Tools for PowerShell procedures, see [Setting the CPU cores and threads per CPU core for a DB instance class](SQLServer.Concepts.General.OptimizeCPU.Enabling.md).

Some considerations to keep in mind while specifying processor features:
+ **Create** – Specify both the `coreCount` and `threadsPerCore` for the `ProcessorFeature` parameter from the allowed values. See [DB instance classes that support Optimize CPU](SQLServer.Concepts.General.OptimizeCPU.Support.md).
+ **Modify** – When modifying from one instance class configured with Optimize CPU settings to another one that supports Optimize CPU settings, you must specify the default processor features using the [UseDefaultProcessorFeatures](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) parameter or explicitly define the options during the modify request.
**Note**  
Changing the vCPU count can have implications for the licensing fee cost associated with the DB instance.
+ **Snapshot restore** – When restoring a snapshot to the same instance type as source, the restored DB instance inherits the Optimize CPU settings from the snapshot. If restoring to a different instance type, you need to define the Optimize CPU settings for the target instance or specify the [UseDefaultProcessorFeatures](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html) parameter.
+ **Point-in-time restore** – Point-in-time restore (PITR) involves restoring a specific snapshot based on the designated time for PITR and subsequently applying all transactional log backups to that snapshot, thereby bringing the instance to the specified point in time. For PITR, the Optimize CPU settings, `coreCount` and `threadsPerCore`, are derived from the source snapshot (not the point in time) unless custom values are specified during the PITR request. If the source snapshot being used is enabled with Optimize CPU settings and you are using a different instance type for PITR, you must define the Optimize CPU settings for the target instance or specify the [UseDefaultProcessorFeatures](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.html) parameter.

## Limitations
<a name="SQLServer.Concepts.General.OptimizeCPU.Limitations"></a>

The following limitations apply when using Optimize CPU:
+ Optimize CPU supports the following editions: Enterprise, Standard, and Web (License Included), and Enterprise, Standard, and Developer (Bring Your Own Media). Supported instance families include m7i, r7i, m8i, r8i, m8a, r8a, and x2m.
+ The valid number of CPU cores and threads per core depends on the instance class. For the valid values for each instance class, see [DB instance classes that support Optimize CPU](SQLServer.Concepts.General.OptimizeCPU.Support.md).
+ SQL Server requires a minimum number of vCPUs, and that minimum depends on the SQL Server edition. Amazon RDS rejects an Optimize CPU configuration that results in fewer vCPUs than the required minimum. This minimum applies only when you specify processor features. A DB instance that uses the instance class defaults can have fewer vCPUs.