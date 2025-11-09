# Use service roles for AWS IoT SiteWise Monitor

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

To allow federated SiteWise Monitor portal users to access your AWS IoT SiteWise and
AWS IAM Identity Center resources, you must attach a service role to each portal that you create.
The service role must specify SiteWise Monitor as a trusted entity and include the [AWSIoTSiteWiseMonitorPortalAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSIoTSiteWiseMonitorPortalAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSIoTSiteWiseMonitorPortalAccess") managed policy or define [equivalent permissions](#monitor-service-role-permissions "#monitor-service-role-permissions"). This policy is
maintained by AWS and defines the set of permissions that SiteWise Monitor uses to access your AWS IoT SiteWise
and IAM Identity Center resources.

When you create a SiteWise Monitor portal, you must choose a role that allows users of that portal to
access your AWS IoT SiteWise and IAM Identity Center resources. The AWS IoT SiteWise console can
create and configure the role for you. You can edit the role in IAM later. Your portal users
will have issues using their SiteWise Monitor portals if you remove the required permissions from the
role or delete the role.

###### Note

Portals created before April 29, 2020 didn't require service roles. If you created portals
before this date, you must attach service roles to continue using them. To do so, navigate to
the **Portals** page in the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/"), and then choose
**Migrate all portals to use IAM roles**.

The following sections describe how to create and manage the SiteWise Monitor service role in the
AWS Management Console or the AWS Command Line Interface.

###### Contents

- [Service role permissions for
  SiteWise Monitor (Classic)](monitor-service-role.md#monitor-service-role-permissions "monitor-service-role.md#monitor-service-role-permissions")
- [Service role permissions for
  SiteWise Monitor (AI-aware)](monitor-service-role.md#monitor-ai-service-role-permissions "monitor-service-role.md#monitor-ai-service-role-permissions")
- [Manage the SiteWise Monitor service role (console)](monitor-service-role.md#manage-portal-role-console "monitor-service-role.md#manage-portal-role-console")
  - [Find a portal's service role (console)](monitor-service-role.md#find-portal-role-console "monitor-service-role.md#find-portal-role-console")
  - [Create a SiteWise Monitor service role (AWS IoT SiteWise
    console)](monitor-service-role.md#create-portal-role-sitewise-console "monitor-service-role.md#create-portal-role-sitewise-console")
  - [Create a SiteWise Monitor service role (IAM
    console)](monitor-service-role.md#create-portal-role-iam-console "monitor-service-role.md#create-portal-role-iam-console")
  - [Change a portal's service role (console)](monitor-service-role.md#change-portal-role-console "monitor-service-role.md#change-portal-role-console")

- [Manage the SiteWise Monitor service role (CLI)](monitor-service-role.md#manage-portal-role-cli "monitor-service-role.md#manage-portal-role-cli")
  - [Find a portal's service role (CLI)](monitor-service-role.md#find-portal-role-cli "monitor-service-role.md#find-portal-role-cli")
  - [Create the SiteWise Monitor service role (CLI)](monitor-service-role.md#create-portal-role-cli "monitor-service-role.md#create-portal-role-cli")

- [SiteWise Monitor updates to
  AWSIoTSiteWiseMonitorServiceRole](monitor-service-role.md#monitor-role-permission-updates "monitor-service-role.md#monitor-role-permission-updates")

## Service role permissions for

SiteWise Monitor (Classic)

When you create a portal, AWS IoT SiteWise lets you create a role whose name starts with **AWSIoTSiteWiseMonitorServiceRole**. This role allows federated SiteWise Monitor users to access
your portal configuration, assets, asset data, and IAM Identity Center
configuration.

The role trusts the following service to assume the role:

- `monitor.iotsitewise.amazonaws.com`

The role uses the following permissions policy, which starts with **AWSIoTSiteWiseMonitorServicePortalPolicy**, to allow SiteWise Monitor users to complete actions
on resources in your account. The [AWSIoTSiteWiseMonitorPortalAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSIoTSiteWiseMonitorPortalAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSIoTSiteWiseMonitorPortalAccess") managed policy defines equivalent
permissions.

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

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
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
 "iotsitewise:GetAssetPropertyAggregates"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about the required permissions for alarms, see [Set up permissions for event alarms in AWS IoT SiteWise](alarms-iam-permissions.md "alarms-iam-permissions.md").

When a portal user signs in, SiteWise Monitor creates a [session policy](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") based on
the intersection of the service role and that user's access policies. Access policies define
identities' level of access to your portals and projects. For more information about portal
permissions and access policies, see [Administer your SiteWise Monitor portals](administer-portals.md "administer-portals.md") and [CreateAccessPolicy](../APIReference/API_CreateAccessPolicy.md "../APIReference/API_CreateAccessPolicy.md").

## Service role permissions for

SiteWise Monitor (AI-aware)

When you create a portal, AWS IoT SiteWise lets you create a role whose name starts with **IoTSiteWisePortalRole**. This role allows federated SiteWise Monitor users to access
your portal configuration, assets, asset data, and IAM Identity Center
configuration.

###### Warning

**Project owner** and **Project viewer** roles are not supported for SiteWise Monitor (AI-aware).

The role trusts the following service to assume the role:

- `monitor.iotsitewise.amazonaws.com`

The role uses the following permissions policy, which starts with **IoTSiteWiseAIPortalAccessPolicy**, to allow SiteWise Monitor users to complete actions
on resources in your account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:CreateProject",
 "iotsitewise:DescribePortal",
 "iotsitewise:ListProjects",
 "iotsitewise:DescribeProject",
 "iotsitewise:UpdateProject",
 "iotsitewise:DeleteProject",
 "iotsitewise:CreateDashboard",
 "iotsitewise:DescribeDashboard",
 "iotsitewise:UpdateDashboard",
 "iotsitewise:DeleteDashboard",
 "iotsitewise:ListDashboards",
 "iotsitewise:ListAssets",
 "iotsitewise:DescribeAsset",
 "iotsitewise:ListAssociatedAssets",
 "iotsitewise:ListAssetProperties",
 "iotsitewise:DescribeAssetProperty",
 "iotsitewise:GetAssetPropertyValue",
 "iotsitewise:GetAssetPropertyValueHistory",
 "iotsitewise:GetAssetPropertyAggregates",
 "iotsitewise:GetInterpolatedAssetPropertyValues",
 "iotsitewise:BatchGetAssetPropertyAggregates",
 "iotsitewise:BatchGetAssetPropertyValue",
 "iotsitewise:BatchGetAssetPropertyValueHistory",
 "iotsitewise:ListAssetRelationships",
 "iotsitewise:DescribeAssetModel",
 "iotsitewise:ListAssetModels",
 "iotsitewise:DescribeAssetCompositeModel",
 "iotsitewise:DescribeAssetModelCompositeModel",
 "iotsitewise:ListAssetModelProperties",
 "iotsitewise:ExecuteQuery",
 "iotsitewise:ListTimeSeries",
 "iotsitewise:DescribeTimeSeries",
 "iotsitewise:InvokeAssistant",
 "iotsitewise:DescribeDataset",
 "iotsitewise:ListDatasets",
 "iotevents:DescribeAlarmModel",
 "iotevents:ListTagsForResource",
 "iottwinmaker:ListWorkspaces",
 "iottwinmaker:ExecuteQuery",
 "iottwinmaker:GetWorkspace",
 "identitystore:DescribeUser"
 ],
 "Resource": "*"
 }
 ]
}`

```

When a portal user signs in, SiteWise Monitor creates a [session policy](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") based on
the intersection of the service role and that user's access policies.

## Manage the SiteWise Monitor service role (console)

The AWS IoT SiteWise console facilitates the management of the SiteWise Monitor service role for portals. Upon
creating a portal, the console checks for existing roles suitable for attachment. If none are
available, the console can create and configure a service role for you. For more information,
see [Create a portal in SiteWise Monitor](monitor-create-portal.md "monitor-create-portal.md").

###### Topics

- [Find a portal's service role (console)](#find-portal-role-console "#find-portal-role-console")
- [Create a SiteWise Monitor service role (AWS IoT SiteWise
  console)](#create-portal-role-sitewise-console "#create-portal-role-sitewise-console")
- [Create a SiteWise Monitor service role (IAM
  console)](#create-portal-role-iam-console "#create-portal-role-iam-console")
- [Change a portal's service role (console)](#change-portal-role-console "#change-portal-role-console")

### Find a portal's service role (console)

Use the following steps to find the service role attached to a SiteWise Monitor portal.

###### To find a portal's service role

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation pane, choose **Portals**.
3. Choose the portal for which you want to find the service role.

The role attached to the portal appears under **Permissions**,
**Service role**.

### Create a SiteWise Monitor service role (AWS IoT SiteWise

console)

When you create a SiteWise Monitor portal, you can create a service role for your portal. For
more information, see [Create a portal in SiteWise Monitor](monitor-create-portal.md "monitor-create-portal.md").

You can also create a service role for an existing portal in the AWS IoT SiteWise console. This
replaces the portal's existing service role.

###### To create a service role for an existing portal

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Portals**.
3. Choose the portal for which you want to create a new service role.
4. Under **Portal details**, choose **Edit**.
5. Under **Permissions**, choose **Create and use a new
   service role** from the list.
6. Enter a name for your new role.
7. Choose **Save**.

### Create a SiteWise Monitor service role (IAM

console)

You can create a service role from the service role template in the IAM console. This
role template includes the [AWSIoTSiteWiseMonitorPortalAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSIoTSiteWiseMonitorPortalAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSIoTSiteWiseMonitorPortalAccess") managed policy and specifies SiteWise Monitor as a trusted
entity.

###### To create a service role from the portal service role template

1. Navigate to the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. In **Choose a use case**, choose **IoT
   SiteWise**.
5. In **Select your use case**, choose **IoT SiteWise
   Monitor - Portal**.
6. Choose **Next: Permissions**.
7. Choose **Next: Tags**.
8. Choose **Next: Review**.
9. Enter a **Role name** for the new service role.
10. Choose **Create role**.

### Change a portal's service role (console)

Use the following procedure to choose a different SiteWise Monitor service role for a
portal.

###### To change a portal's service role

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Portals**.
3. Choose the portal for which you want to change the service role.
4. Under **Portal details**, choose **Edit**.
5. Under **Permissions**, choose **Use an existing
   role**.
6. Choose an existing role to attach to this portal.
7. Choose **Save**.

## Manage the SiteWise Monitor service role (CLI)

You can use the AWS CLI for the following portal service role management tasks:

###### Topics

- [Find a portal's service role (CLI)](#find-portal-role-cli "#find-portal-role-cli")
- [Create the SiteWise Monitor service role (CLI)](#create-portal-role-cli "#create-portal-role-cli")

### Find a portal's service role (CLI)

To find the service role attached to a SiteWise Monitor portal, run the following command to list
all of your portals in the current Region.

```
aws iotsitewise list-portals
```

The operation returns a response that contains your portal summaries in the following
format.

```
{
  "portalSummaries": [
    {
      "id": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE",
      "name": "WindFarmPortal",
      "description": "A portal that contains wind farm projects for Example Corp.",
      "roleArn": "arn:aws:iam::`123456789012`:role/service-role/`role-name`",
      "startUrl": "https://a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE.app.iotsitewise.aws",
      "creationDate": "2020-02-04T23:01:52.90248068Z",
      "lastUpdateDate": "2020-02-04T23:01:52.90248078Z"
    }
  ]
}
```

You can also use the [DescribePortal](../APIReference/API_DescribePortal.md "../APIReference/API_DescribePortal.md") operation to find your portal's role if you know the ID of your
portal.

### Create the SiteWise Monitor service role (CLI)

Use the following steps to create a new SiteWise Monitor service role.

###### To create a SiteWise Monitor service role

1. Create a role with a trust policy that allows SiteWise Monitor to assume the role. This
   example creates a role named `MySiteWiseMonitorPortalRole` from a
   trust policy stored in a JSON string.

Linux, macOS, or Unix

```
aws iam create-role --role-name MySiteWiseMonitorPortalRole --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "monitor.iotsitewise.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'
```

Windows command prompt

```
aws iam create-role --role-name MySiteWiseMonitorPortalRole --assume-role-policy-document "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"monitor.iotsitewise.amazonaws.com\"},\"Action\":\"sts:AssumeRole\"}]}"
```

2. Copy the role ARN from the role metadata in the output. When you create a portal,
   you use this ARN to associate the role with your portal. For more information about
   creating a portal, see [CreatePortal](../APIReference/API_CreatePortal.md "../APIReference/API_CreatePortal.md") in the _AWS IoT SiteWise API Reference_.
3. 1. For the SiteWise Monitor (Classic) – Attach the `AWSIoTSiteWiseMonitorPortalAccess` policy to the role, or attach
      a policy that defines equivalent permissions.

   ```
   aws iam attach-role-policy --role-name MySiteWiseMonitorPortalRole --policy-arn arn:aws:iam::aws:policy/service-role/AWSIoTSiteWiseMonitorPortalAccess
   ```

   2. For the SiteWise Monitor (AI-aware) – Attach the `IoTSiteWiseAIPortalAccessPolicy` policy to the role, or attach
      a policy that defines equivalent permissions. For example, create a policy with portal access permissions.
      The following example creates a policy named `MySiteWiseMonitorPortalAccess`.

   ```

   aws iam create-policy \
       --policy-name MySiteWiseMonitorPortalAccess \
       --policy-document '{
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "iotsitewise:CreateProject",
                   "iotsitewise:DescribePortal",
                   "iotsitewise:ListProjects",
                   "iotsitewise:DescribeProject",
                   "iotsitewise:UpdateProject",
                   "iotsitewise:DeleteProject",
                   "iotsitewise:CreateDashboard",
                   "iotsitewise:DescribeDashboard",
                   "iotsitewise:UpdateDashboard",
                   "iotsitewise:DeleteDashboard",
                   "iotsitewise:ListDashboards",
                   "iotsitewise:ListAssets",
                   "iotsitewise:DescribeAsset",
                   "iotsitewise:ListAssociatedAssets",
                   "iotsitewise:ListAssetProperties",
                   "iotsitewise:DescribeAssetProperty",
                   "iotsitewise:GetAssetPropertyValue",
                   "iotsitewise:GetAssetPropertyValueHistory",
                   "iotsitewise:GetAssetPropertyAggregates",
                   "iotsitewise:GetInterpolatedAssetPropertyValues",
                   "iotsitewise:BatchGetAssetPropertyAggregates",
                   "iotsitewise:BatchGetAssetPropertyValue",
                   "iotsitewise:BatchGetAssetPropertyValueHistory",
                   "iotsitewise:ListAssetRelationships",
                   "iotsitewise:DescribeAssetModel",
                   "iotsitewise:ListAssetModels",
                   "iotsitewise:DescribeAssetCompositeModel",
                   "iotsitewise:DescribeAssetModelCompositeModel",
                   "iotsitewise:ListAssetModelProperties",
                   "iotsitewise:ExecuteQuery",
                   "iotsitewise:ListTimeSeries",
                   "iotsitewise:DescribeTimeSeries",
                   "iotsitewise:InvokeAssistant",
                   "iotsitewise:DescribeDataset",
                   "iotsitewise:ListDatasets",
                   "iotevents:DescribeAlarmModel",
                   "iotevents:ListTagsForResource",
                   "iottwinmaker:ListWorkspaces",
                   "iottwinmaker:ExecuteQuery",
                   "iottwinmaker:GetWorkspace",
                   "identitystore:DescribeUser"
               ],
               "Resource": "*"
           }
       ]
   }'

   ```

###### To attach a service role to an existing portal

1. To retrieve the portal's existing details, run the following command. Replace
   `portal-id` with the ID of the portal.

```
aws iotsitewise describe-portal --portal-id `portal-id`
```

The operation returns a response that contains the portal's details in the following
format.

```
{
    "portalId": "a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE",
    "portalArn": "arn:aws:iotsitewise:`region`:`account-id`:portal/a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE",
    "portalName": "WindFarmPortal",
    "portalDescription": "A portal that contains wind farm projects for Example Corp.",
    "portalClientId": "E-1a2b3c4d5e6f_sn6tbqHVzLWVEXAMPLE",
    "portalStartUrl": "https://a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE.app.iotsitewise.aws",
    "portalContactEmail": "support@example.com",
    "portalStatus": {
        "state": "ACTIVE"
    },
    "portalCreationDate": "2020-04-29T23:01:52.90248068Z",
    "portalLastUpdateDate": "2020-04-29T00:28:26.103548287Z",
    "roleArn": "arn:aws:iam::123456789012:role/service-role/AWSIoTSiteWiseMonitorServiceRole_1aEXAMPLE"
}
```

2. To attach a service role to a portal, run the following command. Replace
   `role-arn` with the service role ARN, and replace the
   remaining parameters with the portal's existing values.

```
aws iotsitewise update-portal \
  --portal-id `portal-id` \
  --role-arn `role-arn` \
  --portal-name `portal-name` \
  --portal-description `portal-description` \
  --portal-contact-email `portal-contact-email`
```

## SiteWise Monitor updates to

AWSIoTSiteWiseMonitorServiceRole

You can view details about updates to **AWSIoTSiteWiseMonitorServiceRole** for SiteWise Monitor, beginning from when this service
began tracking the changes. For automatic alerts about changes to this page, subscribe to the
RSS feed on the AWS IoT SiteWise Document history page.

| Change                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                     | Date              |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSIoTSiteWiseMonitorPortalAccess](#monitor-service-role-permissions "#monitor-service-role-permissions") – Updated policy | AWS IoT SiteWise updated the [AWSIoTSiteWiseMonitorPortalAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSIoTSiteWiseMonitorPortalAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSIoTSiteWiseMonitorPortalAccess") managed policy for the alarms<br>feature. | May 27, 2021      |
| AWS IoT SiteWise started tracking changes                                                                                   | AWS IoT SiteWise started tracking changes for its service role.                                                                                                                                                                                                                                                                                                 | December 15, 2020 |
