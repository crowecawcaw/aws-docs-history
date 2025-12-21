# Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts

The following code example shows how to This permission-based policy grant full access to Compute Optimizer Automation for standalone AWS accounts

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aco-automation:*",
 "ec2:DescribeVolumes"
 ],
 "Resource": "*"
 }
 ]
}`

```

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
