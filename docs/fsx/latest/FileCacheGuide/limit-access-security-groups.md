# Cache access control with Amazon VPC

A cache is accessible through an elastic network interface that resides
in the virtual private cloud (VPC) based on the Amazon VPC service that you associate with
your cache. You access your cache through its DNS name, which maps to the
cache's network interface. Only resources within the associated VPC, or a peered VPC,
can access your cache's network interface. For more information, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC User Guide._

###### Warning

You must not modify or delete the Amazon File Cache elastic network interface.
Modifying or deleting the network interface can cause a permanent loss of connection
between your VPC and your cache.

## Amazon VPC security groups

To further control network traffic going through your cache's network interface
within your VPC, use security groups to limit access. A _security
group_ acts as a virtual firewall to control the traffic for its
associated resources. In this case, the associated resource is your cache's network
interface. You also use VPC security groups to control network traffic for your clients.

### Controlling access using inbound and

outbound rules

To use a security group to control access to your cache and clients, add the
inbound rules to control incoming traffic and outbound rules to control the
outgoing traffic from your cache and clients. Make sure to have the right network
traffic rules in your security group to map your cache to a folder on your supported
compute instance.

For more information about security group rules, see [Security Group Rules](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#security-group-rules "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#security-group-rules") in the _Amazon EC2 User Guide._

###### To create a security group for your cache

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. In the navigation pane, choose **Security
   Groups**.
3. Choose **Create security group**.
4. Specify a name and description for the security group.
5. For **VPC**, choose the VPC associated with your cache to
   create the security group within that VPC.
6. Choose **Create** to create the security group.

Next, add inbound rules to the security group that you just created to enable
traffic between your Amazon File Cache file servers.

###### To add inbound rules to your security group

1. Select the security group you just created if it's not already selected.
   For **Actions**, choose **Edit inbound
   rules**.
2. Add the following inbound rules.

| Type            | Protocol | Port Range | Source                                                                                                                        | Description                                                                     |
| --------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Custom TCP rule | TCP      | 988        | Choose **Custom** and enter the security group ID of the security group that you just created                                 | Allows traffic between Amazon File Cache file servers                           |
| Custom TCP rule | TCP      | 988        | Choose **Custom** and enter the security group IDs of the security groups associated with your Lustre clients                 | Allows traffic between Amazon File Cache file servers and clients               |
| Custom TCP rule | TCP      | 1018-1023  | Choose **Custom** and enter the security group ID of the security group that you just created                                 | Allows traffic between Amazon File Cache file servers                           |
| Custom TCP rule | TCP      | 1018-1023  | Choose **Custom** and enter the security group IDs of the security groups associated with your File Cache file servers        | Allows traffic between Amazon File Cache file servers                           | 3. Choose **Save** to save and apply the new inbound rules. By default, security group rules allow all outbound traffic (All, 0.0.0.0/0). If your security group doesn't allow all outbound traffic, add the following outbound rules to your security group. These rules allow traffic between Amazon File Cache file servers and clients, and between Amazon File Cache file servers. ###### To add outbound rules to your security group 1. Choose the same security group to which you just added the inbound rules. For **Actions**, choose **Edit outbound rules**. 2. Add the following outbound rules.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Type            | Protocol | Port Range | Source                                                                                                                        | Description                                                                     |
| ---             | ---      | ---        | ---                                                                                                                           | ---                                                                             |
| Custom TCP rule | TCP      | 988        | Choose **Custom** and enter the security group ID of the security group that you just created                                 | Allow Lustre traffic between Amazon File Cache file servers                     |
| Custom TCP rule | TCP      | 988        | Choose **Custom** and enter the security group IDs of the security group associated with your Lustre clients                  | Allow Lustre traffic between Amazon File Cache file servers and Lustre clients  |
| Custom TCP rule | TCP      | 1018-1023  | Choose **Custom** and enter the security group ID of the security group that you just created                                 | Allows Lustre traffic between Amazon File Cache file servers                    |
| Custom TCP rule | TCP      | 1018-1023  | Choose **Custom** and enter the security group IDs of the security groups associated with your Lustre clients                 | Allows traffic between Amazon File Cache file servers and Lustre clients        | 3. Choose **Save** to save and apply the new outbound rules. ###### To associate a security group with your Amazon File Cache 1. Open the AWS Management Console at [https://console.aws.amazon.com/fsx/#fc/file-caches](https://console.aws.amazon.com/fsx/#fc/file-caches "https://console.aws.amazon.com/fsx/#fc/file-caches"). 2. On the console dashboard, chose your cache to view its details. 3. On the **Network & Security** tab, choose your cache's network interface IDs (for example, `ENI-01234567890123456`). Doing this redirects you to the Amazon EC2 console. 4. Choose each network interface ID. Each action opens a new instance of the Amazon EC2 console in your browser. For each security group, choose **Change Security Groups** for **Actions**. 5. In the **Change Security Groups** dialog box, choose the security groups to use, and choose **Save**. ## Lustre client VPC security group rules You use VPC security groups to control access to your Lustre clients by adding inbound rules to control incoming traffic and outbound rules to control the outgoing traffic from your Lustre clients. Make sure to have the right network traffic rules in your security group to ensure that Lustre traffic can flow between your Lustre clients and your Amazon File Caches. Add the following inbound rules to the security groups applied to your clients. |
| Type            | Protocol | Port Range | Source                                                                                                                        | Description                                                                     |
| ---             | ---      | ---        | ---                                                                                                                           | ---                                                                             |
| Custom TCP rule | TCP      | 988        | Choose **Custom** and enter the security group IDs of the security groups that are applied to your Lustre clients             | Allows traffic between Amazon File Cache file servers                           |
| Custom TCP rule | TCP      | 988        | Choose **Custom** and enter the security group IDs of the security groups associated with your Amazon File Cache file servers | Allow Lustre traffic between Amazon File Cache file servers and clients         |
| Custom TCP rule | TCP      | 1018-1023  | Choose **Custom** and enter the security group IDs of the security groups that are applied to your clients                    | Allows traffic between Amazon File Cache file servers                           |
| Custom TCP rule | TCP      | 1018-1023  | Choose **Custom** and enter the security group IDs of the security groups associated with your Amazon File Cache file servers | Allows traffic between Amazon File Cache file servers and clients               | Add the following outbound rules to the security groups applied to your clients.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Type            | Protocol | Port Range | Source                                                                                                                        | Description                                                                     |
| ---             | ---      | ---        | ---                                                                                                                           | ---                                                                             |
| Custom TCP rule | TCP      | 988        | Choose **Custom** and enter the security group IDs of the security groups that are applied to your Lustre clients             | Allows traffic between Lustre clients                                           |
| Custom TCP rule | TCP      | 988        | Choose **Custom** and enter the security group IDs of the security groups associated with your Amazon File Cache file servers | Allow Lustre traffic between Amazon File Cache file servers and Lustre clients  |
| Custom TCP rule | TCP      | 1018-1023  | Choose **Custom** and enter the security group IDs of the security groups that are applied to your Lustre clients             | Allows Lustre traffic between Lustre clients                                    |
| Custom TCP rule | TCP      | 1018-1023  | Choose **Custom** and enter the security group IDs of the security groups associated with your Amazon File Cache file servers | Allows Lustre traffic between Amazon File Cache file servers and Lustre clients |
