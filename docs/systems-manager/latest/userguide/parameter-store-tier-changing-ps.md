# Specifying or changing the Parameter Store default tier (PowerShell)

The following procedure shows how to use the Tools for Windows PowerShell to change the default
parameter tier setting for a specific AWS Region in an Amazon Web Services
account.

###### To specify or change the Parameter Store default tier using PowerShell

1. Change the Parameter Store default tier in the current AWS account and
   AWS Region using the AWS Tools for PowerShell (Tools for PowerShell).

```
Update-SSMServiceSetting -SettingId "arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/parameter-store/default-parameter-tier" -SettingValue "`tier-option`" -Region `region`
```

`region` represents the identifier for an AWS Region supported
by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported
`region` values, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

`tier-option` values include
`Standard`, `Advanced`, and
`Intelligent-Tiering`. For information about these
options, see [Specifying a default parameter tier](ps-default-tier.md "ps-default-tier.md").

There is no output if the command succeeds. 2. Run the following command to view the current default parameter
tier service settings for Parameter Store in the current AWS account and
AWS Region.

```
Get-SSMServiceSetting -SettingId "arn:aws:ssm:`region`:``account-id``:servicesetting/ssm/parameter-store/default-parameter-tier" -Region `region`
```

`region` represents the identifier for an AWS Region supported
by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported
`region` values, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

The system returns information similar to the following.

```
ARN : arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/default-parameter-tier
LastModifiedDate : 4/29/2019 3:35:44 PM
LastModifiedUser : arn:aws:sts::123456789012:assumed-role/Administrator/Jasper
SettingId        : /ssm/parameter-store/default-parameter-tier
SettingValue     : Advanced
Status           : Customized

```

If you want to change the default tier setting again, repeat this
procedure and specify a different `SettingValue` option.
