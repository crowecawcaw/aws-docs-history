

# Using the Primary Endpoint for Amazon RDS for Oracle

The *Primary Endpoint* is a DNS endpoint that always resolves to the current primary DB instance in an Oracle replica configuration. When the primary role moves to another DB instance, in the same AWS Region or a different Region, the Primary Endpoint automatically resolves to the new primary. Your application does not need a connection-string change when the primary role moves.

The primary DB instance and all of its replicas share the same Primary Endpoint. When you promote a replica to a standalone DB instance, it gets its own Primary Endpoint.

**Topics**
+ [Availability and provisioning](#oracle-primary-endpoint.availability)
+ [Finding the Primary Endpoint](#oracle-primary-endpoint.finding)
+ [How the Primary Endpoint behaves](#oracle-primary-endpoint.behavior)
+ [Connection considerations](#oracle-primary-endpoint.considerations)

## Availability and provisioning
<a name="oracle-primary-endpoint.availability"></a>

The Primary Endpoint is available for DB instances with Oracle Enterprise Edition. The Primary Endpoint follows the primary role between a DB instance and its replicas, and Amazon RDS for Oracle supports replicas only on Enterprise Edition. For this reason, Standard Edition 2 (SE2) doesn't support the Primary Endpoint. Every DB instance with Oracle Enterprise Edition has a Primary Endpoint. You don't have to create it, and it's available at no additional charge.

The Primary Endpoint is provided in addition to the instance endpoint. You can update your connection strings to use the Primary Endpoint whenever you're ready.

## Finding the Primary Endpoint
<a name="oracle-primary-endpoint.finding"></a>

You can find the Primary Endpoint for a DB instance by using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon RDS API.

The DNS name of the Primary Endpoint has the following format, where the host label is a 32-character hexadecimal string:

```
rds-0123456789abcdef0123456789abcdef.primary.rds.amazonaws.com
```

The Primary Endpoint uses the same port as the DB instance. As with the instance endpoint, this is the port that's configured for the DB instance (for example, 1521 for Oracle). Specify this port in your connection string.

### Console
<a name="oracle-primary-endpoint.finding.console"></a>

**To find the Primary Endpoint using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the console, choose the AWS Region of your DB instance.

1. Find the Primary Endpoint and port number for your DB instance.

   1. Choose **Databases** to display a list of your DB instances.

   1. Choose the Oracle DB instance name to display the instance details.

   1. On the **Connectivity & security** tab, for **Connect using**, choose **Endpoints**.

   1. Under **Primary Endpoint**, copy the endpoint. Also, note the port number under **Endpoint & port**. You need both the Primary Endpoint and the port number to connect to the current primary DB instance.  
![The Primary Endpoint of a DB instance under Primary Endpoint on the Connectivity & security tab.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/OracleConnect2.png)

### AWS CLI
<a name="oracle-primary-endpoint.finding.cli"></a>

To find the Primary Endpoint of an Oracle DB instance by using the AWS CLI, call the [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) command.

**Example To find the Primary Endpoint using the AWS CLI**  

```
aws rds describe-db-instances --db-instance-identifier {{myinstance}}
```
Search for `PrimaryEndpoint` in the output. The `Address` line contains the DNS name of the Primary Endpoint. The port for both endpoints is the instance port (`Endpoint.Port`). The following is an example of the JSON output.  

```
{
    "DBInstances": [
        {
            "DBInstanceIdentifier": "myinstance",
            "Endpoint": {
                "Address": "myinstance.123456789012.us-west-2.rds.amazonaws.com",
                "Port": 1521,
                "HostedZoneId": "Z1PVIF0B656C1W"
            },
            "PrimaryEndpoint": {
                "Address": "rds-0123456789abcdef0123456789abcdef.primary.rds.amazonaws.com",
                "HostedZoneId": "Z0123456789ABCDEFGHIJ"
            }
        }
    ]
}
```

### Amazon RDS API
<a name="oracle-primary-endpoint.finding.api"></a>

To find the Primary Endpoint of an Oracle DB instance by using the Amazon RDS API, call the [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) operation. The Primary Endpoint appears in the response under the `PrimaryEndpoint` field, which contains the endpoint `Address` and the Amazon Route 53 `HostedZoneId`.

## How the Primary Endpoint behaves
<a name="oracle-primary-endpoint.behavior"></a>

The following list describes what happens to the Primary Endpoint during a switchover, a promotion, a Multi-AZ failover, and other operations.

Switchover  
When you switch over to a replica in the same Region or a different Region, Amazon RDS updates the Primary Endpoint to point to that replica, which becomes the new primary DB instance. After the switchover completes, new connections through the Primary Endpoint go to the new primary, with no connection-string change. The switchover closes existing connections, and your application must reconnect to the new primary DB instance. The Primary Endpoint does not preserve open sessions or in-flight work. For more information, see [Performing an Oracle Data Guard switchover](oracle-replication-switchover.md).

Promotion  
When you promote a replica, it stops replicating and becomes a standalone DB instance with its own new Primary Endpoint. The primary DB instance and its other replicas keep the original Primary Endpoint. Because promotion is permanent, applications that connect to the promoted DB instance must use its new Primary Endpoint.

Multi-AZ failover  
During a Multi-AZ failover, the Primary Endpoint continues to resolve to the current primary DB instance. Continue using the same endpoint, so you don't need to change your connection string.

Deleting read replicas  
Deleting a replica doesn't affect the Primary Endpoint, even if you delete all of them. The Primary Endpoint keeps pointing to the primary DB instance until you delete the primary DB instance. When you delete a primary DB instance that still has replicas, Amazon RDS promotes each replica to a standalone DB instance, and each one gets its own new Primary Endpoint.

SSL/TLS certificates  
When Amazon RDS creates the Primary Endpoint, it regenerates the SSL/TLS certificate of each DB instance in the replica configuration to include the Primary Endpoint DNS name as a subject alternative name (SAN). When you promote a replica, Amazon RDS regenerates its certificate to include its new Primary Endpoint. This way, you get valid SSL/TLS host name verification through the Primary Endpoint without managing your own certificates. For more information about using SSL/TLS with Amazon RDS, see [Using SSL/TLS to encrypt a connection to a DB instance or cluster ](UsingWithRDS.SSL.md).

Restoring from a snapshot or point-in-time recovery (PITR)  
When you restore a DB instance from a snapshot or using point-in-time recovery (PITR), the restored DB instance gets a new Primary Endpoint. The exception is a restore in the same AWS account and AWS Region that uses the original DB instance identifier. In that case, the restored DB instance gets the same Primary Endpoint as the original DB instance, so you don't need to change your connection strings.  
Amazon RDS can't keep the original Primary Endpoint if another DB instance is still using it. For example, if you rename the original DB instance, the Primary Endpoint stays with that instance. If you then restore using the original identifier, Amazon RDS assigns a new Primary Endpoint instead.

## Connection considerations
<a name="oracle-primary-endpoint.considerations"></a>

Because the Primary Endpoint resolves to different DB instances over time, your client must perform a fresh DNS lookup to detect a change after a switchover. Clients and connection pools that cache DNS results might continue to try the previous primary until the cached entry expires. To make sure that your client resolves to the Primary Endpoint, set the DNS time-to-live (TTL) in your client to a low value, such as 60 seconds. For Java virtual machine (JVM) TTL guidance, see [Setting the JVM TTL for DNS name lookups](Concepts.MultiAZ.Failover.md#Concepts.MultiAZ.Failover.Java-DNS).

Design your application to reconnect after a switchover. A switchover closes existing connections, so your application must detect the dropped connection and reconnect through the Primary Endpoint. Connection pools that validate connections before use recover automatically because they perform a fresh DNS lookup for the Primary Endpoint when they create new connections.

During a switchover, Amazon RDS points the Primary Endpoint to the new primary DB instance. A switchover requires both the primary DB instance and the replica to be available. If the primary DB instance is unavailable in an unplanned event, use [promote-read-replica](https://docs.aws.amazon.com/cli/latest/reference/rds/promote-read-replica.html) to promote a replica instead. The promoted DB instance becomes a standalone DB instance with its own new Primary Endpoint, so you must update your application connection string to use it.

**Note**  
If you switch over to a cross-Region replica, the Primary Endpoint points to a DB instance in another AWS Region. Applications that stay in the original Region then connect across Regions, which adds network latency.