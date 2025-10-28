# Route 53 health check execution block sample policy

The following is a sample policy to attach if you add execution blocks to a Region switch plan for Route 53 health checks.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "route53:ListResourceRecordSets"
 ],
 "Resource": [
 "arn:aws:route53:::hostedzone/Z1234567890ABCDEFGHIJ"
 ]
 }
 ]
}`

```
