

# Disabling Microsoft SQL Server resource governor for your RDS for SQL Server instance
<a name="ResourceGovernor.Disabling"></a>

When you disable resource governor on RDS for SQL Server, the service stops managing workload resources. Before you disable resource governor, review how this affects your database connections and configurations.

Disabling resource governor has the following results:
+ The classifier function isn't executed when a new connection is opened.
+ New connections are automatically classified into the default workload group.
+ All existing workload group and resource pool settings are reset to their default values.
+ No events are fired when limits are reached.
+ Resource governor configuration changes can be made, but the changes don't take effect until resource governor is enabled.

To disable resource governor, remove the `RESOURCE_GOVERNOR` option from its option group.

## Console
<a name="ResourceGovernor.Disabling.Console"></a>

The following procedure removes the `RESOURCE_GOVERNOR` option.

**To remove the RESOURCE\_GOVERNOR option from its option group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Option groups**.

1. Choose the option group with the `RESOURCE_GOVERNOR` option (`resource-governor-ee-2022` in the previous examples).

1. Choose **Delete option**.

1. Under **Deletion options**, choose **RESOURCE\_GOVERNOR** for **Options to delete**.

1. Under **Apply immediately**, choose **Yes** to delete the option immediately, or **No** to delete it during the next maintenance window.

1. Choose **Delete**.

## CLI
<a name="ResourceGovernor.Disabling.CLI"></a>

The following procedure removes the `RESOURCE_GOVERNOR` option.

**To remove the RESOURCE\_GOVERNOR option from its option group**
+ Run one of the following commands.  
**Example**  

  For Linux, macOS, or Unix:

  ```
  aws rds remove-option-from-option-group \
      --option-group-name {{resource-governor-ee-2022}} \
      --options RESOURCE_GOVERNOR \
      --apply-immediately
  ```

  For Windows:

  ```
  aws rds remove-option-from-option-group ^
      --option-group-name {{resource-governor-ee-2022}} ^
      --options RESOURCE_GOVERNOR ^
      --apply-immediately
  ```