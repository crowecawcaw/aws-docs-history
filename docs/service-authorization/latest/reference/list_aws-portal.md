

# Actions, resources, and condition keys for AWS Billing Console
<a name="list_aws-portal"></a>

AWS Billing Console (service prefix: `aws-portal`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-portal/aws-portal.json) for this service.

**Topics**
+ [Actions defined by AWS Billing Console](#list_aws-portal-actions-as-permissions)
+ [Permission-only actions for AWS Billing Console](#list_aws-portal-permission-only-actions)
+ [Resource types defined by AWS Billing Console](#list_aws-portal-resources-for-iam-policies)
+ [Condition keys for AWS Billing Console](#list_aws-portal-policy-keys)

## Actions defined by AWS Billing Console
<a name="list_aws-portal-actions-as-permissions"></a>

AWS Billing Console has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Billing Console
<a name="list_aws-portal-permission-only-actions"></a>

The following actions are defined by AWS Billing Console but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetConsoleActionSetEnforced](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | Grants permission to view whether existing or fine-grained IAM actions are being used to control authorization to Billing, Cost Management, and Account consoles |  |   | Read | 
|   [ModifyAccount](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | Allow or deny IAM users permission to modify Account Settings |  |   | Write | 
|   [ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | Allow or deny IAM users permission to modify billing settings |  |   | Write | 
|   [ModifyPaymentMethods](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | Allow or deny IAM users permission to modify payment methods |  |   | Write | 
|   [UpdateConsoleActionSetEnforced](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | Grants permission to change whether existing or fine-grained IAM actions will be used to control authorization to Billing, Cost Management, and Account consoles |  |   | Write | 
|   [ViewAccount](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | Allow or deny IAM users permission to view account settings |  |   | Read | 
|   [ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | Allow or deny IAM users permission to view billing pages in the console |  |   | Read | 
|   [ViewPaymentMethods](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | Allow or deny IAM users permission to view payment methods |  |   | Read | 
|   [ViewUsage](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | Allow or deny IAM users permission to view AWS usage reports |  |   | Read | 

## Resource types defined by AWS Billing Console
<a name="list_aws-portal-resources-for-iam-policies"></a>

AWS Billing Console does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Billing Console
<a name="list_aws-portal-policy-keys"></a>

AWS Billing Console has no service-specific condition keys that can be used in the `Condition` element of policy statements.