# Supported Regions and Aurora DB engines for exporting snapshot data

to Amazon S3

You can export Aurora DB cluster snapshot data to an Amazon S3 bucket. You can export manual
snapshots and automated system snapshots. After the data is exported, you can analyze
the exported data directly through tools like Amazon Athena or Amazon Redshift Spectrum. For more
information, see [Exporting DB cluster snapshot data to Amazon S3](aurora-export-snapshot.md "aurora-export-snapshot.md").

Exporting snapshots to S3 is available in all AWS Regions except the
following:

- Asia Pacific (Malaysia)
- Asia Pacific (New Zealand)
- Asia Pacific (Taipei)
- Asia Pacific (Thailand)
- Mexico (Central)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)

###### Topics

- [Exporting snapshot data to S3 with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.ams "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.ams")
- [Exporting snapshot data to S3 with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.apg "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.apg")

## Exporting snapshot data to S3 with Aurora MySQL

All currently available Aurora MySQL engine versions support
exporting DB cluster snapshot data to Amazon S3. For more information about versions, see
[_Release Notes for Aurora MySQL_](../AuroraMySQLReleaseNotes/Welcome.md "../AuroraMySQLReleaseNotes/Welcome.md").

## Exporting snapshot data to S3 with Aurora PostgreSQL

All currently available Aurora PostgreSQL engine versions support exporting DB cluster
snapshot data to Amazon S3. For more information about versions, see the [_Release Notes for Aurora PostgreSQL_](../AuroraPostgreSQLReleaseNotes/Welcome.md "../AuroraPostgreSQLReleaseNotes/Welcome.md").
