# Resource-based

policy examples for AWS Network Firewall

The Network Firewall service supports only one type of resource-based policy called a _resource policy_, which is attached
to a shared firewall policy or rule group. This policy defines which principals can share firewall policies and rule groups between accounts.

To learn how to attach a resource policy to a
shared rule group or firewall policy, see [Sharing AWS Network Firewall resources](sharing.md "sharing.md").

###### Topics

- [Enable sharing of a firewall policy with an account](#security_iam_resource-based-policy-examples-put-resource-policy "#security_iam_resource-based-policy-examples-put-resource-policy")

## Enable sharing of a firewall policy with an account

The following example grants permissions to the service principal to create or update a resource policy for a firewall policy that's shared across accounts. In the resource policy, you specify the accounts that you want to share the resource with and the operations that you want the accounts to be able to perform.

For information about sharing resources in Network Firewall, see [Sharing AWS Network Firewall resources](sharing.md "sharing.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "`123456789012`"
 },
 "Action": [
 "network-firewall:AssociateFirewallPolicy",
 "network-firewall:ListFirewallPolicies"
 ],
 "Resource": "arn:aws:network-firewall:`us-east-1`:`123456789012`:firewall-policy/`test-action`"
 }
 ]
}`

```
