# Configure access to AWS accounts

Organization instances of IAM Identity Center are integrated with AWS Organizations. This enables you to
centrally manage permissions across multiple AWS accounts without configuring access
individually to each account.

The following table compares the account access management options that you should
consider:

|                                         | IAM roles with account access manager                                                                                                                                                                                                                                                                                      | IAM Identity Center permission sets                                                                                                                                                                                                                                                                                                                       | IAM roles with direct IAM federation                                                                         |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Best for**                            | Workforce users and groups with custom IAM roles that vary across<br>accounts. Decentralized role creation and provisioning with centralized role<br>assignment to users.                                                                                                                                                  | Uniform baseline workforce access such as read-only and admin. Centralized<br>role creation and provisioning.                                                                                                                                                                                                                                             | Workloads                                                                                                    |
| **Scope**                               | Multiple accounts in an AWS organization                                                                                                                                                                                                                                                                                   | Multiple accounts in an AWS organization                                                                                                                                                                                                                                                                                                                  | Per account                                                                                                  |
| **IAM role provisioning**               | • Infrastructure as code (IaC)<br>• Manual provisioning through the AWS IAM console                                                                                                                                                                                                                                        | Automatically provisioned                                                                                                                                                                                                                                                                                                                                 | • Infrastructure as code (IaC)<br>• Manual provisioning through the AWS IAM console or external IdP consoles |
| **Role-to-identity mapping resides in** | Account access manager                                                                                                                                                                                                                                                                                                     | IAM Identity Center                                                                                                                                                                                                                                                                                                                                       | External IdP                                                                                                 |
| **End user experience**                 | Users access AWS accounts through the account access portal URL.<br>Requires IAM Identity Center authentication.                                                                                                                                                                                                           | Users access AWS accounts through the AWS access portal URL.                                                                                                                                                                                                                                                                                              | Users access AWS accounts through account-specific SAML applications<br>(icons) in their IdP portal.         |
| **AWS CLI user experience**             | User signs into AWS and accesses an AWS account with a specific role<br>in a web browser. User types *_aws login_<br>• on the command line<br>to retrieve the IAM role session credentials from the browser. For the<br>duration of the IAM role session, the user can work with the AWS CLI without<br>re-authenticating. | User configures a profile including the desired account and role pair by<br>typing **aws configure sso**. User types *_aws sso<br>login_<br>• to initiate a new session using a profile. If there is<br>no active IAM Identity Center session, the user authenticates in a browser. See the<br>*AWS IAM Identity Center User Guide<br>• for more details. | Custom integrations using AWS SDK credential providers                                                       |

## AWS account types

There are two types of AWS accounts in AWS Organizations:

- **Management account** - The AWS account that is used to
  create the organization.
- **Member accounts** - The rest of the AWS accounts that
  belong to an organization.

For more information about AWS account types, see [AWS Organizations Terminology and Concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the _AWS Organizations User Guide_.

You can also choose to register a member account as a _delegated
administrator_ for IAM Identity Center. Users in this account can perform most IAM Identity Center
administrative tasks. For more information, see [Delegated administration](delegated-admin.md "delegated-admin.md").

For each task and account type, the following table indicates whether the IAM Identity Center
administrative task can be performed by users in the account.

| IAM Identity Center administrative tasks                                      | Member account | Delegated administrator account | Management account |
| ----------------------------------------------------------------------------- | -------------- | ------------------------------- | ------------------ |
| Read users or groups (reading the group itself and the group's<br>membership) | Yes            | Yes                             | Yes                |
| Add, edit, or delete users or groups                                          | No             | Yes\*                           | Yes                |
| Enable or disable user access                                                 | No             | Yes                             | Yes                |
| Enable, disable, or manage incoming attributes                                | No             | Yes                             | Yes                |
| Change or manage identity sources                                             | No             | Yes                             | Yes                |
| Create, edit, or delete customer managed applications                         | No             | Yes                             | Yes                |
| Create, edit, or delete AWS managed applications                              | Yes            | Yes                             | Yes                |
| Configure MFA                                                                 | No             | Yes                             | Yes                |
| Manage permission sets not provisioned in the management<br>account           | No             | Yes                             | Yes                |
| Manage permission sets provisioned in the management account                  | No             | No                              | Yes                |
| Enable IAM Identity Center                                                    | No             | No                              | Yes                |
| Delete IAM Identity Center configuration                                      | No             | No                              | Yes                |
| Enable or disable user access in the management account                       | No             | No                              | Yes                |
| Register or deregister a member account as a delegated<br>administrator       | No             | No                              | Yes                |

\*Refer to the best practices for delegated administration regarding user and group
assignments to the management account.

## Assigning AWS account access

You can use _permission sets_ to simplify how you assign users and
groups in your organization access to AWS accounts. Permission sets are stored in
IAM Identity Center and define the level of access that users and groups have to an AWS account. You
can create a single permission set and assign it to multiple AWS accounts within your
organization. You can also assign multiple permission sets to the same user.

You can also use [account access manager](../../../IAM/latest/UserGuide/account-access-manager.md "../../../IAM/latest/UserGuide/account-access-manager.md")
— an IAM feature — to assign existing IAM roles to IAM Identity Center users and groups in your
organization's accounts. You can use account access manager on its own, or together with
permission sets. Account access manager gives you access to the full IAM role feature
set, including custom trust policies, role tags for ABAC, and configurable role
paths.

For more information about permission sets, see [Create, manage, and delete permission sets](permissionsets.md "permissionsets.md").

###### Note

You can also assign your users single sign-on access to applications. For
information, see [Configure access to applications](manage-your-applications.md "manage-your-applications.md").

## End-user experience

The _AWS access portal_ provides IAM Identity Center users with single sign-on access
to all their assigned AWS accounts and applications through a web portal. The
AWS access portal is different from the [AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/learn-whats-new.md "../../../awsconsolehelpdocs/latest/gsg/learn-whats-new.md"),
which is a collection of service consoles for managing AWS resources.

When you create a permission set, the name that you specify for the permission set
appears in the AWS access portal as an available role. Users sign in to the AWS access portal,
choose an AWS account, and then choose the role. After they choose the role, they can
access AWS services by using the AWS Management Console or retrieve temporary credentials to
access AWS services programmatically.

To open the AWS Management Console or retrieve temporary credentials to access AWS
programmatically, users complete the following steps:

1. Users open a browser window and use the sign-in URL that you provide to
   navigate to the AWS access portal.
2. Using their directory credentials, they sign in to the AWS access portal.
3. After authentication, on the AWS access portal page, they choose the
   **Accounts** tab to display the list of AWS accounts to
   which they have access.
4. Users then choose the AWS account that they want to use.
5. Below the name of the AWS account, any permission sets to which users are
   assigned appear as available roles. For example, if you assigned user
   `john_stiles` to the `PowerUser` permission set, the
   role displays in the AWS access portal as `PowerUser/john_stiles`. Users
   who are assigned multiple permission sets choose which role to use. Users can
   choose their role to access the AWS Management Console.
6. In addition to the role, AWS access portal users can retrieve temporary credentials
   for command line or programmatic access by choosing **Access
   keys**.

For step-by-step guidance that you can provide to your workforce users, see [Setting up and using the AWS access portal](using-the-portal.md "using-the-portal.md") and [Getting IAM Identity Center user credentials for the AWS CLI or AWS SDKs](howtogetcredentials.md "howtogetcredentials.md").

## Enforcing and limiting access

When you enable IAM Identity Center, IAM Identity Center creates a service-linked role. You can also use service
control policies (SCPs).

### Delegating and enforcing access

A _service-linked role_ is a type of IAM role that is linked
directly to an AWS service. After you enable IAM Identity Center, IAM Identity Center can create a
service-linked role in each AWS account in your organization. This role provides
predefined permissions that allow IAM Identity Center to delegate and enforce which users have
single sign-on access to specific AWS accounts in your organization in AWS Organizations.
You need to assign one or more users with access to an account, to use this role.
For more information, see [Understanding service-linked roles in IAM Identity Center](slrconcept.md "slrconcept.md")
and [Using service-linked roles for IAM Identity Center](using-service-linked-roles.md "using-service-linked-roles.md").

### Limiting access to the identity store from member accounts

For the identity store service used by IAM Identity Center, users who have access to a member
account can use API actions that require **Read** permissions.
Member accounts have access to **Read** actions on both the
**sso-directory** and **identitystore**
namespaces. For more information, see [Actions, resources, and condition keys for AWS IAM Identity Center directory](../../../service-authorization/latest/reference/list_awsiamidentitycenterdirectory.md "../../../service-authorization/latest/reference/list_awsiamidentitycenterdirectory.md") and
[Actions, resources, and condition keys for AWS Identity Store](../../../service-authorization/latest/reference/list_awsidentitystore.md "../../../service-authorization/latest/reference/list_awsidentitystore.md") in the
_Service Authorization Reference_.

To prevent users in member accounts from using API operations in the identity
store, you can [attach a service control policy (SCP)](../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md"). An SCP is a type of organization
policy that you can use to manage permissions in your organization. The following
example SCP prevents users in member accounts from accessing any API operation in
the identity store.

```
        {
            "Sid": "ExplicitlyBlockIdentityStoreAccess",
            "Effect": "Deny",
            "Action": ["identitystore:*", "sso-directory:*"],
            "Resource": "*"
        }
```

###### Note

To ensure your AWS managed applications function well with your IAM Identity Center you
should avoid applying this SCP to the AWS accounts where you deployed those
applications. Also, if you use delegated administration, you should avoid
applying this SCP to the delegated administration account. For more information,
see [Best practices](delegated-admin.md#delegated-admin-best-practices "delegated-admin.md#delegated-admin-best-practices").

For more information, see [Service
control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the
_AWS Organizations User Guide_.
