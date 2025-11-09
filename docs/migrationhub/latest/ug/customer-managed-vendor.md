AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Custom Policies for Migration

Tools when using AWS Migration Hub

This is an example role for use by a integrated partner or developer when using
the AWS Migration Hub API or
CLI.

## Integrated Partner Role

Policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "mgh:CreateProgressUpdateStream"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:mgh:us-west-2:`111122223333`:progressUpdateStream/vendor_name"
 },
 {
 "Action": [
 "mgh:AssociateCreatedArtifact",
 "mgh:DescribeMigrationTask",
 "mgh:DisassociateCreatedArtifact",
 "mgh:ImportMigrationTask",
 "mgh:ListCreatedArtifacts",
 "mgh:NotifyMigrationTaskState",
 "mgh:PutResourceAttributes",
 "mgh:NotifyApplicationState",
 "mgh:DescribeApplicationState",
 "mgh:AssociateDiscoveredResource",
 "mgh:DisassociateDiscoveredResource",
 "mgh:ListDiscoveredResources"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:mgh:us-west-2:`111122223333`:progressUpdateStream/vendor_name/*"
 },
 {
 "Action": [
 "mgh:ListMigrationTasks",
 "mgh:GetHomeRegion"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Integrated Partner Policy Trust

Policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
