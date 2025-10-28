# Prevent AWS Secrets Manager replication

Because secrets can be replicated using [`ReplicateSecretToRegions`](../apireference/API_ReplicateSecretToRegions.md "../apireference/API_ReplicateSecretToRegions.md") or when they are created using [`CreateSecret`](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md"), if you want to prevent users from replicating secrets, we recommend you prevent actions that contain the `AddReplicaRegions` parameter. You can use a `Condition` statement in your permission policies to only allow actions that don't add replica regions. See the following policy examples for Condition statements you can use.

###### Example Prevent replication permission

The following policy example shows how to allow all actions that don't add replica regions. This prevents users from replicating secrets through both `ReplicateSecretToRegions` and `CreateSecret`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "secretsmanager:*",
 "Resource": "*",
 "Condition": {
 "Null": {
 "secretsmanager:AddReplicaRegions": "true"
 }
 }
 }
 ]
}`

```

###### Example Allow replication permission only to specific Regions

The following policy shows how to allow all of the following:

- Create secrets without replication
- Create secrets with replication to Regions only in United States and Canada
- Replicate secrets to Regions only in United States and Canada

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:CreateSecret",
 "secretsmanager:ReplicateSecretToRegions"
 ],
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringLike": {
 "secretsmanager:AddReplicaRegions": [
 "us-*",
 "ca-*"
 ]
 }
 }
 }
 ]
}`

```
