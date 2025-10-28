# Use `ListHostedZonesByName` with a CLI

The following code examples show how to use `ListHostedZonesByName`.

CLI

**AWS CLI**

The following command lists up to 100 hosted zones ordered by domain name:

```
`aws route53 list-hosted-zones-by-name`

```

Output:

```
{
  "HostedZones": [
      {
          "ResourceRecordSetCount": 2,
          "CallerReference": "test20150527-2",
          "Config": {
              "Comment": "test2",
              "PrivateZone": false
          },
          "Id": "/hostedzone/Z119WBBTVP5WFX",
          "Name": "2.example.com."
      },
      {
          "ResourceRecordSetCount": 2,
          "CallerReference": "test20150527-1",
          "Config": {
              "Comment": "test",
              "PrivateZone": false
          },
          "Id": "/hostedzone/Z3P5QSUBK4POTI",
          "Name": "www.example.com."
      }
  ],
  "IsTruncated": false,
  "MaxItems": "100"
}
```

The following command lists hosted zones ordered by name, beginning with `www.example.com`:

```
`aws route53 list-hosted-zones-by-name --dns-name `www.example.com``

```

Output:

```
{
  "HostedZones": [
      {
          "ResourceRecordSetCount": 2,
          "CallerReference": "mwunderl20150527-1",
          "Config": {
              "Comment": "test",
              "PrivateZone": false
          },
          "Id": "/hostedzone/Z3P5QSUBK4POTI",
          "Name": "www.example.com."
      }
  ],
  "DNSName": "www.example.com",
  "IsTruncated": false,
  "MaxItems": "100"
}
```

- For API details, see
  [ListHostedZonesByName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones-by-name.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones-by-name.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Returns all of your public and private hosted zones in ASCII order by domain name.**

```
Get-R53HostedZonesByName

```

**Example 2: Returns your public and private hosted zones, in ASCII order by domain name, starting at the specified DNS name.**

```
Get-R53HostedZonesByName -DnsName example2.com

```

- For API details, see
  [ListHostedZonesByName](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Returns all of your public and private hosted zones in ASCII order by domain name.**

```
Get-R53HostedZonesByName

```

**Example 2: Returns your public and private hosted zones, in ASCII order by domain name, starting at the specified DNS name.**

```
Get-R53HostedZonesByName -DnsName example2.com

```

- For API details, see
  [ListHostedZonesByName](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Route 53 with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
