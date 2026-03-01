# Transporting tablespaces

Use the Amazon RDS package `rdsadmin.rdsadmin_transport_util` to copy a set of
tablespaces from an on-premises Oracle database to an RDS for Oracle DB instance. At the physical level,
the transportable tablespace feature incrementally copies source data files and metadata
files to your target instance. You can transfer the files using either Amazon EFS or Amazon S3. For
more information, see [Migrating using Oracle transportable tablespaces](oracle-migrating-tts.md "oracle-migrating-tts.md").

###### Topics

- [Importing transported tablespaces to your DB instance](rdsadmin_transport_util_import_xtts_tablespaces.md "rdsadmin_transport_util_import_xtts_tablespaces.md")
- [Importing transportable tablespace metadata into your DB instance](rdsadmin_transport_util_import_xtts_metadata.md "rdsadmin_transport_util_import_xtts_metadata.md")
- [Listing orphaned files after a tablespace import](rdsadmin_transport_util_list_xtts_orphan_files.md "rdsadmin_transport_util_list_xtts_orphan_files.md")
- [Deleting orphaned data files after a tablespace import](rdsadmin_transport_util_cleanup_incomplete_xtts_import.md "rdsadmin_transport_util_cleanup_incomplete_xtts_import.md")
