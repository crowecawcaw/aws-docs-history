# Troubleshooting connection issues

Having trouble connecting? Here are some common scenarios and how to resolve them.

**Topics**

- [Can't connect to
  an Amazon DocumentDB endpoint](#troubleshooting-connecting "#troubleshooting-connecting")
- [Testing a
  connection to an Amazon DocumentDB instance](#troubleshooting.testing-connection "#troubleshooting.testing-connection")
- [Connecting to an
  invalid endpoint](#troubleshooting.invalid-endpoint "#troubleshooting.invalid-endpoint")
- [Driver configuration impacting number of connections](#troubleshooting.driver.config "#troubleshooting.driver.config")

## Can't connect to

an Amazon DocumentDB endpoint

When you try to connect to Amazon DocumentDB, the following is one of the
most common error messages that you might receive.

```
connecting to: mongodb://docdb-2018-11-08-21-47-27.cluster-ccuszbx3pn5e.us-east-
1.docdb.amazonaws.com:27017/
2018-11-14T14:33:46.451-0800 W NETWORK [thread1] Failed to connect to
172.31.91.193:27017 after 5000ms milliseconds, giving up.
2018-11-14T14:33:46.452-0800 E QUERY [thread1] Error: couldn't connect to server
docdb-2018-11-08-21-47-27.cluster-ccuszbx3pn5e.us-east-1.docdb.amazonaws.com:27017,
connection attempt failed :
connect@src/mongo/shell/mongo.js:237:13
@(connect):1:6
exception: connect failed
```

What this error message typically means is that your client (the
mongo shell in this example) cannot access the Amazon DocumentDB endpoint.
This might be the case for several reasons:

###### Topics

- [Connecting from public endpoints](#troubleshooting.cannot-connect.public-endpoints "#troubleshooting.cannot-connect.public-endpoints")
- [Cross region connections](#troubleshooting.cannot-connect.different-regions "#troubleshooting.cannot-connect.different-regions")
- [Connecting from different Amazon VPCs](#troubleshooting.cannot-connect.different-vpcs "#troubleshooting.cannot-connect.different-vpcs")
- [Security group blocks inbound connections](#troubleshooting.cannot-connect.inbound-not-allowed "#troubleshooting.cannot-connect.inbound-not-allowed")
- [Java Mongo driver read preference issue](#troubleshooting-cannot-connect-java-mongo-issue "#troubleshooting-cannot-connect-java-mongo-issue")

###

Connecting from public endpoints

**You are trying to connect to an Amazon DocumentDB
cluster directly from your laptop or local development
machine.**

Trying to connect to an Amazon DocumentDB cluster directly from a public
endpoint, such as your laptop or local development machine, will
fail. Amazon DocumentDB is virtual private cloud (VPC)-only and does not
currently support public endpoints. Thus, you can't connect
directly to your Amazon DocumentDB cluster from your laptop or local
development environment outside of your VPC.

To connect to an Amazon DocumentDB cluster from outside an Amazon VPC, you
can use an SSH tunnel. For more information, see [Connecting to an Amazon DocumentDB cluster from outside an Amazon VPC](connect-from-outside-a-vpc.md "connect-from-outside-a-vpc.md").
Additionally, if your development environment is in a different
Amazon VPC, you can also use VPC Peering and connect to your Amazon DocumentDB
cluster from another Amazon VPC in the same region or a different
region.

###

Cross region connections

**You are trying to connect to an Amazon DocumentDB
cluster in another region.**

If you try to connect to an Amazon DocumentDB cluster from an Amazon EC2
instance in a Region other than the cluster's Region—for
example, trying to connect to a cluster in US East (N. Virginia) Region
(us-east-1) from US West (Oregon) Region (us-west-2)—the
connection will fail.

To verify the Region of your Amazon DocumentDB cluster, run the
following command. The Region is in the endpoint.

```
aws docdb describe-db-clusters \
   --db-cluster-identifier sample-cluster \
   --query 'DBClusters[*].Endpoint'
```

Output from this operation looks something like the following.

```
[
    "sample-cluster.node.us-east-1.docdb.amazonaws.com"
]
```

To verify the Region of your EC2 instance, run the following
command.

```
 aws ec2 describe-instances \
     --query 'Reservations[*].Instances[*].Placement.AvailabilityZone'
```

Output from this operation looks something like the following.

```
[
    [
        "`us-east-1`a"
    ]
]
```

###

Connecting from different Amazon VPCs

**You are trying to connect to an Amazon DocumentDB
cluster from a VPC that is different than the Amazon VPC your cluster
is deployed to.**

If both your Amazon DocumentDB cluster and Amazon EC2 instance are in the
same AWS Region, but not in the same Amazon VPC, you cannot connect
directly to your Amazon DocumentDB cluster unless VPC Peering is enabled
between the two Amazon VPCs.

To verify the Amazon VPC of your Amazon DocumentDB instance, run the
following command.

```
aws docdb describe-db-instances \
   --db-instance-identifier sample-instance \
   --query 'DBInstances[*].DBSubnetGroup.VpcId'
```

To verify the Amazon VPC of your Amazon EC2 instance, run the following
command.

```
aws ec2 describe-instances \
   --query 'Reservations[*].Instances[*].VpcId'
```

###

Security group blocks inbound connections

**You are trying to connect to an Amazon DocumentDB
cluster, and the cluster’s security group does not allow inbound
connections on the cluster’s port (default port: 27017).**

Suppose that your Amazon DocumentDB cluster and Amazon EC2 instance are both
in the same Region and Amazon VPC and use the same Amazon VPC security
group. If you can't connect to your Amazon DocumentDB cluster, the likely
cause is that your security group (that is, firewall) for your
cluster doesn't allow inbound connections on the port you chose
for your Amazon DocumentDB cluster (default port is 27017).

To verify the port for your Amazon DocumentDB cluster, run the following
command.

```
aws docdb describe-db-clusters \
   --db-cluster-identifier sample-cluster \
   --query 'DBClusters[*].[DBClusterIdentifier,Port]'
```

To get your Amazon DocumentDB security group for your cluster, run the
following command.

```
aws docdb describe-db-clusters \
   --db-cluster-identifier sample-cluster \
   --query 'DBClusters[*].[VpcSecurityGroups[*],VpcSecurityGroupId]'
```

To check the inbound rules for your security group, see the
following topics in the Amazon EC2 documentation:

- [Authorizing Inbound Traffic for Your Linux Instances](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md")
- [Authorizing Inbound Traffic for Your Windows Instances](../../../AWSEC2/latest/WindowsGuide/authorizing-access-to-an-instance.md "../../../AWSEC2/latest/WindowsGuide/authorizing-access-to-an-instance.md")

###

Java Mongo driver read preference issue

**Client read preferences are not honored and some clients cannot write to Amazon DocumentDB after failover unless they reboot.**

This issue, first discovered in Java Mongo Driver 3.7.x, occurs when a client establishes a connection to Amazon DocumentDB using `MongoClientSettings` and, specifically, when chaining the `applyToClusterSettings` method.
The MongoClient Cluster Settings can be defined using a few different methods, such as `hosts()`, `requiredReplicaSetName()`, and `mode()`.

When the client specifies only one host in the `hosts()` method, the mode is set to `ClusterConnectionMode.SINGLE` instead of `ClusterConnectionMode.MULTIPLE`
This causes the client to disregard the read preference and only connect to the server configured in `hosts()`.
So even if the client settings are initialized like below, all reads would still go to the primary instead of the secondary.

```
final ServerAddress serverAddress0 = new ServerAddress("cluster-endpoint", 27317));
    final MongoCredential credential = MongoCredential.createCredential("xxx",
            "admin", "xxxx".toCharArray());
    final MongoClientSettings settings = MongoClientSettings.builder()
            .credential(credential)
            .readPreference(ReadPreference.secondaryPreferred())
            .retryWrites(false)
            .applyToSslSettings(builder -> builder
                    .enabled(false))
            .applyToClusterSettings(builder -> builder.hosts(
                            Arrays.asList(serverAddress0
                            ))
                    .requiredReplicaSetName("rs0"))
            .build();
    MongoClient mongoClient = MongoClients.create(settings);
```

**Failover case**

Using the above client connection settings, if there is a failover and a delayed DNS record update for the cluster writer endpoint, the client would still try to issue writes to the old writer (now reader after failover).
This results in a server-side error (not primary) which is not handled appropriately by the Java driver (this is still under investigation).
Thus, the client can be left in a bad state until the application server is rebooted, for example.

There are two workarounds for this:

- Clients that connect to Amazon DocumentDB via a connection string will not have this issue, since `ClusterConnectionMode` will be set to `MULTIPLE` when setting read preference.

```
MongoClientURI mongoClientURI = new MongoClientURI("mongodb://usr:pass:cluster-endpoint:27317/test?ssl=false&replicaSet=rs0&readpreference=secondaryPreferred");
MongoClient mongoClient = MongoClients.create(mongoClientURI.getURI());
```

Or using `MongoClientSettings` builder with the `applyConnectionString` method.

```
final MongoClientSettings settings = MongoClientSettings.builder()
        .credential(credential)
        .applyConnectionString(new ConnectionString("usr:pass:cluster-endpoint:27317/test?ssl=false&replicaSet=rs0&readpreference=secondaryPreferred"))
        .retryWrites(false)
        .applyToSslSettings(builder → builder
                .enabled(false))
        .build();
MongoClient mongoClient = MongoClients.create(settings);
```

- Explicitly set `ClusterConnectionMode` to `MULTIPLE`.
  This is only needed when using `applyToClusterSettings` and `hosts().size() == 1`.

```
final ServerAddress serverAddress0 = new ServerAddress("cluster-endpoint", 27317));
final MongoCredential credential = MongoCredential.createCredential("xxx","admin", "xxxx".toCharArray());
final MongoClientSettings settings = MongoClientSettings.builder()
    .credential(credential)
    .readPreference(ReadPreference.secondaryPreferred())
    .retryWrites(false)
    .applyToSslSettings(builder → builder
    .enabled(false))
    .applyToClusterSettings(builder → builder
                .hosts(Arrays.asList(serverAddress0))
                .requiredReplicaSetName("rs0"))
                .mode(ClusterConnectionMode.MULTIPLE))
    .build();
MongoClient mongoClient = MongoClients.create(settings);
```

## Testing a

connection to an Amazon DocumentDB instance

You can test your connection to a cluster using common Linux or
Windows tools.

From a Linux or Unix terminal, test the connection by entering
the following (replace `cluster-endpoint` with the
endpoint, and replace `port` with the port of your
instance):

```
nc -zv cluster-endpoint port
```

The following is an example of a sample operation and the return
value:

```
nc -zv docdbTest.d4c7nm7stsfc0.us-west-2.docdb.amazonaws.com 27017

Connection to docdbTest.d4c7nm7stsfc0.us-west-2.docdb.amazonaws.com 27017 port [tcp/*] succeeded!
```

## Connecting to an

invalid endpoint

When connecting to an Amazon DocumentDB cluster and you use a cluster
endpoint that is not valid, an error similar to the following
appears.

```
mongo --ssl \
   --host sample-cluster.node.us-east-1.docdb.amazonaws.com:27017 \
   --sslCAFile global-bundle.pem \
   --username <user-name> \
   --password <password>
```

The output looks like this:

```
MongoDB shell version v3.6
connecting to: mongodb://sample-cluster.node.us-east-1.docdb.amazonaws.com:27017/
2018-11-14T17:21:18.516-0800 I NETWORK [thread1] getaddrinfo("sample-cluster.node.us-east-1.docdb.amazonaws.com") failed:
nodename nor servname provided, or not known 2018-11-14T17:21:18.537-0800 E QUERY [thread1] Error: couldn't initialize
connection to host sample-cluster.node.us-east-1.docdb.amazonaws.com, address is invalid :
connect@src/mongo/shell/mongo.js:237:13@(connect):1:6
exception: connect failed
```

To get the valid endpoint for a cluster, run the following command:

```
aws docdb describe-db-clusters \
   --db-cluster-identifier sample-cluster \
   --query 'DBClusters[*].[Endpoint,Port]'
```

To get the valid endpoint for an instance, run the following
command:

```
aws docdb describe-db-instances \
   --db-instance-identifier sample-instance \
   --query 'DBInstances[*].[Endpoint.Address,Endpoint.Port]'
```

For more information, see [Understanding Amazon DocumentDB endpoints](endpoints.md "endpoints.md").

## Driver configuration impacting number of connections

When using the client driver to connect to an Amazon DocumentDB cluster, it's important to consider the `maxPoolSize` configuration parameter.
The `maxPoolSize` setting determines the maximum number of connections that the client driver will maintain in its connection pool.
