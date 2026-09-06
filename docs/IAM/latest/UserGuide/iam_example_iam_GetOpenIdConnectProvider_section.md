

# Use `GetOpenIdConnectProvider` with a CLI
<a name="iam_example_iam_GetOpenIdConnectProvider_section"></a>

The following code examples show how to use `GetOpenIdConnectProvider`.

------
#### [ CLI ]

**AWS CLI**  
**To return information about the specified OpenID Connect provider**  
This example returns details about the OpenID Connect provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/server.example.com`.  

```
aws iam get-open-id-connect-provider \
    --open-id-connect-provider-arn {{arn:aws:iam::123456789012:oidc-provider/server.example.com}}
```
Output:  

```
{
    "Url": "server.example.com"
        "CreateDate": "2015-06-16T19:41:48Z",
        "ThumbprintList": [
        "12345abcdefghijk67890lmnopqrst987example"
        ],
        "ClientIDList": [
        "example-application-ID"
        ]
}
```
For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) in the *AWS IAM User Guide*.  
+  For API details, see [GetOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-open-id-connect-provider.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example returns details about the OpenID Connect provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/accounts.google.com`. The `ClientIDList` property is a collection that contains all the Client IDs defined for this provider.**  

```
Get-IAMOpenIDConnectProvider -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/oidc.example.com
```
**Output:**  

```
ClientIDList         CreateDate                ThumbprintList                               Url
------------         ----------                --------------                               ---
{MyOIDCApp}          2/3/2015 3:00:30 PM       {12345abcdefghijk67890lmnopqrst98765uvwxy}   oidc.example.com
```
+  For API details, see [GetOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example returns details about the OpenID Connect provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/accounts.google.com`. The `ClientIDList` property is a collection that contains all the Client IDs defined for this provider.**  

```
Get-IAMOpenIDConnectProvider -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/oidc.example.com
```
**Output:**  

```
ClientIDList         CreateDate                ThumbprintList                               Url
------------         ----------                --------------                               ---
{MyOIDCApp}          2/3/2015 3:00:30 PM       {12345abcdefghijk67890lmnopqrst98765uvwxy}   oidc.example.com
```
+  For API details, see [GetOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.