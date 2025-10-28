# Troubleshooting Lake Formation

If you encounter issues when working with AWS Lake Formation, consult the topics in this section.

###### Topics

- [General troubleshooting](#trouble-general "#trouble-general")
- [Troubleshooting cross-account access](#trouble-cross-account "#trouble-cross-account")
- [Troubleshooting blueprints and workflows](#trouble-workflows "#trouble-workflows")
- [Known issues for AWS Lake Formation](limitations.md "limitations.md")
- [Updated error message](error-message-update.md "error-message-update.md")

## General troubleshooting

Use the information here to help you diagnose and fix various Lake Formation issues.

### Error: Insufficient Lake Formation permissions on <Amazon S3

location>

An attempt was made to create or alter a Data Catalog resource without data location permissions
on the Amazon S3 location pointed to by the resource.

If a Data Catalog database or table points to an Amazon S3 location, when you grant the Lake Formation
permissions `CREATE_TABLE` or `ALTER`, you must also grant the
`DATA_LOCATION_ACCESS` permission on the location. If you are granting these
permissions to external accounts or to organizations, you must include the grant option.

After these permissions are granted to an external account, the data lake administrator in
that account must then grant the permissions to principals (users or roles) in the account. When
granting the `DATA_LOCATION_ACCESS` permission that was received from another
account, you must specify the catalog ID (AWS account ID) of the owner account. The owner
account is the account that registered the location.

For more information, see [Underlying data access control](access-control-underlying-data.md "access-control-underlying-data.md") and [Granting data location permissions](granting-location-permissions.md "granting-location-permissions.md").

### Error: "Insufficient encryption key permissions for

Glue API"

An attempt was made to grant Lake Formation permissions without AWS Identity and Access Management (IAM) permissions on the
AWS KMS encryption key for an encrypted Data Catalog.

### My Amazon Athena or Amazon Redshift query that uses

manifests is failing

Lake Formation does not support queries that use manifests.

### Error: "Insufficient Lake Formation permission(s): Required create

tag on catalog"

The user/role must be a data lake administrator.

### Error when deleting invalid data lake administrators

You should delete all invalid data lake administrators (deleted IAM roles that are
defined as data lake administrators) simultaneously. If you try to delete invalid data lake
administrators separately, Lake Formation throws invalid principal error.

## Troubleshooting cross-account access

Use the information here to help you diagnose and fix cross-account access issues.

###### Topics

- [I granted a cross-account Lake Formation permission
  but the recipient can't see the resource](#troubleshooting-problem1 "#troubleshooting-problem1")
- [Principals in the recipient account can see the
  Data Catalog resource but can't access the underlying data](#troubleshooting-problem11 "#troubleshooting-problem11")
- [Error: "Association failed because the
  caller was not authorized" when accepting a AWS RAM resource share invitation](#troubleshooting-cross-acct-accepting "#troubleshooting-cross-acct-accepting")
- [Error: "Not authorized to grant permissions for the
  resource"](#troubleshooting-problem2 "#troubleshooting-problem2")
- [Error: "Access denied to retrieve AWS Organization
  information"](#troubleshooting-problem3 "#troubleshooting-problem3")
- [Error: "Organization <organization-ID> not
  found"](#troubleshooting-problem4 "#troubleshooting-problem4")
- [Error: "Insufficient Lake Formation permissions:
  Illegal combination"](#troubleshooting-problem5 "#troubleshooting-problem5")
- [ConcurrentModificationException on grant/revoke
  requests to external accounts](#troubleshooting-problem6 "#troubleshooting-problem6")
- [Error when using Amazon EMR to access data shared via cross-account](#toubleshooting-problem7 "#toubleshooting-problem7")

### I granted a cross-account Lake Formation permission

but the recipient can't see the resource

- Is the user in the recipient account a data lake administrator? Only data lake
  administrators can see the resource at the time of sharing.
- Are you sharing with an account external to your organization by using the named resource
  method? If so, the data lake administrator of the recipient account must accept a resource
  share invitation in AWS Resource Access Manager (AWS RAM).

For more information, see [Accepting a resource share invitation from AWS RAM](accepting-ram-invite.md "accepting-ram-invite.md").

- Are you using account-level (Data Catalog) resource policies in AWS Glue? If yes, then if you use
  the named resources method, you must include a special statement in the policy that authorizes
  AWS RAM to share policies on your behalf.

For more information, see [Managing cross-account permissions using both
AWS Glue and Lake Formation](hybrid-cross-account.md "hybrid-cross-account.md").

- Do you have the AWS Identity and Access Management (IAM) permissions required to grant cross-account
  access?

For more information, see [Prerequisites](cross-account-prereqs.md "cross-account-prereqs.md").

- The resource that you've granted permissions on must not have any Lake Formation permissions
  granted to the `IAMAllowedPrincipals` group.
- Is there a `deny` statement on the resource in the account-level policy?

### Principals in the recipient account can see the

Data Catalog resource but can't access the underlying data

Principals in the recipient account must have the required AWS Identity and Access Management (IAM) permissions.
For details, see [Accessing the underlying data of a shared
table](cross-account-read-data.md "cross-account-read-data.md").

### Error: "Association failed because the

caller was not authorized" when accepting a AWS RAM resource share invitation

After granting access to a resource to a different account, when the receiving account
attempts to accept the resource share invitation, the action fails.

```
$ aws ram get-resource-share-associations --association-type PRINCIPAL --resource-share-arns arn:aws:ram:`aws-region`:444444444444:resource-share/e1d1f4ba-xxxx-xxxx-xxxx-xxxxxxxx5d8d
{
    "resourceShareAssociations": [
        {
            "resourceShareArn": "arn:aws:ram:`aws-region`:444444444444:resource-share/e1d1f4ba-xxxx-xxxx-xxxx-xxxxxxxx5d8d
",
            "resourceShareName": "LakeFormation-MMCC0XQBH3Y",
            "associatedEntity": "5815803XXXXX",
            "associationType": "PRINCIPAL",
            "status": "FAILED",
            "statusMessage": "Association failed because the caller was not authorized.",
            "creationTime": "2021-07-12T02:20:10.267000+00:00",
            "lastUpdatedTime": "2021-07-12T02:20:51.830000+00:00",
            "external": true
        }
    ]
}
```

The error occurs because the `glue:PutResourcePolicy` is invoked by
AWS Glue when the receiving account accepts the resource share invitation. To
resolve the issue, allow the `glue:PutResourcePolicy` action by the assumed role used
by the producer/grantor account.

### Error: "Not authorized to grant permissions for the

resource"

An attempt was made to grant cross-account permissions on a database or table that is owned
by another account. When a database or table is shared with your account, as a data lake
administrator, you can grant permissions on it only to users in your account.

### Error: "Access denied to retrieve AWS Organization

information"

Your account is an AWS Organizations management account and you do not have the required
permissions to retrieve organization information, such as organizational units in the
account.

For more information, see [Required permissions for cross-account grants](cross-account-prereqs.md#cross-account-permissions-needed "cross-account-prereqs.md#cross-account-permissions-needed").

### Error: "Organization <organization-ID> not

found"

An attempt was made to share a resource with an organization, but sharing with
organizations is not enabled. Enable resource sharing with organizations.

For more information, see [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.

### Error: "Insufficient Lake Formation permissions:

Illegal combination"

A user shared a Data Catalog resource while Lake Formation permissions were granted to the
`IAMAllowedPrincipals` group for the resource. The user must revoke all Lake Formation
permissions from `IAMAllowedPrincipals` before sharing the resource.

### ConcurrentModificationException on grant/revoke

requests to external accounts

When users make multiple concurrent grant and/or revoke permission requests for a principal
on LF-Tag policies, then Lake Formation throws ConcurrentModificationException. Users need to catch
the exception and retry the failed the grant/revoke request. Using batch versions of the
`GrantPermissions`/`RevokePermissions` API operations - [BatchGrantPermissions](../APIReference/API_BatchGrantPermissions.md "../APIReference/API_BatchGrantPermissions.md")and [BatchRevokePermissions](../APIReference/API_BatchRevokePermissions.md "../APIReference/API_BatchRevokePermissions.md") alleviates this problem to an extent by reducing the
number of concurrent grant/revoke requests.

### Error when using Amazon EMR to access data shared via cross-account

When you use Amazon EMR to access data shared with you from another account, some Spark
libraries will attempt to call `Glue:GetUserDefinedFunctions` API operation. Since
versions 1 and 2 of the AWS RAM managed permissions does not support this action, you receive the
following error message:

`"ERROR: User: arn:aws:sts::012345678901:assumed-role/my-spark-role/i-06ab8c2b59299508a is not authorized to perform: glue:GetUserDefinedFunctions on resource: arn:exampleCatalogResource because no resource-based policy allows the glue:GetUserDefinedFunctions action"`

To resolve this error, the data lake administrator who created the resource share must
update the AWS RAM managed permissions attached to the resource share. Version 3 of the AWS RAM
managed permissions allows principals to perform the `glue:GetUserDefinedFunctions`
action.

If you create a new resource share, Lake Formation applies the latest version of the AWS RAM managed
permission by default, and no action is required by you. To enable cross-account data access for
existing resource shares, you need to update the AWS RAM managed permissions to version 3.

You can view the AWS RAM permissions assigned to resources shared with you in AWS RAM. The
following permissions are included in version 3:

```
Databases
  AWSRAMPermissionGlueDatabaseReadWriteForCatalog
  AWSRAMPermissionGlueDatabaseReadWrite

Tables
  AWSRAMPermissionGlueTableReadWriteForCatalog
  AWSRAMPermissionGlueTableReadWriteForDatabase

AllTables
  AWSRAMPermissionGlueAllTablesReadWriteForCatalog
  AWSRAMPermissionGlueAllTablesReadWriteForDatabase

```

###### To update AWS RAM managed permissions version of existing resource shares

You (data lake administrator) can either [update AWS RAM managed permissions to a newer version](../../../ram/latest/userguide/working-with-sharing-update-permissions.md "../../../ram/latest/userguide/working-with-sharing-update-permissions.md") by following instructions in the
_AWS RAM User Guide_ or you can revoke all existing
permissions for the resource type and regrant them. If you revoke permissions, AWS RAM deletes
the AWS RAM resource share associated with the resource type. When you regrant permissions, AWS RAM
creates new resource shares attaching the latest version of AWS RAM managed permissions.

## Troubleshooting blueprints and workflows

Use the information here to help you diagnose and fix blueprint and workflow issues.

###### Topics

- [My blueprint failed with "User: <user-ARN> is not authorized
  to perform: iam:PassRole on resource: <role-ARN>"](#problem-bp-1 "#problem-bp-1")
- [My workflow failed with "User: <user-ARN> is not authorized to
  perform: iam:PassRole on resource: <role-ARN>"](#problem-bp-2 "#problem-bp-2")
- [A crawler in my workflow failed with "Resource does not exist or
  requester is not authorized to access requested permissions"](#problem-bp-3 "#problem-bp-3")
- [A crawler in my workflow failed with "An error occurred
  (AccessDeniedException) when calling the CreateTable operation..."](#problem-bp-4 "#problem-bp-4")

### My blueprint failed with "User: <user-ARN> is not authorized

to perform: iam:PassRole on resource: <role-ARN>"

An attempt was made to create a blueprint by a user who does not have sufficient
permissions to pass the chosen role.

Update the user’s IAM policy to be able to pass the role, or ask the user to choose a
different role with the required passrole permissions.

For more information, see [Lake Formation personas and IAM permissions reference](permissions-reference.md "permissions-reference.md").

### My workflow failed with "User: <user-ARN> is not authorized to

perform: iam:PassRole on resource: <role-ARN>"

The role that you specified for the workflow did not have an inline policy allowing the
role to pass itself.

For more information, see [(Optional) Create an IAM role for workflows](initial-lf-config.md#iam-create-blueprint-role "initial-lf-config.md#iam-create-blueprint-role").

### A crawler in my workflow failed with "Resource does not exist or

requester is not authorized to access requested permissions"

One possible cause is that the passed role did not have sufficient permissions to create a
table in the target database. Grant the role the `CREATE_TABLE` permission on the
database.

### A crawler in my workflow failed with "An error occurred

(AccessDeniedException) when calling the CreateTable operation..."

One possible cause is that the workflow role did not have data location permissions on the
target storage location. Grant data location permissions to the role.

For more information, see [DATA_LOCATION_ACCESS](lf-permissions-reference.md#perm-location "lf-permissions-reference.md#perm-location").
