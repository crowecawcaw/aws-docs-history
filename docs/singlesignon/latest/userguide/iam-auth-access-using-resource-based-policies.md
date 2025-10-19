# Resource-based policy example for IAM Identity Center
 IAM Identity Center

Every application that works with IAM Identity Center and uses [OAuth 2.0](customermanagedapps-saml2-oauth2.md#oidc-concept "customermanagedapps-saml2-oauth2.md#oidc-concept")
 requires a resource-based policy. The application can be customer managed or AWS managed. The required resource-based policy, called the
 *application policy* (or [ActorPolicy](../APIReference/API_IamAuthenticationMethod.md#API_IamAuthenticationMethod_Contents "../APIReference/API_IamAuthenticationMethod.md#API_IamAuthenticationMethod_Contents") in the APIs), defines which [IAM principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying") are authorized to call IAM authentication method API actions
 such as [`CreateTokenWithIAM`](../OIDCAPIReference/API_CreateTokenWithIAM.md "../OIDCAPIReference/API_CreateTokenWithIAM.md"). The IAM authentication method allows an
 IAM principal, such an IAM role or an AWS service, to authenticate to the IAM Identity Center OIDC
 service by presenting IAM credentials to request or manage access tokens at the
 **/token?aws\_iam=t** endpoint. 

The application policy governs operations for issuing tokens
 (`CreateTokenWithIAM`). The policy also governs permission-only actions that are used only by AWS managed applications for
 validating tokens (`IntrospectTokenWithIAM`) and revoking tokens
 (`RevokeTokenWithIAM`). For a customer managed application, you configure
 this policy by specifying which IAM principals are authorized to call
 `CreateTokenWithIAM`. When an authorized principal calls this API action, the
 principal receives access and refresh tokens for the application. 

If you are using the IAM Identity Center console to set up a customer managed application for [trusted identity propagation](trustedidentitypropagation-overview.md "trustedidentitypropagation-overview.md"), see Step 4 in [Set up customer managed OAuth 2.0 applications](customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md "customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md") for information about how to configure the application policy. For an example policy, see [Example policy: Allow an IAM role to create access
 and refresh tokens](#oauth-application-policy-example "#oauth-application-policy-example") later in this topic.


## Policy requirements


The policy must meet the following requirements:



* The policy must include a `Version` element set to "2012-10-17".
* The policy must include at least one `Statement` element.
* Each policy `Statement` must include the following elements: `Effect`, `Principal`, `Action`, and `Resource`.

## Policy elements


The policy must include the following elements:




**Version**

Specifies the policy document version. Set the version to
 `2012-10-17` (the latest version).



**Statement**

Contains the policy `Statements`. The policy must contain at
 least one `Statement`.


Each policy `Statement` consists of the following elements.




**Effect**

(Required) Determines whether to allow or deny the permissions
 in the policy statement. Valid values are `Allow` or
 `Deny`. 



**Principal**

(Required) The [principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying") is the identity that gets the permissions specified in the
 policy statement. You can specify IAM roles or
 AWS service principals.



**Action**

(Required) The IAM Identity Center OIDC service API operations to allow or deny. Valid actions include:



* `sso-oauth:CreateTokenWithIAM`: This action, which corresponds to the [`CreateTokenWithIAM`](../OIDCAPIReference/API_CreateTokenWithIAM.md "../OIDCAPIReference/API_CreateTokenWithIAM.md") API operation, grants permission to create and return access and refresh tokens for authorized client applications that are authenticated using any IAM entity, such as an AWS service role or user. These tokens might contain defined scopes that specify permissions such as `read:profile` or `write:data`.
* `sso-oauth:IntrospectTokenWithIAM` [permission only]: Grants permission to validate and retrieve information about active OAuth 2.0 access tokens and refresh tokens, including their associated scopes and permissions. This permission is used only by AWS managed applications and is not documented in the *IAM Identity Center OIDC API Reference*.
* `RevokeTokenWithIAM` [permission only]: Grants permission to revoke OAuth 2.0 access tokens and refresh tokens, invalidating them before their normal expiration. This permission is used only by AWS managed applications and is not documented in the *IAM Identity Center OIDC API Reference*.


**Resource**

(Required) In this policy, the value of the
 `Resource` element is `"*"`, which
 means "this application."






For more information about AWS policy syntax, see [AWS IAM Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html") in the
 *IAM User Guide*.


## Example policy: Allow an IAM role to create access
 and refresh tokens


The following permissions policy grants permissions to
 `ExampleAppClientRole`, an IAM role assumed by a workload, to create
 and return access and refresh tokens. 



```
{
    "Version": "2012-10-17", 		 	 	  
    "Statement": [
        {
            "Sid": "AllowRoleToCreateTokens",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/ExampleAppClientRole"
            },
            "Action": "sso-oauth:CreateTokenWithIAM",
            "Resource": "*"
        }
    ]
}

```
