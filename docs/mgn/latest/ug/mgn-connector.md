NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Run Commands on Multiple Source Servers with AWS Application Migration Service

Large-scale migrations, involving many source servers, often require preparation and planning. The source servers may have a wide variety of operating system version, and may be distributed across multiple data centers.

Before the migration execution can begin, various actions may need to be performed, for example:

- Verifying the prerequisites to install the MGN replication agent on the source servers.
- Installing the AWS MGN replication agents on the source servers.
  To address these needs, AWS Application Migration Service offers the MGN connector – a feature that allows you to automate running commands on your source environment.

You can install the AWS MGN connector in your source environment and use it to perform actions on source servers in your data center.

This feature, combined with the post-launch action framework, offers automation across the entire deployment process.

###### Topics

- [Prerequisites for installing the MGN connector](mgn-connector-prerequisites.md "mgn-connector-prerequisites.md")
- [Architecture overview when using MGN connector](mgn-connector-architecture.md "mgn-connector-architecture.md")
- [Required permissions for the MGN Connector](mgn-connector-permissions.md "mgn-connector-permissions.md")
- [Set up the MGN Connector](mgn-connector-setup-instructions.md "mgn-connector-setup-instructions.md")
- [Installing the MGN connector on a secured network](mgn-connector-installing-secured-network.md "mgn-connector-installing-secured-network.md")
- [Review your MGN Connectors](mgn-connector-main.md "mgn-connector-main.md")
- [Review details about your MGN connectors](connector-details.md "connector-details.md")
