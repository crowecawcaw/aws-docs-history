This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Enable SSL

The Secure Socket Layer (SSL) enables the secure version of HTTP (HTTPS)
and encrypts
communications between the client and server. Note the following about SSL:

- With SSL, all traffic over the communications layer must use a secure
  protocol. If SSL is disabled, all traffic must use the unsecured version. Traffic
  that uses the wrong protocol fails.
- When SSL is enabled, you must continue to use the `--https` flag with
  subsequent node reconfigurations through the command line interface. If you omit the flag,
  the installer disables SSL.

Use `--https` with the following commands:

    + The run command, such as **sudo sh
     ./`product_installer_name`\_`version``.run`**
    + The configure command, such as **sudo ./configure**

###### To enable SSL

Follow these steps for all nodes that will have SSL enabled.

1. At your workstation, start a remote terminal session to the AWS Elemental Statmux node.
2. At the Linux prompt, log-in with the _elemental_ user credentials.
3. Change to the directory where the configuration script is located, as shown here.

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
```

4. Run the configuration script, as shown here.

```
[elemental@hostname elemental_se]$ **sudo ./configure --https**
```

where `--https` enables SSL.

###### Note

If you run this command when SSL is already enabled, nothing changes in the configuration. SSL is still enabled. 5. At each configuration prompt, accept the suggestion. This way, you won't inadvertently change other aspects of the configuration.
