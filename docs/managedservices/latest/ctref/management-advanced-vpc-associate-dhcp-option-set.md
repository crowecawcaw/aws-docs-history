# VPC | Associate DHCP Option Set

This automation document associates a DHCP Option Set with an AWS VPC after validating that domain name servers are within the VPC CIDR range. It lets you specify the VPC ID and the DHCP Option Set ID that you want to associate. This is useful to manage the DHCP configurations of your VPCs while making sure there is network security compliance.

**Full classification:** Management | Advanced stack components | VPC | Associate DHCP Option Set

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-0c2g2npbyyrny |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

Info not available.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0c2g2npbyyrny](schemas.md#ct-0c2g2npbyyrny-schema-section "schemas.md#ct-0c2g2npbyyrny-schema-section").

## Example: Required Parameters

```
{
  "DocumentName": "AWSManagedServices-AssociateDhcpOptionSetWithVpc",
  "Region": "us-east-1",
  "Parameters": {
    "VPCId": "vpc-12345678",
    "DHCPOptionsId": "dopt-12345678"
  }
}

```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-AssociateDhcpOptionSetWithVpc",
  "Region": "us-west-2",
  "Parameters": {
    "VPCId": "vpc-abcdef123456789a",
    "DHCPOptionsId": "dopt-abcdef123456789a"
  }
}

```
