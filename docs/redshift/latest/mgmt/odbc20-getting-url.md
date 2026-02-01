Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting the ODBC URL

Amazon Redshift displays the ODBC URL for your cluster in the Amazon Redshift console. This URL
contains the information required to set up the connection between your client computer
and the database.

An ODBC URL has the following format:

```

Driver={`*driver*`}; Server=`*endpoint\_host*`; Database=`*database\_name*`; UID=`*user\_name*`; PWD=`*password*`; Port=`*port\_number*`

```

The preceding format's fields have the following values:

| Field      | Value                                                                                                                                                                                                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Driver`   | The name of the 64-bit ODBC driver to use: **Amazon Redshift ODBC<br>Driver (x64)**                                                                                                                                                                                                    |
| `Server`   | The endpoint host of the Amazon Redshift cluster.                                                                                                                                                                                                                                      |
| `Database` | The database that you created for your cluster.                                                                                                                                                                                                                                        |
| `UID`      | The user name of a database user account that has permission to<br>connect to the database. Although this value is a database-level<br>permission and not a cluster-level permission, you can use the Redshift<br>admin user account that you set up when you launched the<br>cluster. |
| `PWD`      | The password for the database user account to connect to the<br>database.                                                                                                                                                                                                              |
| `Port`     | The port number that you specified when you launched the cluster. If<br>you have a firewall, ensure that this port is open for you to<br>use.                                                                                                                                          |

The following is an example ODBC URL:

```

Driver={Amazon Redshift ODBC Driver (x64)}; Server=examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com; Database=dev; UID=adminuser; PWD=insert_your_admin_user_password_here; Port=5439

```

For information on where to find the ODBC URL, see [Finding your cluster connection string](configuring-connections.md#connecting-connection-string "configuring-connections.md#connecting-connection-string").
