# Step F: Downgrade the nodes

When you downgrade, run the installer with the `--downgrade` option for each
node. Downgrade in the following order:

1. Primary Conductor Live
2. Secondary Conductor Live (if applicable)
3. Back-up worker nodes (if applicable)
4. Active worker nodes

###### To downgrade the primary Conductor Live

1. From the Linux prompt, log in with the _elemental_ user
   credentials. Once you are logged in, the initial directory is
   `/home/elemental`.
2. Enter the following command. For example:

```
[elemental@hostname ~]$ **chmod 755 elemental\_production\_conductor\_live247\_3.23.5.12345.run**
```

3. Run the installer as follows. For example:

```
[elemental@hostname ~]$ **sudo ./elemental\_production\_conductor\_live247\_3.23.5.12345.run -skip-all -xeula --start --downgrade --restore-db-backup `<path>`**
```

Options are as follows:

    * `-xeula`: Skips the prompts to read through the EULA. You are prompted
     once to accept it.
    * `--start`: Specifies to start the services without being
     prompted.
    * `--downgrade`: Tells the installer that an earlier version is being
     installed.
    * `--restore-db-backup <path>`: Installs the version old version of
     the database back-up file. Provides the path and file name in the following format:



    ```
    /home/elemental/elemental-db-backup_`<date>`_`<version>`.tar
    ```

4. Reboot the node with the following command:

```
[elemental@hostname ~]$ **sudo reboot**
```

5. Make sure that elemental_se restarts on this node; otherwise, you will not be able to
   downgrade the secondary Conductor Live node. Look for this prompt on the primary Conductor Live command
   line:

```
Starting elemental_se:     [  OK  ]
```

6. Refresh your web browser in order to load the updated web interface.

###### To downgrade the secondary Conductor Live node

Downgrade the secondary Conductor Live node using the same steps that you used above to
downgrade the primary Conductor Live node. Include the clean database option (--cleandb) in the
downgrade command instead of the restore database path. For example:

```
[elemental@hostname ~]$ **sudo ./elemental\_production\_conductor\_live247\_3.23.5.12345.run -skip-all -xeula --start --downgrade --cleandb**
```

###### To downgrade the worker nodes

If you're not downgrading worker nodes, skip this step and go to [Step G: Add the secondary
Conductor Live node](downgrades-add-sec.md "downgrades-add-sec.md").

If you have worker node redundancy, downgrade the back-up nodes first and then the
active nodes.

1. Enter the following command. For example:

```
[elemental@hostname ~]$ **chmod 755 elemental\_production\_live\_2.23.5.12345run**
```

2. Downgrade the active worker nodes following these steps. See [AWS Elemental Live Upgrade Guide](../../../elemental-live/latest/upgradeguide.md "../../../elemental-live/latest/upgradeguide.md") for
   more details.

Run the installer with the skip-all option. Use the following commands with the actual
file name of the .run file, rather than the example below:

    * For GPU and CPU versions of the software:



    ```
    [elemental@hostname ~]$ **sudo sh ./elemental\_production\_live\_2.23.5.12345.run -c --skip-all --start -xeula --downgrade**
    ```
    * For CPU-only versions of the software:



    ```
    [elemental@hostname ~]$ **sudo sh ./elemental\_production\_live\_cpu\_2.23.5.12345.run -c --skip-all --start -xeula --downgrade**
    ```

3. When the installer completes, **do not** reboot or
   restart! Run these two commands first:

```
[elemental@hostname ~]$ **sudo yum versionlock delete device-mapper\***
```

```
[elemental@hostname ~]$ **sudo yum install lvm2**
```

If you don't run these commands before rebooting, the node will boot into
emergency mode and you might lose data. 4. Restart the node with the following command:

```
[elemental@hostname ~] **sudo reboot**
```

On the Conductor Live web interface, a message appears to indicate that the node is
deactivated (offline). 5. When the node has rebooted, the Conductor Live web interface displays a message to indicate
that the node is back online. Refresh your web browser on the Elemental Live node to load the
updated web interface. 6. Repeat the downgrade steps on each worker node before moving on to the next step in
the downgrade process.
