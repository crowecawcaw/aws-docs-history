# Using AWS Resource Explorer to search for resources

AWS Resource Explorer provides immediate search capabilities for your AWS resources without
requiring manual setup. When you access Resource Explorer with the appropriate permissions, the service
automatically enables resource search functionality in your account. You can use the
AWS Management Console or the AWS Command Line Interface (AWS CLI) to search for resources using Resource Explorer.

The search experience you receive depends on your IAM permissions. With basic (Read-Only) search
permissions, you get immediate access to partial results. With additional permissions, you receive complete resource inventory and
enhanced functionality.

The following are some of the main characteristics of Resource Explorer search.

- **Resource Explorer automatically enables search functionality based on
  your permissions.**

When you access Resource Explorer with the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy, the
service automatically provides search capabilities. Users with both the permissions
in the `AWSResourceExplorerReadOnlyAccess` managed policy and the
`iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy) receive complete resource
inventory. The `iam:CreateServiceLinkedRole` permission (included in the
[AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy) is only needed until the
first user creates the service-linked role for the account. Once created,
users with only the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy will also receive complete results in subsequent Regions where they search. Users without the
service-linked role receive partial results immediately (all tagged resources plus
untagged resources created after the [feature launch](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")).

- **Every search uses a view.**

The view is what Resource Explorer uses to determine who has permissions to see which
resources. To use a view in a Resource Explorer search operation, the user must have an
`Allow` on the `resource-explorer-2:Search` operation for
the specified view. This permission comes from an [identity-based permission policy](configure-views-grant-access.md "configure-views-grant-access.md")
attached to the principal making the request.

The view can include a filter that limits which resources can be included in the
results. By creating different views that use filters and by granting different
principals access to different views, you can configure an environment where each
group of users can view only the resources relevant to them.

Resource Explorer provides both user-owned views (which you create and manage) and Resource
Explorer-owned views (which are service-managed and cannot be modified or deleted).
Resource Explorer-owned views do not include resource tags in search results. If no
user-owned view is available, Resource Explorer automatically falls back to using a Resource
Explorer-owned view to ensure search functionality remains available.

For more information about views, see [Configuring a Resource Explorer view to provide access to
resource searches](customer-views.md#configure-views "customer-views.md#configure-views").

- **Resource Explorer uses asynchronous background processes to maintain
  its indexes.**

It can take Resource Explorer some time for its indexing processes to discover newly created
or modified resources and add them to the local index. It can take additional time
for Resource Explorer to replicate changes in the local indexes to the aggregator index.

The same applies to resources that you delete. It can take some time after you
delete a resource for that deletion to be discovered by the indexing process and
that resource's information to be removed from the local index. Additional time is
needed for Resource Explorer to replicate that deletion from the local index to the account's
aggregator index.

Most resource modifications and deletions are visible in search results within
minutes in all Regions where you’ve completed setup for Resource Explorer. In some cases,
modifications or deletions may take up to two weeks to be visible.

- **Search results may be partial during initial
  indexing.**

During the initial indexing process after automatic setup, you may see partial
results while the complete resource inventory is being built. Users with appropriate
permissions will see indexing progress indicators in the console, and results will
become more complete as indexing progresses.

- **A search in Resource Explorer occurs within an
  AWS Region.**

Each Region where you complete setup for Resource Explorer contains an index of only the
resources stored in that Region. Views are also associated with Regions, and can
return only the resources found in that Region's index. The one exception to this is
the aggregator index, that receives a replicated copy of all of the local indexes to
support searching across all Regions in the account.

- **Cross-Region search requires an aggregator index for the
  account.**

To let users search for resources across all AWS Regions, the administrator must
designate one Region to contain the aggregator index for the account. A copy of every
local index is automatically replicated to the aggregator index.

Because of this, only views in the aggregator index Region can return results that include
resources from all AWS Regions in the account.

- **A query consists of any number of free-form text keywords
  and filters.**

Free-form keywords are combined in the query using logical **`OR`** operators. [Filters that use Resource Explorer defined filter names](using-search-query-syntax.md#query-syntax-filters "using-search-query-syntax.md#query-syntax-filters") are combined in the query
using logical **`AND`** operators. Consider
the following example query.

```
test instance service:EC2 region:us-west-2
```

This is evaluated by Resource Explorer as follows.

```
test **OR** instance **AND** service:EC2 **AND** region:us-west-2
```

This query requires that matching resources must be Amazon EC2 resources in the
US West (Oregon) Region, and have at least one of the keywords (_test_, _instance_)
attached in some way, such as in the name, description, or tags.

###### Note

Because of the implicit `AND`, you can successfully use only one
filter for an attribute that can have only one value associated with the
resource. For example, a resource can be part of only one AWS Region.
Therefore, the following query returns no results.

```
region:us-east-1 region:us-west-1
```

This limitation does **_not_** apply to the filters for attributes that can
have multiple values at the same time, such as `tag:`,
`tag.key:`, and `tag.value:`.

- **A search can return only the first 1,000 results if
  you include free-form text.**

If your query includes free-form text, Resource Explorer uses the `Search` API
operation, but if your query does not include free-form text, Resource Explorer uses the
`ListResources` operation. `Search` operations are limited
to 1,000 results that are sorted by relevancy, while the
`ListResources` operation has no upper limit and are
_not_ sorted by relevancy. To view query resources beyond
1,000 results when using free-form text (the `Search` operation),
you must use additional filters to restrict matching results to those you want to
see.

- **There is a per-account quota on the number of search
  operations that you can perform.**

Quotas limit how many queries you can make per second, and how many queries you
can make each month. For specific quota numbers, see [Quotas for Resource Explorer](quotas.md "quotas.md"). Quota usage depends on if Resource Explorer performs resource queries
using the `Search` or `ListResources` operations on your
behalf based on the logic described in the previous list item.

AWS Management Console

###### To search for resources using Resource Explorer

1. On the **[Resource search](https://console.aws.amazon.com/resource-explorer/home#/search "https://console.aws.amazon.com/resource-explorer/home#/search")** page, start by choosing the view that you want to
   use. You can choose from among only those views that you have
   permissions to access.
2. (Optional) Choose a [Query
   template](#query_templates "#query_templates").
   1. For templates that require a specified resource type or
      application, **choose a value**.
   2. Choose **Apply**.

3. (Optional) In the [Quick
   filters](#quick_filters "#quick_filters") menu, choose one or more filters to
   apply to the search query.
4. (Optional) For **Query**, enter the search terms and
   [filters](using-search-query-syntax.md#query-syntax-filters "using-search-query-syntax.md#query-syntax-filters") that identify
   the resources you want to see. For information about all of the
   available syntax options, see [Search query syntax reference for Resource Explorer](using-search-query-syntax.md "using-search-query-syntax.md").
5. Resource Explorer displays all of the results that match both the
   `Filter` defined in the view and the
   **Query** that you provide. If your query includes
   free-form text, the results are sorted by relevance, with those
   resources that match more of your query terms appearing higher in the
   list and resources that match fewer terms appearing further down the
   list.
6. You can view details about the selected resource from within Resource Explorer by
   selecting the checkbox in the table.

Alternatively, you can choose the identifier of a resource to navigate
to that resource type's native console, where you can interact with the
resource in all of the ways supported by that AWS service.

After submitting your search query, Resource Explorer displays a results table. You can
use the

AWS CLI

###### To search for resources using Resource Explorer

Run the following command to search for resources using the specified
view. That view must exist in the Region in which you run the operation. The
following example searches for Amazon EC2 instances that are tagged
`env=production` in the US East (Ohio)
(us-east-2). For information about all of the available
syntax options for the `query-string` parameter, see [Search query syntax reference for Resource Explorer](using-search-query-syntax.md "using-search-query-syntax.md").

```
`$` `aws resource-explorer-2 search \
 --region us-east-1 \
 --query-string "resourcetype:AWS::EC2::Instance tag:env=production"
 --view-arn arn:aws:resource-explorer-2:us-east-2:123456789012:view/My-Resources-View/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111`
```

## Quick filters

The Resource Explorer console provides Quick filters so you can quickly and easily apply filters
like Region, Resource type, or Tag keys and values to your resource query. You can use
Quick filters independently, or in addition to the free-form keyword and defined filter
query.

The Quick filters menu only displays category filter values matching loaded resource
data. For accounts with more than 1,000 resources, you can choose **Load more** at the top of the Resources table to view additional resources
and filter values.

For example, by default the Region category displays five Regions for the first 1,000
loaded resources. After you load more data, the Region category displays a total of 12
Regions across 2,000 resources.

### Search query templates

The Resource Explorer console provides search query templates, which are predefined query
configurations for common queries. Query templates allow you to quickly perform a
search and better understand how to customize your own queries. For some templates,
you must specify the desired resource type or application in the template filter.
After selecting a query template, you can add additional query strings and filters.

You can choose from the following query templates:

- **Tagged resources** — This template
  returns resources with user or system tags, including tagged resource types
  that are not supported by Resource Explorer.
- **All untagged resources** — This
  template returns resources with no user or system tags.
- **All non-taggable resources** — This
  template returns resources that do not support tagging.
- **All untagged resources of
  [`type`]** — This template
  returns resources with no user tags of the specified type.
- **Resources not in
  [`application`]** — This template
  returns resources that do not belong in the specified application.
- **All resources in
  [`application`]** — This template
  returns resources that belong to the specified application.
- **Amazon EC2 resources that are not instances in
  [`application`]** — This
  template returns Amazon EC2 resources that are _not_ the
  `ec2:instance` resource type and that belong in the specified
  application.
