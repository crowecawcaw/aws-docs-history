# Database engine updates for Amazon Aurora MySQL

Amazon Aurora releases updates regularly. Updates are applied to Aurora DB clusters during system
maintenance windows. The timing when updates are applied depends on the region and
maintenance window setting for the DB cluster, as well as the type of update.

Amazon Aurora releases are made available to all AWS Regions over the course of multiple days.
Some Regions might temporarily show an engine version that isn't available in a different Region yet.

Updates are applied to all instances in a DB cluster at the same time. An update requires a database restart on
all instances in a DB cluster, so you experience 20 to 30 seconds of downtime, after which you can resume using
your DB cluster or clusters. You can view or change your maintenance window settings from the
[AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").

For details about the Aurora MySQL versions that are supported by Amazon Aurora, see the [_Release Notes for Aurora MySQL_](../AuroraMySQLReleaseNotes/Welcome.md "../AuroraMySQLReleaseNotes/Welcome.md").

Following, you can learn how to choose the right Aurora MySQL version for your cluster, how to specify the
version when you create or upgrade a cluster, and the procedures to upgrade a cluster from one version to
another with minimal interruption.

###### Topics

- [Checking Aurora MySQL version numbers](AuroraMySQL.Updates.Versions.md "AuroraMySQL.Updates.Versions.md")
- [Long-term support (LTS) and beta releases for Amazon Aurora MySQL](AuroraMySQL.Update.SpecialVersions.md "AuroraMySQL.Update.SpecialVersions.md")
- [Preparing for Amazon Aurora MySQL-Compatible Edition version 2 end of standard support](Aurora.MySQL57.EOL.md "Aurora.MySQL57.EOL.md")
- [Preparing for Amazon Aurora MySQL-Compatible Edition version 1 end of life](Aurora.MySQL56.EOL.md "Aurora.MySQL56.EOL.md")
- [Upgrading Amazon Aurora MySQL DB clusters](AuroraMySQL.Updates.Upgrading.md "AuroraMySQL.Updates.Upgrading.md")
- [Database engine updates and fixes for Amazon Aurora MySQL](AuroraMySQL.Updates.RN.md "AuroraMySQL.Updates.RN.md")
