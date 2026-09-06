

# Managing users in Amazon SageMaker Unified Studio
<a name="user-management"></a>

Users can access the Amazon SageMaker Unified Studio data portal by using either their AWS credentials or single sign-on (SSO) credentials. For IAM-based domains, see [Managing users for IAM-based domains](manage-users-iam-based-domains.md) to manage users in the domain management portal. For Identity Center-based domains, see [Managing users for Identity Center-based domains](manage-users-idc-based-domains.md) to manage users in the Amazon SageMaker Unified Studio console.

Amazon SageMaker Unified Studio supports IAM roles, IAM users, single sign-on users, and single sign-on groups. When these users are added to a domain, the service creates a unique profile for the user. These profiles are most relevant for programmatic interactions with Amazon SageMaker Unified Studio, where API requests accept a user or group profile identifier and responses return user or group profile information. The following types of profiles exist in Amazon SageMaker Unified Studio:

## User profiles
<a name="user-profiles"></a>

Amazon SageMaker Unified Studio supports both IAM identities and single sign-on (SSO) identities to interact with the administration portal and the builder portal. Domain administrators use IAM identities to perform initial administrative domain-related work in the Amazon SageMaker Unified Studio administration portal, including creating projects, configuring VPCs, configuring metadata form types and glossaries, and managing users. Data workers use their SSO corporate identities through to log in to the Amazon SageMaker Unified Studio portal and access projects where they have memberships.

When an IAM identity or single sign-on identity is added as a user of the domain, a user profile is created. There are two types of user profiles:

User profile  
Created from an IAM user or a single sign-on user. The first time an IAM user or single sign-on user logs in to the Amazon SageMaker Unified Studio portal, the service creates a user profile.

IAM role session user profile  
When an IAM role principal is added to Amazon SageMaker Unified Studio, a group profile is created. For each user that federates with the IAM role, an IAM role session user profile is created. This allows the federated user to be identified when working within Amazon SageMaker Unified Studio. For example, the IAM role session user profile has its own space within a notebook.

You can create user profiles programmatically through the `CreateUserProfile` API call:
+ If `userType` is `IAM_USER` or `SSO_USER`, a user profile is created.
+ If `userType` is `IAM_ROLE` and `sessionName` is provided, an IAM role group profile and an IAM role session user profile are created.
+ If `userType` is `IAM_ROLE` and `sessionName` is not provided, an IAM role user profile is created.

**Implicit and explicit user creation**  
**Implicit user creation:** When an IAM role logs in to the portal for the first time, the service creates a group profile for the new IAM role and IAM role session user profiles for the user federating into Amazon SageMaker Unified Studio through the IAM role. Previously, the service created the IAM role as a user profile that was not session-aware. This also applies to API calls. If a user of an IAM role submits a call to get programmatic access, the service creates the session user profile the first time they log in.  
**Explicit user creation:** When you create users programmatically through the `CreateUserProfile` API, you can choose to create the IAM role as either a user profile that isn't session-aware or as a group profile with an IAM role session user profile. In the `CreateUserProfile` call:  
Passing only the IAM role ARN and type creates a user profile that isn't session-aware.
Passing the IAM role ARN, the `sessionName`, and type creates a group profile (if one does not already exist) and an IAM role session user profile.

## Group profiles
<a name="group-profiles"></a>

Group profiles represent groups of Amazon SageMaker Unified Studio users. Groups can be manually created or mapped to identity provider groups of enterprise customers. In Amazon SageMaker Unified Studio, groups serve two purposes:
+ A group can map to a team of users in the organizational chart, reducing the administrative work of a project owner when employees join or leave a team.
+ Corporate administrators use identity provider groups to manage and update user statuses, and domain administrators can use these group memberships to implement domain policies.

Group profiles are created by default for single sign-on groups and IAM roles that are added to the domain.

IAM roles  
When an IAM role is added to the domain, a group profile is created. The first time a user belonging to the group logs in to the Amazon SageMaker Unified Studio portal, an IAM role session user profile is created for the user federating through that IAM role. Project membership and access policies are managed through the IAM role group profile. To create IAM roles programmatically through the `CreateGroupProfile` API, supply the `rolePrincipalARN` to support IAM role session user profiles.

Single sign-on groups  
When a single sign-on group is added to the domain, a group profile is created. The first time a user belonging to the group logs in to the Amazon SageMaker Unified Studio portal, a user profile is created for the user. Project membership and access policies are managed through the single sign-on group profile. To create single sign-on groups programmatically through the `CreateGroupProfile` API, supply the `groupIdentifier`.

**Note**  
During project creation, the Amazon SageMaker Unified Studio service creates the project IAM role as a group profile and adds the group as a project member. An IAM role session user profile is created for the project IAM role. Any logic that depends on the project role being present as a user profile must be updated to handle its presence as a group profile.