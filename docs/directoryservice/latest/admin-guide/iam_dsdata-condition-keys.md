# Directory Service Data condition keys

Use [Directory Service Data](../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/welcome.md "../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/welcome.md") condition keys to add specific statements to users and group level
access. This allows users to decide which principals can perform actions on what resources
and under what conditions.

The _Condition element_, or _Condition block_, lets you specify conditions where a statement is in effect.
The Condition element is optional. You can create conditional expressions that use condition
operators, such as equals (=) or less than (<), to match the condition in the policy with
values in the request.

If you specify multiple Condition elements in a statement, or multiple keys in a single
Condition element, AWS evaluates them by using a logical AND operation. If you specify
multiple values for a single condition key, AWS evaluates the condition by using a logical
OR operation. All of the conditions must be met before the statement's permissions are
granted. You can also use placeholder variables when you specify conditions. For example,
you can grant an IAM user permission to access a resource only if it's tagged with their
username. For information, see [Condition with
multiple keys or values](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md") in the _IAM User Guide_.

For a list of which actions support these condition keys, see [Actions
defined by AWS Directory Service Data](../../../service-authorization/latest/reference/list_directoryservice-data.md "../../../service-authorization/latest/reference/list_directoryservice-data.md") in the _Service Authorization
Reference_.

###### Note

For information about tag-based resource-level permissions, see [Using tags with IAM
policies](IAM_Auth_Access_IdentityBased.md#using_tags_with_iam_policies "IAM_Auth_Access_IdentityBased.md#using_tags_with_iam_policies").

## ds-data:SAMAccountName

Works with [String operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String").

Use this key to explicitly allow or deny an IAM role from performing actions on
specific users and groups.

###### Important

When using `SAMAccountName` or `MemberName`, we recommend
specifying `ds-data:Identifier` as `SAMAccountName`. This
prevents future identifiers that AWS Directory Service Data supports, such as `SID`, from
breaking existing permissions.

The following policy denies the IAM principal from describing the user
`joe` or describing the group `joegroup`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyDescribe",
 "Effect": "Deny",
 "Action": "ds-data:Describe*",
 "Resource": "*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "ds-data:SAMAccountName": [
 "`joe`",
 "`joegroup`"
 ],
 "ds-data:identifier": [
 "SAMAccountName"
 ]
 }
 }
 }
 ]
}`

```

###### Note

This condition key case insensitive. You must use `StringEqualsIgnoreCase` or `StringNotEqualsIgnoreCase` condition operators to compare
string values regardless of letter cases.

## ds-data:Identifier

Works with [String operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String").

Use this key to define which identifier to use in the IAM policy permissions.
Currently, only `SAMAccountName` is supported.

The following policy allows the IAM principal to update the user
`joe`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "UpdateJoe",
 "Effect": "Allow",
 "Action": "ds-data:UpdateUser",
 "Resource": "arn:aws:ds:`us-east-1`:`111122223333`:directory/`d-012345678`",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "ds-data:SAMAccountName": [
 "`joe`"
 ],
 "ds-data:identifier": [
 "SAMAccountName"
 ]
 }
 }
 }
 ]
}`

```

## ds-data:MemberName

Works with [String operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String").

Use this key to define the members that can have operations performed on them.

###### Important

When using `MemberName` or `SAMAccountName`, we recommend
specifying `ds-data:Identifier` as `SAMAccountName`. This
prevents future identifiers that Directory Service Data supports, such as `SID`, from
breaking existing permissions.

The following policy allows the IAM principal to perform `AddGroupMember`
on member `joe` in any group.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AddJoe",
 "Effect": "Allow",
 "Action": "ds-data:AddGroupMember",
 "Resource": "arn:aws:ds:`us-east-1`:`111122223333`:directory/`d-012345678`",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "ds-data:MemberName": "`joe`"
 }
 }
 }
 ]
}`

```

###### Note

This condition key is case insensitive. You must use `StringEqualsIgnoreCase` or `StringNotEqualsIgnoreCase` condition operators to compare
string values, regardless of letter cases.

## ds-data:MemberRealm

Works with [String operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String").

Use this key to check whether the `ds-data:MemberRealm` value in the policy
matches the member realm in the request.

###### Note

This condition key is case insensitive. You must use `StringEqualsIgnoreCase` or `StringNotEqualsIgnoreCase` condition operators to compare
string values, regardless of letter cases.

The following policy allows the IAM principal to call `AddGroupMember`
for member `bob` in realm `ONE.TRU1.AMAZON.COM`.

###### Note

The following example uses only the `ds-data:MemberName` context key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "addbob",
 "Effect": "Allow",
 "Action": "ds-data:AddGroupMember",
 "Resource": "arn:aws:ds:`us-east-1`:`111122223333`:directory/`d-012345678`",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "ds-data:MemberName": "`bob`",
 "ds-data:MemberRealm": "`one.tru1.amazon.com`"
 }
 }
 }
 ]
}`

```

## ds-data:Realm

Works with [String operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String").

Use this key to check whether the `ds-data:Realm` value in the policy
matches the realm an IAM principal can use to make requests to Directory Service Data APIs.

###### Note

This condition key is case insensitive. You must use `StringEqualsIgnoreCase` or `StringNotEqualsIgnoreCase` condition operators to compare
string values regardless of letter cases.

The following policy denies the IAM principal from calling `ListUsers` on
the realm `one.tru1.amazon.com`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyTrustedList",
 "Effect": "Deny",
 "Action": "ds-data:ListUsers",
 "Resource": "*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "ds-data:Realm": [
 "`one.tru1.amazon.com`"
 ]
 }
 }
 }
 ]
}`

```
