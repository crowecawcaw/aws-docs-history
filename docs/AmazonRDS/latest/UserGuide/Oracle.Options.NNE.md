# Adding the NATIVE_NETWORK_ENCRYPTION option

The general process for adding the `NATIVE_NETWORK_ENCRYPTION` option to a
DB instance is the following:

1. Create a new option group, or copy or modify an existing option group.
2. Add the option to the option group.
3. Associate the option group with the DB instance.
   When the option group is active, NNE is active.

###### To add the NATIVE_NETWORK_ENCRYPTION option to a DB instance using the

AWS Management Console

1. For **Engine**,
   choose the Oracle edition that you want to use.
   NNE is supported on all editions.
2. For **Major engine version**,
   choose the version of your DB instance.

For more information,
see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create"). 3. Add the **NATIVE_NETWORK_ENCRYPTION** option to the option
group. For more information about adding options, see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption").

###### Note

After you add the **NATIVE_NETWORK_ENCRYPTION** option,
you don't need to restart your DB instances. As soon as the option group is
active, NNE is active. 4. Apply the option group to a new or existing DB instance:

    * For a new DB instance, you apply the option group when you launch the instance. For more
     information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
    * For an existing DB instance, you apply the option group by modifying the
     instance and attaching the new option group. After you add the
     **NATIVE\_NETWORK\_ENCRYPTION** option, you don't
     need to restart your DB instance. As soon as the option group is active, NNE
     is active. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
