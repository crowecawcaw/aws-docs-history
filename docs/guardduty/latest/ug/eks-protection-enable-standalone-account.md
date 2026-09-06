

# Enabling EKS Protection for a standalone account
<a name="eks-protection-enable-standalone-account"></a>

A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method of invitation, this section doesn't apply to you. For information about managing multiple accounts, see [Enabling EKS Protection in multiple-account environments](eks-protection-enable-multiple-accounts.md).

After you enable EKS Protection, GuardDuty will start monitoring EKS audit logs for the Amazon EKS clusters in your account.

Choose your preferred access method to enable EKS Protection in your standalone account.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. From the **Region** selector in the upper-right corner, select a Region where you want to enable EKS Protection.

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**. Under **EKS Audit Logs**, choose **Enable** to enable EKS Protection.

1. Choose **Save all**, then choose **Confirm and save**.

------
#### [ API/CLI ]
+ Run the [updateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html) API operation using the regional detector ID of the delegated GuardDuty administrator account and passing the `features` object name as `EKS_AUDIT_LOGS` and status as `ENABLED`. 

  Alternatively, you can also enable EKS Protection running the a AWS CLI command. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable EKS Protection.

  To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty update-detector --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --features [{"Name" : "EKS_AUDIT_LOGS", "Status" : "ENABLED"}]'
  ```

------