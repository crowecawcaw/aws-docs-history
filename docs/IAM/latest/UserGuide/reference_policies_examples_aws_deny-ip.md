# AWS: Denies access to AWS based on

the source IP

This example shows how you might create an identity-based policy that denies access to all AWS actions in the account when the request
comes from _principals_ outside the specified IP range. The
policy is useful when the IP addresses for your company are within the specified ranges. In this
example, the request will be denied unless it originates from the CIDR range 192.0.2.0/24 or
203.0.113.0/24. The policy does not deny requests made by AWS services using [Forward access sessions](access_forward_access_sessions.md "access_forward_access_sessions.md") as
the original requester’s IP address is preserved.

Be careful using negative conditions in the same policy statement as `"Effect":
 "Deny"`. When you do, the actions specified in the policy statement are explicitly
denied in all conditions _except_ for the ones
specified.

###### Important

This policy does not allow any actions. Use this policy in combination with other policies
that allow specific actions.

When other policies allow actions, principals can make requests from within the IP address
range. An AWS service can also make requests using the principal's credentials. When a
principal makes a request from outside the IP range, the request is denied.

For more information about using the `aws:SourceIp` condition key, including
information about when `aws:SourceIp` may not work in your policy, see [AWS global condition context
keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "NotIpAddress": {
 "aws:SourceIp": [
 "`192.0.2.0/24`",
 "`203.0.113.0/24`"
 ]
 }
 }
 }
}`

```
