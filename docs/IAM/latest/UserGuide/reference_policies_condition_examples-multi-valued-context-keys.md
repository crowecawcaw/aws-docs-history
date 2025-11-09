# Multivalued

context key examples

The following set of policy examples demonstrate how to create policy conditions with
multivalued context keys.

## Example:

Deny policy with condition set operator ForAllValues

The following examples show how to use an identity-based policy to deny the use of IAM
tagging actions when specific tag key prefixes are included in the request. The values for
[aws:TagKeys](reference_policies_condition-keys.md#condition-keys-tagkeys "reference_policies_condition-keys.md#condition-keys-tagkeys") include a wildcard
(\*) for partial string matching. The policy includes the `ForAllValues` set
operator with context key `aws:TagKeys` because the request context key can include
multiple values. In order for context key `aws:TagKeys` to match, every value in
the request context must match at least one value in the policy.

The `ForAllValues` set operator also returns true if there are no context keys
in the request.

You can prevent missing context keys or context keys with empty values from evaluating to
true by including a `Null` condition operator in your policy with a value of
`false` to check if the context key in the request exists and its value is not
null. For more information, see [Condition operator to check existence of condition keys](reference_policies_elements_condition_operators.md#Conditions_Null "reference_policies_elements_condition_operators.md#Conditions_Null") .

###### Important

This policy does not allow any actions. Use this policy in combination with other
policies that allow specific actions.

###### Example Deny a single policy condition value for a multivalued context key

In the following example, the policy denies requests where the values for
`aws:TagKeys` in the request do not include the prefix
**key1**. The request context can have multiple values, but because of
the `ForAllValues` condition set operator, all the tag key values in the request
context must start with the prefix **key1**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyRestrictedTags",
 "Effect": "Deny",
 "Action": [
 "iam:Tag*",
 "iam:UnTag*"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "ForAllValues:StringNotLike": {
 "aws:TagKeys": "key1*"
 }
 }
 }
 ]
}`

```

The following table shows how AWS evaluates this policy based on the condition key
values in your request. For a Deny statement, Match is Denied and No match is Not denied, so
it may be allowed by another statement.

| Policy Condition                                                         | Request Context                                         | Result                                               |
| ------------------------------------------------------------------------ | ------------------------------------------------------- | ---------------------------------------------------- |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:TagKeys": "key1*"<br>}<br>` | `<br>aws:TagKeys:<br>– key1:legal<br>`                  | **No match**<br>May be allowed by another statement. |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:TagKeys": "key1*"<br>}<br>` | `<br>aws:TagKeys:<br>– key1:hr<br>– key1:personnel<br>` | **No match**<br>May be allowed by another statement. |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:TagKeys": "key1*"<br>}<br>` | ``<br>aws:TagKeys:<br>– `key2`:audit<br>``              | **Match**                                            |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:TagKeys": "key1*"<br>}<br>` | No `aws:TagKeys` in the request context.                | **Match**                                            |

###### Example Deny multiple policy condition values for a multivalued context key

In the following example, the policy denies requests where the values for
`aws:TagKeys` in the request do not include the prefix
**key1** or **key2**. The request context can have
multiple values, but because of the `ForAllValues` condition set operator, all
the tag key values in the request context must start with the prefix
**key1** or **key2**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyRestrictedTags",
 "Effect": "Deny",
 "Action": [
 "iam:Tag*",
 "iam:UnTag*"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "ForAllValues:StringNotLike": {
 "aws:TagKeys": [
 "key1*",
 "key2*"
 ]
 }
 }
 }
 ]
}`

```

The following table shows how AWS evaluates this policy based on the condition key
values in your request. For a Deny statement, Match is Denied and No match is Not denied, so
it may be allowed by another statement.

| Policy Condition                                                                               | Request Context                                         | Result                                               |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------- |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:TagKeys": [<br>"key1*",<br>"key2*"<br>]<br>}<br>` | `<br>aws:TagKeys:<br>– key1:legal<br>`                  | **No match**<br>May be allowed by another statement. |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:TagKeys": [<br>"key1*",<br>"key2*"<br>]<br>}<br>` | `<br>aws:TagKeys:<br>– key1:hr<br>– key1:personnel<br>` | **No match**<br>May be allowed by another statement. |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:TagKeys": [<br>"key1*",<br>"key2*"<br>]<br>}<br>` | `<br>aws:TagKeys:<br>– key1:hr<br>– key2:audit<br>`     | **No match**<br>May be allowed by another statement. |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:TagKeys": [<br>"key1*",<br>"key2*"<br>]<br>}<br>` | ``<br>aws:TagKeys:<br>– `key3`:legal<br>``              | **Match**                                            |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:TagKeys": [<br>"key1*",<br>"key2*"<br>]<br>}<br>` | No `aws:TagKeys` in the request context.                | **Match**                                            |

## Example:

Deny policy with condition set operator ForAnyValue

The following identity-based policy example denies creating snapshots of EC2 instance
volumes if any snapshots are tagged with one of the tag keys specified in the policy,
`environment` or `webserver`. The policy includes the
`ForAnyValue` set operator with context key `aws:TagKeys` because the
request context key can include multiple values. If your tagging request includes any one of
the tag key values specified in the policy, the `aws:TagKeys` context key returns
true invoking the deny policy effect.

###### Important

This policy does not allow any actions. Use this policy in combination with other
policies that allow specific actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ec2:CreateSnapshot",
 "ec2:CreateSnapshots"
 ],
 "Resource": "arn:aws:ec2:us-west-2::snapshot/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "webserver"
 }
 }
 }
 ]
}`

```

The following table shows how AWS evaluates this policy based on the condition key
values in your request. For a Deny statement, Match is Denied and No match is Not denied, so
it may be allowed by another statement.

| Policy Condition                                                           | Request Context                                                  | Result                                               |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------- |
| `<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "webserver"<br>}<br>` | `<br>aws:TagKeys:<br>– webserver<br>`                            | **Match**                                            |
| `<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "webserver"<br>}<br>` | `<br>aws:TagKeys:<br>– environment<br>– webserver<br>– test<br>` | **Match**                                            |
| `<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "webserver"<br>}<br>` | `<br>aws:TagKeys:<br>– environment<br>– test<br>`                | **No match**<br>May be allowed by another statement. |
| `<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "webserver"<br>}<br>` | No `aws:TagKeys` in the request context.                         | **No match**<br>May be allowed by another statement. |
