# Step 1: Configure required IAM Role permissions

To use VPC Route Server, ensure that the IAM user or role you are using has the
required IAM permissions. Below is a guide to which permissions are required for
each API:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateRouteServer",
 "Effect": "Allow",
 "Action": [
 "sns:CreateTopic"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DeleteRouteServer",
 "Effect": "Allow",
 "Action": [
 "sns:DeleteTopic"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreateRouteServerEndpoint",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:CreateSecurityGroup",
 "ec2:DescribeSecurityGroups",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateTags",
 "ec2:DeleteTags"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DeleteRouteServerEndpoint",
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteSecurityGroup",
 "ec2:RevokeSecurityGroupIngress",
 "ec2:CreateTags",
 "ec2:DeleteTags"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreateRouteServerPeer",
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupIngress"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DeleteRouteServerPeer",
 "Effect": "Allow",
 "Action": [
 "ec2:RevokeSecurityGroupIngress"
 ],
 "Resource": "*"
 }
 ]
}`

```
