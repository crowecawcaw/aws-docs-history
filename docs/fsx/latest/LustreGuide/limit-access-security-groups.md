# File system access control with Amazon VPC

An Amazon FSx file system is accessible through an elastic network interface that resides
in the virtual private cloud (VPC) based on the Amazon VPC service that you associate with
your file system. You access your Amazon FSx file system through its DNS name, which maps to
the file system's network interface. Only resources within the associated VPC, or a
peered VPC, can access your file system's network interface. For more information, see
[What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in
the _Amazon VPC User Guide._

###### Warning

You must not modify or delete the Amazon FSx elastic network interface. Modifying or deleting the
network interface can cause a permanent loss of connection between your VPC and your file system.

## Amazon VPC Security Groups

To further control network traffic going through your file system's network
interface within your VPC, you use security groups to limit access to your file
systems. A _security group_ acts as a virtual
firewall to control the traffic for its associated resources. In this case, the
associated resource is your file system's network interface. You also use VPC security groups to control
network traffic for your Lustre clients.

### EFA-enabled security groups

If you are going to create an EFA-enabled FSx for Lustre, you should first create an EFA-enabled
security group and specify it as the security group for the file system. An EFA requires a security
group that allows all inbound and outbound traffic to and from the security group itself and the
security group of the clients if clients reside in a different security group. For more information,
see [Step 1:
Prepare an EFA-enabled security group](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security") in the _Amazon EC2 User Guide_.

### Controlling Access Using Inbound and Outbound Rules

To use a security group to control access to your Amazon FSx file system and Lustre clients, you add the
inbound rules to control incoming traffic and outbound rules to control the outgoing
traffic from your file system and Lustre clients. Make sure to have the right network traffic rules in
your security group to map your Amazon FSx file system's file share to a folder on your
supported compute instance.

For more information on security group rules, see [Security
Group Rules](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#security-group-rules "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#security-group-rules") in the _Amazon EC2 User Guide_.

###### To create a security group for your Amazon FSx file system

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. In the navigation pane, choose **Security
   Groups**.
3. Choose **Create Security Group**.
4. Specify a name and description for the security group.
5. For **VPC**, choose the VPC associated with your Amazon FSx
   file system to create the security group within that VPC.
6. Choose **Create** to create the security group.

Next, you add inbound rules to the security group that you just created to enable
Lustre traffic between your FSx for Lustre file servers.

###### To add inbound rules to your security group

1. Select the security group you just created if it's not already selected.
   For **Actions**, choose **Edit inbound rules**.
2. Add the following inbound rules.

| Type            | Protocol | Port Range | Source                                                                                                                   | Description                                                                     |
| --------------- | -------- | ---------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Custom TCP rule | TCP      | 988        | Choose \*_Custom_<br>• and enter the security<br>group ID of the security group that you just created                    | Allows Lustre traffic between FSx for Lustre file servers                       |
| Custom TCP rule | TCP      | 988        | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups associated with your Lustre<br>clients | Allows Lustre traffic between FSx for Lustre file servers and<br>Lustre clients |
| Custom TCP rule | TCP      | 1018-1023  | Choose \*_Custom_<br>• and enter the security<br>group ID of the security group that you just created                    | Allows Lustre traffic between FSx for Lustre file servers                       |
| Custom TCP rule | TCP      | 1018-1023  | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups associated with your Lustre<br>clients | Allows Lustre traffic between FSx for Lustre file servers and<br>Lustre clients |

3. Choose **Save** to save and apply the new inbound rules.

By default, security group rules allow all outbound traffic (All, 0.0.0.0/0). If
your security group doesn't allow all outbound traffic, add the following
outbound rules to your security group. These rules allow traffic between FSx for Lustre
file servers and Lustre clients, and between Lustre file servers.

###### To add outbound rules to your security group

1. Choose the same security group to which you just added the inbound rules.
   For **Actions**, choose **Edit outbound
   rules**.
2. Add the following outbound rules.

| Type            | Protocol | Port Range | Source                                                                                                                   | Description                                                                     |
| --------------- | -------- | ---------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Custom TCP rule | TCP      | 988        | Choose \*_Custom_<br>• and enter the security<br>group ID of the security group that you just created                    | Allow Lustre traffic between FSx for Lustre file servers                        |
| Custom TCP rule | TCP      | 988        | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security group associated with your Lustre<br>clients  | Allow Lustre traffic between FSx for Lustre file servers and<br>Lustre clients  |
| Custom TCP rule | TCP      | 1018-1023  | Choose \*_Custom_<br>• and enter the security<br>group ID of the security group that you just created                    | Allows Lustre traffic between FSx for Lustre file servers                       |
| Custom TCP rule | TCP      | 1018-1023  | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups associated with your Lustre<br>clients | Allows Lustre traffic between FSx for Lustre file servers and<br>Lustre clients |

3. Choose **Save** to save and apply the new outbound rules.

###### To associate a security group with your Amazon FSx file system

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. On the console dashboard, choose your file system to view its
   details.
3. On the **Network & Security** tab, click on
   the **Amazon EC2 console** link under **Network Interface(s)**
   to view all network interfaces for your file system.
4. For each network interface, choose **Actions**, then
   choose **Change security groups**.
5. In the **Change security groups** dialog box, choose the
   security groups that you want to associate with the network interface.
6. Choose **Save**.

## Lustre client VPC security group rules

You use VPC security groups to control access to your Lustre clients by adding
inbound rules to control incoming traffic and outbound rules to control the outgoing
traffic from your Lustre clients. Make sure to have the right network traffic rules in
your security group to ensure that Lustre traffic can flow between your Lustre clients and your Amazon FSx file systems.

Add the following inbound rules to the security groups applied to your Lustre clients.

| Type            | Protocol | Port Range | Source                                                                                                                             | Description                                                                     |
| --------------- | -------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Custom TCP rule | TCP      | 988        | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups that are applied to your Lustre clients          | Allows Lustre traffic between Lustre clients                                    |
| Custom TCP rule | TCP      | 988        | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups associated with your FSx for Lustre file systems | Allows Lustre traffic between FSx for Lustre file servers and<br>Lustre clients |
| Custom TCP rule | TCP      | 1018-1023  | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups that are applied to your Lustre clients          | Allows Lustre traffic between Lustre clients                                    |
| Custom TCP rule | TCP      | 1018-1023  | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups associated with your FSx for Lustre file systems | Allows Lustre traffic between FSx for Lustre file servers and<br>Lustre clients |

Add the following outbound rules to the security groups applied to your Lustre clients.

| Type            | Protocol | Port Range | Source                                                                                                                                | Description                                                                     |
| --------------- | -------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Custom TCP rule | TCP      | 988        | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups that are applied to your Lustre clients             | Allows Lustre traffic between Lustre clients                                    |
| Custom TCP rule | TCP      | 988        | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups associated with your FSx for Lustre<br>file systems | Allow Lustre traffic between FSx for Lustre file servers and<br>Lustre clients  |
| Custom TCP rule | TCP      | 1018-1023  | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups that are applied to your Lustre clients             | Allows Lustre traffic between Lustre clients                                    |
| Custom TCP rule | TCP      | 1018-1023  | Choose \*_Custom_<br>• and enter the security<br>group IDs of the security groups associated with your FSx for Lustre<br>file systems | Allows Lustre traffic between FSx for Lustre file servers and<br>Lustre clients |
