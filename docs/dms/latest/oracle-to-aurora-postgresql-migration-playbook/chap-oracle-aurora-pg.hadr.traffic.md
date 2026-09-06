

# Oracle Traffic Director and Amazon RDS Proxy for Amazon Aurora PostgreSQL
<a name="chap-oracle-aurora-pg.hadr.traffic"></a>

With AWS DMS, you can migrate Oracle Traffic Director to Amazon RDS Proxy for PostgreSQL to modernize your applications. Oracle Traffic Director is a web server that distributes client requests across origin servers, while Amazon RDS Proxy for PostgreSQL is a fully managed proxy for PostgreSQL databases.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-0.png)  | N/A | Some features may be replaced by Amazon RDS Proxy | 

## Oracle usage
<a name="chap-oracle-aurora-pg.hadr.traffic.ora"></a>

Starting with Oracle 18c Oracle Connection Manager can be configured to run in Traffic Director mode. This mode introduces multiple features that help with High Availability, scalability, load balancing, zero downtime and security. Oracle Traffic Director is fast and reliable load-balancing solution. By enabling it for Oracle Connection Manager users can now get following features:
+ Increased scalability through usage of transparent connection load-balancing.
+ Essential high availability feature of zero downtime that includes support for planned database maintenance, pluggable database relocation, and unplanned database outages for read-mostly workloads.
+ High availability of Connection Manager (CMAN) which avoids single point of failure
+ Various security features, such as database proxy, firewall, tenant isolation in multi-tenant environment, DDOS protection, and database traffic secure tunneling.

For more information, see [Configuring Oracle Connection Manager in Traffic Director Mode](https://docs.oracle.com/en/database/oracle/oracle-database/18/netag/configuring-oracle-connection-manager.html#GUID-3917FC5D-4B23-4752-85BA-39A88C4D13F8) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.hadr.traffic.pg"></a>

Oracle Traffic Director mode for Connection Manager can be potentially replaced by Amazon RDS Proxy for migration to Aurora PostgreSQL.

RDS Proxy simplifies connection management for Amazon RDS DB instances and clusters. It handles the network traffic between the client application and the database in an active way first by understanding the database protocol. Then Amazon RDS Proxy adjusts its behavior based on the SQL operations from user application and the result sets from the database.

RDS Proxy also reduces the memory and CPU overhead for the database connection management. The database needs less memory and CPU resources when applications open many simultaneous connections. Amazon RDS Proxy also doesn’t require applications to close and reopen connections that stay idle for a long time. Similarly, it requires less application logic to reestablish connections in case of a database problem.

The infrastructure for Amazon RDS Proxy is highly available and deployed over multiple Availability Zones (AZs). The computation, memory, and storage for Amazon RDS Proxy are independent of Amazon RDS DB instances and Aurora DB clusters. This separation helps lower overhead on database servers, so that they can devote their resources to serving database workloads. The Amazon RDS Proxy compute resources are serverless, automatically scaling based on your database workload.

For more information, see [Amazon RDS Proxy](chap-oracle-aurora-pg.tools.rdsproxy.md) and [Using Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) in the *Amazon RDS user guide*.