# IAM and AWS STS quotas

AWS Identity and Access Management (IAM) and AWS Security Token Service (STS) have quotas that limit the size of objects. This
affects how you name an object, the number of objects you can create, and the number of
characters you can use when you pass an object.

###### Note

To get account-level information about IAM usage and quotas, use the [GetAccountSummary](../APIReference/API_GetAccountSummary.md "../APIReference/API_GetAccountSummary.md") API operation or the
[get-account-summary](../../../cli/latest/reference/iam/get-account-summary.md "../../../cli/latest/reference/iam/get-account-summary.md") AWS CLI
command.

## IAM name requirements

IAM names have the following requirements and restrictions:

- Policy documents can contain only the following Unicode characters: horizontal tab
  (U+0009), linefeed (U+000A), carriage return (U+000D), and characters in the range U+0020
  to U+00FF.
- Names of users, groups, roles, policies, instance profiles, server certificates, and
  paths must be alphanumeric, including the following common characters: plus (+), equals
  (=), comma (,), period (.), at (@), underscore (\_), and hyphen (-). Path names must begin
  and end with a forward slash (/).
- Names of users, groups, roles, and instance profiles must be unique within the
  account. They aren’t distinguished by case, for example, you can't create groups named
  both `ADMINS` and `admins`.
- The external ID value that a third party uses to assume a role must have a minimum of
  2 characters and a maximum of 1,224 characters. The value must be alphanumeric without
  white space. It can also include the following symbols: plus (+), equal (=), comma (,),
  period (.), at (@), colon (:), forward slash (/), and hyphen (-). For more information
  about the external ID, see [Access to AWS accounts owned by third
  parties](id_roles_common-scenarios_third-party.md "id_roles_common-scenarios_third-party.md").
- Policy names for [inline
  policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md") must be unique to the user, group, or role they're embedded in. The
  names can contain any Basic Latin (ASCII) characters except for the following reserved
  characters: backward slash (\), forward slash (/), asterisk (\*), question mark (?), and
  white space. These characters are reserved according to [RFC 3986, section 2.2](https://datatracker.ietf.org/doc/html/rfc3986#section-2.2 "https://datatracker.ietf.org/doc/html/rfc3986#section-2.2").
- User passwords (login profiles) can contain any Basic Latin (ASCII) characters.
- AWS account ID aliases must be unique across AWS products, and must be
  alphanumeric following DNS naming conventions. An alias must be lowercase, it must not
  start or end with a hyphen, it can't contain two consecutive hyphens, and it can't be a
  12-digit number.

For a list of Basic Latin (ASCII) characters, go to the [Library of Congress
Basic Latin (ASCII) Code Table](https://www.loc.gov/marc/specifications/codetables/BasicLatin.html "https://www.loc.gov/marc/specifications/codetables/BasicLatin.html").

## IAM object quotas

Quotas, also referred to as limits in AWS, are the maximum values for the resources,
actions, and items in your AWS account. Use Service Quotas to manage your IAM quotas.

For the list of IAM service endpoints and service quotas, see [AWS Identity and Access Management endpoints and
quotas](../../../general/latest/gr/iam-service.md "../../../general/latest/gr/iam-service.md") in the _AWS General Reference_.

**To request a quota increase**

1. Follow the sign-in procedure appropriate to your user type as described in the topic
   [How to
   sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_ to sign in to the AWS Management Console.
2. Open the Service Quotas console.
3. In the navigation pane, choose **AWS services**.
4. On the navigation bar, choose the **US East (N. Virginia)** Region. Then
   search for `IAM`.
5. Choose **AWS Identity and Access Management (IAM)**, choose a quota, and follow the
   directions to request a quota increase.

For more information, see [Requesting a Quota Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

To see an example of how to request
an IAM quota increase using the Service Quotas console, watch the following video.

You can request an increase to default quotas for adjustable IAM quotas. Requests up to
the [maximum quota](#autoapproved "#autoapproved") are automatically approved and
completed within a few minutes.

The following table lists the resources for which quota increases area can be
automatically approved.

| Resource                              | Default quota   | Maximum quota   |
| ------------------------------------- | --------------- | --------------- |
| Customer managed policies per account | 1500            | 5000            |
| Groups per account                    | 300             | 500             |
| Instance profiles per account         | 1000            | 5000            |
| Managed policies per role             | 10              | 20              |
| Managed policies per user             | 10              | 20              |
| Managed policies per group            | 10              | 10              |
| Role trust policy length              | 2048 characters | 4096 characters |
| Roles per account                     | 1000            | 5000            |
| Server certificates per account       | 20              | 1000            |

## IAM Access Analyzer quotas

For the list of IAM Access Analyzer service endpoints and service quotas, see [IAM Access Analyzer endpoints
and quotas](../../../general/latest/gr/access-analyzer.md "../../../general/latest/gr/access-analyzer.md") in the _AWS General Reference_.

## IAM Roles Anywhere quotas

For the list of IAM Roles Anywhere service endpoints and service quotas, see [AWS Identity and Access Management Roles Anywhere
endpoints and quotas](../../../general/latest/gr/rolesanywhere.md "../../../general/latest/gr/rolesanywhere.md") in the _AWS General Reference_.

## STS request quotas

The AWS Security Token Service (AWS STS) enforces the following request quotas.

For AWS STS requests made using [AWS credentials](security-creds.md "security-creds.md"), the
default request quota is **600 requests per second**, per
account, per Region. The following AWS STS operations share this quota:

- AssumeRole
- DecodeAuthorizationMessage
- GetAccessKeyInfo
- GetCallerIdentity
- GetFederationToken
- GetSessionToken

###### Note

Requests to AWS STS by AWS service principals, such as those used to assume roles for
use with an AWS service, do not consume STS request per second quota in your
accounts.

For example, if an AWS account makes 100 GetCallerIdentity requests per second and 100
AssumeRole calls per second in the same region, that account is consuming 200 of its available
600 STS requests per second for that region.

For cross-account AssumeRole requests, only the account making the AssumeRole request
impacts the STS quota. The target account does not have any of it’s quota consumed.

To request an increase to STS request quotas, please open a ticket with AWS
support.

###### Note

With the upcoming changes to the AWS STS global endpoint
(`https://sts.amazonaws.com`), requests to the global endpoint will not share a
requests per second (RPS) quota with AWS STS Regional endpoints in Regions that are
[enabled by default](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md"). When a request to the AWS STS global endpoint originates from a
single Region, it will count against the global endpoint's RPS quota. However, when requests
come from multiple Regions, each additional Region will receive its own independent RPS
quota. For more information about the AWS STS global endpoint changes, see [AWS STS global endpoint
changes](id_credentials_temp_region-endpoints.md#reference_sts_global_endpoint_changes "id_credentials_temp_region-endpoints.md#reference_sts_global_endpoint_changes").

## IAM and STS character limits

The following are the maximum character counts and size limits for IAM and AWS STS. You
can't request an increase for the following limits.

| Description                                                                                           | Limit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Alias for an AWS account ID                                                                           | 3–63 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| For [inline<br>policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md") | You can add as many inline policies as you want to an IAM user, role, or group.<br>But the total aggregate policy size (the sum size of all inline policies) per entity<br>can't exceed the following limits:<br>• User policy size can't exceed 2,048 characters.<br>• Role policy size can't exceed 10,240 characters.<br>• Group policy size can't exceed 5,120 characters.<br>NoteIAM doesn't count white space when calculating the size of a policy against<br>these limits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| For [managed policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md")   | • The size of each managed policy can't exceed 6,144 characters.<br>NoteIAM doesn't count white space when calculating the size of a policy against<br>this limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Group name                                                                                            | 128 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Instance profile name                                                                                 | 128 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Password for a login profile                                                                          | 1–128 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Path                                                                                                  | 512 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Policy name                                                                                           | 128 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Role name                                                                                             | 64 charactersImportantIf you intend to use a role with the \*_Switch Role_<br>• feature<br>in the AWS Management Console, then the combined `Path` and `RoleName`<br>can't exceed 64 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Role session duration                                                                                 | 12 hours<br>When you assume a role from the AWS CLI or API, you can use the<br>`duration-seconds` CLI parameter or the `DurationSeconds`<br>API parameter to request a longer role session. You can specify a value from 900<br>seconds (15 minutes) up to the maximum session duration setting for the role, which<br>can range 1–12 hours. If you don't specify a value for the<br>`DurationSeconds` parameter, your security credentials are valid for<br>one hour. IAM users who switch roles in the console are granted the maximum<br>session duration, or the remaining time in the user's session, whichever is less.<br>The maximum session duration setting doesn't limit sessions assumed by AWS<br>services. To learn how to view the maximum value for your role, see [Update the maximum session duration<br>for a role](id_roles_update-role-settings.md#id_roles_update-session-duration "id_roles_update-role-settings.md#id_roles_update-session-duration"). |
| Role session name                                                                                     | 64 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Role [session policies](access_policies.md#policies_session "access_policies.md#policies_session")    | • The size of the passed JSON policy document and all passed managed policy<br>ARN characters combined can't exceed 2,048 characters.<br>• You can pass a maximum of 10 managed policy ARNs when you create a<br>session.<br>• You can pass only one JSON policy document when you programmatically create<br>a temporary session for a role or AWS STS federated user principal.<br>• Additionally, an AWS conversion compresses the passed session policies and<br>session tags into a packed binary format that has **a<br>separate limit**. The `PackedPolicySize` response element<br>indicates by percentage how close the policies and tags for your request are to<br>the upper size limit.<br>• We recommend that you pass session policies using the AWS CLI or AWS API.<br>The AWS Management Console might add additional console session information to the packed<br>policy.                                                                                     |
| Role [session tags](id_session-tags.md "id_session-tags.md")                                          | • Session tags must meet the tag key limit of 128 characters and the tag value<br>limit of 256 characters.<br>• You can pass up to 50 session tags.<br>• An AWS conversion compresses the passed session policies and session tags<br>into a packed binary format that has a separate limit. You can pass session tags<br>using the AWS CLI or AWS API. The `PackedPolicySize` response element<br>indicates by percentage how close the policies and tags for your request are to<br>the upper size limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SAML authentication response base64 encoded                                                           | 100,000 charactersThis character limit applies to [`assume-role-with-saml`](../../../cli/latest/reference/sts/assume-role-with-saml.md "../../../cli/latest/reference/sts/assume-role-with-saml.md") CLI or [`AssumeRoleWithSAML`](../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md "../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md") API operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Tag key                                                                                               | 128 charactersThis character limit applies to tags on IAM resources and<br>[session tags](id_session-tags.md "id_session-tags.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Tag value                                                                                             | 256 charactersThis character limit applies to tags on IAM resources and<br>[session tags](id_session-tags.md "id_session-tags.md").Tag values can be<br>empty which means tag values can have a length of 0 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Unique IDs created by IAM                                                                             | 128 characters. For example:<br>• User IDs that begin with `AIDA`<br>• Group IDs that begin with `AGPA`<br>• Role IDs that begin with `AROA`<br>• Managed policy IDs that begin with `ANPA`<br>• Server certificate IDs that begin with `ASCA`<br>NoteThis isn't intended to be an exhaustive list, nor is it a guarantee that IDs<br>of a certain type begin only with the specified letter combination.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| User name                                                                                             | 64 characters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
