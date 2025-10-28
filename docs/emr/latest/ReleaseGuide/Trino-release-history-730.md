# Amazon EMR 7.3.0 - Trino

release notes

## Amazon EMR 7.3.0 - Trino changes

- This release upgrades Trino from version 436 to 442.
- This release redirects Hudi queries to the new Hudi corrector. The old Hive connector
  can no longer read Hudi tables. Note
- This release removes the Rubix module from Amazon EMR because it is now deprecated from open-source.
- This release [removes legacy mode](https://github.com/trinodb/trino/pull/21013 "https://github.com/trinodb/trino/pull/21013") in the `hive.security` property. The default
  is now `allow-all`.
