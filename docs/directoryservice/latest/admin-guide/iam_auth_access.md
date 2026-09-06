

# Identity and access management for Directory Service
<a name="iam_auth_access"></a>

Access to Directory Service requires credentials that AWS can use to authenticate your requests. Those credentials must have permissions to access AWS resources, such as an Directory Service directory. The following sections provide details on how you can use [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) and Directory Service to help secure your resources by controlling who can access them:

 
+ [Authentication](#authentication)
+ [Access control](#access_control)

## Authentication
<a name="authentication"></a>

Learn how to access AWS using [IAM identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html).

## Access control
<a name="access_control"></a>

You can have valid credentials to authenticate your requests, but unless you have permissions you cannot create or access Directory Service resources. For example, you must have permissions to create an Directory Service directory or to create a directory snapshot.

The following sections describe how to manage permissions for Directory Service. We recommend that you read the overview first.

 
+ [Overview of managing access permissions to your Directory Service resources](IAM_Auth_Access_Overview.md)
+  [Using identity-based policies (IAM policies) for Directory Service](IAM_Auth_Access_IdentityBased.md) 
+  [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md) 