AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Creating Resource Explorer views to use for search

All searches must use a [view](customer-views.md#configure-views "customer-views.md#configure-views"). A view defines filters that determine which resources can
be returned by queries that use the view. Views also control who can search for
resources.

###### Resource Explorer-owned views

Resource Explorer provides Resource Explorer-owned views that are service-managed and cannot be modified or
deleted by users. These views serve as automatic fallbacks to ensure search
functionality remains available even when no user-owned views exist in a Region.
Resource Explorer-owned views do not include resource tags in search results.

When automatic setup occurs, Resource Explorer creates a default user-owned view in each Region
that includes Tags. The view hierarchy follows this priority: user-owned views are used
first, with automatic fallback to Resource Explorer-owned views when no user-owned view is
available.

A view is stored in an AWS Region, and returns search results from only that Region's
index. If the Region contains the [aggregator index](manage-aggregator-region.md "manage-aggregator-region.md"), then the view returns
search results from the user-owned index in every Region in the account.

Multi-account views allow you to search for resources in accounts across your
organization. Only the management account, or a delegated administrator for the
organization, can create a multi-account view. Resource Explorer can create a default view for you
during initial set up if you chose the relevant options in either [Quick Setup](https://console.aws.amazon.com/systems-manager/quick-setup/create-configuration?configurationType=AWSQuickSetupType-ResourceExplorer "https://console.aws.amazon.com/systems-manager/quick-setup/create-configuration?configurationType=AWSQuickSetupType-ResourceExplorer") for Resource Explorer in the Systems Manager console.
At any later time, you can create additional views that have different filters for different
sets of users.

You can create a view by using the AWS Management Console or by running AWS CLI commands or their equivalent API
operations in an AWS SDK.

###### Minimum permissions

To run this procedure, you must have the following permissions. Note that with
Resource Explorer's automatic setup, view creation is optional since Resource Explorer-owned views provide
fallback search functionality:

- **Action:**
  `resource-explorer-2:CreateView`

**Resource:** This can be `*` to allow
creation of a view in any AWS Region in the account.

- **When view creation is needed:** While Resource Explorer
  automatically creates default views during setup and provides Resource
  Explorer-owned views as fallbacks, you may want to create custom views for specific
  filtering requirements, tag-based searches, or to control access permissions for
  different user groups.

AWS Management Console

###### To create a view

1. Open the Resource Explorer console **[Views](https://console.aws.amazon.com/resource-explorer/home#/views "https://console.aws.amazon.com/resource-explorer/home#/views")** page and choose **Create
   view**.
2. On the **Create view** page, for
   **Name**, enter a name for the view.

The name must be no more than 64 characters long, and can include
letters, digits, and the hyphen (-) character. The name must be unique
within its AWS Region. 3. Choose the AWS Region in which you want to create the view. To
create a view that returns resources from all Regions in the account,
choose the AWS Region that contains the aggregator index. 4. (Optional) For **Scope**, choose whether your search
returns multi-account resources, or returns resources only from your
account. Account level scope is the default.

Only the management account or delegated administrator can see the
option to create a multi-account view. 5. Choose whether to filter the results.

    * **Include all resources**


    No query filters are included. All resources in the index
     associated with the view can be returned in search
     results.
    * **Include only resources that match a specified
     filter**


    Turns on the **Resource filters** check box
     where you can choose filter *names* and *operators*. For an
     explanation of each of the available filter names and operators,
     see [Filters](using-search-query-syntax.md#query-syntax-filters "using-search-query-syntax.md#query-syntax-filters").
    * Choose the optional resource attributes to include in results
     from this view. Select the check box next to
     **Tags** to let users search for resources
     based on their tag key names and values. If you don't include
     tags in the view then users can't make search requests that use
     tag keys and values to further filter the results.
    * Optionally, you can attach tags to the view. Expand the
     **Tags** box, and enter up to 50 tag
     key/value pairs. You can use tags to categorize resources, or as
     part of an attribute-based access control (ABAC) security
     permission strategy. For more information, see [Adding tags to views](configure-views-tag.md "configure-views-tag.md").
    * Choose **Create view**.

The console returns to the **Search** page where you
can use your new view to perform a search.

**Next step:** Grant the principals in
your account permissions to search with your new view. For more
information, see [Granting access to Resource Explorer views for
search](configure-views-grant-access.md "configure-views-grant-access.md")

AWS CLI

###### To create a view

Run the following command to create a view in the specified AWS Region.
The following example creates a view that returns only resources related to
the Amazon EC2 service that are tagged with a `Stage` key and the
value `prod`.

```
`$` `aws resource-explorer-2 create-view \
 --region us-west-2 \
 --view-name "My-EC2-Prod-Resources" \
 --filters FilterString="service:ec2 tag:stage=prod" \
 --included-properties Name=tags``{
 "View": {
 "Filters": {
 "FilterString": "service:ec2 tag:stage=prod"
 },
 "IncludedProperties": [
 {
 "Name": "tags"
 }
 ],
 "LastUpdatedAt": "2022-08-03T16:13:37.625000+00:00",
 "Owner": "123456789012",
 "Scope": "arn:aws:iam::123456789012:root",
 "ViewArn": "arn:aws:resource-explorer-2:us-west-2:123456789012:view/My-EC2-Prod-Resources/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111"
 }
}`
```

###### To create an organization level view

The following example creates a view that returns resources from
across your organization. This must be performed by the organization's
management account, or a delegated administrator account.

1. Run the `aws organizations describe-organization` command
   to get your organization ARN.
2. Run the following command to create a view for the specified
   organization.

```
`$` `aws resource-explorer-2 create-view \
 --region us-west-2 \
 --view-name entire-org-view \
 --scope "arn:aws:organizations::111111111111:organization/o-exampleorgid"``{
 "View": {
 "Filters": {
 "FilterString": ""
 },
 "IncludedProperties": [],
 "LastUpdatedAt": "2022-08-03T16:13:37.625000+00:00",
 "Owner": "111111111111",
 "Scope": "arn:aws:organizations::111111111111:organization/o-exampleorgid",
 "ViewArn": "arn:aws:resource-explorer-2:us-west-2:111111111111:view/entire-org-view/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111"
 }
}`
```

###### To create an organizational unit level view

The following example creates a view that returns resources from all
members of this organizational unit. This view behaves similarly to an
organizational level view. This must be performed by the organization's
management account, or a delegated administrator account.

1. Run the `aws organizations describe-organizational-unit`
   command to get your organization ARN.
2. Run the following command to create a view for the specified
   organizational unit.

```
`$` `aws resource-explorer-2 create-view \
 --region us-west-2 \
 --view-name entire-ou-view \
 --scope "arn:aws:organizations::222222222222:ou/o-exampleorgid/ou-exampleouid"``{
 "View": {
 "Filters": {
 "FilterString": ""
 },
 "IncludedProperties": [],
 "LastUpdatedAt": "2022-08-03T16:13:37.625000+00:00",
 "Owner": "222222222222",
 "Scope": "arn:aws:organizations::222222222222:ou/o-exampleorgid/ou-exampleouid",
 "ViewArn": "arn:aws:resource-explorer-2:us-west-2:222222222222:view/entire-ou-view/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111"
 }
}`
```

**Next step:** Grant the principals in your
account permissions to search with your new view. For more information, see
[Granting access to Resource Explorer views for
search](configure-views-grant-access.md "configure-views-grant-access.md")
