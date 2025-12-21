Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Troubleshooting connection issues in

Amazon Redshift

If you have issues with connecting to your cluster from a SQL client tool, there are
several things that you can check to narrow down the problem. If you are using SSL or
server certificates, first remove this complexity while you troubleshoot the connection
issue. Then add this back when you have found a solution. For more information, see
[Configuring security options for
connections](connecting-ssl-support.md "connecting-ssl-support.md").

For information about behavior changes in Amazon Redshift functionality that may affect your application, see
[Behavior changes in Amazon Redshift](behavior-changes.md "behavior-changes.md").

###### Important

Amazon Redshift has changed the way that SSL certificates are managed. If you have trouble
connecting using SSL, you might need to update your current trust root CA
certificates. For more information, see [Transitioning to ACM
certificates for SSL connections](connecting-transitioning-to-acm-certs.md "connecting-transitioning-to-acm-certs.md").

The following section has some example error messages and possible solutions for
connection issues. Because different SQL client tools provide different error messages,
this is not a complete list, but should be a good starting point for troubleshooting
issues.

## Connecting from outside

of Amazon EC2 and encountering a firewall timeout issue

Your client connection to the database appears to hang or timeout when
running long queries, such as a COPY command. In this case, you might observe
that the Amazon Redshift console displays that the query has completed, but the client
tool itself still appears to be running the query. The results of the query
might be missing or incomplete depending on when the connection stopped.

### Possible

solutions

This issue happens when you connect to Amazon Redshift from a machine other than an
Amazon EC2 instance. In this case, idle connections are terminated by an intermediate
network component, such as a firewall, after a period of inactivity. This
behavior is typical when you log on from a virtual private network (VPN) or your
local network.

To avoid these timeouts, we recommend the following changes:

- Increase client system values that deal with TCP/IP timeouts. Make
  these changes on the computer you are using to connect to your cluster.
  The timeout period should be adjusted for your client and network. For
  more information, see [Change
  TCP/IP timeout settings](#connecting-firewall-guidance.change-tcpip-settings "#connecting-firewall-guidance.change-tcpip-settings").
- Optionally, set keepalive behavior at the DSN level. For more
  information, see [Change DSN
  timeout settings](#connecting-firewall-guidance.change-dsn-settings "#connecting-firewall-guidance.change-dsn-settings").

### Change

TCP/IP timeout settings

To change TCP/IP timeout settings, configure the timeout settings according to
the operating system that you use to connect to your cluster.

- Linux — If your client is running on Linux, run the following
  command as the root user to change the timeout settings for the current
  session:

```
/sbin/sysctl -w net.ipv4.tcp_keepalive_time=200 net.ipv4.tcp_keepalive_intvl=200 net.ipv4.tcp_keepalive_probes=5
```

To persist the settings, create or modify the file
`/etc/sysctl.conf` with the following values then reboot
your system.

```
net.ipv4.tcp_keepalive_time=200
net.ipv4.tcp_keepalive_intvl=200
net.ipv4.tcp_keepalive_probes=5
```

- Windows — If your client runs on Windows, edit the values for
  the following registry settings under
  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\:

      + KeepAliveTime: 30000
      + KeepAliveInterval: 1000
      + TcpMaxDataRetransmissions: 10

  These settings use the DWORD data type. If they do not exist under the
  registry path, you can create the settings and specify these recommended
  values. For more information about editing the Windows registry, refer
  to Windows documentation.

After you set these values, restart your computer for the changes to
take effect.

- Mac — If your client is running on a Mac, run the following
  commands to change the timeout settings for the current session:

```
sudo sysctl net.inet.tcp.keepintvl=200000
sudo sysctl net.inet.tcp.keepidle=200000
sudo sysctl net.inet.tcp.keepinit=200000
sudo sysctl net.inet.tcp.always_keepalive=1
```

To persist the settings, create or modify the file
`/etc/sysctl.conf` with the following values:

```
net.inet.tcp.keepidle=200000
net.inet.tcp.keepintvl=200000
net.inet.tcp.keepinit=200000
net.inet.tcp.always_keepalive=1
```

Restart your computer, and then run the following commands to verify
that the values are set.

```
sysctl net.inet.tcp.keepidle
sysctl net.inet.tcp.keepintvl
sysctl net.inet.tcp.keepinit
sysctl net.inet.tcp.always_keepalive
```

### Change DSN

timeout settings

You can set keepalive behavior at the DSN level if you choose. You do this by
adding or modifying the following parameters in the odbc.ini file:

**KeepAlivesCount**

The number of TCP keepalive packets that can be lost before the
connection is considered broken.

**KeepAlivesIdle**

The number of seconds of inactivity before the driver sends a TCP
keepalive packet.

**KeepAlivesInterval**

The number of seconds between each TCP keepalive
retransmission.

If these parameters don't exist, or if they have a value of 0, the system
uses the keepalive parameters specified for TCP/IP to determine DSN keepalive
behavior. On Windows, you can find the TCP/IP parameters in the registry in
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\`.
On Linux and macOS, you can find the TCP/IP parameters can be found in the
sysctl.conf file.

## Connection is refused or

fails

When your connection if refused or fails, you may receive an error similar to one of the following.

- "Failed to establish a connection to
  `<endpoint>`."
- "Could not connect to server: Connection timed out. Is the server running
  on host `'<endpoint>'` and accepting TCP/IP
  connections on port `'<port>'`?"
- "Connection refused. Check that the hostname and port are correct and that
  the postmaster is accepting TCP/IP connections."

### Possible

solutions

Generally, when you receive an error message indicating that there is a failure to
establish a connection, it is an issue with permission to access the cluster or with
network traffic reaching the cluster.

To connect to the cluster from a client tool outside of the network that the
cluster is in, you add a inbound rule to the cluster's security group. The rule
configuration depends on whether the Amazon Redshift cluster is created in a virtual private
cloud (VPC):

- If you created the Amazon Redshift cluster in a virtual private cloud (VPC) based
  on Amazon VPC, add an inbound rule to the VPC security group that specifies the
  client CIDR/IP address, in Amazon VPC. For more information about configuring the
  VPC security groups for your cluster and publicly accessible options, see
  [Redshift resources in a VPC](managing-clusters-vpc.md "managing-clusters-vpc.md").
- If you created your Amazon Redshift cluster outside a VPC, add your client
  CIDR/IP address to the cluster security group in Amazon Redshift. For more
  information about configuring cluster security groups, see [Amazon Redshift security groups](security-network-isolation.md#working-with-security-groups "security-network-isolation.md#working-with-security-groups").

If you attempt to connect to the cluster from a client tool that runs on an Amazon EC2
instance, you also add an inbound rule. In this case, add a rule to the cluster
security group. The rule must specify the Amazon EC2 security group associated with the
client tool's Amazon EC2 instance.

In some cases, you might have a layer between your client and server, such as a
firewall. In these cases, make sure that the firewall accepts inbound connections
over the port that you configured for your cluster.

## Client and driver are

incompatible

If your client and driver are incompatible, you may receive an error that says, "The specified DSN contains an architecture mismatch between the Driver and
Application."

### Possible

solutions

When you attempt to connect and get an error about an architecture mismatch, this
means that the client tool and the driver aren't compatible. This occurs
because their system architecture doesn't match. For example, this can happen
if you have a 32-bit client tool but have installed the 64-bit version of the
driver. Sometimes 64-bit client tools can use 32-bit drivers, but you can't use
32-bit applications with 64-bit drivers. Make sure that the driver and client tool
are using the same version of the system architecture.

## Queries appear to hang and sometimes fail

to reach the cluster

You experience an issue with queries completing, where the queries appear to be
running but hang in the SQL client tool. Sometimes the queries fail to appear in the
cluster, such as in system tables or the Amazon Redshift console.

### Possible

solutions

This issue can happen due to packet drop. In this case, there is a difference in
the maximum transmission unit (MTU) size in the network path between two Internet
Protocol (IP) hosts. The MTU size determines the maximum size, in bytes, of a packet
that can be transferred in one Ethernet frame over a network connection. In AWS,
some Amazon EC2 instance types support an MTU of 1500 (Ethernet v2 frames) and other
instance types support an MTU of 9001 (TCP/IP jumbo frames).

To avoid issues that can occur with differences in MTU size, we recommend doing
one of the following:

- If your cluster uses the EC2-VPC platform, configure the Amazon VPC security
  group with an inbound custom Internet Control Message Protocol (ICMP) rule
  that returns `Destination Unreachable`. The rule thus instructs
  the originating host to use the lowest MTU size along the network path. For
  details on this approach, see [Configuring security groups to allow
  ICMP "destination unreachable"](#configure-custom-icmp "#configure-custom-icmp").
- If your cluster uses the EC2-Classic platform, or you can't allow the
  ICMP inbound rule, disable TCP/IP jumbo frames so that Ethernet v2 frames
  are used. For details on this approach, see [Configuring the MTU of an instance](#set-mtu "#set-mtu").

### Configuring security groups to allow

ICMP "destination unreachable"

When there is a difference in the MTU size in the network between two hosts,
first make sure that your network settings don't block path MTU discovery
(PMTUD). PMTUD enables the receiving host to respond to the originating host
with the following ICMP message: `Destination Unreachable: fragmentation
 needed and DF set (ICMP Type 3, Code 4)`. This message instructs the
originating host to use the lowest MTU size along the network path to resend the
request. Without this negotiation, packet drop can occur because the request is
too large for the receiving host to accept. For more information about this ICMP
message, go to [RFC792](http://tools.ietf.org/html/rfc792 "http://tools.ietf.org/html/rfc792") on
the _Internet Engineering Task Force (IETF)_ website.

If you don't explicitly configure this ICMP inbound rule for your Amazon VPC
security group, PMTUD is blocked. In AWS, security groups are virtual
firewalls that specify rules for inbound and outbound traffic to an instance.
For information about Amazon Redshift cluster security group, see [Amazon Redshift security groups](security-network-isolation.md#working-with-security-groups "security-network-isolation.md#working-with-security-groups"). For clusters using the
EC2-VPC platform, Amazon Redshift uses VPC security groups to allow or deny traffic to the
cluster. By default, the security groups are locked down and deny all inbound
traffic. For information about how to set inbound and outbound rules for
EC2-Classic or EC2-VPC instances, see [Differences between instances in EC2-Classic and a VPC](../../../AWSEC2/latest/UserGuide/ec2-classic-platform.md#ec2_classic_platform "../../../AWSEC2/latest/UserGuide/ec2-classic-platform.md#ec2_classic_platform") in the
_Amazon EC2 User Guide_.

For more information about how to add rules to VPC security groups, see [VPC security groups](managing-vpc-security-groups.md "managing-vpc-security-groups.md"). For more information about
specific PMTUD settings required in this rule, see [Path MTU
discovery](../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery "../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery") in the _Amazon EC2 User Guide._

### Configuring the MTU of an instance

In some cases, your cluster might use the EC2-Classic platform or you
can't allow the custom ICMP rule for inbound traffic. In these cases, we
recommend that you adjust the MTU to 1500 on the network interface (NIC) of the
EC2 instances you connect to your Amazon Redshift cluster from. This adjustment disables
TCP/IP jumbo frames to ensure that connections consistently use the same packet
size. However, this option reduces your maximum network throughput for the
instance entirely, not just for connections to Amazon Redshift. For more information, see
the following procedures.

###### To set MTU on a Microsoft Windows operating

system

If your client runs in a Microsoft Windows operating system, you can
review and set the MTU value for the Ethernet adapter by using the
`netsh` command.

1. Run the following command to determine the current MTU value:

```
netsh interface ipv4 show subinterfaces
```

2. Review the `MTU` value for the `Ethernet`
   adapter in the output.
3. If the value is not `1500`, run the following command to
   set it:

```
netsh interface ipv4 set subinterface "Ethernet" mtu=1500 store=persistent
```

After you set this value, restart your computer for the changes to
take effect.

###### To set MTU on a Linux operating

system

If your client runs in a Linux operating system, you can review and set
the MTU value by using the `ip` command.

1. Run the following command to determine the current MTU value:

```
$ ip link show eth0
```

2. Review the value following `mtu` in the output.
3. If the value is not `1500`, run the following command to
   set it:

```
$ sudo ip link set dev eth0 mtu 1500
```

###### To set MTU on a Mac operating system

- Follow instructions on the MacOS support site about `How to
change the MTU for troubleshooting purposes`. For more
  information, search the [support
  site.](https://support.apple.com "https://support.apple.com")

## Setting the JDBC fetch size parameter

By default, the Redshift JDBC driver uses a ring buffer to manage memory efficiently
and prevent out-of-memory errors. The fetch size parameter is only applicable when the
ring buffer is explicitly disabled. For more information, review the [link](jdbc20-configuration-options.md#jdbc20-enablefetchringbuffer-option "jdbc20-configuration-options.md#jdbc20-enablefetchringbuffer-option").
In this configuration, you should set the fetch size to control how many rows are retrieved in each batch.

###### When to Use Fetch Size?

Use the fetch size parameter when:

- You need fine-grained control over row-based batching
- Working with legacy applications that require traditional fetch size behavior

###### Setting Fetch Size

When ring buffer is disabled, the JDBC driver collects all results for a query at one time by default.
Queries that return large result sets can consume excessive memory. To retrieve
result sets in batches instead of all at once, set the JDBC fetch size parameter in your application.

###### Note

Fetch size is not supported for ODBC.

For the best performance, set the fetch size to the highest value that does not lead
to out of memory errors. A lower fetch size value results in more server trips, which
prolong execution times. The server reserves resources, including the WLM query slot and
associated memory, until the client retrieves the entire result set or the query is
canceled. When you tune the fetch size appropriately, those resources are released more
quickly, making them available to other queries.

###### Note

If you need to extract large datasets, we recommend using an
[UNLOAD](../dg/r_UNLOAD.md "../dg/r_UNLOAD.md")
statement to transfer the data to
Amazon S3. When you use UNLOAD, the compute nodes work in parallel to speed up the
transfer of data.

For more information about setting the JDBC fetch size parameter, go to [Getting results based on a cursor](https://jdbc.postgresql.org/documentation/query/#getting-results-based-on-a-cursor "https://jdbc.postgresql.org/documentation/query/#getting-results-based-on-a-cursor") in the PostgreSQL documentation.
