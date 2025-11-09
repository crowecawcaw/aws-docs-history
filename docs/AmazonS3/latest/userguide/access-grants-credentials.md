# Request access to Amazon S3 data through

S3 Access Grants

After you [create an access grant](access-grants-grant.md "access-grants-grant.md") using S3 Access Grants, grantees can request credentials to access the S3
data that they were granted access to. Grantees can be AWS Identity and Access Management (IAM) principals, your corporate directory identities, or authorized applications.

An application or AWS service can use the S3 Access Grants `GetDataAccess` API operation to ask
S3 Access Grants for access to your S3 data on behalf of a grantee. `GetDataAccess` first verifies that you
have granted this identity access to the data. Then, S3 Access Grants uses the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API operation to obtain a temporary
credential token and vends it to the requester. This temporary credential token is an
AWS Security Token Service (AWS STS) token.

The `GetDataAccess` request must include the `target` parameter,
which specifies the scope of the S3 data that the temporary credentials apply to. This
`target` scope can be the same as the scope of the grant or a subset of that
scope, but the `target` scope must be within the scope of the grant that was
given to the grantee. The request must also specify the `permission` parameter
to indicate the permission level for the temporary credentials, whether `READ`,
`WRITE`, or `READWRITE`.

###### Privilege

The requester can specify the privilege level of the temporary token in their credential
request. Using the `privilege` parameter, the requester can reduce or increase
the temporary credentials' scope of access, within the boundaries of the grant scope. The
default value of the `privilege` parameter is `Default`, which means
that the target scope of the credential returned is the original grant scope. The other
possible value for `privilege` is `Minimal`. If the
`target` scope is reduced from the original grant scope, then the temporary
credential is de-scoped to match the `target` scope, as long as the
`target` scope is within the grant scope.

The following table details the effect of the `privilege` parameter on two grants.
One grant has the scope `S3://`amzn-s3-demo-bucket1`/bob/*`, which includes the
entire `bob/` prefix in the `amzn-s3-demo-bucket1` bucket. The other
grant has the scope `S3://`amzn-s3-demo-bucket1`/bob/reports/*`, which includes only
the `bob/reports/` prefix in the `amzn-s3-demo-bucket1` bucket.

| Grant scope                                 | Requested scope                               | Privilege | Returned scope                                | Effect                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------- | --------------------------------------------- | --------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `S3://`amzn-s3-demo-bucket1`/bob/*`         | ``amzn-s3-demo-bucket1`/bob/\*`               | `Default` | ``amzn-s3-demo-bucket1`/bob/\*`               | The requester has access to all objects that have key names that start<br>with the prefix `*bob/*` in the<br>`amzn-s3-demo-bucket1` bucket.                                                                                                                                                                                                             |
| `S3://`amzn-s3-demo-bucket1`/bob/*`         | ``amzn-s3-demo-bucket1`/bob/`                 | `Minimal` | ``amzn-s3-demo-bucket1`/bob/`                 | Without a wild card \<br>• character after the prefix name<br>`bob/`, the requester has access to only the object named<br>`bob/` in the `amzn-s3-demo-bucket1` bucket.<br>It's not common to have such an object. The requester doesn't have<br>access to any other objects, including those that have key names that<br>start with the `bob/` prefix. |
| `S3://`amzn-s3-demo-bucket1`/bob/*`         | ``amzn-s3-demo-bucket1`/bob/images/\*`        | `Minimal` | ``amzn-s3-demo-bucket1`/bob/images/\*`        | The requester has access to all objects that have key names that start<br>with the prefix `*bob/images/\**`in the<br>`amzn-s3-demo-bucket1` bucket.                                                                                                                                                                                                     |
| `S3://`amzn-s3-demo-bucket1`/bob/reports/*` | ``amzn-s3-demo-bucket1`/bob/reports/file.txt` | `Default` | ``amzn-s3-demo-bucket1`/bob/reports/\*`       | The requester has access to all objects that have key names that start<br>with the `bob/reports` prefix in the<br>`amzn-s3-demo-bucket1` bucket, which is the scope of the<br>matching grant.                                                                                                                                                           |
| `S3://`amzn-s3-demo-bucket1`/bob/reports/*` | ``amzn-s3-demo-bucket1`/bob/reports/file.txt` | `Minimal` | ``amzn-s3-demo-bucket1`/bob/reports/file.txt` | The requester has access only to the object with the key name<br>`bob/reports/file.txt` in the<br>`amzn-s3-demo-bucket1` bucket. The requester has no access<br>to any other object.                                                                                                                                                                    |

###### Directory identities

`GetDataAccess` considers all of the identities involved in a request when matching suitable grants. For corporate directory identities, `GetDataAccess` also returns the grants of the IAM identity that is used for the identity-aware session. For more information on identity-aware sessions, see [Granting permissions to use identity-aware console sessions](../../../IAM/latest/UserGuide/id_credentials_temp_control-access_sts-setcontext.md "../../../IAM/latest/UserGuide/id_credentials_temp_control-access_sts-setcontext.md") in the _AWS Identity and Access Management User Guide_. `GetDataAccess` generates credentials restricting scope to the most restrictive grant, as shown in the following table:

| Grant scope for IAM identity               | Grant scope for directory identity     | Requested scope                                      | Returned scope                                       | Privilege | Effect                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------ | -------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `S3://`amzn-s3-demo-bucket1`/bob/*`        | ``amzn-s3-demo-bucket1`/bob/images/\*` | `S3://`amzn-s3-demo-bucket1`/bob/images/image1.jpeg` | `S3://`amzn-s3-demo-bucket1`/bob/images/*`           | `Default` | The requestor has access to all of the objects that have key names that start with the prefix *bob/<br>• as a part of the grant for the IAM role but is restricted to the prefixes *bob/images/<br>• as a part of the grant for the directory identity. Both the IAM role and directory identity provide access to the requested scope, which is `bob/images/image1.jpeg`, but the directory identity has a more restrictive grant. So, the returned scope is restricted to the more restrictive grant for the directory identity. |
| `S3://`amzn-s3-demo-bucket1`/bob/*`        | ``amzn-s3-demo-bucket1`/bob/images/\*` | `S3://`amzn-s3-demo-bucket1`/bob/images/image1.jpeg` | `S3://`amzn-s3-demo-bucket1`/bob/images/image1.jpeg` | `Minimal` | Because the Privilege is set to `Minimal`, even though the identity has access to a bigger scope, only the requested scope is returned `bob/images/image1.jpeg`.                                                                                                                                                                                                                                                                                                                                                                   |
| `S3://`amzn-s3-demo-bucket1`/bob/images/*` | ``amzn-s3-demo-bucket1`/bob/\*`        | `S3://`amzn-s3-demo-bucket1`/bob/images/image1.jpeg` | `S3://`amzn-s3-demo-bucket1`/bob/images/*`           | `Default` | The requestor has access to all of the objects that have key names that start with the prefix *bob/<br>• as a part of the grant for the directory identity but is restricted to the prefixes *bob/images/<br>• as a part of the grant for the IAM role. Both the IAM role and directory identity provide access to the requested scope, which is `bob/images/image1.jpeg`, but the IAM role has a more restrictive grant. So, the returned scope is restricted to the more restrictive grant for the IAM role.                     |
| `S3://`amzn-s3-demo-bucket1`/bob/images/*` | ``amzn-s3-demo-bucket1`/bob/\*`        | `S3://`amzn-s3-demo-bucket1`/bob/images/image1.jpeg` | `S3://`amzn-s3-demo-bucket1`/bob/images/image1.jpeg` | `Minimal` | Because the Privilege is set to `Minimal`, even though the identity has access to a bigger scope, only the requested scope is returned `bob/images/image1.jpeg`.                                                                                                                                                                                                                                                                                                                                                                   |

###### Duration

The `durationSeconds` parameter sets the temporary credential's duration, in
seconds. The default value is `3600` seconds (1 hour), but the requester (the
grantee) can specify a range from `900` seconds (15 minutes) up to
`43200` seconds (12 hours). If the grantee requests a value higher than this
maximum, the request fails.

###### Note

In your request for a temporary token, if the location is an object, set the value of
the `targetType` parameter in your request to `Object`. This
parameter is required only if the location is an object and the privilege level is
`Minimal`. If the location is a bucket or a prefix, you don't need to
specify this parameter.

###### Examples

You can request temporary credentials by using the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and the AWS SDKs. See these examples.

For additional information, see [GetDataAccess](../API/API_control_GetDataAccess.md "../API/API_control_GetDataAccess.md") in the _Amazon Simple Storage Service API Reference_.

To install the AWS CLI, see [Installing the
AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

To use the following example command, replace the `user input
 placeholders` with your own information.

###### Example Request temporary credentials

Request:

```
aws s3control get-data-access \
--account-id `111122223333` \
--target `s3://`amzn-s3-demo-bucket`/prefixA*` \
--permission `READ` \
--privilege Default \
--region `us-east-2`

```

Response:

```
{
"Credentials": {
"AccessKeyId": "`Example-key-id`",
"SecretAccessKey": "`Example-access-key`",
"SessionToken": "`Example-session-token`",
"Expiration": "`2023-06-14T18:56:45+00:00`"},
"MatchedGrantTarget": "`s3://`amzn-s3-demo-bucket`/prefixA*`*",
"Grantee": {
    "GranteeType": "IAM",
    "GranteeIdentifier": "arn:aws:iam::`111122223333`:role/`role-name`"
 }
}
```

For information about the Amazon S3 REST API support for requesting temporary credentials from
S3 Access Grants, see [GetDataAccess](../API/API_control_GetDataAccess.md "../API/API_control_GetDataAccess.md") in the
_Amazon Simple Storage Service API Reference_.

This section provides an example of how grantees request temporary credentials from S3 Access Grants
by using the AWS SDKs.

Java
The following code example returns the temporary credentials that the grantee uses to
access your S3 data. To use this code example, replace the
`user input placeholders`
with your own information.

###### Example Get temporary credentials

Request:

```
public void getDataAccess() {
GetDataAccessRequest getDataAccessRequest = GetDataAccessRequest.builder()
.accountId("`111122223333`")
.permission(Permission.`READ`)
.privilege(Privilege.`MINIMAL`)
.target("`s3://`amzn-s3-demo-bucket`/prefixA*`")
.build();
GetDataAccessResponse getDataAccessResponse = s3Control.getDataAccess(getDataAccessRequest);
LOGGER.info("GetDataAccessResponse: " + getDataAccessResponse);
}
```

Response:

```
GetDataAccessResponse(
Credentials=Credentials(
AccessKeyId="`Example-access-key-id`",
SecretAccessKey="`Example-secret-access-key`",
SessionToken="`Example-session-token`",
Expiration=`2023-06-07T06:55:24Z`
))
```
