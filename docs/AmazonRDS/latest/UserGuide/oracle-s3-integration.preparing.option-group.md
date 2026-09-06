

# Adding the Amazon S3 integration option
<a name="oracle-s3-integration.preparing.option-group"></a>

To integrate Amazon RDS for Oracle with Amazon S3, your DB instance must be associated with an option group that includes the `S3_INTEGRATION` option.

## Console
<a name="oracle-s3-integration.preparing.option-group.console"></a>

**To configure an option group for Amazon S3 integration**

1. Create a new option group or identify an existing option group to which you can add the `S3_INTEGRATION` option.

   For information about creating an option group, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create).

1. Add the `S3_INTEGRATION` option to the option group.

   For information about adding an option to an option group, see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption).

1. Create a new RDS for Oracle DB instance and associate the option group with it, or modify an RDS for Oracle DB instance to associate the option group with it.

   For information about creating a DB instance, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md).

   For information about modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).

## AWS CLI
<a name="oracle-s3-integration.preparing.option-group.cli"></a>

**To configure an option group for Amazon S3 integration**

1. Create a new option group or identify an existing option group to which you can add the `S3_INTEGRATION` option.

   For information about creating an option group, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create).

1. Add the `S3_INTEGRATION` option to the option group.

   For example, the following AWS CLI command adds the `S3_INTEGRATION` option to an option group named **myoptiongroup**.  
**Example**  

   For Linux, macOS, or Unix:

   ```
   aws rds add-option-to-option-group \
      --option-group-name {{myoptiongroup}} \
      --options OptionName=S3_INTEGRATION,OptionVersion=1.0
   ```

   For Windows:

   ```
   aws rds add-option-to-option-group ^
      --option-group-name {{myoptiongroup}} ^
      --options OptionName=S3_INTEGRATION,OptionVersion=1.0
   ```

1. Create a new RDS for Oracle DB instance and associate the option group with it, or modify an RDS for Oracle DB instance to associate the option group with it.

   For information about creating a DB instance, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md).

   For information about modifying an RDS for Oracle DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).