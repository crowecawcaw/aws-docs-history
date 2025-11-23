# User views

User views are created and managed by users or administrators. When automatic setup
occurs, Resource Explorer creates user-owned default views that include tags for comprehensive
filtering capabilities.

When you create a view, you specify filters that restrict which resources are included
in search results. For example, you could choose to include only resources of a few
specified resource types that are used by those to whom you grant access to this view.
Results from queries that users make with a view are always automatically filtered to
include only those resources that match the view's criteria.

To grant access to use a view, you can use assign permissions using one of the
following methods.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:

      + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
      + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

  Grant permission to allow your roles, groups, or users to invoke the
  `resource-explorer-2:GetView` and `resource-explorer-2:Search`
  operations on a view identified by its [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md"). Alternatively, you can use the
  [Resource Explorer read only
  AWS managed policy](security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess "security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess") for all principals who need to use the view to search.
  You can create multiple views that have different filters and scopes and thus return
  different subsets of your resource information. Then, you can grant permissions for each
  view to those users who need to see the information included by that view's
  results.

## Configuring a Resource Explorer view to provide access to

resource searches

Views are the key to searching for your resources. Every AWS Resource Explorer search
operation must use a view. Views are the method the administrator can use to
control access to the information about resources in your AWS account.

A view can be accessed by only principals (IAM roles or users) that have
permission to use that view. To search successfully with Resource Explorer, a principal must
have `Allow` access to both the `resource-explorer-2:GetView`
and `resource-explorer-2:Search` operations on the view's
[ARN](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

Views contain built-in filters that the administrator can use to limit results
to only items of interest. For example, you can create a view that includes only
resources related to a certain project. Users who don't need to see information
about other projects can use this view to see only those resources of
interest.

A view is a Regional resource. The view is created and stored in a specific
AWS Region and returns in its results only information from the index in that
Region. To include results from across all Regions in the account, the view must
reside in the Region that contains the [aggregator
index](getting-started-terms-and-concepts.md#term-aggr-index "getting-started-terms-and-concepts.md#term-aggr-index"). That Region contains a replica of the indexes from all other
Regions in the account.

There are several key elements to every view:

**Permissions to search**

You can use standard AWS permission policies to control who can use
each view. This is provided by [identity-based permission policies](../../../IAM/latest/UserGuide/access_policies.md#policies_id-based "../../../IAM/latest/UserGuide/access_policies.md#policies_id-based") attached to the
principals that give you granular control over who can see the
information provided by each view. For example, you can grant access to
the `Production-resources` view to allow searching only by
the engineers that operate your production services. Then, you can grant
different permissions to the `Pre-production-resources` view
to allow searching for pre-production resources by your
developers.

If you use the AWS managed policy named
`AWSResourceExplorerReadOnlyAccess` with your principals, it
grants them the ability to search using any view in the account.

Alternatively, you can create your own permissions policy and grant
the following permissions for only specified views:

- `resource-explorer-2:GetView`
- `resource-explorer-2:Search`

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

For more information about permissions related to views, see [Granting access to Resource Explorer views for
search](configure-views-grant-access.md "configure-views-grant-access.md").

**Filtering the search**

A view serves as a virtual window through which the user can see the
resources in the account. You can create multiple views, each presenting
a different view of the larger picture. For example, you can create
a view that allows searching only resources associated with your
pre-production environment, as identified by tags attached to your
resources. Then, you could create a separate view that allows searching
only resources in your production environment, based on different values
in the tags. If you configure multiple views with different
`FilterString` values, you don't have to re-enter those
query parameters every time you [Search](../apireference/API_Search.md "../apireference/API_Search.md").

Views also can specify which optional pieces of information about
the resources to include in the results. The default list of fields is
always included in results. In addition to the default list, you can
request that the view also include any tags attached to the
resource.

**Scope of the search**

- **Region scope** – When
  you search in an AWS Region with Resource Explorer, the results can
  include only resources that are indexed in that Region. The
  index in most Regions is labelled `LOCAL` because it
  contains information about resources within only that Region.
  Searches in those Regions can return only those resources.
- **Account scope** – You
  can promote one local index to be the aggregator index for the
  account. When you do this, all other Regions where Resource Explorer is
  turned on replicate their index information to the Region with
  the aggregator index. If you search in that Region, those results
  include resources from all Regions with user-owned (local)
  indexes in the account. When you use the **Quick
  Setup** option to configure the server, Resource Explorer
  automatically creates an aggregator index in the Region you specify.
  Also, the **Quick Setup** option creates a
  default view in that Region to support searching all resources
  in the account across all Regions with user-owned (local)
  indexes.

### Default views

If a user attempts to search without explicitly specifying a view, Resource Explorer uses
the _default view_ defined for that
AWS Region.

Resource Explorer automatically creates a default view as follows:

- If you turn on Resource Explorer using the AWS Management Console and choose the
  **Quick setup** option, you must specify which
  Region contains the aggregator index for the account. Resource Explorer automatically
  creates a default view in the specified aggregator index Region.
- If you register Resource Explorer using the AWS Management Console and choose the
  **Advanced setup** option, you can _optionally_ choose to create the
  aggregator index for the account in a specified Region. If you do this,
  Resource Explorer creates a default view automatically in the aggregator index Region.
- If you register Resource Explorer by using the console and choose _not_ to register an aggregator index Region, Resource Explorer
  creates a default view for the local index in each Region.
- If you register Resource Explorer by using the AWS CLI or the API operations,
  Resource Explorer doesn't automatically create a default view. Instead, you must
  configure the default view manually for each Region where you expect
  users to search from.

###### Topics

- [Creating Resource Explorer views to use for search](configure-views-create.md "configure-views-create.md")
- [Granting access to Resource Explorer views for
  search](configure-views-grant-access.md "configure-views-grant-access.md")
- [Setting a default view in an
  AWS Region](configure-views-set-default.md "configure-views-set-default.md")
- [Adding tags to views](configure-views-tag.md "configure-views-tag.md")
- [Sharing Resource Explorer views](configure-views-share.md "configure-views-share.md")
- [Deleting views in Resource Explorer](configure-views-delete.md "configure-views-delete.md")
