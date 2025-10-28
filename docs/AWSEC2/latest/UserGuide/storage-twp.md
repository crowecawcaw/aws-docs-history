# Torn write prevention on Amazon EC2 Linux instances

###### Note

Torn write prevention is supported with Linux instances only.

Torn write prevention is a block storage feature designed by AWS to improve the performance
of your I/O-intensive relational database workloads and reduce latency without negatively impacting
data resiliency. Relational databases that use InnoDB or XtraDB as the database engine, such as
MySQL and MariaDB, will benefit from torn write prevention.

Typically, relational databases that use pages larger than the _power fail
atomicity_ of the storage device use _data logging_ mechanisms
to protect against torn writes. MariaDB and MySQL use a _doublewrite buffer_
file to log data before writing it to data tables. In the event of incomplete or torn writes,
as a result of operating system crashes or power loss during write transactions, the database
can recover the data from the doublewrite buffer. The additional I/O overhead associated with
writing to the doublewrite buffer impacts database performance and application latency, and it
reduces the number transactions that can be processed per second. For more information about
doublewrite buffer, see the [MariaDB](https://mariadb.com/kb/en/innodb-doublewrite-buffer/ "https://mariadb.com/kb/en/innodb-doublewrite-buffer/") and [MySQL](https://dev.mysql.com/doc/refman/5.7/en/innodb-doublewrite-buffer.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-doublewrite-buffer.html") documentation.

With _torn write prevention_, data is written to storage in
_all-or-nothing_ write transactions, which eliminates the need for using
the doublewrite buffer. This prevents partial, or torn, data from being written to storage in
the event of operating system crashes or power loss during write transactions. The number of
transactions processed per second can be increased by up to 30 percent, and write latency can be
decreased by up to 50 percent, without compromising the resiliency of your workloads.

###### Pricing

There are no additional costs for using torn write prevention.

###### Contents

- [Supported block sizes](supported-block-sizes.md "supported-block-sizes.md")
- [Requirements](twp-reqs.md "twp-reqs.md")
- [Check instance support](twp-namespace.md "twp-namespace.md")
- [Configure workload](configure-twp.md "configure-twp.md")
