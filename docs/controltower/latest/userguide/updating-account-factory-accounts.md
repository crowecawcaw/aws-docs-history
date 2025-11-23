# Update and move accounts with AWS Control Tower

The easiest way to update an enrolled account is through the AWS Control Tower console.
Individual account updates are useful for resolving drift, such as [Moved member account](governance-drift.md#drift-account-moved "governance-drift.md#drift-account-moved"). Account updates
also are required as part of a full landing zone update.

## Update the account in the

console

###### To update an account in the AWS Control Tower console

1. When signed in to AWS Control Tower, navigate to the
   **Organization** page.
2. In the list of OUs and accounts, select the name of the account you wish
   to update. Accounts that are available for updating show a status of
   **Update available**.
3. Next you'll see the **Account details** page for your
   selected account.
4. In the upper right, choose **Update account**.

If you move an account from one organizational unit (OU) to another, remember that the
controls applied by the new OU may be different than the controls in the former OU. Be
sure that the controls in the new OU meet your policy requirements for the
account.

AWS Control Tower accounts are modified differently, depending on whether you have opted-in for
auto-enrollment of accounts, or not. For more information about auto-enrollment, see
[Optionally configure auto-enrollment for
accounts](configure-auto-enroll.md "configure-auto-enroll.md").

**Control behavior when accounts are moved between  OUs, with
auto-enroll enabled**

When you move an account into a new OU, AWS Control Tower applies the OU's enabled
baselines and controls to the account. Controls and baselines from the previous OU
are removed. If you move an account outside an OU that's registered, AWS Control Tower
removes all deployed baselines and controls.

**Control behavior when accounts are moved between  OUs,
without auto-enroll**

When you move an account between OUs, the controls for the destination OU are
applied to the  account. However, the controls that applied to the account from the
former OU are not  removed. The exact behavior of the controls is specific to the
implementation of the  controls that are active on the former OU and the destination
OU.

- _For controls implemented with AWS Config rules:_
  The controls from the previous OU  are not removed. These controls must be
  removed manually.
- _For controls implemented with SCPs:_ The
  SCP-based controls from the previous OU are  removed. The SCP-based controls
  for the destination OU go into effect on this account.
- _For controls implemented with CloudFormation
  hooks:_ This behavior  depends on the status of controls in
  the new OU.
  - _If the destination OU has no hook-based
    controls active:_ The old  controls remain active for
    the moved account, unless you remove them  manually.
  - _If the destination OU has hook controls
    active:_ The old controls are  removed and the
    controls in the destination OU are applied to the  account.
