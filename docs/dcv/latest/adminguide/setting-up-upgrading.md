# Upgrading the Amazon DCV Server

The following topic describes how to upgrade the Amazon DCV server.

###### Contents

- [Compatibility considerations](#compatibility-considerations "#compatibility-considerations")
- [Upgrading the Amazon DCV Server on Windows](#upgrading-windows-upgrade "#upgrading-windows-upgrade")
- [Upgrading the Amazon DCV Server on Linux](#upgrading-linux "#upgrading-linux")
- [Upgrading the Amazon DCV Server on macOS](#upgrading-macos "#upgrading-macos")

## Compatibility considerations

Amazon DCV server versions 2017 and later are compatible with Amazon DCV client versions 2017 and later.

###### Note

For information about the Amazon DCV server licensing compatibility requirements for on-premises and non
EC2-based servers, see [Licensing requirements](setting-up-license.md#licensing-requirements "setting-up-license.md#licensing-requirements").

## Upgrading the Amazon DCV Server on Windows

###### To upgrade the Amazon DCV server on Windows

1. Using an RDP client, connect to the Amazon DCV server as the administrator.
2. Ensure that there are no running Amazon DCV sessions. Use the `dcv
list-sessions` Amazon DCV command to check for any running sessions. If
   there are running sessions, use the `dcv close-session` Amazon DCV
   command to stop them.
3. After you confirm that there are no running sessions, stop the Amazon DCV server. For more
   information, see [Stopping the Amazon DCV Server](manage-stop.md "manage-stop.md").
4. Back up your Amazon DCV server configuration. Open the Registry Editor, navigate to
   **HKEY_USERS/S-1-5-18/Software/GSettings/com/nicesoftware/dcv**,
   right-click the **dcv** key, and choose
   **Export**.
5. Download the latest version of the Amazon DCV Server from the [NICE](http://download.amazondcv.com "http://download.amazondcv.com") website.
6. Follow the steps described in [Using the wizard](setting-up-installing-wininstall.md#setting-up-installing-windows-wizard "setting-up-installing-wininstall.md#setting-up-installing-windows-wizard"), starting at step
7.
8. After the installation is complete, confirm that the Amazon DCV server configuration is still
   correct. Open the Registry Editor, navigate to
   **HKEY_USERS/S-1-5-18/Software/GSettings/com/nicesoftware/dcv**
   and compare the parameters to the configuration that you exported in step
9.
10. Test the Amazon DCV server by starting a new Amazon DCV session. For more information, see
    [Starting Amazon DCV sessions](managing-sessions-start.md "managing-sessions-start.md").

## Upgrading the Amazon DCV Server on Linux

###### To upgrade the Amazon DCV server on Linux

1. Use SSH to sign in to the server using the `root` user.
2. Ensure that there are no running Amazon DCV sessions. Use the `dcv
list-sessions` Amazon DCV command to check for any running sessions. If
   there are running sessions, use the `dcv close-session` Amazon DCV
   command to stop them.
3. After you confirm that there are no running sessions, stop the Amazon DCV server. For more
   information, see [Stopping the Amazon DCV Server](manage-stop.md "manage-stop.md").
4. Back up your Amazon DCV server configuration. Copy the `/etc/dcv/dcv.conf`
   file to a safe location.
5. Follow the steps described in [Install the Amazon DCV Server](setting-up-installing-linux-server.md#linux-server-install "setting-up-installing-linux-server.md#linux-server-install").
6. After the installation is complete, confirm that the Amazon DCV server configuration is still
   correct. Open the file that you copied in step 4 and compare it to the
   `/etc/dcv/dcv.conf` file.
7. Test the Amazon DCV server by starting a new Amazon DCV session. For more information, see
   [Starting Amazon DCV sessions](managing-sessions-start.md "managing-sessions-start.md").

## Upgrading the Amazon DCV Server on macOS

###### To upgrade the Amazon DCV server on macOS

1. Use SSH to sign in to the server using user.
2. Ensure that there are no running Amazon DCV sessions. Use the `dcv
list-sessions` Amazon DCV command to check for any running sessions. If
   there are running sessions, use the `dcv close-session` Amazon DCV
   command to stop them.
3. After you confirm that there are no running sessions, stop the Amazon DCV server. For more
   information, see [Stopping the Amazon DCV Server](manage-stop.md "manage-stop.md").
4. Back up your Amazon DCV server configuration. Copy the `/etc/dcv/dcv.conf`
   file to a safe location.
5. Follow the steps described in [Installing the Amazon DCV Server on macOS](setting-up-installing-macos.md "setting-up-installing-macos.md").
6. After the installation is complete, confirm that the Amazon DCV server configuration is still
   correct. Open the file that you copied in step 4 and compare it to the
   `/etc/dcv/dcv.conf` file.
7. Test the Amazon DCV server by starting a new Amazon DCV session. For more information, see
   [Starting Amazon DCV sessions](managing-sessions-start.md "managing-sessions-start.md").
