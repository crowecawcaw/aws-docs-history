

# Resolving drift
<a name="resolving-drift"></a>

Although detection is automatic, the steps to resolve drift must be done manually through the console, or with the APIs. (Except in certain cases when auto-enroll is enabled for accounts that are moved.)

For example, you can resolve policy drift for controls programmatically, by calling the [`ResetEnabledControl`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledControl.html) API.

To resolve *configuration baseline drift* for an OU, you can choose **Re-register OU** in the console. If the drift is caused by a single account, you can choose **Update account** in the console. To resolve baseline drift with the APIs, you can call the [`ResetEnabledBaseline`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledBaseline.html) API on the OU.

**Summary**
+ Many types of drift can be resolved through the **Landing zone settings** page. You can choose the **Reset** button in the **Versions** section to resolve these types of drift.
+ If your OU has fewer than 1000 accounts, you can resolve drift in Account Factory provisioned accounts, or SCP drift, by selecting **Re-register OU** on the **Organization** page or the **OU details** page.
+ You may be able to resolve account drift, such as [Moved member account](governance-drift.md#drift-account-moved), by updating an individual account. For more information, see [Update the account in the console](updating-account-factory-accounts.md#update-account-in-console).
+ For controls, many types of drift can be resolved by calling the [`ResetEnabledControl` API.](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledControl.html)
+ Baseline drift on OUs and accounts can be resolved by calling the [`ResetEnabledBaseline`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledBaseline.html) API, or by choosing **Re-register OU** or **Update account** in the AWS Control Tower console.
+ To resolve *inheritance drift* that occurs when accounts are moved between OUs, you can enable the auto-enrollment feature. When auto-enrollment is enabled, AWS Control Tower automatically remediates inheritance drift by applying the baseline resources and control configurations from the destination OU to the moved account. You can enable auto-enrollment on the landing zone **Settings** page in the console, or by calling the [`UpdateLandingZone`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateLandingZone.html) API with the `RemediationType` parameter set to **Inheritance Drift**. For more information, see [Move and enroll accounts with auto-enrollment](account-auto-enrollment.md).

**When you take action to resolve drift on a landing zone version, the behavior depends on your current version.**  
If you are on landing zone version 3.1 or above, you can choose **Update** to change your landing zone configuration without upgrading versions, or choose **Reset** to reapply your saved configurations to your drifted landing zone resources. Drift is resolved as part of the update process.
If you are on a landing zone version earlier than 3.1, you cannot choose **Reset**. You must choose **Update** and upgrade your landing zone to at least version 3.1.