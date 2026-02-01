Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting the JDBC URL

Before you can connect to your Amazon Redshift cluster from a SQL client tool, you need to
know the JDBC URL of your cluster. The JDBC URL has the following format:
`jdbc:redshift://`endpoint`:`port`/`database``.

The fields of the preceding format have the following values.

| Field      | Value                                                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `jdbc`     | The protocol for the connection.                                                                                                                 |
| `redshift` | The subprotocol that specifies to use the Amazon Redshift driver<br>to connect to the database.                                                  |
| `endpoint` | The endpoint of the Amazon Redshift cluster.                                                                                                     |
| `port`     | The port number that you specified when you launched<br>the cluster. If you have a firewall, make sure that this port is open<br>for you to use. |
| `database` | The database that you created for your<br>cluster.                                                                                               |

The following is an example JDBC URL:
`jdbc:redshift://examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com:5439/dev`

If your URL values contain any of the following URI reserved characters, the values
must be URL encoded:

- ;
- -
- {
- }
- [
- ]
- &
- =
- ?
- an empty space
  For example, if your `PWD` value is `password:password`, a
  connection URL using that value would look something like the following:

`jdbc:redshift://redshift.company.us-west-1.redshift.amazonaws.com:9000/dev;UID=amazon;PWD=password%3Apassword`

For information about how to get your JDBC connection, see [Finding your cluster connection
string](connecting-connection-string.md "connecting-connection-string.md").

If the client computer fails to connect to the database, you can troubleshoot possible
issues. For more information, see [Troubleshooting connection issues in
Amazon Redshift](troubleshooting-connections.md "troubleshooting-connections.md").
