# Resource: Deny action when any

condition keys match strings

The following policy denies access to the [RegisterJobDefinition](../APIReference/API_RegisterJobDefinition.md "../APIReference/API_RegisterJobDefinition.md") API operation when either the
`batch:Image` (container image ID) condition key is
"`string1`" or the `batch:LogDriver` (container
log driver) condition key is "`string2`." When a job spans
multiple containers such as a multi-node parallel job, it's possible for the containers
to have different configurations. If multiple condition keys are evaluated in one
statement, they're combined using `AND` logic. So, if any of the multiple
condition keys doesn't match for a container, the `Deny` effect isn't applied
for that container. Rather, a different container in the same job might be
denied.

For the list of condition keys for AWS Batch, see [Condition keys for AWS Batch](../../../service-authorization/latest/reference/list_awsbatch.md#awsbatch-policy-keys "../../../service-authorization/latest/reference/list_awsbatch.md#awsbatch-policy-keys") in the _Service Authorization Reference_.
Except for `batch:ShareIdentifier`, all `batch` condition keys can
be used in this way. (The `batch:ShareIdentifier` condition key is
defined for a job, not a job definition.)

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "batch:RegisterJobDefinition"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "batch:RegisterJobDefinition"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "batch:Image": [
 "`string1`"
 ]
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "batch:RegisterJobDefinition"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "batch:LogDriver": [
 "`string2`"
 ]
 }
 }
 }
 ]
}`

```
