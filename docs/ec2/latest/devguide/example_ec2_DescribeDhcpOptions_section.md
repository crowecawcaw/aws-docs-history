# Use `DescribeDhcpOptions` with a CLI

The following code examples show how to use `DescribeDhcpOptions`.

CLI

**AWS CLI**

**Example 1: To describe your DHCP options**

The following `describe-dhcp-options` example retrieves details about your DHCP options.

```
`aws ec2 describe-dhcp-options`

```

Output:

```
{
    "DhcpOptions": [
        {
            "DhcpConfigurations": [
                {
                    "Key": "domain-name",
                    "Values": [
                        {
                            "Value": "us-east-2.compute.internal"
                        }
                    ]
                },
                {
                    "Key": "domain-name-servers",
                    "Values": [
                        {
                            "Value": "AmazonProvidedDNS"
                        }
                    ]
                }
            ],
            "DhcpOptionsId": "dopt-19edf471",
            "OwnerId": "111122223333"
        },
        {
            "DhcpConfigurations": [
                {
                    "Key": "domain-name",
                    "Values": [
                        {
                            "Value": "us-east-2.compute.internal"
                        }
                    ]
                },
                {
                    "Key": "domain-name-servers",
                    "Values": [
                        {
                            "Value": "AmazonProvidedDNS"
                        }
                    ]
                }
            ],
            "DhcpOptionsId": "dopt-fEXAMPLE",
            "OwnerId": "111122223333"
        }
    ]
}
```

For more information, see [Working with DHCP Option Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md#DHCPOptionSet "../../../vpc/latest/userguide/VPC_DHCP_Options.md#DHCPOptionSet") in the _AWS VPC User Guide_.

**Example 2: To describe your DHCP options and filter the output**

The following `describe-dhcp-options` example describes your DHCP options and uses a filter to return only DHCP options that have `example.com` for the domain name server. The example uses the `--query` parameter to display only the configuration information and ID in the output.

```
`aws ec2 describe-dhcp-options \
 --filters `Name=key,Values=domain-name-servers` `Name=value,Values=example.com` \
 --query `"DhcpOptions[*].[DhcpConfigurations,DhcpOptionsId]"``

```

Output:

```
[
    [
        [
            {
                "Key": "domain-name",
                "Values": [
                    {
                        "Value": "example.com"
                    }
                ]
            },
            {
                "Key": "domain-name-servers",
                "Values": [
                    {
                        "Value": "172.16.16.16"
                    }
                ]
            }
        ],
        "dopt-001122334455667ab"
    ]
]
```

For more information, see [Working with DHCP Option Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md#DHCPOptionSet "../../../vpc/latest/userguide/VPC_DHCP_Options.md#DHCPOptionSet") in the _AWS VPC User Guide_.

- For API details, see
  [DescribeDhcpOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-dhcp-options.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-dhcp-options.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists your DHCP options sets.**

```
Get-EC2DhcpOption

```

**Output:**

```
DhcpConfigurations                    DhcpOptionsId    Tag
------------------                    -------------    ---
{domain-name, domain-name-servers}    dopt-1a2b3c4d    {}
{domain-name, domain-name-servers}    dopt-2a3b4c5d    {}
{domain-name-servers}                 dopt-3a4b5c6d    {}
```

**Example 2: This example gets configuration details for the specified DHCP options set.**

```
(Get-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d).DhcpConfigurations

```

**Output:**

```
Key                    Values
---                    ------
domain-name            {abc.local}
domain-name-servers    {10.0.0.101, 10.0.0.102}
```

- For API details, see
  [DescribeDhcpOptions](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists your DHCP options sets.**

```
Get-EC2DhcpOption

```

**Output:**

```
DhcpConfigurations                    DhcpOptionsId    Tag
------------------                    -------------    ---
{domain-name, domain-name-servers}    dopt-1a2b3c4d    {}
{domain-name, domain-name-servers}    dopt-2a3b4c5d    {}
{domain-name-servers}                 dopt-3a4b5c6d    {}
```

**Example 2: This example gets configuration details for the specified DHCP options set.**

```
(Get-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d).DhcpConfigurations

```

**Output:**

```
Key                    Values
---                    ------
domain-name            {abc.local}
domain-name-servers    {10.0.0.101, 10.0.0.102}
```

- For API details, see
  [DescribeDhcpOptions](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
