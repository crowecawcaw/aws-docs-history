

# Actions, resources, and condition keys for AWS Migration Acceleration Program Credits
<a name="list_mapcredits"></a>

AWS Migration Acceleration Program Credits (service prefix: `mapcredits`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mapcredits/mapcredits.json) for this service.

**Topics**
+ [Actions defined by AWS Migration Acceleration Program Credits](#list_mapcredits-actions-as-permissions)
+ [Permission-only actions for AWS Migration Acceleration Program Credits](#list_mapcredits-permission-only-actions)
+ [Resource types defined by AWS Migration Acceleration Program Credits](#list_mapcredits-resources-for-iam-policies)
+ [Condition keys for AWS Migration Acceleration Program Credits](#list_mapcredits-policy-keys)

## Actions defined by AWS Migration Acceleration Program Credits
<a name="list_mapcredits-actions-as-permissions"></a>

AWS Migration Acceleration Program Credits has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Migration Acceleration Program Credits
<a name="list_mapcredits-permission-only-actions"></a>

The following actions are defined by AWS Migration Acceleration Program Credits but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [ListAssociatedPrograms](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  **
  - **Description:** Grants permission to view the user's associated Migration Acceleration Program agreements
  - **Resource types (\*required):** [agreement\*](#list_mapcredits-resource-agreement)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListQuarterCredits](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  **
  - **Description:** Grants permission to view Migration Acceleration Program agreements credits associated with the user's payer account
  - **Resource types (\*required):** [agreement\*](#list_mapcredits-resource-agreement)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListQuarterSpend](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  **
  - **Description:** Grants permission to view Migration Acceleration Program agreements eligible spend associated with the user's payer account
  - **Resource types (\*required):** [agreement\*](#list_mapcredits-resource-agreement)
  - **Condition keys:**  
  - **Access level:** List



## Resource types defined by AWS Migration Acceleration Program Credits
<a name="list_mapcredits-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [agreement](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | arn:${Partition}:mapcredits:::${Agreement}/${AgreementId} |   | 

## Condition keys for AWS Migration Acceleration Program Credits
<a name="list_mapcredits-policy-keys"></a>

AWS Migration Acceleration Program Credits has no service-specific condition keys that can be used in the `Condition` element of policy statements.