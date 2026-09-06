

# Updating configuration policies
<a name="update-policy"></a>

After creating a configuration policy, the delegated AWS Security Hub CSPM administrator account can update the policy details and policy associations. When policy details are updated, accounts that are associated with the configuration policy automatically start using the updated policy.

For background information about the benefits of central configuration and how it works, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md).

**Note**  
Configuration policies support AWS standards and controls only. You cannot include multicloud standards (such as CIS Azure Foundations Benchmark v4.0.0) or Azure controls in a configuration policy. Including a multicloud standard ARN or control ID returns `InvalidInputException`. To enable or configure multicloud standards, use local configuration mechanisms directly in the desired AWS account.

The delegated administrator can update the following policy settings:
+ Enable or disable Security Hub CSPM.
+ Enable one or more [security standards](standards-reference.md).
+ Indicate which [security controls](securityhub-controls-reference.md) are enabled across enabled standards. You can do this by providing a list of specific controls that should be enabled, and Security Hub CSPM disables all other controls, including new controls when they are released. Alternatively, you can provide a list of specific controls that should be disabled, and Security Hub CSPM enables all other controls, including new controls when they are released.
+ Optionally, [customize parameters](https://docs.aws.amazon.com/securityhub/latest/userguide/custom-control-parameters.html) for select enabled controls across enabled standards.

Choose your preferred method, and follow the steps to update a configuration policy.

**Note**  
If you use central configuration, Security Hub CSPM automatically disables controls that involve global resources in all Regions except the home Region. Other controls that you choose to enable though a configuration policy are enabled in all Regions where they are available. To limit findings for these controls to just one Region, you can update your AWS Config recorder settings and turn off global resource recording in all Regions except the home Region.  
If an enabled control that involves global resources isn't supported in the home Region, Security Hub CSPM tries to enable the control in one linked Region where the control is supported. With central configuration, you lack coverage for a control that isn't available in the home Region or any of the linked Regions.  
For a list of controls that involve global resources, see [Controls that use global resources](controls-to-disable.md#controls-to-disable-global-resources).

------
#### [ Console ]

**To update configuration policies**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

   Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region.

1. In the navigation pane, choose **Settings** and **Configuration**.

1. Choose the **Policies** tab.

1. Select the configuration policy that you want to edit, and choose **Edit**. If desired, edit the policy settings. Leave this section as is if you want to keep the policy settings unchanged.

1. Choose **Next**.If desired, edit the policy associations. Leave this section as is if you want to keep the policy associations unchanged. You can associate or disassociate the policy with a maximum of 15 targets (accounts, OUs, or root) when you update it. 

1. Choose **Next**.

1. Review your changes, and choose **Save and apply**. In your home Region and linked Regions, this action overrides the existing configuration settings of accounts that are associated with this configuration policy. Accounts may be associated with a configuration policy through application, or inheritance from a parent node.

------
#### [ API ]

**To update configuration policies**

1. To update the settings in a configuration policy, invoke the [UpdateConfigurationPolicy](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateConfigurationPolicy.html) API from the Security Hub CSPM delegated administrator account in the home Region.

1. Provide the Amazon Resource Name (ARN) or ID of the configuration policy that you want to update. 

1. Provide updated values for the fields under `ConfigurationPolicy`. Optionally, you can also provide a reason for the update.

1. To add new associations for this configuration policy, invoke the [StartConfigurationPolicyAssociation](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StartConfigurationPolicyAssociation.html) API from the Security Hub CSPM delegated administrator account in the home Region. To remove one or more current associations, invoke the [StartConfigurationPolicyDisassociation](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StartConfigurationPolicyDisassociation.html) API from the Security Hub CSPM delegated administrator account in the home Region.

1. For the `ConfigurationPolicyIdentifier` field, provide the ARN or ID of the configuration policy whose associations you want to update.

1. For the `Target` field, provide the accounts, OUs, or root ID that you want to associate or disassociate. This action overrides previous policy associations for the specified OUs or accounts.

**Note**  
When you invoke the `UpdateConfigurationPolicy` API, Security Hub CSPM performs a full list replacement for the `EnabledStandardIdentifiers`, `EnabledSecurityControlIdentifiers`, `DisabledSecurityControlIdentifiers`, and `SecurityControlCustomParameters` fields. Each time you invoke this API, provide the full list of standards that you want to enable and the full list of controls that you want to enable or disable and customize parameters for.

**Example API request to update a configuration policy:**

```
{
    "Identifier": "arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Description": "Updated configuration policy",
    "UpdatedReason": "Disabling CloudWatch.1",
    "ConfigurationPolicy": {
        "SecurityHub": {
             "ServiceEnabled": true,
             "EnabledStandardIdentifiers": [
                    "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0",
                    "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0" 
                ],
            "SecurityControlsConfiguration": {
                "DisabledSecurityControlIdentifiers": [
                    "CloudTrail.2",
                    "CloudWatch.1"
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

------
#### [ AWS CLI ]

**To update configuration policies**

1. To update the settings in a configuration policy, run the [update-configuration-policy](https://docs.aws.amazon.com/cli/latest/reference/securityhub/update-configuration-policy.html) command from the Security Hub CSPM delegated administrator account in the home Region.

1.  Provide the Amazon Resource Name (ARN) or ID of the configuration policy that you want to update.

1. Provide updated values for the fields under `configuration-policy`. Optionally, you can also provide a reason for the update.

1. To add new associations for this configuration policy, run the [start-configuration-policy-association](https://docs.aws.amazon.com/cli/latest/reference/securityhub/start-configuration-policy-association.html) command from the Security Hub CSPM delegated administrator account in the home Region. To remove one or more current associations, run the [start-configuration-policy-disassociation](https://docs.aws.amazon.com/cli/latest/reference/securityhub/start-configuration-policy-association.html) command from the Security Hub CSPM delegated administrator account in the home Region.

1. For the `configuration-policy-identifier` field, provide the ARN or ID of the configuration policy whose associations you want to update.

1. For the `target` field, provide the accounts, OUs, or root ID that you want to associate or disassociate. This action overrides previous policy associations for the specified OUs or accounts.

**Note**  
When you run the `update-configuration-policy` command, Security Hub CSPM performs a full list replacement for the `EnabledStandardIdentifiers`, `EnabledSecurityControlIdentifiers`, `DisabledSecurityControlIdentifiers`, and `SecurityControlCustomParameters` fields. Each time you run this command, provide the full list of standards that you want to enable and the full list of controls that you want to enable or disable and customize parameters for.

**Example command to update a configuration policy:**

```
aws securityhub update-configuration-policy \
--region {{us-east-1}} \
--identifier "{{arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}" \
--description "{{Updated configuration policy}}" \
--updated-reason "{{Disabling CloudWatch.1}}" \
--configuration-policy '{"SecurityHub": {"ServiceEnabled": {{true}}, "EnabledStandardIdentifiers": ["{{arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0}}","{{arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0}}"],"SecurityControlsConfiguration":{"DisabledSecurityControlIdentifiers": ["{{CloudTrail.2}}","{{CloudWatch.1}}"], "SecurityControlCustomParameters": [{"SecurityControlId": "{{ACM.1}}", "Parameters": {"{{daysToExpiration}}": {"ValueType": "{{CUSTOM}}", "Value": {"{{Integer}}": {{15}}}}}}]}}}'
```

------

The `StartConfigurationPolicyAssociation` API returns a field called `AssociationStatus`. This field tells you whether a policy association is pending or in a state of success or failure. It can take up to 24 hours for the status to change from `PENDING` to `SUCCESS` or `FAILURE`. For more information about association status, see [Reviewing the association status of a configuration policy](view-policy.md#configuration-association-status).