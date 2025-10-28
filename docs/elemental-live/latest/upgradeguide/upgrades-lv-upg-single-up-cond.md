# Step D: Upgrade the Elemental Live software

These steps must be performed on the Elemental Live hardware unit.

There are two procedures for upgrading a node. Choose the procedure that applies to your
deployment.

###### Topics

- [Upgrade without change](#upgrades-live-step-upgrade-no-change "#upgrades-live-step-upgrade-no-change")
- [Upgrade and change deployment](#upgrades-live-step-upgrade-change "#upgrades-live-step-upgrade-change")

## Upgrade without change

###### To upgrade a node without changing the deployment

Follow this procedure if you don't need to change anything about the deployment.

1.  From a Linux prompt, log in with the _elemental_ user
    credentials. Once you're logged in, the initial directory is
    `/home/elemental`.
2.  Run the installer with the skip-all option:

        * For GPU and CPU versions of the software.



        ```
        [elemental@hostname ~]$ **sudo sh ./elemental\_production\_live\_2.25.4.12345.run --skip-all --start**
        ```
        * For CPU-only versions of the software.



        ```
        [elemental@hostname ~]$ **sudo sh ./elemental\_production\_live\_cpu\_2.25.4.12345.run --skip-all --start**
        ```

    The installer automatically stops the software, if it's still running. The following
    prompts are skipped:

        * You are not prompted to change the network setup (eth0 and eth1) or the Ethernet
         partitioning (setup of eth0 as a management interface).
        * You are not prompted to choose the time zone.
        * You are not prompted to enable or disable user authentication.

    You _are_ prompted to accept the EULA (end user license
    agreement).

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

The reboot takes approximately 5 minutes. When the reboot completes, the elemental
\_se service automatically starts. Look for this message on the command line:

```
Starting elemental_se: [ OK ]
```

4. If you're not prompted to reboot, you are prompted to start elemental_se:

```
Would you like to start the Elemental service now? [Y]
```

Enter `Y`.

The restart takes approximately 1 minute. When the restart is done, this message
appears:

```
Installation and configuration complete!
Please open a web browser and point it to http://xxx.xxx.xxx.xxx to get to the web interface.
Enjoy!
```

5. Refresh your web browser to load the updated Elemental Live web interface.

## Upgrade and change deployment

###### To upgrade a node and change the deployment

Follow this procedure if you want to change something in the deployment. Specifically,
follow this procedure if you want to enable OCR conversion for the first time. This
feature is available in AWS Elemental Live version 2.22.0 and later. (For information about this
feature, see [Support for OCR Conversion](../ug/support-for-ocr.md "../ug/support-for-ocr.md")
in the _AWS Elemental Live User Guide_.)

1. Follow the appropriate procedure in the _AWS Elemental Live Installation
   Guide_:
   - [Install the
     AWS Elemental Live software](../installguide/install-lv-ig-install-sw.md "../installguide/install-lv-ig-install-sw.md"): to install on hardware
   - [Install
     the AWS Elemental Live software](../installguide/install-vm-lv-ig-install-sw.md "../installguide/install-vm-lv-ig-install-sw.md"): to install on a VM

2. Once installation is complete, you might be prompted to reboot.

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

The reboot takes approximately 5 minutes. When the reboot completes, the elemental
\_se service automatically starts. Look for this message on the command line:

```
Starting elemental_se: [ OK ]
```

3. If you're not prompted to reboot, you are prompted to start elemental_se:

```
Would you like to start the Elemental service now? [Y]
```

Enter `Y`.

The restart takes approximately 1 minute. When the restart is done, this message
appears:

```
Installation and configuration complete!
Please open a web browser and point it to http://xxx.xxx.xxx.xxx to get to the web interface.
Enjoy!
```

4. Refresh your web browser to load the updated Elemental Live web interface.
