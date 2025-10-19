# Logging IAM Identity Center API calls with AWS CloudTrail

AWS IAM Identity Center is integrated with AWS CloudTrail, a service that provides a record of actions taken
 by a user, role, or an AWS service in IAM Identity Center. CloudTrail captures API calls for IAM Identity Center as events.
 The calls captured include calls from the IAM Identity Center console and code calls to the IAM Identity Center API
 operations. If you create a 
 [trail](../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-trails "../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-trails"), 
 you can enable continuous delivery of CloudTrail events to an
 Amazon S3 bucket, including events for IAM Identity Center. If you do not configure a trail, you can still view
 the most recent events in the CloudTrail console in **Event history**. Using the
 information collected by CloudTrail, you can determine the request that was made to IAM Identity Center, the IP
 address from which the request was made, who made the request, when it was made, and
 additional details. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

The following table summarizes the CloudTrail events of IAM Identity Center, their CloudTrail event sources, and
 matching APIs. Refer to the [IAM Identity Center API
 references](https://docs.aws.amazon.com/singlesignon/ "https://docs.aws.amazon.com/singlesignon/") to learn more about the APIs. 

###### Note

There is an additional group of CloudTrail events, referred to as Sign-in, which AWS emits
 for signing in to AWS as an IAM Identity Center user. These events have no matching public APIs, and
 therefore aren't listed in the API references. 



| CloudTrail events | Public APIs | Description | CloudTrail event sources |
| --- | --- | --- | --- |
| [IAM Identity Center](sso-info-in-cloudtrail.md#cloudtrail-events-iam-identity-center-operations "sso-info-in-cloudtrail.md#cloudtrail-events-iam-identity-center-operations") | [IAM Identity Center](../APIReference/welcome.md "../APIReference/welcome.md") | The IAM Identity Center APIs enable the management of permission sets, applications, trusted token issuers, account and application assignments, IAM Identity Center instances, and tags. | `sso.amazonaws.com` |
| [Identity Store](sso-info-in-cloudtrail.md#cloudtrail-events-identity-store-operations "sso-info-in-cloudtrail.md#cloudtrail-events-identity-store-operations") | [Identity Store](../IdentityStoreAPIReference/welcome.md "../IdentityStoreAPIReference/welcome.md") | The Identity Store APIs enable the management of the life cycle of your workforce's users and groups, and the users' group memberships. Also, they support the management of users' MFA devices. | `sso-directory.amazonaws.com`, `identitystore.amazonaws.com` |
| [OIDC](sso-info-in-cloudtrail.md#cloudtrail-events-oidc-operations "sso-info-in-cloudtrail.md#cloudtrail-events-oidc-operations") | [OIDC](../OIDCAPIReference/Welcome.md "../OIDCAPIReference/Welcome.md") | The OIDC APIs support trusted identity propagation, and sign-in to AWS CLI and IDE toolkits as an already authenticated IAM Identity Center user. | `sso.amazonaws.com`, `sso-oauth.amazonaws.com` |
| [AWS access portal](sso-info-in-cloudtrail.md#cloudtrail-events-access-portal-operations "sso-info-in-cloudtrail.md#cloudtrail-events-access-portal-operations") | [AWS access portal](../PortalAPIReference/Welcome.md "../PortalAPIReference/Welcome.md") | The AWS access portal APIs support the operations of the AWS access portal and users getting account credentials through the AWS CLI. | `sso.amazonaws.com` |
| SCIM | [SCIM](../developerguide/what-is-scim.md "../developerguide/what-is-scim.md") | The SCIM APIs support the provisioning of users, groups, and group memberships through the SCIM protocol. See [Logging IAM Identity Center SCIM API calls with AWS CloudTrail](scim-logging-using-cloudtrail.md "scim-logging-using-cloudtrail.md") for more information. | `identitystore-scim.amazonaws.com` |
| [AWS Sign-In](understanding-sign-in-events.md "understanding-sign-in-events.md") | No public API | AWS emits Sign-in CloudTrail events for user authentication and federation flows into IAM Identity Center. | `signin.amazon.com` | ###### Topics <br>• [CloudTrail use cases for IAM Identity Center](sso-cloudtrail-use-cases.md "sso-cloudtrail-use-cases.md") <br>• [IAM Identity Center information in CloudTrail](sso-info-in-cloudtrail.md "sso-info-in-cloudtrail.md")
