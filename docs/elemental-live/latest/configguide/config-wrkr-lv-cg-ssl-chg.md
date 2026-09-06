

# Disable HTTPS
<a name="config-wrkr-lv-cg-ssl-chg"></a>

. Read this section only if you are using Elemental Live version 2.25 or earlier. With these versions, you must explicitly enable HTTPS, if you want users or applications to have a secure connection to Elemental Live.

(With Elemental Live version 2.26 and later, HTTPS is enabled by default. Furthermore, you can't disable HTTPS.)

For information about how to enable HTTPS, see [Enable HTTPS](config-wrkr-lv-cg-ssl.md).

**Note**  
This information applies only to Elemental Live 2.25 and earlier.

To disable HTTPS, run the `configure` command without the `--https` flag.

1. At your workstation, start a remote terminal session to the primary AWS Elemental Conductor Live node.

1. At the Linux prompt, log-in with the *elemental* user credentials.

1. Change to the directory where the configuration script is located, as shown here.

   ```
   [elemental@hostname ~]$ cd /opt/elemental_se
   ```

1. Run the configuration script, as shown here.

   ```
   [elemental@hostname elemental_se]$ sudo ./configure --skip-all 
   ```

   The `skip--all` option means that the script disables HTTPS but doesn't change the configuration in any other way.
**Note**  
If you run this command when HTTPS is already disabled, nothing changes in the configuration. HTTPS is still disabled.