

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Getting the ODBC URL
<a name="odbc20-getting-url"></a>

Amazon Redshift displays the ODBC URL for your cluster in the Amazon Redshift console. This URL contains the information required to set up the connection between your client computer and the database.

An ODBC URL has the following format: 

```
Driver={{{driver}}}; Server={{endpoint_host}}; Database={{database_name}}; UID={{user_name}}; PWD={{password}}; Port={{port_number}}
```

The preceding format's fields have the following values:


| Field | Value | 
| --- | --- | 
| {{Driver}} | The name of the 64-bit ODBC driver to use: Amazon Redshift ODBC Driver (x64) | 
| {{Server}} | The endpoint host of the Amazon Redshift cluster. | 
| {{Database}} | The database that you created for your cluster. | 
| {{UID}} | The user name of a database user account that has permission to connect to the database. Although this value is a database-level permission and not a cluster-level permission, you can use the Redshift admin user account that you set up when you launched the cluster. | 
| {{PWD}} | The password for the database user account to connect to the database. | 
| {{Port}} | The port number that you specified when you launched the cluster. If you have a firewall, ensure that this port is open for you to use. | 

The following is an example ODBC URL: 

```
Driver={Amazon Redshift ODBC Driver (x64)}; Server=examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com; Database=dev; UID=adminuser; PWD=insert_your_admin_user_password_here; Port=5439
```

For information on where to find the ODBC URL, see [Finding your cluster connection string](https://docs.aws.amazon.com/redshift/latest/mgmt/configuring-connections.html#connecting-connection-string). 