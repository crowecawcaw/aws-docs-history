# Create a security group

Security groups act as a firewall for associated compute environment container instances, controlling both
inbound and outbound traffic at the container instance level. A security group can be used only in the VPC for which
it is created.

You can add rules to a security group that enable you to connect to your container instance from your IP address
using SSH. You can also add rules that allow inbound and outbound HTTP and HTTPS access from anywhere. Add any rules
to open ports that are required by your tasks.

Note that if you plan to launch container instances in multiple Regions, you need to create a security group in
each Region. For more information, see [Regions and
Availability Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") in the _Amazon EC2 User Guide_.

###### Note

You need the public IP address of your local computer, which you can get using a service. For example, we
provide the following service: [http://checkip.amazonaws.com/](http://checkip.amazonaws.com/ "http://checkip.amazonaws.com/") or
[https://checkip.amazonaws.com/](https://checkip.amazonaws.com/ "https://checkip.amazonaws.com/"). To locate another service that
provides your IP address, use the search phrase "what is my IP address." If you're connecting through an Internet
service provider (ISP) or from behind a firewall without a static IP address, find out the range of IP addresses
that are used by client computers.

###### To create a security group using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Security Groups**.
3. Choose **Create security group**.
4. Enter a name and description for the security group. You cannot change the name and description of a security
   group after it is created.
5. From **VPC**, choose the VPC.
6. (Optional) By default, new security groups start with only an outbound rule that allows all traffic to leave
   the resource. You must add rules to enable any inbound traffic or to restrict the outbound traffic.

AWS Batch container instances don't require any inbound ports to be open. However, you might want to add an SSH
rule. That way, you can log into the container instance and examine the containers in jobs with Docker commands. If
you want your container instance to host a job that runs a web server, you can also add rules for HTTP. Complete
the following steps to add these optional security group rules.

On the **Inbound** tab, create the following rules and choose
**Create**:

    * Choose **Add Rule**. For **Type**, choose **HTTP**. For
     **Source**, choose **Anywhere** (`0.0.0.0/0`).
    * Choose **Add Rule**. For **Type**, choose **SSH**. For
     **Source**, choose **Custom IP**, and specify the public IP address of your
     computer or network in Classless Inter-Domain Routing (CIDR) notation. If your company allocates addresses from a
     range, specify the entire range, such as `203.0.113.0/24`. To specify an individual IP address in CIDR
     notation, choose **My IP**. This adds the routing prefix `/32` to the public IP
     address.


    ###### Note

    For security reasons, we don't recommend that you allow SSH access from all IP addresses
     (`0.0.0.0/0`) to your instance but only for testing purposes and only for a short time.

7. You can add tags now, or you can add them later. To add a tag, choose **Add new tag** and
   enter the tag key and value.
8. Choose **Create security group**.
   To create a security group using the command line, see [>create-security-group](../../../cli/latest/reference/ec2/create-security-group.md "../../../cli/latest/reference/ec2/create-security-group.md") (AWS CLI)

For more information about security groups, see [Work with security
groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md#working-with-security-groups "../../../vpc/latest/userguide/VPC_SecurityGroups.md#working-with-security-groups").
