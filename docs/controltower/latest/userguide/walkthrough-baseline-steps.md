

# Examples: Register an AWS Control Tower OU with APIs only
<a name="walkthrough-baseline-steps"></a>

This walkthrough of examples is a companion document. For explanations, caveats, and more information, see [Types of baselines](types-of-baselines.md).

**Prerequisites**

You must have an existing OU that is not registered with AWS Control Tower, and which you would like to register. Or, you must have a registered OU that you would like to re-register for purposes of updating.

**Register an OU**

1. Check whether the `IdentityCenterBaseline` is enabled for the landing zone. If so, get the Identity Center Enabled Baseline identifier.

   ```
   aws controltower list-baselines --query 'baselines[?name==`IdentityCenterBaseline`].[arn]'
   ```

   ```
   aws controltower list-enabled-baselines --query 'enabledBaselines[?baselineIdentifier==`<Identity Center Baseline Arn>`].[arn]'
   ```

1. Get the ARN of the target OU.

   ```
   aws organizations describe-organizational-unit --organizational-unit-id <Organizational Unit ID> --query 'OrganizationalUnit.[Arn]'
   ```

1. Get the ARN of the `AWSControlTowerBaseline` baseline.

   ```
   aws controltower list-baselines --query 'baselines[?name==`AWSControlTowerBaseline`].[arn]'
   ```

1. Create the `AWSControlTowerBaseline` baseline on the target OU.

   *If the Identity Center Baseline is enabled:*

   ```
   aws controltower enable-baseline --baseline-identifier {{<AWSControlTowerBaseline ARN>}} --baseline-version {{<BASELINE VERSION>}} --target-identifier {{<OU ARN>}} --parameters '[{"key":"IdentityCenterEnabledBaselineArn","value":"{{<Identity Center Enabled Baseline ARN>}}"}]'
   ```

   *If the Identity Center Baseline is not enabled, omit the `parameters` flag, as follows:*

   ```
   aws controltower enable-baseline --baseline-identifier {{<AWSControlTowerBaseline ARN>}} --baseline-version {{<BASELINE VERSION>}} --target-identifier {{<OU ARN>}}
   ```

**Re-register an OU**

After you make updates to landing zone settings, or update your landing zone version, you must **Re-register** OUs to give them the latest changes. Follow these steps to re-register an OU programmatically, by resetting the associated `EnabledBaseline` resource and any associated `EnabledControl` resources.

**Important**  
If the OU has optional controls enabled, you must also call the [`ResetEnabledControl`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledControl.html) API for each enabled optional control after resetting the baseline. This step ensures that the optional controls remain consistent with the latest landing zone configuration. If you skip this step, optional controls on the OU may not reflect the latest landing zone changes. If you do not have any optional controls enabled, this step is not required.

1. Get the ARN of the target OU to re-register.

   ```
   aws organizations describe-organizational-unit --organizational-unit-id {{<OU ID>}} --query 'OrganizationalUnit.[Arn]'
   ```

1. Get the ARN of the `EnabledBaseline` resource for the target OU. 

   ```
   aws controltower list-enabled-baselines --query 'enabledBaselines[?targetIdentifier==`{{<OUARN>}}`].[arn]'
   ```

1. Reset the Enabled Baseline.

   ```
   aws controltower reset-enabled-baseline --enabled-baseline-identifier {{<EnabledBaselineArn>}}
   ```

1. If the OU has optional controls enabled, list the enabled controls for the OU and reset each one so they remain consistent with the latest landing zone configuration.

   List the enabled controls on the target OU:

   ```
   aws controltower list-enabled-controls --target-identifier {{<OU ARN>}}
   ```

   For each enabled optional control returned, reset it by calling:

   ```
   aws controltower reset-enabled-control --enabled-control-identifier {{<EnabledControlArn>}}
   ```

   For more information, see [ResetEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledControl.html) in the *AWS Control Tower API Reference*.