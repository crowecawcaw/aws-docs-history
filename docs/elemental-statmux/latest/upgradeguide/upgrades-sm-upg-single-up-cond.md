This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Step D: Upgrade the Node

The upgrade steps that you take depend on the version that you're upgrading to. The
following section describes upgrading to 2.20.x.

These steps must be performed on the AWS Elemental Statmux hardware unit.

1.  From a Linux prompt, log in with the _elemental_ user credentials. Once
    you're logged in, the initial directory is `/home/elemental`.
2.  Run the installer with the skip-all option:

        * For GPU and CPU versions of the software.



        ```
        [elemental@hostname ~]$ **sudo sh ./elemental\_production\_statmux\_2.20.n.nnnnn.run --skip-all --start**
        ```
        * For CPU-only versions of the software.



        ```
        [elemental@hostname ~]$ **sudo sh ./elemental\_production\_statmux\_cpu\_2.20.n.nnnnn.run --skip-all --start**
        ```

    The installer automatically stops the software, if it's still running. The following
    prompts are skipped:

        * You are not prompted to change the network setup (eth0 and eth1) or the
         Ethernet partitioning (setup of eth0 as a management interface).
        * You are not prompted to choose the time zone.
        * You are not prompted to enable or disable user authentication.

    You _are_ prompted to accept the EULA (end user license agreement).

The new software is installed and all services except `elemental_se` are
automatically be restarted. 3. Once installation is complete, you might be prompted to reboot.

```
Installation and configuration complete!
.
.
.
NOTE: You must reboot your system to finish the installation!
```

Enter this command to reboot:

```
`[elemental@hostname ~]$` **sudo reboot**
```

The reboot takes approximately 5 minutes. When the reboot completes, the elemental \_se service automatically starts. Look
for this message on the command line:

```
Starting elemental_se: [ OK ]
```

4. If you're not prompted to reboot, you are prompted to start elemental_se:

```
Would you like to start the Elemental service now? [Y]
```

Enter
`Y`.

The restart takes approximately 1 minute. When the restart is done, this message appears:

```
Installation and configuration complete!
Please open a web browser and point it to http://xxx.xxx.xxx.xxx to get to the web interface.
Enjoy!
```

5. Refresh your web browser to load the updated AWS Elemental Statmux web interface.
