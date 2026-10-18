

# Setting the CPU cores and threads per CPU core for a DB instance class
<a name="SQLServer.Concepts.General.OptimizeCPU.Enabling"></a>

You can configure the number of CPU cores and threads per core for the DB instance class when you perform the following operations:
+ [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md)
+ [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md)
+ [Restoring to a DB instance](USER_RestoreFromSnapshot.md)
+ [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md)

**Note**  
When you modify a DB instance to configure the number of CPU cores or threads per core, there is a brief outage similar to when you modify the instance class.

Set the CPU cores by using the AWS Management Console, the [AWS CLI](https://aws.amazon.com/cli/), [AWS Tools for PowerShell](https://aws.amazon.com/powershell/), or the [Amazon RDS API](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/Welcome.html). The AWS CLI and AWS Tools for PowerShell come preinstalled in [AWS CloudShell](https://aws.amazon.com/cloudshell/).

The Optimize CPU settings are the [ProcessorFeature](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ProcessorFeature.html) values `coreCount` and `threadsPerCore`. The processor feature values are `null` if Optimize CPU is not configured.

## Console
<a name="SQLServer.Concepts.General.OptimizeCPU.Enabling.CON"></a>

**To set the processor features when you create a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Create database**.

1. When setting the **Instance configuration** options:

   1. Under **Optimize CPU**, select **Configure the number of vCPUs**.

   1. Under **vCPUs**, choose the number of **thread(s) per CPU core** and the number of **core(s)**. The lists show the valid values for the selected instance class. For more information, see [DB instance classes that support Optimize CPU](SQLServer.Concepts.General.OptimizeCPU.Support.md).  
![Database create page when setting OCPU settings.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/OCPU-screenshot.png)

1. After completing other selections, choose **Create database**.

**To view the processor features of a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance.

1. Choose the **Configuration** tab.

1. Under **Processor Features**, view the **vCPU**, **Core count**, and **Threads per core** values.

**To modify the processor features of a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance that you want to modify.

1. Choose **Modify**.

1. For **Optimize CPU**, choose **Configure the number of vCPUs**.

1. Under **vCPUs**, choose the number of **thread(s) per CPU core** and the number of **core(s)**. The lists show the valid values for the selected instance class. For more information, see [DB instance classes that support Optimize CPU](SQLServer.Concepts.General.OptimizeCPU.Support.md).

1. Choose **Continue**.

1. For **When to apply modifications**, choose **Apply during the next scheduled maintenance window** or **Apply immediately**.

1. Choose **Modify DB instance**.

**To return a DB instance to the default processor features**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance that you want to modify.

1. Choose **Modify**.

1. For **Optimize CPU**, choose **Use default vCPUs**.

1. Choose **Continue**.

1. For **When to apply modifications**, choose **Apply during the next scheduled maintenance window** or **Apply immediately**.

1. Choose **Modify DB instance**.

## AWS CLI
<a name="SQLServer.Concepts.General.OptimizeCPU.Enabling.CLI"></a>

**To set the processor features when you create a DB instance**

1. To configure Optimize CPU using the AWS CLI, include the `--processor-features` option in the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) command. Specify the number of CPU cores with the `coreCount` and `threadsPerCore` as `1`.

1. Use the following syntax:

   ```
   aws rds create-db-instance \
       --db-instance-identifier {{my-rds-instance}} \
       --engine sqlserver-ee \
       --engine-version 17.00 \
       --license-model license-included \
       --db-instance-class db.r8i.8xlarge \
       --allocated-storage 300 \
       --master-username {{admin}} \
       --manage-master-user-password \
       --no-multi-az \
       --vpc-security-group-ids {{sg-0123456789abcdef0}} \
       --db-subnet-group-name {{mydbsubnetgroup}} \
       --processor-features "Name=coreCount,Value={{12}}" "Name=threadsPerCore,Value=1"
   ```

**Example of viewing valid processor features for a DB instance class**  
Use the [describe-orderable-db-instance-options](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-orderable-db-instance-options.html) command to show the default and allowed values.  

```
aws rds describe-orderable-db-instance-options \
    --engine sqlserver-ee \
    --db-instance-class db.r8i.8xlarge \
    --query "OrderableDBInstanceOptions[0].AvailableProcessorFeatures"
```
In addition, you can run the following commands for DB instance class processor information:  
+ [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) – Shows the processor information for the specified DB instance
+ [describe-db-snapshots](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-snapshots.html) – Shows the processor information for the specified DB snapshot
+ [describe-valid-db-instance-modifications](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-valid-db-instance-modifications.html) – Shows the valid modifications to the processor for the specified DB instance

**Example of setting the number of CPU cores for a DB instance**  
The following example uses the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command to modify {{my-rds-instance}} by setting the number of CPU cores to 12 and threadsPerCore to 1. Apply the changes immediately by using `--apply-immediately`. If you want to apply the changes during the next scheduled maintenance window, omit the `--apply-immediately` option.  

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-rds-instance}} \
    --processor-features "Name=coreCount,Value={{12}}" "Name=threadsPerCore,Value=1" \
    --apply-immediately
```

**Example of returning to default processor features for a DB instance**  
The following example uses the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command to modify {{my-rds-instance}} by returning it to the default processor features.  

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-rds-instance}} \
    --use-default-processor-features \
    --apply-immediately
```

## PowerShell
<a name="SQLServer.Concepts.General.OptimizeCPU.Enabling.PS"></a>

**To set the processor features when you create a DB instance**

1. To configure Optimize CPU using AWS Tools for PowerShell, include the `-ProcessorFeature` parameter in the [New-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-RDSDBInstance.html) cmdlet. Specify the number of CPU cores with the `coreCount` and `threadsPerCore` as `1`.

1. Use the following syntax:

   ```
   New-RDSDBInstance `
       -DBInstanceIdentifier {{my-rds-instance}} `
       -Engine sqlserver-ee `
       -EngineVersion 17.00 `
       -LicenseModel license-included `
       -DBInstanceClass db.r8i.8xlarge `
       -AllocatedStorage 300 `
       -MasterUsername {{admin}} `
       -ManageMasterUserPassword $true `
       -MultiAZ $false `
       -VpcSecurityGroupId {{sg-0123456789abcdef0}} `
       -DBSubnetGroupName {{mydbsubnetgroup}} `
       -ProcessorFeature @{Name='coreCount';Value='{{12}}'},@{Name='threadsPerCore';Value='1'}
   ```

**Example of viewing valid processor features for a DB instance class**  
Use the [Get-RDSOrderableDBInstanceOption](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-RDSOrderableDBInstanceOption.html) cmdlet to show the default and allowed values.  

```
Get-RDSOrderableDBInstanceOption `
    -Engine sqlserver-ee `
    -DBInstanceClass db.r8i.8xlarge |
    Select-Object -First 1 -ExpandProperty AvailableProcessorFeatures
```
In addition, you can run the following cmdlets for DB instance class processor information:  
+ [Get-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-RDSDBInstance.html) – Shows the processor information for the specified DB instance
+ [Get-RDSDBSnapshot](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-RDSDBSnapshot.html) – Shows the processor information for the specified DB snapshot
+ [Get-RDSValidDBInstanceModification](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-RDSValidDBInstanceModification.html) – Shows the valid modifications to the processor for the specified DB instance

**Example of setting the number of CPU cores for a DB instance**  
The following example uses AWS Tools for PowerShell and the [Edit-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-RDSDBInstance.html) cmdlet to modify {{my-rds-instance}} by setting the number of CPU cores to 12 and threadsPerCore to 1. If you want to apply the changes during the next scheduled maintenance window, omit the `-ApplyImmediately` parameter.  

```
Edit-RDSDBInstance `
    -DBInstanceIdentifier {{my-rds-instance}} `
    -ProcessorFeature @{Name='coreCount';Value='{{12}}'},@{Name='threadsPerCore';Value='1'} `
    -ApplyImmediately $true
```

**Example of returning to default processor features for a DB instance**  
The following example uses AWS Tools for PowerShell and the [Edit-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-RDSDBInstance.html) cmdlet to modify {{my-rds-instance}} by returning it to the default processor features.  

```
Edit-RDSDBInstance `
    -DBInstanceIdentifier {{my-rds-instance}} `
    -UseDefaultProcessorFeature $true `
    -ApplyImmediately $true
```