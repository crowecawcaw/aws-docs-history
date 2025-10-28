# Reverting to default control parameter values

A control parameter can have a default value that AWS Security Hub CSPM defines. Occasionally, Security Hub CSPM updates the default
value for a parameter to reflect evolving security best practices. If you haven't specified a custom value for a control parameter,
the control automatically tracks those updates and uses the new default value.

You can revert to using default parameter values for a control. The instructions for reversion depend on whether you use
[central configuration](central-configuration-intro.md "central-configuration-intro.md") in Security Hub CSPM. Central
configuration is a feature that the delegated Security Hub CSPM administrator can use to configure Security Hub CSPM capabilities across AWS Regions, accounts,
and organizational units (OUs).

###### Note

Not all control parameters have a default Security Hub CSPM value. In such cases, when
`ValueType` is set to `DEFAULT`, there isn't a specific default value that Security Hub CSPM uses. Rather,
Security Hub CSPM ignores the parameter in the absence of a custom value.

## Reverting to default control parameters in multiple accounts and Regions

If you use central configuration, you can revert control parameters for multiple, centrally managed accounts and OUs in the home Region and linked Regions.

Choose your preferred method, and follow the steps to revert to default parameter values across multiple accounts and Regions using central configuration.

Security Hub CSPM console

###### To revert to default control parameter values in multiple accounts and Regions (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region. 2. In the navigation pane, choose **Settings** and **Configuration**. 3. Choose the **Policies** tab. 4. Select a policy, and then choose **Edit**. 5. Under **Custom policy**, the **Controls** section shows a
list of controls that you specified custom parameters for. 6. Find the control that has one or more parameter values to revert. Then, choose **Remove** to revert to the default values. 7. In the **Accounts** section, verify the accounts or OUs that you want to apply the policy to. 8. Choose **Next**. 9. Review your changes, and verify that they're correct. When you finish, choose **Save policy and apply**. In your home Region and all linked Regions, this action overrides the existing configuration settings
of accounts and OUs that are associated with this configuration policy. Accounts and OUs can be associated with a configuration policy
through direct application or inheritance from a parent.

Security Hub CSPM API

###### To revert to default control parameter values in multiple accounts and Regions (API)

1. Invoke the [UpdateConfigurationPolicy](../../1.0/APIReference/API_UpdateConfigurationPolicy.md "../../1.0/APIReference/API_UpdateConfigurationPolicy.md") API from the delegated administrator account in the
   home Region.
2. For the `Identifier` field, provide the Amazon Resource Name (ARN) or ID of the policy that you want to update.
3. For the `SecurityControlCustomParameters`
   object, provide the identifier of each control for which you want to revert one or more parameters.
4. In the `Parameters` object, for each parameter that you want to revert, provide `DEFAULT` for the
   `ValueType` field. When `ValueType` is set to `DEFAULT`, you don't need to provide a value for the `Value` field.
   If a value is included in your request, Security Hub CSPM ignores it. If your request
   omits a parameter that the control supports, that parameter retains its current value.

###### Warning

If you omit a control object from the `SecurityControlCustomParameters` field, Security Hub CSPM reverts all custom parameters for the control to their default values. A
completely empty list for `SecurityControlCustomParameters` reverts custom parameters for all controls to their default values.

For example, the following AWS CLI command reverts the `daysToExpiration` control parameter for `ACM.1` to its default value in the specified
configuration policy.
This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securityhub create-configuration-policy \
--region `us-east-1` \
--identifier "`arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`" \
--name `"TestConfigurationPolicy"` \
--description `"Updated configuration policy"` \
--updated-reason `"Revert ACM.1 parameter to default value"`
--configuration-policy '{"SecurityHub": {"ServiceEnabled": `true`, "EnabledStandardIdentifiers": ["`arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0`","`arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0`"],"SecurityControlsConfiguration":{"DisabledSecurityControlIdentifiers": `["CloudTrail.2"]`, "SecurityControlCustomParameters": [{"SecurityControlId": `"ACM.1"`, "Parameters": {"`daysToExpiration`": {"ValueType": `"DEFAULT"`}}}]}}}'`

```

## Reverting to default control parameters in a single

account and Region

If you don't use central configuration or have a self-managed account, you can revert to using default parameter values
for your account in one Region at a time.

Choose your preferred method, and follow the steps to revert to default parameter values for your account in a
single Region. To revert to default parameter values in additional Regions, repeat these steps in each additional Region.

###### Note

If you disable Security Hub CSPM, your custom control parameters are reset. If you enable Security Hub CSPM again in the future, all
controls will use default parameter values to start.

Security Hub CSPM console

###### To revert to default control parameter values in one account and Region (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Controls**. Choose the control that you want to revert to
   default parameter values.
3. On the `Parameters` tab, choose **Customized** next to a control parameter. Then, choose **Remove customization**.
   This parameter now uses the default Security Hub CSPM value and tracks future updates to the default value.
4. Repeat the preceding step for each parameter value that you want to revert.

Security Hub CSPM API

###### To revert to default control parameter values in one account and Region (API)

1. Invoke the [UpdateSecurityControl](../../1.0/APIReference/API_UpdateSecurityControl.md "../../1.0/APIReference/API_UpdateSecurityControl.md") API.
2. For `SecurityControlId`, provide the ARN or ID of the control whose
   parameters you want to revert.
3. In the `Parameters` object, for each parameter that you want to revert, provide `DEFAULT` for the
   `ValueType` field. When `ValueType` is set to `DEFAULT`, you don't need to provide a value for the `Value` field.
   If a value is included in your request, Security Hub CSPM ignores it.
4. Optionally, for `LastUpdateReason`, provide a reason for reverting to default parameter values.

For example, the following AWS CLI command reverts the `daysToExpiration` control parameter for `ACM.1` to its default value.
This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securityhub update-security-control \
--region `us-east-1` \
--security-control-id `ACM.1` \
--parameters '{"daysToExpiration": {"ValueType": `"DEFAULT"`}}' \
--last-update-reason `"New internal requirement"``

```
