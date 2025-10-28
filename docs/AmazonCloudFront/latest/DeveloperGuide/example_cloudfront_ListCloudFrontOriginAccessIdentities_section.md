# Use `ListCloudFrontOriginAccessIdentities` with a CLI

The following code examples show how to use `ListCloudFrontOriginAccessIdentities`.

CLI

**AWS CLI**

**To list CloudFront origin access identities**

The following example gets a list of the CloudFront origin access identities
(OAIs) in your AWS account:

```
`aws cloudfront list-cloud-front-origin-access-identities`

```

Output:

```
{
    "CloudFrontOriginAccessIdentityList": {
        "Items": [
            {
                "Id": "E74FTE3AEXAMPLE",
                "S3CanonicalUserId": "cd13868f797c227fbea2830611a26fe0a21ba1b826ab4bed9b7771c9aEXAMPLE",
                "Comment": "Example OAI"
            },
            {
                "Id": "EH1HDMBEXAMPLE",
                "S3CanonicalUserId": "1489f6f2e6faacaae7ff64c4c3e6956c24f78788abfc1718c3527c263bf7a17EXAMPLE",
                "Comment": "Test OAI"
            },
            {
                "Id": "E2X2C9TEXAMPLE",
                "S3CanonicalUserId": "cbfeebb915a64749f9be546a45b3fcfd3a31c779673c13c4dd460911ae402c2EXAMPLE",
                "Comment": "Example OAI #2"
            }
        ]
    }
}
```

- For API details, see
  [ListCloudFrontOriginAccessIdentities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cloud-front-origin-access-identities.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cloud-front-origin-access-identities.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns a list of Amazon CloudFront origin access identities. Because the -MaxItem parameter specifies a value of 2, the results include two identities.**

```
Get-CFCloudFrontOriginAccessIdentityList -MaxItem 2

```

**Output:**

```
IsTruncated : True
Items       : {E326XXXXXXXXXT, E1YWXXXXXXX9B}
Marker      :
MaxItems    : 2
NextMarker  : E1YXXXXXXXXX9B
Quantity    : 2
```

- For API details, see
  [ListCloudFrontOriginAccessIdentities](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns a list of Amazon CloudFront origin access identities. Because the -MaxItem parameter specifies a value of 2, the results include two identities.**

```
Get-CFCloudFrontOriginAccessIdentityList -MaxItem 2

```

**Output:**

```
IsTruncated : True
Items       : {E326XXXXXXXXXT, E1YWXXXXXXX9B}
Marker      :
MaxItems    : 2
NextMarker  : E1YXXXXXXXXX9B
Quantity    : 2
```

- For API details, see
  [ListCloudFrontOriginAccessIdentities](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
