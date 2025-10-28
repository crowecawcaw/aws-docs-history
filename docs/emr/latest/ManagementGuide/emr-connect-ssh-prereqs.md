# Before you connect to Amazon EMR: Authorize inbound

traffic

Before you connect to an Amazon EMR cluster, you must authorize inbound SSH traffic (port 22) from trusted clients such as your computer's IP address. In order to do so, edit the
managed security group rules for the nodes to which you want to connect. For example,
the following instructions show you how to add an inbound rule for SSH access to the
default ElasticMapReduce-master security group.

For more information about using security groups with Amazon EMR, see [Control network traffic with security groups for your Amazon EMR cluster](emr-security-groups.md "emr-security-groups.md").

Console

###### To grant trusted sources SSH access to the primary security group

with the console

To edit your security groups, you must have permission to manage
security groups for the VPC that the cluster is in. For more
information, see [Changing Permissions for a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") and the [Example Policy](../../../IAM/latest/UserGuide/reference_policies_examples_ec2_securitygroups-vpc.md "../../../IAM/latest/UserGuide/reference_policies_examples_ec2_securitygroups-vpc.md") that allows managing EC2 security groups in
the _IAM User Guide_.

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane,
   choose **Clusters**, and then choose the cluster
   that you want to update. This opens up the cluster details page. The
   **Properties** tab on this page will be
   pre-selected.
3. Under **Networking** in the
   **Properties** tab, select the arrow next to
   **EC2 security groups (firewall)** to expand
   this section. Under **Primary node**, select the
   security group link. This opens the EC2 console.
4. Choose the **Inbound rules** tab and then choose
   **Edit inbound rules**.
5. Check for an inbound rule that allows public access with the
   following settings. If it exists, choose **Delete**
   to remove it.
   - **Type**

   SSH
   - **Port**

   22
   - **Source**

   Custom 0.0.0.0/0

###### Warning

Before December 2020, the ElasticMapReduce-master security
group had a pre-configured rule to allow inbound traffic on Port
22 from all sources. This rule was created to simplify initial
SSH connections to the primary node. We strongly recommend that
you remove this inbound rule and restrict traffic to trusted
sources. 6. Scroll to the bottom of the list of rules and choose **Add
Rule**. 7. For **Type**, select **SSH**.
This selection automatically enters **TCP** for
**Protocol** and **22** for
**Port Range**. 8. For source, select **My IP** to automatically add
your IP address as the source address. You can also add a range of
**Custom** trusted client IP addresses, or
create additional rules for other clients. Many network environments
dynamically allocate IP addresses, so you might need to update your
IP addresses for trusted clients in the future. 9. Choose **Save**. 10. Optionally return to Step 3, choose **Core and task
nodes**, and repeat Steps 4 - 8. This grants core and
task nodes SSH client access.
