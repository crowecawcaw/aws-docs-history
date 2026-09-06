

# Update organizations
<a name="ou-updates"></a>

The quickest way to update an organizational unit (OU) or to update multiple accounts within an OU is to perform one of the following actions: 
+ Re-register the OU if `AWSControlTowerBaseline` is enabled.
+ Reset enabled baselines or reset enabled controls if `AWSControlTowerBaseline` is not enabled.

## What happens during re-registration
<a name="effects-of-re-registering"></a>

**When you re-register an OU:**
+ The **AWS Control Tower baseline status** field indicates whether the `AWSControlTowerBaseline` is applied to the account (**Enabled**), whether the baseline has not been applied (**Not enabled**), or whether applying the baseline failed previously (**Failed**).
+ When you re-register the OU, the `AWSControlTowerExecution` role is added to all accounts with status **Not enabled** or **Failed**.
+ AWS Control Tower creates a single sign-on (IAM Identity Center) login for those new enrolled accounts.
+ **Enabled** accounts are re-enrolled into AWS Control Tower.
+ Drift on any preventive controls applied to the OU is fixed, because the SCPs are returned to their default definitions.
+ All accounts are updated to reflect the latest landing zone changes.

For more information, see [About enrolling existing accounts](enroll-account.md).

**Tip**  
When you re-register an OU, or when you're updating your landing zone version and multiple member accounts, you may see a failure message mentioning the **StackSet-AWSControlTowerExecutionRole**. This StackSet in the management account can fail because the **AWSControlTowerExecution** IAM role already exists in all enrolled member accounts. This error message is expected behavior, and it can be disregarded.