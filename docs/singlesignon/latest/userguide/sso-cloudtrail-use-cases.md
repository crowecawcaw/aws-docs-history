# CloudTrail use cases for IAM Identity Center

The CloudTrail events that IAM Identity Center emits can be valuable for a variety of use cases.
 Organizations can use these event logs to monitor and audit the user access and activity
 within their AWS environment. This can help compliance use cases, as the logs capture
 details on who is accessing what resources and when. You can also use the CloudTrail data for
 incident investigations, allowing teams to analyze user actions and track suspicious
 behavior. Additionally, the event history can support troubleshooting efforts, providing
 visibility into changes made to user permissions and configurations over time.

The following sections describe the foundational use cases that inform your workflows
 such as audit, incident investigation, and troubleshooting.


## Identifying the user in
 IAM Identity Center user-initiated CloudTrail events


IAM Identity Center emits two CloudTrail fields that enable you to identify the IAM Identity Center user behind the CloudTrail
 events, such as signing into IAM Identity Center or AWS CLI, and using the AWS access portal, including managing
 MFA devices:



* `userId` – The unique and immutable user identifier from the
 Identity Store of an IAM Identity Center instance.
* `identityStoreArn` – The Amazon Resource Name (ARN) of the
 Identity Store that contains the user.

The `userID` and `identityStoreArn` fields display in the
 `onBehalfOf` element nested inside the [`userIdentity`](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") element as shown in the following example CloudTrail
 event log. This event log shows these two fields on an event where the
 `userIdentity` type is "`IdentityCenterUser`". You can also find
 these fields on events for authenticated IAM Identity Center users where the `userIdentity`
 type is "`Unknown`". Your workflows should accept both type values.



```
"userIdentity":{
  "type":"IdentityCenterUser",
  "accountId":"111122223333",
  "onBehalfOf": {
    "userId": "544894e8-80c1-707f-60e3-3ba6510dfac1",
    "identityStoreArn": "arn:aws:identitystore::111122223333:identitystore/d-1234567890"
    },
    "credentialId" : "90e292de-5eb8-446e-9602-90f7c45044f7"
  }

```

###### Tip

We recommend you use `userId` and `identityStoreArn` for
 identifying the user behind IAM Identity Center CloudTrail events. The `userName` and
 `principalId` fields under the `userIdentity` element are no
 longer available. If your workflows, such as audit or incident response, depend on
 having access to the `username`, you have two options:


* Retrieve the username from the IAM Identity Center directory as explained in [Username in sign-in CloudTrail
 events](username-sign-in-cloudtrail-events.md "username-sign-in-cloudtrail-events.md").
* Get the `UserName` that IAM Identity Center emits under the
 `additionalEventData` element in Sign-in. This option doesn't require
 access to the IAM Identity Center directory. For more information, see [Username in sign-in CloudTrail
 events](username-sign-in-cloudtrail-events.md "username-sign-in-cloudtrail-events.md").

To retrieve the details of a user, including the `username` field, you
 query the Identity Store with user ID and Identity Store ID as parameters. You can perform this
 action through the [`DescribeUser`](../IdentityStoreAPIReference/API_DescribeUser.md "../IdentityStoreAPIReference/API_DescribeUser.md") API request or through the CLI. The following is an
 example CLI command. You can omit the `region` parameter if your IAM Identity Center instance
 is in the CLI default Region.



```
aws identitystore describe-user \
--identity-store-id  d-1234567890 \
--user-id  544894e8-80c1-707f-60e3-3ba6510dfac1 \
--region `your-region-id`

```

To determine the Identity Store ID value for the CLI command in the previous example, you
 can extract the Identity Store ID from the `identityStoreArn` value. In the example
 ARN `arn:aws:identitystore::111122223333:identitystore/d-1234567890`, the
 Identity Store ID is `d-1234567890`. Alternatively, you can locate the Identity Store ID
 by navigating to **Identity Store** tab in the **Settings**
 section of the IAM Identity Center console. 


If you are automating the lookup of users in the IAM Identity Center directory, we recommend that you
 estimate the frequency of user lookups, and consider the [IAM Identity Center throttle limit on the Identity Store API](limits.md#ssodirectorylimits "limits.md#ssodirectorylimits"). Caching
 retrieved user attributes can help you stay within the throttle limit.


## Correlating user events within the same user session


The [AuthWorkflowID](understanding-sign-in-events.md "understanding-sign-in-events.md") field emitted in sign-in events enables tracking all 
 CloudTrail events associated with a sign-in sequence before the commencement of an 
 IAM Identity Center user session.


For user actions inside the AWS access portal, the `credentialId` value is 
 set to the ID of the IAM Identity Center user’s session used to request the action. You can use 
 this value to identify CloudTrail events initiated within the same authenticated 
 IAM Identity Center user session in the AWS access portal.


###### Note

You can't use `credentialId` to correlate sign-in events to the subsequent events, such as the use of the 
 AWS access portal. The value of the `credentialId` field emitted in sign-in events has internal use, and we recommend 
 that you not rely on it. The value of the `credentialId` field emitted for [AWS access portal events](sso-info-in-cloudtrail.md#cloudtrail-events-access-portal-operations "sso-info-in-cloudtrail.md#cloudtrail-events-access-portal-operations") invoked with OIDC 
 equals the ID of the access token.


## Identifying user background session details in IAM Identity Center user-initiated CloudTrail events


The following CloudTrail event captures the process of OAuth 2.0 token exchange, in which an existing access token (the `subjectToken`) that represents the user's interactive session is exchanged for a refresh token (the `requestedTokenType`). The refresh token allows any user initiated long-running jobs to continue running with the user's permissions, even after the user signs out. 


For IAM Identity Center [user background sessions](user-background-sessions.md "user-background-sessions.md"), the CloudTrail event includes an additional element called `resource` in the `requestParameters` element. The `resource` parameter contains the Amazon Resource Name (ARN) of the job that runs in the background. This element is present only in CloudTrail event records and is not included in the IAM Identity Center [CreateTokenWithIAM](../OIDCAPIReference/API_CreateTokenWithIAM.md "../OIDCAPIReference/API_CreateTokenWithIAM.md") API or SDK responses.



```
{
  "clientId": "EXAMPLE-CLIENT-ID",
  "grantType": "urn:ietf:params:oauth:grant-type:token-exchange",
  "code": "HIDDEN_DUE_TO_SECURITY_REASONS",
  "redirectUri": "https://example.com/callback",
  "assertion": "HIDDEN_DUE_TO_SECURITY_REASONS",
  "subjectToken": "HIDDEN_DUE_TO_SECURITY_REASONS",
  "subjectTokenType": "urn:ietf:params:oauth:token-type:access_token",
  "requestedTokenType": "urn:ietf:params:oauth:token-type:refresh_token",
  "resource": "arn:aws:sagemaker:us-west-2:123456789012:training-job/my-job"
}

```

## Correlating users between IAM Identity Center and external
 directories


IAM Identity Center provides two user attributes that you can use to correlate a user in its
 directory to the same user in an external directory (for example, Microsoft Active
 Directory and Okta Universal Directory). 



* `externalId` – The external identifier of an IAM Identity Center user. We
 recommend you map this identifier to an immutable user identifier in the external
 directory. Note that IAM Identity Center doesn't emit this value in CloudTrail.
* `username` – A customer-provided value that users usually sign
 in with. The value can change (for example, with a SCIM update). Note that when the
 identity source is AWS Directory Service, the username that IAM Identity Center emits in CloudTrail matches the username
 that you enter to authenticate. The username doesn't need to be an exact match to the
 username in the IAM Identity Center directory. 


 If you have access to the CloudTrail events but not the IAM Identity Center directory, you can use
 the username emitted under the `additionalEventData` element at sign-in.
 For more details about username in `additionalEventData`, refer to [Username in sign-in CloudTrail
 events](username-sign-in-cloudtrail-events.md "username-sign-in-cloudtrail-events.md").

The mapping of these two user attributes to corresponding user attributes in an
 external directory is defined in IAM Identity Center when the identity source is the AWS Directory Service. For
 infomration, see [Attribute mappings between IAM Identity Center and External
 Identity Providers directory](attributemappingsconcept.md "attributemappingsconcept.md"). External IdPs that provision users with SCIM
 have their own mapping. Even if you use the IAM Identity Center directory as the identity source, you
 can use the `externalId` attribute to cross-reference security principals to
 your external directory.


The following section explains how you can look up an IAM Identity Center user given the user’s
 `username` and `externalId`.


## Viewing an IAM Identity Center user by username and
 externalId


You can retrieve user attributes from the IAM Identity Center directory for a known username by
 first requesting a corresponding `userId` using the [`GetUserId`](../IdentityStoreAPIReference/API_GetUserId.md "../IdentityStoreAPIReference/API_GetUserId.md") API request, then issue a [`DescribeUser`](../IdentityStoreAPIReference/API_DescribeUser.md "../IdentityStoreAPIReference/API_DescribeUser.md") API request, as shown in the previous example. The
 following example demonstrates how you can retrieve a `userId` from the
 Identity Store for a specific username. You can omit the `region` parameter if your
 IAM Identity Center instance is in the default Region with the CLI.



```
aws identitystore get-user-id \
    --identity-store d-9876543210 \
    --alternate-identifier '{
      "UniqueAttribute": {
      "AttributePath": "username",
      "AttributeValue": "`anyuser@example.com`"
        }
          }' \
    --`region your-region-id`

```

Similarly, you can use the same mechanism when you know the `externalId`.
 Update the attribute path in the previous example with the `externalId` value,
 and the attribute value with the specific `externalId` for which you are
 searching.


## Viewing a user’s Secure Identifier (SID) in Microsoft
 Active Directory (AD) and externalId


In certain cases, IAM Identity Center emits a user’s SID in the `principalId` field of
 CloudTrail events, such as those that the AWS access portal and OIDC APIs emit. **These cases are being phased out.** We recommend your workflows use the AD
 attribute `objectguid` when you need a unique user identifier from AD. You can
 find this value in the `externalId` attribute in the IAM Identity Center directory. However,
 if your workflows require the use of SID, retrieve the value from AD as it’s not available
 through IAM Identity Center APIs.


[Correlating user events within the same user session](#correlating-users "#correlating-users") describes how
 you can use the `externalId` and `username` fields to correlate an
 IAM Identity Center user to a matching user in an external directory. By default, IAM Identity Center maps
 `externalId` to the `objectguid` attribute in AD, and this mapping
 is fixed. IAM Identity Center allows administrators the flexibility to map `username`
 differently than its default mapping to `userprincipalname` in AD.


You can view these mappings in the IAM Identity Center console. Navigate to the **Identity
 Source** tab of **Settings**, and choose **Manage
 sync** in the **Actions** menu. In the **Manage
 Sync** section, choose the **View attribute mappings** button. 


While you can use any unique AD user identifier available in IAM Identity Center to look up a user
 in AD, we recommend using the `objectguid` in your queries because it is an
 immutable identifier. The following example shows how to query Microsoft AD with
 Powershell to retrieve a user using the user’s `objectguid` value of
 `16809ecc-7225-4c20-ad98-30094aefdbca`. A successful response to this query
 includes the user’s SID.



```
Install-WindowsFeature -Name  RSAT-AD-PowerShell
 
  Get-ADUser `
  -Filter {objectGUID -eq  [GUID]::Parse("16809ecc-7225-4c20-ad98-30094aefdbca")} `
  -Properties *

```
