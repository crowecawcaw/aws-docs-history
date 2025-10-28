# Logging in to the File Gateway local console

When the VM is ready for you to log in, the login screen is displayed. If this is your first
time logging in to the VM local console, you use the temporary sign-in credentials to
log in. These temporary credentials give you access to menus where you can configure
gateway network settings and change the password from the local console. The initial
user name is `admin` and the temporary password is `password`. You
must change the password on first log in.

###### To change the temporary password

1. On the **AWS Appliance Activation - Configuration** main menu, enter the corresponding numeral for **Gateway Console**.
2. Run the `passwd` command. For information about how to run the command, see [Running Storage Gateway commands on the
   local console](MaintenanceGatewayConsole-fgw.md "MaintenanceGatewayConsole-fgw.md").

## Setting the local console password from the Storage Gateway console

You can also manage the local console's password from the Storage Gateway web-based console.
Any successful password updates made with the web-based console will override the
password used by the gateway VM's local console, including the temporary password if
you have never logged in locally. If the gateway is not currently reachable over the
network, the password update process will fail.

###### To set the local console password on the Storage Gateway console

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. On the navigation pane, choose **Gateways**, and then
   select the gateway for which you want to set a new password.
3. For **Actions**, choose **Set Local Console
   Password**.
4. In the **Set Local Console Password** dialog box, enter a
   new password, confirm the password, and then choose
   **Save**.

Your new password replaces the current password. The Storage Gateway service doesn't save,
store, or log the password but instead safely transmits it over an encrypted
channel to the VM, where it is securely stored.

###### Note

The password can consist of any character on the keyboard and can be
1–512 characters long.
