# Downtime during the time zone file update

When RDS updates your time zone file, existing data that uses `TIMESTAMP WITH
 TIME ZONE` might change. In this case, your primary consideration is
downtime.

###### Warning

If you add the `TIMEZONE_FILE_AUTOUPGRADE` option, your engine upgrade
might have prolonged downtime. Updating time zone data for a large database might
take hours or even days.

The length of the time zone file update depends on factors such as the
following:

- The amount of `TIMESTAMP WITH TIME ZONE` data in your
  database
- The DB instance configuration
- The DB instance class
- The storage configuration
- The database configuration
- The database parameter settings
  Additional downtime can occur when you do the following:

- Add the option to the option group when the DB instance uses an outdated time zone
  file
- Upgrade the Oracle database engine when the new engine version contains a new
  version of the time zone file

###### Note

During the time zone file update, RDS for Oracle calls `PURGE
 DBA_RECYCLEBIN`.
