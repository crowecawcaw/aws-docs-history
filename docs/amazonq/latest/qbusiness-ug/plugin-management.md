# Managing Amazon Q Business plugins

To manage Amazon Q plugins, you can take the following actions:

###### Actions

- [Updating a plugin](#plugin-update "#plugin-update")
- [Deleting a plugin](#plugin-delete "#plugin-delete")
- [Getting plugin properties](#plugin-properties "#plugin-properties")
- [Listing plugins](#plugin-list "#plugin-list")
- [Listing configured plugin actions](#plugin-list-actions "#plugin-list-actions")
- [Listing available plugin actions](#plugin-list-actions-type "#plugin-list-actions-type")
- [Listing plugin metadata](#plugin-list-metadata "#plugin-list-metadata")

## Updating a plugin

To update a plugin, you can use AWS Management Console or the [UpdatePlugin](../api-reference/API_UpdatePlugin.md "../api-reference/API_UpdatePlugin.md") API operation. The following tabs provide a
procedure for the console and code examples for the AWS CLI.

Console
**To update a plugin**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. For **Plugins**, select the plugin that you want
   to update, and then choose **Actions**.
5. For **Actions**, choose
   **Edit**.

On the plugins configuration page, you can edit your
settings.

**To deactivate a plugin**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. For **Plugins**, select the plugin that you want
   to deactivate, and then choose **Actions**.
5. For **Actions**, choose
   **Deactivate**.

Your plugin will be deactivated. After your plugin is deactivated,
its status will change to **Inactive**.

**To reactivate a plugin**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. For **Plugins**, select the plugin that you want
   to reactivate, and then choose **Actions**.
5. For **Actions**, choose
   **Reactivate**.

Your plugin will be activated. After your plugin is reactivated,
its status will change to **Active**.

AWS CLI
**To edit a plugin**

```

aws qbusiness update-plugin \
--application-id `application-id` \
--plugin-id `plugin-id` \
--display-name `display-name` \
--server-url `https://example.atlassian.net` \
--auth-configuration basicAuthConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>}`"
```

**To disable a plugin**

```

aws qbusiness update-plugin \
--application-id `application-id` \
--plugin-id `plugin-id` \
--state DISABLED
```

**To enable a plugin**

```

aws qbusiness update-plugin \
--application-id `application-id` \
--plugin-id `plugin-id` \
--state ENABLED
```

## Deleting a plugin

To delete a plugin, you can use the AWS Management Console or the [DeletePlugin](../api-reference/API_DeletePlugin.md "../api-reference/API_DeletePlugin.md") API operation. The following tabs provide a
procedure for the console and code examples for the AWS CLI.

Console
**To delete a plugin**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. For **Plugins**, select the plugin that you want
   to delete, and then choose **Actions**.
5. For **Actions**, choose
   **Delete**.
6. In the dialog box, type `delete` to confirm
   your action.

The console displays a successful deletion message when the plugin
deletion process is finished.

AWS CLI
**To delete a plugin**

```

aws qbusiness delete-plugin \
--application-id `application-id` \
--plugin-id `plugin-id`
```

## Getting plugin properties

To get the details of an Amazon Q plugin, you can use either the AWS Management Console
or the [GetPlugin](../api-reference/API_GetPlugin.md "../api-reference/API_GetPlugin.md") API operation. The following tabs provide a
procedure for the console and code examples for the AWS CLI.

Console
**To get plugin details**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. For **Plugins**, select the configured plugin
   that you want to see details for.
5. On the **Plugin settings** page, the following
   details are available:
   - **Name** – The name of your
     plugin.
   - **Type** – The type of your
     plugin.
   - **AWS Secrets Manager** – The
     Secrets Manager secret.
   - **Creation time** – The time stamp
     for when your plugin was created.
   - **Plugin ID** – The ID that's
     assigned to your plugin.

AWS CLI
**To get plugin details**

```

aws qbusiness get-plugin \
--application-id `application-id` \
--plugin-id `plugin-id`
```

## Listing plugins

To list Amazon Q plugins, you can use the AWS Management Console or the [ListPlugins](../api-reference/API_ListPlugins.md "../api-reference/API_ListPlugins.md") API operation. The following tabs provide a
procedure for the console and code examples for the AWS CLI.

Console
**To list plugins**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. In **Plugins**, a list of plugins that are
   attached to your application is available.

AWS CLI
**To list plugins**

```

aws qbusiness list-plugins \
--application-id `application-id`
```

## Listing configured plugin actions

To list actions configured for a specific Amazon Q plugin, you can use the
AWS Management Console or the [ListPluginActions](../api-reference/API_ListPluginActions.md "../api-reference/API_ListPluginActions.md") API operation. The
following tabs provide a procedure for the console and code examples for the
AWS CLI.

Console
**To list specific actions configured for a
plugin**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. In **Plugins**, select your plugin from the list
   of plugins configured for your application.
5. On the plugin summary page, you'll find the actions supported by
   your plugin under **Actions supported**.

AWS CLI
**To list specific actions configured for a
plugin**

```

aws qbusiness list-plugin-actions \
--application-id `application-id` \
--plugin-id `plugin-id`
```

## Listing available plugin actions

To list all available actions for a specific Amazon Q plugin, you can use
the AWS Management Console or the [ListPluginTypeActions](../api-reference/API_ListPluginTypeActions.md "../api-reference/API_ListPluginTypeActions.md") API operation. The
following tabs provide a procedure for the console and code examples for the
AWS CLI.

Console
**To list all available actions for a specific
plugin**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. On the **Plugins** page, under each plugin type,
   you'll find all the plugins actions supported by Amazon Q Business.

AWS CLI
**To list all available actions for a specific
plugin**

```

aws qbusiness list-plugin-type-actions \
--plugin-type `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | QUICKSIGHT | SERVICENOW_NOW_PLATFORM | JIRA_CLOUD | SALESFORCE_CRM | ZENDESK_SUITE | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | MICROSOFT_TEAMS | MICROSOFT_EXCHANGE | PAGERDUTY_ADVANCE | SMARTSHEET | ASANA`
```

## Listing plugin metadata

To list metadata for a specific Amazon Q plugin, you can use the AWS Management Console
or the [ListPluginTypeMetadata](../api-reference/API_ListPluginTypeMetadata.md "../api-reference/API_ListPluginTypeMetadata.md") API operation.
The following tabs provide a procedure for the console and code examples for the
AWS CLI.

Console
**To list metadata for a specific plugin**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. On the **Plugins** page, under each plugin type,
   you'll find all the plugin metadata (category, description, and
   type) supported by Amazon Q Business.

AWS CLI
**To list metadata for a specific plugin**

```

aws qbusiness list-plugin-type-metadata
```
