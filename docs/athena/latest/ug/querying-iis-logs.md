# Query internet information server (IIS) logs stored in

Amazon S3

You can use Amazon Athena to query Microsoft Internet Information Services (IIS) web server
logs stored in your Amazon S3 account. While IIS uses a [variety](<https://docs.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms525807(v%3Dvs.90)> "https://docs.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms525807(v%3Dvs.90)") of log file formats, this topic shows you how to create table schemas
to query W3C extended and IIS log file format logs from Athena.

Because the W3C extended and IIS log file formats use single character delimiters (spaces
and commas, respectively) and do not have values enclosed in quotation marks, you can use
the [LazySimpleSerDe](lazy-simple-serde.md "lazy-simple-serde.md") to create Athena tables for them.

###### Topics

- [Query W3C extended log
  file format](querying-iis-logs-w3c-extended-log-file-format.md "querying-iis-logs-w3c-extended-log-file-format.md")
- [Query IIS log file
  format](querying-iis-logs-iis-log-file-format.md "querying-iis-logs-iis-log-file-format.md")
- [Query NCSA log file format](querying-iis-logs-ncsa-log-file-format.md "querying-iis-logs-ncsa-log-file-format.md")
