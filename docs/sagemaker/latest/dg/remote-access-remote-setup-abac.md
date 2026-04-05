# Advanced access control

Amazon SageMaker AI supports [attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") to achieve fine-grained access
control for remote Visual Studio Code connections using ABAC policies. The following are
example ABAC policies for remote VS Code connections.

###### Topics

- [Remote access enforcement](#remote-access-remote-setup-abac-remote-access-enforcement "#remote-access-remote-setup-abac-remote-access-enforcement")
- [Tag-based access control](#remote-access-remote-setup-abac-tag-based-access-control "#remote-access-remote-setup-abac-tag-based-access-control")

## Remote access enforcement

Control access to resources using the `sagemaker:RemoteAccess`
condition key. This is supported by both `CreateSpace` and
`UpdateSpace` APIs. The following example uses
`CreateSpace`.

You can ensure that users cannot create spaces with remote access enabled.
This helps maintain security by defaulting to more restricted access settings.
The following policy ensures users can:

- Create new Studio spaces where remote access is explicitly
  disabled
- Create new Studio spaces without specifying any remote access
  settings

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyCreateSpaceRemoteAccessEnabled",
 "Effect": "Deny",
 "Action": [
 "sagemaker:CreateSpace",
 "sagemaker:UpdateSpace"
 ],
 "Resource": "arn:aws:sagemaker:*:*:space/*",
 "Condition": {
 "StringEquals": {
 "sagemaker:RemoteAccess": [
 "ENABLED"
 ]
 }
 }
 },
 {
 "Sid": "AllowCreateSpace",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateSpace",
 "sagemaker:UpdateSpace"
 ],
 "Resource": "arn:aws:sagemaker:*:*:space/*"
 }
 ]
}`

```

## Tag-based access control

Implement [tag-based](../../../whitepapers/latest/tagging-best-practices/what-are-tags.md "../../../whitepapers/latest/tagging-best-practices/what-are-tags.md") access control to restrict connections based on resource
and principal tags.

You can ensure users can only access resources appropriate for their role and
project assignments. You can use the following policy to:

- Allow users to connect only to spaces that match their assigned team,
  environment, and cost center
- Implement fine-grained access control based on organizational
  structure

In the following example, the space is tagged with the following:

```
{ "Team": "ML", "Environment": "Production", "CostCenter": "12345" }
```

You can have a role that contains the following policy to match resource and
principal tags:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RestrictStartSessionOnTaggedSpacesInDomain",
 "Effect": "Allow",
 "Action": [
 "sagemaker:StartSession"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`111122223333`:space/`domain-id`/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Team": "${aws:PrincipalTag/Team}",
 "aws:ResourceTag/Environment": "${aws:PrincipalTag/Environment}",
 "aws:ResourceTag/CostCenter": "${aws:PrincipalTag/CostCenter}",
 "aws:ResourceTag/IDC_UserName": "${aws:PrincipalTag/IDC_UserName}"
 }
 }
 }
 ]
}`

```

When the role’s tags match, the user has permission to start the session and
remotely connect to their space. See [Control access to AWS
resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") for more information.
