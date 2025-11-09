AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configuring permissions for Compliance

As a security best practice, we recommend that you update the AWS Identity and Access Management (IAM) role
used by your managed nodes with the following permissions to restrict the node's ability
to use the [PutComplianceItems](../APIReference/API_PutComplianceItems.md "../APIReference/API_PutComplianceItems.md") API action. This API action registers a compliance type
and other compliance details on a designated resource, such as an Amazon EC2 instance or a
managed node.

If your node is an Amazon EC2 instance, you must update the IAM instance profile used by
the instance with the following permissions. For more information about instance
profiles for EC2 instance managed by Systems Manager, see [Configure instance permissions required for
Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").
For other types of managed nodes, update the IAM role used by the node with the
following permissions. For more information, see [Update permissions
for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:PutComplianceItems"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ec2:SourceInstanceARN": "${ec2:SourceInstanceARN}"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:PutComplianceItems"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ssm:SourceInstanceARN": "${ssm:SourceInstanceARN}"
 }
 }
 }
 ]
}`

```
