After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Step 5: Configuring security group inbound

rules

After you set up routing, you need to add inbound rule for the default security group to
allow inbound traffic. The default security group comes with your AWS account. For more
information, see [Default security groups](../../../vpc/latest/userguide/default-security-group.md "../../../vpc/latest/userguide/default-security-group.md") in
the _Amazon VPC User Guide_.

A security group acts as a firewall that controls the traffic allowed to and from the
resources in your VPC. You can choose the ports and protocols to allow for inbound traffic or
outbound traffic. For each security group, you add separate sets of rules for inbound traffic
and outbound traffic. For more information, see [Security group rules](../../../vpc/latest/userguide/security-group-rules.md "../../../vpc/latest/userguide/security-group-rules.md") in the _Amazon VPC User Guide_.

As an example, add an entry to allow TCP traffic for port _5005_ to
connect to a q process in your account running on port _5005_. This makes
port _5005_ of any host launched with the default security group to be
reachable.

###### To create an inbound rule

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Security Groups**.
3. Under the **Inbound rules** tab, choose **Edit inbound
   rules**.
4. On **Inbound rules** page, choose **Add
   rules**.
5. For **Type**, choose _Custom TCP_.
6. For **Port range** enter _5005_.

As another example, you can also allow all traffic from FinSpace to all ports. To allow
all ports by default, follow the above steps of creating an inbound rule. In step 5, for
**Type**, choose _All TCP_.

###### Note

    * If you need to restrict outbound traffic to specific ports and destination, add [network ACL](step1-config-ntw.md#nacl "step1-config-ntw.md#nacl") while creating a network connection to
     deny outbound traffic from FinSpace for each port range and destination.
    * When you create an Amazon EC2 instance, you need to specify the default security group for these
     inbound rules to apply. See next section for an example of how an Amazon EC2 instance is
     created with this security group.


    If you have hosts with different port rules you
     can create a security group for each host. When you launch an EC2 instance, use the
     security group with the port rules for your host.
