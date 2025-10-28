# Permissions and

examples for AWS CodeConnections

The following policy statements and examples can help you manage AWS CodeConnections.

For information about how to create an IAM identity-based policy using these
example JSON policy documents, see [Creating policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

## Example: A policy for creating AWS CodeConnections with the CLI and viewing with the

console

A role or user designated to use the AWS CLI or SDK to view, create, tag, or
delete connections should have permissions limited to the following.

###### Note

You cannot complete a connection in the console with only the following
permissions. You need to add the permissions in the next section.

To use the console to view a list of available connections, view tags, and use
a connection, use the following policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConnectionsFullAccess",
 "Effect": "Allow",
 "Action": [
 "codeconnections:CreateConnection",
 "codeconnections:DeleteConnection",
 "codeconnections:UseConnection",
 "codeconnections:GetConnection",
 "codeconnections:ListConnections",
 "codeconnections:TagResource",
 "codeconnections:ListTagsForResource",
 "codeconnections:UntagResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: A policy for creating AWS CodeConnections with the console

A role or user designated to manage connections in the console should have the
permissions required to complete a connection in the console and create an
installation, which includes authorizing the handshake to the provider and
creating installations for connections to use. `UseConnection` should
also be added to use the connection in the console. Use the following policy to
view, use, create, tag, or delete a connection in the console.

###### Note

Beginning July 1, 2024, the console creates connections with `codeconnections` in the resource ARN. Resources with both service prefixes will continue to display in the console.

###### Note

For resources created using the console, policy statement actions must
include `codestar-connections` as the service prefix as shown in
the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codestar-connections:CreateConnection",
 "codestar-connections:DeleteConnection",
 "codestar-connections:GetConnection",
 "codestar-connections:ListConnections",
 "codestar-connections:GetInstallationUrl",
 "codestar-connections:GetIndividualAccessToken",
 "codestar-connections:ListInstallationTargets",
 "codestar-connections:StartOAuthHandshake",
 "codestar-connections:UpdateConnectionInstallation",
 "codestar-connections:UseConnection",
 "codestar-connections:TagResource",
 "codestar-connections:ListTagsForResource",
 "codestar-connections:UntagResource"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Example: An administrator-level policy for managing AWS CodeConnections

In this example, you want to grant an IAM user in your AWS account full
access to CodeConnections so that the user can add, update, and delete connections. This
is a full access policy, equivalent to the
**AWSCodePipeline_FullAccess** managed policy. Like that
managed policy, you should only attach this kind of policy statement to IAM
users, groups, or roles that require full administrative access to connections
across your AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConnectionsFullAccess",
 "Effect": "Allow",
 "Action": [
 "codeconnections:CreateConnection",
 "codeconnections:DeleteConnection",
 "codeconnections:UseConnection",
 "codeconnections:GetConnection",
 "codeconnections:ListConnections",
 "codeconnections:ListInstallationTargets",
 "codeconnections:GetInstallationUrl",
 "codeconnections:StartOAuthHandshake",
 "codeconnections:UpdateConnectionInstallation",
 "codeconnections:GetIndividualAccessToken",
 "codeconnections:TagResource",
 "codeconnections:ListTagsForResource",
 "codeconnections:UntagResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: A contributor-level policy for using AWS CodeConnections

In this example, you want to grant access to the day-to-day usage of CodeConnections,
such as creating and viewing details of connections, but not to more destructive
actions, such as deleting connections.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSCodeConnectionsPowerUserAccess",
 "Effect": "Allow",
 "Action": [
 "codeconnections:CreateConnection",
 "codeconnections:UseConnection",
 "codeconnections:GetConnection",
 "codeconnections:ListConnections",
 "codeconnections:ListInstallationTargets",
 "codeconnections:GetInstallationUrl",
 "codeconnections:GetIndividualAccessToken",
 "codeconnections:StartOAuthHandshake",
 "codeconnections:UpdateConnectionInstallation",
 "codeconnections:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: A read-only-level policy for using AWS CodeConnections

In this example, you want to grant an IAM user in your account read-only
access to the connections in your AWS account. This example shows how you
might create a policy that allows viewing these items.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "ConnectionsforReadOnly",
 "Statement": [
 {
 "Sid": "ReadsAPIAccess",
 "Effect": "Allow",
 "Action": [
 "codeconnections:GetConnection",
 "codeconnections:ListConnections",
 "codeconnections:ListInstallationTargets",
 "codeconnections:GetInstallationUrl",
 "codeconnections:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example:

Limit host VPC permissions using the **VpcId**
context key

In the following example, the customer can use the **VpcId** context key to limit creation or management of hosts to
hosts with specified VPC.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "codeconnections:CreateHost",
 "codeconnections:UpdateHost"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "codeconnections:VpcId": "vpc-EXAMPLE"
 }
 }
 }
 ]
}`

```
