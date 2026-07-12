NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Configuring AWS Transform MGN Settings

AWS Transform MGN uses replication settings to determine how data is replicated from source
servers to your AWS account and Region. Learn how to configure your initial replication
template and how to set individual server replication settings.

You must configure the replication template upon first use of AWS Transform MGN. The replication
template determines how your servers are replicated to AWS through
settings such as Replication Server instance type, target storage type, security groups, data routing, and tags. The settings configured in the
replication template are automatically used for every server you add to AWS Transform MGN.

Once you have configured your Replication template, you can make changes to individual
servers or a group of servers by editing their replication settings within the Server
Details View.

You can also configure optional post-launch settings that automate target instance
deployment and prepare your migrated servers for disaster recovery with AWS Elastic Disaster Recovery.

###### Topics

- [Replication template](replication-settings-template.md "replication-settings-template.md")
- [Launch template](launch-template.md "launch-template.md")
- [Post-launch template](post-launch-settings.md "post-launch-settings.md")
