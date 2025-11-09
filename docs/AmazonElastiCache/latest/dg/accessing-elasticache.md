# Accessing your ElastiCache cluster or replication group

Your Amazon ElastiCache instances are designed to be accessed through an Amazon EC2 instance.

If you launched your ElastiCache instance in an Amazon Virtual Private Cloud (Amazon VPC), you can access your ElastiCache
instance from an Amazon EC2 instance in the same Amazon VPC. Or, by using VPC peering, you can
access your ElastiCache instance from an Amazon EC2 in a different Amazon VPC.

If you launched your ElastiCache instance in EC2 Classic,
you allow the EC2 instance to access your cluster by granting the Amazon EC2 security group
associated with the instance access to your cache security group.
By default, access to a cluster is restricted to the account that launched the cluster.

###### Topics

- [Grant access to your cluster or replication group](#grant-access "#grant-access")

## Grant access to your cluster or replication group

### You launched your cluster into EC2-VPC

If you launched your cluster into an Amazon Virtual Private Cloud (Amazon VPC), you can connect to your ElastiCache
cluster only from an Amazon EC2 instance that is running in the same Amazon VPC.
In this case, you will need to grant network ingress to the cluster.

###### Note

If your are using _Local Zones_, make sure you have enabled it. For more information, see [Enable Local Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#opt-in-local-zone "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#opt-in-local-zone").
By doing so, your VPC is extended to that Local Zone and your VPC will treat the subnet as any subnet in any other Availability Zone and relevant gateways, route tables and other security group considerations. will be automatically adjusted.

###### To grant network ingress from an Amazon VPC security group to a cluster

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Network & Security**, choose
   **Security Groups**.
3. From the list of security groups, choose the security group for your Amazon VPC.
   Unless you created a security group for ElastiCache use,
   this security group will be named _default_.
4. Choose the **Inbound** tab, and then do
   the following:
   1. Choose **Edit**.
   2. Choose **Add rule**.
   3. In the **Type** column, choose **Custom TCP
      rule**.
   4. In the **Port range** box, type the port number for your cluster
      node. This number must be the same one that you specified when you
      launched the cluster.
      The default port for Memcached is `11211`
      The default port for Valkey and Redis OSS is `6379`.
   5. In the **Source** box, choose **Anywhere**
      which has the port range (0.0.0.0/0) so that any Amazon EC2 instance that you
      launch within your Amazon VPC can connect to your ElastiCache nodes.

   ###### Important

   Opening up the ElastiCache cluster to 0.0.0.0/0 does not expose the cluster to the Internet
   because it has no public IP address and therefore cannot be accessed from outside the VPC.
   However, the default security group may be applied to other Amazon EC2 instances in the customer’s account,
   and those instances may have a public IP address.
   If they happen to be running something on the default port,
   then that service could be exposed unintentionally.
   Therefore, we recommend creating a VPC Security Group that will be used exclusively by ElastiCache.
   For more information, see [Custom Security Groups](../../../AWSEC2/latest/UserGuide/using-network-security.md#creating-your-own-security-groups "../../../AWSEC2/latest/UserGuide/using-network-security.md#creating-your-own-security-groups"). 6. Choose **Save**.

When you launch an Amazon EC2 instance into your Amazon VPC, that instance will be able to connect to
your ElastiCache cluster.

### Accessing ElastiCache resources from outside AWS

Amazon ElastiCache is an AWS service that provides cloud-based in-memory key-value store.
The service is designed to be accessed exclusively from within AWS.
However, if the ElastiCache cluster is hosted inside a VPC,
you can use a Network Address Translation (NAT) instance
to provide outside access.

#### Requirements

The following requirements must be met for you to access your
ElastiCache resources from outside AWS:

- The cluster must reside within a VPC and be accessed through a Network Address Translation
  (NAT) instance.
  There are no exceptions to this requirement.
- The NAT instance must be launched in the same VPC as the cluster.
- The NAT instance must be launched in a public subnet separate from the cluster.
- An Elastic IP Address (EIP) must be associated with the NAT instance.
  The port forwarding feature of iptables is used to forward a port on the NAT instance
  to the cache node port within the VPC.

#### Considerations

The following considerations should be kept in mind when accessing your
ElastiCache resources from outside ElastiCache.

- Clients connect to the EIP and cache port of the NAT instance.
  Port forwarding on the NAT instance forwards traffic to the appropriate cluster node.
- If a cluster node is added or replaced, the iptables rules need to be updated to reflect this change.

#### Limitations

This approach should be used for testing and development purposes only.
It is not recommended for production use due to the following limitations:

- The NAT instance is acting as a proxy between clients and multiple clusters.
  The addition of a proxy impacts the performance of the cluster.
  The impact increases with number of clusters you are accessing through the NAT instance.
- The traffic from clients to the NAT instance is unencrypted.
  Therefore, you should avoid sending sensitive data via the NAT instance.
- The NAT instance adds the overhead of maintaining another instance.
- The NAT instance serves as a single point of failure.
  For information about how to set up high availability NAT on VPC, see [High Availability for Amazon VPC NAT Instances: An Example](https://aws.amazon.com/articles/2781451301784570 "https://aws.amazon.com/articles/2781451301784570").

#### How to access ElastiCache resources from outside AWS

The following procedure demonstrates how to connect to your ElastiCache resources
using a NAT instance.

These steps assume the following:

- `iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 6380 -j DNAT --to 10.0.1.231:6379`
- `iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 6381 -j DNAT --to 10.0.1.232:6379`

Next you need NAT in the opposite direction:

`iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to-source 10.0.0.55`

You also need to enable IP forwarding, which is disabled by default:

`sudo sed -i 's/net.ipv4.ip_forward=0/net.ipv4.ip_forward=1/g' /etc/sysctl.conf

sudo sysctl --system`

- You are accessing a Memcached cluster with:
  - IP address – _10.0.1.230_
  - Default Memcached port – _11211_
  - Security group – \*\*10\.0\.0\.55\*\*

- You are accessing a Valkey or Redis OSS cluster with:
  - IP address – _10.0.1.230_
  - Default port – _6379_
  - Security group – _sg-bd56b7da_
  - AWS instance IP address – _198.99.100.27_

- Your trusted client has the IP address _198.51.100.27_.
- Your NAT instance has the Elastic IP Address _203.0.113.73_.
- Your NAT instance has security group _sg-ce56b7a9_.

###### To connect to your ElastiCache resources using a NAT instance

1. Create a NAT instance in the same VPC as your cluster but in a public subnet.

By default, the VPC wizard will launch a _cache.m1.small_ node type.
You should select a node size based on your needs. You must use EC2 NAT AMI to be able to access ElastiCache from outside AWS.

For information about creating a NAT instance, see [NAT Instances](../../../AmazonVPC/latest/UserGuide/VPC_NAT_Instance.md "../../../AmazonVPC/latest/UserGuide/VPC_NAT_Instance.md") in the AWS VPC User Guide. 2. Create security group rules for the cluster and NAT instance.

The NAT instance security group and the cluster instance should have the following rules:

    * Two inbound rules




    	+ With Memcached, the first rule is to allow TCP connections from trusted clients to each cache port
    	 forwarded from the NAT instance (11211 - 11213).
    	+ With Valkey and Redis OSS, the first rule is to allow TCP connections from trusted clients to each cache port
    	 forwarded from the NAT instance (6379 - 6381).
    	+ A second rule to allow SSH access to trusted clients.


    NAT instance security group - inbound rules with Memcached| Type | Protocol | Port range | Source |
    | --- | --- | --- | --- |
    | Custom TCP Rule | TCP | 11211-11213 | 198.51.100.27/32 |
    | SSH | TCP | 22 | 198.51.100.27/32 |




    NAT instance security group - inbound rules with Valkey or Redis OSS| Type | Protocol | Port range | Source |
    | --- | --- | --- | --- |
    | Custom TCP Rule | TCP | 6379-6380 | 198.51.100.27/32 |
    | SSH | TCP | 22 | 203.0.113.73/32 |
    * With Memcached, an outbound rule to allow TCP connections to cache port (11211).




    NAT instance security group - outbound rule| Type | Protocol | Port range | Destination |
    | --- | --- | --- | --- |
    | Custom TCP Rule | TCP | 11211 | sg-ce56b7a9<br>(NAT Security Group) |
    * With Valkey or Redis OSS, an outbound rule to allow TCP connections to cache port (6379).




    NAT instance security group - outbound rule| Type | Protocol | Port range | Destination |
    | --- | --- | --- | --- |
    | Custom TCP Rule | TCP | 6379 | sg-ce56b7a9<br>(NAT Security Group) |
    * With Memcached, an inbound rule for the cluster's security group
     that allows TCP connections from the NAT instance to
     the cache port (11211).




    Cluster instance security group - inbound rule| Type | Protocol | Port range | Source |
    | --- | --- | --- | --- |
    | Custom TCP Rule | TCP | 11211 | sg-ce56b7a9 (NAT Security Group) |
    * With Valkey or Redis OSS, an inbound rule for the cluster's security group
     that allows TCP connections from the NAT instance to
     the cache port (6379).




    Cluster instance security group - inbound rule| Type | Protocol | Port range | Source |
    | --- | --- | --- | --- |
    | Custom TCP Rule | TCP | 6379 | sg-ce56b7a9 (NAT Security Group) |

3. Validate the rules.
   - Confirm that the trusted client is able to SSH to the NAT instance.
   - Confirm that the trusted client is able to connect to the cluster from the NAT instance.

4. **Memcached**

Add an iptables rule to the NAT instance.

An iptables rule must be added to the NAT table for each node in the cluster
to forward the cache port from the NAT instance to the cluster node.
An example might look like the following:

```
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 11211 -j DNAT --to 10.0.1.230:11211
```

The port number must be unique for each node in the cluster.
For example, if working with a three node Memcached cluster using ports 11211 - 11213,
the rules would look like the following:

```
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 11211 -j DNAT --to 10.0.1.230:11211
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 11212 -j DNAT --to 10.0.1.231:11211
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 11213 -j DNAT --to 10.0.1.232:11211
```

Confirm that the trusted client is able to connect to the cluster.

The trusted client should connect to the EIP associated with the NAT instance and
the cluster port corresponding to the appropriate cluster node.
For example, the connection string for PHP might look like the following:

```
$memcached->connect( '203.0.113.73', 11211 );
$memcached->connect( '203.0.113.73', 11212 );
$memcached->connect( '203.0.113.73', 11213 );
```

A telnet client can also be used to verify the connection. For example:

```
telnet 203.0.113.73 11211
telnet 203.0.113.73 11212
telnet 203.0.113.73 11213
```

**Valkey or Redis OSS**

Add an iptables rule to the NAT instance.

An iptables rule must be added to the NAT table for each node in the cluster
to forward the cache port from the NAT instance to the cluster node.
An example might look like the following:

```
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 6379 -j DNAT --to 10.0.1.230:6379
```

The port number must be unique for each node in the cluster.
For example, if working with a three node Redis OSS cluster using ports 6379 - 6381,
the rules would look like the following:

```
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 6379 -j DNAT --to 10.0.1.230:6379
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 6380 -j DNAT --to 10.0.1.231:6379
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 6381 -j DNAT --to 10.0.1.232:6379
```

Confirm that the trusted client is able to connect to the cluster.

The trusted client should connect to the EIP associated with the NAT instance and
the cluster port corresponding to the appropriate cluster node.
For example, the connection string for PHP might look like the following:

```
redis->connect( '203.0.113.73', 6379 );
redis->connect( '203.0.113.73', 6380 );
redis->connect( '203.0.113.73', 6381 );
```

A telnet client can also be used to verify the connection. For example:

```
telnet 203.0.113.73 6379
telnet 203.0.113.73 6380
telnet 203.0.113.73 6381
```

5. Save the iptables configuration.

Save the rules after you test and verify them.
If you are using a Redhat-based Linux distribution (like Amazon Linux),
run the following command:

```
service iptables save
```

#### Related topics

The following topics may be of additional interest.

- [Access Patterns for Accessing an ElastiCache Cache in an Amazon VPC](elasticache-vpc-accessing.md "elasticache-vpc-accessing.md")
- [Accessing an ElastiCache Cache from an Application Running in a Customer's Data Center](elasticache-vpc-accessing.md#elasticache-vpc-accessing-data-center "elasticache-vpc-accessing.md#elasticache-vpc-accessing-data-center")
- [NAT Instances](../../../AmazonVPC/latest/UserGuide/VPC_NAT_Instance.md "../../../AmazonVPC/latest/UserGuide/VPC_NAT_Instance.md")
- [Configuring ElastiCache Clients](ClientConfig.md "ClientConfig.md")
- [High Availability for Amazon VPC NAT Instances: An Example](https://aws.amazon.com/articles/2781451301784570 "https://aws.amazon.com/articles/2781451301784570")
