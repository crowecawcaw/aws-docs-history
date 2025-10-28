# Create a security group for your VPC

Your virtual private cloud (VPC) comes with a default security group. You can
create additional security groups. Security groups can be used only with resources
in the VPC for which it is created.

By default, new security groups start with only an outbound rule that allows all
traffic to leave the resource. You must add rules to enable any inbound traffic or
to restrict the outbound traffic. You can add rules when you create a security
group or later on. For more information, see [Security group rules](security-group-rules.md "security-group-rules.md").

###### Required permissions

Before you begin, ensure that you have the required permissions. For more information,
see the following:

- [Manage security groups](vpc-policy-examples.md#vpc-security-groups-iam "vpc-policy-examples.md#vpc-security-groups-iam")
- [Manage security group rules](vpc-policy-examples.md#vpc-security-group-rules-iam "vpc-policy-examples.md#vpc-security-group-rules-iam")

###### To create a security group using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Security groups**.
3. Choose **Create security group**.
4. Enter a name and description for the security group. You can't change the
   name and description of a security group after it is created.
5. For **VPC**, choose the VPC in which you'll create the
   resources to which you'll associate the security group.
6. (Optional) To add inbound rules, choose **Inbound rules**.
   For each rule, choose **Add rule** and specify the protocol,
   port, and source. For more information, see
   [Configure security group rules](working-with-security-group-rules.md "working-with-security-group-rules.md").
7. (Optional) To add outbound rules, choose **Outbound rules**.
   For each rule, choose **Add rule** and specify the protocol,
   port, and destination.
8. (Optional) To add a tag, choose **Add new tag** and
   enter the tag key and value.
9. Choose **Create security group**.

###### To create a security group using the AWS CLI

Use the [create-security-group](../../../cli/latest/reference/ec2/create-security-group.md "../../../cli/latest/reference/ec2/create-security-group.md") command.

Alternately, you can create a new security group by copying an existing one. When
you copy a security group, we automatically add the same inbound and outbound
rules as the original security group and use the same VPC as the original security
group. You can enter a name and description for the new security group. You can
optionally choose a different VPC, and you can modify the inbound and outbound
rules as needed. However, you can't copy a security group from one Region to
another Region.

###### To create a security group based on an existing one

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Security groups**.
3. Select a security group.
4. Choose **Actions**, **Copy to new security group**.
5. Enter a name and description for the security group.
6. (Optional) Choose a different VPC if needed.
7. (Optional) Add, remove, or edit the security group rules as needed.
8. Choose **Create security group**.
