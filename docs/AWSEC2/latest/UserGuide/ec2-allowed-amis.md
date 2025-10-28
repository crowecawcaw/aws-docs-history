# Control the discovery and use of AMIs in Amazon EC2 with

Allowed AMIs

To control the discovery and use of Amazon Machine Images (AMIs) by users in your
AWS account, you can use the _Allowed AMIs_ feature. You
specify criteria that AMIs must meet to be visible and available within your account. When
the criteria are enabled, users launching instances will only see and have access to AMIs
that comply with the specified criteria. For example, you can specify a list of trusted AMI
providers as the criteria, and only AMIs from these providers will be visible and available
for use.

Before enabling the Allowed AMIs settings, you can enable _audit
mode_ to preview which AMIs will or won't be visible and available for use.
This lets you refine the criteria as needed to ensure that only the intended AMIs are
visible and available to users in your account. Additionally, use the [describe-instance-image-metadata](../../../cli/latest/reference/ec2/describe-instance-image-metadata.md "../../../cli/latest/reference/ec2/describe-instance-image-metadata.md") command to find instances that were launched
with AMIs that don't meet the specified criteria. This information can guide your decision
to either update your launch configurations to use compliant AMIs (for example, specifying a
different AMI in a launch template) or adjust your criteria to allow these AMIs.

You specify the Allowed AMIs settings at the account level, either directly in the account
or by using a declarative policy. These settings must be configured in each AWS Region
where you want to control AMI usage. Using a declarative policy allows you to apply the
settings across multiple Regions simultaneously, as well as across multiple accounts
simultaneously. When a declarative policy is in use, you can't modify the settings directly
within an account. This topic describes how to configure the settings directly within an
account. For information about using declarative policies, see [Declarative
policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User Guide_.

###### Note

The Allowed AMIs feature only controls the discovery and use of public AMIs or AMIs
shared with your account. It does not restrict the AMIs owned by your account.
Regardless of the criteria you set, the AMIs created by your account are always
discoverable and usable by users in your account.

###### Key benefits of Allowed AMIs

- **Compliance and security**: Users can only discover
  and use AMIs that meet the specified criteria, reducing the risk of non-compliant
  AMI usage.
- **Efficient management**: By reducing the number of
  allowed AMIs, managing the remaining ones becomes easier and more efficient.
- **Centralized account-level implementation**:
  Configure the Allowed AMIs settings at the account level, either directly within the
  account or through a declarative policy. This provides a centralized and efficient
  way to control AMI usage across the entire account.

###### Contents

- [How Allowed AMIs works](#how-allowed-amis-works "#how-allowed-amis-works")
- [Best practices for
  implementing Allowed AMIs](#best-practice-for-implementing-allowed-amis "#best-practice-for-implementing-allowed-amis")
- [Required IAM permissions](#iam-permissions-for-allowed-amis "#iam-permissions-for-allowed-amis")
- [Manage the settings for Allowed
  AMIs](manage-settings-allowed-amis.md "manage-settings-allowed-amis.md")

## How Allowed AMIs works

To control which AMIs can be discovered and used in your account, you define a set of
criteria against which to evaluate the AMIs. The criteria are made up of one or more
`ImageCriterion` as shown in the following diagram. An explanation
follows the diagram.

![The Allowed AMIs ImageCriteria configuration hierarchy.](images/ami_allowed-amis-imagecriteria.png)

The configuration has three levels:

- **1** – Parameter values
  - Multi-value parameters:
    - `ImageProviders`
    - `ImageNames`
    - `MarketplaceProductCodes`

    An AMI can match _any_ values within a parameter to
    be allowed.

    Example: `ImageProviders` = `amazon`
    **OR** account
    `111122223333`
    **OR** account
    `444455556666` (The evaluation logic
    for parameter values is not shown in the diagram.)

  - Single-value parameters:
    - `CreationDateCondition`
    - `DeprecationTimeCondition`

- **2** – `ImageCriterion`
  - Groups multiple parameters with **AND** logic.
  - An AMI must match _all_ parameters
    within an `ImageCriterion` to be allowed.
  - Example: `ImageProviders` = `amazon`
    **AND**
    `CreationDateCondition` = 300 days or less

- **3** – `ImageCriteria`
  - Groups multiple `ImageCriterion` with **OR** logic.
  - An AMI can match _any_
    `ImageCriterion` to be allowed.
  - Forms the complete configuration against which AMIs are evaluated.

###### Topics

- [Allowed AMIs parameters](#allowed-amis-criteria "#allowed-amis-criteria")
- [Allowed AMIs configuration](#allowed-amis-json-configuration "#allowed-amis-json-configuration")
- [How criteria are
  evaluated](#how-allowed-amis-criteria-are-evaluated "#how-allowed-amis-criteria-are-evaluated")
- [Limits](#allowed-amis-json-configuration-limits "#allowed-amis-json-configuration-limits")
- [Allowed AMIs operations](#allowed-amis-operations "#allowed-amis-operations")

### Allowed AMIs parameters

The following parameters can be configured to create `ImageCriterion`:

`ImageProviders`

The AMI providers whose AMIs are allowed.

Valid values are aliases that are defined by AWS, and AWS account
IDs, as follows:

- `amazon` – An alias that identifies AMIs created by Amazon or
  verified providers
- `aws-marketplace` – An alias that identifies
  AMIs created by verified providers in the AWS Marketplace
- `aws-backup-vault` – An alias that
  identifies backup AMIs that reside in logically air-gapped AWS
  Backup vault accounts. If you use the AWS Backup logically
  air-gapped vault feature, ensure this alias is included as an
  AMI provider.
- AWS account IDs – One or more 12-digit AWS account
  IDs
- `none` – Indicates that only AMIs created by
  your account can be discovered and used. Public or shared AMIs
  can't be discovered and used. When specified,
  no other criteria can be specified.

`ImageNames`

The names of allowed AMIs, using exact matches or wildcards
(`?` or `*`).

`MarketplaceProductCodes`

The AWS Marketplace product codes for allowed AMIs.

`CreationDateCondition`

The maximum age for allowed AMIs.

`DeprecationTimeCondition`

The maximum period since deprecation for allowed AMIs.

For the valid values and constraints for each criterion, see [ImageCriterionRequest](../APIReference/API_ImageCriterionRequest.md "../APIReference/API_ImageCriterionRequest.md") in the _Amazon EC2 API Reference_.

### Allowed AMIs configuration

The core configuration for Allowed AMIs is the `ImageCriteria` configuration
that defines the criteria for allowed AMIs. The following JSON structure shows the
parameters that can be specified:

```
{
    "State": "enabled" | "disabled" | "audit-mode",
    "ImageCriteria" : [
        {
            "ImageProviders": ["string",...],
            "MarketplaceProductCodes": ["string",...],
            "ImageNames":["string",...],
            "CreationDateCondition" : {
                "MaximumDaysSinceCreated": integer
            },
            "DeprecationTimeCondition" : {
                "MaximumDaysSinceDeprecated": integer
            }
         },
         ...
}
```

#### ImageCriteria example

The following `ImageCriteria` example configures four
`ImageCriterion`. An AMI is allowed if it matches any one of
these `ImageCriterion`. For information about how the criteria are
evaluated, see [How criteria are
evaluated](#how-allowed-amis-criteria-are-evaluated "#how-allowed-amis-criteria-are-evaluated").

```
{
    "ImageCriteria": [
        // ImageCriterion 1: Allow AWS Marketplace AMIs with product code "abcdefg1234567890"
        {
            "MarketplaceProductCodes": [
                "`abcdefg1234567890`"
            ]
        },
        // ImageCriterion 2: Allow AMIs from providers whose accounts are
        // "123456789012" OR "123456789013" AND AMI age is less than 300 days
        {
            "ImageProviders": [
                "`123456789012`",
                "`123456789013`"
            ],
            "CreationDateCondition": {
                "MaximumDaysSinceCreated": `300`
            }
        },
        // ImageCriterion 3: Allow AMIs from provider whose account is "123456789014"
        // AND with names following the pattern "golden-ami-*"
        {
            "ImageProviders": [
                "`123456789014`"
            ],
            "ImageNames": [
                "`golden-ami-*`"
            ]
        },
        // ImageCriterion 4: Allow AMIs from Amazon or verified providers
        // AND which aren't deprecated
        {
            "ImageProviders": [
                "amazon"
            ],
            "DeprecationTimeCondition": {
                "MaximumDaysSinceDeprecated": `0`
            }
        }
    ]
}
```

### How criteria are

evaluated

The following table explains the evaluation rules that determine if an AMI is allowed,
showing how the `AND` or `OR` operator is applied at each
level:

| Evaluation level                                                                   | Operator | Requirement to be an Allowed AMI                         |
| ---------------------------------------------------------------------------------- | -------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parameter values for `ImageProviders`, `ImageNames`, and `MarketplaceProductCodes` | `OR`     | AMI must match at least one value in each parameter list |
| `ImageCriterion`                                                                   | `AND`    | AMI must match all parameters in each `ImageCriterion`   |
| `ImageCriteria`                                                                    | `OR`     | AMI must match any one of the `ImageCriterion`           | Using the preceding evaluation rules, let's see how to apply them to the [ImageCriteria example](#allowed-amis-json-configuration-example "#allowed-amis-json-configuration-example"): <br>• `ImageCriterion` 1: Allows AMIs that have the AWS Marketplace product code `abcdefg1234567890` `OR` <br>• `ImageCriterion` 2: Allows AMIs that meet both of these criteria: + Owned by either account `123456789012` `OR` `123456789013` <br>• `AND` + Created within the last 300 days `OR` <br>• `ImageCriterion` 3: Allows AMIs that meet both of these criteria: + Owned by account `123456789014` <br>• `AND` + Named with the pattern `golden-ami-*` `OR` <br>• `ImageCriterion` 4: Allows AMIs that meet both of these criteria: + Published by Amazon or verified providers (specified by the `amazon` alias) <br>• `AND` + Not deprecated (maximum days since deprecation is `0`) ### Limits The `ImageCriteria` can include up to: <br>• 10 `ImageCriterion` Each `ImageCriterion` can include up to: <br>• 200 values for `ImageProviders` <br>• 50 values for `ImageNames` <br>• 50 values for `MarketplaceProductCodes` **Example of limits** Using the preceding [ImageCriteria example](#allowed-amis-json-configuration-example "#allowed-amis-json-configuration-example"): <br>• There are 4 `ImageCriterion`. Up to 6 more can be added to the request to reach the limit of 10. <br>• In the first `ImageCriterion`, there is 1 value for `MarketplaceProductCodes`. Up to 49 more can be added to this `ImageCriterion` to reach the limit of 50. <br>• In the second `ImageCriterion`, there are 2 values for `ImageProviders`. Up to 198 more can be added to this `ImageCriterion` to reach the limit of 200. <br>• In the third `ImageCriterion`, there is 1 value for `ImageNames`. Up to 49 more can be added to this `ImageCriterion` to reach the limit of 50. ### Allowed AMIs operations The Allowed AMIs feature has three operational states for managing the image criteria: **enabled**, **disabled**, and **audit mode**. These allow you to enable or disable the image criteria, or review them as needed. ###### Enabled When Allowed AMIs is enabled: <br>• The `ImageCriteria` are applied. <br>• Only allowed AMIs are discoverable in the EC2 console and by APIs that use images (for example, that describe, copy, store, or perform other actions that use images). <br>• Instances can only be launched using allowed AMIs. ###### Disabled When Allowed AMIs is disabled: <br>• The `ImageCriteria` are not applied. <br>• No restrictions are placed on AMI discoverability or usage. ###### Audit mode In audit mode: <br>• The `ImageCriteria` are applied, but no restrictions are placed on AMI discoverability or usage. <br>• In the EC2 console, for each AMI, the **Allowed image** field displays either **Yes** or **No** to indicate whether the AMI will be discoverable and available to users in the account when Allowed AMIs is enabled. <br>• In the command line, the response for the `describe-image` operation includes `"ImageAllowed": true` or `"ImageAllowed": false` to indicate whether the AMI will be discoverable and available to users in the account when Allowed AMIs is enabled. <br>• In the EC2 console, the AMI Catalog displays **Not allowed** next to AMIs that won't be discoverable or available to users in the account when Allowed AMIs is enabled. ## Best practices for implementing Allowed AMIs When implementing Allowed AMIs, consider these best practices to ensure a smooth transition and minimize potential disruptions to your AWS environment. 1. **Enable audit mode** Begin by enabling Allowed AMIs in audit mode. This state allows you to see which AMIs would be affected by your criteria without actually restricting access, providing a risk-free evaluation period. 2. **Set Allowed AMIs criteria** Carefully establish which AMI providers align with your organization's security policies, compliance requirements, and operational needs. ###### Note When using AWS managed services like Amazon ECS or Amazon EKS, we recommend specifying the `amazon` alias to allow AMIs created by AWS. These services depend on Amazon-published AMIs to launch instances. Be cautious when setting `CreationDateCondition` restrictions for any AMIs. Setting overly restrictive date conditions (for example, AMIs must be less than 5 days old) can cause instance launch failures if the AMIs, whether from AWS or other providers, are not updated within your specified time frame. We recommend pairing `ImageNames` with `ImageProviders` for better control and specificity. Using `ImageNames` alone might not uniquely identify an AMI. 3. **Check for impact on expected business processes** You can use the console or the CLI to identify any instances that were launched with AMIs that don't meet the specified criteria. This information can guide your decision to either update your launch configurations to use compliant AMIs (for example, specifying a different AMI in a launch template) or adjust your criteria to allow these AMIs. Console: Use the [ec2-instance-launched-with-allowed-ami](../../../config/latest/developerguide/ec2-instance-launched-with-allowed-ami.md "../../../config/latest/developerguide/ec2-instance-launched-with-allowed-ami.md") AWS Config rule to check if running or stopped instances were launched with AMIs that meet your Allowed AMIs criteria. The rule is **NON_COMPLIANT** if an AMI doesn't meet the Allowed AMIs criteria, and **COMPLIANT** if it does. The rule only operates when the Allowed AMIs setting is set to **enabled** or **audit mode**. CLI: Run the [describe-instance-image-metadata](../../../cli/latest/reference/ec2/describe-instance-image-metadata.md "../../../cli/latest/reference/ec2/describe-instance-image-metadata.md") command and filter the response to identify any instances that were launched with AMIs that don't meet the specified criteria. For the console and CLI instructions, see [Find instances launched from AMIs that aren't allowed](manage-settings-allowed-amis.md#identify-instances-with-allowed-AMIs "manage-settings-allowed-amis.md#identify-instances-with-allowed-AMIs"). 4. **Enable Allowed AMIs** Once you've confirmed that the criteria will not adversely affect expected business processes, enable Allowed AMIs. 5. **Monitor instance launches** Continue to monitor instance launches from AMIs across your applications and the AWS managed services you use, such as Amazon EMR, Amazon ECR, Amazon EKS, and AWS Elastic Beanstalk. Check for any unexpected issues and make necessary adjustments to the Allowed AMIs criteria. 6. **Pilot new AMIs** To test third-party AMIs that do not comply with your current Allowed AMIs settings, AWS recommends the following approaches: <br>• Use a separate AWS account: Create an account with no access to your business-critical resources. Ensure that the Allowed AMIs setting is not enabled in this account, or that the AMIs you want to test are explicitly allowed, so that you can test them. <br>• Test in another AWS Region: Use a Region where the third-party AMIs are available, but where you have not yet enabled the Allowed AMIs settings. These approaches help ensure your business-critical resources remain secure while you test new AMIs. ## Required IAM permissions To use the Allowed AMIs feature, you need the following IAM permissions: <br>• `GetAllowedImagesSettings` <br>• `EnableAllowedImagesSettings` <br>• `DisableAllowedImagesSettings` <br>• `ReplaceImageCriteriaInAllowedImagesSettings` |
