# Considerations for controls and

accounts

When working with controls and accounts, consider the following properties:

###### Controls and accounts

- Accounts created through the Account Factory in AWS Control Tower inherit the controls of
  the parent OU, and the associated resources are created.
- Accounts created outside of an AWS Control Tower landing zone do not inherit AWS Control Tower
  controls. These are called _unenrolled_
  accounts.
- Accounts created outside of AWS Control Tower won't inherit controls in AWS Control Tower
  until you enroll them. However, these unenrolled accounts _are_ displayed in AWS Control Tower.

Accounts inherit controls from an OU upon enrollment in that OU.

- An OU can contain enrolled or unenrolled _member
  accounts_.
- Controls do not apply to an unenrolled account unless it becomes a member
  account of a registered AWS Control Tower OU. In that case, preventive controls for the
  OU will apply to the unenrolled account. Detective controls will not
  apply.
- When you enable optional controls, AWS Control Tower creates and manages certain
  additional AWS resources in your accounts. Do not modify or delete resources
  created by AWS Control Tower. Doing so could result in the controls entering an unknown
  state. For more information, see [The AWS Control Tower controls library](controls-reference.md "controls-reference.md").
- When you move an account from one OU to another, the controls from the
  previous OU are not removed. If you enable any new hook-based control on the
  destination OU, the old hook-based control is removed from the account, and the
  new control replaces it. Controls implemented with SCPs and AWS Config rules always
  must be removed manually when an account changes OUs.
