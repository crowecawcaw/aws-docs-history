# AWS Elastic Disaster Recovery (AWS DRS) settings

AWS Elastic Disaster Recovery includes multiple configuration options for resources consumed and produced by the service. There are three
main catergoies that these configuration options fall in to:

- **Replication Settings** - Configuration Options for
  Replication Servers.
- **Launch Settings** - Configuration Options for Source Server Launches.
- **Post Launch Actions** - SSM Documents associated with Source Servers after Recovery Instances launch.

**Launch Settings** and **Replication
Settings** are configurable on an individual Source Server, as well as defaults
for a Region. **Default launch** settings and **Default replication** settings are initially configured while
Initializing the AWS Elastic Disaster Recovery Service. A newly added Source Server is implicitly configured
with the same settings defined in the **Default launch**
settings and **Default replication** settings upon
installation. You can adjust the individual configuration of a Source Server's Settings
anytime after installation.

###### Topics

- [AWS DRS replication settings](replication-settings.md "replication-settings.md")
- [AWS DRS launch settings](launch-settings-overview.md "launch-settings-overview.md")
- [Configuring the default post-launch actions](post-launch-action-settings-overview.md "post-launch-action-settings-overview.md")
