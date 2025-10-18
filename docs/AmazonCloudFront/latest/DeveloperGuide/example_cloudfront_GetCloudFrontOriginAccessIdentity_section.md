# Use `GetCloudFrontOriginAccessIdentity` with a CLI

The following code examples show how to use `GetCloudFrontOriginAccessIdentity`.


CLI


**AWS CLI**

**To get a CloudFront origin access identity**


The following example gets the CloudFront origin access identity (OAI) with the
ID `E74FTE3AEXAMPLE`, including its `ETag` and the associated S3 canonical
ID. The OAI ID is returned in the output of the
create-cloud-front-origin-access-identity and
list-cloud-front-origin-access-identities commands.



```
`aws cloudfront get-cloud-front-origin-access-identity --id `E74FTE3AEXAMPLE``

```

Output:



```
{
    "ETag": "E2QWRUHEXAMPLE",
    "CloudFrontOriginAccessIdentity": {
        "Id": "E74FTE3AEXAMPLE",
        "S3CanonicalUserId": "cd13868f797c227fbea2830611a26fe0a21ba1b826ab4bed9b7771c9aEXAMPLE",
        "CloudFrontOriginAccessIdentityConfig": {
            "CallerReference": "cli-example",
            "Comment": "Example OAI"
        }
    }
}
```


* For API details, see
 [GetCloudFrontOriginAccessIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This example returns a specific Amazon CloudFront origin access identity, specified by the -Id parameter. Although the -Id parameter is not required, if you do not specify it, no results are returned.**



```
Get-CFCloudFrontOriginAccessIdentity -Id E3XXXXXXXXXXRT

```

**Output:**



```
      CloudFrontOriginAccessIdentityConfig    Id                                      S3CanonicalUserId
      ------------------------------------    --                                      -----------------
      Amazon.CloudFront.Model.CloudFrontOr... E3XXXXXXXXXXRT                          4b6e...
```


* For API details, see
 [GetCloudFrontOriginAccessIdentity](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This example returns a specific Amazon CloudFront origin access identity, specified by the -Id parameter. Although the -Id parameter is not required, if you do not specify it, no results are returned.**



```
Get-CFCloudFrontOriginAccessIdentity -Id E3XXXXXXXXXXRT

```

**Output:**



```
      CloudFrontOriginAccessIdentityConfig    Id                                      S3CanonicalUserId
      ------------------------------------    --                                      -----------------
      Amazon.CloudFront.Model.CloudFrontOr... E3XXXXXXXXXXRT                          4b6e...
```


* For API details, see
 [GetCloudFrontOriginAccessIdentity](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
