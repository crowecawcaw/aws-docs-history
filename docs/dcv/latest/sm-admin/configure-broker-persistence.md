# Configuring broker persistence

Session Manager brokers support integration with external databases. The external database allows
Session Manager to persist status data and keys so they are available afterwards. In fact the broker data is
distributed over the cluster, making it susceptible to data loss if a host needs to reboot or
a cluster is terminated. With this feature enabled, you can add and remove broker nodes. Also, you can
stop a cluster and restart it, without the need to regenerate keys or lose information about which Amazon DCV Server
is open or closed.

The following types of information can be set to persist:

- Keys for setting up sessions to establish connection with clients
- In-flight sessions data
- Amazon DCV server status
  Amazon DCV Session Manager supports DynamoDB, MariaDB, and MySQL databases. You must set up and manage one of these
  databases to use this feature. If your broker machines are hosted on Amazon EC2,
  we recommend using DynamoDB as the external database, since it does not require any
  additional setup.

###### Note

You may incur additional costs when running an external database. To see information on DynamoDB pricing, see
[Pricing for Provisioned Capacity](https://aws.amazon.com/dynamodb/pricing/provisioned/ "https://aws.amazon.com/dynamodb/pricing/provisioned/").

## Configure the broker to persist on DynamoDB

Configure the brokers to start storing their data on DynamoDB:

1. Open `/etc/dcv-session-manager-broker/session-manager-broker.properties`
   using your preferred text editor and make the following edits:
   - Set `enable-persistence = true`
   - Set `persistence-db = dynamodb`
   - For `dynamodb-region` specify the &aws; Region where you want to store the
     tables containing the broker data. For the list of supported Regions,
     see [DynamoDB service endpoints](../../../general/latest/gr/ddb.md "../../../general/latest/gr/ddb.md").
   - For `dynamodb-table-rcu` specify the amount of Read Capacity
     Units (RCU) that each table supports. For more information about RCU, see
     [DynamoDB provisioned capacity](https://aws.amazon.com/dynamodb/pricing/provisioned "https://aws.amazon.com/dynamodb/pricing/provisioned").
   - For `dynamodb-table-wcu` specify the amount of Write Capacity Units
     (WCU) that each table supports. For more info on WCU, see [DynamoDB provisioned capacity](https://aws.amazon.com/dynamodb/pricing/provisioned "https://aws.amazon.com/dynamodb/pricing/provisioned").
   - For dynamodb-table-name-prefix specify the prefix that is added to each DynamoDB
     table (useful to distinguish multiple broker clusters using the same account). Only
     alphanumeric characters, dot, dash, and underscore are allowed.

2. Stop all the brokers in the cluster. For each broker, run the following command:

```
sudo systemctl stop dcv-session-manager-broker
```

3. Ensure all brokers in the cluster are stopped and then restart all of them. Start each broker by running
   the following command:

```
sudo systemctl start dcv-session-manager-broker
```

The broker host must have permission to call the DynamoDB APIs. On Amazon EC2 instances, the
credentials are automatically retrieved using the Amazon EC2 metadata service. If you need to
specify different credentials, you can set them using one of the supported credential
retrieval techniques (such as Java system properties or environment variables). For more
information, see [Supplying and Retrieving &aws; Credentials](../../../sdk-for-java/latest/developer-guide/credentials.md#credentials-profiles "../../../sdk-for-java/latest/developer-guide/credentials.md#credentials-profiles").

## Configure the broker to persist on MariaDB/MySQL

###### Note

The `/etc/dcv-session-manager-broker/session-manager-broker.properties` file contains sensitive data. By default,
its write access is restricted to root and its read access is restricted to root and to the user running the Broker. By default,
this is the `dcvsmbroker` user. The Broker checks at startup that the file has the expected permissions.

Configure the brokers to start persisting their data on MariaDB/MySQL:

1. Open `/etc/dcv-session-manager-broker/session-manager-broker.properties`
   with your preferred text editor and make the following edits:
   - Set `enable-persistence = true`
   - Set `persistence-db = mysql`
   - Set `jdbc-connection-url = jdbc:mysql://`<db_endpoint>`:`<db_port>`/`<db_name>`?createDatabaseIfNotExist=true`

   In this configuration, <db_endpoint> is the database endpoint, <db_port> is the
   database port, and <db_name> is the database name.
   - For `jdbc-user` specify the name of the user that has access to the
     database.
   - For `jdbc-password` specify the password of the user that has access to the
     database.

2. Stop all the brokers in the cluster. For each broker, run the following command:

```
sudo systemctl stop dcv-session-manager-broker
```

3. Ensure all brokers in the cluster are stopped, and then restart all of them. For each broker,
   run the following command:

```
sudo systemctl start dcv-session-manager-broker
```
