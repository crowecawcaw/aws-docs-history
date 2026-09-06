

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

You can use the following permissions in IAM policies for AWS Partner Central. You can combine permissions into a single IAM policy to grant the permissions you want.

### ListPartnerPaths
<a name="listpartnerpaths"></a>

`ListPartnerPaths` provides access to list partner paths in AWS Partner Central.
+ **Action groups:** `ListOnly`, `ReadOnly`, `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### EnrollInPartnerPath
<a name="enrollinpartnerpath"></a>

`EnrollInPartnerPath` provides access to enroll in partner paths in AWS Partner Central.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetPartnerDashboard
<a name="getpartnerdashboard"></a>

`GetPartnerDashboard` provides access to retrieve partner dashboard information in AWS Partner Central.
+ **Action groups:** `ReadOnly`, `ReadWrite`
+ **Required resources:** `arn:${Partition}:partnercentral::${Account}:catalog/${Catalog}/ReportingData/${TableId}/Dashboard/${DashboardId}`
+ **Condition keys:** `partnercentral:Catalog`

### CreateBusinessPlan
<a name="createbusinessplan"></a>

`CreateBusinessPlan` provides access to create business plans in AWS Partner Central.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### PutBusinessPlan
<a name="putbusinessplan"></a>

`PutBusinessPlan` provides access to update business plans in AWS Partner Central.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### ListBusinessPlans
<a name="listbusinessplans"></a>

`ListBusinessPlans` provides access to list business plans in AWS Partner Central.
+ **Action groups:** `ListOnly`, `ReadOnly`, `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetBusinessPlan
<a name="getbusinessplan"></a>

`GetBusinessPlan` provides access to retrieve business plan details in AWS Partner Central.
+ **Action groups:** `ReadOnly`, `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### CreateCollaborationChannelRequest
<a name="createcollaborationchannelrequest"></a>

`CreateCollaborationChannelRequest` provides access to create collaboration channel requests in AWS Partner Central.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### ListCollaborationChannels
<a name="listcollaborationchannels"></a>

`ListCollaborationChannels` provides access to list collaboration channels in AWS Partner Central.
+ **Action groups:** `ListOnly`, `ReadOnly`, `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetCollaborationChannel
<a name="getcollaborationchannel"></a>

`GetCollaborationChannel` provides access to retrieve collaboration channel details in AWS Partner Central.
+ **Action groups:** `ReadOnly`, `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### CreateCollaborationChannelMembers
<a name="createcollaborationchannelmembers"></a>

`CreateCollaborationChannelMembers` provides access to create collaboration channel members in AWS Partner Central.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### SearchPartnerProfiles
<a name="searchpartnerprofiles"></a>

`SearchPartnerProfiles` provides access to search public partner profiles in AWS Partner Central.
+ **Action groups:** `ListOnly`, `ReadOnly`, `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetPartnerProfile
<a name="getpartnerprofile"></a>

`GetPartnerProfile` provides access to retrieve public partner profile details in AWS Partner Central.
+ **Action groups:** `ReadOnly`, `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetProgramManagementAccount
<a name="getprogrammanagementaccount"></a>

`GetProgramManagementAccount` provides access to retrieve program management account details in AWS Partner Central.
+ **Action groups:** `ReadOnly`, `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.
+ **Condition keys:** `partnercentral:Catalog`

### UseSession
<a name="usesession"></a>

`UseSession` provides access to use Partner Central agents sessions in AWS Partner Central.
+ **Action groups:** `ReadWrite`
+ **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.
+ **Condition keys:** `partnercentral:Catalog`

## Condition keys for AWS Partner Central
<a name="condition-keys-for-aws-partner-central"></a>

AWS Partner Central defines the following condition keys that you can use in the `Condition` element of an IAM policy.

### partnercentral:Catalog
<a name="partnercentral-catalog"></a>

Filters access by a specific Catalog.
+ **Type:** `String`

  **Valid values:** `[AWS | Sandbox]`

### partnercentral:RelatedEntityType
<a name="partnercentral-relatedentitytype"></a>

Filters access by entity types for Opportunity association.
+ **Type:** `String`

  **Valid values:** `[Solutions | AwsProducts | AwsMarketplaceOffers]`

### partnercentral:ChannelHandshakeType
<a name="partnercentral-channelhandshaketype"></a>

Filters access by channel handshake types.
+ **Type:** `String`

  **Valid values:** `[START_SERVICE_PERIOD | REVOKE_SERVICE_PERIOD | PROGRAM_MANAGEMENT_ACCOUNT]`

### partnercentral:VerificationType
<a name="partnercentral-verificationtype"></a>

Filters access by the type of verification being performed.
+ **Type:** `String`

  **Valid values:** `[BUSINESS_VERIFICATION | REGISTRANT_VERIFICATION]`

### partnercentral:FulfillmentTypes
<a name="partnercentral-fulfillmenttypes"></a>

Filters access by benefit fulfillment types.
+ **Type:** `ArrayOfString`

  **Valid values:** `[CREDITS | CASH | ACCESS]`

### partnercentral:Programs
<a name="partnercentral-programs"></a>

Filters access by program.
+ **Type:** `ArrayOfString`