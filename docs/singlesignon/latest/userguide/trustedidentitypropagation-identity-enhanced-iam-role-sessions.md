# Identity-enhanced IAM role sessions

The [AWS Security Token Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html") (STS) enables an application to obtain an
 identity-enhanced IAM role session. Identity-enhanced role sessions have
 an added identity context that carries a user identifier to the
 AWS service that it calls. AWS services can look up the group
 memberships and attributes of the user in IAM Identity Center and use them to authorize
 the user’s access to resources.

AWS applications obtain identity-enhanced role sessions by making
 requests to the AWS STS [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html")
 API action and passing a context assertion with the user’s identifier
 (`userId`) in the `ProvidedContexts` parameter of
 the request to `AssumeRole`. The context assertion is obtained
 from the `idToken` claim received in response to a request to
 `SSO OIDC` to [`CreateTokenWithIAM`](../OIDCAPIReference/API_CreateTokenWithIAM.md "../OIDCAPIReference/API_CreateTokenWithIAM.md"). When an AWS application
 uses an identity-enhanced role session to access a resource, CloudTrail logs the
 `userId`, the initiating session, and the action taken. For
 more information, see [Identity-enhanced IAM role session logging](#trustedidentitypropagation-identity-enhanced-iam-role-session-logging "#trustedidentitypropagation-identity-enhanced-iam-role-session-logging").

###### Topics

* [Types of
 identity-enhanced IAM role sessions](#types-identity-enhanced-iam-role-sessions "#types-identity-enhanced-iam-role-sessions")
* [Identity-enhanced IAM role session logging](#trustedidentitypropagation-identity-enhanced-iam-role-session-logging "#trustedidentitypropagation-identity-enhanced-iam-role-session-logging")

## Types of
 identity-enhanced IAM role sessions


AWS STS can create two different types of identity-enhanced IAM role
 sessions, depending on the context assertion provided to the
 `AssumeRole` request. Applications that have obtained Id
 tokens from IAM Identity Center can add `sts:identiy_context` (recommended)
 or `sts:audit_context` (Supported for backward compatibility)
 to IAM role sessions. An identity-enhanced IAM role session can have
 only one of these context assertions, not both.


### Identity-enhanced IAM role sessions created with
 `sts:identity_context`


When an identity-enhanced role session contains
 `sts:identity_context` the called AWS service
 determines if resource authorization is based on the user who is
 represented in the role session, or if it is based on the role.
 AWS services that support user-based authorization provide the
 application's administrator with controls to assign access to the
 user or to groups for which the user is a member. 


AWS services that do not support user-based authorization
 disregard the `sts:identity_context`. CloudTrail logs the
 userId of the IAM Identity Center user with all actions taken by the role. For
 more information, see [Identity-enhanced IAM role session logging](#trustedidentitypropagation-identity-enhanced-iam-role-session-logging "#trustedidentitypropagation-identity-enhanced-iam-role-session-logging").


To obtain this type of identity-enhanced role session from AWS STS,
 applications provide the value of the
 `sts:identity_context` field in the [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html") request using the
 `ProvidedContexts` request parameter. Use
 `arn:aws:iam::aws:contextProvider/IdentityCenter` as
 the value for `ProviderArn`.


For more information on how the authorization behaves, see the
 documentation for the receiving AWS service.


### Identity-enhanced
 IAM role sessions created with
 `sts:audit_context`


In the past, `sts:audit_context` was used to enable
 AWS services to log the user identity without using it to make an
 authorization decision. AWS services are now able to use a single
 context - `sts:identity_context` - to achieve this as
 well as to make authorization decisions. We recommend using
 `sts:identity_context` in all new deployments of
 trusted identity propagation.


## Identity-enhanced IAM role session logging


When a request is made to an AWS service using an identity-enhanced
 IAM role session, the user's IAM Identity Center `userId` is logged to
 CloudTrail in the `OnBehalfOf` element. The way in which events are
 logged in CloudTrail varies based on the AWS service. Not all AWS services
 log the `onBehalfOf` element.


The following is an example of how a request made to an AWS service
 using an identity-enhanced role session is logged in CloudTrail.



```
"userIdentity": {
      "type": "AssumedRole",
      "principalId": "AROAEXAMPLE:MyRole",
      "arn": "arn:aws:sts::111111111111:assumed-role/MyRole/MySession",
      "accountId": "111111111111",
      "accessKeyId": "ASIAEXAMPLE",
      "sessionContext": {
        "sessionIssuer": {
            "type": "Role",
            "principalId": "AROAEXAMPLE",
            "arn": "arn:aws:iam::111111111111:role/MyRole",
            "accountId": "111111111111",
            "userName": "MyRole"
        },
        "attributes": {
            "creationDate": "2023-12-12T13:55:22Z",
            "mfaAuthenticated": "false"
        }
    },
    "onBehalfOf": {
        "userId": "11111111-1111-1111-1111-1111111111",
        "identityStoreArn": "arn:aws:identitystore::111111111111:identitystore/d-111111111"
    }
}
```
