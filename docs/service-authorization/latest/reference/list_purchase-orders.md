

# Actions, resources, and condition keys for AWS Purchase Orders Console
<a name="list_purchase-orders"></a>

AWS Purchase Orders Console (service prefix: `purchase-orders`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/purchase-orders/purchase-orders.json) for this service.

**Topics**
+ [Actions defined by AWS Purchase Orders Console](#list_purchase-orders-actions-as-permissions)
+ [Permission-only actions for AWS Purchase Orders Console](#list_purchase-orders-permission-only-actions)
+ [Resource types defined by AWS Purchase Orders Console](#list_purchase-orders-resources-for-iam-policies)
+ [Condition keys for AWS Purchase Orders Console](#list_purchase-orders-policy-keys)

## Actions defined by AWS Purchase Orders Console
<a name="list_purchase-orders-actions-as-permissions"></a>

AWS Purchase Orders Console has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Purchase Orders Console
<a name="list_purchase-orders-permission-only-actions"></a>

The following actions are defined by AWS Purchase Orders Console but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AddPurchaseOrder](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to add a new purchase order
  - **Resource types (\*required):** [purchase-order\*](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_purchase-orders-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_purchase-orders-aws_TagKeys)
  - **Access level:** Write

- **   [DeletePurchaseOrder](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to delete a purchase order
  - **Resource types (\*required):** [purchase-order\*](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetConsoleActionSetEnforced](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view whether existing or fine-grained IAM actions are being used to control authorization to Billing, Cost Management, and Account consoles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPurchaseOrder](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to get a purchase order
  - **Resource types (\*required):** [purchase-order\*](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPurchaseOrderInvoices](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to list purchase order invoices
  - **Resource types (\*required):** [purchase-order\*](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPurchaseOrders](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to list all purchase orders for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to list tags for a purchase order
  - **Resource types (\*required):** [purchase-order](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ModifyPurchaseOrders](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to modify purchase orders and details
  - **Resource types (\*required):** [purchase-order\*](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_purchase-orders-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_purchase-orders-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to tag purchase orders with given key value pairs
  - **Resource types (\*required):** [purchase-order\*](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_purchase-orders-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_purchase-orders-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to remove tags from a purchase order
  - **Resource types (\*required):** [purchase-order\*](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_purchase-orders-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConsoleActionSetEnforced](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to change whether existing or fine-grained IAM actions will be used to control authorization to Billing, Cost Management, and Account consoles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePurchaseOrder](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to update an existing purchase order
  - **Resource types (\*required):** [purchase-order\*](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_purchase-orders-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_purchase-orders-aws_TagKeys)
  - **Access level:** Write

- **   [UpdatePurchaseOrderStatus](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to set purchase order status
  - **Resource types (\*required):** [purchase-order\*](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ViewPurchaseOrders](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view purchase orders and details
  - **Resource types (\*required):** [purchase-order](#list_purchase-orders-resource-purchase-order)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by AWS Purchase Orders Console
<a name="list_purchase-orders-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [purchase-order](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | arn:${Partition}:purchase-orders::${Account}:purchase-order/${ResourceName} | [aws:ResourceTag/${TagKey}](#list_purchase-orders-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Purchase Orders Console
<a name="list_purchase-orders-policy-keys"></a>

AWS Purchase Orders Console defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the set of tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 