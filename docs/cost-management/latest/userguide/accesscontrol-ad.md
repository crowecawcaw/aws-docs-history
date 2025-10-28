# Controlling access for Cost Anomaly Detection

You can use resource-level access controls and attribute-based access control (ABAC)
tags for cost anomaly monitors and anomaly subscriptions. Each anomaly monitor and
anomaly subscription resource has a unique Amazon Resource Name (ARN). You can also
attach tags (key-value pairs) to each feature. Both resource ARNs and ABAC tags can be
used to give granular access control to user roles or groups within your
AWS accounts.

For more information about resource-level access controls and ABAC tags, see [How AWS Cost Management works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

###### Note

Cost Anomaly Detection doesn't support resource-based policies. Resource-based policies are directly
attached to AWS resources. For more information about the difference between
policies and permissions, see [Identity-based policies and resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") in the
_IAM User Guide_.

## Controlling access using

resource-level policies

You can use resource-level permissions to allow or deny access to one or more Cost Anomaly Detection
resources in an IAM policy. Alternatively, use resource-level permissions to allow
or deny access to all Cost Anomaly Detection resources.

When you create an IAM, use the following Amazon Resource Name (ARN)
formats:

- `AnomalyMonitor` resource ARN

`arn:${partition}:ce::${account-id}:anomalymonitor/${monitor-id}`

- `AnomalySubscription` resource ARN

`arn:${partition}:ce::${account-id}:anomalysubscription/${subscription-id}`

To allow the IAM entity to get and create an anomaly monitor or anomaly
subscription, use a policy similar to this example policy.

###### Note

- For `ce:GetAnomalyMonitor` and
  `ce:GetAnomalySubscription`, users have all or none of
  the resource-level access control. This requires the policy to use a
  generic ARN in the form of
  `arn:${partition}:ce::${account-id}:anomalymonitor/*`,
  `arn:${partition}:ce::${account-id}:anomalysubscription/*`,
  or `*`.
- For `ce:CreateAnomalyMonitor` and
  `ce:CreateAnomalySubscription`, we don't have a resource
  ARN for this resource. So, the policy always uses the generic ARN that
  was mentioned in the previous bullet.
- For `ce:GetAnomalies`, use the optional
  `monitorArn` parameter. When used with this parameter, we
  confirm if the user has access to the `monitorArn`
  passed.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ce:GetAnomalyMonitors",
 "ce:CreateAnomalyMonitor"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:ce::999999999999:anomalymonitor/*"
 },
 {
 "Action": [
 "ce:GetAnomalySubscriptions",
 "ce:CreateAnomalySubscription"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:ce::999999999999:anomalysubscription/*"
 }
 ]
}`

```

To allow the IAM entity to update or delete anomaly monitors, use a policy
similar to this example policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ce:UpdateAnomalyMonitor",
 "ce:DeleteAnomalyMonitor"
 ],
 "Resource": [
 "arn:aws:ce::999999999999:anomalymonitor/f558fa8a-bd3c-462b-974a-000abc12a000",
 "arn:aws:ce::999999999999:anomalymonitor/f111fa8a-bd3c-462b-974a-000abc12a001"
 ]
 }
 ]
}`

```

## Controlling access using tags (ABAC)

You can use tags (ABAC) to control access to Cost Anomaly Detection resources that support tagging.
To control access using tags, provide the tag information in the
`Condition` element of a policy. You can then create an IAM policy
that allows or denies access to a resource based on the resource's tags. You can use
tag condition keys to control access to resources, requests, or any part of the
authorization process. For more information about IAM roles using tags, see [Controlling
access to and for users and roles using tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md") in the
_IAM User Guide_.

Create an identity-based policy that allows updating anomaly monitors. If the
monitor tag `Owner` has the value of the user name, use a policy that's
similar to this example policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ce:UpdateAnomalyMonitor"
 ],
 "Resource": "arn:aws:ce::*:anomalymonitor/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Owner": "${aws:username}"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ce:GetAnomalyMonitors",
 "Resource": "*"
 }
 ]
}`

```
