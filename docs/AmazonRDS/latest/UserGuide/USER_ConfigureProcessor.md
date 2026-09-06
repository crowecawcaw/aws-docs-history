

# Configuring the processor for a DB instance class in RDS for Oracle
<a name="USER_ConfigureProcessor"></a>

Amazon RDS DB instance classes support Intel Hyper-Threading Technology, which enables multiple threads to run concurrently on a single Intel Xeon CPU core. Each thread is represented as a virtual CPU (vCPU) on the DB instance. A DB instance has a default number of CPU cores, which varies according to DB instance class. For example, a db.m4.xlarge DB instance class has two CPU cores and two threads per core by default—four vCPUs in total.

**Note**  
Each vCPU is a hyperthread of an Intel Xeon CPU core.

**Topics**
+ [Overview of processor configuration for RDS for Oracle](#USER_ConfigureProcessor.Overview)
+ [DB instance classes that support processor configuration](#USER_ConfigureProcessor.CPUOptionsDBInstanceClass)
+ [Setting the CPU cores and threads per CPU core for a DB instance class](#USER_ConfigureProcessor.SettingCPUOptions)

## Overview of processor configuration for RDS for Oracle
<a name="USER_ConfigureProcessor.Overview"></a>

When you use RDS for Oracle, you can usually find a DB instance class that has a combination of memory and number of vCPUs to suit your workloads. However, you can also specify the following processor features to optimize your RDS for Oracle DB instance for specific workloads or business needs:
+ **Number of CPU cores** – You can customize the number of CPU cores for the DB instance. You might do this to potentially optimize the licensing costs of your software with a DB instance that has sufficient amounts of RAM for memory-intensive workloads but fewer CPU cores.
+ **Threads per core** – You can disable Intel Hyper-Threading Technology by specifying a single thread per CPU core. You might do this for certain workloads, such as high-performance computing (HPC) workloads.

You can control the number of CPU cores and threads for each core separately. You can set one or both in a request. After a setting is associated with a DB instance, the setting persists until you change it.

The processor settings for a DB instance are associated with snapshots of the DB instance. When a snapshot is restored, its restored DB instance uses the processor feature settings used when the snapshot was taken.

If you modify the DB instance class for a DB instance with nondefault processor settings, either specify default processor settings or explicitly specify processor settings at modification. This requirement ensures that you are aware of the third-party licensing costs that might be incurred when you modify the DB instance.

There is no additional or reduced charge for specifying processor features on an RDS for Oracle DB instance. You're charged the same as for DB instances that are launched with default CPU configurations.

## DB instance classes that support processor configuration
<a name="USER_ConfigureProcessor.CPUOptionsDBInstanceClass"></a>

You can configure the number of CPU cores and threads per core only when the following conditions are met: 
+ You're configuring an RDS for Oracle DB instance. For information about the DB instance classes supported by different Oracle Database editions, see [RDS for Oracle DB instance classes](Oracle.Concepts.InstanceClasses.md).
+ Your DB instance is using the Bring Your Own License (BYOL) licensing option of RDS for Oracle. For more information about Oracle licensing options, see [RDS for Oracle licensing options](Oracle.Concepts.Licensing.md).
+ Your DB instance doesn't belong to one of the db.r5 or db.r5b instance classes that have predefined processor configurations. These instance classes have names in the form db.r5.{{instance\_size}}.tpc{{threads\_per\_core}}.mem{{ratio}} or db.r5b.{{instance\_size}}.tpc{{threads\_per\_core}}.mem{{ratio}}. For example, db.r5b.xlarge.tpc2.mem4x is preconfigured with 2 threads per core (tpc2) and 4x as much memory as the standard db.r5b.xlarge instance class. You can't configure the processor features of these optimized instance classes. For more information, see [Supported RDS for Oracle DB instance classes](Oracle.Concepts.InstanceClasses.md#Oracle.Concepts.InstanceClasses.Supported).

You can use the following AWS CLI command to show the default vCPUs, cores, threads per core, and valid numbers of cores for an instance class. Replace `{{r7i.48xlarge}}` in the sample command with the name of your instance class.

```
aws ec2 describe-instance-types \
    --instance-types {{r7i.48xlarge}} \
    --query '{
        DefaultVCPUs: InstanceTypes[0].VCpuInfo.DefaultVCpus,
        DefaultCores: InstanceTypes[0].VCpuInfo.DefaultCores,
        DefaultThreadsPerCore: InstanceTypes[0].VCpuInfo.DefaultThreadsPerCore,
        ValidCores: InstanceTypes[0].VCpuInfo.ValidCores
    }' \
    --output json
```

In the following table, you can find the DB instance classes that support setting a number of CPU cores and CPU threads per core. You can also find the default value and the valid values for the number of CPU cores and CPU threads per core for each DB instance class.


<a name="db-instance-class-cpu-core-support"></a>
<table>
<thead>
  <tr><th>DB instance class</th><th>Default vCPUs</th><th>Default CPU cores</th><th>Default threads per core</th><th>Valid number of CPU cores</th><th>Valid number of threads per core</th></tr>
</thead>
<tbody>
  <tr><td colspan="6"><b>db.m6i – memory-optimized instance classes</b></td></tr>
  <tr><td>db.m6i.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.m6i.xlarge</td><td>4</td><td>2</td><td>2</td><td>2</td><td>1, 2</td></tr>
  <tr><td>db.m6i.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.m6i.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.m6i.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.m6i.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td>db.m6i.12xlarge</td><td>48</td><td>24</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24</td><td>1, 2</td></tr>
  <tr><td>db.m6i.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td>db.m6i.24xlarge</td><td>96</td><td>48</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48</td><td>1, 2</td></tr>
  <tr><td>db.m6i.32xlarge</td><td>128</td><td>64</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.m5 – general-purpose instance classes</b></td></tr>
  <tr><td>db.m5.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.m5.xlarge</td><td>4</td><td>2</td><td>2</td><td>2</td><td>1, 2</td></tr>
  <tr><td>db.m5.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.m5.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.m5.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td>db.m5.12xlarge</td><td>48</td><td>24</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24</td><td>1, 2</td></tr>
  <tr><td>db.m5.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td>db.m5.24xlarge</td><td>96</td><td>48</td><td>2</td><td>4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.m5d – general-purpose instance classes</b></td></tr>
  <tr><td>db.m5d.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.m5d.xlarge</td><td>4</td><td>2</td><td>2</td><td>2</td><td>1, 2</td></tr>
  <tr><td>db.m5d.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.m5d.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.m5d.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td>db.m5d.12xlarge</td><td>48</td><td>24</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24</td><td>1, 2</td></tr>
  <tr><td>db.m5d.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td>db.m5d.24xlarge</td><td>96</td><td>48</td><td>2</td><td>4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.m4 – general-purpose instance classes</b></td></tr>
  <tr><td>db.m4.10xlarge</td><td>40</td><td>20</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20</td><td>1, 2</td></tr>
  <tr><td>db.m4.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.r7i – memory-optimized instance classes</b></td></tr>
  <tr><td>db.r7i.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.r7i.xlarge</td><td>4</td><td>2</td><td>2</td><td>1, 2</td><td>1, 2</td></tr>
  <tr><td>db.r7i.2xlarge</td><td>8</td><td>4</td><td>2</td><td>1, 2, 3, 4</td><td>1, 2</td></tr>
  <tr><td>db.r7i.4xlarge</td><td>16</td><td>8</td><td>2</td><td>1, 2, 3, 4, 5, 6, 7, 8</td><td>1, 2</td></tr>
  <tr><td>db.r7i.8xlarge</td><td>32</td><td>16</td><td>2</td><td>1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16</td><td>1, 2</td></tr>
  <tr><td>db.r7i.12xlarge</td><td>48</td><td>24</td><td>2</td><td>1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24</td><td>1, 2</td></tr>
  <tr><td>db.r7i.16xlarge</td><td>64</td><td>32</td><td>2</td><td>1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32</td><td>1, 2</td></tr>
  <tr><td>db.r7i.24xlarge</td><td>96</td><td>48</td><td>2</td><td>1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48</td><td>1, 2</td></tr>
  <tr><td>db.r7i.48xlarge</td><td>192</td><td>96</td><td>2</td><td>4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.r6i – memory-optimized instance classes</b></td></tr>
  <tr><td>db.r6i.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.r6i.xlarge</td><td>4</td><td>2</td><td>2</td><td>1, 2</td><td>1, 2</td></tr>
  <tr><td>db.r6i.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.r6i.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.r6i.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td>db.r6i.12xlarge</td><td>48</td><td>24</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24</td><td>1, 2</td></tr>
  <tr><td>db.r6i.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td>db.r6i.24xlarge</td><td>96</td><td>48</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48</td><td>1, 2</td></tr>
  <tr><td>db.r6i.32xlarge</td><td>128</td><td>64</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.r5 – memory-optimized instance classes</b></td></tr>
  <tr><td>db.r5.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.r5.xlarge</td><td>4</td><td>2</td><td>2</td><td>2</td><td>1, 2</td></tr>
  <tr><td>db.r5.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.r5.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.r5.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td>db.r5.12xlarge</td><td>48</td><td>24</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24</td><td>1, 2</td></tr>
  <tr><td>db.r5.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td>db.r5.24xlarge</td><td>96</td><td>48</td><td>2</td><td>4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.r5 – memory-optimized instance classes</b></td></tr>
  <tr><td>db.r5b.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.r5b.xlarge</td><td>4</td><td>2</td><td>2</td><td>2</td><td>1, 2</td></tr>
  <tr><td>db.r5b.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.r5b.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.r5b.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td>db.r5b.12xlarge</td><td>48</td><td>24</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24</td><td>1, 2</td></tr>
  <tr><td>db.r5b.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td>db.r5b.24xlarge</td><td>96</td><td>48</td><td>2</td><td>4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.r5d – memory-optimized instance classes</b></td></tr>
  <tr><td>db.r5d.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.r5d.xlarge</td><td>4</td><td>2</td><td>2</td><td>2</td><td>1, 2</td></tr>
  <tr><td>db.r5d.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.r5d.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.r5d.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td>db.r5d.12xlarge</td><td>48</td><td>24</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24</td><td>1, 2</td></tr>
  <tr><td>db.r5d.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td>db.r5d.24xlarge</td><td>96</td><td>48</td><td>2</td><td>4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.r4 – memory-optimized instance classes</b></td></tr>
  <tr><td>db.r4.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.r4.xlarge</td><td>4</td><td>2</td><td>2</td><td>1, 2</td><td>1, 2</td></tr>
  <tr><td>db.r4.2xlarge</td><td>8</td><td>4</td><td>2</td><td>1, 2, 3, 4</td><td>1, 2</td></tr>
  <tr><td>db.r4.4xlarge</td><td>16</td><td>8</td><td>2</td><td>1, 2, 3, 4, 5, 6, 7, 8</td><td>1, 2</td></tr>
  <tr><td>db.r4.8xlarge</td><td>32</td><td>16</td><td>2</td><td>1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16</td><td>1, 2</td></tr>
  <tr><td>db.r4.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.r3 – memory-optimized instance classes</b></td></tr>
  <tr><td>db.r3.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.r3.xlarge</td><td>4</td><td>2</td><td>2</td><td>1, 2</td><td>1, 2</td></tr>
  <tr><td>db.r3.2xlarge</td><td>8</td><td>4</td><td>2</td><td>1, 2, 3, 4</td><td>1, 2</td></tr>
  <tr><td>db.r3.4xlarge</td><td>16</td><td>8</td><td>2</td><td>1, 2, 3, 4, 5, 6, 7, 8</td><td>1, 2</td></tr>
  <tr><td>db.r3.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.x2idn – memory-optimized instance classes</b></td></tr>
  <tr><td>db.x2idn.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td>db.x2idn.24xlarge</td><td>96</td><td>48</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48</td><td>1, 2</td></tr>
  <tr><td>db.x2idn.32xlarge</td><td>128</td><td>64</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.x2iedn – memory-optimized instance classes</b></td></tr>
  <tr><td>db.x2iedn.xlarge</td><td>4</td><td>2</td><td>2</td><td>1, 2</td><td>1, 2</td></tr>
  <tr><td>db.x2iedn.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.x2iedn.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.x2iedn.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td>db.x2iedn.16xlarge</td><td>64</td><td>32</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32</td><td>1, 2</td></tr>
  <tr><td>db.x2iedn.24xlarge</td><td>96</td><td>48</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48</td><td>1, 2</td></tr>
  <tr><td>db.x2iedn.32xlarge</td><td>128</td><td>64</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.x2iezn – memory-optimized instance classes</b></td></tr>
  <tr><td>db.x2iezn.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.x2iezn.4xlarge</td><td>16</td><td>8</td><td>2</td><td>2, 4, 6, 8</td><td>1, 2</td></tr>
  <tr><td>db.x2iezn.6xlarge</td><td>24</td><td>12</td><td>2</td><td>2, 4, 6, 8, 10, 12</td><td>1, 2</td></tr>
  <tr><td>db.x2iezn.8xlarge</td><td>32</td><td>16</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16</td><td>1, 2</td></tr>
  <tr><td>db.x2iezn.12xlarge</td><td>48</td><td>24</td><td>2</td><td>2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24</td><td>1, 2</td></tr>
  <tr><td colspan="6"><b>db.z1d – memory-optimized instance classes</b></td></tr>
  <tr><td>db.z1d.large</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1, 2</td></tr>
  <tr><td>db.z1d.xlarge</td><td>4</td><td>2</td><td>2</td><td>2</td><td>1, 2</td></tr>
  <tr><td>db.z1d.2xlarge</td><td>8</td><td>4</td><td>2</td><td>2, 4</td><td>1, 2</td></tr>
  <tr><td>db.z1d.3xlarge</td><td>12</td><td>6</td><td>2</td><td>2, 4, 6</td><td>1, 2</td></tr>
  <tr><td>db.z1d.6xlarge</td><td>24</td><td>12</td><td>2</td><td>2, 4, 6, 8, 10, 12</td><td>1, 2</td></tr>
  <tr><td>db.z1d.12xlarge</td><td>48</td><td>24</td><td>2</td><td>4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24</td><td>1, 2</td></tr>
</tbody>
</table>


**Note**  
You can use AWS CloudTrail to monitor and audit changes to the process configuration of Amazon RDS for Oracle DB instances. For more information about using CloudTrail, see [Monitoring Amazon RDS API calls in AWS CloudTrail](logging-using-cloudtrail.md).

## Setting the CPU cores and threads per CPU core for a DB instance class
<a name="USER_ConfigureProcessor.SettingCPUOptions"></a>

You can configure the number of CPU cores and threads per core for the DB instance class when you perform the following operations:
+ [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md)
+ [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md)
+ [Restoring to a DB instance](USER_RestoreFromSnapshot.md)
+ [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md)

**Note**  
When you modify a DB instance to configure the number of CPU cores or threads per core, there is a brief DB instance outage.

You can set the CPU cores and the threads per CPU core for a DB instance class using the AWS Management Console, the AWS CLI, or the RDS API.

### Console
<a name="USER_ConfigureProcessor.Console"></a>

When you are creating, modifying, or restoring a DB instance, you set the DB instance class in the AWS Management Console. The **Instance specifications** section shows options for the processor. The following image shows the processor features options.

![Configure processor options.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/vcpu-config.png)


Set the following options to the appropriate values for your DB instance class under **Processor features**:
+ **Core count – **Set the number of CPU cores using this option. The value must be equal to or less than the maximum number of CPU cores for the DB instance class.
+ **Threads per core** – Specify **2** to enable multiple threads per core, or specify **1** to disable multiple threads per core.

When you modify or restore a DB instance, you can also set the CPU cores and the threads per CPU core to the defaults for the instance class.

When you view the details for a DB instance in the console, you can view the processor information for its DB instance class on the **Configuration** tab. The following image shows a DB instance class with one CPU core and multiple threads per core enabled.

![View processor options.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/vcpu-view.png)


For Oracle DB instances, the processor information only appears for Bring Your Own License (BYOL) DB instances.

### AWS CLI
<a name="USER_ConfigureProcessor.CLI"></a>

You can set the processor features for a DB instance when you run one of the following AWS CLI commands:
+ [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html)
+ [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html)
+ [restore-db-instance-from-db-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-db-snapshot.html)
+ [restore-db-instance-from-s3](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-s3.html)
+ [restore-db-instance-to-point-in-time](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-to-point-in-time.html)

To configure the processor of a DB instance class for a DB instance by using the AWS CLI, include the `--processor-features` option in the command. Specify the number of CPU cores with the `coreCount` feature name, and specify whether multiple threads per core are enabled with the `threadsPerCore` feature name. 

The option has the following syntax.

```
--processor-features "Name=coreCount,Value={{<value>}}" "Name=threadsPerCore,Value={{<value>}}"
```

The following are examples that configure the processor:

**Topics**
+ [Setting the number of CPU cores for a DB instance](#USER_ConfigureProcessor.CLI.Example1)
+ [Setting the number of CPU cores and disabling multiple threads for a DB instance](#USER_ConfigureProcessor.CLI.Example2)
+ [Viewing the valid processor values for a DB instance class](#USER_ConfigureProcessor.CLI.Example3)
+ [Returning to default processor settings for a DB instance](#USER_ConfigureProcessor.CLI.Example4)
+ [Returning to the default number of CPU cores for a DB instance](#USER_ConfigureProcessor.CLI.Example5)
+ [Returning to the default number of threads per core for a DB instance](#USER_ConfigureProcessor.CLI.Example6)

#### Setting the number of CPU cores for a DB instance
<a name="USER_ConfigureProcessor.CLI.Example1"></a>

**Example**  
The following example modifies `mydbinstance` by setting the number of CPU cores to 4. The changes are applied immediately by using `--apply-immediately`. If you want to apply the changes during the next scheduled maintenance window, omit the `--apply-immediately` option.   
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mydbinstance}} \
    --processor-features "Name=coreCount,Value={{4}}" \
    {{--apply-immediately}}
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mydbinstance}} ^
    --processor-features "Name=coreCount,Value={{4}}" ^
    {{--apply-immediately}}
```

#### Setting the number of CPU cores and disabling multiple threads for a DB instance
<a name="USER_ConfigureProcessor.CLI.Example2"></a>

**Example**  
The following example modifies `mydbinstance` by setting the number of CPU cores to `4` and disabling multiple threads per core. The changes are applied immediately by using `--apply-immediately`. If you want to apply the changes during the next scheduled maintenance window, omit the `--apply-immediately` option.  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mydbinstance}} \
    --processor-features "Name=coreCount,Value={{4}}" "Name=threadsPerCore,Value={{1}}" \
    {{--apply-immediately}}
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mydbinstance}} ^
    --processor-features "Name=coreCount,Value={{4}}" "Name=threadsPerCore,Value={{1}}" ^
    {{--apply-immediately}}
```

#### Viewing the valid processor values for a DB instance class
<a name="USER_ConfigureProcessor.CLI.Example3"></a>

**Example**  
You can view the valid processor values for a particular DB instance class by running the [describe-orderable-db-instance-options](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-orderable-db-instance-options.html) command and specifying the instance class for the `--db-instance-class` option. For example, the output for the following command shows the processor options for the db.r3.large instance class.  

```
aws rds describe-orderable-db-instance-options --engine oracle-ee --db-instance-class db.r3.large
```
Following is sample output for the command in JSON format.  

```
    {
                "SupportsIops": true,
                "MaxIopsPerGib": 50.0,
                "LicenseModel": "bring-your-own-license",
                "DBInstanceClass": "db.r3.large",
                "SupportsIAMDatabaseAuthentication": false,
                "MinStorageSize": 100,
                "AvailabilityZones": [
                    {
                        "Name": "us-west-2a"
                    },
                    {
                        "Name": "us-west-2b"
                    },
                    {
                        "Name": "us-west-2c"
                    }
                ],
                "EngineVersion": "12.1.0.2.v2",
                "MaxStorageSize": 32768,
                "MinIopsPerGib": 1.0,
                "MaxIopsPerDbInstance": 40000,
                "ReadReplicaCapable": false,
                "AvailableProcessorFeatures": [
                    {
                        "Name": "coreCount",
                        "DefaultValue": "1",
                        "AllowedValues": "1"
                    },
                    {
                        "Name": "threadsPerCore",
                        "DefaultValue": "2",
                        "AllowedValues": "1,2"
                    }
                ],
                "SupportsEnhancedMonitoring": true,
                "SupportsPerformanceInsights": false,
                "MinIopsPerDbInstance": 1000,
                "StorageType": "io1",
                "Vpc": false,
                "SupportsStorageEncryption": true,
                "Engine": "oracle-ee",
                "MultiAZCapable": true
    }
```
In addition, you can run the following commands for DB instance class processor information:  
+ [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) – Shows the processor information for the specified DB instance.
+ [describe-db-snapshots](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-snapshots.html) – Shows the processor information for the specified DB snapshot.
+ [describe-valid-db-instance-modifications](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-valid-db-instance-modifications.html) – Shows the valid modifications to the processor for the specified DB instance.
In the output of the preceding commands, the values for the processor features are not null only if the following conditions are met:  
+ You are using an RDS for Oracle DB instance.
+ Your RDS for Oracle DB instance supports changing processor values.
+ The current CPU core and thread settings are set to nondefault values.
If the preceding conditions aren't met, you can get the instance type using [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html). You can get the processor information for this instance type by running the EC2 operation [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html).

#### Returning to default processor settings for a DB instance
<a name="USER_ConfigureProcessor.CLI.Example4"></a>

**Example**  
The following example modifies `mydbinstance` by returning its DB instance class to the default processor values for it. The changes are applied immediately by using `--apply-immediately`. If you want to apply the changes during the next scheduled maintenance window, omit the `--apply-immediately` option.   
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mydbinstance}} \    
    --use-default-processor-features \
    {{--apply-immediately}}
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mydbinstance}} ^
    --use-default-processor-features ^
    {{--apply-immediately}}
```

#### Returning to the default number of CPU cores for a DB instance
<a name="USER_ConfigureProcessor.CLI.Example5"></a>

**Example**  
The following example modifies `mydbinstance` by returning its DB instance class to the default number of CPU cores for it. The threads per core setting isn't changed. The changes are applied immediately by using `--apply-immediately`. If you want to apply the changes during the next scheduled maintenance window, omit the `--apply-immediately` option.   
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mydbinstance}} \
    --processor-features "Name=coreCount,Value=DEFAULT" \
    {{--apply-immediately}}
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mydbinstance}} ^
    --processor-features "Name=coreCount,Value=DEFAULT" ^
    {{--apply-immediately}}
```

#### Returning to the default number of threads per core for a DB instance
<a name="USER_ConfigureProcessor.CLI.Example6"></a>

**Example**  
The following example modifies `mydbinstance` by returning its DB instance class to the default number of threads per core for it. The number of CPU cores setting isn't changed. The changes are applied immediately by using `--apply-immediately`. If you want to apply the changes during the next scheduled maintenance window, omit the `--apply-immediately` option.  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mydbinstance}} \
    --processor-features "Name=threadsPerCore,Value=DEFAULT" \
    {{--apply-immediately}}
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mydbinstance}} ^
    --processor-features "Name=threadsPerCore,Value=DEFAULT" ^
    {{--apply-immediately}}
```

### RDS API
<a name="USER_ConfigureProcessor.API"></a>

You can set the processor features for a DB instance when you call one of the following Amazon RDS API operations:
+ [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html)
+ [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html)
+ [RestoreDBInstanceFromDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html)
+ [RestoreDBInstanceFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromS3.html)
+ [RestoreDBInstanceToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.html)

To configure the processor features of a DB instance class for a DB instance by using the Amazon RDS API, include the `ProcessFeatures` parameter in the call.

The parameter has the following syntax.

```
ProcessFeatures "Name=coreCount,Value={{<value>}}" "Name=threadsPerCore,Value={{<value>}}"
```

Specify the number of CPU cores with the `coreCount` feature name, and specify whether multiple threads per core are enabled with the `threadsPerCore` feature name. 

You can view the valid processor values for a particular DB instance class by running the [DescribeOrderableDBInstanceOptions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeOrderableDBInstanceOptions.html) operation and specifying the instance class for the `DBInstanceClass` parameter. You can also use the following operations:
+ [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) – Shows the processor information for the specified DB instance.
+ [DescribeDBSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshots.html) – Shows the processor information for the specified DB snapshot.
+ [DescribeValidDBInstanceModifications](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeValidDBInstanceModifications.html) – Shows the valid modifications to the processor for the specified DB instance.

In the output of the preceding operations, the values for the processor features are not null only if the following conditions are met:
+ You are using an RDS for Oracle DB instance.
+ Your RDS for Oracle DB instance supports changing processor values.
+ The current CPU core and thread settings are set to nondefault values.

If the preceding conditions aren't met, you can get the instance type using [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html). You can get the processor information for this instance type by running the EC2 operation [DescribeInstanceTypes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypes.html).