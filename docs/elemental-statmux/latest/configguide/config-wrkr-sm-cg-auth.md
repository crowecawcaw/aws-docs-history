This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Enable User Authentication

You can require users to provide valid credentials when they access AWS Elemental Statmux from both the web interface and REST API.

- For the web interface, users must complete the fields on the login screen.
- For the REST API, users must include these additional HTTP headers in commands that they send:

      + `X-Auth-User`
      + `X-Auth-Expires`
      + `X-Auth-Key`

  For more information about using the API with authentication enabled, see the
  AWS Elemental Statmux REST API documentation.

###### To enable user authentication

1. At your workstation, start a remote terminal session to the AWS Elemental Statmux node.
2. At the Linux prompt, log in with the _elemental_ user credentials.
3. Change to the directory where the configuration script is located, as shown here.

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
```

4. Run the configuration script, as shown here.

```
[elemental@hostname elemental_se]$ **sudo ./configure --config-auth**
```

###### Important

If you have SSL enabled, you must also include the `--https` flag in the
command. Otherwise, the script will disable SSL. 5. For the prompt `Do you wish to enable authentication?`, type
`Y`. 6. If you didn't use the `--https` flag in the configure command, the following prompt appears.

```
If you wish to enable authentication, please re-run with the ‘--https’ option.
If SSL isn’t enabled, any usernames/passwords entered here including LDAP passwords would be transmitted in plain text without encryption. This poses a significant security risk.
Accept the risk and continue without SSL?
```

If you intended to enable authentication without SSL enabled, enter `Y` to proceed.
Otherwise, enter `N` to re-enter the configuration script with `--https`. 7. For the prompt `Do you wish to enable PAM?`, type `N`. If you're using PAM authentication, type `Y`.

For information about the different authentication options, see [User Authentication Reference](config-wrkr-sm-cg-auth-ref.md "config-wrkr-sm-cg-auth-ref.md") 8. At the prompts, create an admin API user name, email address, and password.

Note that the only time you log in with this information is upon initial access
to each node's web interface after authentication is enabled. For more information about the
administrator API user, see [Authentication User Types](auth-ref-type-user.md "auth-ref-type-user.md") 9. For the prompt `Httpd must be restarted, which may interrupt REST
 commands. Restart now?`, type `Y`. 10. Create users through the node's web interface. For instructions, see [Add Users](config-wrkr-sm-cg-users.md "config-wrkr-sm-cg-users.md").
