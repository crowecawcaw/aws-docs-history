# Troubleshooting Communication Errors

###### Topics

- [Solving Communication Problems over TCP Port 443 between the staging area and the Elastic Disaster Recovery Service](#Solving-Communication-Problems "#Solving-Communication-Problems")
- [Calculating the required bandwidth for TCP Port 1500](#Calculating-Bandwidth "#Calculating-Bandwidth")
- [Verifying Communication over Port 1500](#Verifying-Communication-1500 "#Verifying-Communication-1500")
- [Solving Communication Problems over Port 1500](#Solving-Problems-1500 "#Solving-Problems-1500")

## Solving Communication Problems over TCP Port 443 between the staging area and the Elastic Disaster Recovery Service

Verify the following network configuration items for the staging area:

- **DHCP** – [Check the DHCP options set of the VPC of the staging area.](../../../directoryservice/latest/admin-guide/dhcp_options_set.md "../../../directoryservice/latest/admin-guide/dhcp_options_set.md")
  Ensure that the IPv4 CIDR, the DHCP options set, the Route table, and the
  Network ACL are correct.
- **DNS** – Ensure that you are allowing
  outbound DNS resolution and connectivity over TCP Port 443.

AWS Elastic Disaster Recovery requires outbound access from the staging area to the API
endpoints for the following services:
[AWS Elastic Disaster Recovery](../../../general/latest/gr/drs.md#drs-region "../../../general/latest/gr/drs.md#drs-region"),
[Amazon S3](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md"),
and [Amazon EC2](../../../general/latest/gr/ec2-service.md "../../../general/latest/gr/ec2-service.md").
Refer to each service's endpoint documentation for the correct domain, including
IPv6 and FIPS endpoints if applicable to your environment.

Console

###### Verify staging area route table and network ACL

1. In the VPC Console, select **Subnets**
   and find the staging area subnet. Note the associated
   **Route table** and
   **Network ACL**.
2. Select **Route tables**, find the
   route table for the staging area subnet, and select the
   **Routes** tab. Verify that a route
   exists for outbound internet traffic (destination
   `0.0.0.0/0` with a target of an Internet Gateway,
   NAT Gateway, or VPN Gateway).
3. Select **Network ACLs**, find the
   ACL for the staging area subnet, and verify that the
   **Outbound Rules** allow TCP port
   443 and that the **Inbound Rules**
   allow the ephemeral port range for return traffic.
4. Check the security group associated with the replication
   servers to ensure outbound TCP 443 is allowed.

CLI

###### Verify staging area route table and network ACL

1. Check the route table for the staging area subnet:

```
aws ec2 describe-route-tables \
  --filters Name=association.subnet-id,Values=`subnet-1234567890abcdefg` \
  --query 'RouteTables[0].Routes[*].{Dest:DestinationCidrBlock,GatewayId:GatewayId,NatGatewayId:NatGatewayId,State:State}'
```

If this returns null, the subnet uses the VPC main route table.
Find it by VPC ID:

```
aws ec2 describe-route-tables \
  --filters Name=vpc-id,Values=`vpc-1234567890abcdefg` Name=association.main,Values=true \
  --query 'RouteTables[0].Routes[*].{Dest:DestinationCidrBlock,GatewayId:GatewayId,NatGatewayId:NatGatewayId}'
```

Verify that a route to `0.0.0.0/0` exists with an
Internet Gateway (`igw-`), NAT Gateway
(`nat-`), or VPN Gateway (`vgw-`)
target. 2. Check the network ACL for the staging area subnet:

```
aws ec2 describe-network-acls \
  --filters Name=association.subnet-id,Values=`subnet-1234567890abcdefg` \
  --query 'NetworkAcls[0].Entries[*].{RuleNum:RuleNumber,Protocol:Protocol,Action:RuleAction,CIDR:CidrBlock,PortRange:PortRange}'
```

Verify that outbound rules allow TCP port 443 and inbound
rules allow the [ephemeral port range](../../../vpc/latest/userguide/custom-network-acl.md#nacl-ephemeral-ports "../../../vpc/latest/userguide/custom-network-acl.md#nacl-ephemeral-ports") for return traffic. 3. Check the replication server security group:

```
aws drs get-replication-configuration \
  --source-server-id `s-1234567890abcdefg` \
  --query 'replicationServersSecurityGroupsIDs'
```

```
aws ec2 describe-security-groups \
  --group-ids `sg-1234567890abcdefg` \
  --query 'SecurityGroups[0].IpPermissionsEgress[*].{Port:ToPort,CIDR:IpRanges[0].CidrIp}'
```

## Calculating the required bandwidth for TCP Port 1500

The required bandwidth for transferring the replicated data over TCP Port 1500 should be
based on the write speed of the participating Source machines. The recommended bandwidth should
be at least the sum of the average write speed of all replicated source machines.

_Minimal bandwidth = the sum of the write speed of all Source
machines_

For example, suppose you are replicating two Source machines. One has a write speed of 5
MBps (meaning it writes 5 megabytes of data every second), while the other has 7 MBps. In this case,
the recommended bandwidth should be at least 12 MBps.

### Finding the Write Speed of Your source servers

To calculate the required bandwidth for transferring replicated data over TCP Port 1500,
you need to know the write speed of your source machines. Use the following tools to find the
write speed of your source servers:

#### Linux

Use the iostat command-line utility, located in the sysstat package. The iostat utility
monitors system input/output device loading and generates statistical reports.

The iostat utility is installed with yum (RHEL/CentOS), via [apt-get](https://www.howtoforge.com/tutorial/how-to-install-and-use-iostat-on-ubuntu-1604/ "https://www.howtoforge.com/tutorial/how-to-install-and-use-iostat-on-ubuntu-1604/") (Ubuntu), and via [zypper](https://unix.stackexchange.com/questions/281094/install-iotop-iostat-via-zypper-or-anything-else-on-a-suse-sles-12-virual-ma?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa "https://unix.stackexchange.com/questions/281094/install-iotop-iostat-via-zypper-or-anything-else-on-a-suse-sles-12-virual-ma?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa") (SUSE).

To use iostat for checking the write speed of a Source machine, enter the
following: iostat -x <interval>

- -x - displays extended statistics.
- <interval> – the number of seconds iostat waits between each
  report. Each subsequent report covers the time since the previous
  report.

For example, to check the write speed of a machine every 3 seconds, enter the following
command:

iostat -x 3

We recommend that you run the iostat utility for at least 24 hours, since the write speed
to the disk changes during the day, and it will take 24 hours of runtime to identify the
average running speed.

#### Windows

Install and use the DiskMon application. DiskMon logs and displays all hard disk activity
on a Windows system.

[Installing
DiskMon](https://docs.microsoft.com/en-us/sysinternals/downloads/diskmon "https://docs.microsoft.com/en-us/sysinternals/downloads/diskmon")

DiskMon presents read and write offsets in terms of sectors (512 bytes).
Events can be either timed for their duration (in microseconds), or stamped with the absolute
time that they were initiated.

## Verifying Communication over Port 1500

If there is a connection problem from the Source server to the Replication Servers or the
Staging Area, use the following methods to check the connection.

Linux

###### Verify TCP Port 1500 connectivity from a Linux source server

1. Test connectivity directly from the source server to the
   replication server IP on port 1500:

```
nc -zv `replication-server-ip` 1500
```

2. Alternatively, launch a test Linux instance in the staging
   area subnet and open a listener:

```
# On the test instance in the staging area:
nc -l 1500

# On the source server:
telnet `test-instance-ip` 1500
```

3. If the connection fails, check the firewall on the source
   server:

```
sudo iptables -L -n | grep 1500
```

Windows

###### Verify TCP Port 1500 connectivity from a Windows source server

1. Test connectivity from the source server to the replication
   server IP on port 1500 using PowerShell:

```
Test-NetConnection -ComputerName `replication-server-ip` -Port 1500
```

2. If `TcpTestSucceeded` is `False`,
   check the Windows Firewall:

```
Get-NetFirewallRule | Where-Object {$_.LocalPort -eq 1500 -or $_.RemotePort -eq 1500} | Format-Table DisplayName, Direction, Action, Enabled
```

## Solving Communication Problems over Port 1500

If TCP port 1500 connectivity fails between the source server and the staging
area, check the following:

- The Network ACL on the staging area subnet may deny the traffic.
- Route rules on the staging area subnet may be inaccurately set.
- The firewall (both internal and external) on the source server may block communication.
- The **Use private IP for data replication**
  setting in the AWS Elastic Disaster Recovery Console may not be set correctly for your network topology.

Console

###### Verify network ACL, route table, and security group for port 1500

1. In the VPC Console, select **Network
   ACLs** and find the ACL associated with the staging
   area subnet.
2. On the **Inbound Rules** tab,
   verify that a rule allows TCP port 1500 from the source server
   address space. On the **Outbound
   Rules** tab, verify that the [ephemeral port range](../../../vpc/latest/userguide/custom-network-acl.md#nacl-ephemeral-ports "../../../vpc/latest/userguide/custom-network-acl.md#nacl-ephemeral-ports") is allowed for return traffic.
3. Select **Route tables** and
   verify that the staging area subnet has a route for inbound
   traffic from the source environment.
4. Check the security group associated with the replication
   servers to ensure inbound TCP port 1500 is allowed.

CLI

###### Verify network ACL, route table, and security group for port 1500

1. Check the network ACL rules for the staging area subnet:

```
aws ec2 describe-network-acls \
  --filters Name=association.subnet-id,Values=`subnet-1234567890abcdefg` \
  --query 'NetworkAcls[0].Entries[*].{RuleNum:RuleNumber,Protocol:Protocol,Action:RuleAction,CIDR:CidrBlock,PortRange:PortRange}'
```

Verify that inbound rules allow TCP port 1500 and outbound
rules allow the ephemeral port range. 2. Check the route table:

```
aws ec2 describe-route-tables \
  --filters Name=association.subnet-id,Values=`subnet-1234567890abcdefg` \
  --query 'RouteTables[0].Routes[*].{Dest:DestinationCidrBlock,GatewayId:GatewayId,NatGatewayId:NatGatewayId}'
```

3. Check the replication server security group for inbound TCP
   1500:

```
aws drs get-replication-configuration \
  --source-server-id `s-1234567890abcdefg` \
  --query 'replicationServersSecurityGroupsIDs'
```

```
aws ec2 describe-security-groups \
  --group-ids `sg-1234567890abcdefg` \
  --query 'SecurityGroups[0].IpPermissions[*].{Port:ToPort,CIDR:IpRanges[0].CidrIp}'
```

4. Check the source server firewall:

   - **Linux:**

   ```
   sudo iptables -L -n | grep 1500
   sudo firewall-cmd --list-all 2>/dev/null
   ```
   - **Windows (PowerShell):**

   ```
   Get-NetFirewallRule | Where-Object {$_.Enabled -eq 'True'} |
     Get-NetFirewallPortFilter | Where-Object {$_.RemotePort -eq 1500 -or $_.LocalPort -eq 1500}
   ```
