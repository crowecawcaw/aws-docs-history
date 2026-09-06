

# Setting up Trusted Language Extensions in your Aurora PostgreSQL DB cluster
<a name="PostgreSQL_trusted_language_extension-setting-up"></a>

The following steps assume that your Aurora PostgreSQL DB cluster is associated with a custom DB cluster parameter group. You can use the AWS Management Console or the AWS CLI for these steps.

When you set up Trusted Language Extensions in your Aurora PostgreSQL DB cluster , you install it in a specific database for use by the database users who have permissions on that database. 

## Console
<a name="PostgreSQL_trusted_language_extension-setting-up.CON"></a>

**To set up Trusted Language Extensions**

Perform the following steps using an account that's a member of the `rds_superuser` group (role).

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose your Aurora PostgreSQL DB cluster's Writer instance .

1. Open the **Configuration** tab for your Aurora PostgreSQL DB cluster writer instance.  Among the Instance details, find the **Parameter group** link.

1. Choose the link to open the custom parameters associated with your Aurora PostgreSQL DB cluster. 

1. In the **Parameters** search field, type `shared_pre` to find the `shared_preload_libraries` parameter.

1. Choose **Edit parameters** to access the property values.

1. Add `pg_tle` to the list in the **Values** field. Use a comma to separate items in the list of values.  
![The shared_preload_libraries parameter with pg_tle added.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg_rpg_shared_preload_pg_tle.png)

1. Reboot the writer instance of your Aurora PostgreSQL DB cluster so that your change to the `shared_preload_libraries` parameter takes effect.

1. When the instance is available, verify that `pg_tle` has been initialized. Use `psql` to connect to the writer instance of your Aurora PostgreSQL DB cluster, and then run the following command.

   ```
   SHOW shared_preload_libraries;
   shared_preload_libraries 
   --------------------------
   rdsutils,pg_tle
   (1 row)
   ```

1. With the `pg_tle` extension initialized, you can now create the extension. 

   ```
   CREATE EXTENSION pg_tle;
   ```

   You can verify that the extension is installed by using the following `psql` metacommand.

   ```
   labdb=> \dx
                            List of installed extensions
     Name   | Version |   Schema   |                Description
   ---------+---------+------------+--------------------------------------------
    pg_tle  | 1.0.1   | pgtle      | Trusted-Language Extensions for PostgreSQL
    plpgsql | 1.0     | pg_catalog | PL/pgSQL procedural language
   ```

1. Grant the `pgtle_admin` role to the primary user name that you created for your Aurora PostgreSQL DB cluster when you set it up. If you accepted the default, it's `postgres`. 

   ```
   labdb=> GRANT pgtle_admin TO postgres;
   GRANT ROLE
   ```

   You can verify that the grant has occurred by using the `psql` metacommand as shown in the following example. Only the `pgtle_admin` and `postgres` roles are shown in the output. For more information, see [Understanding PostgreSQL roles and permissions](Appendix.PostgreSQL.CommonDBATasks.Roles.md). 

   ```
   labdb=> \du
                             List of roles
       Role name    |           Attributes            |               Member of
   -----------------+---------------------------------+-----------------------------------
   pgtle_admin     | Cannot login                     | {}
   postgres        | Create role, Create DB          +| {rds_superuser,pgtle_admin}
                   | Password valid until infinity    |...
   ```

1. Close the `psql` session using the `\q` metacommand.

   ```
   \q
   ```

To get started creating TLE extensions, see [Example: Creating a trusted language extension using SQL](PostgreSQL_trusted_language_extension-creating-TLE-extensions.md#PostgreSQL_trusted_language_extension-simple-example). 

## AWS CLI
<a name="PostgreSQL_trusted_language_extension-setting-up-CLI"></a>

You can avoid specifying the `--region` argument when you use CLI commands by configuring your AWS CLI with your default AWS Region. For more information, see [Configuration basics](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) in the *AWS Command Line Interface User Guide*.

**To set up Trusted Language Extensions**

1. Use the [modify-db-parameter-group](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-parameter-group.html) AWS CLI command to add `pg_tle` to the `shared_preload_libraries` parameter.

   ```
   aws rds modify-db-parameter-group \
      --db-parameter-group-name {{custom-param-group-name}} \
      --parameters "ParameterName=shared_preload_libraries,ParameterValue=pg_tle,ApplyMethod=pending-reboot" \
      --region {{aws-region}}
   ```

1. Use the [reboot-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/reboot-db-instance) AWS CLI command to reboot the writer instance of your Aurora PostgreSQL DB cluster and initialize the `pg_tle` library.

   ```
   aws rds reboot-db-instance \
       --db-instance-identifier {{writer-instance}} \
       --region {{aws-region}}
   ```

1. When the instance is available, you can verify that `pg_tle` has been initialized. Use `psql` to connect to the writer instance of your Aurora PostgreSQL DB cluster, and then run the following command.

   ```
   SHOW shared_preload_libraries;
   shared_preload_libraries 
   --------------------------
   rdsutils,pg_tle
   (1 row)
   ```

   With `pg_tle` initialized, you can now create the extension.

   ```
   CREATE EXTENSION pg_tle;
   ```

1. Grant the `pgtle_admin` role to the primary user name that you created for your Aurora PostgreSQL DB cluster when you set it up. If you accepted the default, it's `postgres`.

   ```
   GRANT pgtle_admin TO postgres;
   GRANT ROLE
   ```

1. Close the `psql` session as follows.

   ```
   labdb=> \q
   ```

To get started creating TLE extensions, see [Example: Creating a trusted language extension using SQL](PostgreSQL_trusted_language_extension-creating-TLE-extensions.md#PostgreSQL_trusted_language_extension-simple-example). 