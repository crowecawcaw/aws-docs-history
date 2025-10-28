# Troubleshooting service control policies (SCPs) with AWS Organizations

Use the information here to help you diagnose and fix common errors found in service control policies (SCPs).

Service control policies (SCPs) in AWS Organizations are similar to IAM policies and share a
common syntax. This syntax begins with the rules of [JavaScript Object Notation](http://www.json.org "http://www.json.org") (JSON). JSON describes an
_object_ with name and value pairs that make up the object. The
[IAM policy grammar](../../../IAM/latest/UserGuide/policies-grammar.md "../../../IAM/latest/UserGuide/policies-grammar.md") builds
on that by defining what names and values have meaning for, and are understood by, the
AWS services that use policies to grant permissions.

AWS Organizations uses a subset of the IAM syntax and grammar. For details, see [SCP syntax](orgs_manage_policies_scps_syntax.md "orgs_manage_policies_scps_syntax.md").

###### Common policy errors

- [More than one policy object](#morethanonepolicyblock "#morethanonepolicyblock")
- [More than one statement element](#morethanonestatement "#morethanonestatement")
- [Policy document exceeds maximum size](#scptoolong "#scptoolong")

## More than one policy object

An SCP must consist of one and only one JSON object. You denote an object by
placing { } braces around it. Although you can nest other objects within a JSON
object by embedding additional { } braces within the outer pair, a policy can
contain only one outermost pair of { } braces. The following example is **_incorrect_** because it
contains two objects at the top level (called out in
`red`):

JSON

```
``{`
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:Describe*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "s3:*",
 "Resource": "*"
 }
 ]
`}``

```

You can, however, meet the intention of the preceding example with the use of
correct policy grammar. Instead of including two complete policy objects, each with
its own `Statement` element, you can combine the two blocks into a single
`Statement` element. The `Statement` element has an array
of two objects as its value, as shown in the following example:

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:Describe*",
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": "s3:*",
      "Resource": "*"
    }
  ]
}

```

This example cannot be further compressed into a `Statement` with one
element because the two elements have different effects. Generally, you can combine
statements only when the `Effect` and `Resource` elements in
each statement are identical.

## More than one statement element

This error might at first appear to be a variation on the error in the preceding
section. However, syntactically it's a different type of error. In the following
example, there is only one policy object as denoted by a single pair of { } braces
at the top level. However, that object contains two `Statement` elements
within it.

An SCP must contain only one `Statement` element, consisting of the
name (`Statement`) appearing to the left of a colon, followed by its
value on the right. The value of a `Statement` element must be an object,
denoted by { } braces, containing one `Effect` element, one
`Action` element, and one `Resource` element. The
following example is **_incorrect_** because it contains two
`Statement` elements in the policy object:

JSON

```
`{
 "Version":"2012-10-17",
 "`Statement`": [
 {
 "Effect": "Allow",
 "Action": "ec2:Describe*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "s3:*",
 "Resource": "*"
 }
 ]
}`

```

Because a value object can be an array of multiple value objects, you can solve
this problem by combining the two `Statement` elements into one element
with an object array, as shown in the following example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": `[`
 {
 "Effect": "Allow",
 "Action": "ec2:Describe*",
 "Resource":"*"
 }`,`
 {
 "Effect": "Deny",
 "Action": "s3:*",
 "Resource": "*"
 }
 `]`
}`

```

The value of the `Statement` element is an object array. The array in
the example consists of two objects, each of which is a correct value for a
`Statement` element. Each object in the array is separated by commas.

## Policy document exceeds maximum size

The maximum size of an SCP document is 5,120 characters. This maximum size includes all
characters, including white space. To reduce the size of your SCP, you can remove
all white space characters (such as spaces and line breaks) that are outside
quotation marks.

###### Note

If you save the policy by
using the AWS Management Console, extra white space between JSON elements and outside of quotation marks is
removed and not counted. If you save the policy using an SDK
operation or the AWS CLI, then the policy is saved exactly as you
provided and no automatic removal of characters occurs.
