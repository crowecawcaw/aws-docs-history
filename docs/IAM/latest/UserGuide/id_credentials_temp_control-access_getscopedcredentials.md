

# Permissions for GetScopedCredentials

The `GetScopedCredentials` operation is called with existing temporary security credentials and returns a new set of temporary security credentials for the same session. You can use it to give a workload, agent, or process fewer permissions than the session it runs in, without assuming another role. The resulting credentials keep the identity of the calling session, including the session ARN, role session name, and session tags, but have reduced permissions, a shorter session duration, or both.

The permissions for the temporary security credentials that are returned by `GetScopedCredentials` are determined by the intersection of the following:
+ The effective permissions of the calling session (which itself may already be constrained by identity policies, session policies, permissions boundaries, SCPs, RCPs, and VPC endpoint policies).
+ The scope down policy you pass in the `GetScopedCredentials` request.
+ Any scope down policies applied by prior `GetScopedCredentials` calls in the chain (if called recursively).

![Three overlapping circles for a recursive call. They are the effective permissions of the calling session, the scope down policies from earlier calls, and the scope down policy from this call. The region shared by all three is the permissions of the resulting credentials.](https://docs.aws.amazon.com/IAM/latest/UserGuide/images/GetScopedCredentials-scope-down-recursive-call.png)


The resulting credentials can never have more permissions than the calling session. The scope down policy can only restrict permissions further and cannot grant new permissions.

## How policy evaluation works
<a name="id_credentials_temp_control-access_getscopedcredentials_evaluation"></a>

`GetScopedCredentials` adds the scope down policy you provide as a new scope down layer on the resulting session. This layer intersects with all existing policies that apply to the session. An action is allowed only if every layer permits it.

`GetScopedCredentials` scope down policies differ from `AssumeRole` session policies in two ways:

1. Each time you call `AssumeRole` with a session policy, the new session policies replace the ones on the calling session. However, with `GetScopedCredentials`, each call's scope down policy is added as an independent layer that intersects with all prior layers. Prior restrictions are never removed.

1. When you scope down permissions by re-assuming a role with a session policy, role chaining caps the resulting session duration to a maximum of one hour. `GetScopedCredentials` does not impose this cap. When you do not specify a duration, the scoped down credentials keep the calling session's remaining duration. You can also request a shorter session duration, but it cannot exceed the remaining duration of the calling session.

## Calling GetScopedCredentials requires explicit permission
<a name="id_credentials_temp_control-access_getscopedcredentials_permission"></a>

To call `GetScopedCredentials`, the calling principal must have the `sts:GetScopedCredentials` action allowed in its effective permissions. This follows the standard IAM implicit-deny model. If no policy grants this action, the call is denied.

The following is an example of an identity-based policy granting permission to `GetScopedCredentials`:

**Example**  

```json
{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "sts:GetScopedCredentials",
                "Resource": "*"
            }
        ]
    }
```

## Condition keys for GetScopedCredentials
<a name="id_credentials_temp_control-access_getscopedcredentials_conditions"></a>

You can use the `sts:DurationSeconds` condition key to restrict the lifetime of scoped down credentials. For example, an SCP could enforce that scoped down credentials can never be valid for more than 15 minutes.

**Example SCP restricting scoped down credential duration to 900 seconds (15 minutes)**  

```json
{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Deny",
                "Action": "sts:GetScopedCredentials",
                "Resource": "*",
                "Condition": {
                    "NumericGreaterThan": {
                        "sts:DurationSeconds": "900"
                    }
                }
            }
        ]
    }
```

## Identity preservation
<a name="id_credentials_temp_control-access_getscopedcredentials_identity"></a>

`GetScopedCredentials` does not change the identity of the session. The following properties are preserved on the resulting credentials:
+ Principal ARN
+ Role session name
+ Session tags (including transitive tag keys)
+ Source identity
+ Context keys (including `aws:SourceIp` and Trusted Identity Propagation context)

## Restrictions on the resulting credentials
<a name="id_credentials_temp_control-access_getscopedcredentials_restrictions"></a>
+ Permissions can only decrease, never increase.
+ Session lifetime can only decrease, never increase.
+ Session tags cannot be added or modified.
+ Source identity cannot be set or changed.

## Revoking scoped credentials
<a name="id_credentials_temp_control-access_getscopedcredentials_revoking"></a>

Temporary security credentials returned by `GetScopedCredentials` inherit the `aws:TokenIssueTime` context key of the original temporary credentials since `GetScopedCredentials` scopes down an existing session rather than creating a new one. This is also true for credentials returned by recursive `GetScopedCredentials` calls.

You can revoke scoped down credentials together with the parent session since they share the same creation time. When you choose **Revoke active sessions** for a role in the IAM console, IAM attaches the `AWSRevokeOlderSessions` inline policy to the role. This policy uses the `aws:TokenIssueTime` condition key to deny requests made with credentials issued before the time that you revoke the sessions. It applies to every set of scoped down credentials created from those sessions, including credentials from recursive calls. You cannot use `aws:TokenIssueTime` to revoke scoped down credentials separately from the session that they were created from. For more information, see [Revoke IAM role temporary security credentials](id_roles_use_revoke-sessions.md).

The `creationDate` field in your CloudTrail events is mapped from this context key. In the following sample CloudTrail event, the `creationDate` field in `userIdentity.sessionContext.attributes` shows the time when the role session was created, while `eventTime` shows when `GetScopedCredentials` was called.

```json
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROARXXILGLBL5EXAMPLE:jane",
        "arn": "arn:aws:sts::111122223333:assumed-role/Developer/jane",
        "accessKeyId": "ASIAI44QH8DHBEXAMPLE",
        ...,
        "sessionContext": {
            ...,
            "attributes": {
                "creationDate": "2026-10-12T00:00:00Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2026-10-12T02:55:00Z",
    "eventSource": "sts.amazonaws.com",
    "eventName": "GetScopedCredentials",
    "awsRegion": "us-west-2",
    ...
    "requestParameters": {
        "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::amzn-s3-demo-bucket/*\"}]}",
        "scopedSessionDescription": "report-status-job",
        "durationSeconds": 300
    },
    "responseElements": {
        "credentials": {
            "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
            "sessionToken": "IQoJb3JpZ2luX2VjEHMaCXVzL...",
            "expiration": "2026-10-12T03:00:00Z"
        },
        "sessionInfo": {
            "scopedSessionId": "AROARXXILGLBL5EXAMPLE:jane",
            "arn": "arn:aws:sts::111122223333:assumed-role/Developer/jane"
        },
        "sessionTokenUtilization": 17,
        "sessionTokenSize": 724,
        "scopedPoliciesCount": 1
    },
    "readOnly": false,
    ...
}
```

## Using scope down policies with encrypted resources
<a name="id_credentials_temp_control-access_getscopedcredentials_kms-cache"></a>

Some AWS services cache AWS Key Management Service (AWS KMS) data keys using a cache lookup key that doesn't include session-specific context, so a scope down policy that removes AWS KMS permissions might not prevent access to data that the calling session's role accessed recently. For more information, see [Using session-specific context with AWS services that cache data keys](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-aws.html#conditions-aws-session-data-key-caching) in the *AWS Key Management Service Developer Guide*.

## Services not supported by GetScopedCredentials
<a name="id_credentials_temp_control-access_getscopedcredentials_unsupported-services"></a>

Scoped down credentials vended by `GetScopedCredentials` cannot be used with the following services. Calls made to these services may be denied.
+ Amazon MemoryDB
+ AWS Quick
+ Amazon CloudSearch
+ Amazon Neptune Database, on engine versions earlier than 1.2.0.0
+ Amazon OpenSearch Service for the following engine and software versions:
  + Elasticsearch 7.9 through OpenSearch 3.7 on software release earlier than R20260929
  + Elasticsearch 6.2 through 7.8 on software release earlier than R20260720
  + All Elasticsearch versions below 6.2 on software release earlier than R20260626

## Example: Removing specific permissions using a deny list
<a name="id_credentials_temp_control-access_getscopedcredentials_deny-lists"></a>

A common use case for `GetScopedCredentials` is to keep most of the calling session's permissions while removing a few sensitive actions. This approach is called a deny list. For example, you might give an agent credentials that keep the developer's permissions, except terminating instances, deleting resources, or assuming other roles. Because a scope down policy can only reduce permissions, the resulting credentials never have more access than the calling session.

To create a deny list, use a scope down policy with an `Allow` statement that uses the `NotAction` element.

**Example scope down policy that uses Allow with NotAction**  

```json
{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "NotAction": [
                    "ec2:TerminateInstances",
                    "rds:DeleteDBInstance",
                    "s3:DeleteObject",
                    "sts:AssumeRole*"
                ],
                "Resource": "*"
            }
        ]
    }
```

When you pass this policy to `GetScopedCredentials`, the resulting credentials keep the calling session's permissions, except for the listed actions. The effective permissions are:

```
effective permissions = caller's existing permissions ∩ (all actions EXCEPT the excluded ones)
```

This policy has the same effect as an `Allow` statement for all actions combined with a `Deny` statement for the listed actions.

## Same-account resource-based policies
<a name="id_credentials_temp_control-access_getscopedcredentials_same-account-rbp"></a>

**Note**  
When using temporary security credentials vended by `AssumeRole`, access to a resource in the same account can be granted by either a resource-based policy or the identity-based policy. However, for credentials vended by `GetScopedCredentials`, both the identity-based policy and scope down policy must explicitly allow access to the action, regardless of what the resource policy grants. This difference only applies when the resource policy trusts `Principal "*"` or names the session principal directly (for example, `arn:aws:sts::123456789012:assumed-role/MyRole/my-session`).