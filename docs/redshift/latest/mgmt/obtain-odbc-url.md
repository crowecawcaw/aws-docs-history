Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting the ODBC URL

Amazon Redshift displays the ODBC URL for your cluster in the Amazon Redshift console. This
URL contains the information to set up the connection between your client
computer and the database.

An ODBC URL has the following format:
`Driver={`driver`};Server=`endpoint`;Database=`database_name`;UID=`user_name`;PWD=`password`;Port=`port_number``

The fields of the format shown preceding have the following values.

| Field      | Value                                                                                                                                                                                                                                                          |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Driver`   | The name of the 64-bit ODBC driver to<br>use: **Amazon Redshift (x64)**.<br>The name of the 32-bit ODBC driver: **Amazon Redshift<br>(x86)**.                                                                                                                  |
| `Server`   | The endpoint of the Amazon Redshift cluster.                                                                                                                                                                                                                   |
| `Database` | The database that you created for your<br>cluster.                                                                                                                                                                                                             |
| `UID`      | The user name of a user account that has<br>permission to connect to the database. This value is a database<br>permission, not an Amazon Redshift permission, although you can use the<br>admin user account that you set up when you launched the<br>cluster. |
| `PWD`      | The password for the user account to connect<br>to the database.                                                                                                                                                                                               |
| `Port`     | The port number that you specified when you<br>launched the cluster. If you have a firewall, ensure that this<br>port is open for you to use.                                                                                                                  |

The fields in the preceding tables can contain the following special
characters:

```
[]{}(),;?*=!@
```

If you use these special characters you must enclose the value in curly
braces. For example, the password value `Your;password123` in a
connection string is represented as `PWD={Your;password123};`.

Since `Field=value` pairs are separated by semicolon, the
combination of `}` and `;` with any number of spaces in
between is considered the end of a `Field={value};` pair. We
recommend you avoid the sequence `};` in your field values. For
example, if you set your password value as `PWD={This is a passwor}
 ;d};`, your password would be `This is a passwor} ;` and
the URL would error out.

The following is an example ODBC URL.

```
Driver={Amazon Redshift (x64)};
                    Server=examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com;
                    Database=dev;
                    UID=adminuser;
                    PWD=`insert_your_admin_user_password_here`;
                    Port=5439
```

For information about how to get your ODBC connection, see [Finding your cluster connection
string](connecting-connection-string.md "connecting-connection-string.md").
