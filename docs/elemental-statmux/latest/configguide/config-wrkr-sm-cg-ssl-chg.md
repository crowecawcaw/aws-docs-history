This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Disable SSL

This section describes how to disable HTTPs (SSL) access to the node. For assistance
enabling, see [Enable SSL](config-wrkr-sm-cg-ssl.md "config-wrkr-sm-cg-ssl.md").

To disable SSL, run the configure command without the `--https` flag.

1. At your workstation, start a remote terminal session to the AWS Elemental Statmux node.
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
