# Checking the status of control parameter changes

When you attempt to customize a control parameter or revert to the default value, you can validate whether the desired changes were effective.
This helps ensure that a control works as you expect and provides the intended
security value. If a parameter update is unsuccessful, Security Hub CSPM retains the current value for the parameter.

To verify that a parameter update was successful, you can review the details of the control on the Security Hub CSPM console. On the
console, choose **Controls** on the navigation pane. Then, choose a control to display its details. The **Parameters** tab shows the status of the parameter change.

Programmatically, if your request to update a parameter is valid, the
value of the `UpdateStatus` field is `UPDATING` in a response to the [BatchGetSecurityControls](../../1.0/APIReference/API_BatchGetSecurityControls.md "../../1.0/APIReference/API_BatchGetSecurityControls.md") operation.
This means that the update was valid, but all findings might
not yet include the updated parameter values. When the value of `UpdateState` changes to
`READY`, Security Hub CSPM uses the updated control parameter values when running security checks of the control. Findings include the updated parameter values.

The `UpdateSecurityControl` operation returns an `InvalidInputException` response
for invalid parameter values. The response provides additional details about the reason for failure. For example, you might have specified a
value that's outside the valid range for a parameter. Or, you might have specified a value that doesn't use the correct data type. Submit your request
again with valid input.

If an internal failure occurs when you try to update a parameter value, Security Hub CSPM automatically retries if you
have AWS Config enabled. For more information, see [Considerations before enabling and configuring AWS Config](securityhub-setup-prereqs.md#securityhub-prereq-config "securityhub-setup-prereqs.md#securityhub-prereq-config").
