# Release notes for Amazon Relational Database Service (Amazon RDS) for Oracle

The Amazon RDS for Oracle release notes provide details about the Oracle Database versions that are
supported by Amazon RDS.

Updates to your Amazon RDS for Oracle DB instances keep them current. If you apply updates, you
can be confident that your DB instance is running a version of the database software that
has been tested by both Oracle and Amazon. We don't support applying one-off patches to
individual DB instances.

You can specify any currently supported Oracle Database version when creating a new DB
instance. You can specify the major version, such as Oracle Database 21c Release 1
(21.0.0.0), and any supported minor version for the specified major version. If no version
is specified, Amazon RDS defaults to a supported version, typically the most recent version. If a
major version is specified but a minor version isn't, Amazon RDS defaults to a recent release of
the major version that you specified. To see a list of supported versions and defaults for
newly created DB instances, use the [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS CLI command. To view the major versions of your
Oracle databases, run the [describe-db-major-engine-versions](../../../cli/latest/reference/rds/describe-db-major-engine-versions.md "../../../cli/latest/reference/rds/describe-db-major-engine-versions.md") AWS CLI command or use the [DescribeDBMajorEngineVersions](../APIReference/API_DescribeDBMajorEngineVersions.md "../APIReference/API_DescribeDBMajorEngineVersions.md") RDS API operation.

These release notes apply to RDS for Oracle. If you are looking for details about RDS Custom for Oracle,
please see [Supported Regions and DB engines for RDS Custom](../UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.md "../UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.md").

**Topics**

- [Amazon RDS for Oracle Database 21c (21.0.0.0)](oracle-version-21-0.md "oracle-version-21-0.md")
- [Amazon RDS for Oracle Database 19c (19.0.0.0)](oracle-version-19-0.md "oracle-version-19-0.md")
- [Amazon RDS for Oracle Database 18c (18.0.0.0)](oracle-version-18-0.md "oracle-version-18-0.md")
- [Amazon RDS for Oracle Database 12c Release 2 (12.2.0.1)](oracle-version-12-2.md "oracle-version-12-2.md")
- [Amazon RDS for Oracle Database 12c Release 1 (12.1.0.2)](oracle-version-12-1.md "oracle-version-12-1.md")
- [Amazon RDS for Oracle Database 11g Release 2 (11.2.0.4)](oracle-version-11-2.md "oracle-version-11-2.md")
