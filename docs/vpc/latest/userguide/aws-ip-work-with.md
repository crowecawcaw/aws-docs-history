# Find the IP address ranges for AWS services

The AWS IP address range JSON file provided by AWS can be a valuable resource for finding
the IP addresses of various AWS services and leveraging that information to enhance your
network security and access control. By parsing the detailed data contained within this
JSON file, you can precisely identify the IP address ranges associated with specific AWS services
and Regions.

For example, you can utilize the IP address ranges to configure robust network
security policies, setting up granular firewall rules to allow or deny access to certain
AWS resources. This information can also be useful for a variety of AWS Network Firewall tasks. This level of control is crucial for protecting your applications and
data, ensuring that only authorized traffic can reach the necessary AWS services.
Additionally, having this IP intelligence can help you ensure your applications are
properly configured to communicate with the right AWS endpoints, improving overall
reliability and performance.

Beyond just firewall rules, the `ip-ranges.json` file can also be leveraged to
configure sophisticated egress filtering on your network infrastructure. By
understanding the destination IP address ranges for different AWS services, you can set
up routing policies or leverage advanced network security solutions like to selectively permit or block outbound traffic based on its intended
destination. This egress control is essential for mitigating the risk of data leakage
and unauthorized access.

It's important to note that the `ip-ranges.json` file is regularly updated, so
maintaining an up-to-date local copy is crucial to ensure you have the most accurate and
current information. By continuously leveraging the contents of this file, you can
efficiently manage network access and security for your AWS-based applications,
strengthening your overall cloud security posture.

The following examples can help you filter the AWS IP address ranges to just what
you are looking for. On Linux, you can download and use the [the
jq tool](https://stedolan.github.io/jq/ "https://stedolan.github.io/jq/") to parse a local copy of the JSON file. The [AWS Tools for Windows PowerShell](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md")
includes a cmdlet, [Get-AWSPublicIpAddressRange](../../../powershell/latest/reference/items/Get-AWSPublicIpAddressRange.md "../../../powershell/latest/reference/items/Get-AWSPublicIpAddressRange.md"),
that you can use to parse this JSON file. For more information, see the following blog:
[Querying the Public IP Address Ranges for AWS](https://aws.amazon.com/blogs/developer/querying-the-public-ip-address-ranges-for-aws/ "https://aws.amazon.com/blogs/developer/querying-the-public-ip-address-ranges-for-aws/").

To get the JSON file, see [Download the JSON file](aws-ip-ranges.md#aws-ip-download "aws-ip-ranges.md#aws-ip-download"). For more information about the syntax
of the JSON file, see [Syntax for AWS IP address range JSON](aws-ip-syntax.md "aws-ip-syntax.md").

###### Examples

- [Get the file creation date](#filter-ip-ranges-creation-date "#filter-ip-ranges-creation-date")
- [Get the IP addresses for a specific Region](#filter-ip-ranges-region "#filter-ip-ranges-region")
- [Get all IPv4 addresses](#filter-ip-ranges-ipv4 "#filter-ip-ranges-ipv4")
- [Get all IPv4 addresses for a specific service](#filter-ip-ranges-ipv4-service "#filter-ip-ranges-ipv4-service")
- [Get all IPv4 addresses for a specific service in a specific Region](#filter-ip-ranges-ipv4-service-region "#filter-ip-ranges-ipv4-service-region")
- [Get all IPv6 addresses](#filter-ip-ranges-ipv6 "#filter-ip-ranges-ipv6")
- [Get all IPv6 addresses for a specific service](#filter-ip-ranges-ipv6-service "#filter-ip-ranges-ipv6-service")
- [Get all IP addresses for a specific border group](#filter-ip-ranges-border-group "#filter-ip-ranges-border-group")

## Get the file creation date

The following example gets the creation date of `ip-ranges.json`.

jq

```
`$` `jq .createDate < ip-ranges.json``"2024-08-01-17-22-15"`
```

PowerShell

```
`PS C:\>` `Get-AWSPublicIpAddressRange -OutputPublicationDate``Thursday, August 1, 2024 9:22:35 PM`
```

## Get the IP addresses for a specific Region

The following example filters the JSON file for the IP addresses for the specified Region.

jq

```
`$` `jq '.prefixes[] | select(.region=="us-east-1")' < ip-ranges.json``{
 "ip_prefix": "23.20.0.0/14",
 "region": "us-east-1",
 "network_border_group": "us-east-1",
 "service": "AMAZON"
},
{
 "ip_prefix": "50.16.0.0/15",
 "region": "us-east-1",
 "network_border_group": "us-east-1",
 "service": "AMAZON"
},
{
 "ip_prefix": "50.19.0.0/16",
 "region": "us-east-1",
 "network_border_group": "us-east-1",
 "service": "AMAZON"
},
...`
```

PowerShell

```
`PS C:\>` `Get-AWSPublicIpAddressRange -Region us-east-1``IpPrefix Region NetworkBorderGroup Service
-------- ------ ------- -------
23.20.0.0/14 us-east-1 us-east-1 AMAZON
50.16.0.0/15 us-east-1 us-east-1 AMAZON
50.19.0.0/16 us-east-1 us-east-1 AMAZON
...`
```

## Get all IPv4 addresses

The following example filters the JSON file for the IPv4 addresses.

jq

```
`$` `jq -r '.prefixes | .[].ip_prefix' < ip-ranges.json``23.20.0.0/14
27.0.0.0/22
43.250.192.0/24
...`
```

PowerShell

```
`PS C:\>` `Get-AWSPublicIpAddressRange | where {$_.IpAddressFormat -eq "Ipv4"} | select IpPrefix``IpPrefix
--------
23.20.0.0/14
27.0.0.0/22
43.250.192.0/24
...`
```

## Get all IPv4 addresses for a specific service

The following example filters the JSON file for the IPv4 addresses for the specified service.

jq

```
`$` `jq -r '.prefixes[] | select(.service=="GLOBALACCELERATOR") | .ip_prefix' < ip-ranges.json``13.248.117.0/24
15.197.34.0/23
15.197.36.0/22
...`
```

PowerShell

```
`PS C:\>` `Get-AWSPublicIpAddressRange -ServiceKey GLOBALACCELERATOR | where {$_.IpAddressFormat -eq "Ipv4"} | select IpPrefix``IpPrefix
--------
13.248.117.0/24
15.197.34.0/23
15.197.36.0/22
...`
```

## Get all IPv4 addresses for a specific service in a specific Region

The following example filters the JSON file for the IPv4 addresses for the specified service in the specified Region.

jq

```
`$` `jq -r '.prefixes[] | select(.region=="us-east-1") | select(.service=="GLOBALACCELERATOR") | .ip_prefix' < ip-ranges.json``13.248.124.0/24
99.82.166.0/24
99.82.171.0/24
...`
```

PowerShell

```
`PS C:\>` `Get-AWSPublicIpAddressRange -Region us-east-1 -ServiceKey GLOBALACCELERATOR | where {$_.IpAddressFormat -eq "Ipv4"} | select IpPrefix``IpPrefix
--------
13.248.117.0/24
99.82.166.0/24
99.82.171.0/24
...`
```

## Get all IPv6 addresses

The following example filters the JSON file for the IPv6 addresses.

jq

```
`$` `jq -r '.ipv6_prefixes | .[].ipv6_prefix' < ip-ranges.json``2a05:d07c:2000::/40
2a05:d000:8000::/40
2406:dafe:2000::/40
...`
```

PowerShell

```
`PS C:\>` `Get-AWSPublicIpAddressRange | where {$_.IpAddressFormat -eq "Ipv6"} | select IpPrefix``IpPrefix
--------
2a05:d07c:2000::/40
2a05:d000:8000::/40
2406:dafe:2000::/40
...`
```

## Get all IPv6 addresses for a specific service

The following example filters the JSON file for the IPv6 addresses for the specified service.

jq

```
`$` `jq -r '.ipv6_prefixes[] | select(.service=="GLOBALACCELERATOR") | .ipv6_prefix' < ip-ranges.json``2600:1f01:4874::/47
2600:1f01:4802::/47
2600:1f01:4860::/47
2600:9000:a800::/40
...`
```

PowerShell

```
`PS C:\>` `Get-AWSPublicIpAddressRange -ServiceKey GLOBALACCELERATOR | where {$_.IpAddressFormat -eq "Ipv6"} | select IpPrefix``IpPrefix
--------
2600:1f01:4874::/47
2600:1f01:4802::/47
2600:1f01:4860::/47
2600:9000:a800::/40
...`
```

## Get all IP addresses for a specific border group

The following example filters the JSON file for all IP addresses for the specified border group.

jq

```
`$` `jq -r '.prefixes[] | select(.network_border_group=="us-west-2-lax-1") | .ip_prefix' < ip-ranges.json``70.224.192.0/18
52.95.230.0/24
15.253.0.0/16
...`
```

PowerShell

```
`PS C:\>` `Get-AWSPublicIpAddressRange | where {$_.NetworkBorderGroup -eq "us-west-2-lax-1"} | select IpPrefix``IpPrefix
--------
70.224.192.0/18
52.95.230.0/24
15.253.0.0/16
...`
```
