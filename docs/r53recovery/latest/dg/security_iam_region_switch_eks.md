# Amazon EKS resource scaling execution block sample policy

The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon EKS resource scaling.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "eks:DescribeCluster"
 ],
 "Resource": [
 "arn:aws:eks:us-east-1:123456789012:cluster/app-eks-primary",
 "arn:aws:eks:us-west-2:123456789012:cluster/app-eks-secondary"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "eks:ListAssociatedAccessPolicies"
 ],
 "Resource": [
 "arn:aws:eks:us-east-1:123456789012:access-entry/app-eks-primary/*",
 "arn:aws:eks:us-west-2:123456789012:access-entry/app-eks-secondary/*"
 ]
 }
 ]
}`

```

Note: In addition to this IAM policy, the plan execution role needs to be added to the Amazon EKS cluster's access entries with the
`AmazonArcRegionSwitchScalingPolicy`
access policy. For more information, see [Configure EKS access entry permissions](eks-resource-scaling-block.md#eks-resource-scaling-block-permissions "eks-resource-scaling-block.md#eks-resource-scaling-block-permissions").
