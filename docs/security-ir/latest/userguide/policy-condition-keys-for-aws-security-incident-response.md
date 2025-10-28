# Policy condition keys for AWS

Security Incident Response

**Supports service-specific policy
condition keys:** No

Administrators can use AWS JSON policies to specify who has
access to what. That is, which
**principal** can perform
**actions** on what
**resources**, and under what
**conditions**.

The Condition element (or Condition
_block_) lets you specify conditions in
which a statement is in effect. The Condition element is
optional. You can create conditional expressions that use
[condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the
condition in the policy with values in the request.

If you specify multiple Condition elements in a statement, or
multiple keys in a single Condition element, AWS evaluates
them using a logical AND operation. If you specify multiple
values for a single condition key, AWS evaluates the condition
using a logical OR operation. All of the conditions must be
met before the statement's permissions are granted.

You can also use placeholder variables when you specify
conditions. For example, you can grant an IAM user permission
to access a resource only if it is tagged with their IAM user
name. For more information, see
[IAM
policy elements: variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the
_IAM User Guide_.

AWS supports global condition keys and service-specific
condition keys. To see all AWS global condition keys, see
[AWS
global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User
Guide_.
