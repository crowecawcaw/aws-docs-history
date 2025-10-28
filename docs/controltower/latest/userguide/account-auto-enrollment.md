# Move and enroll accounts with auto-enrollment

The account auto-enrollment feature is available for landing zones of version 3.1 and above.

If you optionally enable this feature, you can utilize the AWS Organizations APIs and console to
move accounts into AWS Control Tower, without creating [_inheritance drift_](governance-drift.md "governance-drift.md"). The
account automatically receives baseline resources and control configurations from the destination
organizational unit (OU) in AWS Control Tower. This optional capability also allows you to move
accounts between OUs within AWS Control Tower, without creating inheritance drift, if the two OUs
have the same baseline configuration and the same controls enabled.

**To activate auto-enrollment:** You can select
auto-enrollment of accounts on the landing zone **Settings** page in
the AWS Control Tower console, or by calling the AWS Control Tower `CreateLandingZone` or
`UpdateLandingZone` APIs, with the value of the
`RemediationType` parameter set to **Inheritance
Drift**.

**To apply auto-enrollment:** After selecting this option
in your **Settings** page, you can move an account by means of the
AWS Organizations console, the AWS Organizations `MoveAccount` API, or the AWS Control Tower
console.

**To unenroll an account with auto-enrollment:** If you
move an account outside an OU that's registered, AWS Control Tower removes all deployed baseline resources
and controls automatically.

###### Note

If the source and
destination OUs in AWS Control Tower have different configurations, the account may show [Moved member account](governance-drift.md#drift-account-moved "governance-drift.md#drift-account-moved") drift.

## Prerequisites: Configure for auto-enrollment

- You must be running AWS Control Tower landing zone version 3.1 or later.
- Opt into the AWS Control Tower auto-enrollment capability through the landing zone
  **Settings** page in the console, or through the AWS Control Tower
  landing zone APIs, by setting the value of the `RemediationTypes`
  parameter to `Inheritance Drift`. When you have opted in, AWS Control Tower
  reacts to `move account` events for AWS Organizations, and it remediates
  inheritance drift for the moved accounts immediately, on your behalf.

## Required permissions

Specific roles and permissions are required for you to use the AWS Organizations
`CreateAccount` API and `MoveAccount` API. For more
information about using AWS Organizations with AWS Control Tower, see [AWS Control Tower and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-CTower.md "../../../organizations/latest/userguide/services-that-can-integrate-CTower.md").

## API usage examples

For more information and examples regarding these APIs, see [`CreateAccount`](../../../organizations/latest/APIReference/API_CreateAccount.md "../../../organizations/latest/APIReference/API_CreateAccount.md") and [`MoveAccount`](../../../organizations/latest/APIReference/API_MoveAccount.md "../../../organizations/latest/APIReference/API_MoveAccount.md") in the _AWS Organizations API
Reference_.

## Considerations

- **Enrollment timeline:** An account moved to an
  OU that's registered with AWS Control Tower is enrolled with an _eventual
  consistency_ model. This process typically takes a few minutes, up
  to several hours, depending on the number of accounts being moved.
- **Unenrollment process:** You can use the same
  process to unenroll your accounts from AWS Control Tower by moving them to an OU outside
  AWS Control Tower. This process removes any roles and resources deployed by AWS Control Tower and
  any controls enabled in AWS Control Tower.
