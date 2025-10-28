# Failing over a Multi-AZ DB cluster for Amazon RDS

If there is a planned or unplanned outage of your writer DB instance in a Multi-AZ DB cluster, Amazon RDS
automatically fails over to a reader DB instance in different Availability Zone. This ensures high
availability with minimal disruption. Failovers can occur during hardware failures, network
issues, or manual requests. The topic outlines the automatic detection of failures, the
sequence of events during failover, and its impact on read and write operations. It also
provides best practices for monitoring and minimizing failover times.

The time it takes for the failover to complete depends on the database activity and other
conditions when the writer DB instance became unavailable. Failover times are typically under 35
seconds. Failover completes when both reader DB instances have applied outstanding transactions
from the failed writer. When the failover is complete, it can take additional time for the
RDS console to reflect the new Availability Zone.

###### Topics

- [Automatic failovers](#multi-az-db-clusters-concepts-failover-automatic "#multi-az-db-clusters-concepts-failover-automatic")
- [Manually failing over a Multi-AZ DB cluster](#multi-az-db-clusters-concepts-failover-manual "#multi-az-db-clusters-concepts-failover-manual")
- [Determining whether a Multi-AZ DB cluster has failed over](#multi-az-db-clusters-concepts-failover-determining "#multi-az-db-clusters-concepts-failover-determining")
- [Setting the JVM TTL for DNS name lookups](#multi-az-db-clusters-concepts-failover-java-dns "#multi-az-db-clusters-concepts-failover-java-dns")

## Automatic failovers

Amazon RDS handles failovers automatically so you can resume database operations as quickly as possible
without administrative intervention. To fail over, the writer DB instance switches automatically to a reader
DB instance.

## Manually failing over a Multi-AZ DB cluster

If you manually fail over a Multi-AZ DB cluster, RDS first terminates the primary DB instance. Then, the
internal monitoring system detects that the primary DB instance is unhealthy and promotes
a readable replica DB instance. Failover times are typically under 35 seconds.

You can fail over a Multi-AZ DB cluster manually using the AWS Management Console, the AWS CLI, or the RDS
API.

###### To fail over a Multi-AZ DB cluster manually

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the Multi-AZ DB cluster that you want to fail over.
4. For **Actions**, choose **Failover**.

The **Failover DB cluster** page appears. 5. Choose **Failover** to confirm the manual failover.
To fail over a Multi-AZ DB cluster manually, use the AWS CLI command [failover-db-cluster](../../../cli/latest/reference/rds/failover-db-cluster.md "../../../cli/latest/reference/rds/failover-db-cluster.md").

```
aws rds failover-db-cluster --db-cluster-identifier `mymultiazdbcluster`
```

To fail over a Multi-AZ DB cluster manually, call the Amazon RDS API
[FailoverDBCluster](../APIReference/API_FailoverDBCluster.md "../APIReference/API_FailoverDBCluster.md") and specify the
`DBClusterIdentifier`.

## Determining whether a Multi-AZ DB cluster has failed over

To determine if your Multi-AZ DB cluster has failed over, you can do the following:

- Set up DB event subscriptions to notify you by email or SMS that a failover has been
  initiated. For more information about events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
- View your DB events by using the Amazon RDS console or API operations.
- View the current state of your Multi-AZ DB cluster by using the Amazon RDS console,
  the AWS CLI, and the RDS API.

For information on how you can respond to failovers, reduce recovery time, and other best
practices for Amazon RDS, see [Best practices for Amazon RDS](CHAP_BestPractices.md "CHAP_BestPractices.md").

## Setting the JVM TTL for DNS name lookups

The failover mechanism automatically changes the Domain Name System (DNS) record of the DB
instance to point to the reader DB instance. As a result, you need to re-establish
any existing connections to your DB instance. In a Java virtual machine (JVM)
environment, due to how the Java DNS caching mechanism works, you might need to
reconfigure JVM settings.

The JVM caches DNS name lookups. When the JVM resolves a host name to an IP address, it
caches the IP address for a specified period of time, known as the
_time-to-live_ (TTL).

Because AWS resources use DNS name entries that occasionally change, we recommend that you configure your JVM with a TTL value of
no more than 60 seconds. Doing this makes sure that when a resource's IP address changes, your application can receive
and use the resource's new IP address by requerying the DNS.

On some Java configurations, the JVM default TTL is set so that it never refreshes DNS entries until the JVM is restarted. Thus, if
the IP address for an AWS resource changes while your application is still running, it can't use that resource until
you manually restart the JVM and the cached IP information is refreshed. In this case, it's crucial to set the
JVM's TTL so that it periodically refreshes its cached IP information.

###### Note

The default TTL can vary according to the version of your JVM and whether a security
manager is installed. Many JVMs provide a default TTL less than 60 seconds. If
you're using such a JVM and not using a security manager, you can ignore
the rest of this topic. For more information on security managers in Oracle, see
[The security manager](https://docs.oracle.com/javase/tutorial/essential/environment/security.html "https://docs.oracle.com/javase/tutorial/essential/environment/security.html") in the Oracle documentation.

To modify the JVM's TTL, set the [`networkaddress.cache.ttl`](https://docs.oracle.com/javase/7/docs/technotes/guides/net/properties.html "https://docs.oracle.com/javase/7/docs/technotes/guides/net/properties.html") property value. Use one of the following methods, depending on your
needs:

- To set the property value globally for all applications that use the JVM, set `networkaddress.cache.ttl` in the
  `$JAVA_HOME/jre/lib/security/java.security` file.

```
networkaddress.cache.ttl=60
```

- To set the property locally for your application only, set `networkaddress.cache.ttl` in your application's
  initialization code before any network connections are established.

```
java.security.Security.setProperty("networkaddress.cache.ttl" , "60");
```
