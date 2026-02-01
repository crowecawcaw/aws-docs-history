Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Building the connection URL

Use the connection URL to supply connection information to the data store that you are
accessing. The following is the format of the connection URL for the Amazon Redshift JDBC
driver version 2.x. Here, [Host] the endpoint of the Amazon Redshift server and [Port] is the
number of the Transmission Control Protocol (TCP) port that the server uses to listen
for client requests.

```
jdbc:redshift://[Host]:[Port]
```

The following is the format of a connection URL that specifies some optional
settings.

```
jdbc:redshift://[Host]:[Port]/[database];[Property1]=[Value];
[Property2]=[Value];
```

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

For example, suppose that you want to connect to port 9000 on an Amazon Redshift cluster in the
US West (N. California) Region on AWS. You also want to access the database named
`dev` and authenticate the connection using a database username and
password. In this case, you use the following connection URL.

```
jdbc:redshift://redshift.company.us-west-1.redshift.amazonaws.com:9000/dev;UID=amazon;PWD=amazon
```

You can use the following characters to separate the configuration options from the
rest of the URL string:

- ;
- ?
  For example, the following URL strings are equivalent:

```
jdbc:redshift://my_host:5439/dev;ssl=true;defaultRowFetchSize=100
```

```
jdbc:redshift://my_host:5439/dev?ssl=true;defaultRowFetchSize=100
```

You can use the following characters to separate configuration options from each other
in the URL string:

- ;
- &
  For example, the following URL strings are equivalent:

```
jdbc:redshift://my_host:5439/dev;ssl=true;defaultRowFetchSize=100
```

```
jdbc:redshift://my_host:5439/dev;ssl=true&defaultRowFetchSize=100
```

The following URL example specifies a log level of 6 and the path for the logs.

```
jdbc:redshift://redshift.amazonaws.com:5439/dev;DSILogLevel=6;LogPath=/home/user/logs;
```

Don't duplicate properties in the connection URL.

For a complete list of the configuration options that you can specify, see [Options for JDBC driver version 2.x
configuration](jdbc20-configuration-options.md "jdbc20-configuration-options.md").

###### Note

When you connect, don't use the IP address of a cluster node or the IP address of
the VPC endpoint. Always use the Redshift endpoint to avoid an unnecessary outage.
The only exception to using the endpoint URL is when you use a custom domain name.
For more information, see [Using a custom domain name for client connections](connecting-connection-CNAME.md "connecting-connection-CNAME.md").
