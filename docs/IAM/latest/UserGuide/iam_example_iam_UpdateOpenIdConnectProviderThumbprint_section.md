

# Use `UpdateOpenIdConnectProviderThumbprint` with a CLI
<a name="iam_example_iam_UpdateOpenIdConnectProviderThumbprint_section"></a>

The following code examples show how to use `UpdateOpenIdConnectProviderThumbprint`.

------
#### [ CLI ]

**AWS CLI**  
**To replace the existing list of server certificate thumbprints with a new list**  
This example updates the certificate thumbprint list for the OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com` to use a new thumbprint.  

```
aws iam update-open-id-connect-provider-thumbprint \
    --open-id-connect-provider-arn {{arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com}} \
    --thumbprint-list {{7359755EXAMPLEabc3060bce3EXAMPLEec4542a3}}
```
If your OIDC provider's discovery and JWKS endpoints use different certificates, include thumbprints for both endpoints in the `--thumbprint-list` value.  
This command produces no output.  
For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) in the *AWS IAM User Guide*.  
+  For API details, see [UpdateOpenIdConnectProviderThumbprint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-open-id-connect-provider-thumbprint.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example updates the certificate thumbprint list for the OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com` to use a new thumbprint. The OIDC provider shares the new value when the certificate that is associated with the provider changes.**  

```
Update-IAMOpenIDConnectProviderThumbprint -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com -ThumbprintList 7359755EXAMPLEabc3060bce3EXAMPLEec4542a3
```
+  For API details, see [UpdateOpenIdConnectProviderThumbprint](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example updates the certificate thumbprint list for the OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com` to use a new thumbprint. The OIDC provider shares the new value when the certificate that is associated with the provider changes.**  

```
Update-IAMOpenIDConnectProviderThumbprint -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com -ThumbprintList 7359755EXAMPLEabc3060bce3EXAMPLEec4542a3
```
+  For API details, see [UpdateOpenIdConnectProviderThumbprint](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.