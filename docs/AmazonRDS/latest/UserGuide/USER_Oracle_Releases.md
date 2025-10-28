# Oracle Database engine release notes

Updates to your Amazon RDS for Oracle DB instances keep them current. If you apply updates, you can be confident that your DB instance is running
a version of the database software that has been tested by both Oracle and Amazon. We don't support applying one-off patches to
individual RDS for Oracle DB instances.

You can specify any currently supported Oracle Database version when you create a new DB instance. You can specify the major version, such
as Oracle Database 19c, and any supported minor version for the specified major version. If no version is specified, Amazon RDS defaults to a
supported version, typically the most recent version. If a major version is specified but a minor version is not, Amazon RDS defaults to a recent
release of the major version that you have specified. To see a list of supported versions and defaults for newly created DB instances, use the
[`describe-db-engine-versions`](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS CLI command.

For details about the Oracle Database versions that Amazon RDS supports, see the [_Amazon RDS for Oracle Release Notes_](../OracleReleaseNotes/Welcome.md "../OracleReleaseNotes/Welcome.md").
