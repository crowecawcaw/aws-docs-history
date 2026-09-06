

# Working with Amazon EMR-managed security groups
<a name="emr-man-sec-groups"></a>

**Note**  
Amazon EMR aims to use inclusive alternatives for potentially offensive or non-inclusive industry terms such as "master" and "slave". We've transitioned to new terminology to foster a more inclusive experience and to facilitate your understanding of the service components.  
We now describe "nodes" as **instances**, and we describe Amazon EMR instance types as **primary**, **core**, and **task** instances. During the transition, you might still find legacy references to the outdated terms, such as those that pertain to security groups for Amazon EMR.

Different managed security groups are associated with the primary instance and with the core and task instances in a cluster. An additional managed security group for service access is required when you create a cluster in a private subnet. For more information about the role of managed security groups with respect to your network configuration, see [Amazon VPC options when you launch a cluster](emr-clusters-in-a-vpc.md).

When you specify managed security groups for a cluster, you must use the same type of security group, default or custom, for all managed security groups. For example, you can't specify a custom security group for the primary instance, and then not specify a custom security group for core and task instances.

If you use default managed security groups, you don't need to specify them when you create a cluster. Amazon EMR automatically uses the defaults. Moreover, if the defaults don't exist in the cluster's VPC yet, Amazon EMR creates them. Amazon EMR also creates them if you explicitly specify them and they don't exist yet.

You can edit rules in managed security groups after clusters are created. When you create a new cluster, Amazon EMR checks the rules in the managed security groups that you specify, and then creates any missing *inbound* rules that the new cluster needs in addition to rules that may have been added earlier. Unless specifically stated otherwise, each rule for default Amazon EMR-managed security groups is also added to custom Amazon EMR-managed security groups that you specify.

The default managed security groups are as follows:
+ **ElasticMapReduce-primary**

  For rules in this security group, see [Amazon EMR-managed security group for the primary instance (public subnets)](#emr-sg-elasticmapreduce-master).
+ **ElasticMapReduce-core**

  For rules in this security group, see [Amazon EMR-managed security group for core and task instances (public subnets)](#emr-sg-elasticmapreduce-slave).
+ **ElasticMapReduce-Primary-Private**

  For rules in this security group, see [Amazon EMR-managed security group for the primary instance (private subnets)](#emr-sg-elasticmapreduce-master-private).
+ **ElasticMapReduce-Core-Private**

  For rules in this security group, see [Amazon EMR-managed security group for core and task instances (private subnets)](#emr-sg-elasticmapreduce-slave-private).
+ **ElasticMapReduce-ServiceAccess**

  For rules in this security group, see [Amazon EMR-managed security group for service access (private subnets)](#emr-sg-elasticmapreduce-sa-private).

## Amazon EMR-managed security group for the primary instance (public subnets)
<a name="emr-sg-elasticmapreduce-master"></a>

The default managed security group for the primary instance in public subnets has the **Group Name** of **ElasticMapReduce-primary**. It has the following rules. If you specify a custom managed security group, Amazon EMR adds all the same rules to your custom security group.


<table>
<thead>
  <tr><th>Type</th><th>Protocol</th><th>Port range</th><th>Source</th><th>Details</th></tr>
</thead>
<tbody>
  <tr><td colspan="5"><i>Inbound rules</i></td></tr>
  <tr><td>All ICMP-IPv4</td><td>All</td><td>N/A</td><td rowspan="3">The Group ID of the managed security group for the primary instance. In other words, the same security group in which the rule appears.</td><td rowspan="3">These reflexive rules allow inbound traffic from any instance associated with the specified security group. Using the default <code>ElasticMapReduce-primary</code> for multiple clusters allows the core and task nodes of those clusters to communicate with each other over ICMP or any TCP or UDP port. Specify custom managed security groups to restrict cross-cluster access.</td></tr>
  <tr><td>All TCP</td><td>TCP</td><td>All</td></tr>
  <tr><td>All UDP</td><td>UDP</td><td>All</td></tr>
  <tr><td>All ICMP-IPV4</td><td>All</td><td>N/A</td><td rowspan="3">The Group ID of the managed security group specified for core and task nodes.</td><td rowspan="3">These rules allow all inbound ICMP traffic and traffic over any TCP or UDP port from any core and task instances that are associated with the specified security group, even if the instances are in different clusters.</td></tr>
  <tr><td>All TCP</td><td>TCP</td><td>All</td></tr>
  <tr><td>All UDP</td><td>UDP</td><td>All</td></tr>
  <tr><td>Custom</td><td>TCP</td><td>8443</td><td>Various Amazon IP address ranges</td><td>These rules allow the cluster manager to communicate with the primary node.</td></tr>
</tbody>
</table>


**To grant trusted sources SSH access to the primary security group with the console**

To edit your security groups, you must have permission to manage security groups for the VPC that the cluster is in. For more information, see [Changing Permissions for a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html) and the [Example Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_securitygroups-vpc.html) that allows managing EC2 security groups in the *IAM User Guide*.

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr).

1. Choose **Clusters**. Choose the **ID** of the cluster you want to modify.

1. In the **Network and security** pane, expand the **EC2 security groups (firewall)** dropdown.

1. Under **Primary node**, choose your security group.

1. Choose **Edit inbound rules**.

1. Check for an inbound rule that allows public access with the following settings. If it exists, choose **Delete** to remove it.
   + **Type**

     SSH
   + **Port**

     22
   + **Source**

     Custom 0.0.0.0/0
**Warning**  
Before December 2020, there was a pre-configured rule to allow inbound traffic on Port 22 from all sources. This rule was created to simplify initial SSH connections to the primary node. We strongly recommend that you remove this inbound rule and restrict traffic to trusted sources.

1. Scroll to the bottom of the list of rules and choose **Add Rule**.

1. For **Type**, select **SSH**.

   Selecting SSH automatically enters **TCP** for **Protocol** and **22** for **Port Range**.

1. For source, select **My IP** to automatically add your IP address as the source address. You can also add a range of **Custom** trusted client IP addresses, or create additional rules for other clients. Many network environments dynamically allocate IP addresses, so you might need to update your IP addresses for trusted clients in the future.

1. Choose **Save**.

1. Optionally, choose the other security group under **Core and task nodes** in the **Network and security ** pane and repeat the steps above to allow SSH client access to core and task nodes.

## Amazon EMR-managed security group for core and task instances (public subnets)
<a name="emr-sg-elasticmapreduce-slave"></a>

The default managed security group for core and task instances in public subnets has the **Group Name** of **ElasticMapReduce-core**. The default managed security group has the following rules, and Amazon EMR adds the same rules if you specify a custom managed security group.


<table>
<thead>
  <tr><th>Type</th><th>Protocol</th><th>Port range</th><th>Source</th><th>Details</th></tr>
</thead>
<tbody>
  <tr><td colspan="5"><i>Inbound rules</i></td></tr>
  <tr><td>All ICMP-IPV4</td><td>All</td><td>N/A</td><td rowspan="3">The Group ID of the managed security group for core and task instances. In other words, the same security group in which the rule appears.</td><td rowspan="3">These reflexive rules allow inbound traffic from any instance associated with the specified security group. Using the default <code>ElasticMapReduce-core</code> for multiple clusters allows the core and task instances of those clusters to communicate with each other over ICMP or any TCP or UDP port. Specify custom managed security groups to restrict cross-cluster access.</td></tr>
  <tr><td>All TCP</td><td>TCP</td><td>All</td></tr>
  <tr><td>All UDP</td><td>UDP</td><td>All</td></tr>
  <tr><td>All ICMP-IPV4</td><td>All</td><td>N/A</td><td rowspan="3">The Group ID of the managed security group for the primary instance.</td><td rowspan="3">These rules allow all inbound ICMP traffic and traffic over any TCP or UDP port from any primary instances that are associated with the specified security group, even if the instances are in different clusters. </td></tr>
  <tr><td>All TCP</td><td>TCP</td><td>All</td></tr>
  <tr><td>All UDP</td><td>UDP</td><td>All</td></tr>
</tbody>
</table>


## Amazon EMR-managed security group for the primary instance (private subnets)
<a name="emr-sg-elasticmapreduce-master-private"></a>

The default managed security group for the primary instance in private subnets has the **Group Name** of **ElasticMapReduce-Primary-Private**. The default managed security group has the following rules, and Amazon EMR adds the same rules if you specify a custom managed security group.


<table>
<thead>
  <tr><th>Type</th><th>Protocol</th><th>Port range</th><th>Source</th><th>Details</th></tr>
</thead>
<tbody>
  <tr><td colspan="5"><i>Inbound rules</i></td></tr>
  <tr><td>All ICMP-IPv4</td><td>All</td><td>N/A</td><td rowspan="3">The Group ID of the managed security group for the primary instance. In other words, the same security group in which the rule appears.</td><td rowspan="3">These reflexive rules allow inbound traffic from any instance associated with the specified security group and reachable from within the private subnet. Using the default <code>ElasticMapReduce-Primary-Private</code> for multiple clusters allows the core and task nodes of those clusters to communicate with each other over ICMP or any TCP or UDP port. Specify custom managed security groups to restrict cross-cluster access.</td></tr>
  <tr><td>All TCP</td><td>TCP</td><td>All</td></tr>
  <tr><td>All UDP</td><td>UDP</td><td>All</td></tr>
  <tr><td>All ICMP-IPV4</td><td>All</td><td>N/A</td><td rowspan="3">The Group ID of the managed security group for core and task nodes.</td><td rowspan="3">These rules allow all inbound ICMP traffic and traffic over any TCP or UDP port from any core and task instances that are associated with the specified security group and reachable from within the private subnet, even if the instances are in different clusters.</td></tr>
  <tr><td>All TCP</td><td>TCP</td><td>All</td></tr>
  <tr><td>All UDP</td><td>UDP</td><td>All</td></tr>
  <tr><td>HTTPS (8443)</td><td>TCP</td><td>8443</td><td>The Group ID of the managed security group for service access in a private subnet.</td><td>This rule allows the cluster manager to communicate with the primary node.<br />Required for Amazon EMR releases 7.x and earlier.</td></tr>
  <tr><td colspan="5"><i>Outbound rules</i></td></tr>
  <tr><td>All traffic</td><td>All</td><td>All</td><td>0.0.0.0/0</td><td>Provides outbound access to the internet. </td></tr>
  <tr><td>Custom TCP</td><td>TCP</td><td>9443</td><td>The Group ID of the managed security group for service access in a private subnet.</td><td>If the above "All traffic" default outbound rule is removed, this rule is a minimum requirement for Amazon EMR releases 5.30.0 to 7.x. Amazon EMR does not add this rule when you use a custom managed security group. </td></tr>
  <tr><td>Custom TCP</td><td>TCP</td><td>443 (https)</td><td>The Group ID of the managed security group for service access in a private subnet.</td><td>If the above "All traffic" default outbound rule is removed, this rule is a minimum requirement for Amazon EMR 5.30.0 and later to connect to Amazon S3 over https.<br />For Amazon EMR 8.0.0 and later and Amazon EMR Spark 8.0.0 and later, this rule is also required for the primary instance to communicate with the cluster manager through the VPC endpoint. Amazon EMR does not add this rule when you use a custom managed security group. </td></tr>
</tbody>
</table>


## Amazon EMR-managed security group for core and task instances (private subnets)
<a name="emr-sg-elasticmapreduce-slave-private"></a>

The default managed security group for core and task instances in private subnets has the **Group Name** of **ElasticMapReduce-Core-Private**. The default managed security group has the following rules, and Amazon EMR adds the same rules if you specify a custom managed security group.


<table>
<thead>
  <tr><th>Type</th><th>Protocol</th><th>Port range</th><th>Source</th><th>Details</th></tr>
</thead>
<tbody>
  <tr><td colspan="5"><i>Inbound rules</i></td></tr>
  <tr><td>All ICMP-IPV4</td><td>All</td><td>N/A</td><td rowspan="3">The Group ID of the managed security group for core and task instances. In other words, the same security group in which the rule appears.</td><td rowspan="3">These reflexive rules allow inbound traffic from any instance associated with the specified security group. Using the default <code>ElasticMapReduce-core</code> for multiple clusters allows the core and task instances of those clusters to communicate with each other over ICMP or any TCP or UDP port. Specify custom managed security groups to restrict cross-cluster access.</td></tr>
  <tr><td>All TCP</td><td>TCP</td><td>All</td></tr>
  <tr><td>All UDP</td><td>UDP</td><td>All</td></tr>
  <tr><td>All ICMP-IPV4</td><td>All</td><td>N/A</td><td rowspan="3">The Group ID of the managed security group for the primary instance.</td><td rowspan="3">These rules allow all inbound ICMP traffic and traffic over any TCP or UDP port from any primary instances that are associated with the specified security group, even if the instances are in different clusters. </td></tr>
  <tr><td>All TCP</td><td>TCP</td><td>All</td></tr>
  <tr><td>All UDP</td><td>UDP</td><td>All</td></tr>
  <tr><td>HTTPS (8443)</td><td>TCP</td><td>8443</td><td>The Group ID of the managed security group for service access in a private subnet.</td><td>This rule allows the cluster manager to communicate with core and task nodes.<br />Required for Amazon EMR releases 7.x and earlier.</td></tr>
  <tr><td colspan="5"><i>Outbound rules</i></td></tr>
  <tr><td>All traffic</td><td>All</td><td>All</td><td>0.0.0.0/0</td><td>See <a href="#private-sg-egress-rules">Editing outbound rules</a> below.</td></tr>
  <tr><td>Custom TCP</td><td>TCP</td><td>443 (https)</td><td>The Group ID of the managed security group for service access in a private subnet.</td><td>If the above "All traffic" default outbound rule is removed, this rule is a minimum requirement for Amazon EMR 5.30.0 and later to connect to Amazon S3 over https. Amazon EMR does not add this rule when you use a custom managed security group. </td></tr>
</tbody>
</table>


### Editing outbound rules
<a name="private-sg-egress-rules"></a>

By default, Amazon EMR creates this security group with outbound rules that allow all outbound traffic on all protocols and ports. Allowing all outbound traffic is selected because various Amazon EMR and customer applications that can run on Amazon EMR clusters may require different egress rules. Amazon EMR is not able to anticipate these specific settings when creating default security groups. You can scope down egress in your security groups to include only those rules that suit your use cases and security policies. At minimum, this security group requires the following outbound rules, but some applications might need additional egress.


| Type | Protocol | Port range | Destination | Details | 
| --- | --- | --- | --- | --- | 
| All TCP | TCP | All | pl-{{xxxxxxxx}} | Managed Amazon S3 prefix list com.amazonaws.{{MyRegion}}.s3. | 
| All Traffic | All | All | sg-{{xxxxxxxxxxxxxxxxx}} | The ID of the ElasticMapReduce-Core-Private security group. | 
| All Traffic | All | All | sg-{{xxxxxxxxxxxxxxxxx}} | The ID of the ElasticMapReduce-Primary-Private security group. | 
| Custom TCP | TCP | 9443 | sg-{{xxxxxxxxxxxxxxxxx}} | The ID of the `ElasticMapReduce-ServiceAccess` security group.<br />Required for Amazon EMR releases 7.x and earlier. | 

## Amazon EMR-managed security group for service access (private subnets)
<a name="emr-sg-elasticmapreduce-sa-private"></a>

The default managed security group for service access in private subnets has the **Group Name** of **ElasticMapReduce-ServiceAccess**.

For Amazon EMR 8.0.0 and later and Amazon EMR Spark 8.0.0 and later, this security group is attached to the Amazon EMR service VPC endpoint and must allow inbound traffic over HTTPS (port 443) from cluster instances. The same rule is needed if you are using custom security groups.


<table>
<thead>
  <tr><th>Type</th><th>Protocol</th><th>Port range</th><th>Source</th><th>Details</th></tr>
</thead>
<tbody>
  <tr><td colspan="5"><i>Inbound rules</i></td></tr>
  <tr><td>HTTPS</td><td>TCP</td><td>443</td><td>The CIDR block(s) of the cluster's VPC.</td><td>This rule allows communication between EMR cluster instances and the cluster manager.</td></tr>
</tbody>
</table>


For Amazon EMR releases 7.x and earlier, this security group is attached to an ENI in your subnet. It has inbound rules, and outbound rules that allow traffic over HTTPS (port 8443, port 9443) to the other managed security groups in private subnets. These rules allow the cluster manager to communicate with the primary node and with core and task nodes. The same rules are needed if you are using custom security groups.


<table>
<thead>
  <tr><th>Type</th><th>Protocol</th><th>Port range</th><th>Source</th><th>Details</th></tr>
</thead>
<tbody>
  <tr><td colspan="5"><i>Inbound rules</i> Required for Amazon EMR clusters with Amazon EMR release 5.30.0 to 7.x.</td></tr>
  <tr><td>Custom TCP</td><td>TCP</td><td>9443</td><td>The Group ID of the managed security group for primary instance. </td><td>This rule allows the communication between primary instance's security group to the service access security group.</td></tr>
  <tr><td colspan="5"><i>Outbound rules</i> Required for Amazon EMR clusters with releases 7.x or earlier.</td></tr>
  <tr><td>Custom TCP</td><td>TCP</td><td>8443</td><td>The Group ID of the managed security group for primary instance. </td><td rowspan="2">These rules allow the cluster manager to communicate with the primary node and with core and task nodes.</td></tr>
  <tr><td>Custom TCP</td><td>TCP</td><td>8443</td><td>The Group ID of the managed security group for core and task instances. </td></tr>
</tbody>
</table>
