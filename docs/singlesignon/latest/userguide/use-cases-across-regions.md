

# Availability of IAM Identity Center use cases in the primary and additional Regions
<a name="use-cases-across-regions"></a>


| Feature | Regional availability | 
| --- | --- | 
|  Workforce directory with a user portal  |  | 
| User access to the AWS access portal including portal sign-in and global sessions (one sign-in for all Regions) | All enabled Regions | 
| Display of all assigned accounts | All enabled Regions | 
| Display of all assigned applications (regardless of where the applications were created) | All enabled Regions | 
| Read access to users, groups, and memberships in the AWS Console or via Identity Store APIs | All enabled Regions | 
| Revoke user sessions | All enabled Regions | 
| Automatic synchronization of users and groups from an external identity source (such as external IdP through SCIM API or Identity Store API). This row applies only to external identity providers. | Primary Region only | 
| Configure automatic identity provisioning with SCIM | Primary Region only | 
| Configure SAML SSO with an external IdP | Primary Region only - read access through the console in all enabled Regions | 
| Create/update/delete operations on users, groups and group memberships via the console or Identity Store APIs. | Primary Region only. When using the Identity Center directory, these operations are available through the IAM Identity Center console and Identity Store API in the primary Region. When using an external IdP with SCIM provisioning, write operations are blocked in the console (except disable/enable user access and delete user). Additional Regions: read-only access. | 
| User data plane operations (password reset, MFA device management) via the AWS access portal (Identity Center directory only) | All enabled Regions (applies only when using the Identity Center directory as the identity source) | 
|  Multi-account access  |  | 
| Access assigned accounts via the AWS access portal, AWS CLI, and shortcut links | All enabled Regions | 
| Manage multi-account permission sets and their assignments in the console and APIs (including temporary elevated access) | Primary Region only | 
|  Access to applications and AWS services  |  | 
| Deploy AWS managed applications through the application console and APIs | All enabled Regions – subject to applications' regional availability and support for deployment in additional Regions | 
| Create customer managed applications through the Identity Center console and APIs | All enabled Regions | 
| Manage application metadata and assignments in the console and APIs | Application's connected IAM Identity Center Region | 
| Launch applications from the AWS access portal or directly via an application link or bookmark | All enabled Regions | 
| SSO to Amazon EC2 instances | All enabled Regions | 
|  Trusted identity propagation  |  | 
| Create a trusted token issuer | Primary Region only | 
| Trusted identity propagation with AWS managed applications | All enabled Regions - Applications that propagate identity context to each other must be in the same Region | 
|  Other administrative features  |  | 
| All other administrative features such as Region management, KMS key management, instance management, and session management (except session revocation) | Primary Region only - read access available in all enabled Regions for some data (permission set assignments excluded) | 