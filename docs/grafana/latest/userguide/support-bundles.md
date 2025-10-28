# Gather information for support

Support bundles provide a simple way to collect information about your Grafana workspace
through the user interface. When you encounter problems with your Grafana workspace, you
can send product support a support bundle that contains information about your workspace,
including:

- Grafana version
- Installed plugins
- Grafana configuration
- Database information and migrations

###### Note

Support bundles are only available in workspaces compatible with Grafana version 10
or newer.

## Support bundle components

A support bundle can include any of the following components:

- **Usage statistics** – Usage statistics
  for the Grafana workspace.
- **User information** – A list of users of
  the Grafana workspace.
- **Database and migration information** –
  Database information, and migration log.
- **Plugin information** – Information
  about installed plugins in the workspace.
- **Basic information** – Basic information
  about the Grafana workspace, including version, and memory usage.
- **Settings** – The settings of the
  Grafana workspace.
- **SAML** – Healthcheck connection and
  metadata for SAML (only displayed if SAML is enabled).
- **LDAP** – Healthcheck connection and
  metadata for LDAP (only displayed if LDAP is enabled).
- **OAuth2** – Healthcheck connection and
  metadata for each OAuth2 provider (only displayed if OAuth provider is
  enabled).

## Creating a support bundle

Use the following procedure to create a support bundle.

###### Note

This procedure requires `admin` permissions in the workspace.

###### To create a support bundle

1. Sign into your Grafana workspace.
2. Select the Help icon
3. From the help menu, choose **Support Bundles**.
4. Select **New Support Bundle**.
5. Choose the components that you want to include in the support bundle.
6. Select **Create**.
7. After the support bundle is ready, select **Download**.

Grafana downloads the support bundle to an archive (`tar.gz`)
file.

You can open the file to view the contents of the support bundle. You can directly
send the file to support, if needed. If the bundle contains private information, and
you must send it via a channel that is not private, you may consider encrypting it. You
can use a tool like [age](https://age-encryption.org/ "https://age-encryption.org/") to encrypt the
file before sending.
