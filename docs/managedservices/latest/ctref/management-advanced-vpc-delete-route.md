# VPC | Delete Route

Delete a route in a route table within a VPC.

**Full classification:** Management | Advanced stack components | VPC | Delete route

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-1nusoameibz5p |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

Info not available.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-1nusoameibz5p](schemas.md#ct-1nusoameibz5p-schema-section "schemas.md#ct-1nusoameibz5p-schema-section").

## Example: Required Parameters

```
{
    "DocumentName": "AWSManagedServices-DeleteRoute",
    "Region": "us-east-1",
    "Parameters": {
      "RouteTableId": "rtb-abcdabcdabcdabcda"
    }
  }
```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-DeleteRoute",
  "Region": "us-east-1",
  "Parameters": {
    "RouteTableId": "rtb-abcdabcdabcdabcda",
    "DestinationCidrBlock": "10.0.0.0/8",
    "DestinationPrefixListId": "pl-abcdabcd"
  }
}
```
