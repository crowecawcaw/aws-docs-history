# Using Unified Search in the AWS Management Console

The AWS Management Console includes a search bar at the top of every AWS console page. This search
bar can search the AWS service documentation and blog topics, and take you directly to
AWS service console pages. It can also return the resources in your AWS account when you
have appropriate Resource Explorer permissions.

With [Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md"), users can search for resources from **_any_** AWS service console without having to first
navigate to the AWS Resource Explorer console. Unified Search returns regional results from the current
Region by default, or cross-region results if an aggregator index is configured.

Access to resource results in Unified Search is permission-based. Users with, at minimum,
the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy can immediately
search for resources in any Region where they have access, with results varying based on
their permission level and the type of indexes available in the Region.

###### Tip

When you want to use the Unified Search bar to search specifically for resources,
begin your search query by typing `/Resources`. This causes AWS
resources to be ranked higher in the search results than results that do not represent
resources.

###### Topics

- [Checking if resource search is enabled](#check-unified-search "#check-unified-search")
- [Enabling Unified Search](#enable-unified-search "#enable-unified-search")

###### Important

Unified Search automatically inserts a wildcard character (`*`) operator at the
end of the first keyword in the string. This means that unified search results include resources
that match any string that starts with the specified keyword.

The search performed by the **Query** text box on the [Resource search](https://console.aws.amazon.com/resource-explorer/home#/explorer "https://console.aws.amazon.com/resource-explorer/home#/explorer") page in the
Resource Explorer console does **_not_**
automatically append a wildcard character. You can insert a `*` manually after
any term in the search string.

## Checking if resource search is enabled

To see if resource search is enabled in your AWS account, verify that the following
requirements for Resource Explorer are met:

- Users must have, at minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy. Resource Explorer
  automatically provides search functionality, with results varying based on
  permission level and index type (user-owned indexes provide complete results,
  Resource Explorer-owned indexes provide partial results).
- (Optional) For cross-region search results, you can create an aggregator index
  in a Region of your choice. Without an aggregator, Unified Search returns
  regional results from the current Region.

## Enabling Unified Search

Resource search in Unified Search is automatically available when users have
appropriate Resource Explorer permissions. To enhance Unified Search functionality with full
results, cross-Region results, or custom views, you can optionally complete the
following steps:

1. (Optional) [Creating user-owned indexes for enhanced
   Resource Explorer functionality](manage-service-turn-on-region.md "manage-service-turn-on-region.md") to create
   user-owned indexes for complete search results.
2. (Optional) [Enabling cross-Region search by creating an
   aggregator index](manage-aggregator-region.md "manage-aggregator-region.md") to enable cross-Region
   search results.
3. (Optional) [Configuring a Resource Explorer view to provide access to
   resource searches](customer-views.md#configure-views "customer-views.md#configure-views") for specific filtering
   requirements or access control.
