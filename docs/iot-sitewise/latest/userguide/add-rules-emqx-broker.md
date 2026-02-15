# Add authorization rules through the

EMQX Dashboard for users

You can add or update authorization rules using the EMQX Dashboard or the
AWS IoT SiteWise EMQX CLI tool. The AWS IoT SiteWise EMQX CLI tool manages authorization using
EMQX's built-in database.

###### Note

Adding authorization rules is an advanced configuration step that
requires understanding of MQTT topic patterns and access control. For
more information about creating authorization rules using EMQX's
built-in database, see [Use Built-in Database](https://docs.emqx.com/en/emqx/latest/access-control/authz/mnesia.html "https://docs.emqx.com/en/emqx/latest/access-control/authz/mnesia.html") in the _EMQX
Docs_.

###### Note

The EMQX-related instructions provided are for reference only. As EMQX
documentation and features may change over time, and we do not maintain
their documentation, we recommend consulting [EMQX's official
documentation](https://docs.emqx.com/en/emqx/latest/ "https://docs.emqx.com/en/emqx/latest/") for the most current information.

EMQX dashboard
This procedure shows how you can add authorization rules on
the EMQX dashboard.

The EMQX dashboard is only accessible from within the gateway
host. If you try to connect from outside of the gateway host,
you can't access the dashboard.

###### To add authorization rules using the EMQX

Dashboard

1. Ensure that you are within the gateway host.
2. Open a browser window and visit [`http://localhost:18083/`](http://localhost:18083/ "http://localhost:18083/").
3. Login to the the EMQX dashboard. This procedure
   assumes that you've changed your default login
   credentials to something of your choosing. For more
   information on intial setup, see [Enable username and
   password authentication](configure-emqx-broker.md#emqx-broker-username-password-auth "configure-emqx-broker.md#emqx-broker-username-password-auth").
4. Choose the shield icon, then
   **Authorization** from the dropdown
   menu.
5. Choose the **Permissions** button
   on the **Built-in Database** row.
6. In the Built-in Database authorization section, add or
   update the user authorization rules for your business
   needs. For more guidance on creating rules, see the
   [Use Built-in Database](https://docs.emqx.com/en/emqx/latest/access-control/authz/mnesia.html "https://docs.emqx.com/en/emqx/latest/access-control/authz/mnesia.html") section in the
   _EMQX Docs_.

AWS IoT SiteWise CLI tool using Linux

###### To manage authorization rules using the AWS IoT SiteWise EMQX CLI

tool in Linux:

- Add authorization rules for a user using the following
  format:

```
/greengrass/v2/bin/swe-emqx-cli auth add `your-username` `your-action` `your-permission` `your-topic` [`your-action-permission-topic`]
```

###### Example Add authorization rules for a user

This example shows how to add rules for a user named
`system1`:

```
/greengrass/v2/bin/swe-emqx-cli auth add system1 \
    publish allow "sensors/#" \
    subscribe allow "control/#" \
    all deny "#"
```

###### Example: View authorization rules for a user

To view authorization rules for the `system1`
users, run the following command:

```
/greengrass/v2/bin/swe-emqx-cli auth list system1
```

###### Example: View all existing authorization rules

To view all of the authorization rules you currently have,
run the following command:

```
/greengrass/v2/bin/swe-emqx-cli auth list
```

###### Example: Delete all authorization rules for a user

To delete all of the authorization rules applied to a
particular user, run the following command:

```
/greengrass/v2/bin/swe-emqx-cli auth delete system1
```

You are prompted to confirm the deletion.

AWS IoT SiteWise CLI tool using Windows

###### To manage authorization rules using the AWS IoT SiteWise EMQX CLI

tool in Windows PowerShell:

- Add authorization rules for a user using the following
  format:

```
C:\greengrass\v2\bin\swe-emqx-cli.ps1 auth add `your-username` `your-action` `your-permission` `your-topic` [`your-action-permission-topic`]
```

###### Example: Add authorization rules for a user

This example shows how to add rules for a user named
`system1`:

```
C:\greengrass\v2\bin\swe-emqx-cli.ps1 auth add system1 `
    publish allow "sensors/#" `
    subscribe allow "control/#" `
    all deny "#"
```

###### Example: View authorization rules for a user

To view authorization rules for the `system1`
users, run the following command:

```
C:\greengrass\v2\bin\swe-emqx-cli.ps1 auth list system1
```

###### Example: View all existing authorization rules

To view all of the authorization rules you currently have,
run the following command:

```
C:\greengrass\v2\bin\swe-emqx-cli.ps1 auth list
```

###### Example: Delete all authorization rules for a user

To delete all of the authorization rules applied to a
particular user, run the following command:

```
C:\greengrass\v2\bin\swe-emqx-cli.ps1 auth delete system1
```

You are prompted to confirm the deletion.
