AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Terms and concepts for Resource Explorer

AWS Resource Explorer is a resource search and discovery service. With Resource Explorer, you can explore your
resources by using an internet search engine-like experience. You can search for your
resources, such as Amazon Elastic Compute Cloud instances, Amazon Kinesis streams, or Amazon DynamoDB tables by using
resource metadata like names, tags, and IDs. Resource Explorer works across AWS Regions in your
account to simplify your cross-Region workloads.

Resource Explorer is available immediately when you have the appropriate permissions. Users with the
permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy can start searching
for resources right away without any setup. Users with both the permissions in the
`AWSResourceExplorerReadOnlyAccess` managed policy and the
`iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy) get complete search results with
automatic infrastructure creation (index and view) on first search in a Region. The
`iam:CreateServiceLinkedRole` permission is needed only by one user initially
to create the service-linked role for the account. After the service-linked role exists in
the account, all users with search permission searching in a new Region can create an index
and a view for full results.

Resource Explorer provides fast responses to your search queries by using indexes that are created
and maintained by the AWS Resource Explorer service. Resource Explorer uses a variety of data sources to gather
information about resources in your AWS account. Resource Explorer stores that information in the
indexes for Resource Explorer to search.

Resource Explorer operates in two modes: automatic setup and manual setup. With automatic setup,
Resource Explorer creates the necessary infrastructure (indexes and views) when you first search in a
Region, provided you have the required permissions. Manual setup allows administrators to
pre-configure Resource Explorer infrastructure before users begin searching.

You should understand the following concepts to successfully use AWS Resource Explorer .

###### Concepts

- [Resource Explorer administrator](#term-admin "#term-admin")
- [Resource Explorer user](#term-user "#term-user")
- [Index](#term-index "#term-index")
- [View](#term-view "#term-view")
- [Resource](#term-resource "#term-resource")
- [Unified Search in the AWS Management Console](#term-unified-search "#term-unified-search")
- [Multi-account search](#term-multi-account-search "#term-multi-account-search")
  The following diagram shows three AWS Regions in which users have searched for
  resources, and one Region where no search has occurred yet. Regions with
  user-owned
  (local) indexes provide complete search results, while Regions with only
  Resource Explorer owned indexes provide partial results (all tagged resources and supported untagged
  resources created after the [immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release).

In this example scenario, a user selected the US West (Oregon) Region
(`us-west-2`) to contain the aggregator index for the account. All Regions
with user-owned (local)
indexes replicate their local indexes to the Region with the
aggregator index.

The default view created by Resource Explorer doesn't have any filters. Therefore, results from
searching with this view can include resources of any type in all Regions in the account
where Resource Explorer is turned on including Tags.

![4 Regions: Resource Explorer registered in 3. Default view, aggregator index, or AWS account in 1.](/images/resource-explorer/latest/userguide/images/AREX-Overview-IAD.png)

|                                                                                        |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Legend**                                                                             |
| Gear icon with magnifying glass, representing system configuration or search settings. | Resource Explorer<br>is set up with a user-owned (local) index in this<br>AWS Region.<br>Information<br>about the Region's resources is stored in a local index in that Region.<br>Every Region's<br>user-owned<br>(local) index is also replicated (indicated by the arrows)<br>to the Region that contains the aggregator index.                                                                |
| Notebook icon representing a document or file with lined pages.                        | The index in this AWS Region is configured to be the aggregator index<br>for the account. Resource Explorer replicates the resource information collected in the<br>user-owned<br>(local) indexes of all other Regions<br>into<br>the aggregator index in this Region. Searches made in this<br>Region can include results from all Regions<br>with<br>user-owned (local) indexes in the account. |
| Blue square border with white interior, representing a placeholder for an image.       | The default view created by \*_Quick Setup_<br>• includes all<br>resources in all<br>AWS Regions<br>with user-owned (local) indexes.                                                                                                                                                                                                                                                              |

## Resource Explorer administrator

A Resource Explorer _administrator_ is an AWS Identity and Access Management (IAM)
principal who has the permission to manage Resource Explorer and its settings in the
AWS account. With Resource Explorer functionality available
in an account by default, manual administrator setup is optional for basic
functionality. Users with appropriate permissions can start searching immediately and
Resource Explorer will automatically create the necessary infrastructure. The Resource Explorer administrator
can configure the following features:

- Complete setup for individual AWS Regions in the AWS account by creating
  user-owned indexes in those Regions by searching or in
  **Settings**. This provides complete search results and
  lets Resource Explorer discover all resources and populate the index with comprehensive
  information about those resources.
- Enable cross-Region search by updating the index type in one AWS Region to
  make it the [aggregator index](#term-index "#term-index") for its
  AWS account.. The aggregator index in this Region receives replicated copies
  of the resource information from all other Regions in the account where
  user-owned indexes exist.
- Create [views](#term-view "#term-view") that define the subset of
  indexed information users can search and discover in Resource Explorer.
- While not part of the Resource Explorer actions, the Resource Explorer administrator must also be
  able to grant search permissions to the principals in the account. The
  administrator can grant these permissions to principals by adding the relevant
  permissions to existing IAM permission policies, or by using the [Resource Explorer read only
  AWS managed policy](security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess "security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess").

To provide access, add permissions to your users, groups, or roles:

    + Users and groups in AWS IAM Identity Center:


    Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the *AWS IAM Identity Center User Guide*.
    + Users managed in IAM through an identity provider:


    Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
     in the *IAM User Guide*.
    + IAM users:




    	- Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
    	- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

The administrator typically has all Resource Explorer permissions
(`resource-explorer-2:*`) on all Resource Explorer resources, including the indexes
and views. These permissions can be granted by using the [Resource Explorer full access AWS
managed policy](security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerFullAccess "security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerFullAccess").

## Resource Explorer user

Resource Explorer provides three permission-based experience tiers for users:

**Full Experience**

**Permissions:** At minimum, the permissions
in the `AWSResourceExplorerReadOnlyAccess` managed policy. If
the service-linked role doesn't exist in the account, one user needs the
`iam:CreateServiceLinkedRole` permission (included in the
[AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy) to create it
initially

**Experience:** Complete single-Region
resource search results with automatic updates

**Enhancement:** Can optionally enable
cross-Region search by selecting an aggregator index

**Enhanced Experience**

**Permissions:** At minimum, the permissions
in the `AWSResourceExplorerReadOnlyAccess` managed
policy

**Experience:** Partial results immediately
(all tagged resources and supported untagged resources created after the
[immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release)

**Enhancement:**
Can upgrade to full experience by obtaining service-linked
role creation permission or having another user with permissions create the
service-linked role in the account

**No Access**

**Permissions:** Missing the permissions in
the `AWSResourceExplorerReadOnlyAccess` managed
policy

**Experience:** No resource search
access

**Enhancement:** Must obtain proper
permissions to access the service

A Resource Explorer _user_ is an IAM principal that has
permission to do one or more of the following tasks:

- Perform a search for resources by using a view to query Resource Explorer. A Resource Explorer user
  wants to discover and find AWS resources and typically uses the Resource Explorer
  console, or the Resource Explorer `Search` operations provided by the AWS SDKs
  or the AWS CLI.

A role or user can get IAM get permission to search with one of two
methods:

    + The [Resource Explorer read only AWS managed policy](security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess "security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess") to the IAM role,
     group, or user.
    + An IAM permission policy with a statement containing the following
     minimum permissions to the IAM role, group, or user.



    ```
    {
        "Effect": "Allow",
        "Action": [
            "resource-explorer-2:Search",
            "resource-explorer-2:GetView",
        "Resource": "`*`"
    }
    ```

- Although typically considered an administrator task, you can delegate to
  trusted users the ability to define create views. To do this, the administrator
  can grant permission to call the `resource-explorer-2:CreateView`
  operation in an IAM permission policy attached to the relevant roles, groups,
  or users. If the view requires specific permissions, then provision for adding
  or modifying the IAM policies for the relevant users must be made.

For information about how to search for resources using Resource Explorer, see [Using AWS Resource Explorer to search for resources](using-search.md "using-search.md").

## Index

An _index_ is the collection of information
maintained by Resource Explorer about all of the AWS resources in one AWS Region in your
AWS account. Resource Explorer updates the index automatically as you create and delete resources
in your AWS account. In the earlier diagram, the boxes under the AWS Region names
represent the Resource Explorer indexes maintained in each AWS Region. The index in a Region is
the source of information for any views created in that Region. Users can't directly
query the index. Instead, they must always query using a view.

There are three types of indexes:

**Resource Explorer-owned
index**

A _Resource Explorer owned index_ exists in every
AWS Region and is managed by the Resource Explorer service. These indexes cannot be
deleted or modified by users. Resource Explorer owned indexes provide partial search
results, including all tagged resources and supported untagged resources
created after the [immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release. Users with only the
permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy
access resources through these indexes.

**User-owned (local) index**

There is one _user-owned (local) index_
in every AWS Region in which you complete setup for Resource Explorer. A user-owned
index contains complete information about all resources in the same Region
and provides full search results.

**Aggregator index**

The Resource Explorer administrator can also designate the index in one AWS Region
to be the _aggregator index_ for the
AWS account. The aggregator index receives and stores a copy of the index
for every other Region where user-owned indexes exist in the account. The
aggregator index also receives and stores information about the resources in
its own Region. In the earlier diagram, the Region `us-west-2`
contains the aggregator index for the account. The primary reason to
designate an aggregator index for the account is so that you can create views
that can include resources from all Regions in the account. Using an
aggregator index is optional but recommended for cross-region search
capabilities. There can be **_only one_** aggregator index in an
AWS account.

When you complete setup for Resource Explorer, you can specify which AWS Region
contains the aggregator index. You can also change the
AWS Region used for the aggregator index later. For information about how
to promote a local index to make it the aggregator index for its
AWS account, see [Enabling cross-Region search by creating an
aggregator index](manage-aggregator-region.md "manage-aggregator-region.md").

After the service-linked role has been created in the account (created by a user with
the `iam:CreateServiceLinkedRole` permission, which is included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy), automatic index creation
occurs when users with, at minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy perform their
first search in a Region that doesn't have a user-index set up already. If the
service-linked role doesn't exist in the account, the user needs the
`iam:CreateServiceLinkedRole` permission to create it. After the
service-linked role exists in the account, any user with, at minimum, the permissions in
the `AWSResourceExplorerReadOnlyAccess` managed policy can trigger
automatic index creation for complete search results.

An index is a resource with an [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md"). However, you can use this ARN only in
permission policies to grant access to operations that interact directly with the index.
With those operations, you can create views and set them as the default in a Region,
enable or disable Resource Explorer in a Region, and create an aggregator index for the account.
The ARN of an index looks similar to the following example:

```
arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111
```

## View

A _view_ is the mechanism used to query the resources
listed in an index. The view defines what information in the index is visible and
available for search and discovery purposes. A user never directly queries the Resource Explorer
index. Instead, queries must always go through a view which lets the view creator limit
which resources the user can see in search results.

For more information about views in Resource Explorer, see [Working with views](views.md "views.md").

## Resource

A _resource_ is an entity in AWS that you can work
with. Resources are created by AWS services as you use the features of the service.
Examples include an Amazon EC2 instance, an Amazon S3 bucket, or an AWS CloudFormation stack. Some resource
types can contain customer data. All resource types have attributes or metadata to
describe the resource, including a name, description, and the [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") that you
use to uniquely reference a resource. Most [resource types also support tags](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md").
Tags are custom metadata that you can attach to your resources for a variety of
purposes, such as [cost allocation in your
billing](../../../awsaccountbilling/latest/aboutv2/aws-tags.md "../../../awsaccountbilling/latest/aboutv2/aws-tags.md"), [security authorization using
attribute-based access control](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md"), or to support your other categorization
needs.

The primary purpose of Resource Explorer is to help you find the resources that exist in your
AWS account. Resource Explorer uses a variety of techniques to discover all of your resources and
place information about them in an [index](#term-index "#term-index"). Then, you
can query the index through whatever [views](#term-view "#term-view") that your
administrator makes available to you.

###### Important

Resource Explorer excludes intentionally those resources types whose inclusion would expose
customer data. The following resource types are **_not_** indexed by Resource Explorer and are therefore
never returned in search results.

- Amazon S3 objects that are contained _within_
  a bucket
- Amazon DynamoDB table items
- DynamoDB attribute values

## Unified Search in the AWS Management Console

At the top of the AWS Management Console, in every AWS service, there is a search bar that you
can use to search for a variety of AWS related things. You can search for services and
features, and get links directly to the relevant page in that service's console. You can
also search for documentation and blog articles related to your search term.

[Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md") automatically uses the default view in the AWS Region that
contains the aggregator index for the account or the default or service view per Region.
This lets you search for a resource from any page in the AWS Management Console, without having to
first open Resource Explorer.

###### Important

Unified Search automatically inserts a wildcard character (`*`) operator at the
end of the first keyword in the string. This means that unified search results include resources
that match any string that starts with the specified keyword.

The search performed by the **Query** text box on the [Resource search](https://console.aws.amazon.com/resource-explorer/home#/explorer "https://console.aws.amazon.com/resource-explorer/home#/explorer") page in the
Resource Explorer console does **_not_**
automatically append a wildcard character. You can insert a `*` manually after
any term in the search string.

For more information about Unified Search and its integration with Resource Explorer, see [Using Unified Search in the AWS Management Console](using-unified-search.md "using-unified-search.md").

## Multi-account search

With multi-account search, you can search and discover resources across AWS Organizations and
AWS Regions with a single keyword search.

For more information about multi-account search and how to enable it for Resource Explorer, see
[Turning on multi-account search](manage-service-multi-account.md "manage-service-multi-account.md").
