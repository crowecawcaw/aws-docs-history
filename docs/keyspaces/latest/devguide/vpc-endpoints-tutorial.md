# Step 6: (Optional) Best practices

to configure the connection pool size for your application

In this section, we outline how to determine the ideal connection pool size based on
the query throughput requirements of your application.

Amazon Keyspaces allows a maximum of 3,000 CQL queries per second per TCP connection. So there's
virtually no limit on the number of connections that a driver can establish with Amazon Keyspaces.
However, we recommend that you match the connection pool size to the requirements of
your application and consider the available endpoints when you're using Amazon Keyspaces with VPC
endpoint connections.

You configure the connection pool size in the client driver. For example, based on a
local pool size of **2** and a VPC interface endpoint created across
**3** Availability Zones, the driver establishes
**6** connections for querying (7 in total, which includes a
control connection). Using these 6 connections, you can support a maximum of 18,000 CQL
queries per second.

If your application needs to support 40,000 CQL queries per second, work backwards
from the number of queries that are needed to determine the required connection pool
size. To support 40,000 CQL queries per second, you need to configure the local pool
size to be at least 5, which supports a minimum of 45,000 CQL queries per second.

You can monitor if you exceed the quota for the maximum number of operations per
second, per connection by using the `PerConnectionRequestRateExceeded` CloudWatch
metric in the `AWS/Cassandra` namespace. The
`PerConnectionRequestRateExceeded` metric shows the number of requests to
Amazon Keyspaces that exceed the quota for the per-connection request rate.

The code examples in this step show how to estimate and configure connection pooling
when you're using interface VPC endpoints.

Java
You can configure the number of connections per pool in the Java driver.
For a complete example of a Java client driver connection, see [Using a Cassandra Java client driver to
access Amazon Keyspaces programmatically](using_java_driver.md "using_java_driver.md").

When the client driver is started, first the control connection is
established for administrative tasks, such as for schema and topology
changes. Then the additional connections are created.

In the following example, the local pool size driver configuration is
specified as 2. If the VPC endpoint is created across 3 subnets within the
VPC, this results in 7 `NewConnections` in CloudWatch for the interface
endpoint, as shown in the following formula.

```
`NewConnections = 3 (VPC subnet endpoints created across) * 2 (pool size) + 1 ( control connection)`
```

```
datastax-java-driver {

    basic.contact-points = [ "cassandra.`us-east-1`.amazonaws.com:9142"]
    advanced.auth-provider{
        class = PlainTextAuthProvider
           username = "`ServiceUserName`"
           password = "`ServicePassword`"
    }
    basic.load-balancing-policy {
        local-datacenter = "`us-east-1`"
        slow-replica-avoidance = false
    }

    advanced.ssl-engine-factory {
        class = DefaultSslEngineFactory
        truststore-path = "./src/main/resources/cassandra_truststore.jks"
        truststore-password = "`my_password`"
        hostname-validation = false
      }
    advanced.connection {
        pool.local.size = 2
          }
}
```

If the number of active connections doesn’t match your configured pool
size (aggregation across subnets) + 1 control connection, something is
preventing the connections from being created.

Node.js
You can configure the number of connections per pool in the Node.js
driver. For a complete example of a Node.js client driver connection, see
[Using a Cassandra Node.js client driver to
access Amazon Keyspaces programmatically](using_nodejs_driver.md "using_nodejs_driver.md").

The code example below uses the
`keyspaces-bundle.pem` file for the digital
certicate. See [Before you begin](using_nodejs_driver.md#using_nodejs_driver.BeforeYouBegin "using_nodejs_driver.md#using_nodejs_driver.BeforeYouBegin") for more
information.

For the following code example, the local pool size driver configuration
is specified as 1. If the VPC endpoint is created across 4 subnets within
the VPC, this results in 5 `NewConnections` in CloudWatch for the
interface endpoint, as shown in the following formula.

```
NewConnections = 4 (VPC subnet endpoints created across) * 1 (pool size) + 1 ( control connection)
```

```
const cassandra = require('cassandra-driver');
const fs = require('fs');
const types = cassandra.types;
const auth = new cassandra.auth.PlainTextAuthProvider('ServiceUserName', 'ServicePassword');
const sslOptions1 = {
         ca: [
                    fs.readFileSync('/home/ec2-user/`keyspaces-bundle.pem`', 'utf-8')],
                    host: 'cassandra.`us-east-1`.amazonaws.com',
                    rejectUnauthorized: true
        };
const client = new cassandra.Client({
                   contactPoints: ['cassandra.`us-east-1`.amazonaws.com'],
                   localDataCenter: '`us-east-1`',
                   pooling: { coreConnectionsPerHost: { [types.distance.local]: 1 } },
                   consistency: types.consistencies.localQuorum,
                   queryOptions: { isIdempotent: true },
                   authProvider: auth,
                   sslOptions: sslOptions1,
                   protocolOptions: { port: 9142 }
        });
```
