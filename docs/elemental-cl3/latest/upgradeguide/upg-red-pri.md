# Step O: Upgrade the primary Conductor

node

###### Warning

Do not clear the database of the primary Conductor Live node when you
run the installer!

Perform these steps on the primary Conductor Live node.

###### To upgrade the primary node

1. From the Linux command line, log in to the worker node.
   Use the _elemental_ user
   credentials.
2. Run the installer. _Do not_ include the `-c` option to clear the database. Use this command:

```
[elemental@hostname ~]$ **sudo sh ./elemental\_production\_conductor\_live247\_3.25.5.12345 --skip-all --start -xeula**
```

The installer automatically stops the software. You will
not be prompted to do the following:

    * Change the network setup (eth0 and eth1) or the
     Ethernet partitioning (setup of eth0 as a management
     interface).
    * Choose the timezone.
    * Enable or disable user authentication.

3. Make sure that the elemental_se service restarts. Look for
   this prompt on the primary Conductor Live command line:

```
Starting elemental_se:            [OK]
```

4. If you copied a script to a safe location (as described in
   [Move custom files](upgrades-cl3-upg-red-single-ver-version.md#upg-red-move "upgrades-cl3-upg-red-single-ver-version.md#upg-red-move")), copy it back to its location in
   `/opt/elemental_se/scripts`.
