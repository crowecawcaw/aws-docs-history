# Single-valued

context key policy examples

The following set of policy examples demonstrate how to create policy conditions with
single-valued context keys.

## Example:

Multiple condition blocks with single-valued context keys

When a condition block has multiple conditions, each with a single context key, all
context keys must resolve to true for the desired `Allow` or `Deny`
effect to be invoked. When you use negated matching condition operators, the evaluation logic
of the condition value is reversed.

The following example lets users create EC2 volumes and apply tags to the volumes during
volume creation. The request context must include a value for context key
`aws:RequestTag/project`, and the value for context key
`aws:ResourceTag/environment` can be anything except production.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:CreateVolume",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:us-east-1:123456789012:volume/*",
 "Condition": {
 "StringLike": {
 "aws:RequestTag/project": "*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:us-east-1:123456789012:*/*",
 "Condition": {
 "StringNotEquals": {
 "aws:ResourceTag/environment": "production"
 }
 }
 }
 ]
}`

```

The request context must include a project tag-value and cannot be created for a
production resource to invoke the `Allow` effect. The following EC2 volume is
successfully created because the project name is `Feature3` with a `QA`
resource tag.

```
aws ec2 create-volume \
    --availability-zone us-east-1a \
    --volume-type gp2 \
    --size 80 \
    --tag-specifications 'ResourceType=volume,Tags=[{Key=project,Value=Feature3},{Key=environment,Value=QA}]'
```

## Example:

One condition block with multiple single-valued context keys and values

When a condition block contains multiple context keys and each context key has multiple
values, each context key must resolve to true for at least one key value for the desired
`Allow` or `Deny` effect to be invoked. When you use negated matching
condition operators, the evaluation logic of the context key value is reversed.

The following example allows users to start and run tasks on Amazon Elastic Container Service clusters.

- The request context must include `production`
  **OR**
  `prod-backup` for the `aws:RequestTag/environment` context key
  **AND**.
- The `ecs:cluster` context key makes sure that tasks are run on either the
  `default1`
  **OR**
  `default2` ARN ECS clusters.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:RunTask",
 "ecs:StartTask"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": [
 "production",
 "prod-backup"
 ]
 },
 "ArnEquals": {
 "ecs:cluster": [
 "arn:aws:ecs:us-east-1:`111122223333`:cluster/default1",
 "arn:aws:ecs:us-east-1:`111122223333`:cluster/default2"
 ]
 }
 }
 }
 ]
}`

```

The following table shows how AWS evaluates this policy based on the condition key
values in your request.

| Policy condition                                                                                                                                                                                                                      | Request context                                                                                               | Result   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------- |
| `"StringEquals": { "aws:RequestTag/environment": [ "production", "prod-backup" ] }, "ArnEquals": { "ecs:cluster": [ "arn:aws:ecs:us-east-1:111122223333:cluster/default1", "arn:aws:ecs:us-east-1:111122223333:cluster/default2" ] }` | `aws:RequestTag: environment:production ecs:cluster: arn:aws:ecs:us-east-1:111122223333:cluster/default1`     | Match    |
| `"StringEquals": { "aws:RequestTag/environment": [ "production", "prod-backup" ] }, "ArnEquals": { "ecs:cluster": [ "arn:aws:ecs:us-east-1:111122223333:cluster/default1", "arn:aws:ecs:us-east-1:111122223333:cluster/default2" ] }` | `aws:RequestTag: environment:prod-backup ecs:cluster: arn:aws:ecs:us-east-1:111122223333:cluster/default2`    | Match    |
| `"StringEquals": { "aws:RequestTag/environment": [ "production", "prod-backup" ] }, "ArnEquals": { "ecs:cluster": [ "arn:aws:ecs:us-east-1:111122223333:cluster/default1", "arn:aws:ecs:us-east-1:111122223333:cluster/default2" ] }` | `aws:RequestTag: webserver:production ecs:cluster: arn:aws:ecs:us-east-1:111122223333:cluster/default2`       | No match |
| `"StringEquals": { "aws:RequestTag/environment": [ "production", "prod-backup" ] }, "ArnEquals": { "ecs:cluster": [ "arn:aws:ecs:us-east-1:111122223333:cluster/default1", "arn:aws:ecs:us-east-1:111122223333:cluster/default2" ] }` | No `aws:RequestTag` in the request context. `ecs:cluster arn:aws:ecs:us-east-1:111122223333:cluster/default2` | No match |
