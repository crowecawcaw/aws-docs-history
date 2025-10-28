# Extend your workspace with plugins

_Grafana plugins_ add the ability to connect to new data sources, or
add visualization or other functionality to the workspace. Broadly, plugins have three
types:

- **Panel plugins** – Panel plugins add new
  visualization types that are available for use in your dashboards. These define
  the rendering of the data in the frontend.
- **Data source plugins** – Data source
  plugins communicate with external sources of data, and
  return the data in a format that Grafana can use.
- **App plugins** – Applications, also known as
  app plugins. These include bundle data sources and panels, and can provide a
  cohesive experience within your Grafana workspace.

###### Note

When Amazon determines that a plugin is often failing or hasn't been maintained, it might
remove the plugin from the list of available plugins in the console.

For Amazon Managed Grafana workspaces that support version 9 or newer, you can enable plugin
management. This allows workspace admins to install or uninstall plugins from the
_plugin catalog_.

## Find plugins with the plugin catalog

Your Amazon Managed Grafana workspace includes a page that shows all of your installed plugins and
a list of all plugins that are available to install in your workspace. This page is the
_plugin catalog_. In addition to the plugins that are
installed by default, you can install up to 50 more plugins.

The available plugins fall broadly into the following categories:

- **AWS Data Sources** – This is an
  application plugin, provided by Amazon Managed Grafana, to easily discover AWS
  resources in your account. This is installed by default. For more information,
  see [Use the AWS Data Sources plugin to find
  AWS data](aws-datasources-plugin.md "aws-datasources-plugin.md").
- **Core plugins** – These plugins
  are provided by default in Grafana. They include popular data sources
  and panel visualizations. They are tagged as
  **Core** in the plugin catalog. These are installed by
  default and cannot be removed.
- **Enterprise plugins** – These plugins
  are available to Grafana workspaces that have an enterprise license.
  These are not installed by default. They are tagged as
  **Enterprise** in the plugin catalog. They can only be
  installed if you have a valid enterprise license. For details about how to
  upgrade a workspace to an Enterprise license, see [Managing your access to Amazon Managed Grafana
  Enterprise plugins](AMG-workspace-manage-enterprise.md "AMG-workspace-manage-enterprise.md").
- **Community plugins** – These plugins
  are provided for Grafana workspaces from various sources,
  including Grafana Labs, AWS, and others. In
  Grafana workspaces that support version 9 or newer, these are not installed by
  default (earlier workspaces have some of these installed automatically). These
  are typically open source plugins. You can install or remove these
  plugins.

###### Note

Using community plugins is at your discretion. As part of the [shared responsibility model](security.md "security.md") between you and
AWS, you are expected to understand what you are installing into your
workspace for these third party plugins. You are also responsible for the
plugins meeting your security needs.

**Plugin support**

Plugins come from a wide variety of sources, and support varies for them.

- **AWS Data Sources plugin** – This
  plugin is provided by and supported by AWS.
- **Enterprise plugins** – The Enterprise
  plugins are supported by both AWS and Grafana Labs—you can submit issues
  through either support team.
- **Core plugins** – The core plugins and
  other plugins provided by AWS or Grafana Labs are supported in Amazon Managed Grafana by
  AWS. You can submit an issue in GitHub for bug-fixes or enhancements, or
  create a ticket with AWS or Grafana Labs.
- **Community plugins** – Community plugins
  not created by AWS or Grafana Labs are typically supported through GitHub
  issues or other forums. Support information in those cases is included in the
  details for the plugin in the plugin catalog.

You can also submit issues for plugins through the GitHub forums for [Amazon Managed Grafana](https://github.com/aws/amazon-managed-grafana-roadmap/issues "https://github.com/aws/amazon-managed-grafana-roadmap/issues")
or [Grafana](https://github.com/grafana/grafana/issues "https://github.com/grafana/grafana/issues").

**Plugin versions**

Most plugins are updated on a regular cadence. The plugin catalog in a Amazon Managed Grafana
workspace shows the most recent versions of a plugin, and you choose which version to
install. When a plugin has an outdated version with a known security issue,
the outdated version is removed from availability.

You can also [update](#update-plugin "#update-plugin") plugins that are already
installed.

###### Note

Sometimes, a new version of a plugin is made available that fixes a security
issue in an installed plugin. For severe issues, Amazon Managed Grafana might automatically
update the plugin in your workspaces to the version with the fix.

## Manage plugins with the plugin catalog

You manage the plugins for your Amazon Managed Grafana workspace from the plugin catalog. You
can only install plugins that are listed in the plugin catalog within your
workspace.

The following describes the prerequisites for using the plugin catalog, and how to
find the plugin catalog.

**Prerequisites**

- You must have an [Amazon Managed Grafana
  workspace](AMG-create-workspace.md "AMG-create-workspace.md") that supports version 9, and have an account that can log
  into that workspace.
- The workspace must have [plugin
  management enabled](AMG-configure-workspace.md "AMG-configure-workspace.md").
- Your user account must be an [admin for your
  Amazon Managed Grafana workspace](Grafana-user-roles.md "Grafana-user-roles.md").
- To install and use Enterprise plugins, you must first [upgrade to an Enterprise
  license](AMG-workspace-manage-enterprise.md "AMG-workspace-manage-enterprise.md").

###### To view the plugin catalog

1. Sign in to your Amazon Managed Grafana workspace.
2. From the left menu, choose **Administration**, then
   **Plugins**. This opens the plugin catalog.
3. By default, the plugin catalog lists the installed plugins. To view all
   available plugins, choose **All** under the
   **State** filter at the top of the catalog. Installed plugins
   include a tag that says **Installed**.

## Install or remove a plugin

###### Note

You must meet the prerequisites from the preceding section, or you will not
have permission to modify plugins.

###### To install or remove a Grafana plugin

1. Go to the plugin catalog.
2. By default, the plugin catalog lists the installed plugins only. To view all
   available plugins, choose **All** under the
   **State** filter at the top of the catalog. Installed plugins
   include a tag that says **Installed**.
3. Select the plugin to install or uninstall. For example, if you want to remove
   the _Datadog_ data source, select the
   **Datadog** plugin.
4. On the plugin details page, choose the uninstall or install option.
5. After a plugin is installed, it can take up to a few minutes before the
   change is synced across all parts of the workspace. It is good to wait a few
   minutes before using the new plugin.

###### Note

You can have 50 plugins installed in a workspace (beyond the default Core
plugins).

## Update a plugin

###### To update an existing Grafana plugin

1. Sign in to your Amazon Managed Grafana workspace.
2. From the left menu, choose **Administration**, then
   **Plugins**. This opens the plugin catalog,
   listing only the installed plugins.
3. Select the plugin to update.
4. On the plugin details page, check to see if there is an update available. If
   so, choose the option to update the plugin and choose the version to update
   to.

###### Note

If you see a note that you do not have permission to modify the plugin,
confirm that [plugin management is
enabled](AMG-configure-workspace.md "AMG-configure-workspace.md") for your workspace. You must also be an [admin](Grafana-user-roles.md "Grafana-user-roles.md") for the Amazon Managed Grafana
workspace.
