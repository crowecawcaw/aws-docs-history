# Examples: Register an AWS Control Tower OU with APIs

only

This walkthrough of examples is a companion document. For explanations, caveats, and more
information, see [Types of baselines](types-of-baselines.md "types-of-baselines.md").

**Prerequisites**

You must have an existing OU that is not registered with AWS Control Tower, and which you would
like to register. Or, you must have a registered OU that you would like to re-register for
purposes of updating.

**Register an OU**

1. Check whether the `IdentityCenterBaseline` is enabled for the landing zone.
   If so, get the Identity Center Enabled Baseline identifier.

```
aws controltower list-baselines --query 'baselines[?name==`IdentityCenterBaseline`].[arn]'
```

```
aws controltower list-enabled-baselines --query 'enabledBaselines[?baselineIdentifier==`<Identity Center Baseline Arn>`].[arn]'
```

2. Get the ARN of the target OU.

```
aws organizations describe-organizational-unit --organizational-unit-id <Organizational Unit ID> --query 'OrganizationalUnit.[Arn]'
```

3. Get the ARN of the `AWSControlTowerBaseline` baseline.

```
aws controltower list-baselines --query 'baselines[?name==`AWSControlTowerBaseline`].[arn]'
```

4. Create the `AWSControlTowerBaseline` baseline on the target OU.

_If the Identity Center Baseline is enabled:_

```
aws controltower enable-baseline --baseline-identifier `<AWSControlTowerBaseline ARN>` --baseline-version `<BASELINE VERSION>` --target-identifier `<OU ARN>` --parameters '[{"key":"IdentityCenterEnabledBaselineArn","value":"`<Identity Center Enabled Baseline ARN>`"}]'
```

_If the Identity Center Baseline is not enabled, omit the
`parameters` flag, as follows:_

```

aws controltower enable-baseline --baseline-identifier `<AWSControlTowerBaseline ARN>` --baseline-version `<BASELINE VERSION>` --target-identifier `<OU ARN>`
```

**Re-register an OU**

After you make updates to landing zone settings, or update your landing zone version, you must
**Re-register** OUs to give them the latest changes. Follow these steps
to re-register an OU programmatically, by resetting the associated
`EnabledBaseline` resource.

1. Get the ARN of the target OU to re-register.

```
aws organizations describe-organizational-unit --organizational-unit-id `<OU ID>` --query 'OrganizationalUnit.[Arn]'
```

2. Get the ARN of the `EnabledBaseline` resource for the target OU.

```
aws controltower list-enabled-baselines --query 'enabledBaselines[?targetIdentifier==``<OUARN>``].[arn]'
```

3. Reset the Enabled Baseline.

```
aws controltower reset-enabled-baseline --enabled-baseline-identifier `<EnabledBaselineArn>`
```
