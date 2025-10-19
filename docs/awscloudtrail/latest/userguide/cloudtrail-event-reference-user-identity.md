# CloudTrail userIdentity element

AWS Identity and Access Management (IAM) provides different types of identities. The `userIdentity`
 element contains details about the type of IAM identity that made the request, and which
 credentials were used. If temporary credentials were used, the element shows how the
 credentials were obtained. 

###### Contents

* [Examples](cloudtrail-event-reference-user-identity.md#cloudtrail-event-reference-user-identity-examples "cloudtrail-event-reference-user-identity.md#cloudtrail-event-reference-user-identity-examples")
* [Fields](cloudtrail-event-reference-user-identity.md#cloudtrail-event-reference-user-identity-fields "cloudtrail-event-reference-user-identity.md#cloudtrail-event-reference-user-identity-fields")
* [Values for AWS STS APIs with SAML and web identity federation](cloudtrail-event-reference-user-identity.md#STS-API-SAML-WIF "cloudtrail-event-reference-user-identity.md#STS-API-SAML-WIF")
* [AWS STS source identity](cloudtrail-event-reference-user-identity.md#STS-API-source-identity "cloudtrail-event-reference-user-identity.md#STS-API-source-identity")
## Examples


**`userIdentity` with IAM user credentials**


The following example shows the `userIdentity` element of a simple request made with the credentials
 of the IAM user named `Alice`.
 



```
"userIdentity": {
    "type": "IAMUser",
    "principalId": "AIDAJ45Q7YFFAREXAMPLE",
    "arn": "arn:aws:iam::123456789012:user/Alice",
    "accountId": "123456789012",
    "accessKeyId": "",
    "userName": "Alice"
}
```

**`userIdentity` with temporary security credentials**


The following example shows a `userIdentity` element for a request made with
 temporary security credentials obtained by assuming an IAM role. The element contains
 additional details about the role that was assumed to get credentials. 



```
"userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAIDPPEZS35WEXAMPLE:AssumedRoleSessionName",
    "arn": "arn:aws:sts::123456789012:assumed-role/RoleToBeAssumed/MySessionName",
    "accountId": "123456789012",
    "accessKeyId": "",
    "sessionContext": {
        "sessionIssuer": {
            "type": "Role",
            "principalId": "AROAIDPPEZS35WEXAMPLE",
            "arn": "arn:aws:iam::123456789012:role/RoleToBeAssumed",
            "accountId": "123456789012",
            "userName": "RoleToBeAssumed"
        },
        "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "20131102T010628Z"
        }    
    }
}
```

**`userIdentity` for a request made on behalf of an IAM Identity Center
 user**


The following example shows a `userIdentity` element for a request made on behalf of an IAM Identity Center user. 



```
"userIdentity": {
    "type": "IdentityCenterUser",
    "accountId": "123456789012",
    "onBehalfOf": {
        "userId": "544894e8-80c1-707f-60e3-3ba6510dfac1",
        "identityStoreArn": "arn:aws:identitystore::123456789012:identitystore/d-9067642ac7" 
    },
    "credentialId": "EXAMPLEVHULjJdTUdPJfofVa1sufHDoj7aYcOYcxFVllWR_Whr1fEXAMPLE"
}
```

To learn more about how you can use `userId`, `identityStoreArn`, and `credentialId`, 
 see [Identifying the user and session in IAM Identity Center user-initiated CloudTrail events](../../../singlesignon/latest/userguide/sso-cloudtrail-use-cases.md#user-session-iam-identity-center "../../../singlesignon/latest/userguide/sso-cloudtrail-use-cases.md#user-session-iam-identity-center")
 
 in the *IAM Identity Center User Guide*.


## Fields


The following fields can appear in a `userIdentity` element.




**`type`**

The type of the identity. The following values are possible:



* `Root` – The request was made with your AWS account credentials. If
 the `userIdentity` type is `Root`, and you set
 an alias for your account, the `userName` field contains
 your account alias. For more information, see [Your
 AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html").
* `IAMUser` – The request was made with the
 credentials of an IAM user.
* `AssumedRole` – The request was made with temporary security
 credentials that were obtained with a role by making a call to the
 AWS Security Token Service (AWS STS) [`AssumeRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html") API. This can include
 [roles
 for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html") and cross-account API access.
* `Role` – The request was made with a persistent IAM identity that
 has specific permissions. The issuer of the role sessions is always
 the role. For more information about roles, see [Roles terms and concepts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html") in the
 *IAM User Guide*.
* `FederatedUser` – The request was made with temporary security
 credentials obtained from a call to the AWS STS [`GetFederationToken`](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html") API. The
 `sessionIssuer` element indicates if the API was
 called with root or IAM user credentials.


For more information about temporary security credentials, see [Temporary Security
 Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html") in the
 *IAM User Guide*.
* `Directory` – The request was made to a directory
 service, and the type is unknown. Directory services include the
 following: Amazon WorkDocs and Amazon Quick Suite.
* `AWSAccount` – The request was made by another AWS account
* `AWSService` – The request was made by an AWS account that belongs
 to an AWS service. For example, AWS Elastic Beanstalk assumes an IAM role in
 your account to call other AWS services on your behalf.
* `IdentityCenterUser` – The request was made on behalf of an IAM Identity Center user.
* `Unknown` – The request was made with an identity type that CloudTrail can't
 determine.

**Optional:** False


`AWSAccount` and `AWSService` appear for `type` in your
 logs when there is cross-account access using an IAM role that you
 own.


###### Example: Cross-account access initiated by another AWS
 account

1. You own an IAM role in your account.
2. Another AWS account switches to that role to assume the role for
 your account.
3. Because you own the IAM role, you receive a log that shows the
 other account assumed the role. The `type` is
 `AWSAccount`. For an example log entry, see [AWS STS API event in CloudTrail log file](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html#stscloudtrailexample "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html#stscloudtrailexample").

###### Example: Cross-account access initiated by an AWS service

1. You own an IAM role in your account.
2. An AWS account owned by an AWS service assumes that
 role.
3. Because you own the IAM role, you receive a log that shows the
 AWS service assumed the role. The `type` is
 `AWSService`.


**`userName`**

The friendly name of the identity that made the call. The value that appears in
 `userName` is based on the value in `type`. The
 following table shows the relationship between `type` and
 `userName`:




| `type` | `userName` | Description |
| --- | --- | --- |
| `Root` (no alias set) | Not present | If you haven't set up an alias for your AWS account, the `userName` field doesn't appear. For more information about account aliases, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html"). Note that the `userName` field can't contain `Root`, because `Root` is an identity type and not a user name. |
| `Root` (alias set) | The account alias | For more information about AWS account aliases, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html"). |
| `IAMUser` | The user name of the IAM user |  |
| `AssumedRole` | Not present | For the `AssumedRole` type, you can find the `userName` field in `sessionContext` as part of the [sessionIssuer](#sessionissuer "#sessionissuer") element. For an example entry, see [Examples](#cloudtrail-event-reference-user-identity-examples "#cloudtrail-event-reference-user-identity-examples"). |
| `Role` | User-defined | The `sessionContext` and `sessionIssuer` section contains information about the identity that issued the session for the role. |
| `FederatedUser` | Not present | The `sessionContext` and `sessionIssuer` section contains information about the identity that issued the session for the federated user. |
| `Directory` | Can be present | For example, the value can be the [account alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html") or email address of the associated [AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html"). |
| `AWSService` | Not present |  |
| `AWSAccount` | Not present |  |
| `IdentityCenterUser` | Not present\* | The `onBehalfOf` section contains information about the IAM Identity Center user ID and identity store ARN for which the call was made. To learn more about how you can use these two fields, see [Identifying the user and session in IAM Identity Center user-initiated CloudTrail events](../../../singlesignon/latest/userguide/sso-cloudtrail-use-cases.md#user-session-iam-identity-center "../../../singlesignon/latest/userguide/sso-cloudtrail-use-cases.md#user-session-iam-identity-center") in the IAM Identity Center User Guide. \* IAM Identity Center emits the `userName` field under the `additionalEventData` element in two sign-in CloudTrail events. For more information, see [Username in sign-in CloudTrail events](../../../singlesignon/latest/userguide/username-sign-in-cloudtrail-events.md "../../../singlesignon/latest/userguide/username-sign-in-cloudtrail-events.md")  in the IAM Identity Center User Guide. |
| `Unknown` | Can be present | For example, the value can be the [account alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html") or email address of the associated [AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html"). | ###### Note The `userName` field contains the string `HIDDEN_DUE_TO_SECURITY_REASONS` when the recorded event is a console sign-in failure caused by incorrect user name input. CloudTrail does not record the contents in this case because the text could contain sensitive information, as in the following examples: <br>• A user accidentally types a password in the user name field. <br>• A user clicks the link for one AWS account's sign-in page, but then types the account number for a different one. <br>• A user accidentally types the account name of a personal email account, a bank sign-in identifier, or some other private ID. **Optional:** True **`principalId`** A unique identifier for the entity that made the call. For requests made with temporary security credentials, this value includes the session name that is passed to the `AssumeRole`, `AssumeRoleWithWebIdentity`, or `GetFederationToken` API call. **Optional:** True **`arn`** The Amazon Resource Name (ARN) of the principal that made the call. The last section of the arn contains the user or role that made the call. **Optional:** True **`accountId`** The account that owns the entity that granted permissions for the request. If the request was made with temporary security credentials, this is the account that owns the IAM user or role used to obtain credentials. If the request was made with an IAM Identity Center authorized access token, this is the account that owns the IAM Identity Center instance. **Optional:** True **`accessKeyId`** The access key ID that was used to sign the request. If the request was made with temporary security credentials, this is the access key ID of the temporary credentials. For security reasons, `accessKeyId` might not be present, or might be displayed as an empty string. **Optional:** True **`sessionContext`** If the request was made with temporary security credentials, `sessionContext` provides information about the session created for those credentials. You create a session when you call any API that returns temporary credentials. Users also create sessions when they work in the console and make requests with APIs that include [multi-factor authentication](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"). The following attributes can appear in `sessionContext`: <br>• `sessionIssuer` – If a user make a request with temporary security credentials, `sessionIssuer` provides information about how the user obtained credentials. For example, if the they obtained temporary security credentials by assuming a role, this element provides information about the assumed role. If they obtained credentials with root or IAM user credentials to call AWS STS `GetFederationToken`, the element provides information about the root account or IAM user. This element has the following attributes: + `type` – The source of the temporary security credentials, such as `Root`, `IAMUser`, or `Role`. + `userName` – The friendly name of the user or role that issued the session. The value that appears depends on the `sessionIssuer` identity `type`. The following table shows the relationship between `sessionIssuer type` and `userName`:
| `sessionIssuer` type | `userName` | Description |
| --- | --- | --- |
| `Root` (no alias set) | Not present | If you have not set up an alias for your account, the `userName` field does not appear. For more information about AWS account aliases, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html"). Note that the `userName` field can't contain `Root`, because `Root` is an identity type, not a user name. |
| `Root` (alias set) | The account alias | For more information about AWS account aliases, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html"). |
| `IAMUser` | The user name of the IAM user | This also applies when a federated user is using a session issued by `IAMUser`. |
| `Role` | The role name | A role assumed by an IAM user, AWS service, or web identity federated user in a role session. | + `principalId` – The internal ID of the entity used to get credentials. + `arn` – The ARN of the source (account, IAM user, or role) that was used to get temporary security credentials. + `accountId` – The account that owns the entity that was used to get credentials. <br>• `webIdFederationData` – If the request was made with temporary security credentials obtained by [web identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html"), `webIdFederationData` lists information about the identity provider. This element has the following attributes: + `federatedProvider` – The principal name of the identity provider (for example, `www.amazon.com` for Login with Amazon or `accounts.google.com` for Google). + `attributes` – The application ID and user ID as reported by the provider (for example, `www.amazon.com:app_id` and `www.amazon.com:user_id` for Login with Amazon). ###### Note The omission of this field or presence of this field with an empty value signifies that there is no information about the identity provider. <br>• `assumedRoot` – The value is `true` for a temporary session when a management account or delegated administrator calls AWS STS [`AssumedRoot`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html"). For more information, see [Track privileged tasks in CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html") in the *IAM User Guide*. This is an optional field. <br>• `attributes` – The attributes for the session. + `creationDate` – The date and time when the temporary security credentials were issued. Represented in ISO 8601 basic notation. + `mfaAuthenticated` – The value is `true` if the root user or IAM user who used their credentials for the request also authenticated with an MFA device; otherwise, `false`. <br>• `sourceIdentity` – See [AWS STS source identity](#STS-API-source-identity "#STS-API-source-identity") in this topic. The `sourceIdentity` field occurs in events when users assume an IAM role to perform an action. `sourceIdentity` identifies the original user identity making the request, whether that user's identity is an IAM user, an IAM role, a user authenticated through SAML-based federation, or a user authenticated through OpenID Connect (OIDC)-compliant web identity federation. For more information about configuring AWS STS to collect source identity information, see [Monitor and control actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html") in the *IAM User Guide*. <br>• `ec2RoleDelivery` – The value is `1.0` if the credentials were provided by Amazon EC2 Instance Metadata Service Version 1 (IMDSv1). The value is `2.0` if the credentials were provided using the new IMDS scheme. AWS credentials provided by the Amazon EC2 Instance Metadata Service (IMDS) include an ec2:RoleDelivery IAM context key. This context key makes it easy to enforce use of the new scheme on a service-by-service or resource-by-resource basis by using the context key as a condition in IAM policies, resource policies, or AWS Organizations service control policies. For more information, see [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html") in the *Amazon EC2 User Guide*. **Optional:** True **`invokedBy`** The name of the AWS service that made the request, when a request is made by an AWS service such as Amazon EC2 Auto Scaling or AWS Elastic Beanstalk. This field is only present when a request is made by an AWS service. This includes requests made by services using forward access sessions (FAS), AWS service principals, service-linked roles, or service roles used by an AWS service. **Optional:** True **`onBehalfOf`** If the request was made by an IAM Identity Center caller, `onBehalfOf` provides information about the IAM Identity Center user ID and identity store ARN for which the call was made. This element has the following attributes: <br>• `userId` – The ID of the IAM Identity Center user who the call was made on behalf of. <br>• `identityStoreArn` – The ARN of the IAM Identity Center identity store that the call was made on behalf of. **Optional:** True **`inScopeOf`** If the request was made in scope of an AWS service, such as Lambda or Amazon ECS, it provides information about the resource or credentials related to the request. This element can contain the following attributes: <br>• `sourceArn` – The ARN of the resource that invoked the service-to-service request. <br>• `sourceAccount` – The owner account ID for the `sourceArn`. It appears together with `sourceArn`. <br>• `issuerType` – The resource type of `credentialsIssuedTo`. For example, `AWS::Lambda::Function`. <br>• `credentialsIssuedTo` – The resource related to the environment where the credentials were issued. **Optional:** True **`credentialId`** The credential ID for the request. This is only set when the caller uses a bearer token, such as an IAM Identity Center authorized access token. **Optional:** True ## Values for AWS STS APIs with SAML and web identity federation AWS CloudTrail supports logging AWS Security Token Service (AWS STS) API calls made with Security Assertion Markup Language (SAML) and web identity federation. When a user makes a call to the [`AssumeRoleWithSAML`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html") and [`AssumeRoleWithWebIdentity`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html") APIs, CloudTrail records the call and delivers the event to your Amazon S3 bucket. The `userIdentity` element for these APIs contains the following values. **`type`** The identity type. <br>• `SAMLUser` – The request was made with SAML assertion. <br>• `WebIdentityUser` – The request was made by a web identity federation provider. **`principalId`** A unique identifier for the entity that made the call. <br>• For `SAMLUser`, this is a combination of the `saml:namequalifier` and `saml:sub` keys. <br>• For `WebIdentityUser`, this is a combination of the issuer, application ID, and user ID. **`userName`** The name of the identity that made the call. <br>• For `SAMLUser`, this is the `saml:sub` key. <br>• For `WebIdentityUser`, this is the user ID. **`identityProvider`** The principal name of the external identity provider. This field appears only for `SAMLUser` or `WebIdentityUser` types. <br>• For `SAMLUser`, this is the `saml:namequalifier` key for the SAML assertion. <br>• For `WebIdentityUser`, this is the issuer name of the web identity federation provider. This can be a provider that you configured, such as the following: + `cognito-identity.amazon.com` for Amazon Cognito + `www.amazon.com` for Login with Amazon + `accounts.google.com` for Google + `graph.facebook.com` for Facebook The following is an example `userIdentity` element for the `AssumeRoleWithWebIdentity` action. ``` "userIdentity": { "type": "WebIdentityUser", "principalId": "accounts.google.com:`application-id`.apps.googleusercontent.com:`user-id`", "userName": "`user-id`", "identityProvider": "accounts.google.com" } ``` For example logs of how the `userIdentity` element appears for `SAMLUser` and `WebIdentityUser` types, see [Logging IAM and AWS STS API calls with AWS CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"). ## AWS STS source identity An IAM administrator can configure AWS Security Token Service to require that users specify their identity when they use temporary credentials to assume roles. The `sourceIdentity` ﬁeld occurs in events when users assume an IAM role or perform any actions with the assumed role. The `sourceIdentity` field identifies the original user identity making the request, whether that user's identity is an IAM user, an IAM role, a user authenticated by using SAML-based federation, or a user authenticated by using OpenID Connect (OIDC)-compliant web identity federation. After the IAM administrator configures AWS STS, CloudTrail logs `sourceIdentity` information in the following events and locations within the event record: <br>• The AWS STS `AssumeRole`, `AssumeRoleWithSAML`, or `AssumeRoleWithWebIdentity` calls that a user identity makes when it assumes a role. `sourceIdentity` is found in the `requestParameters` block of the AWS STS calls. <br>• The AWS STS `AssumeRole`, `AssumeRoleWithSAML`, or `AssumeRoleWithWebIdentity` calls that a user identity makes if it uses a role to assume another role, known as [role chaining](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-role-chaining "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-role-chaining"). `sourceIdentity` is found in the `requestParameters` block of the AWS STS calls. <br>• The AWS service API calls that the user identity makes while assuming a role and using the temporary credentials assigned by AWS STS. In service API events, `sourceIdentity` is found in the `sessionContext` block. For example, if a user identity creates a new S3 bucket, `sourceIdentity` occurs in the `sessionContext` block of the `CreateBucket` event. For more information about how to configure AWS STS to collect source identity information, see [Monitor and control actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html") in the *IAM User Guide*. For more information about AWS STS events that are logged to CloudTrail, see [Logging IAM and AWS STS API calls with AWS CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html") in the *IAM User Guide*. The following are example snippets of events that show the `sourceIdentity` field. **Example `requestParameters` section** In the following example event snippet, a user makes an AWS STS `AssumeRole` request, and sets a source identity, represented here by ``source-identity-value-set``. The user assumes a role represented by the role ARN `arn:aws:iam::123456789012:role/Assumed_Role`. The `sourceIdentity` field is in the `requestParameters` block of the event. ``` "eventVersion": "1.05", "userIdentity": { "type": "AWSAccount", "principalId": "AIDAJ45Q7YFFAREXAMPLE", "accountId": "123456789012" }, "eventTime": "2020-04-02T18:20:53Z", "eventSource": "sts.amazonaws.com", "eventName": "AssumeRole", "awsRegion": "us-east-1", "sourceIPAddress": "203.0.113.64", "userAgent": "aws-cli/1.16.96 Python/3.6.0 Windows/10 botocore/1.12.86", "requestParameters": { "roleArn": "arn:aws:iam::123456789012:role/Assumed_Role", "roleSessionName": "Test1", "sourceIdentity": "`source-identity-value-set`", }, ``` **Example `responseElements` section** In the following example event snippet, a user makes an AWS STS `AssumeRole` request to assume a role named `Developer_Role`, and sets a source identity, `Admin`. The user assumes a role represented by the role ARN `arn:aws:iam::111122223333:role/Developer_Role`. The `sourceIdentity` field is shown in both the `requestParameters` and `responseElements` blocks of the event. The temporary credentials used to assume the role, the session token string, and the assumed role ID, session name, and session ARN are shown in the `responseElements` block, along with the source identity. ``` "requestParameters": { "roleArn": "arn:aws:iam::111122223333:role/Developer_Role", "roleSessionName": "Session_Name", "sourceIdentity": "Admin" }, "responseElements": { "credentials": { "accessKeyId": "ASIAIOSFODNN7EXAMPLE", "expiration": "Jan 22, 2021 12:46:28 AM", "sessionToken": "XXYYaz... EXAMPLE_SESSION_TOKEN XXyYaZAz" }, "assumedRoleUser": { "assumedRoleId": "AROACKCEVSQ6C2EXAMPLE:Session_Name", "arn": "arn:aws:sts::111122223333:assumed-role/Developer_Role/Session_Name" }, "sourceIdentity": "Admin" } ... ``` **Example `sessionContext` section** In the following example event snippet, a user is assuming a role named `DevRole` to call an AWS service API. The user sets a source identity, represented here by `source-identity-value-set`. The `sourceIdentity` field is in the `sessionContext` block, within the `userIdentity` block of the event. ``` { "eventVersion": "1.08", "userIdentity": { "type": "AssumedRole", "principalId": "AROAJ45Q7YFFAREXAMPLE: Dev1", "arn": "arn: aws: sts: : 123456789012: assumed-role/DevRole/Dev1", "accountId": "123456789012", "accessKeyId": "ASIAIOSFODNN7EXAMPLE", "sessionContext": { "sessionIssuer": { "type": "Role", "principalId": "AROAJ45Q7YFFAREXAMPLE", "arn": "arn: aws: iam: : 123456789012: role/DevRole", "accountId": "123456789012", "userName": "DevRole" }, "webIdFederationData": {}, "attributes": { "mfaAuthenticated": "false", "creationDate": "2021-02-21T23: 46: 28Z" }, "sourceIdentity": "`source-identity-value-set`" } } } ```
