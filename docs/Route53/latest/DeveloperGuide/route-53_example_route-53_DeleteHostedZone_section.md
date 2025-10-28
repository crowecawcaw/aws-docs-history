# Use `DeleteHostedZone` with a CLI

The following code examples show how to use `DeleteHostedZone`.

CLI

**AWS CLI**

**To delete a hosted zone**

The following `delete-hosted-zone` command deletes the hosted zone with an `id` of `Z36KTIQEXAMPLE`:

```
`aws route53 delete-hosted-zone --id `Z36KTIQEXAMPLE``

```

- For API details, see
  [DeleteHostedZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-hosted-zone.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-hosted-zone.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Deletes the hosted zone with the specified ID. You will be prompted for confirmation before the command proceeds unless you add the -Force switch parameter.**

```
Remove-R53HostedZone -Id Z1PA6795UKMFR9

```

- For API details, see
  [DeleteHostedZone](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Deletes the hosted zone with the specified ID. You will be prompted for confirmation before the command proceeds unless you add the -Force switch parameter.**

```
Remove-R53HostedZone -Id Z1PA6795UKMFR9

```

- For API details, see
  [DeleteHostedZone](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Route 53 with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
