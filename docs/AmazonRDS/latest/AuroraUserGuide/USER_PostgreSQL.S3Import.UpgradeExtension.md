

# Upgrading the aws\_s3 extension
<a name="USER_PostgreSQL.S3Import.UpgradeExtension"></a>

Upgrading your Aurora PostgreSQL DB cluster to a new version doesn't upgrade the `aws_s3` extension at the same time. To upgrade the extension after the engine upgrade completes, use the `ALTER EXTENSION ... UPDATE` command. For the general procedure, see [Upgrading PostgreSQL extensions](USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades.md).