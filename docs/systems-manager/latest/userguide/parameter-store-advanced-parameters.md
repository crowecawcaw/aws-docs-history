# Choosing parameter tiers in Parameter Store

To control parameter storage attributes, Parameter Store includes _standard parameters_ and _advanced
parameters_. You configure each parameter individually for an account and Region. The parameter tier determines the
maximum size of a parameter value, the number of parameters in a specific tier that you can create,
whether you can use parameter policies, and whether charges apply.

Parameter tiers are different from parameter throughput. Tiers control parameter storage attributes, whereas throughput controls request rate.

## Standard and advanced parameter tiers

The following table describes the differences between the tiers.

The following table describes the differences between parameter tiers.

| Feature or use case                                    | Standard                                                                       | Advanced                                                                                                                                                                                                                            |
| ------------------------------------------------------ | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use case                                               | Best for most configuration data and low-scale workloads. This is the default. | Best when you need higher limits, larger values, or parameter policies.                                                                                                                                                             |
| Maximum parameters<br>(per AWS account and AWS Region) | 10,000                                                                         | 100,000                                                                                                                                                                                                                             |
| Maximum value size                                     | 4 KB                                                                           | 8 KB                                                                                                                                                                                                                                |
| Parameter policies                                     | Not supported                                                                  | Supported<br>For more information, see [Assigning parameter policies in Parameter Store](parameter-store-policies.md "parameter-store-policies.md").                                                                                |
| Shareability across AWS accounts                       | Not supported                                                                  | Supported<br>For more information, see [Working with shared parameters in Parameter Store](parameter-store-shared-parameters.md "parameter-store-shared-parameters.md").                                                            |
| Upgrade and downgrade capability                       | Upgradeable                                                                    | Not downgradeable                                                                                                                                                                                                                   |
| Cost                                                   | No additional charge                                                           | Charges apply<br>For more information, see [AWS Systems Manager<br>Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store "https://aws.amazon.com/systems-manager/pricing/#Parameter_Store"). |

For a complete list of Parameter Store quotas and limits, see [AWS Systems Manager
endpoints and quotas](../../../general/latest/gr/ssm.md#parameter-store "../../../general/latest/gr/ssm.md#parameter-store") in the _AWS General Reference_.

## Default tier and individual parameter tier settings

Parameter Store supports the following related settings:

- Default parameter tier for your AWS account and Region

This setting controls what tier Parameter Store uses when you create a new parameter and don’t explicitly specify a tier.
You can set the default to `Standard`, `Advanced`, or `Intelligent-Tiering`.

- Tier for an individual parameter

You can specify the tier when you create or update an individual parameter.
You can change a standard parameter to an advanced parameter, but you can't
change an advanced parameter to a standard parameter.

The default parameter tier is separate from the tier of an individual parameter. Changing the default parameter tier affects only new parameters that you create
without specifying a tier. Existing parameters aren't affected.

## Viewing parameter tier settings

You can view the default tier setting for your AWS account and Region, and the tier setting for each individual parameter.

### View the default parameter tier

To view the default parameter tier for your AWS account and Region, use the action. The following example
retrieves the default parameter tier.

```
aws ssm get-service-setting \
    --region us-east-1 \
    --setting-id arn:aws:ssm:us-east-1:111122223333:servicesetting/ssm/parameter-store/default-parameter-tier
```

The following example shows sample output.

```
{
    "ServiceSetting": {
        "SettingId": "/ssm/parameter-store/default-parameter-tier",
        "SettingValue": "Standard",
        "Status": "Default"
    }
}
```

### View the tier for a specific parameter

To view the tier for a specific parameter, use the action. The following example
returns the tier of parameter `/myapp/dev/log-level`.

```
aws ssm describe-parameters \
    --region us-east-1 \
    --parameter-filters "Key=Name,Option=Equals,Values=/myapp/dev/log-level" \
    --query "Parameters[0].Tier" \
    --output text
```

The command returns the parameter tier, such as `Standard` or `Advanced`.

###### Topics

- [Specifying a default parameter tier for your AWS account and AWS Region](ps-default-tier.md "ps-default-tier.md")
- [Changing a standard parameter to an advanced parameter](parameter-store-advanced-parameters-enabling.md "parameter-store-advanced-parameters-enabling.md")
- [Limitations on changing tiers for individual parameters](#parameter-store-tiers-limitations "#parameter-store-tiers-limitations")

## Limitations on changing tiers for individual parameters

You can change a standard parameter to an advanced parameter at any time.
You _can't_ change an advanced parameter to a standard
parameter for the following reasons:

- Changing the parameter to the standard tier would truncate the
  parameter value from `8 KB` to `4 KB`, resulting
  in data loss.
- Changing the parameter to the standard tier would remove any policies
  attached to the parameter.
- Advanced and standard parameters use a different form of encryption.

If you no longer need an advanced parameter, or if you no longer want to incur
charges for an advanced parameter, delete it and recreate it as a new standard
parameter.

The default parameter tier is a separate setting. You can change the default
parameter tier for an AWS account and Region from `Standard` to
`Advanced`, and then change it back to `Standard`. The
default tier setting affects only new parameters that you create without
specifying a tier. Existing parameters aren't affected.

For example, you can create parameters while the default tier is
`Standard`, and then set the default parameter tier to
`Advanced`. New parameters that you create without specifying a tier
use the `Advanced` tier. You can later change the default tier back
to `Standard` without changing the tier of existing parameters.

Advanced parameters incur charges. For more information, see
[AWS Systems Manager Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store "https://aws.amazon.com/systems-manager/pricing/#Parameter_Store").
