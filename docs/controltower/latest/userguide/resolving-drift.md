# Resolving drift

Although detection is automatic, the steps to resolve drift must be done
manually through the console, or with the APIs. (Except in certain cases when auto-enroll is enabled for accounts that are moved.)

For example, you can resolve policy drift for controls
programmatically, by calling the [`ResetEnabledControl`](../APIReference/API_ResetEnabledControl.md "../APIReference/API_ResetEnabledControl.md") API.

To resolve _configuration baseline drift_ for an OU, you can choose **Re-register OU** in the
console. If the drift is caused by a single account, you can choose **Update
account** in the console. To resolve baseline drift with the APIs, you can
call the [`ResetEnabledBaseline`](../APIReference/API_ResetEnabledBaseline.md "../APIReference/API_ResetEnabledBaseline.md") API on the OU.

###### Summary

- Many types of drift can be resolved through the **Landing zone
  settings** page. You can choose the **Reset**
  button in the **Versions** section to resolve these types of
  drift.
- If your OU has fewer than 1000 accounts, you can resolve drift in Account
  Factory provisioned accounts, or SCP drift, by selecting **Re-register
  OU** on the **Organization** page or the
  **OU details** page.
- You may be able to resolve account drift, such as [Moved member account](governance-drift.md#drift-account-moved "governance-drift.md#drift-account-moved"), by
  updating an individual account. For more information, see [Update the account in the
  console](updating-account-factory-accounts.md#update-account-in-console "updating-account-factory-accounts.md#update-account-in-console").
- For controls, many types of drift can be resolved by calling the
  [`ResetEnabledControl` API.](../APIReference/API_ResetEnabledControl.md "../APIReference/API_ResetEnabledControl.md")
- Baseline drift on OUs and accounts can be resolved by calling the
  [`ResetEnabledBaseline`](../APIReference/API_ResetEnabledBaseline.md "../APIReference/API_ResetEnabledBaseline.md") API, or by choosing
  **Re-register OU** or **Update account**
  in the AWS Control Tower console.
- To resolve _inheritance drift_ that occurs when accounts
  are moved between OUs, you can enable the auto-enrollment feature. When
  auto-enrollment is enabled, AWS Control Tower automatically remediates inheritance drift
  by applying the baseline resources and control configurations from the
  destination OU to the moved account. You can enable auto-enrollment on the
  landing zone **Settings** page in the console, or by calling the
  [`UpdateLandingZone`](../APIReference/API_UpdateLandingZone.md "../APIReference/API_UpdateLandingZone.md") API with the
  `RemediationType` parameter set to **Inheritance
  Drift**. For more information, see [Move and enroll accounts with auto-enrollment](account-auto-enrollment.md "account-auto-enrollment.md").

###### When you take action to resolve drift on a landing zone version, two behaviors

are possible.

- If you are on the latest landing zone version, when you choose
  **Reset** and then choose **Confirm**,
  your drifted landing zone resources are reset to the saved AWS Control Tower
  configuration. The landing zone version stays the same.
- If you are not on the latest version, you must choose
  **Update**. The landing zone is upgraded to the latest
  landing zone version. Drift is resolved as part of this process.
