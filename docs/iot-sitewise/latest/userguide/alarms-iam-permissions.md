# Set up permissions for event alarms in AWS IoT SiteWise

When you use an AWS IoT Events alarm model to monitor an AWS IoT SiteWise asset property, you must have the following IAM permissions:

- An AWS IoT Events service role that allows AWS IoT Events to send data to AWS IoT SiteWise. For more information,
  see [Identity and access management for AWS IoT Events](../../../iotevents/latest/developerguide/security-iam.md "../../../iotevents/latest/developerguide/security-iam.md")
  in the _AWS IoT Events Developer Guide_.
- You must have the following AWS IoT SiteWise action permissions: `iotsitewise:DescribeAssetModel` and `iotsitewise:UpdateAssetModelPropertyRouting`.
  These permissions allow AWS IoT SiteWise to send asset property values to AWS IoT Events alarm models.
  For more information, see [Resource-based policies](../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based "../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based")
  in the _IAM User Guide_.

## Required action permissions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal**
can perform **actions** on what **resources**, and under what **conditions**.
The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy.

Before you define an AWS IoT Events alarm model, you must grant the following permissions that allow AWS IoT SiteWise to send asset property values to the alarm model.

- `iotsitewise:DescribeAssetModel`, `iotsitewise:ListAssetModels` – Allows AWS IoT Events to check if an asset property exists.
- `iotsitewise:UpdateAssetModelPropertyRouting` – Allows AWS IoT SiteWise to automatically create subscriptions that enable AWS IoT SiteWise to send data to AWS IoT Events.

For more information about AWS IoT SiteWise supported actions,
see [Actions defined by AWS IoT SiteWise](../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions "../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions") in the _Service Authorization Reference_.

###### Example permissions policy 1

The following policy allows AWS IoT SiteWise to send asset property values to any AWS IoT Events alarm models.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotevents:CreateAlarmModel",
 "iotevents:UpdateAlarmModel"
 ],
 "Resource": "arn:aws:iotevents:`us-east-1`:123456789012:alarmModel/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:DescribeAssetModel",
 "iotsitewise:ListAssetModels",
 "iotsitewise:UpdateAssetModelPropertyRouting"
 ],
 "Resource": "arn:aws:iotsitewise:`us-east-1`:123456789012:asset-model/*"
 }
 ]
}`

```

###### Example permissions policy 2

The following policy allows AWS IoT SiteWise to send values of a specified asset property to a specified AWS IoT Events alarm model.

JSON

```


```

## (Optional) ListInputRoutings permission

When you update or delete an asset model, AWS IoT SiteWise can check if an alarm model in AWS IoT Events
is monitoring an asset property associated with this asset model. This prevents you from deleting an asset property
that an AWS IoT Events alarm is currently using. To enable this feature in AWS IoT SiteWise, you must have the `iotevents:ListInputRoutings` permission.
This permission allows AWS IoT SiteWise to make calls to the [ListInputRoutings](../../../iotevents/latest/apireference/API_ListInputRoutings.md "../../../iotevents/latest/apireference/API_ListInputRoutings.md") API operation supported by AWS IoT Events.

###### Note

We strongly recommend that you add the `ListInputRoutings` permission.

###### Example permissions policy

The following policy allows you to update and delete asset models, and use the `ListInputRoutings` API in AWS IoT SiteWise.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:UpdateAssetModel",
 "iotsitewise:DeleteAssetModel",
 "`iotevents:ListInputRoutings`"
 ],
 "Resource": "arn:aws:iotsitewise:`us-east-1`:123456789012:asset-model/*"
 }
 ]
}`

```

## Required permissions for SiteWise Monitor

If you want to use the alarms feature in SiteWise Monitor portals, you must update the [SiteWise Monitor service role](monitor-service-role.md "monitor-service-role.md") with the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:DescribePortal",
 "iotsitewise:CreateProject",
 "iotsitewise:DescribeProject",
 "iotsitewise:UpdateProject",
 "iotsitewise:DeleteProject",
 "iotsitewise:ListProjects",
 "iotsitewise:BatchAssociateProjectAssets",
 "iotsitewise:BatchDisassociateProjectAssets",
 "iotsitewise:ListProjectAssets",
 "iotsitewise:CreateDashboard",
 "iotsitewise:DescribeDashboard",
 "iotsitewise:UpdateDashboard",
 "iotsitewise:DeleteDashboard",
 "iotsitewise:ListDashboards",
 "iotsitewise:CreateAccessPolicy",
 "iotsitewise:DescribeAccessPolicy",
 "iotsitewise:UpdateAccessPolicy",
 "iotsitewise:DeleteAccessPolicy",
 "iotsitewise:ListAccessPolicies",
 "iotsitewise:DescribeAsset",
 "iotsitewise:ListAssets",
 "iotsitewise:ListAssociatedAssets",
 "iotsitewise:DescribeAssetProperty",
 "iotsitewise:GetAssetPropertyValue",
 "iotsitewise:GetAssetPropertyValueHistory",
 "iotsitewise:GetAssetPropertyAggregates",
 "iotsitewise:BatchPutAssetPropertyValue",
 "iotsitewise:ListAssetRelationships",
 "iotsitewise:DescribeAssetModel",
 "iotsitewise:ListAssetModels",
 "iotsitewise:UpdateAssetModel",
 "iotsitewise:UpdateAssetModelPropertyRouting",
 "sso-directory:DescribeUsers",
 "sso-directory:DescribeUser",
 "iotevents:DescribeAlarmModel",
 "iotevents:ListTagsForResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotevents:BatchAcknowledgeAlarm",
 "iotevents:BatchSnoozeAlarm",
 "iotevents:BatchEnableAlarm",
 "iotevents:BatchDisableAlarm"
 ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "iotevents:keyValue": "false"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotevents:CreateAlarmModel",
 "iotevents:TagResource"
 ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "aws:RequestTag/iotsitewisemonitor": "false"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotevents:UpdateAlarmModel",
 "iotevents:DeleteAlarmModel"
 ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "aws:ResourceTag/iotsitewisemonitor": "false"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "iotevents.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```
