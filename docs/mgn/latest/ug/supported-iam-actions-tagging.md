NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Grant permission to tag resources during creation

Some resource-creating Amazon MGN API actions enable you to specify tags when you create
the resource. You can use resource tags to implement attribute-based control (ABAC).

To enable users to tag resources on creation, they must have permissions to use the
action that creates the resource, such as `mgn:RegisterAgentForMgn`. If tags are
specified in the resource-creating action, Amazon performs additional authorization on the
`mgn:TagResource`
action to verify if users have permissions to create tags.
Therefore, users must also have explicit permissions to use the
`mgn:TagResource`
action.

In the IAM policy definition for the `mgn:TagResource` action, use the
Condition element with the `mgn:CreateAction` condition key to give tagging
permissions to the action that creates the resource. The following example demonstrates a
policy that allows an agent installer to create a source server and apply any tags to the
source server on creation. The installer is not permitted to tag any existing resources (it
cannot call the `mgn:TagResource` action directly).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "mgn:SendAgentMetricsForMgn",
 "mgn:SendAgentLogsForMgn",
 "mgn:SendClientMetricsForMgn",
 "mgn:SendClientLogsForMgn"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mgn:RegisterAgentForMgn",
 "mgn:UpdateAgentSourcePropertiesForMgn",
 "mgn:UpdateAgentReplicationInfoForMgn",
 "mgn:UpdateAgentConversionInfoForMgn",
 "mgn:GetAgentInstallationAssetsForMgn",
 "mgn:GetAgentCommandForMgn",
 "mgn:GetAgentConfirmedResumeInfoForMgn",
 "mgn:GetAgentRuntimeConfigurationForMgn",
 "mgn:UpdateAgentBacklogForMgn",
 "mgn:GetAgentReplicationInfoForMgn"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "mgn:TagResource",
 "Resource": "arn:aws:mgn:*:*:source-server/*",
 "Condition": {
 "StringEquals": {
 "mgn:CreateAction": "RegisterAgentForMgn"
 }
 }
 }
 ]
}`

```

The `mgn:TagResource` action is only evaluated if tags are applied during the resource-creating action. Therefore, an
installer that has permissions to create a resource (assuming there are no tagging conditions) does not require permissions to use the `mgn:TagResource` action if no tags are specified in the request. However, if the installer attempts to create a resource with tags, the request
fails if the installer does not have permissions to use the `mgn:TagResource` action.
