# What third-party providers can I

create connections for?

Connections can associate your AWS resources with the following third-party
repositories:

- Azure DevOps
- Bitbucket Cloud
- GitHub.com
- GitHub Enterprise Cloud

###### Note

Currently, custom domains for GitHub Enterprise Cloud are not supported.

- GitHub Enterprise Server
- GitLab.com

###### Important

Connections support for GitLab includes version 15.x and later.

- GitLab self-managed installation (for Enterprise Edition or Community Edition)
  For an overview of the connections workflow, see [Workflow to create or update
  connections](welcome-connections-workflow.md "welcome-connections-workflow.md").

The steps to create connections for a cloud provider type, such as GitHub, are different
from the steps for an installed provider type, such as GitHub Enterprise Server. For the
high-level steps to create a connection by provider type, see [Working with connections](connections.md "connections.md").

###### Note

To use connections in the Europe (Milan) AWS Region, you must:

1. Install a Region-specific app
2. Enable the Region
   This Region-specific app supports connections in the Europe (Milan) Region. It is
   published on the third-party provider site, and it is separate from the existing app
   supporting connections for other Regions. By installing this app, you authorize third-party
   providers to share your data with the service for this Region only, and you can revoke the
   permissions at any time by uninstalling the app.

The service will not process or store your data unless you enable the Region. By enabling this Region, you grant our service permissions to process and store your
data.

Even if the Region is not enabled, third-party providers can still share your data with
our service if the Region-specific app remains installed, so make sure to uninstall the app
once you disable the Region. For more information, see [Enabling
a Region](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable").
