# Disabling controls in Security Hub CSPM

To reduce finding noise, it can be helpful to disable controls that aren't relevant to
your environment. In AWS Security Hub CSPM, you can disable a control across all security standards or
for only specific standards.

If you disable a control across all standards, the following occurs:

- Security checks for the control are no longer performed.
- No additional findings are generated for the control.
- Existing findings are no longer updated for the control.
- Existing findings for the control are archived automatically, typically within
  3–5 days on a best-effort basis.
- Security Hub CSPM removes any related AWS Config rules that it created for the control.
  If you disable a control for only specific standards, Security Hub CSPM stops running security checks
  for the control for only those standards. This also removes the control from [calculations of the security score](standards-security-score.md "standards-security-score.md") for each of
  those standards. If the control is enabled in other standards, Security Hub CSPM retains the associated
  AWS Config rule, if applicable, and continues running security checks for the control for the
  other standards. Security Hub CSPM also includes the control when it calculates the security score for
  each of the other standards, which affects your summary security score.

If you disable a standard, all of the controls that apply to the standard are disabled
automatically for that standard. However, the controls might continue to be enabled in other
standards. When you disable a standard, Security Hub CSPM doesn't track which controls were disabled for
the standard. Consequently, if you later re-enable the same standard, all the controls that
apply to it are automatically enabled. For information about disabling a standard, see [Disabling a standard](disable-standards.md "disable-standards.md").

Disabling a control isn't a permanent action. Suppose you disable a control, and then
enable a standard that includes the control. The control is then enabled for that standard.
When you enable a standard in Security Hub CSPM, all the controls that apply to the standard are
automatically enabled. For information about enabling a standard, see [Enabling a standard](enable-standards.md "enable-standards.md").

###### Topics

- [Disabling a control across
  standards](disable-controls-across-standards.md "disable-controls-across-standards.md")
- [Disabling a control in a specific
  standard](disable-controls-standard.md "disable-controls-standard.md")
- [Suggested controls to disable](controls-to-disable.md "controls-to-disable.md")
