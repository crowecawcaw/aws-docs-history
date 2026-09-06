

# Use `AddClientIdToOpenIdConnectProvider` with a CLI
<a name="iam_example_iam_AddClientIdToOpenIdConnectProvider_section"></a>

The following code examples show how to use `AddClientIdToOpenIdConnectProvider`.

------
#### [ CLI ]

**AWS CLI**  
**To add a client ID (audience) to an Open-ID Connect (OIDC) provider**  
The following `add-client-id-to-open-id-connect-provider` command adds the client ID `my-application-ID` to the OIDC provider named `server.example.com`.  

```
aws iam add-client-id-to-open-id-connect-provider \
    --client-id {{my-application-ID}} \
    --open-id-connect-provider-arn {{arn:aws:iam::123456789012:oidc-provider/server.example.com}}
```
This command produces no output.  
To create an OIDC provider, use the `create-open-id-connect-provider` command.  
For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) in the *AWS IAM User Guide*.  
+  For API details, see [AddClientIdToOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-client-id-to-open-id-connect-provider.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This command adds the client ID (or audience) `my-application-ID` to the existing OIDC provider named `server.example.com`.**  

```
Add-IAMClientIDToOpenIDConnectProvider -ClientID "my-application-ID" -OpenIDConnectProviderARN "arn:aws:iam::123456789012:oidc-provider/server.example.com"
```
+  For API details, see [AddClientIdToOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This command adds the client ID (or audience) `my-application-ID` to the existing OIDC provider named `server.example.com`.**  

```
Add-IAMClientIDToOpenIDConnectProvider -ClientID "my-application-ID" -OpenIDConnectProviderARN "arn:aws:iam::123456789012:oidc-provider/server.example.com"
```
+  For API details, see [AddClientIdToOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.