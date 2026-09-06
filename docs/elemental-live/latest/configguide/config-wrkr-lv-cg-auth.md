

# Enable user authentication
<a name="config-wrkr-lv-cg-auth"></a>

You can require users to provide valid credentials when they access Elemental Live from both the web interface and REST API.
+ For the web interface, users must complete the fields on the login screen.
+ For the REST API, users must include these additional HTTP headers in commands that they send:
  + `X-Auth-User`
  + `X-Auth-Expires`
  + `X-Auth-Key`

  For more information about using the API with authentication enabled, see the Elemental Live REST API documentation.

**To enable user authentication**

1. Disable Conductor redundancy, if applicable. For help, see [the section about disabling redundancy in](https://docs.aws.amazon.com/elemental-conductor/latest/configguide/conductor-live-config-ha-chg.html) the AWS Elemental Conductor Live Configuration Guide.

1. At your workstation, start a remote terminal session to the primary Elemental Live node.

1. At the Linux prompt, log in with the *elemental* user credentials.

1. Change to the directory where the configuration script is located, as shown here.

   ```
   [elemental@hostname ~]$ cd /opt/elemental_se
   ```

1. Run the configuration script, as shown here.

   ```
   [elemental@hostname elemental_se]$ sudo ./configure --config-auth {{--https}}
   ```

   Complete {{`--https`}} as follows:
   + If you are using Elemental Live 2.25 or earlier, and if you enabled SSL when you configured the node\*x\*, enter `HTTPS`. If you omit this flag, the script disables SSL.
   + If you are using Elemental Live 2.26 or later, there is no need to enter this option. SSL is enabled by default in these versions.

1. For the prompt `Do you wish to enable authentication?`, type **Y**.

1. For the prompt `Do you wish to enable PAM?`, type **N**. If you're using PAM authentication, type **Y**.

   For information about the different authentication options, see [User authentication reference](config-wrkr-lv-cg-auth-ref.md). 

1. At the prompts, create an admin API user name, email address, and password.

   Note that the only time you log in with this information is upon initial access to each node's web interface after authentication is enabled. For more information about the administrator API user, see [Authentication user types](auth-ref-type-user.md).

1. For the prompt `Httpd must be restarted, which may interrupt REST commands. Restart now?`, type **Y**.

1. Create users through the node's web interface. For instructions, see [Add users](config-wrkr-lv-cg-users.md).