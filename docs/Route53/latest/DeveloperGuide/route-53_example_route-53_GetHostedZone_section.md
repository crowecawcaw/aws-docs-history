

# Use `GetHostedZone` with a CLI
<a name="route-53_example_route-53_GetHostedZone_section"></a>

The following code examples show how to use `GetHostedZone`.

------
#### [ CLI ]

**AWS CLI**  
**To get information about a hosted zone**  
The following `get-hosted-zone` example gets information about the hosted zone with an `id` of `Z1R8UBAEXAMPLE`.  

```
aws route53 get-hosted-zone \
    --id {{Z1R8UBAEXAMPLE}}
```
Output:  

```
{
    "HostedZone": {
        "Id": "/hostedzone/Z1R8UBAEXAMPLE",
        "Name": "example.com.",
        "CallerReference": "2014-04-01-18:47",
        "Config": {
            "Comment": "command-line version",
            "PrivateZone": false
        },
        "ResourceRecordSetCount": 2
    },
    "DelegationSet": {
        "NameServers": [
            "ns-2048.awsdns-64.com",
            "ns-2049.awsdns-65.net",
            "ns-2050.awsdns-66.org",
            "ns-2051.awsdns-67.co.uk"
        ]
    }
}
```
For more information, see [Working with hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-working-with.html) in the *Amazon Route 53 Developer Guide*.  
+  For API details, see [GetHostedZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: Returns details of the hosted zone with ID Z1D633PJN98FT9.**  

```
Get-R53HostedZone -Id Z1D633PJN98FT9
```
+  For API details, see [GetHostedZone](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: Returns details of the hosted zone with ID Z1D633PJN98FT9.**  

```
Get-R53HostedZone -Id Z1D633PJN98FT9
```
+  For API details, see [GetHostedZone](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Route 53 with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.