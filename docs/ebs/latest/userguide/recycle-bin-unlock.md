# Unlock a Recycle Bin retention rule to allow

it to be updated or deleted

You can't modify or delete a locked retention rule. If you need to modify a
locked retention rule, you must first unlock it. After you have unlocked the
retention rule, you must wait for the unlock delay period to expire before you
can modify or delete it. You can't modify or delete a retention rule during
the unlock delay period.

An unlocked retention rule can be modified and deleted at any time by a user
who has the required IAM permissions. Leaving your retention rules unlocked
could expose them to accidental or malicious modifications and deletions.

**Considerations**

- You can re-lock a retention rule during the unlock delay period.
- You can re-lock a retention rule after the unlock delay period has expired.
- You can't bypass the unlock delay period.
- You can't change the unlock delay period after the initial lock.
  We recommend that you use Amazon EventBridge rules to notify you of retention rule lock state changes.
  For more information, see [Monitor Recycle Bin using Amazon EventBridge](rbin-eventbridge.md "rbin-eventbridge.md").

You can unlock a locked Region-level retention rule using one of the following methods.

Recycle Bin console

###### To unlock a retention rule

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation panel, choose **Retention rules**.
3. In the grid, select the locked retention rule to unlock, and choose
   **Actions**, **Edit retention rule lock**.
4. On the Edit retention rule lock screen, choose **Unlock**, and then
   choose **Save**.

AWS CLI

###### To unlock a locked retention rule

Use the [unlock-rule](../../../cli/latest/reference/rbin/unlock-rule.md "../../../cli/latest/reference/rbin/unlock-rule.md")
AWS CLI command. For `--identifier`, specify the ID of the retention rule to unlock.

```
aws rbin unlock-rule \
--identifier `rule_ID`
```

###### Example

The following example command unlocks retention rule `6lsJ2Fa9nh9`

```
aws rbin unlock-rule \
--identifier 6lsJ2Fa9nh9
```
