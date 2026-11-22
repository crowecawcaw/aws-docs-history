

# Limit profiles


|  | 
| --- |
|    Intended audience:  System administrators and AWS Quick administrators  | 

With Limits Management, you can monitor resource consumption. You can cap per-user usage before account-level service limits are reached. You can govern two resource types: *index storage* and *agent hours*.

You create reusable *limit profiles* that define per-user limits, and then you assign those profiles to individual users, groups from your enterprise identity provider (IdP), roles, or the entire account as a default. Quick enforces the most specific assignment that applies to each user.

## Understanding index storage and agent hours
<a name="understanding-capacity"></a>

Limit profiles govern two resource types: index storage and agent hours. Understanding how each is measured helps you set effective per-user caps.

### Index storage
<a name="index-storage"></a>

Index capacity is measured by the original (raw) file size of documents at their source location before any processing by Quick. Supported source locations include Amazon S3, SharePoint, and Confluence. For full details on how index capacity is allocated, pooled, and purchased, see [Index capacity](https://docs.aws.amazon.com/quick/latest/userguide/manage-unstructured-data-capacity.html).

Index storage allocation is based on user count and subscription tier and is pooled at the payer-account level. Because the pool is shared, a single heavy user can consume capacity that would otherwise be available to other users. With limit profiles, you can cap individual consumption so that no single user exhausts the shared pool.

### Agent hours
<a name="agent-hours-metering"></a>

Agent hours measure the time consumed by AI-powered features in Quick. The following activities are metered:
+ Quick Research – Time from research request submission until the report completes.
+ Quick Flows – Runtime while workflows are actively executing, excluding idle and waiting time.
+ Quick Automate – Runtime of deployed automations.
+ Desktop app – Time spent actively using the AI assistant.
+ Custom apps – Runtime of AI-powered custom applications.
+ Artifact generation – Time spent generating documents, presentations, and images.

## Viewing usage
<a name="viewing-usage"></a>

Index capacity consumption is visible three ways: by user, by knowledge base, and by space. The **Per-user Capacity Overview** table provides an at-a-glance summary.

The **Per-user Capacity Overview** table provides an at-a-glance summary with the following columns.

User  
The user's display name.

Role  
The user's assigned role (Author or Reader).

Storage usage  
Current index storage that the user consumed.

Agent-hours usage  
Agent hours that the user consumed in the current billing cycle.

Usage distribution  
A breakdown of consumption across knowledge bases and spaces.

### User detail side panel
<a name="user-detail-side-panel"></a>

Select a user row to open a side panel that shows the following details:
+ Linked limit profiles for each resource type
+ Storage consumption compared to the user's effective limit
+ Agent-hours consumption for the current billing cycle
+ Usage distribution across knowledge bases and spaces

For additional analytics on agent-hours consumption trends, see [Usage metrics](https://docs.aws.amazon.com/quick/latest/userguide/qs-usage-metrics.html).

## Managing limit profiles
<a name="managing-limit-profiles"></a>

### Create a limit profile
<a name="create-limit-profile"></a>

Each limit profile requires a name and at least one limit. You can configure the following fields:
+ **Name** (required) – A descriptive name for the profile.
+ **Description** (optional) – Additional context about the profile's purpose.
+ **Storage limit** (optional) – The maximum index storage in GB that the user can consume.
+ **Agent hours per month** (optional) – The maximum agent hours the user can consume per billing cycle.

You must set at least one of the two limits (storage or agent hours) when creating a profile.

### Assign a limit profile
<a name="assign-limit-profile"></a>

You can assign a limit profile to the following:
+ An individual user
+ A group from your IdP
+ A role (Admin, Author, Reader, Admin Pro, Author Pro, or Reader Pro)
+ The account default, which applies to all users who do not have a more specific assignment

You can assign a limit profile to a group. Every member of the group receives the profile. A user can belong to more than one group, and each group can have its own assigned profile. Quick applies the profile's limits to each member of the group individually; members do not share the limit as a pool. For example, if you assign a profile with a 10 GB storage limit to a group of 50 users, each member can consume up to 10 GB of index storage. Group assignment is available in Quick Enterprise edition.

Assignments apply within a Quick namespace. A limit profile that you assign to a user or group in one namespace doesn't apply to users or groups in another namespace. If your account has more than one namespace, the assignments panel shows a list of namespaces, and you choose the namespace that you want to manage.

#### To assign a limit profile in Quick Admin
<a name="assign-in-quick-admin"></a>

1. Sign in to Quick as an administrator, open Quick Admin, and then choose **Limit profiles**.

1. Choose the limit profile that you want to assign.

1. Under **Assign profile**, choose **Manage assignment**. The panel lists the current assignments under **Currently assigned to this profile**, grouped by **Users**, **Groups**, **Roles**, and **Account**. If your account has more than one namespace, choose the namespace from the list at the top of the panel.

1. To assign the profile to a user or group, in **Find assignees**, search for the user or group. To narrow the search, choose **Users** or **Groups** from the list next to the search box. Matches appear under **Not assigned to this profile**. Choose **Add user** or **Add group** next to the match.

1. To assign the profile to a role, expand **Roles**, and then choose **Add role** next to the role.

1. To make the profile the account default, expand **Account**, and then choose **Add account** next to your account.

1. In **Confirm assignment changes**, review the change, and then choose **Confirm & apply**.

To remove an assignment, under **Currently assigned to this profile**, choose the options menu next to the user, group, role, or account, and then choose **Remove**.

#### Import and download assignments
<a name="import-download-assignments"></a>

To import, download, or remove assignments in bulk, choose the options menu next to **Currently assigned to this profile**, and then choose **Import**, **Download**, or **Remove all**. Import adds users and groups from a CSV or text file. List one email address, user name, or group name on each line, or in the first column of a CSV file. To set the namespace for each row, add the header row `identifier,namespace` and put the namespace in the second column. Rows without a namespace, and files without a header row, use the namespace selected in the panel. Import doesn't add roles or the account default; assign those from the **Roles** and **Account** sections. Quick lists the matched users and groups for you to confirm before it adds them. Each import file can contain up to 500 assignments; to import more, upload additional files. A download includes up to 10,000 assignments in one file. If a profile has more than 10,000 assignments, the file contains the first 10,000, and Quick displays a warning that not all assignments are included. You can browse all assignments in the panel without a limit.

#### Assign a limit profile through the API
<a name="assign-through-api"></a>

You manage user, group, and account assignments through the Quick governance policy management operations. In these operations, you identify the limit profile by its policy ARN (`PolicyArn`) and the user, group, or account by its principal ARN (`PrincipalArn`). For limit profiles, the policy type (`PolicyType`) is `LIMITS_PROFILE`. Role assignments are not available through these operations; to assign a limit profile to a role, use Quick Admin. If your IAM policies already allow `quicksight:BatchAssignLimitsProfile` and `quicksight:BatchUnassignLimitsProfile`, those permissions also authorize these operations for limit profiles, and you don't need to add permissions. The following table lists the operations that manage limit profile assignments. For request syntax, see the [AWS Quick API Reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).


| Operation | Description | 
| --- | --- | 
| PutPolicyAssignment | Assigns a limit profile to one user, group, or account, replacing any existing limit profile assignment on that principal. Returns the assigned PolicyArn, the displaced profile as ReplacedPolicyArn if one was replaced, and the new Revision. | 
| BatchPutPolicyAssignmentByPolicy | Assigns one limit profile to between 1 and 50 principals in a single call. The call is not atomic: The response lists Success and Errors for each principal, so inspect Errors for any principals that failed. | 
| GetPolicyAssignment | Returns the limit profile currently assigned to a principal for a given PolicyType, using a strongly consistent read. A principal with no assignment returns an empty result. | 
| DeletePolicyAssignment | Removes a principal's assignment to the named limit profile. It is idempotent: Removing an assignment that is not present still succeeds. If the principal is assigned a different limit profile, the call fails with a conflict, so you do not remove the wrong one. | 
| BatchDeletePolicyAssignmentByPolicy | Removes between 1 and 50 principals' assignments to one limit profile in a single call. The call is not atomic: Inspect Success and Errors. | 
| ListPrincipalsForPolicy | Lists the principals assigned to a limit profile (a reverse lookup by PolicyArn). Optionally filter by PrincipalType, for example, GROUP. Results are paginated with MaxResults (1 to 100) and NextToken, and are eventually consistent. | 

These operations share the following parameters.

`AccountId`  
The ID of the AWS account that contains the Quick account.

`PolicyArn`  
The ARN of the limit profile to assign or remove, in the format `arn:aws:quicksight:region:account-id:limits-profile/profile-id`.

`PrincipalArn`  
The ARN of the user, group, or account the assignment applies to.

`PolicyType`  
The policy type. For limit profiles, use `LIMITS_PROFILE`.

`PrincipalType`  
The principal type. For limit profiles, use `USER`, `GROUP`, or `ACCOUNT`. On `ListPrincipalsForPolicy`, this is an optional filter.

`ExistingPolicyArn`  
(Optional) The limit profile you believe is currently assigned to the principal. When you provide it, the write proceeds only if it matches the current assignment, which prevents overwriting an assignment that changed since you last read it.

`Revision`  
(Optional) A compare-and-set token returned by the most recent read. When you provide it on a write, the change is applied only if it matches the assignment's current revision, which guards against concurrent updates.

##### Example commands (AWS CLI)
<a name="assign-api-cli-examples"></a>

The following examples show how to manage limit profile assignments with the AWS Command Line Interface (AWS CLI). The example commands use placeholders for values that you replace with your own:
+ `account-id` – The ID of your AWS account.
+ `region` – The AWS Region of your Quick account.
+ `profile-id` – The ID of the limit profile.
+ `user-name` – The name of the user, in the default namespace.
+ `group-name` – The name of the group, in the default namespace.

`PutPolicyAssignment` assigns the limit profile to one group:

```
aws quicksight put-policy-assignment \
--account-id account-id \
--policy-arn arn:aws:quicksight:region:account-id:limits-profile/profile-id \
--principal-arn arn:aws:quicksight:region:account-id:group/default/group-name
```

To make the limit profile the account default, use the account as the principal:

```
aws quicksight put-policy-assignment \
--account-id account-id \
--policy-arn arn:aws:quicksight:region:account-id:limits-profile/profile-id \
--principal-arn arn:aws:quicksight:region:account-id:account/account-id
```

To make the assignment conditional, add `--existing-policy-arn` (the limit profile you expect is currently assigned) or `--revision` (the token from your last read). The assignment proceeds only if the value matches the current assignment:

```
aws quicksight put-policy-assignment \
--account-id account-id \
--policy-arn arn:aws:quicksight:region:account-id:limits-profile/profile-id \
--principal-arn arn:aws:quicksight:region:account-id:group/default/group-name \
--existing-policy-arn arn:aws:quicksight:region:account-id:limits-profile/existing-profile-id \
--revision 3
```

`BatchPutPolicyAssignmentByPolicy` assigns one limit profile to up to 50 users, groups, or accounts. The call is not atomic, so the output reports `Success` and `Errors` separately:

```
aws quicksight batch-put-policy-assignment-by-policy \
--account-id account-id \
--policy-arn arn:aws:quicksight:region:account-id:limits-profile/profile-id \
--assignments \
PrincipalArn=arn:aws:quicksight:region:account-id:group/default/group-1 \
PrincipalArn=arn:aws:quicksight:region:account-id:user/default/user-name
```

`GetPolicyAssignment` returns the limit profile currently assigned to a principal:

```
aws quicksight get-policy-assignment \
--account-id account-id \
--policy-type LIMITS_PROFILE \
--principal-arn arn:aws:quicksight:region:account-id:group/default/group-name
```

`DeletePolicyAssignment` removes a principal's assignment to the named limit profile:

```
aws quicksight delete-policy-assignment \
--account-id account-id \
--policy-arn arn:aws:quicksight:region:account-id:limits-profile/profile-id \
--principal-arn arn:aws:quicksight:region:account-id:group/default/group-name
```

`BatchDeletePolicyAssignmentByPolicy` removes up to 50 principals' assignments to one limit profile:

```
aws quicksight batch-delete-policy-assignment-by-policy \
--account-id account-id \
--policy-arn arn:aws:quicksight:region:account-id:limits-profile/profile-id \
--principal-arns \
arn:aws:quicksight:region:account-id:group/default/group-1 \
arn:aws:quicksight:region:account-id:user/default/user-name
```

`ListPrincipalsForPolicy` lists the principals assigned to a limit profile. Filter with `--principal-type` and page with `--max-results` and `--next-token`:

```
aws quicksight list-principals-for-policy \
--account-id account-id \
--policy-arn arn:aws:quicksight:region:account-id:limits-profile/profile-id \
--principal-type GROUP \
--max-results 50
```

### Resolution hierarchy
<a name="resolution-hierarchy"></a>

A limit profile can apply to a user at several levels. Quick applies the most specific assignment, in this order: user, then group, then role, then account. Quick resolves each limit type separately. For storage and for agent hours, Quick uses the value from the most specific level that sets that limit type. A profile assigned directly to a user overrides any group profiles, and group profiles override role and account profiles, for each limit type that the profile sets. If a profile doesn't set a limit type, Quick takes that limit type from the next level that sets it.
+ **User-level** – A limit profile assigned directly to a user takes the highest priority.
+ **Group-level** – A limit profile assigned to a group applies to all members of the group unless overridden by a user-level assignment. When a user belongs to more than one group that has an assigned profile, Quick combines those profiles. For more information, see [How Quick resolves multiple group assignments](#resolve-multiple-group-assignments).
+ **Role-level** – A limit profile assigned to a role applies to all users in that role unless overridden by a group-level or user-level assignment.
+ **Account-level** – The account default profile applies to all users unless overridden by a group-level, role-level, or user-level assignment.
+ **System default** – The built-in subscription entitlement applies when no administrator-configured profile is in effect.

The rules for multiple groups apply when the group level applies, that is, when no profile assigned directly to the user sets that limit type. To give one member of a group a different limit, assign a limit profile directly to that user.

#### How Quick resolves multiple group assignments
<a name="resolve-multiple-group-assignments"></a>

When a user belongs to more than one group and the group level applies, Quick combines all of the user's group profiles. For each limit type, the user receives the highest value across those profiles. Quick evaluates storage and agent hours separately, so the effective storage limit and the effective agent hours limit can come from different profiles. The order of the groups does not matter. The combined result is the same. A group profile that sets only one limit type contributes only to that limit type. If none of the user's group profiles sets a limit type, Quick takes that limit type from the role level, then the account level, and then the system default.

For example, a user belongs to two groups. The group **Finance analysts** has a profile with a 20 GB storage limit and 10 agent hours per month. The group **Research** has a profile with a 5 GB storage limit and 40 agent hours per month. The following table shows how the two profiles combine for the user.


| Assignment | Storage limit (GB) | Agent hours per month | 
| --- | --- | --- | 
| Finance analysts group profile | 20 | 10 | 
| Research group profile | 5 | 40 | 
| Effective limit for the user | 20 | 40 | 

In this example, the user can consume up to 20 GB of index storage, from the **Finance analysts** profile, and up to 40 agent hours per month, from the **Research** profile. This differs from custom permissions. For custom permissions, Quick uses the most restrictive combination: A capability that any group profile denies is denied for the user. For limit profiles, Quick uses the highest limit for each limit type across the user's group profiles.

**Important**  
A limit profile that you read for an individual user reflects only a profile that you assigned directly to that user. It doesn't reflect a profile that applies through group membership, which might fall through to the group, role, or account level. To see the effective limits for a user, including limits that come from group membership, use **Check effective limits**. For more information, see [Check effective limits](#check-effective-limits).

#### Check effective limits
<a name="check-effective-limits"></a>

Use **Check effective limits** on a limit profile's page to verify which limits apply and the level at which they apply (user, group, role, or account). Choose **User**, **Group**, **Role**, or **Account**, and then search for the principal. When the group level applies, a user can belong to more than one group that has an assigned profile. In that case, the effective limits combine the profiles from all of those groups. After you create, change, or remove an assignment, the new effective limits can take up to 15 minutes to take effect.

## How limits are enforced
<a name="limit-enforcement"></a>

As long as a user stays below their effective limit, they can work without interruption.

When a user reaches 100% of a limit:
+ **Index storage** – New file uploads and knowledge base ingestion are blocked for that user.
+ **Agent hours** – New agent invocations are blocked until the next billing cycle begins.

Existing content is always preserved. Tightening a limit never deletes files or knowledge bases.

Enforcement is global across all AWS Regions. Usage in any Region counts toward the same per-user limit.

## End-user visibility
<a name="end-user-visibility"></a>

Your users can view their own consumption in the **My usage** widget (available in **My stuff**). The widget shows:
+ Agent hours used compared to their monthly limit. This value resets at the start of each billing cycle.
+ Index storage capacity consumed compared to their effective limit.

For programmatic management of limit profiles, see the AWS Quick API Reference.