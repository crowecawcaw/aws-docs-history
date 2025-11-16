# Adding the EFS_INTEGRATION option

To integrate Amazon RDS for Oracle with Amazon EFS, your DB instance must be associated with an option
group that includes the `EFS_INTEGRATION` option.

Multiple Oracle DB instances that belong to the same option group share the same EFS file
system. Different DB instances can access the same data, but access can be divided by using
different Oracle directories. For more information see [Transferring files between RDS for Oracle
and an Amazon EFS file system](oracle-efs-integration.md "oracle-efs-integration.md").

###### To configure an option group for Amazon EFS integration

1. Create a new option group or identify an existing option group to which
   you can add the `EFS_INTEGRATION` option.

For information about creating an option group, see
[Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create"). 2. Add the `EFS_INTEGRATION` option to the option group. You need
to specify the `EFS_ID` file system ID and set the
`USE_IAM_ROLE` flag.

For more information, see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption"). 3. Associate the option group with your DB instance in either of the
following ways:

    * Create a new Oracle DB instance and associate the option group
     with it. For information about creating a DB instance, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
    * Modify an Oracle DB instance to associate the option group with
     it. For information about modifying an Oracle DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

###### To configure an option group for EFS integration

1. Create a new option group or identify an existing option group to which
   you can add the `EFS_INTEGRATION` option.

For information about creating an option group, see
[Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create"). 2. Add the `EFS_INTEGRATION` option to the option group.

For example, the following AWS CLI command adds the
`EFS_INTEGRATION` option to an option group named
`myoptiongroup`.

###### Example

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
   --option-group-name `myoptiongroup` \
   --options "OptionName=EFS_INTEGRATION,OptionSettings=\
   [{Name=EFS_ID,Value=fs-1234567890abcdef0},{Name=USE_IAM_ROLE,Value=TRUE}]"
```

For Windows:

```
aws rds add-option-to-option-group ^
   --option-group-name `myoptiongroup` ^
   --options "OptionName=EFS_INTEGRATION,OptionSettings=^
   [{Name=EFS_ID,Value=fs-1234567890abcdef0},{Name=USE_IAM_ROLE,Value=TRUE}]"
```

3. Associate the option group with your DB instance in either of the
   following ways:
   - Create a new Oracle DB instance and associate the option group
     with it. For information about creating a DB instance, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
   - Modify an Oracle DB instance to associate the option group with
     it. For information about modifying an Oracle DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
