# Enabling EKS Protection for a

standalone account

A standalone account owns the decision to enable or disable a protection plan in their
AWS account in a specific Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method of
invitation, this section doesn't apply to you. For
information about managing multiple accounts, see [Enabling EKS Protection in multiple-account
environments](eks-protection-enable-multiple-accounts.md "eks-protection-enable-multiple-accounts.md").

After you enable EKS Protection, GuardDuty will start monitoring EKS audit logs for the Amazon EKS
clusters in your account.

Choose your preferred access method to enable EKS Protection in your standalone account.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. From the **Region** selector in the upper-right
   corner, select a Region where you want to enable EKS Protection.
3. In the navigation pane, choose EKS Protection.
4. The **EKS Protection** page provides the current status of
   EKS Protection for your account. Choose **Enable** to enable
   EKS Protection.
5. Choose **Confirm** to save your selection.

API/CLI

- Run the [updateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md") API operation using the
  regional detector ID of the delegated GuardDuty administrator account and passing the
  `features` object name as `EKS_AUDIT_LOGS` and
  status as `ENABLED`.

Alternatively, you can also enable EKS Protection running the a AWS CLI
command. Run the following command, and replace
`12abc34d567e8fa901bc2d34e56789f0` with
your account's detector ID and `us-east-1` with
the Region where you want to enable EKS Protection.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-detector --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --features [{"Name" : "EKS_AUDIT_LOGS", "Status" : "ENABLED"}]'
```
