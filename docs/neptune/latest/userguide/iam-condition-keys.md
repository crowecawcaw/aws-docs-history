# Customizing access to Amazon Neptune resources using IAM condition context keys

You can specify conditions in IAM policies that control access to Neptune
management actions and resources. The policy statement then takes effect only when
the conditions are true.

For example, you might want a policy statement to take effect only after a
specific date, or allow access only when a specific value is present in the API
request.

To express conditions, you use predefined condition keys in the [`Condition`](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md")
element of a policy statement, together with [IAM
condition policy operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") such as equals or less than.

If you specify multiple `Condition` elements in a statement, or
multiple keys in a single `Condition` element, AWS evaluates them using
a logical `AND` operation. If you specify multiple values for a single
condition key, AWS evaluates the condition using a logical `OR`
operation. All of the conditions must be met before the statement's permissions are
granted.

You can also use placeholder variables when you specify conditions. For example,
you can grant an IAM user permission to access a resource only if it is tagged with
their IAM user name. For more information, see [IAM Policy Elements:
Variables and Tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User Guide_.

The data type of a condition key determines which condition operators you can
use to compare values in the request with the values in the policy statement.
If you use a condition operator that is not compatible with that data type, the
match always fails and the policy statement never applies.

###### IAM condition keys for Neptune administrative policy statements

- [Global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")   –  
  You can use most AWS global condition keys in Neptune administrative policy
  statements.
- [Service-specific condition keys](iam-admin-condition-keys.md "iam-admin-condition-keys.md")   –  
  These are keys that are defined for specific AWS services. The ones that Neptune
  supports for administrative policy statements are listed in [IAM condition keys for administering Amazon Neptune](iam-admin-condition-keys.md "iam-admin-condition-keys.md").

###### IAM condition keys for Neptune data-access policy statements

- [Global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")   –  
  The subset of these keys that Neptune supports in data-access policy statements is listed in
  [AWS global condition context keys supported by Neptune in data-access policy statements](iam-data-condition-keys.md#iam-data-global-condition-keys "iam-data-condition-keys.md#iam-data-global-condition-keys").
- Service-specific condition keys that Neptune defines for data-access policy statements
  are listed in [Condition Keys](iam-data-condition-keys.md "iam-data-condition-keys.md").
