# Using roles to create operational insight OpsItems in Systems Manager OpsCenter

Systems Manager uses the service-linked role named **`AWSServiceRoleForAmazonSSM_OpsInsights`**. AWS Systems Manager uses this IAM service role to create and update operational insight OpsItems in Systems Manager OpsCenter.

## `AWSServiceRoleForAmazonSSM_OpsInsights` service-linked role permissions for

Systems Manager operational insight OpsItems

The `AWSServiceRoleForAmazonSSM_OpsInsights` service-linked role trusts the following
services to assume the role:

- `opsinsights.ssm.amazonaws.com`

The role permissions policy allows Systems Manager to complete the following
actions on the specified resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateOpsItem",
 "Effect": "Allow",
 "Action": [
 "ssm:CreateOpsItem",
 "ssm:AddTagsToResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowAccessOpsItem",
 "Effect": "Allow",
 "Action": [
 "ssm:UpdateOpsItem",
 "ssm:GetOpsItem"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/SsmOperationalInsight": "true"
 }
 }
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user,
group, or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating the

`AWSServiceRoleForAmazonSSM_OpsInsights` service-linked role for
Systems Manager

You must create a service-linked role. If you enable operational insights by
using Systems Manager in the AWS Management Console, you can create the service-linked role by
choosing the **Enable** button.

## Editing the

`AWSServiceRoleForAmazonSSM_OpsInsights` service-linked role for
Systems Manager

Systems Manager does not allow you to edit the `AWSServiceRoleForAmazonSSM_OpsInsights`
service-linked role. After you create a service-linked role, you cannot change
the name of the role because various entities might reference the role. However,
you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the

`AWSServiceRoleForAmazonSSM_OpsInsights` service-linked role for
Systems Manager

If you no longer need to use a feature or service that requires a
service-linked role, we recommend that you delete that role. That way you don’t
have an unused entity that is not actively monitored or maintained. However, you
must clean up your service-linked role before you can manually delete it.

### Cleaning up the `AWSServiceRoleForAmazonSSM_OpsInsights` service-linked role

Before you can use IAM to delete the `AWSServiceRoleForAmazonSSM_OpsInsights`
service-linked role, you must first deactivate operational insights in Systems Manager
OpsCenter. For more information, see [Analyzing operational
insights to reduce OpsItems](OpsCenter-working-operational-insights.md "OpsCenter-working-operational-insights.md").

### Manually delete the

`AWSServiceRoleForAmazonSSM_OpsInsights` service-linked role

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForAmazonSSM_OpsInsights` service-linked role. For more information,
see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for the

Systems Manager  `AWSServiceRoleForAmazonSSM_OpsInsights` service-linked role

Systems Manager does not support using service-linked roles in every Region
where the service is available. You can use the AWSServiceRoleForAmazonSSM_OpsInsights role in the
following Regions.

| Region name               | Region identity | Support in Systems Manager |
| ------------------------- | --------------- | -------------------------- |
| US East (N. Virginia)     | us-east-1       | Yes                        |
| US East (Ohio)            | us-east-2       | Yes                        |
| US West (N. California)   | us-west-1       | Yes                        |
| US West (Oregon)          | us-west-2       | Yes                        |
| Asia Pacific (Mumbai)     | ap-south-1      | Yes                        |
| Asia Pacific (Tokyo)      | ap-northeast-1  | Yes                        |
| Asia Pacific (Seoul)      | ap-northeast-2  | Yes                        |
| Asia Pacific (Singapore)  | ap-southeast-1  | Yes                        |
| Asia Pacific (Sydney)     | ap-southeast-2  | Yes                        |
| Asia Pacific (Hong Kong)  | ap-east-1       | Yes                        |
| Canada (Central)          | ca-central-1    | Yes                        |
| Europe (Frankfurt)        | eu-central-1    | Yes                        |
| Europe (Ireland)          | eu-west-1       | Yes                        |
| Europe (London)           | eu-west-2       | Yes                        |
| Europe (Paris)            | eu-west-3       | Yes                        |
| Europe (Stockholm)        | eu-north-1      | Yes                        |
| Europe (Milan)            | eu-south-1      | Yes                        |
| South America (São Paulo) | sa-east-1       | Yes                        |
| Middle East (Bahrain)     | me-south-1      | Yes                        |
| Africa (Cape Town)        | af-south-1      | Yes                        |
| AWS GovCloud (US)         | us-gov-west-1   | Yes                        |
| AWS GovCloud (US)         | us-gov-east-1   | Yes                        |
