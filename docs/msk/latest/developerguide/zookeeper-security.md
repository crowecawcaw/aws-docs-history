# Control access to Apache ZooKeeper nodes in your Amazon MSK cluster

For security reasons you can limit access to the Apache ZooKeeper nodes that are part of
your Amazon MSK cluster. To limit access to the nodes, you can assign a separate security group to them. You can then decide who gets access to that security group.

###### Important

This section does not apply for clusters running in KRaft mode. See [KRaft mode](metadata-management.md#kraft-intro "metadata-management.md#kraft-intro").

###### This topic contains the following sections:

- [To place your Apache ZooKeeper nodes in a separate security group](zookeeper-security-group.md "zookeeper-security-group.md")
- [Using TLS security with Apache ZooKeeper](zookeeper-security-tls.md "zookeeper-security-tls.md")
