# AWS usage reports for Amazon EFS

When you download a usage report, you can choose to aggregate usage data by hour, day, or
month. The Amazon EFS usage report lists operations by usage type and AWS Region. For more
detailed reports about your Amazon EFS storage usage, download dynamically generated AWS usage
reports. You can choose which usage type, operation, and time period to include. You can also
choose how the data is aggregated. For more information about downloading usage reports, see [Downloading an AWS Usage Report](../../../cur/latest/userguide/usage-report.md "../../../cur/latest/userguide/usage-report.md")
in the _AWS Data Exports User Guide_.

The Amazon EFS usage report includes the following information:

- Service – Amazon EFS
- UsageType – One of the following
  values:

      + A code that identifies the type of storage
      + A code that identifies the type of request
      + A code that identifies the type of data transfer
      + A code that identifies the throughput mode
      + A code that identifies the backup usage

  For a detailed explanation of Amazon EFS usage types, see [Understanding billing and
  usage reports for Amazon EFS](billing-usage-reports-understand.md "billing-usage-reports-understand.md").

- Resource – The name of the resource
  associated with the listed usage.
- StartTime – Start time of the day that
  the usage applies to, in Coordinated Universal Time (UTC).
- EndTime – End time of the day that the
  usage applies to, in Coordinated Universal Time (UTC).
- UsageValue – One of the following volume
  values. The typical unit of measurement for data is gigabytes (GB). However,
  depending on the service and the report, terabytes (TB) might appear
  instead.

      + The number of requests during the specified time period
      + The amount of data transferred
      + The amount of data stored in a given hour

  For information about understanding the codes and abbreviations used in the billing and usage reports for
  Amazon EFS, see
  [Understanding billing and
  usage reports for Amazon EFS](billing-usage-reports-understand.md "billing-usage-reports-understand.md").
