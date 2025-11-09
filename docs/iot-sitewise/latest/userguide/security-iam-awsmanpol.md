# AWS managed policies for AWS IoT SiteWise

Simplify adding permissions to users, groups, and roles using AWS managed policies
rather than to writing policies yourself. It takes time and expertise to [create IAM customer managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team precise
permissions. For a faster setup, consider using our AWS managed policies for common use
cases. Find AWS managed policies in your AWS account. For more information about AWS
managed policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services take care of updating and maintaining AWS managed policies, meaning you cannot
modify these policies' permissions. Occasionally, AWS IoT SiteWise may add permissions to accommodate new
features, impacting all identities with the policy attached. Such updates are common with
the introduction of new services or features. However, permissions are never removed,
ensuring your setups remain intact.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service
launches a new feature, AWS adds read-only permissions for new operations and resources.
For a list with descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed

policy: AWSIoTSiteWiseReadOnlyAccess

Use the `AWSIoTSiteWiseReadOnlyAccess` AWS managed policy to allow
read-only access to AWS IoT SiteWise.

You can attach the `AWSIoTSiteWiseReadOnlyAccess` policy to your IAM
identities.

**Service-level permissions**

This policy provides read-only access to AWS IoT SiteWise, including permissions to execute
read-only SQL queries. No other service permissions are included in this policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:BatchGetAssetPropertyAggregates",
 "iotsitewise:BatchGetAssetPropertyValue",
 "iotsitewise:BatchGetAssetPropertyValueHistory",
 "iotsitewise:DescribeAccessPolicy",
 "iotsitewise:DescribeAction",
 "iotsitewise:DescribeAsset",
 "iotsitewise:DescribeAssetCompositeModel",
 "iotsitewise:DescribeAssetModel",
 "iotsitewise:DescribeAssetModelCompositeModel",
 "iotsitewise:DescribeAssetModelInterfaceRelationship",
 "iotsitewise:DescribeAssetProperty",
 "iotsitewise:DescribeBulkImportJob",
 "iotsitewise:DescribeComputationModel",
 "iotsitewise:DescribeComputationModelExecutionSummary",
 "iotsitewise:DescribeDashboard",
 "iotsitewise:DescribeDataset",
 "iotsitewise:DescribeDefaultEncryptionConfiguration",
 "iotsitewise:DescribeExecution",
 "iotsitewise:DescribeGateway",
 "iotsitewise:DescribeGatewayCapabilityConfiguration",
 "iotsitewise:DescribeLoggingOptions",
 "iotsitewise:DescribePortal",
 "iotsitewise:DescribeProject",
 "iotsitewise:DescribeStorageConfiguration",
 "iotsitewise:DescribeTimeSeries",
 "iotsitewise:GetAssetPropertyAggregates",
 "iotsitewise:GetAssetPropertyValue",
 "iotsitewise:GetAssetPropertyValueHistory",
 "iotsitewise:GetInterpolatedAssetPropertyValues",
 "iotsitewise:ListAccessPolicies",
 "iotsitewise:ListActions",
 "iotsitewise:ListAssetModelCompositeModels",
 "iotsitewise:ListAssetModelProperties",
 "iotsitewise:ListAssetModels",
 "iotsitewise:ListAssetProperties",
 "iotsitewise:ListAssetRelationships",
 "iotsitewise:ListAssets",
 "iotsitewise:ListAssociatedAssets",
 "iotsitewise:ListBulkImportJobs",
 "iotsitewise:ListCompositionRelationships",
 "iotsitewise:ListComputationModelDataBindingUsages",
 "iotsitewise:ListComputationModelResolveToResources",
 "iotsitewise:ListComputationModels",
 "iotsitewise:ListDashboards",
 "iotsitewise:ListDatasets",
 "iotsitewise:ListExecutions",
 "iotsitewise:ListGateways",
 "iotsitewise:ListInterfaceRelationships",
 "iotsitewise:ListPortals",
 "iotsitewise:ListProjectAssets",
 "iotsitewise:ListProjects",
 "iotsitewise:ListTagsForResource",
 "iotsitewise:ListTimeSeries"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed

policy: AWSServiceRoleForIoTSiteWise

The `AWSServiceRoleForIoTSiteWise` role uses the `AWSServiceRoleForIoTSiteWise` policy with the
following permissions. This policy:

- Allows AWS IoT SiteWise to deploy SiteWise Edge gateways (which run on
  `AWS IoT Greengrass`).
- Allows AWS IoT SiteWise to perform logging.
- Allows AWS IoT SiteWise to run a metadata search query, against
  the AWS IoT TwinMaker database.

If you are using AWS IoT SiteWise with a singe user account,the `AWSServiceRoleForIoTSiteWise` role
creates the `AWSServiceRoleForIoTSiteWise` policy in your IAM account, and attaches it to the
`AWSServiceRoleForIoTSiteWise`
[Service-linked roles for
AWS IoT SiteWise](using-service-linked-roles.md "using-service-linked-roles.md").

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

## AWS IoT SiteWise updates to AWS managed

policies

You can view details about updates to AWS managed policies for AWS IoT SiteWise, beginning
from when this service began tracking the changes. For automatic alerts about changes to
this page, subscribe to the RSS feed on the AWS IoT SiteWise Document history page.

| Change                                                                                                                                                                        | Description                                                                                               | Date               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSServiceRoleForIoTSiteWise](#security-iam-awsmanpol-AWSServiceRoleForIoTSiteWise "#security-iam-awsmanpol-AWSServiceRoleForIoTSiteWise") – Update to an existing policy    | AWS IoT SiteWise now can run a metadata search query, against the AWS IoT TwinMaker<br>database.          | November 6, 2023   |
| [AWSIoTSiteWiseReadOnlyAccess](#security-iam-awsmanpol-AWSIoTSiteWiseReadOnlyAccess "#security-iam-awsmanpol-AWSIoTSiteWiseReadOnlyAccess") – Update to an<br>existing policy | AWS IoT SiteWise added a new policy prefix, `BatchGet*`, that<br>enables you to do batch read operations. | September 16, 2022 |
| [AWSIoTSiteWiseReadOnlyAccess](#security-iam-awsmanpol-AWSIoTSiteWiseReadOnlyAccess "#security-iam-awsmanpol-AWSIoTSiteWiseReadOnlyAccess") – New policy                      | AWS IoT SiteWise added a new policy to grant read-only access to<br>AWS IoT SiteWise.                     | November 24, 2021  |
| AWS IoT SiteWise started tracking changes                                                                                                                                     | AWS IoT SiteWise started tracking changes for its AWS managed<br>policies.                                | November 24, 2021  |
