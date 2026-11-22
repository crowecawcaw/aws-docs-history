

# Step 2: Create DNS records

Before you add hosts and install VMware Cloud Foundation (VCF), create DNS records for each ESX host and for each VCF management appliance that you plan to deploy. Create a forward (A) record and a reverse (PTR) record for each one. Amazon Elastic VMware Service performs a DNS lookup of the fully qualified domain name (FQDN) of each host during host creation. Host creation fails if the records don’t already exist.

**Important**  
Create the A and PTR records for every host before you add that host. If the records don’t resolve, the host transitions to `CREATE_FAILED`.

The host FQDN is `<host-name>.<domain>`. `<host-name>` is the name that you pass when you add the host. `<domain>` is the domain name in the DHCP option set of your VPC. For more information, see [Configure DNS and NTP with a DHCP option set](network-dhcp-dns-ntp.md).

## Plan host names
<a name="self-deployed-dns-names"></a>

When you plan host names, include the length of your domain name.
+ The FQDN of each host and VCF management appliance must not exceed 62 characters. The FQDN is the host name combined with the domain name from your VPC DHCP option set. A longer host FQDN causes an error when you add the host.
+ We recommend that you keep each host name to 15 characters or fewer, to follow NetBIOS naming limits. A longer host name doesn’t cause a deployment failure.

## Record requirements
<a name="self-deployed-dns-requirements"></a>

Host records must meet these requirements.
+ The A record IP address is within the host management (`vmkManagement`) VLAN CIDR block that you specified when you created the environment.
+ The A record IP address matches the management IP address that the host gets. In the example deployment in this guide, Amazon EVS gave the hosts the next free addresses of the host management VLAN subnet in order, starting at `.11`. We recommend that you create the host A records in the order in which you add the hosts, starting at that address.
+ Each A record has a matching PTR record in your reverse lookup zone.
+ Both forward and reverse lookups succeed from the Amazon EVS service access subnet.

VCF management appliance records (for vCenter Server, NSX Manager, and the other appliances for your VCF version) must meet these requirements.
+ The FQDNs match the host names that you configure during VCF installation.
+ The IP addresses fall within the range of the appropriate VLAN subnet.
+ The records resolve from the Amazon EVS management VLAN and from any network from which you reach the VCF management appliances.

The names and number of appliances depend on your VCF version and topology. For the full list, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html). For the records that the diskless example needs, with example addresses, see [DNS records for the example](getting-started-diskless.md#getting-started-diskless-dns).

## Create the records
<a name="self-deployed-dns-create"></a>

If you use Route 53 private hosted zones, create the records in the forward and reverse zones that you created with the network foundation. For more information, see [Create private hosted zones and a Resolver inbound endpoint](network-dhcp-dns-ntp.md#network-dhcp-dns-zones).

1. Create an A record in a forward zone for each host and each VCF management appliance.

1. Create a PTR record in a reverse zone for each A record. A PTR record name is the IP address in reverse order, under the reverse zone. For example, with a reverse zone named `10.10.in-addr.arpa`, the PTR record for 10.10.0.11 has the name `11.0.10.10.in-addr.arpa` and points to `esx01.evs.example.com.`.

## Verify the records
<a name="self-deployed-dns-verify"></a>

Verify the records from an instance in your VPC, such as the instance in [Launch an instance to reach the VPC](network-dhcp-dns-ntp.md#network-access-instance). Query each DNS server in your DHCP option set for the forward and reverse record of every host and appliance. The following example verifies one host against two DNS servers.

```bash
nslookup esx01.evs.example.com 10.10.200.100
nslookup esx01.evs.example.com 10.10.200.101
nslookup 10.10.0.11 10.10.200.100
nslookup 10.10.0.11 10.10.200.101
```

Each command must return the expected name or address. Don’t add a host until all lookups succeed for it. If you use Route 53, also wait until Route 53 reports the record changes as in sync.

You have created and verified the DNS records. For troubleshooting, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

Next step: [Step 3: Add hosts](self-deployed-add-hosts.md).