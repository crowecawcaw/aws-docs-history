# Notification settings in Accelerate

Communications between you and AMS occur for many reasons:

- Events created by monitoring alerts
- Patching service notifications, if you have opted-in to the Patch add on
- Service requests and incident reports
- Occasional important AWS announcements (your CSDM contacts you if any action on your part is required)
  All notifications are sent using an email that you provided for patch notifications when you were onboarded. Otherwise, notifications are sent to the default email that you provided to AMS when you were onboarded.
  Because it's difficult to keep individual emails updated, we recommend that you use a group email that can be updated
  on your end. All notifications sent to you are also received by AMS operations and analyzed before making a response.

You can use named lists of contacts for non-resource based notifications, such as alerts based on GuardDuty or AWS Config.
For example, you might have a list named `SecurityContacts` and another named `OperationsContacts`.
AMS sends alarms and notifications to these lists.

See [AWS Config Control Compliance report](acc-report-config-control-compliance.md "acc-report-config-control-compliance.md") for more details.
