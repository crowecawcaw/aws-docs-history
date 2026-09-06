

# Uninstall AWS Backint agent
<a name="uninstall-agent"></a>

Use the following steps to uninstall AWS Backint agent.

1. Disable scheduled data and log backups if you are still using the agent for backups.

1. Remove the following symbolic links from the SAP HANA opt directory `/usr/sap/<SID>/SYS/global/hdb/opt`.

   1. SAP HANA link – `<HANA Opt directory>/hdbbackint` 

   1. Config YAML link – `<HANA Opt directory>/hdbconfig/aws-backint-agent-config.yaml` 

1. Remove or rename the agent installation directory.

1. Modify or remove the agent configuration parameters in the `global.ini` file.

   Reset the following parameters that are modified during agent installation, to default.

   1.  `catalog_backup_parameter_file` 

   1.  `data_backup_parameter_file` 

   1.  `log_backup_parameter_file` 

   1.  `catalog_backup_using_backint` – Set to false

   1.  `log_backup_using_backint` – Set to false

1. Reconfigure the changes as database administrative user for them to take effect.

   ```
   hdbnsutil -reconfig
   ```

Your backups on Amazon S3 or AWS Backup remain intact even after uninstalling AWS Backint agent from your Amazon EC2 instances. If you do not need the backups, you can delete them from Amazon S3 or AWS Backup.