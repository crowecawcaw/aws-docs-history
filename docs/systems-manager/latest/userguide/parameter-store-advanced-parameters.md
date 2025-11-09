AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Managing parameter

tiers

Parameter Store, a tool in AWS Systems Manager, includes _standard
parameters_ and _advanced
parameters_. You individually configure parameters to use either the
standard-parameter tier (the default tier) or the advanced-parameter tier.

You can change a standard parameter to an advanced parameter at any time, but you
can’t revert an advanced parameter to a standard parameter. This is because
reverting an advanced parameter to a standard parameter would cause the system to
truncate the size of the parameter from 8 KB to 4 KB, resulting in data loss.
Reverting would also remove any policies attached to the parameter. Also, advanced
parameters use a different form of encryption than standard parameters. For more
information, see [How
AWS Systems Manager Parameter Store uses AWS KMS](../../../kms/latest/developerguide/services-parameter-store.md "../../../kms/latest/developerguide/services-parameter-store.md") in the
_AWS Key Management Service Developer Guide_.

If you no longer need an advanced parameter, or if you no longer want to incur
charges for an advanced parameter, delete it and recreate it as a new standard
parameter.

The following table describes the differences between the tiers.

|                                                                        | Standard             | Advanced                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Total number of parameters allowed<br>(per AWS account and AWS Region) | 10,000               | 100,000                                                                                                                                                                                                                             |
| Maximum size of a parameter value                                      | 4 KB                 | 8 KB                                                                                                                                                                                                                                |
| Parameter policies available                                           | No                   | Yes<br>For more information, see [Assigning parameter policies in<br>Parameter Store](parameter-store-policies.md "parameter-store-policies.md").                                                                                   |
| Cost                                                                   | No additional charge | Charges apply<br>For more information, see [AWS Systems Manager<br>Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store "https://aws.amazon.com/systems-manager/pricing/#Parameter_Store"). |

###### Topics

- [Specifying a default parameter tier](#ps-default-tier "#ps-default-tier")
- [Changing a
  standard parameter to an advanced parameter](#parameter-store-advanced-parameters-enabling "#parameter-store-advanced-parameters-enabling")

## Specifying a default parameter tier

In requests to create or update a parameter (that is, the
`PutParameter` operation), you can specify the parameter
tier to use in the request. The following is an example, using the AWS Command Line Interface
(AWS CLI).

Linux & macOS

```
aws ssm put-parameter \
    --name "default-ami" \
    --type "String" \
    --value "t2.micro" \
    --tier "Standard"
```

Windows

```
aws ssm put-parameter ^
    --name "default-ami" ^
    --type "String" ^
    --value "t2.micro" ^
    --tier "Standard"
```

Whenever you specify a tier in the request, Parameter Store creates or updates the
parameter according to your request. However, if you don't explicitly specify a
tier in a request, the Parameter Store default tier setting determines which tier the
parameter is created in.

The default tier when you begin using Parameter Store is the standard-parameter tier.
If you use the advanced-parameter tier, you can specify one of the following as
the default:

- **Advanced**: With this option, Parameter
  Store evaluates all requests as advanced parameters.
- **Intelligent-Tiering**: With this
  option, Parameter Store evaluates each request to determine if the parameter is
  standard or advanced.

If the request doesn't include any options that require an advanced
parameter, the parameter is created in the standard-parameter tier. If
one or more options requiring an advanced parameter are included in the
request, Parameter Store creates a parameter in the advanced-parameter
tier.

###### Benefits of Intelligent-Tiering

The following are reasons you might choose Intelligent-Tiering as the
default tier.

**Cost control** – Intelligent-Tiering helps
control your parameter-related costs by always creating standard parameters
unless an advanced parameter is absolutely necessary.

**Automatic upgrade to the advanced-parameter
tier** – When you make a change to your code that requires
upgrading a standard parameter to an advanced parameter, Intelligent-Tiering
handles the conversion for you. You don't need to change your code to handle the
upgrade.

Here are some examples of automatic upgrades:

- Your AWS CloudFormation templates provision numerous parameters when they're
  run. When this process causes you to reach the 10,000 parameter quota in
  the standard-parameter tier, Intelligent-Tiering automatically upgrades
  you to the advanced-parameter tier, and your AWS CloudFormation processes aren't
  interrupted.
- You store a certificate value in a parameter, rotate the certificate
  value regularly, and the content is less than the 4 KB quota of the
  standard-parameter tier. If a replacement certificate value exceeds 4
  KB, Intelligent-Tiering automatically upgrades the parameter to the
  advanced-parameter tier.
- You want to associate numerous existing standard parameters to a
  parameter policy, which requires the advanced-parameter tier. Instead of
  your having to include the option `--tier Advanced` in all
  the calls to update the parameters, Intelligent-Tiering automatically
  upgrades the parameters to the advanced-parameter tier. The
  Intelligent-Tiering option upgrades parameters from standard to advanced
  whenever criteria for the advanced-parameter tier are introduced.

Options that require an advanced parameter include the following:

- The content size of the parameter is more than 4 KB.
- The parameter uses a parameter policy.
- More than 10,000 parameters already exist in your AWS account in the
  current AWS Region.

###### Default Tier Options

The tier options you can specify as the default include the
following.

- **Standard** – The
  standard-parameter tier is the default tier when you begin to use
  Parameter Store. Using the standard-parameter tier, you can create 10,000
  parameters for each AWS Region in an AWS account. The content size
  of each parameter can equal a maximum of 4 KB. Standard parameters don't
  support parameter policies. There is no additional charge to use the
  standard-parameter tier. Choosing **Standard** as the
  default tier means that Parameter Store always attempts to create a standard
  parameter for requests that don't specify a tier.
- **Advanced** – Use the
  advanced-parameter tier to create a maximum of 100,000 parameters for
  each AWS Region in an AWS account. The content size of each
  parameter can equal a maximum of 8 KB. Advanced parameters support
  parameter policies. To share a parameter, it must be in the advanced
  parameter tier. There is a charge to use the advanced-parameter tier.
  For more information, see [AWS Systems Manager Pricing for
  Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store "https://aws.amazon.com/systems-manager/pricing/#Parameter_Store"). Choosing **Advanced** as the
  default tier means that Parameter Store always attempts to create an advanced
  parameter for requests that don't specify a tier.

###### Note

When you choose the advanced-parameter tier, explicitly authorize
AWS to charge your account for any advanced parameters you
create.

- **Intelligent-Tiering** – With the
  Intelligent-Tiering option, Parameter Store determines whether to use the
  standard-parameter tier or advanced-parameter tier based on the content
  of the request. For example, if you run a command to create a parameter
  with content under 4 KB, and there are fewer than 10,000 parameters in
  the current AWS Region in your AWS account, and you don't specify a
  parameter policy, a standard parameter is created. If you run a command
  to create a parameter with more than 4 KB of content, you already have
  more than 10,000 parameters in the current AWS Region in your
  AWS account, or you specify a parameter policy, an advanced parameter
  is created.

###### Note

When you choose Intelligent-Tiering, explicitly authorize AWS to
charge your account for any advanced parameters you created.

You can change the Parameter Store default tier setting at any time.

### Configuring permissions

to specify a Parameter Store default tier

Verify that you have permission in AWS Identity and Access Management (IAM) to change the default
parameter tier in Parameter Store by doing one of the following:

- Make sure that you attach the `AdministratorAccess`
  policy to your IAM entity (such as user, group, or role).
- Make sure that you have permission to change the default tier
  setting by using the following API operations:
  - [GetServiceSetting](../APIReference/API_GetServiceSetting.md "../APIReference/API_GetServiceSetting.md")
  - [UpdateServiceSetting](../APIReference/API_UpdateServiceSetting.md "../APIReference/API_UpdateServiceSetting.md")
  - [ResetServiceSetting](../APIReference/API_ResetServiceSetting.md "../APIReference/API_ResetServiceSetting.md")

Grant the following permissions to the IAM entity to allow a user to
view and change the default tier setting for parameters in a specific
AWS Region in an AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetServiceSetting"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:UpdateServiceSetting"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:servicesetting/ssm/parameter-store/default-parameter-tier"
 }
 ]
}`

```

Administrators can specify read-only permission by assigning the following
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetServiceSetting"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "ssm:ResetServiceSetting",
 "ssm:UpdateServiceSetting"
 ],
 "Resource": "*"
 }
 ]
}`

```

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

### Specifying or changing the

Parameter Store default tier using the console

The following procedure shows how to use the Systems Manager console to specify or
change the default parameter tier for the current AWS account and
AWS Region.

###### Tip

If you haven't created a parameter yet, you can use the AWS Command Line Interface
(AWS CLI) or AWS Tools for Windows PowerShell to change the default parameter tier. For
information, see [Specifying or changing
the Parameter Store default tier using the AWS CLI](#parameter-store-tier-changing-cli "#parameter-store-tier-changing-cli") and [Specifying or changing
the Parameter Store default tier (PowerShell)](#parameter-store-tier-changing-ps "#parameter-store-tier-changing-ps").

###### To specify or change the Parameter Store default tier

1.  Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2.  In the navigation pane, choose **Parameter Store**.
3.  Choose the **Settings** tab.
4.  Choose **Change default tier**.
5.  Choose one of the following options.

        * **Standard**
        * **Advanced**
        * **Intelligent-Tiering**

    For information about these options, see [Specifying a default parameter tier](#ps-default-tier "#ps-default-tier").

6.  Review the message, and choose
    **Confirm**.

If you want to change the default tier setting later, repeat this
procedure and specify a different default tier option.

### Specifying or changing

the Parameter Store default tier using the AWS CLI

The following procedure shows how to use the AWS CLI to change the default
parameter tier setting for the current AWS account and
AWS Region.

###### To specify or change the Parameter Store default tier using the

AWS CLI

1. Open the AWS CLI and run the following command to change the default
   parameter tier setting for a specific AWS Region in an
   AWS account.

```
aws ssm update-service-setting --setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/parameter-store/default-parameter-tier --setting-value `tier-option`
```

`region` represents the identifier for an AWS Region supported
by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported
`region` values, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

`tier-option` values include
`Standard`, `Advanced`, and
`Intelligent-Tiering`. For information about these
options, see [Specifying a default parameter tier](#ps-default-tier "#ps-default-tier").

There is no output if the command succeeds. 2. Run the following command to view the current default parameter
tier service settings for Parameter Store in the current AWS account and
AWS Region.

```
aws ssm get-service-setting --setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/parameter-store/default-parameter-tier
```

The system returns information similar to the following.

```
{
    "ServiceSetting": {
        "SettingId": "/ssm/parameter-store/default-parameter-tier",
        "SettingValue": "Advanced",
        "LastModifiedDate": 1556551683.923,
        "LastModifiedUser": "arn:aws:sts::123456789012:assumed-role/Administrator/Jasper",
        "ARN": "arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/default-parameter-tier",
        "Status": "Customized"
    }
}
```

If you want to change the default tier setting again, repeat this
procedure and specify a different `SettingValue` option.

### Specifying or changing

the Parameter Store default tier (PowerShell)

The following procedure shows how to use the Tools for Windows PowerShell to change the default
parameter tier setting for a specific AWS Region in an Amazon Web Services
account.

###### To specify or change the Parameter Store default tier using

PowerShell

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
options, see [Specifying a default parameter tier](#ps-default-tier "#ps-default-tier").

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

## Changing a

standard parameter to an advanced parameter

Use the following procedure to change an existing standard parameter to an
advanced parameter. For information about how to create a new advanced
parameter, see [Creating Parameter Store parameters in
Systems Manager](sysman-paramstore-su-create.md "sysman-paramstore-su-create.md").

###### To change a standard parameter to an advanced parameter

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Parameter Store**.
3. Choose a parameter, and then choose **Edit**.
4. For **Description**, enter information about this
   parameter.
5. Choose **Advanced**.
6. For **Value**, enter the value of this parameter.
   Advanced parameters have a maximum value limit of 8 KB.
7. Choose **Save changes**.
