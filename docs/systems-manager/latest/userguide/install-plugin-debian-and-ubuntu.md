

# Install the Session Manager plugin on Debian Server and Ubuntu Server
<a name="install-plugin-debian-and-ubuntu"></a>

1. Download the Session Manager plugin deb package.

------
#### [ x86\_64 ]

   ```
   curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb" -o "session-manager-plugin.deb"
   ```

------
#### [ ARM64 ]

   ```
   curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_arm64/session-manager-plugin.deb" -o "session-manager-plugin.deb"
   ```

------

1. Run the install command.

   ```
   sudo dpkg -i session-manager-plugin.deb
   ```

1. Verify that the installation was successful. For information, see [Verify the Session Manager plugin installation](install-plugin-verify.md).

**Note**  
If you ever want to uninstall the plugin, run `sudo dpkg -r session-manager-plugin`