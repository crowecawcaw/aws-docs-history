# Understanding the immediate

resource discovery experience

## Immediate resource discovery experience

Beginning October 6, 2025, Resource Explorer provides immediate resource discovery functionality
without requiring manual setup. When you first access Resource Explorer through the console,
[Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md"), CLI, or API, the service automatically enables search
capabilities based on your IAM permissions. Setup occurs when you use the Search or ListResources APIs from Resource Explorer either directly or through Unified Search. This eliminates the traditional setup
barrier and provides immediate value while maintaining all existing functionality for
customers who have already configured Resource Explorer.

The automatic experience provides different levels of functionality based on your
permissions:

- **Immediate search access:** If you have, at
  minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy, you
  can immediately search all tagged resources and supported untagged resources
  created after the [immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release.
- **Complete resource inventory:** For complete
  resource inventory with automatic updates, you'll also need the
  `iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy). Once the
  service-linked role is created in your account by any user, subsequent users
  need only the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy to
  create an index and view for full results on first search in each Region
  .
- **Enhanced functionality:** Cross-Region search
  capabilities remain available as optional enhancements that can be enabled with
  a single click.

This approach differs from the previous manual setup approach where users had to
explicitly configure indexes and views before they could search for resources. Now,
basic search functionality is available immediately, with enhanced features accessible
through progressive permission-based upgrades.

## Permission tiers and user

experiences

Resource Explorer provides three distinct user experiences based on your IAM
permissions:

### Tier 1: Full search experience

**Required permissions:** At minimum, the permissions
in the `AWSResourceExplorerReadOnlyAccess` managed policy and the
`iam:CreateServiceLinkedRole` permission (needed only for initial
service-linked role creation per account).

**Experience:** Complete resource search results with
automatic infrastructure creation. On first search, Resource Explorer automatically creates the
service-linked role and user-owned indexes and views in the Region, providing full
search functionality including all tagged and supported untagged resources with ongoing
automatic updates. On search in subsequent Regions, Resource Explorer automatically creates
user-owned indexes and views per Region. After the service-linked role is created in
your account by any user, subsequent users need only the permissions in the
`AWSResourceExplorerReadOnlyAccess` managed policy to create
an index and view for full results on first search in each Region.

**Available through managed policies:**
`AdministratorAccess`, `AWSResourceExplorerFullAccess`, or
custom policies with both permissions.

### Tier 2: Partial search

experience

**Required permissions:** At minimum, the permissions
in the `AWSResourceExplorerReadOnlyAccess` managed policy only
(missing `iam:CreateServiceLinkedRole` and service-linked role does not
already exist in account)

**Experience:** If no service-linked role exists in
your account, you get immediate partial search results from Resource Explorer-owned
indexes. Results include all tagged resources and supported untagged resources
created after the [immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release, but not complete historical data. If
the service-linked role already exists in your account (created by another user),
you can get full results in each Region you search with just the permissions in the
`AWSResourceExplorerReadOnlyAccess` managed policy.

**Available through managed policies:**
`ReadOnlyAccess`, `AWSResourceExplorerReadOnlyAccess`, or
custom policies with search and list indexes permissions only.

**Upgrade path:** To get complete results when no
service-linked role exists, obtain `iam:CreateServiceLinkedRole`
permission (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy) from your administrator
or sign in with a role that has this permission.

### Tier 3: No search access

**Permissions:** No `AWSResourceExplorerReadOnlyAccess` managed policy
permissions

**Experience:** Access denied errors when attempting
to search. This tier respects IAM boundaries and provides complete access
control.

**Upgrade path:** Obtain, at minimum, the permissions
in the `AWSResourceExplorerReadOnlyAccess` managed policy from your
administrator to access basic search functionality.

### Troubleshooting permission

issues

If you encounter permission-related issues:

- **Access denied errors:** You need, at
  minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy.
  Contact your administrator to obtain the necessary permissions or sign in
  with a role that has this permission.
- **Partial results only:** You have search
  permission but lack `iam:CreateServiceLinkedRole` permission
  (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy). You can continue
  with partial results or request additional permissions for complete
  functionality.
- **Service-linked role creation errors:** If
  you see errors about creating service-linked roles, you need
  `iam:CreateServiceLinkedRole` permission or must sign in with
  a role that has this permission.

## Understanding indexing progress and

completion

When Resource Explorer automatically creates infrastructure for complete search functionality,
indexing happens in the background. Understanding the progress indicators helps you know
what to expect.

### Timeline expectations

- **Immediate partial results:** Available
  instantly when you first access Resource Explorer with appropriate permissions.
- **Complete resource inventory:** Full
  indexing typically completes within minutes to hours, depending on the
  number of resources in your account and Regions.
- **Ongoing updates:** Once complete indexing
  finishes, resource updates are reflected in search results within
  minutes.

### Completion criteria and indicators

You can identify indexing progress and completion through several
indicators:

- **Console banners:** Blue banners indicate
  "indexing in progress" while green banners show "setup completed
  successfully."
- **Search result completeness:** Partial
  results include all tagged resources and supported untagged resources
  created after the [immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release. Complete results include your
  full supported resource inventory with historical data and automatic
  updates.
- **Index status:** You can check index status
  on the Settings page or using the `GetIndex` API operation.
  Active status indicates completed indexing.

Complete indexing means Resource Explorer has discovered and indexed all supported resource
types in your account, providing comprehensive search results with ongoing automatic
updates.
