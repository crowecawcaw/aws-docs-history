# Using cost categories with

other cost management and optimization services

You can use AWS Cost Categories to associate cost categories with specific
resources. This allows you to use cost categories as a grouping mechanism in other
cost management and optimization products. When you associate resources with a
, you create a bidirectional relationship. Meaning, the
is used as a grouping mechanism by the associated resource, and when
the rules are updated, the changes are reflected in the associated
resources and corresponding cost management optimization services.

## Setting up resource

associations

Resource associations must be configured through the supporting cost management
and optimization product console. Association can only be made if dimensions used in
cost categories rules are supported by the cost management and optimization
product.

## Managing resource

associated cost categories

Managing resource-associated cost categories works similarly as managing
regular cost categories. However, some functionalities can be limited due to the
lack of support by the associated resources.

## Creating and editing

associated cost categories

Create or edit associated cost categories by creating rules
using supported dimensions.

## Viewing associated

cost categories

You can view all of the resources associated to your . You have
visibility into where and how cost categories are utilized as a grouping
mechanism across services in the Billing and Cost Management console.

###### To view your cost category

associated resources

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose
   **Cost categories**.
3. In the table, choose the **Associated features** tab.

## Deleting associated

cost categories

You can't delete cost categories with associated resources directly. The
association must be removed before you can delete the cost category.
