

# Torn write prevention on Amazon EC2 Linux instances
<a name="storage-twp"></a>

**Note**  
Torn write prevention is supported for Linux instances only.

Torn write prevention is a block storage feature designed by AWS to improve the performance of your I/O-intensive relational database workloads and reduce latency without negatively impacting data resiliency. Relational databases that use InnoDB or XtraDB as the database engine, such as MySQL and MariaDB, will benefit from torn write prevention.

Typically, relational databases that use pages larger than the *power fail atomicity* of the storage device use *data logging* mechanisms to protect against torn writes. MariaDB and MySQL use a *doublewrite buffer* file to log data before writing it to data tables. In the event of incomplete or torn writes, as a result of operating system crashes or power loss during write transactions, the database can recover the data from the doublewrite buffer. The additional I/O overhead associated with writing to the doublewrite buffer impacts database performance and application latency, and it reduces the number transactions that can be processed per second. For more information about doublewrite buffer, see the [ MariaDB](https://mariadb.com/kb/en/innodb-doublewrite-buffer/) and [ MySQL](https://dev.mysql.com/doc/refman/5.7/en/innodb-doublewrite-buffer.html) documentation.

With *torn write prevention*, data is written to storage in *all-or-nothing* write transactions, which eliminates the need for using the doublewrite buffer. This prevents partial, or torn, data from being written to storage in the event of operating system crashes or power loss during write transactions. The number of transactions processed per second can be increased by up to 30 percent, and write latency can be decreased by up to 50 percent, without compromising the resiliency of your workloads.

**Pricing**  
There are no additional costs for using torn write prevention.

**Topics**
+ [Supported block sizes](supported-block-sizes.md)
+ [Requirements](twp-reqs.md)
+ [Check instance support](twp-namespace.md)
+ [Configure workload](configure-twp.md)