

# Adding the NATIVE\_NETWORK\_ENCRYPTION option
<a name="Oracle.Options.NNE.Add"></a>

The general process for adding the `NATIVE_NETWORK_ENCRYPTION` option to a DB instance is the following: 

1. Create a new option group, or copy or modify an existing option group.

1. Add the option to the option group.

1. Associate the option group with the DB instance.

When the option group is active, NNE is active. 

**To add the NATIVE\_NETWORK\_ENCRYPTION option to a DB instance using the AWS Management Console**

1. For **Engine**, choose the Oracle edition that you want to use. NNE is supported on all editions. 

1. For **Major engine version**, choose the version of your DB instance. 

   For more information, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create). 

1. Add the **NATIVE\_NETWORK\_ENCRYPTION** option to the option group. For more information about adding options, see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption).
**Note**  
After you add the **NATIVE\_NETWORK\_ENCRYPTION** option, you don't need to restart your DB instances. As soon as the option group is active, NNE is active. 

1. Apply the option group to a new or existing DB instance: 
   + For a new DB instance, you apply the option group when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md).
   + For an existing DB instance, you apply the option group by modifying the instance and attaching the new option group. After you add the **NATIVE\_NETWORK\_ENCRYPTION** option, you don't need to restart your DB instance. As soon as the option group is active, NNE is active. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md). 