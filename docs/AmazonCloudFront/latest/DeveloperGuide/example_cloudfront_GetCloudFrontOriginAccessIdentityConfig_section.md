# Use `GetCloudFrontOriginAccessIdentityConfig` with a CLI

The following code examples show how to use `GetCloudFrontOriginAccessIdentityConfig`.

CLI

**AWS CLI**

**To get a CloudFront origin access identity configuration**

The following example gets metadata about the CloudFront origin access identity
(OAI) with the ID `E74FTE3AEXAMPLE`, including its `ETag`. The OAI ID is
returned in the output of the
create-cloud-front-origin-access-identity and
list-cloud-front-origin-access-identities commands.

```
`aws cloudfront get-cloud-front-origin-access-identity-config --id `E74FTE3AEXAMPLE``

```

Output:

```
{
    "ETag": "E2QWRUHEXAMPLE",
    "CloudFrontOriginAccessIdentityConfig": {
        "CallerReference": "cli-example",
        "Comment": "Example OAI"
    }
}
```

- For API details, see
  [GetCloudFrontOriginAccessIdentityConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity-config.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity-config.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns configuration information about a single Amazon CloudFront origin access identity, specified by the -Id parameter. Errors occur if no -Id parameter is specified..**

```
Get-CFCloudFrontOriginAccessIdentityConfig -Id E3XXXXXXXXXXRT

```

**Output:**

```
      CallerReference                                             Comment
      ---------------                                             -------
      mycallerreference: 2/1/2011 1:16:32 PM                      Caller reference: 2/1/2011 1:16:32 PM
```

- For API details, see
  [GetCloudFrontOriginAccessIdentityConfig](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns configuration information about a single Amazon CloudFront origin access identity, specified by the -Id parameter. Errors occur if no -Id parameter is specified..**

```
Get-CFCloudFrontOriginAccessIdentityConfig -Id E3XXXXXXXXXXRT

```

**Output:**

```
      CallerReference                                             Comment
      ---------------                                             -------
      mycallerreference: 2/1/2011 1:16:32 PM                      Caller reference: 2/1/2011 1:16:32 PM
```

- For API details, see
  [GetCloudFrontOriginAccessIdentityConfig](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using CloudFront with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
