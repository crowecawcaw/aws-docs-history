# Customizing control parameter values

The instructions for customizing control parameters vary based on whether you use [central configuration](central-configuration-intro.md "central-configuration-intro.md") in AWS Security Hub CSPM. Central
configuration is a feature that the delegated Security Hub CSPM administrator can use to configure Security Hub CSPM capabilities across AWS Regions, accounts,
and organizational units (OUs).

If your organization uses central configuration, the delegated administrator can create configuration policies that include custom
control parameters. These policies can be associated with centrally managed member accounts and OUs, and they take effect
in your home Region and all linked Regions. The delegated administrator can also designate one or more accounts
as self-managed, which allows the account owner to configure its own parameters separately in each Region. If your organization
doesn't use central configuration, you must customize control parameters separately in each account and Region.

We recommend using central configuration because it allows you to align control parameter values across different
parts of your organization. For example, all of your test accounts might use certain parameter values, and all production
accounts might use different values.

## Customizing control parameters in multiple accounts and Regions

If you're the delegated Security Hub CSPM administrator for an organization that uses central configuration, choose your
preferred method, and follow the steps to customize control parameters across multiple accounts and Regions.

Security Hub CSPM console

###### To customize control parameter values in multiple accounts and Regions (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Ensure that you're signed in to the home Region. 2. In the navigation pane, choose **Settings** and **Configuration**. 3. Choose the **Policies** tab. 4. To create a new configuration policy that includes custom parameters, choose **Create policy**.
To specify custom parameters in an existing configuration policy, select the policy, and then choose **Edit**.

**To create a new configuration policy with custom control parameter values**

    1. In the **Custom policy** section, choose the security standards and
    controls that you want to enable.
    2. Select **Customize control parameters**.
    3. Select a control, and then specify custom values for one or more parameters.
    4. To customize parameters for more controls, choose **Customize additional control**.
    5. In the **Accounts** section, select the accounts or OUs that you want to apply the policy to.
    6. Choose **Next**.
    7. Choose **Create policy and apply**. In your home Region and all linked Regions, this action overrides the existing configuration settings
     of accounts and OUs that are associated with this configuration policy. Accounts and OUs can be associated with a configuration policy
     through direct application or inheritance from a parent.

**To customize control parameter values in an existing configuration policy**

    1. In the **Controls** section, under **Custom policy**, specify
    the new custom parameter values that you want.
    2. If this is your first time customizing control parameters in this policy, select
     **Customize control parameters**, and then select a control to customize. To
     customize parameters for more controls, choose **Customize additional control**.
    3. In the **Accounts** section, verify the accounts or OUs that you want to apply the policy to.
    4. Choose **Next**.
    5. Review your changes, and verify that they're correct. When you finish, choose **Save policy and apply**. In your home Region and all linked Regions, this action overrides the existing configuration settings
     of accounts and OUs that are associated with this configuration policy. Accounts and OUs can be associated with a configuration policy
     through direct application or inheritance from a parent.

Security Hub CSPM API
**To customize control parameter values in multiple accounts and Regions (API)**

###### To create a new configuration policy with custom control parameter values

1. Invoke the [CreateConfigurationPolicy](../../1.0/APIReference/API_CreateConfigurationPolicy.md "../../1.0/APIReference/API_CreateConfigurationPolicy.md") API from the delegated administrator account in the home Region.
2. For the `SecurityControlCustomParameters`
   object, provide the identifier of each control that you want to customize.
3. For the `Parameters` object, provide the name of each parameter that you
   want to customize. For each parameter that you customize, provide `CUSTOM` for `ValueType`.
   For `Value`, provide the data type of the parameter and the custom value. The `Value` field
   can't be empty when `ValueType` is `CUSTOM`. If your request
   omits a parameter that the control supports, that parameter retains its current value. You can find
   supported parameters, data types, and valid values for a control by invoking the
   [GetSecurityControlDefinition](../../1.0/APIReference/API_GetSecurityControlDefinition.md "../../1.0/APIReference/API_GetSecurityControlDefinition.md") API.

###### To customize control parameter values in an existing configuration policy

1. Invoke the [UpdateConfigurationPolicy](../../1.0/APIReference/API_UpdateConfigurationPolicy.md "../../1.0/APIReference/API_UpdateConfigurationPolicy.md") API from the delegated administrator account in the home Region.
2. For the `Identifier` field, provide the Amazon Resource Name (ARN) or ID of the configuration policy that you want to update.
3. For the `SecurityControlCustomParameters`
   object, provide the identifier of each control that you want to customize.
4. For the `Parameters` object, provide the name of each parameter that you
   want to customize. For each parameter that you customize, provide `CUSTOM` for `ValueType`.
   For `Value`, provide the data type of the parameter and the custom value. If your request
   omits a parameter that the control supports, that parameter retains its current value. You can find
   supported parameters, data types, and valid values for a control by invoking the
   [GetSecurityControlDefinition](../../1.0/APIReference/API_GetSecurityControlDefinition.md "../../1.0/APIReference/API_GetSecurityControlDefinition.md") API.

For example, the following AWS CLI command creates a new configuration policy with a custom value for the `daysToExpiration` parameter of `ACM.1`.
This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securityhub create-configuration-policy \
--region `us-east-1` \
--name `"SampleConfigurationPolicy"` \
--description `"Configuration policy for production accounts"` \
--configuration-policy '{"SecurityHub": {"ServiceEnabled": `true`, "EnabledStandardIdentifiers": [`"arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0","arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0"`],"SecurityControlsConfiguration":{"DisabledSecurityControlIdentifiers": [`"CloudTrail.2"`], "SecurityControlCustomParameters": [{"SecurityControlId": `"ACM.1"`, "Parameters": {"daysToExpiration": {"ValueType": `"CUSTOM"`, "Value": "Integer": `15`}}}]}}}'`

```

## Customizing control parameters in a single account and Region

If you don't use central configuration or have a self-managed account,
you can customize control parameters for your account in one
Region at a time only.

Choose your preferred method, and follow the steps to customize control parameters. Your changes apply only to your
account in the current Region. To customize the control parameters in additional Regions, repeat the following steps in
each additional account and Region in which you want to customize parameters. The same control can use different parameter values
in different Regions.

Security Hub CSPM console

###### To customize control parameter values in one account and Region (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Controls**. In the table, choose a control that supports custom
   parameters and you want to change the parameters for. The **Custom parameters** column indicates which controls support custom parameters.
3. On the details page for the control, choose the **Parameters** tab, and then choose
   **Edit**.
4. Specify the parameter values that you want.
5. Optionally, in the **Reason for change** section, select a reason for customizing
   the parameters.
6. Choose **Save**.

Security Hub CSPM API

###### To customize control parameter values in one account and Region (API)

1. Invoke the [UpdateSecurityControl](../../1.0/APIReference/API_UpdateSecurityControl.md "../../1.0/APIReference/API_UpdateSecurityControl.md") API.
2. For `SecurityControlId`, provide the ID of the control that
   you want to customize.
3. For the `Parameters` object, provide the name of each parameter that you want to
   customize. For each parameter that you customize, provide
   `CUSTOM` for `ValueType`. For
   `Value`, provide the data type of the parameter and
   the custom value. If your request omits a parameter that the control
   supports, that parameter retains its current value. You can find
   supported parameters, data types, and valid values for a control by
   invoking the [GetSecurityControlDefinition](../../1.0/APIReference/API_GetSecurityControlDefinition.md "../../1.0/APIReference/API_GetSecurityControlDefinition.md")
   API.
4. Optionally, for `LastUpdateReason`, provide a reason for customizing the control parameters.

For example, the following AWS CLI command defines a custom value for the `daysToExpiration` parameter of `ACM.1`.
This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securityhub update-security-control \
--region `us-east-1` \
--security-control-id `ACM.1` \
--parameters '{"daysToExpiration": {"ValueType": `"CUSTOM"`, "Value": {`"Integer": 15`}}}' \
--last-update-reason `"Internal compliance requirement"``

```
