This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Disable SSL

This section describes how to disable HTTPS (SSL) access to the node. If possible, we
recommend that you always keep HTTPS enabled.

To disable SSL, run the **Configure** command with the
`--http` flag.

1. At your workstation, start a remote terminal session to the AWS Elemental Server node.
2. At the Linux prompt, log-in with the _elemental_ user credentials.
3. Change to the directory where the configuration script is located, as shown here.

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
```

4. Run the configuration script, as shown here.

```
[elemental@hostname elemental_se]$ **sudo ./configure**
```

###### Note

If you run this command when SSL is already disabled, nothing changes in the configuration. SSL is still disabled. 5. At each configuration prompt, accept the suggestion. This way, you won't inadvertently change other aspects of the configuration.
