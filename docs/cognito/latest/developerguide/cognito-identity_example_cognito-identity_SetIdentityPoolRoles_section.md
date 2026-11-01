

# Use `SetIdentityPoolRoles` with a CLI
<a name="cognito-identity_example_cognito-identity_SetIdentityPoolRoles_section"></a>

The following code examples show how to use `SetIdentityPoolRoles`.

------
#### [ CLI ]

**AWS CLI**  
**To set identity pool roles**  
The following `set-identity-pool-roles` example sets an identity pool role.  

```
aws cognito-identity set-identity-pool-roles \
    --identity-pool-id {{"us-west-2:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}} \
    --roles authenticated="arn:aws:iam::123456789012:role/Cognito_MyIdentityPoolAuth_Role"
```
This command produces no output.  
For more information, see [IAM roles](https://docs.aws.amazon.com/cognito/latest/developerguide/iam-roles.html) in the *Amazon Cognito Developer Guide*.  
+  For API details, see [SetIdentityPoolRoles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/set-identity-pool-roles.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: Configures the specific Identity Pool to have an unauthenticated IAM role.**  

```
Set-CGIIdentityPoolRole -IdentityPoolId us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1 -Role @{ "unauthenticated" = "arn:aws:iam::123456789012:role/CommonTests1Role" }
```
+  For API details, see [SetIdentityPoolRoles](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: Configures the specific Identity Pool to have an unauthenticated IAM role.**  

```
Set-CGIIdentityPoolRole -IdentityPoolId us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1 -Role @{ "unauthenticated" = "arn:aws:iam::123456789012:role/CommonTests1Role" }
```
+  For API details, see [SetIdentityPoolRoles](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.