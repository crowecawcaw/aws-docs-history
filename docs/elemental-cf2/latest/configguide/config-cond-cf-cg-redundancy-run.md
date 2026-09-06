

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step C: Run the Redundancy Install Script
<a name="config-cond-cf-cg-redundancy-run"></a>

This install script configures Conductor redundancy.

1. On the primary Conductor, enter the following command to run the database redundancy install script.

   ```
   [elemental@hostname ~]$ sudo /opt/elemental_se/.support_utils/dbrepl configure dbrepl_config.yml primary
   ```

   where <dbrepl\_config> is the file that you created above.

1. You are prompted to restart the Conductor node. 

   ```
   [elemental@hostname ~]$ sudo /etc/init.d/elemental_se restart
   ```

1. On the secondary Conductor, enter the following command to configure the secondary Conductor.

   ```
   [elemental@hostname ~]$ sudo /opt/elemental_se/.support_utils/dbrepl configure dbrepl_config.yml secondary
   ```

   where <dbrepl\_config> is the file you created above.

1. You are prompted to restart the Conductor node.

   ```
   [elemental@hostname ~]$ sudo /etc/init.d/elemental_se restart
   ```