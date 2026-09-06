

# Setting up the pglogical extension
<a name="Appendix.PostgreSQL.CommonDBATasks.pglogical.basic-setup"></a>

To set up the `pglogical` extension on your Aurora PostgreSQL DB cluster, you add `pglogical` to the shared libraries on the custom DB cluster parameter group for your Aurora PostgreSQL DB cluster. You also need to set the value of the `rds.logical_replication` parameter to `1`, to turn on logical decoding. Finally, you create the extension in the database. You can use the AWS Management Console or the AWS CLI for these tasks. 

You must have permissions as the `rds_superuser` role to perform these tasks.

The steps following assume that your Aurora PostgreSQL DB cluster is associated with a custom DB cluster parameter group. For information about creating a custom DB cluster parameter group, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md). 

## Console
<a name="Appendix.PostgreSQL.CommonDBATasks.pglogical.basic-setup.CON"></a>

**To set up the pglogical extension**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose your Aurora PostgreSQL DB cluster's Writer instance .

1. Open the **Configuration** tab for your Aurora PostgreSQL DB cluster writer instance.  Among the Instance details, find the **Parameter group** link. 

1. Choose the link to open the custom parameters associated with your Aurora PostgreSQL DB cluster. 

1. In the **Parameters** search field, type `shared_pre` to find the `shared_preload_libraries` parameter.

1. Choose **Edit parameters** to access the property values.

1. Add `pglogical` to the list in the **Values** field. Use a comma to separate items in the list of values.   
![The shared_preload_libraries parameter with pglogical added.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg_rpg_shared_preload_pglogical.png)

1. Find the `rds.logical_replication` parameter and set it to `1`, to turn on logical replication.

1. Reboot the writer instance of your Aurora PostgreSQL DB cluster so that your changes take effect. 

1. When the instance is available, you can use `psql` (or pgAdmin) to connect to the writer instance of your Aurora PostgreSQL DB cluster. 

   ```
   psql --host={{111122223333}}.{{aws-region}}.rds.amazonaws.com --port=5432 --username={{postgres}} --password --dbname={{labdb}}
   ```

1. To verify that pglogical is initialized, run the following command.

   ```
   SHOW shared_preload_libraries;
   shared_preload_libraries 
   --------------------------
   rdsutils,pglogical
   (1 row)
   ```

1. Verify the setting that enables logical decoding, as follows.

   ```
   SHOW wal_level;
   wal_level
   -----------
    logical
   (1 row)
   ```

1. Create the extension, as follows.

   ```
   CREATE EXTENSION pglogical;
   EXTENSION CREATED
   ```

1. Choose **Save changes**.

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose your Aurora PostgreSQL DB cluster's writer instance from the Databases list to select it, and then choose **Reboot** from the Actions menu.

## AWS CLI
<a name="Appendix.PostgreSQL.CommonDBATasks.pglogical.basic-setup.CLI"></a>

**To setup the pglogical extension**

To setup pglogical using the AWS CLI, you call the [modify-db-parameter-group](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-parameter-group.html) operation to modify certain parameters in your custom parameter group as shown in the following procedure.

1. Use the following AWS CLI command to add `pglogical` to the `shared_preload_libraries` parameter.

   ```
   aws rds modify-db-parameter-group \
      --db-parameter-group-name {{custom-param-group-name}} \
      --parameters "ParameterName=shared_preload_libraries,ParameterValue=pglogical,ApplyMethod=pending-reboot" \
      --region {{aws-region}}
   ```

1. Use the following AWS CLI command to set `rds.logical_replication` to `1` to turn on the logical decoding capability for the writer instance of the Aurora PostgreSQL DB cluster. 

   ```
   aws rds modify-db-parameter-group \
      --db-parameter-group-name {{custom-param-group-name}} \
      --parameters "ParameterName=rds.logical_replication,ParameterValue=1,ApplyMethod=pending-reboot" \
      --region {{aws-region}}
   ```

1. Use the following AWS CLI command to reboot the writer instance of your Aurora PostgreSQL DB cluster so that the pglogical library is initialized.

   ```
   aws rds reboot-db-instance \
       --db-instance-identifier {{writer-instance}} \
       --region {{aws-region}}
   ```

1. When the instance is available, use `psql` to connect to the writer instance of your Aurora PostgreSQL DB cluster. 

   ```
   psql --host={{111122223333}}.{{aws-region}}.rds.amazonaws.com --port=5432 --username={{postgres}} --password --dbname={{labdb}}
   ```

1. Create the extension, as follows.

   ```
   CREATE EXTENSION pglogical;
   EXTENSION CREATED
   ```

1. Reboot the writer instance of your Aurora PostgreSQL DB cluster using the following AWS CLI command.

   ```
   aws rds reboot-db-instance \
       --db-instance-identifier {{writer-instance}} \
       --region {{aws-region}}
   ```