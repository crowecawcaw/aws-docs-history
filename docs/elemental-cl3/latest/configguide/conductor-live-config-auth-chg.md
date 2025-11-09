# Disabling user authentication

This section describes how to disable user authentication on the cluster.

###### To disable user authentication

You disable user authentication by running the configuration script in the same way as
you ran it to enable user authentication. In other words, if authentication is enabled and
you include `--config-auth`, then the script disables authentication.

1. [Check if HA redundancy](config-conductor-live-ha-current-state.md "config-conductor-live-ha-current-state.md")
   is currently enabled on the Conductor Live. If it is, [disable it](conductor-live-config-ha-chg.md "conductor-live-config-ha-chg.md") now[Disabling Conductor Live HA
   (high availability)](conductor-live-config-ha-chg.md "conductor-live-config-ha-chg.md").
2. At your workstation, [start a remote
   terminal session](ready-conductor-live-config-access.md "ready-conductor-live-config-access.md") to the primary Conductor Live node.
3. At the Linux prompt, log in with the _elemental_ user
   credentials.
4. Change to the directory where the configuration script is located, then enter the
   configure command :

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
[elemental@hostname elemental_se]$ sudo ./configure --config-auth
```

5. Answer the prompts as follows:

| Prompt                                                                        | Value to enter |
| ----------------------------------------------------------------------------- | -------------- |
| `Httpd must be restarted, which may interrupt REST commands. Restart<br>now?` | `Y`            |
| `Do you wish to update the admin user?`                                       | `N`            |

When you return to the web interface, you are not prompted to log in, and the menu to
enable or disable node authentication on the worker nodes has disappeared. 6. The `configure` command in the previous step disables user authentication
but leaves HTTPS enabled. Therefore, if you also want to disable HTTPS, enter the
configure command as follows:

```
[elemental@hostname elemental_se]$ sudo ./configure --https --skip-all
```

7. If applicable, [re-enable HA](conductor-live-config-ha.md "conductor-live-config-ha.md").
