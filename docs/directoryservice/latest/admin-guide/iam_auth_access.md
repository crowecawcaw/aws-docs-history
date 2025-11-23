# Identity and access management for Directory Service

Access to Directory Service requires credentials that AWS can use to authenticate your requests.
Those credentials must have permissions to access AWS resources, such as an Directory Service
directory. The following sections provide details on how you can use [AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") and Directory Service to help secure
your resources by controlling who can access them:

- [Authentication](#authentication "#authentication")
- [Access control](#access_control "#access_control")

## Authentication

Learn how to access AWS using [IAM identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md").

## Access control

You can have valid credentials to authenticate your requests, but unless you have
permissions you cannot create or access Directory Service resources. For example, you must have
permissions to create an Directory Service directory or to create a directory snapshot.

The following sections describe how to manage permissions for Directory Service. We recommend that
you read the overview first.

- [Overview of managing access permissions to
  your Directory Service resources](IAM_Auth_Access_Overview.md "IAM_Auth_Access_Overview.md")
- [Using identity-based policies (IAM
  policies) for Directory Service](IAM_Auth_Access_IdentityBased.md "IAM_Auth_Access_IdentityBased.md")
- [Directory Service API permissions: Actions,
  resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md "UsingWithDS_IAM_ResourcePermissions.md")
