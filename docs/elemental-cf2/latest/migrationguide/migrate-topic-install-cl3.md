# Installing Conductor File on nodes

1. From the Linux command line, log in to the Conductor node where you want to
   install Conductor File software. Use the _elemental_ user
   credentials.
2. Run the installer:
   - For the **primary** (or only) Conductor File, enter this
     command:

   ```
   [elemental@hostname ~]$ **sudo sh ./elemental\_production\_conductor\_file\_2.18.0.12345.run --skip-all --start -xeula**
   ```

   Where:

   `--skip-all` skips all the prompts, which means you won't
   change anything about the configuration.

   Don't change anything about the configuration as part of the upgrade
   either of the Conductor nodes. Don't change the hostname. If you want to
   change anything about the configuration, you can do so after you've
   completed the migration.

   `--start` restarts the software after installation.

   `--xeula` skips the display of the license agreement. There
   is no need to view this prompt because you have previously accepted the
   agreement.
   - For the **secondary** Conductor File, enter this
     command:

   ```
   [elemental@hostname ~]$ **sudo sh ./elemental\_production\_conductor\_file\_2.18.0.12345.run --cleandb --skip-all --start -xeula**
   ```

   Where:

   `--cleandb` deletes the application database. This option
   is required on the secondary Conductor node. You don't need the
   application database because when you add the secondary Conductor node
   back into the cluster, the secondary Conductor node will synchronize
   with the database of the primary Conductor node.

   Note that this option doesn't clean operating system configuration
   data.

   `--skip-all` skips all the prompts, which means you won't
   change anything about the configuration.

   Don't change anything about the configuration as part of the upgrade
   either of the Conductor nodes. Don't change the hostname. If you want to
   change anything about the configuration, you can do so after you've
   completed the migration.

   `--start` restarts the software after installation.

   `--xeula` skips the display of the license agreement. There
   is no need to view this prompt because you have previously accepted the
   agreement.

3. Make sure that the elemental_se service restarts. Look for this prompt on the
   primary Conductor command line:

```
Starting elemental_se:            [OK]
```
