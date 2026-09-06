

# Local write forwarding in Aurora PostgreSQL
<a name="aurora-postgresql-write-forwarding"></a>

 *Local (in-cluster) write forwarding* allows your applications to issue read/write transactions directly on an Aurora Replica. The write commands are then forwarded to the writer DB instance to be committed. You can use local write forwarding for your applications that have occasional writes and require *read-after-write consistency*, which is the ability to read the latest write in a transaction. 

 Without write forwarding, your applications must fully split all read and write traffic, maintaining two sets of database connections to send the traffic to the appropriate endpoint. Read replicas receive updates asynchronously from the writer instance. In addition, because replication lag can differ among read replicas, achieving global read consistency across all replicas is difficult. You must transact any reads requiring read-after-write consistency on the writer database instance. Alternatively, you would need to develop complex custom application logic to take advantage of multiple read replicas for scalability while ensuring consistency. 

 With write forwarding, you avoid the need to split those transactions or send them exclusively to the writer instance. You also don't have to develop complex application logic to achieve *read-after-write consistency* consistency. 

 Local write forwarding is available in every Region where Aurora PostgreSQL is available. It is supported in the following Aurora PostgreSQL versions: 
+ 16.4 and higher 16 versions
+ 15.8 and higher 15 versions
+ 14.13 and higher 14 versions

 Local write forwarding is used to forward writes from in-Region replicas. To forward writes from a global replica, see [Using write forwarding in an Amazon Aurora global database](aurora-global-database-write-forwarding.md). 

**Topics**
+ [Limitations and considerations of local write forwarding in Aurora PostgreSQL](aurora-postgresql-write-forwarding-limitations.md)
+ [Configuring Aurora PostgreSQL for Local write forwarding](aurora-postgresql-write-forwarding-configuring.md)
+ [Working with local write forwarding for Aurora PostgreSQL](aurora-postgresql-write-forwarding-understanding.md)
+ [Monitoring local write forwarding in Aurora PostgreSQL](aurora-postgresql-write-forwarding-monitoring.md)