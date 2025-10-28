# Enable

HTTPS

.
Read this section only if
you are using Elemental Live version 2.25 or earlier. With these versions, you must explicitly enable
HTTPS if you want users or applications to have a secure connection to
Elemental Live.

(With
Elemental Live version 2.26 and later, HTTPS is enabled by default. There is no need to enable
it.)

Note the following about
HTTPS
when you use Elemental Live version 2.25 or earlier:

- With HTTPS, all traffic over the communications layer must use a secure protocol. If
  HTTPS is disabled, all traffic must use the unsecured version. Traffic that uses the wrong
  protocol fails.
- When HTTPS is enabled, you must continue to use the `--https` flag with
  subsequent node reconfigurations through the command line interface. If you omit the flag,
  the installer disables HTTPS.

Use `--https` with the following commands:

    + The run command, such as **sudo sh
     ./`product_installer_name`\_`version``.run`**
    + The configure command, such as **sudo ./configure**

###### Note

This information applies only to Elemental Live 2.25 and earlier.

###### To enable HTTPS

Follow these steps on each node.

1. At your workstation, start a remote terminal session to the AWS Elemental Conductor Live node.
2. At the Linux prompt, log-in with the _elemental_ user
   credentials.
3. Change to the directory where the configuration script is located, as shown here.

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
```

4. Run the configuration script, as shown here.

```
[elemental@hostname elemental_se]$ **sudo ./configure --https --skip-all**
```

The `skip--all` option means that the script enables HTTPS but doesn't change
the configuration in any other way.

###### Note

If you run this command when HTTPS is already enabled, nothing changes in the
configuration. HTTPS is still enabled.
