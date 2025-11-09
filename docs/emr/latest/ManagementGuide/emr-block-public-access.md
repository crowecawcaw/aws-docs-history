# Using Amazon EMR block public access

Amazon EMR _block public access (BPA)_ prevents you from launching a
cluster in a public subnet if the cluster has a security configuration that allows
inbound traffic from public IP addresses on a port.

###### Important

_Block public access_ is enabled by default. To increase
account protection, we recommend that you keep it enabled.

## Understanding block public

access

You can use the _block public access_ account-level
configuration to centrally manage public network access to Amazon EMR clusters.

When a user from your AWS account launches a cluster, Amazon EMR checks the port
rules in the security group for the cluster and compares them with your inbound
traffic rules. If the security group has an inbound rule that opens ports to the
public IP addresses IPv4 0.0.0.0/0 or IPv6 ::/0, and those ports aren't specified as
exceptions for your account, Amazon EMR doesn't let the user create the cluster.

If a user modifies the security group rules for a running cluster in a public
subnet to have a public access rule that violates the BPA configuration for your
account, Amazon EMR revokes the new rule if it has permission to do so. If Amazon EMR doesn't
have permission to revoke the rule, it creates an event in the AWS Health
dashboard that describes the violation. To grant the revoke rule permission to
Amazon EMR, see [Configure Amazon EMR to revoke security group
rules](#revoke-block-public-access "#revoke-block-public-access").

Block public access is enabled by default for all clusters in every AWS Region
for your AWS account. BPA applies to the entire lifecycle of a cluster, but
doesn't apply to clusters that you create in private subnets. You can configure
exceptions to the BPA rule; port 22 is an exception by default. For more information
on setting exceptions, see [Configure block public
access](#configure-block-public-access "#configure-block-public-access").

## Configure block public

access

You can update security groups and the block public access configuration in your
accounts at any time.

You can turn block public access (BPA) settings on and off with the AWS Management Console, the
AWS Command Line Interface (AWS CLI), and the Amazon EMR API. Settings apply across your account on a
Region-by-Region basis. To maintain cluster security, we recommend that you use
BPA.

Console

###### To configure block public access with the console

1. Sign in to the AWS Management Console, then open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. On the top navigation bar, select the
   **Region** that you want to configure if
   it's not already selected.
3. Under **EMR on EC2** in the left navigation
   pane, choose **Block public access**.
4. Under **Block public access settings**,
   complete the following steps.

| To...                                | Do this...                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Turn block public access on or off   | Choose **Edit**, choose<br>**Turn on\*<br>• or **Turn<br>off\*<br>• as appropriate, and then choose<br>**Save**.                                                                                                                                                                                                                                                                             |
| Edit ports in the list of exceptions | 1. Choose **Edit\*<br>• and find<br>the **Port range exceptions**<br>section.<br>2. To add ports to the list of exceptions,<br>choose **Add a port range*<br>• and<br>enter a new port or port range. Repeat for each<br>port or port range to add.<br>3. To remove a port or port range, choose<br>\*\*Remove*<br>• next to the entry in<br>the list of port ranges.<br>4. Choose **Save**. |

AWS CLI

###### To configure block public access using the AWS CLI

- Use the `aws emr
put-block-public-access-configuration` command to
  configure block public access as shown in the following
  examples.

| To...                                                          | Do this...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Turn block public access on                                    | Set<br>`BlockPublicSecurityGroupRules` to<br>`true` as shown in the following<br>example. For the cluster to launch, no security<br>group associated with a cluster can have an<br>inbound rule that allows public access.<br>`<br>aws emr put-block-public-access-configuration --block-public-access-configuration BlockPublicSecurityGroupRules=true<br>`                                                                                                                                                                                      |
| Turn block public access off                                   | Set<br>`BlockPublicSecurityGroupRules` to<br>`false` as shown in the following<br>example. Security groups associated with a cluster<br>can have inbound rules that allow public access on<br>any port. We do not recommend this<br>configuration.<br>`<br>aws emr put-block-public-access-configuration --block-public-access-configuration BlockPublicSecurityGroupRules=false<br>`                                                                                                                                                             |
| Turn block public access on and specify<br>ports as exceptions | The following example turns on block public<br>access, and specifies Port 22 and Ports 100-101 as<br>exceptions. This allows clusters to be created if<br>an associated security group has an inbound rule<br>that allows public access on Port 22, Port 100, or<br>Port 101.<br>`<br>aws emr put-block-public-access-configuration --block-public-access-configuration  '{ "BlockPublicSecurityGroupRules": true, "PermittedPublicSecurityGroupRuleRanges": [ { "MinRange": 22, "MaxRange": 22 }, { "MinRange": 100, "MaxRange": 101 } ] }'<br>` |

## Configure Amazon EMR to revoke security group

rules

Amazon EMR needs permission to revoke security group rules and comply with your block
public access configuration. You can use one of the following approaches to give
Amazon EMR the permission that it needs:

- **(Recommended)** Attach the
  `AmazonEMRServicePolicy_v2` managed policy to the service
  role. For more information, see [Service role for Amazon EMR (EMR role)](emr-iam-role.md "emr-iam-role.md").
- Create a new inline policy that allows the
  `ec2:RevokeSecurityGroupIngress` action on security groups.
  For more information about how to modify a role permissions policy, see
  **Modifying a role permissions policy**
  with the [IAM Console](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy"), [AWS API](../../../IAM/latest/UserGuide/roles-managingrole-editing-api.md#roles-modify_permissions-policy-api "../../../IAM/latest/UserGuide/roles-managingrole-editing-api.md#roles-modify_permissions-policy-api"), and [AWS CLI](../../../IAM/latest/UserGuide/roles-managingrole-editing-cli.md#roles-modify_permissions-policy-cli "../../../IAM/latest/UserGuide/roles-managingrole-editing-cli.md#roles-modify_permissions-policy-cli") in the _IAM User Guide_.

## Resolve block public access

violations

If a block public access violation occurs, you can mitigate it with one of the
following actions:

- If you want to access a web interface on your cluster, use one of the
  options described in [View web interfaces hosted on Amazon EMR
  clusters](emr-web-interfaces.md "emr-web-interfaces.md") to access the interface through SSH
  (port 22).
- To allow traffic to the cluster from specific IP addresses rather than
  from the public IP address, add a security group rule. For more information,
  see [Add rules to a security group](../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#adding-security-group-rule "../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#adding-security-group-rule") in the
  _Amazon EC2 Getting Started Guide_.
- **(Not recommended)** You can configure Amazon EMR
  BPA exceptions to include the desired port or range of ports. When you specify a
  BPA exception, you introduce risk with an unprotected port. If you plan to
  specify an exception, you should remove the exception as soon as it's no
  longer needed. For more information, see [Configure block public
  access](#configure-block-public-access "#configure-block-public-access").

## Identify clusters associated with

security group rules

You might need to identify all of the clusters that are associated with a given
security group rule, or to find the security group rule for a given cluster.

- If you know the security group, then you can identify its associated
  clusters if you find the network interfaces for the security group. For more
  information, see [How can I find
  the resources associated with an Amazon EC2 security group?](https://forums.aws.amazon.com/knowledge-center/ec2-find-security-group-resources "https://forums.aws.amazon.com/knowledge-center/ec2-find-security-group-resources") on
  AWS re:Post. The Amazon EC2 instances that are attached to these network interfaces
  will be tagged with the ID of the cluster that they belong to.
- If you want to find the security groups for a known cluster, follow the
  steps in [View Amazon EMR cluster status and details](emr-manage-view-clusters.md "emr-manage-view-clusters.md"). You can find the security
  groups for the cluster in the **Network and security**
  panel in the console, or in the `Ec2InstanceAttributes` field
  from the AWS CLI.
