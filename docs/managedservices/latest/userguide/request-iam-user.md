# Restrict permissions with IAM role policy statements

AMS uses an IAM role to set user permissions through your federation service.

**Single-Account Landing Zone AMS**: See
[SALZ: Default IAM User Roles](defaults-user-role.md#json-default-role "defaults-user-role.md#json-default-role").

**Multi-Account Landing Zone AMS**: See
[MALZ: Default IAM User Roles](defaults-user-role.md#json-default-role-malz "defaults-user-role.md#json-default-role-malz").

An IAM role is an IAM entity that defines a set of permissions for making AWS service requests. IAM roles are not associated with a specific user or group.
Instead, trusted entities assume roles, such as IAM users, applications, or AWS services such as Amazon EC2. For more information, see
[IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md").

You can scope down the desired policy for a user assuming the AMS IAM user role by using the AWS Security Token Service (STS) API operation
[AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") by passing a more restrictive IAM policy under
the `Policy` request field.

Example policy statements that you can use to restrict CT access are provided next.

Using your configured Active Directory (AD) groups, and the AWS Security Token Service (STS) API operation
[AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md"), you can set permissions for certain users or groups, including restricting
access to certain change types (CTs). You can use the policy statements shown below to restrict CT access in various ways.

AMS change type statement in the default IAM instance profile that allows access to all AMS API calls (amscm and amsskms) and all change types:

```
{
    "Sid": "AWSManagedServicesFullAccess",
    "Effect": "Allow",
    "Action": [
        "amscm:*",
        "amsskms:*"
    ],
    "Resource": [
        "*"
    ]
}
```

1. Statement to allow access and all actions for only two specified
   CTs,
   where "Action" is the AMS API operations (either `amscm` or
   `amsskms`), and "Resource" represents existing change type IDs and
   version number:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "amscm:*",
 "Resource": [
 "arn:aws:amscm:*:*:changetype/`ct-ID1:1.0`",
 "arn:aws:amscm:*:*:changetype/`ct-ID2:1.0`"
 ]
 }
 ]
}`

```

2. Statement to allow access for CreateRfc,
   UpdateRfc,
   and SubmitRfc on only two specified
   CTs:
3. Statement to allow access for CreateRfc,
   UpdateRfc,
   and SubmitRfc on all available
   CTs:
4. Statement to deny access for all actions on restricted CT and allow on other
   CTs:
