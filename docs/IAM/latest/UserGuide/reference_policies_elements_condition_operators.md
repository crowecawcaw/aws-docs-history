# IAM JSON policy elements:

Condition operators

Use condition operators in the `Condition` element to match the condition key and
value in the policy against values in the request context. For more information about the
`Condition` element, see [IAM JSON policy elements:
Condition](reference_policies_elements_condition.md "reference_policies_elements_condition.md").

The condition operator that you can use in a policy depends on the condition key you choose.
You can choose a global condition key or a service-specific condition key. To learn which
condition operator you can use for a global condition key, see [AWS global condition context
keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md"). To learn which condition operator you can use for a service-specific condition key, see
[Actions, Resources, and
Condition Keys for AWS Services](reference_policies_actions-resources-contextkeys.md "reference_policies_actions-resources-contextkeys.md") and choose the service that you want to view.

###### Important

If the key that you specify in a policy condition is not present in the request context,
the values do not match and the condition is _false_. If the policy
condition requires that the key is _not_ matched, such as
`StringNotLike` or `ArnNotLike`, and the right key is not present, the
condition is _true_. This logic applies to all condition operators except
[...IfExists](#Conditions_IfExists "#Conditions_IfExists") and [Null check](#Conditions_Null "#Conditions_Null"). These operators test whether the key is present (exists) in the request
context.

The condition operators can be grouped into the following categories:

- [String](#Conditions_String "#Conditions_String")
- [Numeric](#Conditions_Numeric "#Conditions_Numeric")
- [Date and time](#Conditions_Date "#Conditions_Date")
- [Boolean](#Conditions_Boolean "#Conditions_Boolean")
- [Binary](#Conditions_BinaryEquals "#Conditions_BinaryEquals")
- [IP address](#Conditions_IPAddress "#Conditions_IPAddress")
- [Amazon Resource Name (ARN)](#Conditions_ARN "#Conditions_ARN") (available for only
  some services.)
- [...IfExists](#Conditions_IfExists "#Conditions_IfExists") (checks if the key value exists
  as part of another check)
- [Null check](#Conditions_Null "#Conditions_Null") (checks if the key value exists as a
  standalone check)

## String condition operators

String condition operators let you construct `Condition` elements that restrict
access based on comparing a key to a string value.

- **Policy variables** – [Supported](reference_policies_variables.md "reference_policies_variables.md")
- **Wildcards** – [Supported](#Conditions_String-wildcard "#Conditions_String-wildcard")

| Condition operator          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `StringEquals`              | Exact matching, case sensitive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `StringNotEquals`           | Negated matching                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `StringEqualsIgnoreCase`    | Exact matching, ignoring case                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `StringNotEqualsIgnoreCase` | Negated matching, ignoring case                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `StringLike`                | Case-sensitive matching. The values can include multi-character match<br>wildcards (\*) and single-character match wildcards (?) anywhere in the string. You<br>must specify wildcards to achieve partial string matches.<br>NoteIf a key contains multiple values, `StringLike` can be qualified<br>with set operators—`ForAllValues:StringLike` and<br>`ForAnyValue:StringLike`. For more information, see [Set operators<br>for multivalued context keys](reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys "reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys"). |
| `StringNotLike`             | Negated case-sensitive matching. The values can include multi-character match<br>wildcards (\*) or single-character match wildcards (?) anywhere in the string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

###### Example string condition operator

For example, the following statement contains a `Condition` element that uses
[`aws:PrincipalTag`](reference_policies_condition-keys.md#condition-keys-principaltag "reference_policies_condition-keys.md#condition-keys-principaltag") key to specify that the principal making the
request must be tagged with the `iamuser-admin` job category.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "iam:*AccessKey*",
 "Resource": "arn:aws:iam::`111122223333`:user/*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalTag/job-category": "iamuser-admin"
 }
 }
 }
}`

```

If the key that you specify in a policy condition is not present in the request context,
the values do not match. In this example, the `aws:PrincipalTag/job-category` key
is present in the request context if the principal is using an IAM user with attached
tags. It is also included for a principal using an IAM role with attached tags or session
tags. If a user without the tag attempts to view or edit an access key, the condition
returns `false` and the request is implicitly denied by this statement.

The following table shows how AWS evaluates this policy based on the condition key
values in your request.

| Policy Condition                                                                     | Request Context                                             | Result   |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------- | -------- |
| `<br>"StringEquals": {<br>"aws:PrincipalTag/job-category": "iamuser-admin"<br>}<br>` | `<br>aws:PrincipalTag/job-category:<br>– iamuser-admin<br>` | Match    |
| `<br>"StringEquals": {<br>"aws:PrincipalTag/job-category": "iamuser-admin"<br>}<br>` | `<br>aws:PrincipalTag/job-category:<br>– dev-ops<br>`       | No match |
| `<br>"StringEquals": {<br>"aws:PrincipalTag/job-category": "iamuser-admin"<br>}<br>` | No `aws:PrincipalTag/job-category` in the request context.  | No match |

###### Example using a policy variable with a string condition operator

The following example uses the `StringLike` condition operator to perform
string matching with a [policy variable](reference_policies_variables.md "reference_policies_variables.md")
to create a policy that lets an IAM user use the Amazon S3 console to manage his or her own
"home directory" in an Amazon S3 bucket. The policy allows the specified actions on an S3 bucket
as long as the `s3:prefix` matches any one of the specified patterns.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringLike": {
 "s3:prefix": [
 "",
 "home/",
 "home/${aws:username}/"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/home/${aws:username}",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/home/${aws:username}/*"
 ]
 }
 ]
}`

```

The following table shows how AWS evaluates this policy for different users based on
the [aws:username](reference_policies_condition-keys.md#condition-keys-username "reference_policies_condition-keys.md#condition-keys-username") value
in the request context.

| Policy condition                                                                             | Request context                            | Result                                                                                         |
| -------------------------------------------------------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| `<br>"StringLike": {<br>"s3:prefix": [<br>"home/",<br>"home/${aws:username}/"<br>]<br>}<br>` | `<br>aws:username:<br>– martha_rivera<br>` | ``<br>"StringLike": {<br>"s3:prefix": [<br>"home/",<br>"home/`martha_rivera`/"<br>]<br>}<br>`` |
| `<br>"StringLike": {<br>"s3:prefix": [<br>"home/",<br>"home/${aws:username}/"<br>]<br>}<br>` | `<br>aws:username:<br>– nikki_wolf<br>`    | ``<br>"StringLike": {<br>"s3:prefix": [<br>"home/",<br>"home/`nikki_wolf`/"<br>]<br>}<br>``    |
| `<br>"StringLike": {<br>"s3:prefix": [<br>"home/",<br>"home/${aws:username}/"<br>]<br>}<br>` | No `aws:username` in the request context.  | No match                                                                                       |

For an example of a policy that shows how to use the `Condition` element to
restrict access to resources based on an application ID and a user ID for OIDC federation,
see [Amazon S3: Allows Amazon Cognito users to
access objects in their bucket](reference_policies_examples_s3_cognito-bucket.md "reference_policies_examples_s3_cognito-bucket.md").

### Multivalued string condition

operators

If a key in the request contains multiple values, string operators can be qualified with
set operators `ForAllValues` and `ForAnyValue`. For more information
on the evaluation logic of multiple context keys or values, see [Set operators
for multivalued context keys](reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys "reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys").

| Condition operator                                                         | Description                                                                                                                           |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `ForAllValues:StringEquals`<br>`ForAllValues:StringEqualsIgnoreCase`       | All of the values for the condition key in the request must match at least one<br>of the values in your policy.                       |
| `ForAnyValue:StringEquals`<br>`ForAnyValue:StringEqualsIgnoreCase`         | At least one condition key value in the request must match one of the values<br>in your policy.                                       |
| `ForAllValues:StringNotEquals`<br>`ForAllValues:StringNotEqualsIgnoreCase` | Negated matching.<br>None of the values of the context key in the request can match any of the<br>context key values in your policy.  |
| `ForAnyValue:StringNotEquals`<br>`ForAnyValue:StringNotEqualsIgnoreCase`   | Negated matching.<br>At least one context key value in the request must NOT match any of values in<br>the context key in your policy. |
| `ForAllValues:StringLike`                                                  | All of the values for the condition key in the request must match at least one<br>of the values in your policy.                       |
| `ForAnyValue:StringLike`                                                   | At least one condition key value in the request must match one of the values<br>in your policy.                                       |
| `ForAllValues:StringNotLike`                                               | Negated matching.<br>None of the values of the context key in the request can match any of the<br>context key values in your policy.  |
| `ForAnyValue:StringNotLike`                                                | Negated matching.<br>At least one context key value in the request must NOT match any of values in<br>the context key in your policy. |

###### Example using `ForAnyValue` with a string condition operator

This example shows how you might create an identity-based policy that allows using the
Amazon EC2 `CreateTags` action to attach tags to an instance. When you use
`StringEqualsIgnoreCase`, you can attach tags only if the tag contains the
`environment` key with the `preprod` or `storage`
values. When you append `IgnoreCase` to the operator, you allow any existing
tag value capitalization, such as `preprod`, `Preprod`, and
`PreProd`, to resolve to true.

When you add the `ForAnyValue` modifier with the [aws:TagKeys](reference_policies_condition-keys.md#condition-keys-tagkeys "reference_policies_condition-keys.md#condition-keys-tagkeys") condition key,
at least one tag key value in the request must match the value `environment`.
`ForAnyValue` comparison is case sensitive, which stops users from using the
incorrect case for the tag key, such as using `Environment` instead of
`environment`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:*:*:instance/*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "aws:RequestTag/environment": [
 "preprod",
 "storage"
 ]
 },
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "environment"
 }
 }
 }
}`

```

The following table shows how AWS evaluates this policy based on the condition key
values in your request.

| Policy condition                                                                                                                                                                     | Request context                                                                                     | Result   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | -------- |
| `<br>"StringEqualsIgnoreCase": {<br>"aws:RequestTag/environment": [<br>"preprod",<br>"storage"<br>]<br>},<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "environment"<br>}<br>` | `<br>aws:TagKeys:<br>– environment<br>aws:RequestTag/environment:<br>– preprod<br>`                 | Match    |
| `<br>"StringEqualsIgnoreCase": {<br>"aws:RequestTag/environment": [<br>"preprod",<br>"storage"<br>]<br>},<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "environment"<br>}<br>` | `<br>aws:TagKeys:<br>– environment<br>– costcenter<br>aws:RequestTag/environment:<br>– PreProd<br>` | Match    |
| `<br>"StringEqualsIgnoreCase": {<br>"aws:RequestTag/environment": [<br>"preprod",<br>"storage"<br>]<br>},<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "environment"<br>}<br>` | `<br>aws:TagKeys:<br>– Environment<br>aws:RequestTag/Environment:<br>– preprod<br>`                 | No match |
| `<br>"StringEqualsIgnoreCase": {<br>"aws:RequestTag/environment": [<br>"preprod",<br>"storage"<br>]<br>},<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "environment"<br>}<br>` | `<br>aws:TagKeys:<br>– costcenter<br>aws:RequestTag/environment:<br>– preprod<br>`                  | No match |
| `<br>"StringEqualsIgnoreCase": {<br>"aws:RequestTag/environment": [<br>"preprod",<br>"storage"<br>]<br>},<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "environment"<br>}<br>` | No `aws:TagKeys` in the request context.<br>`<br>aws:RequestTag/environment:<br>– storage<br>`      | No match |
| `<br>"StringEqualsIgnoreCase": {<br>"aws:RequestTag/environment": [<br>"preprod",<br>"storage"<br>]<br>},<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "environment"<br>}<br>` | `<br>aws:TagKeys:<br>– environment<br>`<br>No `aws:RequestTag/environment` in the request context.  | No match |
| `<br>"StringEqualsIgnoreCase": {<br>"aws:RequestTag/environment": [<br>"preprod",<br>"storage"<br>]<br>},<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": "environment"<br>}<br>` | No `aws:TagKeys` in the request context.<br>No `aws:RequestTag/environment` in the request context. | No match |

### Wildcard matching

String condition operators perform a patternless matching that does not enforce a
predefined format. ARN and Date condition operators are a subset of string operators that
enforce a structure on the condition key value.

We recommend you use condition operators that correspond to the values you're comparing
keys to. For example, you should use [String condition operators](#Conditions_String "#Conditions_String") when comparing keys
to string values. Similarly, you should use [Amazon Resource Name (ARN) condition operators](#Conditions_ARN "#Conditions_ARN") when comparing
keys to ARN values.

This example shows how you might create a boundary around resources in your
organization. The condition in this policy denies access to Amazon S3 actions unless the
resource being accessed is in a specific set of organizational units (OUs) in AWS Organizations. An
AWS Organizations path is a text representation of the structure of an organization's
entity.

The condition requires that `aws:ResourceOrgPaths` contains any of the listed OU
paths. Because `aws:ResourceOrgPaths` is a multi-value condition, the policy
uses the `ForAllValues:StringNotLike` operator to compare the values of
`aws:ResourceOrgPaths` to the list of OUs in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyS3AccessOutsideMyBoundary",
 "Effect": "Deny",
 "Action": [
 "s3:*"
 ],
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringNotLike": {
 "aws:ResourceOrgPaths": [
 "o-acorg/r-acroot/ou-acroot-mediaou/",
 "o-acorg/r-acroot/ou-acroot-sportsou/*"
 ]
 }
 }
 }
 ]
}`

```

The following table shows how AWS evaluates this policy based on the condition key
values in your request.

| Policy condition                                                                                                                                                      | Request context                                                                      | Result   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | -------- |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:ResourceOrgPaths": [<br>"o-acorg/r-acroot/ou-acroot-mediaou/",<br>"o-acorg/r-acroot/ou-acroot-sportsou/*"<br>]<br>}<br>` | `<br>aws:ResourceOrgPaths:<br>– o-acorg/r-acroot/ou-acroot-sportsou/costcenter/<br>` | Match    |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:ResourceOrgPaths": [<br>"o-acorg/r-acroot/ou-acroot-mediaou/",<br>"o-acorg/r-acroot/ou-acroot-sportsou/*"<br>]<br>}<br>` | `<br>aws:ResourceOrgPaths:<br>– o-acorg/r-acroot/ou-acroot-mediaou/costcenter/<br>`  | No match |
| `<br>"ForAllValues:StringNotLike": {<br>"aws:ResourceOrgPaths": [<br>"o-acorg/r-acroot/ou-acroot-mediaou/",<br>"o-acorg/r-acroot/ou-acroot-sportsou/*"<br>]<br>}<br>` | No `aws:ResourceOrgPaths:` in the request.                                           | No match |

## Numeric condition operators

Numeric condition operators let you construct `Condition` elements that
restrict access based on comparing a key to an integer or decimal value.

- **Policy variables** – Not supported
- **Wildcards** – Not supported

| Condition operator         | Description                       |
| -------------------------- | --------------------------------- |
| `NumericEquals`            | Matching                          |
| `NumericNotEquals`         | Negated matching                  |
| `NumericLessThan`          | "Less than" matching              |
| `NumericLessThanEquals`    | "Less than or equals" matching    |
| `NumericGreaterThan`       | "Greater than" matching           |
| `NumericGreaterThanEquals` | "Greater than or equals" matching |

For example, the following statement contains a `Condition` element that uses
the `NumericLessThanEquals` condition operator with the `s3:max-keys`
key to specify that the requester can list _up to_ 10 objects in
`amzn-s3-demo-bucket` at a time.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket",
 "Condition": {"NumericLessThanEquals": {"s3:max-keys": "10"}}
 }
}`

```

If the key that you specify in a policy condition is not present in the request context,
the values do not match. In this example, the `s3:max-keys` key is always present
in the request when you perform the `ListBucket` operation. If this policy allowed
all Amazon S3 operations, then only the operations that include the `max-keys` context
key with a value of less than or equal to 10 would be allowed.

## Date condition operators

Date condition operators let you construct `Condition` elements that restrict
access based on comparing a key to a date/time value. You use these condition operators with
[`aws:CurrentTime`](reference_policies_condition-keys.md#condition-keys-currenttime "reference_policies_condition-keys.md#condition-keys-currenttime") key or [`aws:EpochTime`](reference_policies_condition-keys.md#condition-keys-epochtime "reference_policies_condition-keys.md#condition-keys-epochtime") key. You must specify date/time values with one of the
[W3C implementations of the ISO 8601 date
formats](http://www.w3.org/TR/NOTE-datetime "http://www.w3.org/TR/NOTE-datetime") or in epoch (UNIX) time.

- **Policy variables** – Not supported
- **Wildcards** – Not supported

| Condition operator      | Description                                    |
| ----------------------- | ---------------------------------------------- |
| `DateEquals`            | Matching a specific date                       |
| `DateNotEquals`         | Negated matching                               |
| `DateLessThan`          | Matching before a specific date and time       |
| `DateLessThanEquals`    | Matching at or before a specific date and time |
| `DateGreaterThan`       | Matching after a specific a date and time      |
| `DateGreaterThanEquals` | Matching at or after a specific date and time  |

For example, the following statement contains a `Condition` element that uses
the `DateGreaterThan` condition operator with the [`aws:TokenIssueTime`](reference_policies_condition-keys.md#condition-keys-tokenissuetime "reference_policies_condition-keys.md#condition-keys-tokenissuetime") key. This condition specifies that the temporary
security credentials used to make the request were issued in 2020. This policy can be updated
programmatically every day to ensure that account members use fresh credentials.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "iam:*AccessKey*",
 "Resource": "arn:aws:iam::`111122223333`:user/*",
 "Condition": {
 "DateGreaterThan": {
 "aws:TokenIssueTime": "2020-01-01T00:00:01Z"
 }
 }
 }
}`

```

If the key that you specify in a policy condition is not present in the request context,
the values do not match. The `aws:TokenIssueTime` key is present in the request
context only when the principal uses temporary credentials to make the request. The key is not
present in AWS CLI, AWS API, or AWS SDK requests that are made using access keys. In this
example, if an IAM user attempts to view or edit an access key, the request is
denied.

## Boolean condition operators

Boolean conditions let you construct `Condition` elements that restrict access
based on comparing a key to `true` or `false`.

If a key contains multiple values, boolean operators can be qualified with set operators
`ForAllValues` and `ForAnyValue`. For more information on the
evaluation logic of multiple context keys or values, see [Set operators
for multivalued context keys](reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys "reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys").

- **Policy variables** – [Supported](reference_policies_variables.md "reference_policies_variables.md")
- **Wildcards** – Not supported

| Condition operator  | Description                                                                                                                                                                                                                                                                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Bool`              | Boolean matching                                                                                                                                                                                                                                                                                                                                                     |
| `ForAllValues:Bool` | Use with the Array of Bool data type. All of the booleans in the context key<br>values must match the boolean values in your policy.<br>To prevent `ForAllValues` operators from evaluating missing context<br>keys or context keys with empty values as Allowed, you can include the [Null condition operator](#Conditions_Null "#Conditions_Null") in your policy. |
| `ForAnyValue:Bool`  | Use with the Array of Bool data type. At least one of the booleans in the<br>context key values must match the boolean values in your policy.                                                                                                                                                                                                                        |

###### Example boolean condition operator

The following identity-based policy uses the `Bool` condition operator with
the [`aws:SecureTransport`](reference_policies_condition-keys.md#condition-keys-securetransport "reference_policies_condition-keys.md#condition-keys-securetransport") key to deny replicating objects and object
tags to the destination bucket and its contents if the request is not over SSL.

###### Important

This policy does not allow any actions. Use this policy in combination with other
policies that allow specific actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BooleanExample",
 "Action": "s3:ReplicateObject",
 "Effect": "Deny",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ],
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 }
 }
 ]
}`

```

The following table shows how AWS evaluates this policy based on the condition key
values in your request.

| Policy condition                                           | Request context                                  | Result   |
| ---------------------------------------------------------- | ------------------------------------------------ | -------- |
| `<br>"Bool": {<br>"aws:SecureTransport": "false"<br>}<br>` | `<br>aws:SecureTransport:<br>– false<br>`        | Match    |
| `<br>"Bool": {<br>"aws:SecureTransport": "false"<br>}<br>` | `<br>aws:SecureTransport:<br>– true<br>`         | No match |
| `<br>"Bool": {<br>"aws:SecureTransport": "false"<br>}<br>` | No `aws:SecureTransport` in the request context. | No match |

## Binary condition operators

The `BinaryEquals` condition operator lets you construct `Condition`
elements that test key values that are in binary format. It compares the value of the
specified key byte for byte against a [base-64](https://en.wikipedia.org/wiki/Base64 "https://en.wikipedia.org/wiki/Base64") encoded representation of the binary value in the policy. If the key that
you specify in a policy condition is not present in the request context, the values do not
match.

- **Policy variables** – Not supported
- **Wildcards** – Not supported

```
"Condition" : {
  "BinaryEquals": {
    "`key`" : "QmluYXJ5VmFsdWVJbkJhc2U2NA=="
  }
}
```

| Policy condition                                                           | Request context                                  | Result   |
| -------------------------------------------------------------------------- | ------------------------------------------------ | -------- |
| `<br>"BinaryEquals": {<br>"key" : "QmluYXJ5VmFsdWVJbkJhc2U2NA=="<br>}<br>` | `<br>key:<br>– QmluYXJ5VmFsdWVJbkJhc2U2NA==<br>` | Match    |
| `<br>"BinaryEquals": {<br>"key" : "QmluYXJ5VmFsdWVJbkJhc2U2NA=="<br>}<br>` | `<br>key:<br>– ASIAIOSFODNN7EXAMPLE<br>`         | No match |
| `<br>"BinaryEquals": {<br>"key" : "QmluYXJ5VmFsdWVJbkJhc2U2NA=="<br>}<br>` | No `key` in the request context.                 | No match |

## IP address condition operators

IP address condition operators let you construct `Condition` elements that
restrict access based on comparing a key to an IPv4 or IPv6 address or range of IP addresses.
You use these with the [`aws:SourceIp`](reference_policies_condition-keys.md#condition-keys-sourceip "reference_policies_condition-keys.md#condition-keys-sourceip") key. The value must be in the standard CIDR format (for
example, 203.0.113.0/24 or 2001:DB8:1234:5678::/64). If you specify an IP address without the
associated routing prefix, IAM uses the default prefix value of `/32`.

Some AWS services support IPv6, using :: to represent a range of 0s. To learn whether a
service supports IPv6, see the documentation for that service.

- **Policy variables** – Not supported
- **Wildcards** – Not supported

| Condition operator | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `IpAddress`        | The specified IP address or range                         |
| `NotIpAddress`     | All IP addresses except the specified IP address or range |

###### Example IP address condition operator

The following statement uses the `IpAddress` condition operator with the
`aws:SourceIp` key to specify that the request must come from the IP range
203.0.113.0 to 203.0.113.255.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "iam:*AccessKey*",
 "Resource": "arn:aws:iam::`111122223333`:user/*",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": "203.0.113.0/24"
 }
 }
 }
}`

```

The `aws:SourceIp` condition key resolves to the IP address that the request
originates from. If the requests originates from an Amazon EC2 instance,
`aws:SourceIp` evaluates to the instance's public IP address.

If the key that you specify in a policy condition is not present in the request context,
the values do not match. The `aws:SourceIp` key is always present in the request
context, except when the requester uses a VPC endpoint to make the request. In this case,
the condition returns `false` and the request is implicitly denied by this
statement.

The following table shows how AWS evaluates this policy based on the condition key
values in your request.

| Policy condition                                                  | Request context                           | Result   |
| ----------------------------------------------------------------- | ----------------------------------------- | -------- |
| `<br>"IpAddress": {<br>"aws:SourceIp": "203.0.113.0/24"<br>}<br>` | `<br>aws:SourceIp:<br>– 203.0.113.1<br>`  | Match    |
| `<br>"IpAddress": {<br>"aws:SourceIp": "203.0.113.0/24"<br>}<br>` | `<br>aws:SourceIp:<br>– 198.51.100.1<br>` | No match |

The following example shows how to mix IPv4 and IPv6 addresses to cover all of your
organization's valid IP addresses. We recommend that you update your organization's policies
with your IPv6 address ranges in addition to IPv4 ranges you already have to ensure the
policies continue to work as you make the transition to IPv6.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "`someservice`:*",
 "Resource": "*",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "203.0.113.0/24",
 "2001:DB8:1234:5678::/64"
 ]
 }
 }
 }
}`

```

The `aws:SourceIp` condition key works only in a JSON policy if you are
calling the tested API directly as a user. If you instead use a service to call the target
service on your behalf, the target service sees the IP address of the calling service rather
than the IP address of the originating user. This can happen, for example, if you use
AWS CloudFormation to call Amazon EC2 to construct instances for you. There is currently no way to pass
the originating IP address through a calling service to the target service for evaluation in
a JSON policy. For these types of service API calls, do not use the
`aws:SourceIp` condition key.

## Amazon Resource Name (ARN) condition operators

Amazon Resource Name (ARN) condition operators let you construct `Condition`
elements that restrict access based on comparing a key to an ARN. The ARN is considered a
string.

- **Policy variables** – [Supported](reference_policies_variables.md "reference_policies_variables.md")
- **Wildcards** – [Supported](reference_policies_elements_resource.md#reference_policies_elements_resource_wildcards "reference_policies_elements_resource.md#reference_policies_elements_resource_wildcards")

| Condition operator           | Description                                                                                                                                                                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ArnEquals`, `ArnLike`       | Case-sensitive matching of the ARN. Each of the six colon-delimited components<br>of the ARN is checked separately and each can include multi-character match<br>wildcards (\*) or single-character match wildcards (?). The `ArnEquals`<br>and `ArnLike` condition operators behave identically. |
| `ArnNotEquals`, `ArnNotLike` | Negated matching for ARN. The `ArnNotEquals` and<br>`ArnNotLike` condition operators behave identically.                                                                                                                                                                                          |

###### Example ARN condition operator

The following resource-based policy example shows a policy attached to an Amazon SQS queue to
which you want to send SNS messages. It gives Amazon SNS permission to send messages to the queue
(or queues) of your choice, but only if the service is sending the messages on behalf of a
particular Amazon SNS topic (or topics). You specify the queue in the `Resource`
field, and the Amazon SNS topic as the value for the `SourceArn` key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {
 "Service": "sns.amazonaws.com"
 },
 "Action": "SQS:SendMessage",
 "Resource": "arn:aws:sqs:`us-east-1`:`123456789012`:`QUEUE-ID`",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:sns:`us-east-1`:`123456789012`:`TOPIC-ID`"
 }
 }
 }
}`

```

The [`aws:SourceArn`](reference_policies_condition-keys.md#condition-keys-sourcearn "reference_policies_condition-keys.md#condition-keys-sourcearn") key is present in the request context only if a
resource triggers a service to call another service on behalf of the resource owner. If an
IAM user attempts to perform this operation directly, the condition returns
`false` and the request is implicitly denied by this statement.

The following table shows how AWS evaluates this policy based on the condition key
values in your request.

| Policy condition                                                                                | Request context                                                           | Result   |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------- |
| `<br>"ArnEquals": {<br>"aws:SourceArn": "arn:aws:sns:us-west-2:123456789012:TOPIC-ID"<br>}<br>` | `<br>aws:SourceArn:<br>– arn:aws:sns:us-west-2:123456789012:TOPIC-ID<br>` | Match    |
| `<br>"ArnEquals": {<br>"aws:SourceArn": "arn:aws:sns:us-west-2:123456789012:TOPIC-ID"<br>}<br>` | `<br>aws:SourceArn:<br>– arn:aws:sns:us-west-2:777788889999:TOPIC-ID<br>` | No match |
| `<br>"ArnEquals": {<br>"aws:SourceArn": "arn:aws:sns:us-west-2:123456789012:TOPIC-ID"<br>}<br>` | No `aws:SourceArn` in the request context.                                | No match |

### Multivalued ARN condition operators

If a key in the request contains multiple values, ARN operators can be qualified with
set operators `ForAllValues` and `ForAnyValue`. For more information
on the evaluation logic of multiple context keys or values, see [Set operators
for multivalued context keys](reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys "reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys").

| Condition operator                                       | Description                                                                                                        |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `ForAllValues:ArnEquals`<br>`ForAllValues:ArnLike`       | All of the ARNs in the request context must match at least one of the ARN<br>patterns in your policy.              |
| `ForAnyValue:ArnEquals`<br>`ForAnyValue:ArnLike`         | At least one ARN in the request context must match one of the ARN patterns in<br>your policy.                      |
| `ForAllValues:ArnNotEquals`<br>`ForAllValues:ArnNotLike` | Negated matching.<br>None of the ARNs in the request context can match any string ARN patterns in<br>your policy.  |
| `ForAnyValue:ArnNotEquals`<br>`ForAnyValue:ArnNotLike`   | Negated matching.<br>At least one ARN in the request context must NOT match any of ARN patterns in<br>your policy. |

###### Example using `ForAllValues` with an ARN condition operator

The following example uses `ForAllValues:ArnLike` to create or update a
logical delivery source for Amazon CloudWatch Logs logs. The condition block includes the condition key
[`logs:LogGeneratingResourceArns`](../../../service-authorization/latest/reference/list_amazoncloudwatchlogs.md#amazoncloudwatchlogs-policy-keys "../../../service-authorization/latest/reference/list_amazoncloudwatchlogs.md#amazoncloudwatchlogs-policy-keys") to filter the log generating
resource ARNs passed in the request. Using this condition operator, all of the ARNs in the
request must match at least one ARN in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": "*",
 "Action": "logs:PutDeliverySource",
 "Resource": "arn:aws:logs:us-east-1:123456789012:delivery-source:*",
 "Condition": {
 "ForAllValues:ArnLike": {
 "logs:LogGeneratingResourceArns": [
 "arn:aws:cloudfront::123456789012:distribution/*",
 "arn:aws:cloudfront::123456789012:distribution/support*"
 ]
 }
 }
 }
 ]
}`

```

The following table shows how AWS evaluates this policy based on the condition key
values in your request.

| Policy condition                                                                                                                                                                                       | Request context                                                                                                                                                        | Result   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `<br>"ForAllValues:ArnLike": {<br>"logs:LogGeneratingResourceArns": [<br>"arn:aws::cloudfront:123456789012:distribution/*",<br>"arn:aws::cloudfront:123456789012:distribution/support*"<br>]<br>}<br>` | `<br>logs:LogGeneratingResourceArns:<br>– arn:aws::cloudfront:123456789012:distribution/costcenter<br>`                                                                | Match    |
| `<br>"ForAllValues:ArnLike": {<br>"logs:LogGeneratingResourceArns": [<br>"arn:aws::cloudfront:123456789012:distribution/*",<br>"arn:aws::cloudfront:123456789012:distribution/support*"<br>]<br>}<br>` | `<br>logs:LogGeneratingResourceArns:<br>– arn:aws::cloudfront:123456789012:distribution/costcenter<br>– arn:aws::cloudfront:123456789012:distribution/support2025<br>` | Match    |
| `<br>"ForAllValues:ArnLike": {<br>"logs:LogGeneratingResourceArns": [<br>"arn:aws::cloudfront:123456789012:distribution/*",<br>"arn:aws::cloudfront:123456789012:distribution/support*"<br>]<br>}<br>` | `<br>logs:LogGeneratingResourceArns:<br>– arn:aws::cloudfront:123456789012:distribution/costcenter<br>– arn:aws::cloudfront:123456789012:distribution/admin<br>`       | No match |
| `<br>"ForAllValues:ArnLike": {<br>"logs:LogGeneratingResourceArns": [<br>"arn:aws::cloudfront:123456789012:distribution/*",<br>"arn:aws::cloudfront:123456789012:distribution/support*"<br>]<br>}<br>` | `<br>logs:LogGeneratingResourceArns:<br>– arn:aws::cloudfront:777788889999:distribution/costcenter<br>`                                                                | No match |
| `<br>"ForAllValues:ArnLike": {<br>"logs:LogGeneratingResourceArns": [<br>"arn:aws::cloudfront:123456789012:distribution/*",<br>"arn:aws::cloudfront:123456789012:distribution/support*"<br>]<br>}<br>` | No `logs:LogGeneratingResourceArns` in the request<br>context.                                                                                                         | Match    |

The `ForAllValues` qualifier returns true if there are no context keys in
the request or if the context key value resolves to a null dataset, such as an empty
string. To prevent missing context keys or context keys with empty values from evaluating
to true, you can include the [Null condition
operator](#Conditions_Null "#Conditions_Null") in your policy with a `false` value to check if the context
key exists and its value is not null.

## ...IfExists condition operators

You can add `IfExists` to the end of any condition operator name except the
`Null` condition—for example, `StringLikeIfExists`. You do this
to say "If the condition key is present in the context of the request, process the key as
specified in the policy. If the key is not present, evaluate the condition element as true."
Other condition elements in the statement can still result in a nonmatch, but not a missing
key when checked with `...IfExists`. If you are using an `"Effect":
 "Deny"` element with a negated condition operator like
`StringNotEqualsIfExists`, the request is still denied even if the condition key
is not present.

**Example using `IfExists`**

Many condition keys describe information about a certain type of resource and only exist
when accessing that type of resource. These condition keys are not present on other types of
resources. This doesn't cause an issue when the policy statement applies to only one type of
resource. However, there are cases where a single statement can apply to multiple types of
resources, such as when the policy statement references actions from multiple services or when
a given action within a service accesses several different resource types within the same
service. In such cases, including a condition key that applies to only one of the resources in
the policy statement can cause the `Condition` element in the policy statement to
fail such that the statement's `"Effect"` does not apply.

For example, consider the following policy example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "`THISPOLICYDOESNOTWORK`",
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "*",
 "Condition": {"StringLike": {"ec2:InstanceType": [
 "t1.*",
 "t2.*",
 "m3.*"
 ]}}
 }
}`

```

The _intent_ of the preceding policy is to enable the user to launch
any instance that is type `t1`, `t2` or `m3`. However,
launching an instance requires accessing many resources in addition to the instance itself;
for example, images, key pairs, security groups, and more. The entire statement is evaluated
against every resource that is required to launch the instance. These additional resources do
not have the `ec2:InstanceType` condition key, so the `StringLike` check
fails, and the user is not granted the ability to launch _any_ instance
type.

To address this, use the `StringLikeIfExists` condition operator instead. This
way, the test only happens if the condition key exists. You could read the following policy
as: "If the resource being checked has an "`ec2:InstanceType`" condition key, then
allow the action only if the key value begins with `t1.`, `t2.`, or
`m3.`. If the resource being checked does not have that condition key, then don't
worry about it." The asterisk (\*) in the condition key values, when used with the
`StringLikeIfExists` condition operator, is interpreted as a wildcard to achieve
partial string matches. The `DescribeActions` statement includes the actions
required to view the instance in the console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RunInstance",
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "*",
 "Condition": {
 "StringLikeIfExists": {
 "ec2:InstanceType": [
 "t1.*",
 "t2.*",
 "m3.*"
 ]
 }
 }
 },
 {
 "Sid": "DescribeActions",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeImages",
 "ec2:DescribeInstances",
 "ec2:DescribeVpcs",
 "ec2:DescribeKeyPairs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following table shows how AWS evaluates this policy based on the condition key
values in your request.

| Policy condition                                                                                     | Request context                               | Result   |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------------- | -------- |
| `<br>"StringLikeIfExists": {<br>"ec2:InstanceType": [<br>"t1.*",<br>"t2.*",<br>"m3.*"<br>]<br>}<br>` | `<br>ec2:InstanceType:<br>– t1.micro<br>`     | Match    |
| `<br>"StringLikeIfExists": {<br>"ec2:InstanceType": [<br>"t1.*",<br>"t2.*",<br>"m3.*"<br>]<br>}<br>` | `<br>ec2:InstanceType:<br>– m2.micro<br>`     | No match |
| `<br>"StringLikeIfExists": {<br>"ec2:InstanceType": [<br>"t1.*",<br>"t2.*",<br>"m3.*"<br>]<br>}<br>` | No `ec2:InstanceType` in the request context. | Match    |

## Condition operator to check existence of condition keys

Use a `Null` condition operator to check if a condition key is absent at the
time of authorization. In the policy statement, use either `true` (the key doesn't
exist — it is null) or `false` (the key exists and its value is not
null).

You can not use a [policy variable](reference_policies_variables.md "reference_policies_variables.md") with
the `Null` condition operator.

For example, you can use this condition operator to determine whether a user is using
temporary credentials or their own credentials to make a request. If the user is using
temporary credentials, then the key `aws:TokenIssueTime` exists and has a value.
The following example shows a condition that states that the user must be using temporary
credentials (the key cannot be absent) for the user to use the Amazon EC2 API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":{
 "Action":"ec2:*",
 "Effect":"Allow",
 "Resource":"*",
 "Condition":{"Null":{"aws:TokenIssueTime":"false"}}
 }
}`

```
