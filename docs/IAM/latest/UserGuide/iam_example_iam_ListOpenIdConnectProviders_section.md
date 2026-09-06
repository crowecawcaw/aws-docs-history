

# Use `ListOpenIdConnectProviders` with a CLI
<a name="iam_example_iam_ListOpenIdConnectProviders_section"></a>

The following code examples show how to use `ListOpenIdConnectProviders`.

------
#### [ CLI ]

**AWS CLI**  
**To list information about the OpenID Connect providers in the AWS account**  
This example returns a list of ARNS of all the OpenID Connect providers that are defined in the current AWS account.  

```
aws iam list-open-id-connect-providers
```
Output:  

```
{
    "OpenIDConnectProviderList": [
        {
            "Arn": "arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com"
        }
    ]
}
```
For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) in the *AWS IAM User Guide*.  
+  For API details, see [ListOpenIdConnectProviders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-open-id-connect-providers.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example returns a list of ARNS of all the OpenID Connect providers that are defined in the current AWS account.**  

```
Get-IAMOpenIDConnectProviderList
```
**Output:**  

```
Arn
---
arn:aws:iam::123456789012:oidc-provider/server.example.com
arn:aws:iam::123456789012:oidc-provider/another.provider.com
```
+  For API details, see [ListOpenIdConnectProviders](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example returns a list of ARNS of all the OpenID Connect providers that are defined in the current AWS account.**  

```
Get-IAMOpenIDConnectProviderList
```
**Output:**  

```
Arn
---
arn:aws:iam::123456789012:oidc-provider/server.example.com
arn:aws:iam::123456789012:oidc-provider/another.provider.com
```
+  For API details, see [ListOpenIdConnectProviders](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.