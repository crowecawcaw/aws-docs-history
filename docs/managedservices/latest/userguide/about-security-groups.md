

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Security groups
<a name="about-security-groups"></a>

In AWS VPCs, AWS Security Groups act as virtual firewalls, controlling the traffic for one or more stacks (an instance or a set of instances). When a stack is launched, it's associated with one or more security groups, which determine what traffic is allowed to reach it:
+ For stacks in your public subnets, the default security groups accept traffic from HTTP (80) and HTTPS (443) from all locations (the internet). The stacks also accept internal SSH and RDP traffic from your corporate network, and AWS bastions. Those stacks can then egress through any port to the Internet. They can also egress to your private subnets and other stacks in your public subnet.
+ Stacks in your private subnets can egress to any other stack in your private subnet, and instances within a stack can fully communicate over any protocol with each other.

**Important**  
The default security group for stacks on private subnets allows all stacks in your private subnet to communicate with other stacks in that private subnet. If you want to restrict communications between stacks within a private subnet, you must create new security groups that describe the restriction. For example, if you want to restrict communications to a database server so that the stacks in that private subnet can only communicate from a specific application server over a specific port, request a special security group. How to do so is described in this section.

## Default Security Groups
<a name="default-sec-groups"></a>

------
#### [ MALZ ]

The following table describes the default inbound security group (SG) settings for your stacks. The SG is named "SentinelDefaultSecurityGroupPrivateOnly-vpc-ID" where {{ID}} is a VPC ID in your AMS multi-account landing zone account. All traffic is allowed outbound to "mc-initial-garden-SentinelDefaultSecurityGroupPrivateOnly" via this security group (all local traffic within stack subnets is allowed). 

All traffic is allowed outbound to 0.0.0.0/0 by a second security group "SentinelDefaultSecurityGroupPrivateOnly".

**Tip**  
If you're choosing a security group for an AMS change type, such as EC2 create, or OpenSearch create domain, you would use one of the default security groups described here, or a security group that you created. You can find the list of security groups, per VPC, in either the AWS EC2 console or VPC console.

There are additional default security groups that are used for internal AMS purposes.


**AMS default security groups (inbound traffic)**  

<table>
<thead>
  <tr><th>Type</th><th>Protocol</th><th>Port range</th><th>Source</th></tr>
</thead>
<tbody>
  <tr><td>All traffic</td><td>All</td><td>All</td><td>SentinelDefaultSecurityGroupPrivateOnly (restricts outbound traffic to members of the same security group)</td></tr>
  <tr><td>All traffic</td><td>All</td><td>All</td><td>SentinelDefaultSecurityGroupPrivateOnlyEgressAll (does not restrict outbound traffic)</td></tr>
  <tr><td>HTTP, HTTPS, SSH, RDP</td><td>TCP</td><td>80 / 443 (Source 0.0.0.0/0)<br />SSH and RDP access is allowed from bastions</td><td>SentinelDefaultSecurityGroupPublic (does not restrict outbound traffic)</td></tr>
  <tr><td colspan="4"><b>MALZ bastions</b>:</td></tr>
  <tr><td>SSH</td><td>TCP</td><td>22</td><td rowspan="4">SharedServices VPC CIDR and DMZ VPC CIDR, plus Customer-provided on-prem CIDRs</td></tr>
  <tr><td>SSH</td><td>TCP</td><td>22</td></tr>
  <tr><td>RDP</td><td>TCP</td><td>3389</td></tr>
  <tr><td>RDP</td><td>TCP</td><td>3389</td></tr>
  <tr><td colspan="4"><b>SALZ bastions</b>:</td></tr>
  <tr><td>SSH</td><td>TCP</td><td>22</td><td>mc-initial-garden-LinuxBastionSG</td></tr>
  <tr><td>SSH</td><td>TCP</td><td>22</td><td>mc-initial-garden-LinuxBastionDMZSG</td></tr>
  <tr><td>RDP</td><td>TCP</td><td>3389</td><td>mc-initial-garden-WindowsBastionSG</td></tr>
  <tr><td>RDP</td><td>TCP</td><td>3389</td><td>mc-initial-garden-WindowsBastionDMZSG</td></tr>
</tbody>
</table>


------
#### [ SALZ ]

The following table describes the default inbound security group (SG) settings for your stacks. The SG is named "mc-initial-garden-SentinelDefaultSecurityGroupPrivateOnly-{{ID}}" where {{ID}} is a unique identifier. All traffic is allowed outbound to "mc-initial-garden-SentinelDefaultSecurityGroupPrivateOnly" via this security group (all local traffic within stack subnets is allowed). 

All traffic is allowed outbound to 0.0.0.0/0 by a second security group "mc-initial-garden-SentinelDefaultSecurityGroupPrivateOnlyEgressAll-{{ID}}".

**Tip**  
If you're choosing a security group for an AMS change type, such as EC2 create, or OpenSearch create domain, you would use one of the default security groups described here, or a security group that you created. You can find the list of security groups, per VPC, in either the AWS EC2 console or VPC console.

There are additional default security groups that are used for internal AMS purposes.


**AMS default security groups (inbound traffic)**  

<table>
<thead>
  <tr><th>Type</th><th>Protocol</th><th>Port range</th><th>Source</th></tr>
</thead>
<tbody>
  <tr><td>All traffic</td><td>All</td><td>All</td><td>SentinelDefaultSecurityGroupPrivateOnly (restricts outbound traffic to members of the same security group)</td></tr>
  <tr><td>All traffic</td><td>All</td><td>All</td><td>SentinelDefaultSecurityGroupPrivateOnlyEgressAll (does not restrict outbound traffic)</td></tr>
  <tr><td>HTTP, HTTPS, SSH, RDP</td><td>TCP</td><td>80 / 443 (Source 0.0.0.0/0)<br />SSH and RDP access is allowed from bastions</td><td>SentinelDefaultSecurityGroupPublic (does not restrict outbound traffic)</td></tr>
  <tr><td colspan="4"><b>MALZ bastions</b>:</td></tr>
  <tr><td>SSH</td><td>TCP</td><td>22</td><td rowspan="4">SharedServices VPC CIDR and DMZ VPC CIDR, plus Customer-provided on-prem CIDRs</td></tr>
  <tr><td>SSH</td><td>TCP</td><td>22</td></tr>
  <tr><td>RDP</td><td>TCP</td><td>3389</td></tr>
  <tr><td>RDP</td><td>TCP</td><td>3389</td></tr>
  <tr><td colspan="4"><b>SALZ bastions</b>:</td></tr>
  <tr><td>SSH</td><td>TCP</td><td>22</td><td>mc-initial-garden-LinuxBastionSG</td></tr>
  <tr><td>SSH</td><td>TCP</td><td>22</td><td>mc-initial-garden-LinuxBastionDMZSG</td></tr>
  <tr><td>RDP</td><td>TCP</td><td>3389</td><td>mc-initial-garden-WindowsBastionSG</td></tr>
  <tr><td>RDP</td><td>TCP</td><td>3389</td><td>mc-initial-garden-WindowsBastionDMZSG</td></tr>
</tbody>
</table>


------

## Create, Change, or Delete Security Groups
<a name="create-security-group"></a>

You can request custom security groups. In cases where the default security groups do not meet the needs of your applications or your organization, you can modify or create new security groups. Such a request would be considered approval-required and would be reviewed by the AMS operations team.

To create a security group outside of stacks and VPCs, submit an RFC using the `Deployment | Advanced stack components | Security group | Create (managed automation)` change type (ct-1oxx2g2d7hc90).

For Active Directory (AD) security group modifications, use the following change types:
+ To add a user: Submit an RFC using Management \| Directory Service \| Users and groups \| Add user to group [ct-24pi85mjtza8k]
+ To remove a user: Submit an RFC using Management \| Directory Service \| Users and groups \| Remove user from group [ct-2019s9y3nfml4]

**Note**  
When using manual CTs, AMS recommends that you use the ASAP **Scheduling** option (choose **ASAP** in the console, leave start and end time blank in the API/CLI) as these CTs require an AMS operator to examine the RFC, and possibly communicate with you before it can be approved and run. If you schedule these RFCs, be sure to allow at least 24 hours. If approval does not happen before the scheduled start time, the RFC is rejected automatically.

## Find Security Groups
<a name="find-security-group"></a>

To find the security groups attached to a stack or instance, use the EC2 console. After finding the stack or instance, you can see all security groups attached to it.

For ways to find security groups at the command line and filter the output, see [`describe-security-groups`](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-security-groups.html).