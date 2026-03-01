# Managing Amazon ECS account settings using the AWS CLI

You can manage your account settings using the Amazon ECS API, AWS CLI or SDKs. The
`dualStackIPv6`, `fargateFIPSMode`, `fargateTaskRetirementWaitPeriod`
and the `fargateEventWindows` account settings can only be viewed or
changed using those tools.

###### Note

You can use dual-stack service endpoints to interact with Amazon ECS from the AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md "dual-stack-endpoint.md").

For information about the available API actions for task definitions see [Account setting
actions](../APIReference/OperationList-query-account.md "../APIReference/OperationList-query-account.md") in the _Amazon Elastic Container Service API Reference_.

Use one of the following commands to modify the default account setting for all users
or roles on your account. These changes apply to the entire AWS account unless a user
or role explicitly overrides these settings for themselves.

- [put-account-setting-default](../../../cli/latest/reference/ecs/put-account-setting-default.md "../../../cli/latest/reference/ecs/put-account-setting-default.md") (AWS CLI)

```
`aws ecs put-account-setting-default --name `serviceLongArnFormat` --value `enabled` --region `us-east-2``
```

You can also use this command to modify other account settings. To do this,
replace the `name` parameter with the corresponding account
setting.

- [Write-ECSAccountSetting](../../../powershell/latest/reference/items/Write-ECSAccountSetting.md "../../../powershell/latest/reference/items/Write-ECSAccountSetting.md") (AWS Tools for Windows PowerShell)

```
`Write-ECSAccountSettingDefault -Name `serviceLongArnFormat` -Value `enabled` -Region `us-east-1` -Force`
```

###### To modify the account settings for your user account (AWS CLI)

Use one of the following commands to modify the account settings for your user. If
you’re using these commands as the root user, changes apply to the entire AWS
account unless a; user or role explicitly overrides these settings for
themselves.

- [put-account-setting](../../../cli/latest/reference/ecs/put-account-setting.md "../../../cli/latest/reference/ecs/put-account-setting.md") (AWS CLI)

```
`aws ecs put-account-setting --name `serviceLongArnFormat` --value `enabled` --region `us-east-1``
```

You can also use this command to modify other account settings. To do this,
replace the `name` parameter with the corresponding account
setting.

- [Write-ECSAccountSetting](../../../powershell/latest/reference/items/Write-ECSAccountSetting.md "../../../powershell/latest/reference/items/Write-ECSAccountSetting.md") (AWS Tools for Windows PowerShell)

```
`Write-ECSAccountSetting -Name `serviceLongArnFormat` -Value `enabled` -Force`
```

###### To modify the account settings for a specific user or role (AWS CLI)

Use one of the following commands and specify the ARN of a user, role, or
root user in the request to modify the account settings for a specific user or
role.

- [put-account-setting](../../../cli/latest/reference/ecs/put-account-setting.md "../../../cli/latest/reference/ecs/put-account-setting.md") (AWS CLI)

```
`aws ecs put-account-setting --name `serviceLongArnFormat` --value `enabled` --principal-arn arn:aws:iam::`aws_account_id`:user/`principalName` --region `us-east-1``
```

You can also use this command to modify other account settings. To do this,
replace the `name` parameter with the corresponding account
setting.

- [Write-ECSAccountSetting](../../../powershell/latest/reference/items/Write-ECSAccountSetting.md "../../../powershell/latest/reference/items/Write-ECSAccountSetting.md") (AWS Tools for Windows PowerShell)

```
`Write-ECSAccountSetting -Name `serviceLongArnFormat` -Value `enabled` -PrincipalArn arn:aws:iam::`aws_account_id`:user/`principalName` -Region `us-east-1` -Force`
```
