Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Query troubleshooting

This section provides a quick reference for identifying and addressing some of the most
common and most serious issues that you are likely to encounter with Amazon Redshift queries.

###### Topics

- [Connection fails](queries-troubleshooting-connection-fails.md "queries-troubleshooting-connection-fails.md")
- [Query hangs](queries-troubleshooting-query-hangs.md "queries-troubleshooting-query-hangs.md")
- [Query takes too long](queries-troubleshooting-query-takes-too-long.md "queries-troubleshooting-query-takes-too-long.md")
- [Load fails](queries-troubleshooting-load-fails.md "queries-troubleshooting-load-fails.md")
- [Load takes too long](queries-troubleshooting-load-takes-too-long.md "queries-troubleshooting-load-takes-too-long.md")
- [Load data is incorrect](queries-troubleshooting-load-data-incorrect.md "queries-troubleshooting-load-data-incorrect.md")
- [Setting the JDBC fetch size parameter](set-the-JDBC-fetch-size-parameter.md "set-the-JDBC-fetch-size-parameter.md")
  These suggestions give you a starting point for troubleshooting. You can also refer to
  the following resources for more detailed information.

For information about behavior changes in Amazon Redshift functionality that may affect your application, see
[Behavior Changes](../mgmt/behavior-changes.md "../mgmt/behavior-changes.md").

- [Accessing Amazon Redshift clusters and
  databases](../mgmt/using-rs-tools.md "../mgmt/using-rs-tools.md")

- [Automatic table optimization](t_Creating_tables.md "t_Creating_tables.md")

- [Loading data in Amazon Redshift](t_Loading_data.md "t_Loading_data.md")

- [Tutorial: Loading data from Amazon S3](tutorial-loading-data.md "tutorial-loading-data.md")
