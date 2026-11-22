

# MGN Connectors

MGN connectors enable you to run commands on multiple source servers. The AWS Transform MGN Connector has two main roles in your migration environment:
+ **Automation server for source actions:** Acts as an automation server that connects to your on-premises environment machines and executes [source actions](source-actions.md) on them. Source actions are custom scripts you define to prepare machines during the migration lifecycle.
+ **Replication agent deployment:** Installs the MGN replication agents on your on-premises machines. The connector also verifies that the prerequisites are met for installation of the MGN replication agent on your source servers.

Use connectors for large-scale migrations with multiple operating system types and versions distributed across multiple data centers. This feature, combined with the post-launch action framework, offers automation across the entire deployment process.

**Topics**
+ [Prerequisites for installing the MGN connector](mgn-connector-prerequisites.md)
+ [Architecture overview for MGN connector](mgn-connector-architecture.md)
+ [Set up the MGN Connector](mgn-connector-setup-instructions.md)
+ [IAM roles needed for the MGN connector](mgn-connector-permissions.md)
+ [Installing the MGN connector on a secured network](mgn-connector-installing-secured-network.md)
+ [Review details about your MGN connectors](connector-details.md)
+ [Manage your MGN Connectors](mgn-connector-main.md)