# Permissions required for viewing Amazon ECS service deployments

When you follow the best practice of granting least privilege, you need to add additional
permissions in order to view service deployments in the console.

You need access to the following actions:

- ListServiceDeployments
- DescribeServiceDeployments
- DescribeServiceRevisions
  You need access to the following resources:

- Service
- Service deployment
- Service revision
  The following example policy contains the required permissions, and limits the actions to a
  specified service.

Replace the `account`, `cluster-name`, and `service-name`
with your values.

JSON

```
`{
"Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:ListServiceDeployments",
 "ecs:DescribeServiceDeployments",
 "ecs:DescribeServiceRevisions"
 ],
 "Resource": [
 "arn:aws:ecs:us-east-1:123456789012:service/cluster-name/service-name",
 "arn:aws:ecs:us-east-1:123456789012:service-deployment/cluster-name/service-name/*",
 "arn:aws:ecs:us-east-1:123456789012:service-revision/cluster-name/service-name/*"
 ]
 }
 ]
}`

```
