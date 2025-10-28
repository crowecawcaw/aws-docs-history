# Single-valued vs. multivalued context keys

The difference between single-valued and multivalued context keys lies in the number of
values in the [request context](intro-structure.md#intro-structure-request "intro-structure.md#intro-structure-request"), not the number
of values in the policy condition.

- _Single-valued_ condition context keys have at most one value
  in the request context. For example, when you tag resources in AWS, each resource
  tag is stored as a key-value pair. Since a resource tag key can have only a single
  tag value, [aws:ResourceTag/tag-key](reference_policies_condition-keys.md#condition-keys-resourcetag "reference_policies_condition-keys.md#condition-keys-resourcetag") is a single-valued context
  key. Do not use a condition set operator with a single-valued context key.
- _Multivalued_ condition context keys can have multiple values
  in the request context. For example, when you tag resources in AWS, you can
  include multiple tag key-value pairs in a single request. Therefore, [aws:TagKeys](reference_policies_condition-keys.md#condition-keys-tagkeys "reference_policies_condition-keys.md#condition-keys-tagkeys") is a multivalued context key. Multivalued
  context keys require a condition set operator.
  For example, a request can originate from at most one VPC endpoint, so [aws:SourceVpce](reference_policies_condition-keys.md#condition-keys-sourcevpce "reference_policies_condition-keys.md#condition-keys-sourcevpce") is a single-valued context key. Since a service
  can have more than one service principal name that belongs to the service, [aws:PrincipalServiceNamesList](reference_policies_condition-keys.md#condition-keys-principalservicenameslist "reference_policies_condition-keys.md#condition-keys-principalservicenameslist") is a multivalued context
  key.

###### Important

The difference between single-valued and multivalued context keys depends on the
number of values in the request context, not the number of values in the policy
condition.

## Key points

- The _Single-valued_ and _Multivalued_
  classifications are included in the description of each condition context key as
  _Value type_ in the [AWS global condition context
  keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md") topic.
- Multivalued context keys in the [Service Authorization Reference](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") use an `ArrayOf` prefix
  followed by the condition operator category type, such as
  `ArrayOfString` or `ArrayOfARN`, indicating that the
  request may include multiple values for a condition context key.
- You can use any available single-valued context key as a policy variable, but
  you cannot use a multivalued context key as a policy variable. For more
  information about policy variables, see [IAM policy elements: Variables and tags](reference_policies_variables.md "reference_policies_variables.md").
- When using context keys that include key-value pairs, it's important to note
  that even though there can be multiple tag-key values, each `tag-key`
  can have only one value.
  - [aws:PrincipalTag/tag-key](reference_policies_condition-keys.md#condition-keys-principaltag "reference_policies_condition-keys.md#condition-keys-principaltag"), [aws:RequestTag/tag-key](reference_policies_condition-keys.md#condition-keys-requesttag "reference_policies_condition-keys.md#condition-keys-requesttag") and [aws:ResourceTag/tag-key](reference_policies_condition-keys.md#condition-keys-resourcetag "reference_policies_condition-keys.md#condition-keys-resourcetag") are single-valued context
    keys.
  - [aws:TagKeys](reference_policies_condition-keys.md#condition-keys-tagkeys "reference_policies_condition-keys.md#condition-keys-tagkeys") defines what tag-keys are
    allowed in a request but does not include the tag-key values. Because
    you can include multiple tag key-value pairs in a request,
    `aws:TagKeys` is a multivalued context key.

- Multivalued context keys require a condition set operator. Do not use
  condition set operators `ForAllValues` or `ForAnyValue`
  with single-valued context keys. Using condition set operators with
  single-valued context keys can lead to overly permissive policies.

## Set operators

for multivalued context keys

To compare your condition context key against a [request context](intro-structure.md#intro-structure-request "intro-structure.md#intro-structure-request") key with multiple values,
you must use the `ForAllValues` or `ForAnyValue` set operators.
These set operators are used to compare two sets of values, such as the set of tags in a
request and the set of tags in a policy condition.

The `ForAllValues` and `ForAnyValue` qualifiers add
set-operation functionality to the condition operator, allowing you to test request
context keys with multiple values against multiple context key values in a policy
condition. Additionally, if you include a multivalued string context key in your policy
with a wildcard or a variable, you must also use the `StringLike`
[condition operator](reference_policies_elements_condition_operators.md#Conditions_String "reference_policies_elements_condition_operators.md#Conditions_String"). Multiple condition key
values must be enclosed in brackets like an [array](reference_policies_grammar.md#policies-grammar-json "reference_policies_grammar.md#policies-grammar-json"), for example, `"Key2":["Value2A", "Value2B"]`.

### ForAllValues

The `ForAllValues` qualifier tests whether the value of every member of
the request context matches the condition operator that follows the qualifier. The
condition returns `true` if every context key value in the request
matches a context key value in the policy. It also returns `true` if
there are no context keys in the request.

###### Important

Use caution if you use `ForAllValues` with an `Allow`
effect, as it can be overly permissive if the presence of missing context keys
in the request context is unexpected. You should always include the [Null](reference_policies_elements_condition_operators.md#Conditions_Null "reference_policies_elements_condition_operators.md#Conditions_Null") condition operator in
your policy with a `false` value to check if the context key exists
and its value is not null. For an example, see [Controlling access based on tag
keys](access_tags.md#access_tags_control-tag-keys "access_tags.md#access_tags_control-tag-keys").

#### Example

ForAllValues set operator

In the following example, ForAllValues is used with aws:TagKeys to allow users
to delete specific tags assigned to an EC2 instance. This policy allows users to
delete only the `environment` and `cost-center` tags. You
can delete them separately or together. The tag-keys in the request must match
exactly the specified keys in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:DeleteTags",
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:instance/*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "environment",
 "cost-center"
 ]
 },
 "Null": {
 "aws:TagKeys": "false"
 }
 }
 }
 ]
}`

```

The following table shows how AWS evaluates this policy based on the
condition key values in your request.

| Policy Condition                                                                                                       | Request Context                            | Result       |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"ForAllValues:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }, "Null": { "aws:TagKeys": "false" }` | `aws:TagKeys: – environment`               | **Match**    |
| `"ForAllValues:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }, "Null": { "aws:TagKeys": "false" }` | `aws:TagKeys: – cost-center`               | **Match**    |
| `"ForAllValues:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }, "Null": { "aws:TagKeys": "false" }` | `aws:TagKeys: – environment – cost-center` | **Match**    |
| `"ForAllValues:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }, "Null": { "aws:TagKeys": "false" }` | `aws:TagKeys: – environment – dept`        | **No match** |
| `"ForAllValues:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }, "Null": { "aws:TagKeys": "false" }` | No `aws:TagKeys` in the request context.   | **No match** | Note that in the last example, the result is "No Match" because the Null condition check prevents matching when the context key is missing. This is a best practice to avoid overly permissive policies. ### ForAnyValue The `ForAnyValue` qualifier tests whether at least one member of the set of request context key values matches at least one member of the set of context key values in your policy condition. The condition returns `true` if any one of the context key values in the request matches any one of the context key values in the policy. For no matching context key or if the key does not exist, the condition returns `false`. ###### Important When using `ForAnyValue` with a `Deny` effect, if the context key is not present in the request, the policy evaluates as **No match**. For consistent behavior, add an explicit [Null](reference_policies_elements_condition_operators.md#Conditions_Null "reference_policies_elements_condition_operators.md#Conditions_Null") condition check in your policy to verify whether the context key exists. For details, see [Condition operator to check existence of condition keys](reference_policies_elements_condition_operators.md#Conditions_Null "reference_policies_elements_condition_operators.md#Conditions_Null") . #### Example ForAnyValue set operator In the following example, ForAnyValue is used with aws:TagKeys to allow users to delete specific tags assigned to an EC2 instance. This policy allows users to delete tags for an instance if the tag keys specified in the request include `environment` or `cost-center`. The request can include additional tag keys beyond those specified in the policy, but must include at least one of the specified keys to match the condition. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:DeleteTags", "Resource": "arn:aws:ec2:us-east-1:`111122223333`:instance/*", "Condition": { "ForAnyValue:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] } } } ] }` `` The following table shows how AWS evaluates this policy based on the condition key values in your request. |
| Policy Condition                                                                                                       | Request Context                            | Result       |
| ---                                                                                                                    | ---                                        | ---          |
| `"ForAnyValue:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }`                                      | `aws:TagKeys: – environment`               | **Match**    |
| `"ForAnyValue:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }`                                      | `aws:TagKeys: – cost-center`               | **Match**    |
| `"ForAnyValue:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }`                                      | `aws:TagKeys: – environment – cost-center` | **Match**    |
| `"ForAnyValue:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }`                                      | `aws:TagKeys: – environment – dept`        | **Match**    |
| `"ForAnyValue:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }`                                      | `aws:TagKeys: – dept`                      | **No match** |
| `"ForAnyValue:StringEquals": { "aws:TagKeys": [ "environment", "cost-center" ] }`                                      | No `aws:TagKeys` in the request context.   | **No match** |
