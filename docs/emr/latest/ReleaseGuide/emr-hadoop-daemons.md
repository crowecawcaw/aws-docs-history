# Hadoop daemon configuration settings

Hadoop daemon settings are different depending on the EC2 instance type that a
cluster node uses. The following tables list the default configuration settings for
each EC2 instance type.

To customize these settings, use the `hadoop-env` configuration
classification. For more information, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

###### Instance Types

- [c1 instances](#emr-hadoop-daemons-c1 "#emr-hadoop-daemons-c1")
- [c3 instances](#emr-hadoop-daemons-c3 "#emr-hadoop-daemons-c3")
- [c4 instances](#emr-hadoop-daemons-c4 "#emr-hadoop-daemons-c4")
- [c5 instances](#emr-hadoop-daemons-c5 "#emr-hadoop-daemons-c5")
- [c5a instances](#emr-hadoop-daemons-c5a "#emr-hadoop-daemons-c5a")
- [c5ad instances](#emr-hadoop-daemons-c5ad "#emr-hadoop-daemons-c5ad")
- [c5d instances](#emr-hadoop-daemons-c5d "#emr-hadoop-daemons-c5d")
- [c5n instances](#emr-hadoop-daemons-c5n "#emr-hadoop-daemons-c5n")
- [c6a instances](#emr-hadoop-daemons-c6a "#emr-hadoop-daemons-c6a")
- [c6g instances](#emr-hadoop-daemons-c6g "#emr-hadoop-daemons-c6g")
- [c6gd instances](#emr-hadoop-daemons-c6gd "#emr-hadoop-daemons-c6gd")
- [c6gn instances](#emr-hadoop-daemons-c6gn "#emr-hadoop-daemons-c6gn")
- [c6i instances](#emr-hadoop-daemons-c6i "#emr-hadoop-daemons-c6i")
- [c6id instances](#emr-hadoop-daemons-c6id "#emr-hadoop-daemons-c6id")
- [c6in instances](#emr-hadoop-daemons-c6in "#emr-hadoop-daemons-c6in")
- [c7a instances](#emr-hadoop-daemons-c7a "#emr-hadoop-daemons-c7a")
- [c7g instances](#emr-hadoop-daemons-c7g "#emr-hadoop-daemons-c7g")
- [c7gd instances](#emr-hadoop-daemons-c7gd "#emr-hadoop-daemons-c7gd")
- [c7gn instances](#emr-hadoop-daemons-c7gn "#emr-hadoop-daemons-c7gn")
- [c7i instances](#emr-hadoop-daemons-c7i "#emr-hadoop-daemons-c7i")
- [c7i-flex instances](#emr-hadoop-daemons-c7i-flex "#emr-hadoop-daemons-c7i-flex")
- [c8g instances](#emr-hadoop-daemons-c8g "#emr-hadoop-daemons-c8g")
- [c8gd instances](#emr-hadoop-daemons-c8gd "#emr-hadoop-daemons-c8gd")
- [d2 instances](#emr-hadoop-daemons-d2 "#emr-hadoop-daemons-d2")
- [d3 instances](#emr-hadoop-daemons-d3 "#emr-hadoop-daemons-d3")
- [d3en instances](#emr-hadoop-daemons-d3en "#emr-hadoop-daemons-d3en")
- [f2 instances](#emr-hadoop-daemons-f2 "#emr-hadoop-daemons-f2")
- [g3 instances](#emr-hadoop-daemons-g3 "#emr-hadoop-daemons-g3")
- [g3s instances](#emr-hadoop-daemons-g3s "#emr-hadoop-daemons-g3s")
- [g4dn instances](#emr-hadoop-daemons-g4dn "#emr-hadoop-daemons-g4dn")
- [g5 instances](#emr-hadoop-daemons-g5 "#emr-hadoop-daemons-g5")
- [g6 instances](#emr-hadoop-daemons-g6 "#emr-hadoop-daemons-g6")
- [g6e instances](#emr-hadoop-daemons-g6e "#emr-hadoop-daemons-g6e")
- [gr6 instances](#emr-hadoop-daemons-gr6 "#emr-hadoop-daemons-gr6")
- [h1 instances](#emr-hadoop-daemons-h1 "#emr-hadoop-daemons-h1")
- [i2 instances](#emr-hadoop-daemons-i2 "#emr-hadoop-daemons-i2")
- [i3 instances](#emr-hadoop-daemons-i3 "#emr-hadoop-daemons-i3")
- [i3en instances](#emr-hadoop-daemons-i3en "#emr-hadoop-daemons-i3en")
- [i4g instances](#emr-hadoop-daemons-i4g "#emr-hadoop-daemons-i4g")
- [i4i instances](#emr-hadoop-daemons-i4i "#emr-hadoop-daemons-i4i")
- [i7i instances](#emr-hadoop-daemons-i7i "#emr-hadoop-daemons-i7i")
- [i7ie instances](#emr-hadoop-daemons-i7ie "#emr-hadoop-daemons-i7ie")
- [i8g instances](#emr-hadoop-daemons-i8g "#emr-hadoop-daemons-i8g")
- [im4gn instances](#emr-hadoop-daemons-im4gn "#emr-hadoop-daemons-im4gn")
- [is4gen instances](#emr-hadoop-daemons-is4gen "#emr-hadoop-daemons-is4gen")
- [m1 instances](#emr-hadoop-daemons-m1 "#emr-hadoop-daemons-m1")
- [m2 instances](#emr-hadoop-daemons-m2 "#emr-hadoop-daemons-m2")
- [m3 instances](#emr-hadoop-daemons-m3 "#emr-hadoop-daemons-m3")
- [m4 instances](#emr-hadoop-daemons-m4 "#emr-hadoop-daemons-m4")
- [m5 instances](#emr-hadoop-daemons-m5 "#emr-hadoop-daemons-m5")
- [m5a instances](#emr-hadoop-daemons-m5a "#emr-hadoop-daemons-m5a")
- [m5ad instances](#emr-hadoop-daemons-m5ad "#emr-hadoop-daemons-m5ad")
- [m5d instances](#emr-hadoop-daemons-m5d "#emr-hadoop-daemons-m5d")
- [m5dn instances](#emr-hadoop-daemons-m5dn "#emr-hadoop-daemons-m5dn")
- [m5n instances](#emr-hadoop-daemons-m5n "#emr-hadoop-daemons-m5n")
- [m5zn instances](#emr-hadoop-daemons-m5zn "#emr-hadoop-daemons-m5zn")
- [m6a instances](#emr-hadoop-daemons-m6a "#emr-hadoop-daemons-m6a")
- [m6g instances](#emr-hadoop-daemons-m6g "#emr-hadoop-daemons-m6g")
- [m6gd instances](#emr-hadoop-daemons-m6gd "#emr-hadoop-daemons-m6gd")
- [m6i instances](#emr-hadoop-daemons-m6i "#emr-hadoop-daemons-m6i")
- [m6id instances](#emr-hadoop-daemons-m6id "#emr-hadoop-daemons-m6id")
- [m6idn instances](#emr-hadoop-daemons-m6idn "#emr-hadoop-daemons-m6idn")
- [m6in instances](#emr-hadoop-daemons-m6in "#emr-hadoop-daemons-m6in")
- [m7a instances](#emr-hadoop-daemons-m7a "#emr-hadoop-daemons-m7a")
- [m7g instances](#emr-hadoop-daemons-m7g "#emr-hadoop-daemons-m7g")
- [m7gd instances](#emr-hadoop-daemons-m7gd "#emr-hadoop-daemons-m7gd")
- [m7i instances](#emr-hadoop-daemons-m7i "#emr-hadoop-daemons-m7i")
- [m7i-flex instances](#emr-hadoop-daemons-m7i-flex "#emr-hadoop-daemons-m7i-flex")
- [m8g instances](#emr-hadoop-daemons-m8g "#emr-hadoop-daemons-m8g")
- [m8gd instances](#emr-hadoop-daemons-m8gd "#emr-hadoop-daemons-m8gd")
- [p2 instances](#emr-hadoop-daemons-p2 "#emr-hadoop-daemons-p2")
- [p3 instances](#emr-hadoop-daemons-p3 "#emr-hadoop-daemons-p3")
- [p4d instances](#emr-hadoop-daemons-p4d "#emr-hadoop-daemons-p4d")
- [p5 instances](#emr-hadoop-daemons-p5 "#emr-hadoop-daemons-p5")
- [r3 instances](#emr-hadoop-daemons-r3 "#emr-hadoop-daemons-r3")
- [r4 instances](#emr-hadoop-daemons-r4 "#emr-hadoop-daemons-r4")
- [r5 instances](#emr-hadoop-daemons-r5 "#emr-hadoop-daemons-r5")
- [r5a instances](#emr-hadoop-daemons-r5a "#emr-hadoop-daemons-r5a")
- [r5ad instances](#emr-hadoop-daemons-r5ad "#emr-hadoop-daemons-r5ad")
- [r5b instances](#emr-hadoop-daemons-r5b "#emr-hadoop-daemons-r5b")
- [r5d instances](#emr-hadoop-daemons-r5d "#emr-hadoop-daemons-r5d")
- [r5dn instances](#emr-hadoop-daemons-r5dn "#emr-hadoop-daemons-r5dn")
- [r5n instances](#emr-hadoop-daemons-r5n "#emr-hadoop-daemons-r5n")
- [r6a instances](#emr-hadoop-daemons-r6a "#emr-hadoop-daemons-r6a")
- [r6g instances](#emr-hadoop-daemons-r6g "#emr-hadoop-daemons-r6g")
- [r6gd instances](#emr-hadoop-daemons-r6gd "#emr-hadoop-daemons-r6gd")
- [r6i instances](#emr-hadoop-daemons-r6i "#emr-hadoop-daemons-r6i")
- [r6id instances](#emr-hadoop-daemons-r6id "#emr-hadoop-daemons-r6id")
- [r6idn instances](#emr-hadoop-daemons-r6idn "#emr-hadoop-daemons-r6idn")
- [r6in instances](#emr-hadoop-daemons-r6in "#emr-hadoop-daemons-r6in")
- [r7a instances](#emr-hadoop-daemons-r7a "#emr-hadoop-daemons-r7a")
- [r7g instances](#emr-hadoop-daemons-r7g "#emr-hadoop-daemons-r7g")
- [r7gd instances](#emr-hadoop-daemons-r7gd "#emr-hadoop-daemons-r7gd")
- [r7i instances](#emr-hadoop-daemons-r7i "#emr-hadoop-daemons-r7i")
- [r7iz instances](#emr-hadoop-daemons-r7iz "#emr-hadoop-daemons-r7iz")
- [r8g instances](#emr-hadoop-daemons-r8g "#emr-hadoop-daemons-r8g")
- [r8gd instances](#emr-hadoop-daemons-r8gd "#emr-hadoop-daemons-r8gd")
- [x1 instances](#emr-hadoop-daemons-x1 "#emr-hadoop-daemons-x1")
- [x1e instances](#emr-hadoop-daemons-x1e "#emr-hadoop-daemons-x1e")
- [x2gd instances](#emr-hadoop-daemons-x2gd "#emr-hadoop-daemons-x2gd")
- [x2idn instances](#emr-hadoop-daemons-x2idn "#emr-hadoop-daemons-x2idn")
- [x2iedn instances](#emr-hadoop-daemons-x2iedn "#emr-hadoop-daemons-x2iedn")
- [x8g instances](#emr-hadoop-daemons-x8g "#emr-hadoop-daemons-x8g")
- [z1d instances](#emr-hadoop-daemons-z1d "#emr-hadoop-daemons-z1d")

## c1 instances

| c1.medium                         | Parameter | Value                                 |
| --------------------------------- | --------- | ------------------------------------- | --------- | ----- |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 192       |
| YARN_PROXYSERVER_HEAPSIZE         | 96        |
| YARN_NODEMANAGER_HEAPSIZE         | 128       |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 128       |
| HADOOP_NAMENODE_HEAPSIZE          | 192       |
| HADOOP_DATANODE_HEAPSIZE          | 96        | c1.xlarge                             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 768       |
| YARN_PROXYSERVER_HEAPSIZE         | 384       |
| YARN_NODEMANAGER_HEAPSIZE         | 512       |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 512       |
| HADOOP_NAMENODE_HEAPSIZE          | 768       |
| HADOOP_DATANODE_HEAPSIZE          | 384       | ## c3 instances c3.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c3.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2396      |
| YARN_PROXYSERVER_HEAPSIZE         | 2396      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2396      |
| HADOOP_NAMENODE_HEAPSIZE          | 1740      |
| HADOOP_DATANODE_HEAPSIZE          | 757       | c3.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2703      |
| YARN_PROXYSERVER_HEAPSIZE         | 2703      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2703      |
| HADOOP_NAMENODE_HEAPSIZE          | 3276      |
| HADOOP_DATANODE_HEAPSIZE          | 1064      | c3.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3317      |
| YARN_PROXYSERVER_HEAPSIZE         | 3317      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3317      |
| HADOOP_NAMENODE_HEAPSIZE          | 6348      |
| HADOOP_DATANODE_HEAPSIZE          | 1679      | ## c4 instances c4.large              | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 1152      |
| YARN_PROXYSERVER_HEAPSIZE         | 1152      |
| YARN_NODEMANAGER_HEAPSIZE         | 1152      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 1152      |
| HADOOP_NAMENODE_HEAPSIZE          | 576       |
| HADOOP_DATANODE_HEAPSIZE          | 384       | c4.xlarge                             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c4.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2396      |
| YARN_PROXYSERVER_HEAPSIZE         | 2396      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2396      |
| HADOOP_NAMENODE_HEAPSIZE          | 1740      |
| HADOOP_DATANODE_HEAPSIZE          | 757       | c4.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2703      |
| YARN_PROXYSERVER_HEAPSIZE         | 2703      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2703      |
| HADOOP_NAMENODE_HEAPSIZE          | 3276      |
| HADOOP_DATANODE_HEAPSIZE          | 1064      | c4.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3317      |
| YARN_PROXYSERVER_HEAPSIZE         | 3317      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3317      |
| HADOOP_NAMENODE_HEAPSIZE          | 6348      |
| HADOOP_DATANODE_HEAPSIZE          | 1679      | ## c5 instances c5.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2252      |
| YARN_PROXYSERVER_HEAPSIZE         | 2252      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2252      |
| HADOOP_NAMENODE_HEAPSIZE          | 1024      |
| HADOOP_DATANODE_HEAPSIZE          | 614       | c5.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2416      |
| YARN_PROXYSERVER_HEAPSIZE         | 2416      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2416      |
| HADOOP_NAMENODE_HEAPSIZE          | 1843      |
| HADOOP_DATANODE_HEAPSIZE          | 778       | c5.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | c5.9xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3563      |
| YARN_PROXYSERVER_HEAPSIZE         | 3563      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3563      |
| HADOOP_NAMENODE_HEAPSIZE          | 7577      |
| HADOOP_DATANODE_HEAPSIZE          | 1925      | c5.12xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4055      |
| YARN_PROXYSERVER_HEAPSIZE         | 4055      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4055      |
| HADOOP_NAMENODE_HEAPSIZE          | 10035     |
| HADOOP_DATANODE_HEAPSIZE          | 2416      | c5.18xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5038      |
| YARN_PROXYSERVER_HEAPSIZE         | 5038      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5038      |
| HADOOP_NAMENODE_HEAPSIZE          | 14950     |
| HADOOP_DATANODE_HEAPSIZE          | 3399      | c5.24xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6021      |
| YARN_PROXYSERVER_HEAPSIZE         | 6021      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6021      |
| HADOOP_NAMENODE_HEAPSIZE          | 19865     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c5a instances c5a.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c5a.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c5a.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c5a.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c5a.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4055      |
| YARN_PROXYSERVER_HEAPSIZE         | 4055      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4055      |
| HADOOP_NAMENODE_HEAPSIZE          | 10035     |
| HADOOP_DATANODE_HEAPSIZE          | 2416      | c5a.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c5a.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c5ad instances c5ad.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c5ad.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c5ad.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c5ad.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c5ad.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c5ad.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c5ad.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c5d instances c5d.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2252      |
| YARN_PROXYSERVER_HEAPSIZE         | 2252      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2252      |
| HADOOP_NAMENODE_HEAPSIZE          | 1024      |
| HADOOP_DATANODE_HEAPSIZE          | 614       | c5d.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2416      |
| YARN_PROXYSERVER_HEAPSIZE         | 2416      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2416      |
| HADOOP_NAMENODE_HEAPSIZE          | 1843      |
| HADOOP_DATANODE_HEAPSIZE          | 778       | c5d.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | c5d.9xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3563      |
| YARN_PROXYSERVER_HEAPSIZE         | 3563      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3563      |
| HADOOP_NAMENODE_HEAPSIZE          | 7577      |
| HADOOP_DATANODE_HEAPSIZE          | 1925      | c5d.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4055      |
| YARN_PROXYSERVER_HEAPSIZE         | 4055      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4055      |
| HADOOP_NAMENODE_HEAPSIZE          | 10035     |
| HADOOP_DATANODE_HEAPSIZE          | 2416      | c5d.18xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5038      |
| YARN_PROXYSERVER_HEAPSIZE         | 5038      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5038      |
| HADOOP_NAMENODE_HEAPSIZE          | 14950     |
| HADOOP_DATANODE_HEAPSIZE          | 3399      | c5d.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6021      |
| YARN_PROXYSERVER_HEAPSIZE         | 6021      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6021      |
| HADOOP_NAMENODE_HEAPSIZE          | 19865     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c5n instances c5n.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2304      |
| YARN_PROXYSERVER_HEAPSIZE         | 2304      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2304      |
| HADOOP_NAMENODE_HEAPSIZE          | 1280      |
| HADOOP_DATANODE_HEAPSIZE          | 665       | c5n.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2519      |
| YARN_PROXYSERVER_HEAPSIZE         | 2519      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2519      |
| HADOOP_NAMENODE_HEAPSIZE          | 2355      |
| HADOOP_DATANODE_HEAPSIZE          | 880       | c5n.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2949      |
| YARN_PROXYSERVER_HEAPSIZE         | 2949      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2949      |
| HADOOP_NAMENODE_HEAPSIZE          | 4505      |
| HADOOP_DATANODE_HEAPSIZE          | 1310      | c5n.9xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4055      |
| YARN_PROXYSERVER_HEAPSIZE         | 4055      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4055      |
| HADOOP_NAMENODE_HEAPSIZE          | 10035     |
| HADOOP_DATANODE_HEAPSIZE          | 2416      | c5n.18xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6021      |
| YARN_PROXYSERVER_HEAPSIZE         | 6021      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6021      |
| HADOOP_NAMENODE_HEAPSIZE          | 19865     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c6a instances c6a.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c6a.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c6a.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c6a.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c6a.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c6a.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c6a.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c6a.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c6a.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c6g instances c6g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c6g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c6g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c6g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c6g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c6g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | ## c6gd instances c6gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c6gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c6gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c6gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c6gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c6gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | ## c6gn instances c6gn.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c6gn.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c6gn.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c6gn.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c6gn.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c6gn.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | ## c6i instances c6i.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c6i.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c6i.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c6i.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c6i.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c6i.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c6i.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c6i.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c6id instances c6id.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c6id.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c6id.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c6id.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c6id.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c6id.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c6id.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c6id.32xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c6in instances c6in.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c6in.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c6in.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c6in.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c6in.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c6in.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c6in.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c6in.32xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c7a instances c7a.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c7a.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c7a.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c7a.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c7a.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c7a.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c7a.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c7a.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c7a.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c7g instances c7g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c7g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c7g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c7g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c7g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c7g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | ## c7gd instances c7gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c7gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c7gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c7gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c7gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c7gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | ## c7gn instances c7gn.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c7gn.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c7gn.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c7gn.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c7gn.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c7gn.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | ## c7i instances c7i.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c7i.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c7i.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c7i.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c7i.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c7i.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c7i.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c7i.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c7i-flex instances c7i-flex.xlarge | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c7i-flex.2xlarge                      | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c7i-flex.4xlarge                      | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c7i-flex.8xlarge                      | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c7i-flex.12xlarge                     | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c7i-flex.16xlarge                     | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | ## c8g instances c8g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c8g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c8g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c8g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c8g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c8g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c8g.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c8g.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## c8gd instances c8gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2124      |
| YARN_PROXYSERVER_HEAPSIZE         | 2124      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2124      |
| HADOOP_NAMENODE_HEAPSIZE          | 972       |
| HADOOP_DATANODE_HEAPSIZE          | 588       | c8gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | c8gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | c8gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | c8gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | c8gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | c8gd.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | c8gd.48xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## d2 instances d2.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | d2.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | d2.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | d2.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## d3 instances d3.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | d3.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | d3.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | d3.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## d3en instances d3en.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | d3en.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | d3en.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | d3en.6xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | d3en.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | d3en.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## f2 instances f2.6xlarge            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | f2.12xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | f2.48xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 42065     |
| YARN_PROXYSERVER_HEAPSIZE         | 42065     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 42065     |
| HADOOP_NAMENODE_HEAPSIZE          | 200089    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## g3 instances g3.4xlarge            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | g3.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g3.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## g3s instances g3s.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | ## g4dn instances g4dn.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2416      |
| YARN_PROXYSERVER_HEAPSIZE         | 2416      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2416      |
| HADOOP_NAMENODE_HEAPSIZE          | 1843      |
| HADOOP_DATANODE_HEAPSIZE          | 778       | g4dn.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | g4dn.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | g4dn.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4710      |
| YARN_PROXYSERVER_HEAPSIZE         | 4710      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4710      |
| HADOOP_NAMENODE_HEAPSIZE          | 13312     |
| HADOOP_DATANODE_HEAPSIZE          | 3072      | g4dn.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6021      |
| YARN_PROXYSERVER_HEAPSIZE         | 6021      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6021      |
| HADOOP_NAMENODE_HEAPSIZE          | 19865     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g4dn.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7331      |
| YARN_PROXYSERVER_HEAPSIZE         | 7331      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7331      |
| HADOOP_NAMENODE_HEAPSIZE          | 26419     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## g5 instances g5.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | g5.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | g5.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | g5.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | g5.12xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g5.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g5.24xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g5.48xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## g6 instances g6.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2396      |
| YARN_PROXYSERVER_HEAPSIZE         | 2396      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2396      |
| HADOOP_NAMENODE_HEAPSIZE          | 1740      |
| HADOOP_DATANODE_HEAPSIZE          | 757       | g6.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2703      |
| YARN_PROXYSERVER_HEAPSIZE         | 2703      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2703      |
| HADOOP_NAMENODE_HEAPSIZE          | 3276      |
| HADOOP_DATANODE_HEAPSIZE          | 1064      | g6.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3317      |
| YARN_PROXYSERVER_HEAPSIZE         | 3317      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3317      |
| HADOOP_NAMENODE_HEAPSIZE          | 6348      |
| HADOOP_DATANODE_HEAPSIZE          | 1679      | g6.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4567      |
| YARN_PROXYSERVER_HEAPSIZE         | 4567      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4567      |
| HADOOP_NAMENODE_HEAPSIZE          | 12595     |
| HADOOP_DATANODE_HEAPSIZE          | 2928      | g6.12xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5795      |
| YARN_PROXYSERVER_HEAPSIZE         | 5795      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5795      |
| HADOOP_NAMENODE_HEAPSIZE          | 18739     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g6.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7045      |
| YARN_PROXYSERVER_HEAPSIZE         | 7045      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7045      |
| HADOOP_NAMENODE_HEAPSIZE          | 24985     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g6.24xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9543      |
| YARN_PROXYSERVER_HEAPSIZE         | 9543      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9543      |
| HADOOP_NAMENODE_HEAPSIZE          | 37478     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g6.48xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 16998     |
| YARN_PROXYSERVER_HEAPSIZE         | 16998     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 16998     |
| HADOOP_NAMENODE_HEAPSIZE          | 74752     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## g6e instances g6e.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | g6e.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | g6e.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | g6e.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g6e.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g6e.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g6e.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | g6e.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## gr6 instances gr6.4xlarge          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4567      |
| YARN_PROXYSERVER_HEAPSIZE         | 4567      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4567      |
| HADOOP_NAMENODE_HEAPSIZE          | 12595     |
| HADOOP_DATANODE_HEAPSIZE          | 2928      | gr6.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7045      |
| YARN_PROXYSERVER_HEAPSIZE         | 7045      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7045      |
| HADOOP_NAMENODE_HEAPSIZE          | 24985     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## h1 instances h1.2xlarge            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | h1.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | h1.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4710      |
| YARN_PROXYSERVER_HEAPSIZE         | 4710      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4710      |
| HADOOP_NAMENODE_HEAPSIZE          | 13312     |
| HADOOP_DATANODE_HEAPSIZE          | 3072      | h1.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7331      |
| YARN_PROXYSERVER_HEAPSIZE         | 7331      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7331      |
| HADOOP_NAMENODE_HEAPSIZE          | 26419     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## i2 instances i2.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | i2.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | i2.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | i2.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## i3 instances i3.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | i3.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | i3.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | i3.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i3.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## i3en instances i3en.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | i3en.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | i3en.3xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4055      |
| YARN_PROXYSERVER_HEAPSIZE         | 4055      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4055      |
| HADOOP_NAMENODE_HEAPSIZE          | 10035     |
| HADOOP_DATANODE_HEAPSIZE          | 2416      | i3en.6xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6021      |
| YARN_PROXYSERVER_HEAPSIZE         | 6021      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6021      |
| HADOOP_NAMENODE_HEAPSIZE          | 19865     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i3en.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9953      |
| YARN_PROXYSERVER_HEAPSIZE         | 9953      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9953      |
| HADOOP_NAMENODE_HEAPSIZE          | 39526     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i3en.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17817     |
| YARN_PROXYSERVER_HEAPSIZE         | 17817     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17817     |
| HADOOP_NAMENODE_HEAPSIZE          | 78848     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## i4g instances i4g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | i4g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | i4g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | i4g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i4g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## i4i instances i4i.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | i4i.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | i4i.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | i4i.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i4i.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i4i.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i4i.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i4i.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## i7i instances i7i.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | i7i.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | i7i.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | i7i.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i7i.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i7i.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i7i.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i7i.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## i7ie instances i7ie.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | i7ie.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | i7ie.3xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | i7ie.6xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i7ie.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i7ie.18xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 13332     |
| YARN_PROXYSERVER_HEAPSIZE         | 13332     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 13332     |
| HADOOP_NAMENODE_HEAPSIZE          | 56422     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i7ie.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i7ie.48xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## i8g instances i8g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | i8g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | i8g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | i8g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i8g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i8g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i8g.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | i8g.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## im4gn instances im4gn.xlarge       | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | im4gn.2xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | im4gn.4xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | im4gn.8xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | im4gn.16xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## is4gen instances is4gen.xlarge     | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2557      |
| YARN_PROXYSERVER_HEAPSIZE         | 2557      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2557      |
| HADOOP_NAMENODE_HEAPSIZE          | 2547      |
| HADOOP_DATANODE_HEAPSIZE          | 919       | is4gen.2xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3025      |
| YARN_PROXYSERVER_HEAPSIZE         | 3025      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3025      |
| HADOOP_NAMENODE_HEAPSIZE          | 4889      |
| HADOOP_DATANODE_HEAPSIZE          | 1387      | is4gen.4xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | is4gen.8xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m1 instances m1.small              | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 256       |
| YARN_PROXYSERVER_HEAPSIZE         | 96        |
| YARN_NODEMANAGER_HEAPSIZE         | 192       |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 128       |
| HADOOP_NAMENODE_HEAPSIZE          | 192       |
| HADOOP_DATANODE_HEAPSIZE          | 96        | m1.medium                             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 384       |
| YARN_PROXYSERVER_HEAPSIZE         | 192       |
| YARN_NODEMANAGER_HEAPSIZE         | 256       |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 256       |
| HADOOP_NAMENODE_HEAPSIZE          | 384       |
| HADOOP_DATANODE_HEAPSIZE          | 192       | m1.large                              | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 768       |
| YARN_PROXYSERVER_HEAPSIZE         | 384       |
| YARN_NODEMANAGER_HEAPSIZE         | 512       |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 512       |
| HADOOP_NAMENODE_HEAPSIZE          | 768       |
| HADOOP_DATANODE_HEAPSIZE          | 384       | m1.xlarge                             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 1024      |
| YARN_PROXYSERVER_HEAPSIZE         | 512       |
| YARN_NODEMANAGER_HEAPSIZE         | 768       |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 1024      |
| HADOOP_NAMENODE_HEAPSIZE          | 2304      |
| HADOOP_DATANODE_HEAPSIZE          | 384       | ## m2 instances m2.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 1536      |
| YARN_PROXYSERVER_HEAPSIZE         | 1024      |
| YARN_NODEMANAGER_HEAPSIZE         | 1024      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 1024      |
| HADOOP_NAMENODE_HEAPSIZE          | 3072      |
| HADOOP_DATANODE_HEAPSIZE          | 384       | m2.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 1536      |
| YARN_PROXYSERVER_HEAPSIZE         | 1024      |
| YARN_NODEMANAGER_HEAPSIZE         | 1024      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 1536      |
| HADOOP_NAMENODE_HEAPSIZE          | 6144      |
| HADOOP_DATANODE_HEAPSIZE          | 384       | m2.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2048      |
| YARN_PROXYSERVER_HEAPSIZE         | 1024      |
| YARN_NODEMANAGER_HEAPSIZE         | 1536      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 1536      |
| HADOOP_NAMENODE_HEAPSIZE          | 12288     |
| HADOOP_DATANODE_HEAPSIZE          | 384       | ## m3 instances m3.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2396      |
| YARN_PROXYSERVER_HEAPSIZE         | 2396      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2396      |
| HADOOP_NAMENODE_HEAPSIZE          | 1740      |
| HADOOP_DATANODE_HEAPSIZE          | 757       | m3.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2703      |
| YARN_PROXYSERVER_HEAPSIZE         | 2703      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2703      |
| HADOOP_NAMENODE_HEAPSIZE          | 3276      |
| HADOOP_DATANODE_HEAPSIZE          | 1064      | ## m4 instances m4.large              | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2252      |
| YARN_PROXYSERVER_HEAPSIZE         | 2252      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2252      |
| HADOOP_NAMENODE_HEAPSIZE          | 1024      |
| HADOOP_DATANODE_HEAPSIZE          | 614       | m4.xlarge                             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2416      |
| YARN_PROXYSERVER_HEAPSIZE         | 2416      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2416      |
| HADOOP_NAMENODE_HEAPSIZE          | 1843      |
| HADOOP_DATANODE_HEAPSIZE          | 778       | m4.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | m4.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | m4.10xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5365      |
| YARN_PROXYSERVER_HEAPSIZE         | 5365      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5365      |
| HADOOP_NAMENODE_HEAPSIZE          | 16588     |
| HADOOP_DATANODE_HEAPSIZE          | 3727      | m4.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7331      |
| YARN_PROXYSERVER_HEAPSIZE         | 7331      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7331      |
| HADOOP_NAMENODE_HEAPSIZE          | 26419     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m5 instances m5.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2416      |
| YARN_PROXYSERVER_HEAPSIZE         | 2416      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2416      |
| HADOOP_NAMENODE_HEAPSIZE          | 1843      |
| HADOOP_DATANODE_HEAPSIZE          | 778       | m5.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | m5.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | m5.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4710      |
| YARN_PROXYSERVER_HEAPSIZE         | 4710      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4710      |
| HADOOP_NAMENODE_HEAPSIZE          | 13312     |
| HADOOP_DATANODE_HEAPSIZE          | 3072      | m5.12xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6021      |
| YARN_PROXYSERVER_HEAPSIZE         | 6021      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6021      |
| HADOOP_NAMENODE_HEAPSIZE          | 19865     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7331      |
| YARN_PROXYSERVER_HEAPSIZE         | 7331      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7331      |
| HADOOP_NAMENODE_HEAPSIZE          | 26419     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5.24xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9953      |
| YARN_PROXYSERVER_HEAPSIZE         | 9953      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9953      |
| HADOOP_NAMENODE_HEAPSIZE          | 39526     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m5a instances m5a.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2416      |
| YARN_PROXYSERVER_HEAPSIZE         | 2416      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2416      |
| HADOOP_NAMENODE_HEAPSIZE          | 1843      |
| HADOOP_DATANODE_HEAPSIZE          | 778       | m5a.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | m5a.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | m5a.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4710      |
| YARN_PROXYSERVER_HEAPSIZE         | 4710      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4710      |
| HADOOP_NAMENODE_HEAPSIZE          | 13312     |
| HADOOP_DATANODE_HEAPSIZE          | 3072      | m5a.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6021      |
| YARN_PROXYSERVER_HEAPSIZE         | 6021      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6021      |
| HADOOP_NAMENODE_HEAPSIZE          | 19865     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5a.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7331      |
| YARN_PROXYSERVER_HEAPSIZE         | 7331      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7331      |
| HADOOP_NAMENODE_HEAPSIZE          | 26419     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5a.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9953      |
| YARN_PROXYSERVER_HEAPSIZE         | 9953      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9953      |
| HADOOP_NAMENODE_HEAPSIZE          | 39526     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m5ad instances m5ad.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m5ad.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m5ad.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m5ad.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m5ad.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5ad.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5ad.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m5d instances m5d.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2416      |
| YARN_PROXYSERVER_HEAPSIZE         | 2416      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2416      |
| HADOOP_NAMENODE_HEAPSIZE          | 1843      |
| HADOOP_DATANODE_HEAPSIZE          | 778       | m5d.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | m5d.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | m5d.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4710      |
| YARN_PROXYSERVER_HEAPSIZE         | 4710      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4710      |
| HADOOP_NAMENODE_HEAPSIZE          | 13312     |
| HADOOP_DATANODE_HEAPSIZE          | 3072      | m5d.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6021      |
| YARN_PROXYSERVER_HEAPSIZE         | 6021      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6021      |
| HADOOP_NAMENODE_HEAPSIZE          | 19865     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5d.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7331      |
| YARN_PROXYSERVER_HEAPSIZE         | 7331      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7331      |
| HADOOP_NAMENODE_HEAPSIZE          | 26419     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5d.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9953      |
| YARN_PROXYSERVER_HEAPSIZE         | 9953      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9953      |
| HADOOP_NAMENODE_HEAPSIZE          | 39526     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m5dn instances m5dn.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m5dn.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m5dn.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m5dn.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m5dn.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5dn.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5dn.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m5n instances m5n.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m5n.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m5n.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m5n.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m5n.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5n.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m5n.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m5zn instances m5zn.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2396      |
| YARN_PROXYSERVER_HEAPSIZE         | 2396      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2396      |
| HADOOP_NAMENODE_HEAPSIZE          | 1740      |
| HADOOP_DATANODE_HEAPSIZE          | 757       | m5zn.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m5zn.3xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3025      |
| YARN_PROXYSERVER_HEAPSIZE         | 3025      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3025      |
| HADOOP_NAMENODE_HEAPSIZE          | 4889      |
| HADOOP_DATANODE_HEAPSIZE          | 1387      | m5zn.6xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3962      |
| YARN_PROXYSERVER_HEAPSIZE         | 3962      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3962      |
| HADOOP_NAMENODE_HEAPSIZE          | 9574      |
| HADOOP_DATANODE_HEAPSIZE          | 2324      | m5zn.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m6a instances m6a.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m6a.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m6a.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m6a.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m6a.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6a.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6a.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6a.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6a.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m6g instances m6g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m6g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m6g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m6g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m6g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5877      |
| YARN_PROXYSERVER_HEAPSIZE         | 5877      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5877      |
| HADOOP_NAMENODE_HEAPSIZE          | 19148     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m6gd instances m6gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m6gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m6gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m6gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m6gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5877      |
| YARN_PROXYSERVER_HEAPSIZE         | 5877      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5877      |
| HADOOP_NAMENODE_HEAPSIZE          | 19148     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m6i instances m6i.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m6i.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m6i.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m6i.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m6i.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5877      |
| YARN_PROXYSERVER_HEAPSIZE         | 5877      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5877      |
| HADOOP_NAMENODE_HEAPSIZE          | 19148     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6i.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6i.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6i.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m6id instances m6id.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m6id.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m6id.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m6id.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m6id.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6id.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6id.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6id.32xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m6idn instances m6idn.xlarge       | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m6idn.2xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m6idn.4xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m6idn.8xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m6idn.12xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6idn.16xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6idn.24xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6idn.32xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m6in instances m6in.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m6in.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m6in.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m6in.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m6in.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5877      |
| YARN_PROXYSERVER_HEAPSIZE         | 5877      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5877      |
| HADOOP_NAMENODE_HEAPSIZE          | 19148     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6in.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6in.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m6in.32xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m7a instances m7a.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m7a.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m7a.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m7a.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m7a.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7a.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7a.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7a.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7a.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m7g instances m7g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m7g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m7g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m7g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m7g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m7gd instances m7gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m7gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m7gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m7gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m7gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m7i instances m7i.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m7i.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m7i.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m7i.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m7i.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5877      |
| YARN_PROXYSERVER_HEAPSIZE         | 5877      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5877      |
| HADOOP_NAMENODE_HEAPSIZE          | 19148     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7i.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7i.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7i.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m7i-flex instances m7i-flex.xlarge | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m7i-flex.2xlarge                      | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m7i-flex.4xlarge                      | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m7i-flex.8xlarge                      | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m7i-flex.12xlarge                     | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m7i-flex.16xlarge                     | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m8g instances m8g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m8g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m8g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m8g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m8g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5877      |
| YARN_PROXYSERVER_HEAPSIZE         | 5877      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5877      |
| HADOOP_NAMENODE_HEAPSIZE          | 19148     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m8g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m8g.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m8g.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## m8gd instances m8gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2401      |
| YARN_PROXYSERVER_HEAPSIZE         | 2401      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2401      |
| HADOOP_NAMENODE_HEAPSIZE          | 1766      |
| HADOOP_DATANODE_HEAPSIZE          | 762       | m8gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | m8gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | m8gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | m8gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 5836      |
| YARN_PROXYSERVER_HEAPSIZE         | 5836      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 5836      |
| HADOOP_NAMENODE_HEAPSIZE          | 18944     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m8gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m8gd.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | m8gd.48xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## p2 instances p2.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | p2.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | p2.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## p3 instances p3.2xlarge            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | p3.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | p3.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## p4d instances p4d.24xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 24576     |
| YARN_PROXYSERVER_HEAPSIZE         | 24576     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 24576     |
| HADOOP_NAMENODE_HEAPSIZE          | 112640    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## p5 instances p5.48xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 42065     |
| YARN_PROXYSERVER_HEAPSIZE         | 42065     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 42065     |
| HADOOP_NAMENODE_HEAPSIZE          | 200089    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r3 instances r3.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r3.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r3.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r3.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r4 instances r4.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r4.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r4.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r4.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r4.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r5 instances r5.xlarge             | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | r5.2xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | r5.4xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4710      |
| YARN_PROXYSERVER_HEAPSIZE         | 4710      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4710      |
| HADOOP_NAMENODE_HEAPSIZE          | 13312     |
| HADOOP_DATANODE_HEAPSIZE          | 3072      | r5.8xlarge                            | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7331      |
| YARN_PROXYSERVER_HEAPSIZE         | 7331      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7331      |
| HADOOP_NAMENODE_HEAPSIZE          | 26419     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5.12xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9953      |
| YARN_PROXYSERVER_HEAPSIZE         | 9953      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9953      |
| HADOOP_NAMENODE_HEAPSIZE          | 39526     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5.16xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12574     |
| YARN_PROXYSERVER_HEAPSIZE         | 12574     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12574     |
| HADOOP_NAMENODE_HEAPSIZE          | 52633     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5.24xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17817     |
| YARN_PROXYSERVER_HEAPSIZE         | 17817     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17817     |
| HADOOP_NAMENODE_HEAPSIZE          | 78848     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r5a instances r5a.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | r5a.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | r5a.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4710      |
| YARN_PROXYSERVER_HEAPSIZE         | 4710      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4710      |
| HADOOP_NAMENODE_HEAPSIZE          | 13312     |
| HADOOP_DATANODE_HEAPSIZE          | 3072      | r5a.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7331      |
| YARN_PROXYSERVER_HEAPSIZE         | 7331      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7331      |
| HADOOP_NAMENODE_HEAPSIZE          | 26419     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5a.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9953      |
| YARN_PROXYSERVER_HEAPSIZE         | 9953      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9953      |
| HADOOP_NAMENODE_HEAPSIZE          | 39526     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5a.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12574     |
| YARN_PROXYSERVER_HEAPSIZE         | 12574     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12574     |
| HADOOP_NAMENODE_HEAPSIZE          | 52633     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5a.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17817     |
| YARN_PROXYSERVER_HEAPSIZE         | 17817     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17817     |
| HADOOP_NAMENODE_HEAPSIZE          | 78848     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r5ad instances r5ad.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r5ad.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r5ad.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r5ad.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5ad.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5ad.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12247     |
| YARN_PROXYSERVER_HEAPSIZE         | 12247     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12247     |
| HADOOP_NAMENODE_HEAPSIZE          | 50995     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5ad.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r5b instances r5b.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r5b.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r5b.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r5b.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5b.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5b.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5b.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r5d instances r5d.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | r5d.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | r5d.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4710      |
| YARN_PROXYSERVER_HEAPSIZE         | 4710      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4710      |
| HADOOP_NAMENODE_HEAPSIZE          | 13312     |
| HADOOP_DATANODE_HEAPSIZE          | 3072      | r5d.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7331      |
| YARN_PROXYSERVER_HEAPSIZE         | 7331      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7331      |
| HADOOP_NAMENODE_HEAPSIZE          | 26419     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5d.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9953      |
| YARN_PROXYSERVER_HEAPSIZE         | 9953      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9953      |
| HADOOP_NAMENODE_HEAPSIZE          | 39526     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5d.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12574     |
| YARN_PROXYSERVER_HEAPSIZE         | 12574     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12574     |
| HADOOP_NAMENODE_HEAPSIZE          | 52633     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5d.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17817     |
| YARN_PROXYSERVER_HEAPSIZE         | 17817     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17817     |
| HADOOP_NAMENODE_HEAPSIZE          | 78848     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r5dn instances r5dn.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r5dn.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r5dn.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r5dn.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5dn.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5dn.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5dn.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r5n instances r5n.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r5n.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r5n.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r5n.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5n.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5n.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r5n.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r6a instances r6a.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r6a.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r6a.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r6a.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6a.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6a.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6a.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6a.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6a.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r6g instances r6g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r6g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r6g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r6g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r6gd instances r6gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r6gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r6gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r6gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r6i instances r6i.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r6i.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r6i.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r6i.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6i.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6i.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6i.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6i.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 21544     |
| YARN_PROXYSERVER_HEAPSIZE         | 21544     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 21544     |
| HADOOP_NAMENODE_HEAPSIZE          | 97484     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r6id instances r6id.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r6id.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r6id.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r6id.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6id.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6id.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6id.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6id.32xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r6idn instances r6idn.xlarge       | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r6idn.2xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r6idn.4xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r6idn.8xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6idn.12xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6idn.16xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6idn.24xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6idn.32xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r6in instances r6in.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r6in.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r6in.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r6in.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6in.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6in.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6in.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r6in.32xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r7a instances r7a.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r7a.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r7a.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r7a.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7a.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7a.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7a.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7a.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7a.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r7g instances r7g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r7g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r7g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r7g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r7gd instances r7gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r7gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r7gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r7gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r7i instances r7i.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r7i.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r7i.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r7i.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7i.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7i.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7i.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7i.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r7iz instances r7iz.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r7iz.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r7iz.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r7iz.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7iz.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7iz.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r7iz.32xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 21544     |
| YARN_PROXYSERVER_HEAPSIZE         | 21544     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 21544     |
| HADOOP_NAMENODE_HEAPSIZE          | 97484     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r8g instances r8g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r8g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r8g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r8g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r8g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r8g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r8g.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r8g.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## r8gd instances r8gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2713      |
| YARN_PROXYSERVER_HEAPSIZE         | 2713      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2713      |
| HADOOP_NAMENODE_HEAPSIZE          | 3328      |
| HADOOP_DATANODE_HEAPSIZE          | 1075      | r8gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | r8gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | r8gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r8gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9584      |
| YARN_PROXYSERVER_HEAPSIZE         | 9584      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9584      |
| HADOOP_NAMENODE_HEAPSIZE          | 37683     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r8gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r8gd.24xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | r8gd.48xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## x1 instances x1.16xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 21544     |
| YARN_PROXYSERVER_HEAPSIZE         | 21544     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 21544     |
| HADOOP_NAMENODE_HEAPSIZE          | 97484     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x1.32xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 41000     |
| YARN_PROXYSERVER_HEAPSIZE         | 41000     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 41000     |
| HADOOP_NAMENODE_HEAPSIZE          | 194764    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## x1e instances x1e.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4520      |
| YARN_PROXYSERVER_HEAPSIZE         | 4520      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4520      |
| HADOOP_NAMENODE_HEAPSIZE          | 12364     |
| HADOOP_DATANODE_HEAPSIZE          | 2882      | x1e.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6952      |
| YARN_PROXYSERVER_HEAPSIZE         | 6952      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6952      |
| HADOOP_NAMENODE_HEAPSIZE          | 24524     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x1e.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 11816     |
| YARN_PROXYSERVER_HEAPSIZE         | 11816     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 11816     |
| HADOOP_NAMENODE_HEAPSIZE          | 48844     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x1e.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 21544     |
| YARN_PROXYSERVER_HEAPSIZE         | 21544     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 21544     |
| HADOOP_NAMENODE_HEAPSIZE          | 97484     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x1e.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 41000     |
| YARN_PROXYSERVER_HEAPSIZE         | 41000     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 41000     |
| HADOOP_NAMENODE_HEAPSIZE          | 194764    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x1e.32xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 79912     |
| YARN_PROXYSERVER_HEAPSIZE         | 79912     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 79912     |
| HADOOP_NAMENODE_HEAPSIZE          | 389324    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## x2gd instances x2gd.xlarge         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | x2gd.2xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | x2gd.4xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2gd.8xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2gd.12xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2gd.16xlarge                         | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## x2idn instances x2idn.16xlarge     | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2idn.24xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2idn.32xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 42065     |
| YARN_PROXYSERVER_HEAPSIZE         | 42065     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 42065     |
| HADOOP_NAMENODE_HEAPSIZE          | 200089    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## x2iedn instances x2iedn.xlarge     | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | x2iedn.2xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2iedn.4xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2iedn.8xlarge                        | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2iedn.16xlarge                       | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 42065     |
| YARN_PROXYSERVER_HEAPSIZE         | 42065     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 42065     |
| HADOOP_NAMENODE_HEAPSIZE          | 200089    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2iedn.24xlarge                       | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 62054     |
| YARN_PROXYSERVER_HEAPSIZE         | 62054     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 62054     |
| HADOOP_NAMENODE_HEAPSIZE          | 300032    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x2iedn.32xlarge                       | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 82042     |
| YARN_PROXYSERVER_HEAPSIZE         | 82042     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 82042     |
| HADOOP_NAMENODE_HEAPSIZE          | 399974    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## x8g instances x8g.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3338      |
| YARN_PROXYSERVER_HEAPSIZE         | 3338      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3338      |
| HADOOP_NAMENODE_HEAPSIZE          | 6451      |
| HADOOP_DATANODE_HEAPSIZE          | 1699      | x8g.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4587      |
| YARN_PROXYSERVER_HEAPSIZE         | 4587      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4587      |
| HADOOP_NAMENODE_HEAPSIZE          | 12697     |
| HADOOP_DATANODE_HEAPSIZE          | 2949      | x8g.4xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 7086      |
| YARN_PROXYSERVER_HEAPSIZE         | 7086      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 7086      |
| HADOOP_NAMENODE_HEAPSIZE          | 25190     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x8g.8xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 12083     |
| YARN_PROXYSERVER_HEAPSIZE         | 12083     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 12083     |
| HADOOP_NAMENODE_HEAPSIZE          | 50176     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x8g.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 17080     |
| YARN_PROXYSERVER_HEAPSIZE         | 17080     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 17080     |
| HADOOP_NAMENODE_HEAPSIZE          | 75161     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x8g.16xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 22077     |
| YARN_PROXYSERVER_HEAPSIZE         | 22077     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 22077     |
| HADOOP_NAMENODE_HEAPSIZE          | 100147    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x8g.24xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 32071     |
| YARN_PROXYSERVER_HEAPSIZE         | 32071     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 32071     |
| HADOOP_NAMENODE_HEAPSIZE          | 150118    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | x8g.48xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 62054     |
| YARN_PROXYSERVER_HEAPSIZE         | 62054     |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 62054     |
| HADOOP_NAMENODE_HEAPSIZE          | 300032    |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | ## z1d instances z1d.xlarge           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 2744      |
| YARN_PROXYSERVER_HEAPSIZE         | 2744      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 2744      |
| HADOOP_NAMENODE_HEAPSIZE          | 3481      |
| HADOOP_DATANODE_HEAPSIZE          | 1105      | z1d.2xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 3399      |
| YARN_PROXYSERVER_HEAPSIZE         | 3399      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 3399      |
| HADOOP_NAMENODE_HEAPSIZE          | 6758      |
| HADOOP_DATANODE_HEAPSIZE          | 1761      | z1d.3xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 4055      |
| YARN_PROXYSERVER_HEAPSIZE         | 4055      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 4055      |
| HADOOP_NAMENODE_HEAPSIZE          | 10035     |
| HADOOP_DATANODE_HEAPSIZE          | 2416      | z1d.6xlarge                           | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 6021      |
| YARN_PROXYSERVER_HEAPSIZE         | 6021      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 6021      |
| HADOOP_NAMENODE_HEAPSIZE          | 19865     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      | z1d.12xlarge                          | Parameter | Value |
| ---                               | ---       |
| YARN_RESOURCEMANAGER_HEAPSIZE     | 9953      |
| YARN_PROXYSERVER_HEAPSIZE         | 9953      |
| YARN_NODEMANAGER_HEAPSIZE         | 2048      |
| HADOOP_JOB_HISTORYSERVER_HEAPSIZE | 9953      |
| HADOOP_NAMENODE_HEAPSIZE          | 39526     |
| HADOOP_DATANODE_HEAPSIZE          | 4096      |
