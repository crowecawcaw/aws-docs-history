

# Verifying network connectivity
<a name="verifying-network-connectivity"></a>

AWS Elastic Disaster Recovery requires two network paths from the staging area for replication to succeed. TCP port 443 provides API communication with AWS service endpoints. TCP port 1500 provides data replication between source servers and replication servers. Use this page to verify both paths and resolve connectivity issues.

**Topics**
+ [Network requirements](#network-requirements)
+ [Verifying TCP port 443](#comm-443-diagnose)
+ [Verifying TCP port 1500](#comm-1500-verify)
+ [Resolving port 1500 issues](#comm-1500-resolve)
+ [Common network configuration issues](#comm-443-checklist)

## Network requirements
<a name="network-requirements"></a>

Elastic Disaster Recovery replication servers require the following network connectivity:
+ **TCP port 443 outbound** from the staging area subnet to the following endpoints:
  + `drs.{{region}}.amazonaws.com`
  + `s3.{{region}}.amazonaws.com`
  + `ec2.{{region}}.amazonaws.com`
+ **TCP port 1500 inbound** to the staging area from source servers, or outbound from source servers to the replication server private or public IP address.

For a complete list of regional endpoints, see [AWS Elastic Disaster Recovery endpoints](https://docs.aws.amazon.com/general/latest/gr/drs.html#drs-region).

## Verifying TCP port 443
<a name="comm-443-diagnose"></a>

Use the following procedures to verify that the staging area networking configuration permits outbound TCP port 443 traffic to AWS service endpoints.

------
#### [ Console ]

**To verify outbound port 443 in the VPC console**

1. Open the Amazon VPC console and navigate to **Route Tables**.

1. Find the route table associated with your staging area subnet. Verify that a route to `0.0.0.0/0` exists with a target of an internet gateway, NAT gateway, or VPN gateway.

1. Choose **Network ACLs** in the navigation pane. Verify that the network ACL associated with the staging area subnet allows outbound traffic on TCP port 443 and allows inbound traffic on ephemeral ports (1024–65535).

1. Choose **Security Groups** in the navigation pane. Find the replication server security group and verify that it allows outbound traffic on TCP port 443 to `0.0.0.0/0` or to the specific service endpoint IP ranges.

------
#### [ CLI ]

**To verify outbound port 443 with the AWS CLI**

1. Verify the route table for the staging area subnet:

   ```
   aws ec2 describe-route-tables \
       --filters Name=association.subnet-id,Values={{subnet-id}} \
       --query 'RouteTables[0].Routes[*].{Dest:DestinationCidrBlock,GatewayId:GatewayId,NatGatewayId:NatGatewayId,State:State}'
   ```

1. Check the network ACL rules for the staging area subnet:

   ```
   aws ec2 describe-network-acls \
       --filters Name=association.subnet-id,Values={{subnet-id}} \
       --query 'NetworkAcls[0].Entries[*].{RuleNum:RuleNumber,Protocol:Protocol,Action:RuleAction,CIDR:CidrBlock,PortRange:PortRange}'
   ```

1. Retrieve the security group IDs assigned to the replication servers:

   ```
   aws drs get-replication-configuration \
       --source-server-id {{server-id}} \
       --query 'replicationServersSecurityGroupsIDs'
   ```

1. Verify the outbound rules for the replication server security group:

   ```
   aws ec2 describe-security-groups \
       --group-ids {{sg-id}} \
       --query 'SecurityGroups[0].IpPermissionsEgress[*].{Port:ToPort,CIDR:IpRanges[0].CidrIp}'
   ```

------

## Verifying TCP port 1500
<a name="comm-1500-verify"></a>

Run connectivity tests from your source server to confirm that TCP port 1500 is reachable on the replication server.

------
#### [ Linux ]

Use `nc` (netcat) to test connectivity:

```
nc -zv {{replication-server-ip}} 1500
```

If `nc` is not available, use `telnet`:

```
telnet {{replication-server-ip}} 1500
```

A successful connection confirms that TCP port 1500 is open between your source server and the replication server.

------
#### [ Windows ]

Use PowerShell to test connectivity:

```
Test-NetConnection -ComputerName {{replication-server-ip}} -Port 1500
```

A result of `TcpTestSucceeded : True` confirms that TCP port 1500 is open between your source server and the replication server.

------

## Resolving port 1500 issues
<a name="comm-1500-resolve"></a>

Check your network configuration to identify and resolve port 1500 connectivity issues.

------
#### [ Console ]

**To verify port 1500 network configuration in the VPC console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Network ACLs**. Verify that the inbound rules for the staging area subnet allow TCP port 1500.

1. Verify that the outbound rules for the network ACL allow the ephemeral port range (1024–65535).

1. In the navigation pane, choose **Route tables**. Verify that the route table for the staging area subnet has a route for inbound traffic from the source server network.

1. In the navigation pane, choose **Security groups**. Locate the security group attached to the replication servers and verify that it allows inbound TCP port 1500.

------
#### [ CLI ]

**To verify port 1500 network configuration with the AWS CLI**

1. Check that the network ACL allows inbound TCP port 1500 and outbound ephemeral ports:

   ```
   aws ec2 describe-network-acls \
       --filters "Name=association.subnet-id,Values={{staging-subnet-id}}"
   ```

   Verify that the inbound rules include an allow entry for TCP port 1500 and that the outbound rules include an allow entry for TCP ports 1024–65535.

1. Get the security group IDs for your replication servers:

   ```
   aws drs get-replication-configuration \
       --source-server-id {{source-server-id}} \
       --query 'replicationServersSecurityGroupsIDs'
   ```

1. Verify that the security group allows inbound TCP port 1500:

   ```
   aws ec2 describe-security-groups \
       --group-ids {{sg-id}} \
       --query 'SecurityGroups[0].IpPermissions[?ToPort==`1500`]'
   ```

1. Check the source server firewall rules. Do one of the following:
   + **Linux** — Run one of the following commands to check firewall rules:

     ```
     iptables -L -n | grep 1500
     ```

     ```
     firewall-cmd --list-all
     ```
   + **Windows** — Run the following PowerShell command to check firewall rules:

     ```
     Get-NetFirewallRule | Where-Object {$_.Enabled -eq 'True'} |
       Get-NetFirewallPortFilter | Where-Object {$_.RemotePort -eq '1500' -or $_.LocalPort -eq '1500'}
     ```

------

## Common network configuration issues
<a name="comm-443-checklist"></a>

The following issues commonly affect TCP port 443 or TCP port 1500 connectivity for Elastic Disaster Recovery replication:
+ **DHCP options set misconfigured** — The VPC DHCP options set specifies incorrect DNS servers, preventing endpoint name resolution.
+ **Route table missing internet route** — The staging area subnet route table has no route to `0.0.0.0/0` through an internet gateway or NAT gateway.
+ **Network ACL denying traffic** — A network ACL rule denies outbound TCP port 443, inbound TCP port 1500, or denies ephemeral port traffic for return packets.
+ **Security group restricting traffic** — The replication server security group does not allow outbound TCP port 443 or inbound TCP port 1500.
+ **NAT gateway issues** — The NAT gateway is in a private subnet without internet access, or all associated Elastic IP addresses are exhausted.
+ **VPC endpoint policy blocking access** — If you use VPC endpoints, the endpoint policy might deny the required API calls for AWS Elastic Disaster Recovery, Amazon S3, or Amazon EC2.
+ **Source server firewall blocking outbound 1500** — A host-based firewall on the source server blocks outbound TCP port 1500 connections.
+ **"Use private IP" setting misconfigured** — The **Use private IP for data replication** setting does not match your network topology. Enable this setting only when the source server can reach the replication server private IP address directly.