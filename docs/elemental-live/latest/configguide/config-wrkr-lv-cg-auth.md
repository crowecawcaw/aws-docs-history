# Enable user authentication

You can require users to provide valid credentials when they access Elemental Live from both the web interface and REST API.

- For the web interface, users must complete the fields on the login screen.
- For the REST API, users must include these additional HTTP headers in commands that they send:

      + `X-Auth-User`
      + `X-Auth-Expires`
      + `X-Auth-Key`

  For more information about using the API with authentication enabled, see the
  Elemental Live REST API documentation.

###### To enable user authentication

1. Disable Conductor redundancy, if applicable. For help, see [the section
   about disabling redundancy in](../../../elemental-conductor/latest/configguide/conductor-live-config-ha-chg.md "../../../elemental-conductor/latest/configguide/conductor-live-config-ha-chg.md") the AWS Elemental Conductor Live Configuration Guide.
2. At your workstation, start a remote terminal session to the primary Elemental Live node.
3. At the Linux prompt, log in with the _elemental_ user
   credentials.
4. Change to the directory where the configuration script is located, as shown here.

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
```

5. Run the configuration script, as shown here.

```
[elemental@hostname elemental_se]$ **sudo ./configure --config-auth** `--https`
```

Complete `--https` as follows:

    * If you are using Elemental Live 2.25 or earlier, and if you enabled SSL when you configured
     the node\*x\*, enter `HTTPS`. If you omit this flag, the script disables
     SSL.
    * If you are using Elemental Live 2.26 or later, there is no need to enter this option. SSL is
     enabled by default in these versions.

6. For the prompt `Do you wish to enable authentication?`,
   type `Y`.
7. For the prompt `Do you wish to enable PAM?`, type
   `N`. If you're using PAM authentication, type
   `Y`.

For information about the different authentication options, see [User authentication
reference](config-wrkr-lv-cg-auth-ref.md "config-wrkr-lv-cg-auth-ref.md"). 8. At the prompts, create an admin API user name, email address, and password.

Note that the only time you log in with this information is upon initial access to each
node's web interface after authentication is enabled. For more information about the
administrator API user, see [Authentication user types](auth-ref-type-user.md "auth-ref-type-user.md"). 9. For the prompt `Httpd must be restarted, which may interrupt REST
 commands. Restart now?`, type `Y`. 10. Create users through the node's web interface. For instructions, see [Add users](config-wrkr-lv-cg-users.md "config-wrkr-lv-cg-users.md").
