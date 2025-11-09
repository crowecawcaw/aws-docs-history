# Step 1: Enable

the
user authentication
feature

There are two steps to enabling user authentication in the cluster.

- The first step is to enable the _user authentication_ feature. You perform this step on the primary Conductor Live, by running the
  configuration script.
- The [second step](conductor-live-config-auth-wrkr.md "conductor-live-config-auth-wrkr.md") is to apply
  user authentication to all the nodes in the cluster. To perform this step, you enable
  _node authentication_ . You perform this step on the
  primary Conductor Live node, not on each worker node.
  This procedure applies to both types of user authentication—local authentication and PAM
  authentication.

**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.

| Node                          | Node where you perform this task |
| ----------------------------- | -------------------------------- |
| Primary Conductor Live node   | Yes                              |
| Secondary Conductor Live node | No                               |
| Each worker node              | No                               |

###### To enable user authentication

To enable user authentication, follow these steps.

1. If HA redundancy is currently enabled on the Conductor Live node, [disable it](conductor-live-config-ha-chg.md "conductor-live-config-ha-chg.md").
2. At your workstation, [start a remote
   terminal session](ready-conductor-live-config-access.md "ready-conductor-live-config-access.md") to the Conductor Live node.
3. Change to the directory where the configuration script is located, then enter the
   configure command to enable HTTPS:

```
[elemental@hostname ~]$ cd /opt/elemental_se
[elemental@hostname elemental_se]$ sudo ./configure --https --skip-all
```

The `--https` option enables HTTPS. When HTTPS is enabled, all user names
and passwords are encrypted.
When
you enable user authentication, you should always enable HTTPS. 4. Enter the configure command again to enable user authentication:

```
[elemental@hostname elemental_se]$ sudo ./configure --config-auth
```

###### Note

Enter the `configure` command twice, as shown. Don't enter a command that
combines the `--https` and `--config-auth` options because HTTPS
won't get enabled. 5. Answer the authentication prompts as follows:

| Prompt                                                                        | Value to enter                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Do you wish to enable authentication?`                                       | `Y`                                                                                                                                                                                                                                  |
| `Do you wish to enable PAM?`                                                  | `Y` to enable PAM<br>authentication`N` to enable local<br>authentication                                                                                                                                                             |
| `Enter admin login`                                                           | We recommend that you set up this default user as the API admin. Therefore,<br>don't accept the default. Instead, assign the name _apiadmin_.For information about this user, see [Types of users](users-types.md "users-types.md"). |
| `Enter admin email`                                                           | Enter an email address.                                                                                                                                                                                                              |
| `Enter admin password`:                                                       | Create a strong password for _apiadmin_.<br>The password must be strong: Minimum 8 characters, at least one uppercase<br>letter, at least one lowercase letter, at least one number, and at least one<br>symbol.                     |
| `Httpd must be restarted, which may interrupt REST commands. Restart<br>now?` | `Y`                                                                                                                                                                                                                                  |

6. After the configuration script has run, the following message appears. This message
   reminds you that users must include these additional HTTP headers in commands that they
   send.

`Authentication has been enabled. The REST interface will require authentication
 as well. Please look a the REST Interface section of the Support for more
 information.` 7. When the service starts and the Conductor node is ready, [re-enable HA](conductor-live-config-ha.md "conductor-live-config-ha.md"), if applicable. 8. Make a note of the user name and password for _apiadmin_.
**Result of this procedure**

You have enabled user authentication on the primary Conductor Live node. You have also created an
API admin (named _apiadmin_). This user has a specific role.
For more information, see [Types of users](users-types.md "users-types.md").
