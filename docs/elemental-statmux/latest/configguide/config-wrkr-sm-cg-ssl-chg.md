

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Disable SSL
<a name="config-wrkr-sm-cg-ssl-chg"></a>

This section describes how to disable HTTPs (SSL) access to the node. For assistance enabling, see [Enable SSL](config-wrkr-sm-cg-ssl.md).

To disable SSL, run the configure command without the `--https` flag.

1. At your workstation, start a remote terminal session to the AWS Elemental Statmux node.

1. At the Linux prompt, log-in with the *elemental* user credentials.

1. Change to the directory where the configuration script is located, as shown here.

   ```
   [elemental@hostname ~]$ cd /opt/elemental_se
   ```

1. Run the configuration script, as shown here.

   ```
   [elemental@hostname elemental_se]$ sudo ./configure 
   ```
**Note**  
If you run this command when SSL is already disabled, nothing changes in the configuration. SSL is still disabled.

1. At each configuration prompt, accept the suggestion. This way, you won't inadvertently change other aspects of the configuration.