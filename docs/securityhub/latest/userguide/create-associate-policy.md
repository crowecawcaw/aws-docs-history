# Creating and associating configuration policies

The delegated AWS Security Hub CSPM administrator account can create configuration policies that specify how Security Hub CSPM, standards, and controls
are configured in specified accounts and organizational units (OUs). A configuration policy takes effect only after the delegated administrator
associates it with at least one account or organizational unit (OUs), or the root. The delegated administrator can also
associate a self-managed configuration with accounts, OUs, or the root.

If this is your first time creating a configuration policy, we recommend first reviewing [How configuration policies work in Security Hub CSPM](configuration-policies-overview.md "configuration-policies-overview.md").

Choose your preferred access method, and follow the steps to create and associate a configuration policy or self-managed configuration. When using the Security Hub CSPM console, you
can associate a configuration with multiple accounts or OUs at the same time. When using the Security Hub CSPM API or AWS CLI, you can associate a configuration with only
one account or OU in each request.

###### Note

If you use central configuration, Security Hub CSPM automatically disables
controls that involve global resources in all Regions except the home Region. Other controls that you choose to enable
though a configuration policy are enabled in all
Regions where they are available. To limit findings for these controls to just one Region, you can update your AWS Config recorder settings and
turn off global resource recording in all Regions except the home Region.

If an enabled control that involves global resources isn't supported in the home Region, Security Hub CSPM tries to
enable the control in one linked Region where the control is supported. With central configuration, you lack coverage for a control
that isn't available in the home Region or any of the linked Regions.

For a list of controls that involve global resources, see [Controls that use global resources](controls-to-disable.md#controls-to-disable-global-resources "controls-to-disable.md#controls-to-disable-global-resources").

Security Hub CSPM console

###### To create and associate configuration policies

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region. 2. In the navigation pane, choose **Configuration**
and the **Policies** tab. Then, choose **Create policy**. 3. On the **Configure organization** page, if this is your first time creating an
configuration policy, you see three options under **Configuration type**. If you've already created
at least one configuration policy, you only see the **Custom policy** option.

    * Choose **Use the AWS recommended Security Hub CSPM configuration across my entire organization**
     to use our recommended policy. The recommended policy enables Security Hub CSPM in all organization accounts, enables the AWS Foundational Security
    Best Practices (FSBP) standard, and enables all new and existing FSBP controls. The controls use default parameter values.
    * Choose **I'm not ready to configure yet** to create a configuration policy later.
    * Choose **Custom policy** to create a custom configuration policy. Specify whether to enable or disable Security Hub CSPM,
     which standards to enable, and which controls to enable across those standards. Optionally, specify [custom parameter values](custom-control-parameters.md "custom-control-parameters.md") for one or more
    enabled controls that support custom parameters.

4. In the **Accounts** section, choose which target accounts, OUs, or the root that
   you want your configuration policy to apply to.
   - Choose **All accounts** if you want to apply the
     configuration policy to the root. This includes all accounts and OUs in the organization
     that don't have another policy applied to them or inherited.
   - Choose **Specific
     accounts** if you want to apply the configuration policy to specific accounts or OUs. Enter the account IDs, or select
     the accounts and OUs from the organization structure. You can apply the policy to a maximum of
     15 targets (accounts, OUs, or root) when you create it. To specify a larger number, edit your policy after creation, and apply it
     to additional targets.
   - Choose **The delegated administrator
     only** to apply the configuration policy to the current delegated administrator account.

5. Choose **Next**.
6. On the **Review and apply** page, review your
   configuration policy details. Then, choose **Create policy and
   apply**. In your home Region and linked Regions, this action overrides the existing configuration settings
   of accounts that are associated with this configuration policy. Accounts may be associated with the configuration policy
   through application, or inheritance from a parent node. Child accounts and OUs of the applied targets
   will automatically inherit this configuration policy unless they are specifically excluded, self-managed, or use a different configuration policy.

Security Hub CSPM API

###### To create and associate configuration policies

1. Invoke the
   [CreateConfigurationPolicy](../../1.0/APIReference/API_CreateConfigurationPolicy.md "../../1.0/APIReference/API_CreateConfigurationPolicy.md") API from the
   Security Hub CSPM delegated administrator account in the home Region.
2. For `Name`, provide a unique name for the configuration policy.
   Optionally, for `Description`, provide a
   description for the configuration policy.
3. For the `ServiceEnabled` field, specify if you want
   Security Hub CSPM to be enabled or disabled in this configuration policy.
4. For the `EnabledStandardIdentifiers` field, specify which
   Security Hub CSPM standards you want to enable in this configuration policy.
5. For the `SecurityControlsConfiguration` object, specify
   which controls you want to enable or disable in this configuration policy.
   Choosing `EnabledSecurityControlIdentifiers` means that
   the specified controls are enabled. Other controls that are part of
   your enabled standards (including newly released controls) are
   disabled. Choosing `DisabledSecurityControlIdentifiers`
   means that the specified controls are disabled. Other controls that
   are part of your enabled standards (including newly released controls)
   are enabled.
6. Optionally, for the `SecurityControlCustomParameters` field, specify
   enabled controls for which you want to customize parameters. Provide `CUSTOM` for the
   `ValueType` field and the custom parameter value for the `Value` field. The value must be
   the correct data type and within valid ranges specified by Security Hub CSPM. Only select controls
   support custom parameter values. For more information, see [Understanding control parameters in Security Hub CSPM](custom-control-parameters.md "custom-control-parameters.md").
7. To apply your configuration policy to accounts or OUs, invoke the
   [StartConfigurationPolicyAssociation](../../1.0/APIReference/API_StartConfigurationPolicyAssociation.md "../../1.0/APIReference/API_StartConfigurationPolicyAssociation.md") API from
   the Security Hub CSPM delegated administrator account in the home Region.
8. For the `ConfigurationPolicyIdentifier` field, provide the Amazon
   Resource Name (ARN) or universally unique identifier (UUID) of the policy. The ARN and UUID are returned by the
   `CreateConfigurationPolicy` API. For a self-managed configuration, the `ConfigurationPolicyIdentifier`
   field is equal to `SELF_MANAGED_SECURITY_HUB`.
9. For the `Target` field, provide the OU, account, or
   the root ID to which you want this configuration policy to apply. You can only provide one target in each API request. Child accounts and OUs of the selected target
   will automatically inherit this configuration policy unless they are self-managed or use a different configuration policy.

**Example API request to create a configuration policy:**

```
{
    "Name": "SampleConfigurationPolicy",
    "Description": "Configuration policy for production accounts",
    "ConfigurationPolicy": {
        "SecurityHub": {
             "ServiceEnabled": true,
             "EnabledStandardIdentifiers": [
                    "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0",
                    "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0"
                ],
            "SecurityControlsConfiguration": {
                "DisabledSecurityControlIdentifiers": [
                    "CloudTrail.2"
                ],
                "SecurityControlCustomParameters": [
                    {
                        "SecurityControlId": "ACM.1",
                        "Parameters": {
                            "daysToExpiration": {
                                "ValueType": "CUSTOM",
                                "Value": {
                                    "Integer": 15
                                }
                            }
                        }
                    }
                ]
            }
        }
    }
}

```

**Example API request to associate a configuration policy:**

```
{
    "ConfigurationPolicyIdentifier": "arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Target": {"OrganizationalUnitId": "ou-examplerootid111-exampleouid111"}
}

```

AWS CLI

###### To create and associate configuration policies

1. Run the [create-configuration-policy](../../../cli/latest/reference/securityhub/create-configuration-policy.md "../../../cli/latest/reference/securityhub/create-configuration-policy.md") command from
   the Security Hub CSPM delegated administrator account in the home Region.
2. For `name`, provide a unique name for the configuration policy.
   Optionally, for `description`, provide a
   description for the configuration policy.
3. For the `ServiceEnabled` field, specify if you want
   Security Hub CSPM to be enabled or disabled in this configuration policy.
4. For the `EnabledStandardIdentifiers` field, specify which
   Security Hub CSPM standards you want to enable in this configuration policy.
5. For the `SecurityControlsConfiguration` field, specify
   which controls you want to enable or disable in this configuration policy.
   Choosing `EnabledSecurityControlIdentifiers` means that
   the specified controls are enabled. Other controls that are part of
   your enabled standards (including newly released controls) are
   disabled. Choosing `DisabledSecurityControlIdentifiers`
   means that the specified controls are disabled. Other controls that
   apply to your enabled standards (including newly released controls)
   are enabled.
6. Optionally, for the `SecurityControlCustomParameters` field, specify
   enabled controls for which you want to customize parameters. Provide `CUSTOM` for the
   `ValueType` field and the custom parameter value for the `Value` field. The value must be
   the correct data type and within valid ranges specified by Security Hub CSPM. Only select controls
   support custom parameter values. For more information, see [Understanding control parameters in Security Hub CSPM](custom-control-parameters.md "custom-control-parameters.md").
7. To apply your configuration policy to accounts or OUs, run the [start-configuration-policy-association](../../../cli/latest/reference/securityhub/start-configuration-policy-association.md "../../../cli/latest/reference/securityhub/start-configuration-policy-association.md") command
   from the Security Hub CSPM delegated administrator account in the home Region.
8. For the `configuration-policy-identifier` field, provide the Amazon
   Resource Name (ARN) or ID of the configuration policy. This ARN and ID are returned by the
   `create-configuration-policy` command.
9. For the `target` field, provide the OU, account, or
   the root ID to which you want this configuration policy to apply. You can only provide one target each time you run the command. Children of the selected target will automatically
   inherit this configuration policy unless they are self-managed or use a different configuration policy.

**Example command to create a configuration policy:**

```
aws securityhub --region us-east-1 create-configuration-policy \
--name "SampleConfigurationPolicy" \
--description "Configuration policy for production accounts" \
--configuration-policy '{"SecurityHub": {"ServiceEnabled": true, "EnabledStandardIdentifiers": ["arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0","arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0"],"SecurityControlsConfiguration":{"DisabledSecurityControlIdentifiers": ["CloudTrail.2"], "SecurityControlCustomParameters": [{"SecurityControlId": "ACM.1", "Parameters": {"daysToExpiration": {"ValueType": "CUSTOM", "Value": {"Integer": 15}}}}]}}}'

```

**Example command to associate a configuration policy:**

```
aws securityhub --region us-east-1 start-configuration-policy-association \
--configuration-policy-identifier "arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" \
--target '{"OrganizationalUnitId": "ou-examplerootid111-exampleouid111"}'

```

The `StartConfigurationPolicyAssociation` API returns a field called `AssociationStatus`. This field
tells you whether a policy association is pending or in a state of success or failure. It can take up to 24 hours for the status to change from
`PENDING` to `SUCCESS` or `FAILURE`. For more information about association status, see
[Reviewing the association status of a configuration policy](view-policy.md#configuration-association-status "view-policy.md#configuration-association-status").
