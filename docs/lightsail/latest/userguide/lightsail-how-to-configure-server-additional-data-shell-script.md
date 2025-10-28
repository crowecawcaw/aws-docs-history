# Configure Linux/Unix instances with launch scripts in Lightsail

When you create a Linux or Unix-based instance, you can add a launch script to add or update
software, or configure your instance in some other way. To configure a Windows-based instance
with additional data, see [Configure your new Lightsail instance using Windows PowerShell](create-powershell-script-that-runs-when-you-create-windows-based-instance-in-lightsail.md "create-powershell-script-that-runs-when-you-create-windows-based-instance-in-lightsail.md").

###### Note

Depending on the machine image you choose, the command to get software on your instance
varies. Amazon Linux uses `yum`, while Debian and Ubuntu both use
`apt-get`. WordPress and other application images use `apt-get`
because they run Debian as their operating system. FreeBSD and openSUSE require additional
user configuration to use custom tools such as `freebsd-update` or
`zypper` (openSUSE).

## Example: Configure an

Ubuntu server to install Node.js

The following example updates the package list and then installs Node.js through the
`apt-get` command.

1. On the **Create an instance** page, choose
   **Ubuntu** on the **OS Only** tab.
2. Scroll down and choose **Add launch script**.
3. Type the following:

```
# update package list
apt-get update -y
# install some of my favorite tools
apt-get install nodejs -y
```

###### Note

Commands you send to configure your server are run as root, so you don't need to
include `sudo` before your commands. 4. Choose **Create instance**.

## Example: Configure a WordPress

server to download and install a plugin

The following example updates the package list, and then downloads and installs the
[BuddyPress plugin](https://wordpress.org/plugins/buddypress/ "https://wordpress.org/plugins/buddypress/") for
WordPress.

1. On the **Create an instance** page, choose
   **WordPress**.
2. Choose **Add launch script**.
3. Type the following:

```
# update package list
apt-get update
# download wordpress plugin
wget "https://downloads.wordpress.org/plugin/buddypress.14.0.0.zip"
apt-get install unzip
# unzip into wordpress plugin directory
unzip buddypress.14.0.0.zip -d /bitnami/wordpress/wp-content/plugins
```

4. Choose **Create instance**.
