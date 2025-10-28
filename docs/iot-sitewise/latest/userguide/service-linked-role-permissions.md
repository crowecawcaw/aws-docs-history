# Service-linked role permissions for

AWS IoT SiteWise

AWS IoT SiteWise uses the service-linked role named **AWSServiceRoleForIoTSiteWise**.
AWS IoT SiteWise uses this service-linked role to deploy SiteWise Edge gateways (which run on AWS IoT Greengrass) and perform logging.

The `AWSServiceRoleForIoTSiteWise` service-linked role uses the `AWSServiceRoleForIoTSiteWise` policy
with the following permissions. This policy:

- Allows AWS IoT SiteWise to deploy SiteWise Edge gateways (which run on `AWS IoT Greengrass`).
- Allows AWS IoT SiteWise to perform logging.
- Allows AWS IoT SiteWise to run a metadata search query, against the AWS IoT TwinMaker database.
  For more information on the allowed actions in `AWSServiceRoleForIoTSiteWise`, see [AWS managed policies for
  AWS IoT SiteWise](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForIoTSiteWise "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForIoTSiteWise").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSiteWiseReadGreenGrass",
 "Effect": "Allow",
 "Action": [
 "greengrass:GetAssociatedRole",
 "greengrass:GetCoreDefinition",
 "greengrass:GetCoreDefinitionVersion",
 "greengrass:GetGroup",
 "greengrass:GetGroupVersion"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSiteWiseAccessLogGroup",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:DescribeLogGroups"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/iotsitewise*"
 },
 {
 "Sid": "AllowSiteWiseAccessLog",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/iotsitewise*:log-stream:*"
 },
 {
 "Sid": "AllowSiteWiseAccessSiteWiseManagedWorkspaceInTwinMaker",
 "Effect": "Allow",
 "Action": [
 "iottwinmaker:GetWorkspace",
 "iottwinmaker:ExecuteQuery"
 ],
 "Resource": "arn:aws:iottwinmaker:*:*:workspace/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "iottwinmaker:linkedServices": [
 "IOTSITEWISE"
 ]
 }
 }
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSiteWiseReadGreenGrass",
 "Effect": "Allow",
 "Action": [
 "greengrass:GetAssociatedRole",
 "greengrass:GetCoreDefinition",
 "greengrass:GetCoreDefinitionVersion",
 "greengrass:GetGroup",
 "greengrass:GetGroupVersion"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSiteWiseAccessLogGroup",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:DescribeLogGroups"
 ],
 "Resource": "arn:aws-us-gov:logs:*:*:log-group:/aws/iotsitewise*"
 },
 {
 "Sid": "AllowSiteWiseAccessLog",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws-us-gov:logs:*:*:log-group:/aws/iotsitewise*:log-stream:*"
 },
 {
 "Sid": "AllowSiteWiseAccessSiteWiseManagedWorkspaceInTwinMaker",
 "Effect": "Allow",
 "Action": [
 "iottwinmaker:GetWorkspace",
 "iottwinmaker:ExecuteQuery"
 ],
 "Resource": "arn:aws-us-gov:iottwinmaker:*:*:workspace/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "iottwinmaker:linkedServices": [
 "IOTSITEWISE"
 ]
 }
 }
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSiteWiseReadGreenGrass",
 "Effect": "Allow",
 "Action": [
 "greengrass:GetAssociatedRole",
 "greengrass:GetCoreDefinition",
 "greengrass:GetCoreDefinitionVersion",
 "greengrass:GetGroup",
 "greengrass:GetGroupVersion"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSiteWiseAccessLogGroup",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:DescribeLogGroups"
 ],
 "Resource": "arn:aws-cn:logs:*:*:log-group:/aws/iotsitewise*"
 },
 {
 "Sid": "AllowSiteWiseAccessLog",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws-cn:logs:*:*:log-group:/aws/iotsitewise*:log-stream:*"
 },
 {
 "Sid": "AllowSiteWiseAccessSiteWiseManagedWorkspaceInTwinMaker",
 "Effect": "Allow",
 "Action": [
 "iottwinmaker:GetWorkspace",
 "iottwinmaker:ExecuteQuery"
 ],
 "Resource": "arn:aws-cn:iottwinmaker:*:*:workspace/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "iottwinmaker:linkedServices": [
 "IOTSITEWISE"
 ]
 }
 }
 }
 ]
}`

```

You can use the logs to monitor and troubleshoot your SiteWise Edge gateways. For more
information, see [Monitor SiteWise Edge gateway logs](monitor-gateway-logs.md "monitor-gateway-logs.md").

To allow an IAM entity (such as a user, group, or role) to create, edit, or delete a
service-linked role, first configure permissions. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the
_IAM User Guide_.
