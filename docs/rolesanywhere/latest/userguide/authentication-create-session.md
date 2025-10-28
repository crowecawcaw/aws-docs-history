# IAM Roles Anywhere CreateSession API

The CreateSession API returns temporary security credentials for workloads that have been
authenticated with IAM Roles Anywhere to access AWS resources. For endpoints, see
[Roles Anywhere Endpoints and Quotas](../../../general/latest/gr/rolesanywhere.md "../../../general/latest/gr/rolesanywhere.md").
To get temporary security credentials through this API, see
[Get temporary security credentials from IAM Roles Anywhere](credential-helper.md "credential-helper.md")

## Request Syntax

```

    POST /sessions HTTP/1.1
    Content-type: application/json
    {
      "durationSeconds": `number`,
      "profileArn": `string`,
      "roleArn": `string`,
      "trustAnchorArn": `string`,
      "roleSessionName": `string`,
    }

```

## URI Request Parameters

The request accepts the following as URI parameters or as JSON in the request body. Our examples put these in the request body.

`profileArn`

The Amazon Resource Name (ARN) of the profile.

Type: String

Required: Yes

`roleArn`

The Amazon Resource Name (ARN) of the role to assume.

Type: String

Required: Yes

`trustAnchorArn`

The Amazon Resource Name (ARN) of the trust anchor.

Type: String

Required: Yes

## Request Body

The request accepts the following data in JSON format.

`durationSeconds`

The duration, in seconds, of the role session. The value is optional and can range from 900 seconds (15 minutes) up to 43200 seconds (12 hours).
Please see the `Expiration` subsection of the
[Credentials Object](authentication-create-session.md#credentials-object "authentication-create-session.md#credentials-object")
section for more details on how this value is used in determining the expiration of the vended session.

Type: Number

Required: No

`profileArn`

The Amazon Resource Name (ARN) of the profile.

Type: String

Required: Yes

`roleArn`

The Amazon Resource Name (ARN) of the role to assume.

Type: String

Required: Yes

`sessionName`

_This parameter has been deprecated._

This parameter is no longer used. Instead, use the `roleSessionName` parameter.

Type: String

Required: No

`trustAnchorArn`

The Amazon Resource Name (ARN) of the trust anchor.

Type: String

Required: Yes

`roleSessionName`

An identifier for the role session.

Type: String

Required: No

## Response Syntax

```

    HTTP/1.1 201
    Content-type: application/json
    {
      "credentialSet":[
        {
          "assumedRoleUser": {
          "arn": `ARN`,
          "assumedRoleId": `String`
          },
          "credentials":{
            "accessKeyId": `String`,
            "expiration": `Timestamp`,
            "secretAccessKey": `String`,
            "sessionToken": `String`
          },
          "packedPolicySize": `Number`,
          "roleArn": `ARN`,
          "sourceIdentity": `String`
        }
      ],
      "subjectArn": `ARN`
    }

```

## Response Elements

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

`assumedRoleUser`

The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you can use to refer to the resulting temporary security credentials.

Type: [AssumedRoleUser](../../../STS/latest/APIReference/API_AssumedRoleUser.md "../../../STS/latest/APIReference/API_AssumedRoleUser.md") object

`credentials`

The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.

Type: [Credentials Object](#credentials-object "#credentials-object")

`packedPolicySize`

A percentage value that indicates the packed size of the session policies and session tags combined passed in the request.
The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.

Type: Integer

Valid Range: Minimum value of 0

`sourceIdentity`

The source identity is specified by the principal that is calling the CreateSession operation. For more information on how the source identity is derived please see the
[Trust Model](trust-model.md#role-trusts "trust-model.md#role-trusts") section.

Type: String

Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]+`

`roleArn`

The Amazon Resource Name (ARN) of the assumed role.

Type: String

`subjectArn`

The Amazon Resource Name (ARN) of the Subject resource.

The Subject resource records the history of the principal that is calling the CreateSession operation, including its first recorded authentication time, and last recorded authentication time.

Type: String

## Credentials Object

AWS credentials for API authentication.

`AccessKeyId`

The access key ID that identifies the temporary security credentials.

Type: String

Length Constraints: Minimum length of 16. Maximum length of 128.

Required: Yes

`Expiration`

The time at which the vended credentials expire. This value is determined based on the values set for
`profileDurationSeconds` and `createSessionDurationSeconds`, where
`profileDurationSeconds` is the value of the `durationSeconds` field that's set on the
profile referenced in the call to `CreateSession`, and `createSessionDurationSeconds` is the value
of the `durationSeconds` parameter in the request to `CreateSession`. From this, `finalDurationSeconds`
is determined by the following: `finalDurationSeconds = min(profileDurationSeconds, createSessionDurationSeconds)`,
where `finalDurationSeconds` is the value for `durationSeconds` that
will be sent in the `AssumeRole` request to assume the target role. If `createSessionDurationSeconds` isn't
provided, then `finalDurationSeconds = profileDurationSeconds`. From this, `Expiration`
is determined by the following: `Expiration = CurrentTime + finalDurationSeconds`. Note that if
`finalDurationSeconds` is greater than the maximum session duration (`MaxSessionDuration`) set on the
role, you will receive an error response from the API.

Type: Timestamp

Required: Yes

`SecretAccessKey`

The secret access key that can be used to sign requests.

Type: String

Required: Yes

`SessionToken`

The token that users must pass to the service API to use the temporary credentials.

Type: String

Required: Yes

##

The relationship between CreateSession and AssumeRole

CreateSession is an X.509 wrapper around [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md"). The temporary session credentials are delivered to
RolesAnywhere by AssumeRole, and then passed on without modification in the result of CreateSession.
CreateSession is not included in any SDK or client as there is not yet native SDK or client support for CreateSession's signing process.

The `roleSessionName` option in the CreateSession request allows you to customize the identifier of a role session.
The provided value will be passed into the AssumeRole request during the CreateSession process and will be incorporated into the ARN and ID of the
[assumed role user](../../../STS/latest/APIReference/API_AssumedRoleUser.md "../../../STS/latest/APIReference/API_AssumedRoleUser.md").
This means that subsequent API requests using the temporary session credentials vended by CreateSession will expose the role session name to the corresponding account in their CloudTrail logs.
Also, you can reference these credentials in a resource-based policy by the ARN or the ID.
The default role session name, when not provided, is the serial number of the X.509 certificate provided in a session request.

The `acceptRoleSessionName` option on a profile controls whether or not a role session name will be accepted in a session request with this profile.
By setting the `acceptRoleSessionName` option to `true`, you acknowledge that a role session name will be honored in a session request if the CreateSession call is made with this specific profile.
This means that the default role session name, which is the serial number of the X.509 certificate, will no longer be used and included in the ARN or ID of the assumed role user.

By default, the `acceptRoleSessionName` attached to the profile is `false`.
If you provide a custom role session name in the CreateSession request but custom role session names are not accepted, you will receive an `Access Denied` error.
However, when a role session name is not presented in the CreateSession request, the role session name will default to the serial number of the end-entity X.509 certificate that was used to authenticate the request,
even when the `acceptRoleSessionName` on the profile is `true`.
