# AWS managed policies for AWS IoT TwinMaker

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AWSIoTTwinMakerServiceRolePolicy

You can't attach AWSIoTTwinMakerServiceRolePolicy to your IAM entities. This policy is attached to a
service-linked role that allows to perform actions on your behalf. For more
information, see [Service-linked role permissions for AWS IoT TwinMaker](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions").

The role permissions policy named AWSIoTTwinMakerServiceRolePolicy allows AWS IoT TwinMaker to complete the
following actions on the specified resources:

- Action: `iotsitewise:DescribeAsset, iotsitewise:ListAssets, iotsitewise:DescribeAssetModel, and iotsitewise:ListAssetModels, iottwinmaker:GetEntity, iottwinmaker:CreateEntity, iottwinmaker:UpdateEntity, iottwinmaker:DeleteEntity, iottwinmaker:ListEntities, iottwinmaker:GetComponentType, iottwinmaker:CreateComponentType, iottwinmaker:UpdateComponentType, iottwinmaker:DeleteComponentType, iottwinmaker:ListComponentTypes` on
  `all your iotsitewise asset and asset-model resources`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "SiteWiseAssetReadAccess",
 "Effect": "Allow",
 "Action": [
 "iotsitewise:DescribeAsset"
 ],
 "Resource": [
 "arn:aws:iotsitewise:*:*:asset/*"
 ]
 },
 {
 "Sid": "SiteWiseAssetModelReadAccess",
 "Effect": "Allow",
 "Action": [
 "iotsitewise:DescribeAssetModel"
 ],
 "Resource": [
 "arn:aws:iotsitewise:*:*:asset-model/*"
 ]
 },
 {
 "Sid": "SiteWiseAssetModelAndAssetListAccess",
 "Effect": "Allow",
 "Action": [
 "iotsitewise:ListAssets",
 "iotsitewise:ListAssetModels"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "TwinMakerAccess",
 "Effect": "Allow",
 "Action": [
 "iottwinmaker:GetEntity",
 "iottwinmaker:CreateEntity",
 "iottwinmaker:UpdateEntity",
 "iottwinmaker:DeleteEntity",
 "iottwinmaker:ListEntities",
 "iottwinmaker:GetComponentType",
 "iottwinmaker:CreateComponentType",
 "iottwinmaker:UpdateComponentType",
 "iottwinmaker:DeleteComponentType",
 "iottwinmaker:ListComponentTypes"
 ],
 "Resource": [
 "arn:aws:iottwinmaker:*:*:workspace/*"
 ],
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

## AWS IoT TwinMaker updates to AWS managed

policies

View details about updates to AWS managed policies for since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Document history page.

| Change                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Date              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSIoTTwinMakerServiceRolePolicy](#security-iam-awsmanpol-IoTTwinMakerServiceRolePolicy "#security-iam-awsmanpol-IoTTwinMakerServiceRolePolicy") –<br>Added a policy | AWS IoT TwinMaker added the role permissions policy named AWSIoTTwinMakerServiceRolePolicy<br>which allows AWS IoT TwinMaker to complete the following actions on the specified<br>resources:<br>• Action: `iotsitewise:DescribeAsset, iotsitewise:ListAssets, iotsitewise:DescribeAssetModel, and iotsitewise:ListAssetModels, iottwinmaker:GetEntity, iottwinmaker:CreateEntity, iottwinmaker:UpdateEntity, iottwinmaker:DeleteEntity, iottwinmaker:ListEntities, iottwinmaker:GetComponentType, iottwinmaker:CreateComponentType, iottwinmaker:UpdateComponentType, iottwinmaker:DeleteComponentType, iottwinmaker:ListComponentTypes` on<br>`all your iotsitewise asset and asset-model resources`<br>For more information, see [Service-linked role permissions for AWS IoT TwinMaker](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions"). | November 17, 2023 |
| started tracking changes                                                                                                                                              | started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | May 11, 2022      |
