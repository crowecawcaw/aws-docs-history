# Controlling cost management data access with Billing View

Billing View is a feature that helps you manage and control access to cost management data
within your AWS environment. With Billing View, cost management data is represented as an AWS
resource. Through resource-based policies, you can configure what data is accessible to an account
when using AWS Billing and Cost Management tools. A billing view is identified by a unique
Amazon Resource Name (ARN), which can be referenced in identity-based policies to perform specific
IAM actions on the cost management data contained in that billing view.

There are three different types of billing views:

| Type                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Managed by | Shareable?                                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------ |
| Primary billing view       | By default, each account has access to its primary billing view, which contains all the<br>cost management data associated with that account. For the management account of an<br>organization, this includes all cost management data incurred by all accounts within the<br>organization. For standalone AWS accounts not using AWS Organizations, as well as for<br>member accounts within an organization, the primary billing view contains all cost management<br>data incurred within the individual account. | AWS        | Not shareable with other accounts                            |
| Billing group billing view | Accounts that have enabled AWS Billing Conductor also have access to billing group<br>billing views, which correspond to each billing group. For more information about billing<br>groups, see [Billing groups](../../../billingconductor/latest/userguide/creating-abc.md "../../../billingconductor/latest/userguide/creating-abc.md") in the _AWS Billing Conductor User<br>Guide_.                                                                                                                               | AWS        | Not shareable with other accounts                            |
| Custom billing view        | Customers can create and delete custom billing views that provide cost visibility across<br>organizations. These billing views can be derived from primary billing views or other custom<br>billing views, and combines cost management data from multiple accounts belonging to multiple<br>organizations. Apply filters to specify which subset of cross-organizational data to include<br>in your view.                                                                                                           | Customer   | Shareable with accounts within and outside your organization |

Billing View allows you to create custom billing views from your organization’s management
(payer) account, which you can define to include a set of filtered cost management data you have
access to. A custom billing view resource can then be shared with other accounts. When a custom billing view is shared with an account, that account can then access
the cost management data defined in the custom billing view.

You can use custom billing views to grant end users and application owners access to relevant
cost management data without requiring access to the management account. Customers with AWS
Organizations enabled can create custom billing views containing a subset of cost management data
from the management account's primary billing view, filtered by cost allocation tags or
accounts. You can also combine cost management data from multiple organizations into a single custom billing view.

Key benefits of using custom billing views include:

- **Streamlined access**: Enable business unit owners who manage
  multiple member accounts to access all of their cost management data without needing to access
  each account individually, saving end users time and eliminating the need for manual data
  aggregation.
- **Consolidated data:** Consolidate cost management data across
  multiple organizations. Enable central teams to have consolidated views of their cost management
  data across multiple organizations.
- **Reduced management account access**: Eliminate the need for
  end users to access the management account of your organization to access cost management data
  spanning multiple accounts.
- **Native AWS Cost Management access**: Empower end users
  across your organization to independently visualize, understand, and forecast their AWS spend
  using Cost Explorer and the AWS Billing and Cost Management home page.
  By sharing custom billing views with other accounts, application owners can monitor their
  application-level AWS spend using Cost Explorer and AWS Budgets, and central teams can
  monitor their spend across multiple organizations. This eliminates the need for central teams to
  manually aggregate information across multiple organizations, and the need for end users to access
  the management account to access cost management data. The following sections guide you through
  the process of creating, sharing, managing, and using custom billing views.

###### Topics

- [Getting started with custom billing views](billing-view-getting-started.md "billing-view-getting-started.md")
- [Creating custom billing views](create-custom-billing-views.md "create-custom-billing-views.md")
- [Sharing custom billing views](share-custom-billing-views.md "share-custom-billing-views.md")
- [Managing custom billing views](manage-custom-billing-views.md "manage-custom-billing-views.md")
- [Accessing cost management data using custom
  billing views](access-data-custom-billing-views.md "access-data-custom-billing-views.md")
