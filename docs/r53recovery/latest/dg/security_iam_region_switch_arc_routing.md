# ARC routing controls execution block sample policy

Note: The Amazon ARC routing controls execution block requires that any service control policies (SCPs)
applied to the plan's execution role allow the access to the following Regions for these services:

- `route53-recovery-control-config: us-west-2`
- `route53-recovery-cluster: us-west-2, us-east-1, eu-west-1, ap-southeast-2, ap-northeast-1`
  The following is a sample policy to attach if you add execution blocks to a Region switch plan for ARC routing controls.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "route53-recovery-control-config:DescribeControlPanel",
 "route53-recovery-control-config:DescribeCluster"
 ],
 "Resource": [
 "arn:aws:route53-recovery-control::123456789012:controlpanel/abcd1234abcd1234abcd1234abcd1234",
 "arn:aws:route53-recovery-control::123456789012:cluster/4b325d3b-0e28-4dcf-ba4a-EXAMPLE11111"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "route53-recovery-cluster:GetRoutingControlState",
 "route53-recovery-cluster:UpdateRoutingControlStates"
 ],
 "Resource": [
 "arn:aws:route53-recovery-control::123456789012:controlpanel/1234567890abcdef1234567890abcdef/routingcontrol/abcdef1234567890",
 "arn:aws:route53-recovery-control::123456789012:controlpanel/1234567890abcdef1234567890abcdef/routingcontrol/1234567890abcdef"
 ]
 }
 ]
}`

```

You can retrieve the routing control control panel ID and the cluster ID by using CLI. For more information, see
[Set up routing control components](getting-started-cli-routing-config.md "getting-started-cli-routing-config.md").
