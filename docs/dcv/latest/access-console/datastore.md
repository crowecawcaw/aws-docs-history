# Datastore

Amazon DCV Access Console persists user data, group data, session templates and the
permission data related to them through integrations with external databases. It
supports DynamoDB, MariaDB, and MySQL databases. You must set up and manage one of these
databases to use Amazon DCV Access Console. If your Amazon DCV Access Console machines are hosted
on Amazon EC2, we recommend using DynamoDB as the external database, since it does not require
any additional setup.

###### Note

Additional costs can happen when running an external database. To see information
on DynamoDB pricing, see [Pricing for Provisioned Capacity](https://aws.amazon.com/dynamodb/pricing/provisioned/ " https://aws.amazon.com/dynamodb/pricing/provisioned/").

###### Configure the Amazon DCV Access Console to persist on DynamoDB

1. On the host running the Handler component, open
   `/etc/dcv-access-console-handler/access-console-handler.properties`
   in your preferred editor and make the following edits:
   - Set `datastore = dynamodb`.
   - For `dynamodb-region` specify the AWS Region where you
     want to store the tables containing the Handler component data. For the
     list of supported Regions, see DynamoDB service endpoints.
   - For `datastore.prefix` specify the prefix that is added to
     each DynamoDB table (useful to distinguish multiple Handler component using
     the same account). Only alphanumeric characters, dot, dash, and
     underscore are allowed.

2. Stop the Handler component.

```
sudo systemctl stop dcv-access-console-handler
```

3. Start the Handler component.

```
sudo systemctl start dcv-access-console-handler
```

The Handler component host must have permission to call the DynamoDB APIs. On
Amazon EC2 instances, the credentials are automatically retrieved using the Amazon EC2
metadata service. If you need to specify different credentials, you can set them
using one of the supported credential retrieval techniques (such as Java system
properties or environment variables). For more information, see Supplying and
Retrieving AWS Credentials.

###### Configure the broker to persist on MariaDB/MySQL

1. On the host running the Handler component, open
   `/etc/dcv-access-console-handler/access-console-handler.properties`
   in your preferred editor and make the following edits:
   - Set `datastore = mysql`.
   - Set `jdbc-connection-url =
jdbc:mysql://`db_endpoint`:`db_port`/`db_name``

   In this configuration, `db_endpoint` is the
   database endpoint, `db_port` is the database
   port, and `db_name` is the database
   name.
   - For `datastore.prefix` specify the prefix that is added to
     each DynamoDB table (useful to distinguish multiple Handler component using
     the same account). Only alphanumeric characters, dot, dash, and
     underscore are allowed.

2. On the host running the Handler component, open
   `/etc/dcv-access-console-handler/access-console-handler-secrets.properties`
   in your preferred editor and make the following edits:
   - For `jdbc-user` specify the name of the user that has
     access to the database.
   - For `jdbc-password` specify the password of the user that
     has access to the database.

3. Stop the Handler component.

```
sudo systemctl stop dcv-access-console-handler
```

4. Start the Handler component.

```
sudo systemctl start dcv-access-console-handler
```

###### Note

The
`/etc/dcv-access-console-handler/access-console-handler-secrets.properties`
file contains sensitive data. By default, its write access is restricted to
root and its read access is restricted to root and to the user running the
Handler component. By default, this is the `dcvaccessconsole` user.
