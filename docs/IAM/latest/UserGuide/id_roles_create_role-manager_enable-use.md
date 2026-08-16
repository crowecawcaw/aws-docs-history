# Manage access to role manager

You control access to role manager at two levels. IAM permissions determine who in an
account can enable role manager and who can use the roles it provides. In an organization,
service control policies (SCPs) determine what member accounts can do.

## Permissions for role manager

To enable or disable role manager, you need the
`iam:PutAccountProperties` permission. The AWS managed policy
`IAMFullAccess` includes it.

To use role manager, a user needs the IAM permissions for the actions that role manager
performs on their behalf. Role manager provides roles through the `AcquireRole`
API, which evaluates each underlying IAM action against the user's permissions:

- If a role that matches the template already exists in the account,
  `AcquireRole` returns that role. This requires the
  `iam:GetRole` permission.
- If no matching role exists, `AcquireRole` creates one from the template.
  This requires the `iam:CreateRole` permission, plus the permissions for what
  the template defines: `iam:PutRolePolicy` if the template adds inline
  policies, and `iam:AttachRolePolicy` if the template attaches managed
  policies.

A user with full IAM access has all the permissions that role manager requires. To see
the exact actions a specific template requires, retrieve the template with
`GetRoleTemplateVersion` and review its policies.

When role manager creates a role, AWS CloudTrail records the creation as a single
`AcquireRole` event. The event shows who called the operation, the role template
and parameter values that were used, and the role that was created.

The following example shows that role manager called the `AcquireRole` operation on behalf
of a user who assumed the role `Admin`, using the `PowerUserRoleTemplate` role template to create
the role `PowerUserRole`.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA123EXAMPLE:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "arn": "arn:aws:sts::123456789012:assumed-role/Admin/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "accountId": "123456789012",
        "accessKeyId": "ASIAWZYMLEXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA123EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2026-08-11T18:18:50Z",
                "mfaAuthenticated": "false"
            }
        },
        "onBehalfOf": {
            "userId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "identityStoreArn": "arn:aws:identitystore::111122223333:identitystore/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
    },
    "eventTime": "2026-08-11T18:23:00Z",
    "eventSource": "iam.amazonaws.com",
    "eventName": "AcquireRole",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "requestParameters": {
        "templateArn": "arn:aws:iam::aws:role-template/iam.amazonaws.com/PowerUserRoleTemplate:1",
        "templateMinorVersion": 0,
        "replacementValues": {
            "AWSServiceName": {
                "values": [
                    "iam.amazonaws.com"
                ]
            }
        }
    },
    "responseElements": {
        "role": {
            "path": "/",
            "roleName": "PowerUserRole",
            "roleId": "AROA987EXAMPLE",
            "arn": "arn:aws:iam::123456789012:role/PowerUserRole",
            "createDate": "2026-08-11T18:23:00Z",
            "assumeRolePolicyDocument": "%7B%22Version%22:%222012-10-17%22,%22Statement%22:%5B%7B%22Effect%22:%22Allow%22,%22Principal%22:%7B%22Service%22:%22iam.amazonaws.com%22%7D,%22Action%22:%22sts:AssumeRole%22%7D%5D%7D"
        }
    },
    "requestID": "fde3dac0-73ac-491c-876b-EXAMPLE89c57",
    "eventID": "c93332cf-1429-4aee-bcaa-EXAMPLE3790d",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "iam.amazonaws.com"
    },
    "sessionCredentialFromConsole": "true"
}
```

## Control role manager in an organization

You can control role manager across an organization with an AWS Organizations service
control policy (SCP). The following examples show how to block enabling role manager, block
role creation, or block template-based role creation only.

These examples use the [deny list strategy](../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md#strategy_using_scps "../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md#strategy_using_scps"), which means you also need `FullAWSAccess` or
another policy that allows actions attached to your organization entities. You still need to
grant permissions to your principals with identity-based policies.

Denying access to `iam:PutAccountProperties` permission will prevent any
member from enabling role manager through the console or the API. This is recommended when
new accounts are created directly through Organizations.

```
{
    "Sid": "DenyRoleManagerEnablement",
    "Effect": "Deny",
    "Action": "iam:PutAccountProperties",
    "Resource": "*",
    "Condition": {
        "ForAnyValue:StringEquals": {
            "iam:AccountPropertyNamespaces": "RoleManager"
        }
    }
}
```

### Block access to use role manager

If it is desired to block access to use role manager, the
`iam:RoleTemplateARN` context key can be used to determine what permissions act
on a templated role creation process. The following policy denies all the IAM actions that
have a non-null value for the `iam:RoleTemplateARN` context key. Note that this
does _not_ prevent all role creation activities— just the role
manager-based role creation or direct templated role creation through the SDK.

```
{
    "Sid": "DenyTemplatedRoleCreation",
    "Effect": "Deny",
    "Action": "iam:*",
    "Resource": "*",
    "Condition": {
        "Null": {
            "iam:RoleTemplateARN": false
        }
    }
}
```

### Block role creation except through role manager

If the desire is to only allow access to role manager based role creation the
following policy can be used to block non-role manager role creations. Note that it
will still allow template based role creations directly through the SDK.

```
{
    "Sid": "DenyNonTemplatedRoleCreation",
    "Effect": "Deny",
    "Action": [
        "iam:GetRole",
        "iam:GetRoleTemplateVersion",
        "iam:CreateRole",
        "iam:AttachRolePolicy",
        "iam:PutRolePolicy",
        "iam:PutRolePermissionsBoundary",
        "iam:TagRole"
    ],
    "Resource": "*",
    "Condition": {
        "Null": {
            "iam:RoleTemplateARN": true
        }
    }
}
```

## Related information

- [Create roles automatically with role manager](id_roles_create_role-manager.md "id_roles_create_role-manager.md")
- [Apply least-privilege permissions to a role created automatically](id_roles_create_role-manager_least-privilege.md "id_roles_create_role-manager_least-privilege.md")
- [Overview of role templates](id_roles_create_role-template.md "id_roles_create_role-template.md")
