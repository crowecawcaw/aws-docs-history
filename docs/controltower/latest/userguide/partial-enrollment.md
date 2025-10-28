# Partial enrollment of accounts

When you're working with baselines, an account can be placed into a state called
**Partially enrolled**.

This state can occur if you re-register an OU by calling the
`ResetEnabledBaseline` API, because AWS Control Tower applies only the mandatory
resources to the accounts in the target OU. An account that is missing the optional
resources (controls) for its parent OU is marked as **Partially
enrolled**.

If you move an unenrolled account into a registered OU and then call the
`ResetEnabledBaseline` API on the OU to enroll that account, AWS Control Tower
applies the resources associated with the `AWSControlTowerBaseline` to the
newly-enrolled account. However, optional controls enabled for this OU are not applied
to the account. The account remains in a **Partially enrolled**
state.

To enroll the account fully, choose **Re-register** or
**Update account** in the console. When you select these operations
from the console, AWS Control Tower applies all of the resources of that OU to the newly-enrolled
account, including the optional controls that are activated for that OU.
