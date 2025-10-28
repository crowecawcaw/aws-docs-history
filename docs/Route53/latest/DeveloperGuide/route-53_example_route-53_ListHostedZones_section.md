# Use `ListHostedZones` with an AWS SDK or CLI

The following code examples show how to use `ListHostedZones`.

CLI

**AWS CLI**

**To list the hosted zones associated with the current AWS account**

The following `list-hosted-zones` command lists summary information about the first 100 hosted zones that are associated with the current AWS account.:

```
`aws route53 list-hosted-zones`

```

If you have more than 100 hosted zones, or if you want to list them in groups smaller than 100, include the `--max-items` parameter. For example, to list hosted zones one at a time, use the following command:

```
`aws route53 list-hosted-zones --max-items `1``

```

To view information about the next hosted zone, take the value of `NextToken` from the response to the previous command, and include it in the `--starting-token` parameter, for example:

```
`aws route53 list-hosted-zones --max-items `1` --starting-token `Z3M3LMPEXAMPLE``

```

- For API details, see
  [ListHostedZones](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Outputs all of your public and private hosted zones.**

```
Get-R53HostedZoneList

```

**Example 2: Outputs all of the hosted zones that are associated with the reusable delegation set that has the ID NZ8X2CISAMPLE**

```
Get-R53HostedZoneList -DelegationSetId NZ8X2CISAMPLE

```

- For API details, see
  [ListHostedZones](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Outputs all of your public and private hosted zones.**

```
Get-R53HostedZoneList

```

**Example 2: Outputs all of the hosted zones that are associated with the reusable delegation set that has the ID NZ8X2CISAMPLE**

```
Get-R53HostedZoneList -DelegationSetId NZ8X2CISAMPLE

```

- For API details, see
  [ListHostedZones](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/route53#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/route53#code-examples").

```
async fn show_host_info(client: &aws_sdk_route53::Client) -> Result<(), aws_sdk_route53::Error> {
    let hosted_zone_count = client.get_hosted_zone_count().send().await?;

    println!(
        "Number of hosted zones in region : {}",
        hosted_zone_count.hosted_zone_count(),
    );

    let hosted_zones = client.list_hosted_zones().send().await?;

    println!("Zones:");

    for hz in hosted_zones.hosted_zones() {
        let zone_name = hz.name();
        let zone_id = hz.id();

        println!("  ID :   {}", zone_id);
        println!("  Name : {}", zone_name);
        println!();
    }

    Ok(())
}


```

- For API details, see
  [ListHostedZones](https://docs.rs/aws-sdk-route53/latest/aws_sdk_route53/client/struct.Client.html#method.list_hosted_zones "https://docs.rs/aws-sdk-route53/latest/aws_sdk_route53/client/struct.Client.html#method.list_hosted_zones")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Route 53 with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
