

# Controlling access in AWS Partner Central
<a name="controlling-access-in-aws-partner-central"></a>

User access to AWS Partner Central is managed through AWS Identity and Access Management (IAM). IAM permissions control who can be authenticated (signed in) and authorized (have permissions) to use AWS Partner Central and AWS Marketplace features. IAM is an AWS service that you can use at no additional charge.

IAM permissions are assigned to individual users by IAM Administrators. These administrators act as security managers for your AWS environment—they provision and de-provision user accounts, assign permissions, and set up security policies. IAM Administrators typically sit within IT or Governance and Security teams.

**Important**  
To access AWS Partner Central, users must work with their IAM Administrator to be provided with the correct level of access. If permissions aren't set up correctly, users might not be able to sign in at all, or they might be able to log in, but may not be able to access the tools and information they need to do their job.

The following resources provide more information about getting started and using IAM:
+ [Create an administrative user](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+ [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-using.html)
+ [Attaching a policy to an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html)
+ [IAM Identities (users, groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)
+ [Controlling access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_permissions.html)
+ [Actions, resources, and condition keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html)

**Topics**
+ [AWS IAM for AWS Partner Central](#aws-iam-for-aws-partner-central)
+ [Adding users to AWS Partner Central](#adding-users-to-aws-partner-central)
+ [Permissions for AWS Partner Central](#permissions-for-aws-partner-central)
+ [Condition keys for AWS Partner Central](#condition-keys-for-aws-partner-central)

## AWS IAM for AWS Partner Central
<a name="aws-iam-for-aws-partner-central"></a>

AWS IAM is built on the concept of role-based access. Within this framework, users are assigned to specific roles or groups associated with a set of IAM policies that control what specific features within AWS Partner Central that a user can access. To simplify this process, AWS has published several Managed policies to simplify user management for common user personas within AWS Partner Central.

The IAM Administrator is responsible for the creation of IAM roles, groups and policies and assignment of users to provision permissions in AWS IAM, but must collaborate with the Partner Central users and their leadership to determine what level of access each user should be granted.

Review the Managed policy mappings for guidance on managed policy assignments based on common Partner Central user personas.

Working with AWS IAM requires specific technical knowledge and appropriate AWS account permissions. These individuals ('IAM Administrators') are required to support set up and management of these permissions. The IAM Administrator is typically someone in your IT Security, Information Security, or Governance/Compliance department.

Partner Central uses AWS IAM to manage all user access through your organization's AWS account. Instead of Partner Central managing users directly, your IT team controls access through AWS IAM. Users are assigned specific policies that determine which Partner Central resources (like Opportunities, Solutions, or Fund Requests) a user can access and whether they can only view information (read access) or also make changes (write access).

**Important**  
If users are not properly provisioned access in IAM, they will not be able to access features in AWS Partner Central. Users should only have access to the features they need to do their job - this is called "least privilege" access.

### IAM Role-Based Access Implementation
<a name="iam-role-based-access-implementation"></a>

Implementation varies by organization but generally follows this process:

Step 1: The IAM Administrator creates IAM roles  
IAM Administrators create roles that define functional personas within AWS Partner Central. Each role describes the specific features and capabilities users in that job function need to access. For example, a role could be created for:  
+ Marketing Managers, responsible for creating co-marketing assets and managing campaigns
+ Operations Administrators, responsible for creating and managing fund requests.
Organizations can create as many roles as needed based on the different personas accessing Partner Central. For a summary of common Partner Central user personas, see here. In addition to these managed policies, organizations can create and customize managed policies to tailor access as needed. For more information, see [AWS managed policies for AWS Partner Central users](https://docs.aws.amazon.com/partner-central/latest/getting-started/managed-policies.html).  
Not sure who your IAM Administrator is? They typically sit in IT Security, Information Security, or Governance/Compliance teams, but this varies by organization. They should have administrator access to the AWS account used to access AWS Partner Central.

Step 2: Assign IAM Policies to Each Role  
Once roles are created, the IAM Administrator assigns specific IAM policies that determine allowed access. For example, the Marketing Manager role might receive read/write access to the Case Studies feature, permission to create and manage Solutions, and the ability to create tickets to APN Support. To simplify this process, AWS publishes Managed Policies—pre-built sets of IAM policies that map to common user roles. Instead of provisioning individual feature-level inline policies, IAM Administrators can assign Managed Policies that align with each role's responsibilities. To see how common Partner Central personas map to published Managed Policies, see here.  
IAM Administrators can use managed policies or build custom policies for specific user permissions. AWS recommends using managed policies when possible to simplify permission management, as they enable automatic AWS updates for common use cases and version control.

Step 3: [Optional] Set up Single Sign-On  
Single Sign-On (SSO) benefits users, organizations, and IT teams by streamlining authentication and enhancing security. For users, SSO simplifies access by allowing them to log in once, with a single set of credentials, to access multiple enterprise applications, reducing password fatigue and enabling faster productivity through seamless navigation across integrated systems. For organizations, SSO enhances security through centralized authentication that enables stronger access controls and improves compliance by making it easier to enforce security policies. For IT teams specifically, SSO simplifies administration by managing user identities and permissions from a single location, accelerates onboarding and offboarding by granting or revoking access to multiple systems simultaneously, and offers integration flexibility by connecting diverse applications through standard protocols. For more information on how to set up SSO for your organization, see here.

## Adding users to AWS Partner Central
<a name="adding-users-to-aws-partner-central"></a>

Adding users to Partner Central requires coordination between the Alliance Lead (who determines access needs) and the IAM Administrator (who implements the technical setup).

**Note**  
IAM permissions can be modified whenever needed, and there's no cap on how many users can receive access rights.

To add a new user:

### For Alliance Leads: Determine User Access Needs
<a name="for-alliance-leads-determine-user-access-needs"></a>

1. **Identify the user's role and required access level:** Review the managed policy mappings to determine which role (persona) best describes their job function. Refer to this table for common Partner Central user personas and which Managed policies best fit that user's required level of access.

1. **Request the IAM Administrator to add the user.** Provide the IAM Administrator with:
   + User's name and company email address
   + Required managed policies (e.g., AWSPartnerCentralOpportunityManagement)
   + Any specific access requirements if custom policies are needed

### For IAM Administrators: Create and Configure User Access
<a name="for-iam-administrators-create-and-configure-user-access"></a>

Depending on your AWS account setup, choose one of the following options to grant users access:

Option 1: Using IAM Identity Center  
**Best for:** Organizations managing multiple users across AWS accounts who want centralized access management with single sign-on (SSO) capabilities.  
**Key benefits:** Centralized user management, automatic permission synchronization across accounts, simplified onboarding/offboarding, and enhanced security with SSO.

Option 2: Using IAM Console (For individual users)  
**Best for:** Small teams or organizations managing a limited number of individual user accounts who need direct AWS Console access.  
**Key benefits:** Quick setup for individual users, direct control over specific user permissions, and straightforward for small-scale deployments.

Option 3: Integrate with a third-party Identity Provider  
**Best for:** Organizations already using enterprise identity providers (like Okta, Azure AD, or Ping Identity) who want to maintain existing authentication workflows.  
**Key benefits:** Seamless integration with existing enterprise identity systems, consistent authentication experience across all business applications, centralized user lifecycle management, and enhanced compliance with corporate security policies.

## Permissions for AWS Partner Central
<a name="permissions-for-aws-partner-central"></a>

Use permissions to limit access to the AWS Partner Central data that you need. This section explains how permissions work, and links to the four parts of the *Service Authorization Reference* for AWS Partner Central: actions, permission-only actions, resource types, and condition keys. For example, you can allow access to opportunities but not to benefit applications or business plans. To do this, allow or deny AWS Partner Central actions in your identity-based policies. These actions use the `partnercentral` prefix.

The *Service Authorization Reference* lists every action, resource type, and condition key that AWS Partner Central defines. For each action, it shows the access level, the supported resource types, and the condition keys. The reference has the following sections for AWS Partner Central:
+ [Actions defined by AWS Partner Central](https://docs.aws.amazon.com/service-authorization/latest/reference/list_partner-central.html#list_partner-central-actions-as-permissions): the permission for each AWS Partner Central API operation
+ [Permission-only actions for AWS Partner Central](https://docs.aws.amazon.com/service-authorization/latest/reference/list_partner-central.html#list_partner-central-permission-only-actions): permissions that don't correspond to an API operation
+ [Resource types defined by AWS Partner Central](https://docs.aws.amazon.com/service-authorization/latest/reference/list_partner-central.html#list_partner-central-resources-for-iam-policies): the Amazon Resource Name (ARN) format of each resource type
+ [Condition keys for AWS Partner Central](https://docs.aws.amazon.com/service-authorization/latest/reference/list_partner-central.html#list_partner-central-policy-keys): the type of each condition key

## Condition keys for AWS Partner Central
<a name="condition-keys-for-aws-partner-central"></a>

Condition keys narrow when a policy statement applies. For example, you can allow an action only in the `Sandbox` catalog. The *Service Authorization Reference* lists each AWS Partner Central condition key and its type. For more information about the values that each key accepts and the actions that support it, see [Permissions](https://docs.aws.amazon.com/partner-central/latest/developer-guide/permissions.html) in the *AWS Partner Central Developer Guide*.