# Amazon ECS Example policies

You can use IAM policies to grant users permissions to view and work with specific
resources in the Amazon ECS console. You can use the example policies in the previous section;
however, they are designed for requests that are made with the AWS CLI or an AWS SDK.

## Example: Allow users to delete an Amazon ECS cluster based on

tags

The following policy allows users to delete clusters when the tag has a key/value pair
of "Purpose/Testing".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ecs:DeleteCluster"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:ecs:us-east-1:`111122223333`:cluster/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Purpose": "Testing"
 }
 }
 }
 ]
}`

```
