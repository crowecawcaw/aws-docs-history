

# Actions, resources, and condition keys for AWS Marketplace Entitlement Service
<a name="list_marketplace-entitlement"></a>

AWS Marketplace Entitlement Service (service prefix: `aws-marketplace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/marketplace/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/marketplace/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/marketplace/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json) for this service.

**Topics**
+ [API operations defined by AWS Marketplace Entitlement Service](#list_marketplace-entitlement-operations)
+ [Actions defined by AWS Marketplace Entitlement Service](#list_marketplace-entitlement-actions-as-permissions)
+ [Resource types defined by AWS Marketplace Entitlement Service](#list_marketplace-entitlement-resources-for-iam-policies)
+ [Condition keys for AWS Marketplace Entitlement Service](#list_marketplace-entitlement-policy-keys)

## API operations defined by AWS Marketplace Entitlement Service
<a name="list_marketplace-entitlement-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_marketplace-entitlement-actions-as-permissions).




- **   GetEntitlements  **
  - **IAM action:**  [aws-marketplace:GetEntitlements](#list_marketplace-entitlement-action-GetEntitlements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Marketplace Entitlement Service
<a name="list_marketplace-entitlement-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetEntitlements](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-entitlements_GetEntitlements.html)  | Grants permission to retrieve entitlement values for a given product. The results can be filtered based on customer identifier or product dimensions |  |   | Read | 

## Resource types defined by AWS Marketplace Entitlement Service
<a name="list_marketplace-entitlement-resources-for-iam-policies"></a>

AWS Marketplace Entitlement Service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Marketplace Entitlement Service
<a name="list_marketplace-entitlement-policy-keys"></a>

AWS Marketplace Entitlement Service has no service-specific condition keys that can be used in the `Condition` element of policy statements.