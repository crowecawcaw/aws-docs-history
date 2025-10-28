# Lock a Recycle Bin retention rule to prevent

it from being updated or deleted

Recycle Bin lets you lock Region-level retention rules at any time.

A locked retention rule can't be modified or deleted, even by users who have the
required IAM permissions. Lock your retention rules to help protect them against
accidental or malicious modifications and deletions.

When you lock a retention rule, you must specify an unlock delay period. This is
the period of time that you must wait after unlocking the retention rule before you
can modify or delete it. You cannot modify or delete the retention rule during the
unlock delay period. You can modify or delete the retention rule only after the
unlock delay period has expired.

You can't change the unlock delay period after the retention rule has been locked.
If your account permissions have been compromised, the unlock delay period gives you
additional time to detect and respond to security threats. The length of this period
should be longer than the time it takes for you to identify and respond to security
breaches. To set the right duration, you can review previous security incidents and
the time needed to identify and remediate an account breach.

We recommend that you use Amazon EventBridge rules to notify you of retention rule lock
state changes. For more information, see [Monitor Recycle Bin using Amazon EventBridge](rbin-eventbridge.md "rbin-eventbridge.md").

**Considerations**

- You can't lock tag-level retention rules, or Region-level retention rules
  that have exclusion tags.
- You can lock an unlocked retention rule at any time.
- The unlock delay period must be 7 to 30 days.
- You can re-lock a retention rule during the unlock delay period. Relocking
  the retention rule resets the unlock delay period.
  You can lock a Region-level retention rule using one of the following methods.

Recycle Bin console

###### To lock a retention rule

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation panel, choose **Retention
   rules**.
3. In the grid, select the unlocked retention rule to lock, and
   choose **Actions**, **Edit retention
   rule lock**.
4. In the Edit retention rule lock screen, choose
   **Lock**, and then for **Unlock
   delay period**, specify the unlock delay period in
   days.
5. Select the **I acknowledge that locking the retention
   rule will prevent it from being modified or
   deleted** check box, and then choose
   **Save**.

AWS CLI

###### To lock an unlocked retention rule

Use the [lock-rule](../../../cli/latest/reference/rbin/lock-rule.md "../../../cli/latest/reference/rbin/lock-rule.md")
AWS CLI command. For `--identifier`, specify the ID of the
retention rule to lock. For `--lock-configuration`,
specify the unlock delay period in days.

```
aws rbin lock-rule \
--identifier `rule_ID` \
--lock-configuration 'UnlockDelay={UnlockDelayUnit=DAYS,UnlockDelayValue=`number_of_days`}'
```

###### Example

The following example command locks retention rule
`6lsJ2Fa9nh9` and sets the unlock delay period to 15
days.

```
aws rbin lock-rule \
--identifier 6lsJ2Fa9nh9 \
--lock-configuration 'UnlockDelay={UnlockDelayUnit=DAYS,UnlockDelayValue=15}'
```
