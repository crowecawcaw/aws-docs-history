# Imds properties for login nodes

Access to the login node's IMDS (and the instance profile credentials) is restricted to root user, cluster administrative user (`pc-cluster-admin`by default) and operating system
specific default user (`ec2-user`on Amazon Linux 2 and RedHat, and `ubuntu`on Ubuntu 18.04.

To restrict IMDS access, AWS ParallelCluster manages a chain of`iptables`.

###### Note

Any customization of`iptables`or`ip6tables`rules can interfere with the mechanism used to restrict IMDS access on the login node.See
also [Imds property setting](HeadNode-v3.md#HeadNode-v3-Imds "HeadNode-v3.md#HeadNode-v3-Imds").
