# Uninstall AWS Backint agent

Use the following steps to uninstall AWS Backint agent.

1. Disable scheduled data and log backups if you are still using the agent for backups.
2. Remove the following symbolic links from the SAP HANA opt directory `/usr/sap/<SID>/SYS/global/hdb/opt`.
   1. SAP HANA link – `<HANA Opt directory>/hdbbackint`
   2. Config YAML link – `<HANA Opt directory>/hdbconfig/aws-backint-agent-config.yaml`

3. Remove or rename the agent installation directory.
4. Modify or remove the agent configuration parameters in the `global.ini` file.

Reset the following parameters that are modified during agent installation, to default.

    1. `catalog_backup_parameter_file`
    2. `data\_backup\_parameter\_file `
    3. `log\_backup\_parameter\_file `
    4. `catalog_backup_using_backint` – Set to false
    5. `log_backup_using_backint` – Set to false

5. Reconfigure the changes as database administrative user for them to take effect.

```
hdbnsutil -reconfig
```

Your backups on Amazon S3 or AWS Backup remain intact even after uninstalling AWS Backint agent from your Amazon EC2 instances. If you do not need the backups, you can delete them from Amazon S3 or AWS Backup.
