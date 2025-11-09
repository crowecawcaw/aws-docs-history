# Actions, resources, and condition keys for AWS Migration Acceleration Program Credits

AWS Migration Acceleration Program Credits (service prefix: `mapcredits`) provides the following service-specific resources, actions, and condition context keys for use in IAM permission policies.

References:

- Learn how to [configure this service](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").
- View a list of the [API operations available for this service](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md").
- Learn how to secure this service and its resources by [using IAM](../../../awsaccountbilling/latest/aboutv2/security-iam.md "../../../awsaccountbilling/latest/aboutv2/security-iam.md") permission policies.

###### Topics

- [Actions defined by AWS Migration Acceleration Program Credits](#awsmigrationaccelerationprogramcredits-actions-as-permissions "#awsmigrationaccelerationprogramcredits-actions-as-permissions")
- [Resource types defined by AWS Migration Acceleration Program Credits](#awsmigrationaccelerationprogramcredits-resources-for-iam-policies "#awsmigrationaccelerationprogramcredits-resources-for-iam-policies")
- [Condition keys for AWS Migration Acceleration Program Credits](#awsmigrationaccelerationprogramcredits-policy-keys "#awsmigrationaccelerationprogramcredits-policy-keys")

## Actions defined by AWS Migration Acceleration Program Credits

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.

The **Access level** column of the Actions table describes how the action is classified (List, Read, Permissions management, or Tagging). This classification can help you understand the level of access that an action grants when you use it in a policy. For more information about access levels, see [Access levels in policy summaries](../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md "../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md").

The **Resource types** column of the Actions table indicates whether each action supports resource-level permissions. If there is no value for this column, you must specify all resources ("\*") to which the policy applies in the `Resource` element of your policy statement. If the column includes a resource type, then you can specify an ARN of that type in a statement with that action. If the action has one or more required resources, the caller must have permission to use the action with those resources. Required resources are indicated in the table with an asterisk (\*). If you limit resource access with the `Resource` element in an IAM policy, you must include an ARN or pattern for each required resource type. Some actions support multiple resource types. If the resource type is optional (not indicated as required), then you can choose to use one of the optional resource types.

The **Condition keys** column of the Actions table includes keys that you can specify in a policy statement's `Condition` element. For more information on the condition keys that are associated with resources for the service, see the **Condition keys** column of the Resource types table.

The **Dependent actions** column of the Actions table shows additional permissions that may be required to successfully call an action. These permissions may be needed in addition to the permission for the action itself. When an action specifies dependent actions, those dependencies may apply to additional resources defined for that action, not only the first resource listed in the table.

###### Note

Resource condition keys are listed in the [Resource types](#awsmigrationaccelerationprogramcredits-resources-for-iam-policies "#awsmigrationaccelerationprogramcredits-resources-for-iam-policies") table. You can find a link to the resource type that applies to an action in the **Resource types (\*required)** column of the Actions table. The resource type in the Resource types table includes the **Condition keys** column, which are the resource condition keys that apply to an action in the Actions table.

For details about the columns in the following table, see [Actions table](reference_policies_actions-resources-contextkeys.md#actions_table "reference_policies_actions-resources-contextkeys.md#actions_table").

| Actions                                                                                                                                                                                 | Description                                                                                                                 | Access level | Resource types (\*required)                                                                                          | Condition keys | Dependent actions |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------- |
| [ListAssociatedPrograms](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md") [permission only] | Grants permission to view the user's associated Migration Acceleration Program agreements                                   | List         | [agreement\*](#awsmigrationaccelerationprogramcredits-agreement "#awsmigrationaccelerationprogramcredits-agreement") |                |                   |
| [ListQuarterCredits](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md") [permission only]     | Grants permission to view Migration Acceleration Program agreements credits associated with the user's payer account        | List         | [agreement\*](#awsmigrationaccelerationprogramcredits-agreement "#awsmigrationaccelerationprogramcredits-agreement") |                |                   |
| [ListQuarterSpend](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md") [permission only]       | Grants permission to view Migration Acceleration Program agreements eligible spend associated with the user's payer account | List         | [agreement\*](#awsmigrationaccelerationprogramcredits-agreement "#awsmigrationaccelerationprogramcredits-agreement") |                |                   |

## Resource types defined by AWS Migration Acceleration Program Credits

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements. Each action in the [Actions table](#awsmigrationaccelerationprogramcredits-actions-as-permissions "#awsmigrationaccelerationprogramcredits-actions-as-permissions") identifies the resource types that can be specified with that action. A resource type can also define which condition keys you can include in a policy. These keys are displayed in the last column of the Resource types table. For details about the columns in the following table, see [Resource types table](reference_policies_actions-resources-contextkeys.md#resources_table "reference_policies_actions-resources-contextkeys.md#resources_table").

| Resource types                                                                                                                                           | ARN                                                         | Condition keys |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------------- |
| [agreement](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md") | `arn:${Partition}:mapcredits:::${Agreement}/${AgreementId}` |                |

## Condition keys for AWS Migration Acceleration Program Credits

MapCredits has no service-specific context keys that can be used in the `Condition` element of policy statements. For the list of the global context keys that are available to all services, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").
