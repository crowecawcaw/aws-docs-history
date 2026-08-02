Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Known limitations for the Amazon RDS (Oracle) connector

The Amazon RDS (Oracle) connector has the following known limitations:

- Deleted database rows will not be tracked in when Amazon Q checks
  for updated content.
- The size of field names and values in a row of your database can't exceed
  400KB.
- Column names should only contain alphanumeric characters and not spaces.
- If you have a large amount of data in your database data source, and do not
  want Amazon Q to index all your database content after the first
  sync, you can choose to sync only new, modified, or deleted documents.
