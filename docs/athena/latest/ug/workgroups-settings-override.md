# Override client-side settings

When you create or edit a workgroup, you can choose the option **Override
client-side settings**. This option is not selected by default. Depending on
whether you select it, Athena does the following:

- If **Override client-side settings** is not selected, workgroup
  settings are not enforced at the client level. When the override client-side
  settings option is not selected for the workgroup, Athena uses the client's settings
  for all queries that run in the workgroup, including the settings for query results
  location, expected bucket owner, encryption, and control of objects written to the
  query results bucket. Each user can specify their own settings in the
  **Settings** menu on the console. If the client-side settings
  are not set, the workgroup-wide settings apply. If you use the AWS CLI, API actions,
  or JDBC and ODBC drivers to run queries in a workgroup that does not override
  client-side settings, your queries use the settings that you specify in your
  queries.
- If **Override client-side settings** is selected, workgroup
  settings are enforced at the workgroup level for all clients in the workgroup. When
  the override client-side settings option is selected for the workgroup, Athena uses
  the workgroup's settings for all queries that run in the workgroup, including the
  settings for query results location, expected bucket owner, encryption, and control
  of objects written to the query results bucket. Workgroup settings override any
  client-side settings that you specify for a query when you use the console, API
  actions, or JDBC or ODBC drivers. After workgroup settings are set to override
  client-side settings, client-side settings in the drivers or the API can be
  omitted.

If you override client-side settings, then the next time that you or any workgroup
user opens the Athena console, Athena notifies you that queries in the workgroup use
the workgroup's settings, and prompts you to acknowledge this change.

###### Note

Because overriding client-side settings can break custom automation that is
based on the availability of results in an arbitrary Amazon S3 bucket, we recommend
that you inform your users before overriding.

###### Important

If you use API actions, the AWS CLI, or the JDBC and ODBC drivers to run queries
in a workgroup that overrides client-side settings, make sure that you either
omit the client-side settings in your queries or update them to match the
settings of the workgroup.

If you specify client-side settings in your queries but run them in a
workgroup that overrides the settings, the queries will run, but the workgroup
settings will be used. For information about viewing the settings for a
workgroup, see [View the workgroup's details](viewing-details-workgroups.md "viewing-details-workgroups.md").
