# Prerequisites for linking to on-premises

NFS data repositories

Before you can link your cache to an on-premises NFS data store, verify that your
resources and configurations meet the following requirements:

- Your on-premises NFS file system must support NFSv3.
- If you're using a domain name to link your NFS file system to Amazon File Cache, you must
  provide the IP address of a DNS server that Amazon File Cache can use to resolve the domain
  name of the on-premises NFSv3 file system. The DNS server can be located in the VPC
  where you plan to create the cache, or it can be on your on-premises network accessible
  from your VPC.
- The DNS server and on premises NFSv3 file system must use private IP
  addresses, as specified in RFC 1918:
  - 10.0.0.0-10.255.255.255 (10/8 prefix)
  - 172.16.0.0-172.31.255.255 (172.16/12 prefix)
  - 192.168.0.0-192.168.255.255 (192.168/16 prefix)

- You must establish an AWS Direct Connect or VPN connection between your on-premises network and the
  Amazon VPC where your Amazon File Cache is located. For more information about AWS Direct Connect,
  see the [_AWS Direct Connect User Guide_](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md").
  For more information about setting up a VPC connection, see
  the [_Amazon VPC User Guide_](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md").

###### Important

Use an AWS VPN connection if you want to encrypt data as it transits between your
Amazon VPC and your on-premises network. For more information, see [What is AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")

- Your on-premises firewall must allow traffic between IP addresses in your
  Amazon VPC subnet IP CIDR and the IP addresses of the DNS server and the on-premises NFSv3 file
  system. The following ports must be open for the daemons involved in sharing data
  via NFS:

| Port | Protocol | Description                                                                                                                                                         |
| ---- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 111  | TCP/UDP  | Port for the \*_portmapper_<br>• daemon. The port number is fixed.                                                                                                  |
| 2049 | TCP/UDP  | Port for the \*_nfsd_<br>• daemon. The port number is fixed.                                                                                                        |
| 635  | TCP/UDP  | Port for the \*_mountd_<br>• daemon. The port assignment is dynamic and<br>could be another port number. You must verify the actual port and make sure it's open.   |
| 4045 | TCP/UDP  | Port for the \*_nlockmgr_<br>• daemon. The port assignment is dynamic and<br>could be another port number. You must verify the actual port and make sure it's open. |
| 4046 | TCP/UDP  | Port for the \*_status_<br>• daemon. The port assignment is dynamic and<br>could be another port number. You must verify the actual port and make sure it's open.   |

You can use the following command to look up dynamic ports for your on-premises NFS servers:

```
rpcinfo -p localhost
```

- Your on-premises NFSv3 file system is configured to allow access to IP addresses
  on the Amazon VPC where the cache is located.
- The Amazon VPC Security Group used for your cache must be configured to allow
  outbound traffic to the IP addresses of the DNS server and on-premises NFSv3 file system.
  Make sure to add outbound rules to allow port 53 for both UDP and TCP for DNS traffic,
  and to allow the TCP ports used by the on-premises NFSv3 file system for NFS.
  For more information, see
  [Controlling access using inbound and
  outbound rules](limit-access-security-groups.md#inbound-outbound-rules "limit-access-security-groups.md#inbound-outbound-rules").
- While Amazon File Cache supports NFSv3 file systems with most NFSv3 export
  policies, you must not use the NFS export option
  `all_squash`. This configuration is required so that Amazon File Cache has the
  necessary permissions to read and write files owned by all users on your NFSv3 file system.
