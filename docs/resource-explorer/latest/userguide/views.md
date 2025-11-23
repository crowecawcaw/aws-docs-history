# Working with views

A _view_ is the mechanism used to query the resources
listed in an index. The view defines what information in the index is visible and available
for search and discovery purposes. A user never directly queries the Resource Explorer index. Instead,
queries must always go through a view which lets the view creator limit which resources the
user can see in search results.

## Granting access to a view

Resource Explorer provides three types of views: User views, AWS managed views, and AWS
service views.

**User views**

User views are created and managed by users or administrators. When
automatic setup occurs, Resource Explorer creates user-owned default views that include
tags for comprehensive filtering capabilities.

**AWS service views**

A [service view](aws-service-views.md "aws-service-views.md") is a pre-defined
view owned and managed by AWS services (not customer accounts) in
AWS Resource Explorer that enables controlled access to resource data.

###### Note

A Resource Explorer-owned view is a type of service view that acts as a fallback
when no user-owned default view exists in a Region. These views cannot
be modified or deleted by users and provide basic search functionality
through Resource Explorer-owned indexes.

**AWS managed views**

A [managed view](aws-managed-views.md "aws-managed-views.md") provides other
AWS services with the ability to access resource information indexed by
Resource Explorer for your AWS account or organization with your consent.

Views are stored on a per-Region basis. A view can access only the Resource Explorer index in
that AWS Region. To access account-wide search results, you must use a view in the
Region that contains the _aggregator index_ for the account. The
**Quick setup** option creates a default view in the AWS Region
with the aggregator index and with filters that include all resources in all
AWS Regions used by the account.

For information about how to create views, see [Configuring a Resource Explorer view to provide access to
resource searches](customer-views.md#configure-views "customer-views.md#configure-views"). For information about how to use views in a
query, see [Using AWS Resource Explorer to search for resources](using-search.md "using-search.md").

Every view has an [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") that you can reference in permission policies to
grant access to individual views. You can also pass a view's ARN as a parameter to any
API or AWS CLI operation that interacts with a view. The ARN of a view looks similar to
the following example.

```
arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View-Name/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111
```

###### Note

Every view ARN includes an AWS generated UUID at the end. This helps to ensure
that users who might have had access to views with a specific name that was deleted
can't automatically access a new view created with the same name.

## Comparison of view types

The following table compares the different types of views available in Resource Explorer:

| Feature                            | User Views | Managed Views             | Service Views        |
| ---------------------------------- | ---------- | ------------------------- | -------------------- |
| Created by                         | User       | AWS Service (per account) | AWS Service (global) |
| Can user modify                    | Yes        | No                        | No                   |
| Can user delete                    | Yes        | Via service only          | No                   |
| Requires user setup                | Yes        | Service manages           | No                   |
| Access to config/relationship data | No         | Yes                       | Yes                  |
| Streaming support                  | No         | No                        | Yes                  |
