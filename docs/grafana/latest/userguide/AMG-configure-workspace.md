# Configure a Amazon Managed Grafana workspace

Amazon Managed Grafana configuration can be separated into configuration of the Amazon Managed Grafana
authentication and permissions, and configuration of the Grafana workspace. This section
includes information regarding configuration of your Grafana workspace.

For more information about configuring Amazon Managed Grafana authentication and permissions, see
the following topics.

- [Authenticate users in Amazon Managed Grafana
  workspaces](authentication-in-AMG.md "authentication-in-AMG.md")
- [Manage user and group access to
  Amazon Managed Grafana workspaces](AMG-manage-users-and-groups-AMG.md "AMG-manage-users-and-groups-AMG.md")
- [Users, teams, and permissions](Grafana-administration-authorization.md "Grafana-administration-authorization.md")
  You can modify the configuration of your Grafana workspace within Amazon Managed Grafana on the
  **Workspace configuration options** tab when viewing the properties
  of your workspace.

Making configuration changes to your Grafana instance can cause the instance to
restart to reload the new settings. After configuration changes are made, your users
might need to refresh any browser pages that show the Grafana workspace.

###### Note

The same options are available to you when you first create your workspace.

###### To change the configuration of a Grafana workspace using the Amazon Managed Grafana

console

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
2. In the left navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the name of the workspace that you want to configure. This opens the
   details for that workspace.
5. Choose the **Workspace configuration options** tab to see the
   instance configuration options for your instance.
6. Select **Edit** next to either **Grafana
   alerting** or **Plugin management**.
   - **Grafana alerting**

   You can enable [Grafana alerting](v10-alerts.md "v10-alerts.md"). To
   view Prometheus alerts in your Grafana workspace, select the check box
   to **Turn Grafana alerting on**. In workspaces running
   version 8 or 9, this will send multiple notifications for your Grafana
   alerts. If you use alerts defined in Grafana, we recommend updating your
   workspace to version 10.4 or later.

   If you want to the classic Grafana alerts instead,
   _clear_ the check box next to **Turn
   Grafana alerting on**. This turns on the [classic dashboard alerts](old-alerts-overview.md "old-alerts-overview.md"). Even
   if you don't turn Grafana alerting on, your existing Grafana alerts are
   evaluated.

   ###### Note

   Classic dashboard alerts will be removed in version 11. In Grafana
   version 10 workspaces, you can preview the Grafana alerting feature.
   For more information, see [Migrating classic dashboard alerts to Grafana
   alerting](v10-alerting-use-grafana-alerts.md "v10-alerting-use-grafana-alerts.md").
   - **Plugin management**

   To turn on plugin management, select the check box to **Turn
   plugin management on**. Turning plugin management on allows
   admins in your Amazon Managed Grafana workspace to install, update, or remove [plugins](grafana-plugins.md "grafana-plugins.md") using the Grafana plugin
   catalog. This option is only available for workspaces that support
   Grafana version 9 or newer.

###### Note

If you turn _off_ Grafana alerting, you lose all changes made
to the alerting configuration while Grafana alerting was on. This includes any new
alert rules that you created.

For more information about using Grafana alerting, and the effects of turning it
on or off, see [Alerts in Grafana version 10](v10-alerts.md "v10-alerts.md").

The next section shows how to make changes to the Grafana instance configuration using
the Amazon Managed Grafana API or the AWS CLI.

## Setting configuration with API or

AWS CLI

You can set the Grafana workspace configuration using the Amazon Managed Grafana API or the
AWS CLI.

###### Note

The `configuration` is a JSON string to allow for future
configuration settings which made be added later.

AWS CLI

###### To update Amazon Managed Grafana instance configuration using the

AWS CLI

Run the following command to turn on the Grafana alerting and
plugin management features for an instance. Replace the
`<region>` and
`<workspace-id>` strings with
appropriate values for your instance.

```
aws grafana update-workspace-configuration \
    --region `region` \
    --workspace-id `<workspace-id>` \
    --configuration '{"plugins": {"pluginAdminEnabled": true}, "unifiedAlerting": {"enabled": true}}'
```

The configuration currently supports the following options. These turn
Grafana alerting or plugin management on or off.

- To enable Grafana alerting, use this configuration
  option:

```
--configuration '{"unifiedAlerting": { "enabled": true }}'
```

- To enable plugin management, use this configuration
  option:

```
--configuration '{"plugins": {"pluginAdminEnabled": true }}'
```

This option is only available in workspaces that support
Grafana version 9 or newer.

Amazon Managed Grafana API

###### To update Amazon Managed Grafana instance configuration using the API

Use the following action to turn on the Grafana alerting and
plugin management features for an instance. Replace the
`<workspace-id>` string with an
appropriate value for your instance.

```
PUT /workspaces/`<workspace-id>`/configuration HTTP/1.1
Content-type: application/json

{
   "configuration": "{ \"unifiedAlerting\": { \"enabled\": true }, \"plugins\": { \"pluginAdminEnabled\": true }}"
}
```

The configuration currently supports the following options. These turn
Grafana alerting or plugin management on or off.

- To enable Grafana alerting, use this configuration
  option:

```
"configuration": "{\"unifiedAlerting\": { \"enabled\": true }}"
```

- To enable plugin management, use this option:

```
"plugins": "{\"pluginAdminEnabled\": true }"
```

This option is only available in workspaces that support
Grafana version 9 or newer.
