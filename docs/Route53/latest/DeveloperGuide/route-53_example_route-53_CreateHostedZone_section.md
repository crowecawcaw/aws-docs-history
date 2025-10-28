# Use `CreateHostedZone` with a CLI

The following code examples show how to use `CreateHostedZone`.

CLI

**AWS CLI**

**To create a hosted zone**

The following `create-hosted-zone` command adds a hosted zone named `example.com` using the caller reference `2014-04-01-18:47`. The optional comment includes a space, so it must be enclosed in quotation marks:

```
`aws route53 create-hosted-zone --name `example.com` --caller-reference `2014-04-01-18:47` --hosted-zone-config Comment="command-line version"`

```

For more information, see Working with Hosted Zones in the _Amazon Route 53 Developer Guide_.

- For API details, see
  [CreateHostedZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Creates a new hosted zone named 'example.com', associated with a reusable delegation set. Note that you must supply a value for the CallerReference parameter so that requests that need to be retried if necessary without the risk of executing the operation twice. Because the hosted zone is being created in a VPC it is automatically private and you should not set the -HostedZoneConfig_PrivateZone parameter.**

```
$params = @{
    Name="example.com"
    CallerReference="myUniqueIdentifier"
    HostedZoneConfig_Comment="This is my first hosted zone"
    DelegationSetId="NZ8X2CISAMPLE"
    VPC_VPCId="vpc-1a2b3c4d"
    VPC_VPCRegion="us-east-1"
}

New-R53HostedZone @params

```

- For API details, see
  [CreateHostedZone](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Creates a new hosted zone named 'example.com', associated with a reusable delegation set. Note that you must supply a value for the CallerReference parameter so that requests that need to be retried if necessary without the risk of executing the operation twice. Because the hosted zone is being created in a VPC it is automatically private and you should not set the -HostedZoneConfig_PrivateZone parameter.**

```
$params = @{
    Name="example.com"
    CallerReference="myUniqueIdentifier"
    HostedZoneConfig_Comment="This is my first hosted zone"
    DelegationSetId="NZ8X2CISAMPLE"
    VPC_VPCId="vpc-1a2b3c4d"
    VPC_VPCRegion="us-east-1"
}

New-R53HostedZone @params

```

- For API details, see
  [CreateHostedZone](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Route 53 with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
