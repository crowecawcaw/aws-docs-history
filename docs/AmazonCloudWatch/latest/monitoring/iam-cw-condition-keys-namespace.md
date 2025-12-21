# Using condition keys to limit

access to CloudWatch namespaces

Use IAM condition keys to limit users to publishing metrics only in the
CloudWatch namespaces that you specify. This section provides examples that describe
how to allow and exclude users from publishing metrics in a namespace.

**Allowing publishing in one namespace
only**

The following policy limits the user to publishing metrics only in the
namespace named `MyCustomNamespace`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Resource": "*",
 "Action": "cloudwatch:PutMetricData",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "MyCustomNamespace"
 }
 }
 }
}`

```

**Excluding publishing from a namespace**

The following policy allows the user to publish metrics in any namespace
except for `CustomNamespace2`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Resource": "*",
 "Action": "cloudwatch:PutMetricData"
 },
 {
 "Effect": "Deny",
 "Resource": "*",
 "Action": "cloudwatch:PutMetricData",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "CustomNamespace2"
 }
 }
 }
 ]
}`

```
